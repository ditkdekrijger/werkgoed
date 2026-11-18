/* Werkgoed site runtime: rendert de canvaspagina's (x-dc sjablonen) als losse, klikbare site. */
(function () {
  var React = window.React;
  var h = React.createElement;
  var PAGES = window.WG_PAGES;
  var START = 'home';

  function camel(s) { return s.replace(/-([a-z])/g, function (_, c) { return c.toUpperCase(); }); }
  var ATTR = { 'class': 'className', 'for': 'htmlFor', 'onclick': 'onClick', 'onchange': 'onChange', 'autocomplete': 'autoComplete', 'tabindex': 'tabIndex', 'readonly': 'readOnly', 'maxlength': 'maxLength' };

  function lookup(path, scope) {
    path = path.trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path);
    var parts = path.split('.');
    var v;
    for (var i = scope.length - 1; i >= 0; i--) {
      if (scope[i] && Object.prototype.hasOwnProperty.call(scope[i], parts[0])) { v = scope[i][parts[0]]; break; }
    }
    for (var k = 1; k < parts.length && v != null; k++) v = v[parts[k]];
    return v;
  }
  var WHOLE = /^\s*\{\{([^}]+)\}\}\s*$/;
  function value(str, scope) {
    var m = str.match(WHOLE);
    if (m) return lookup(m[1], scope);
    if (str.indexOf('{{') < 0) return str;
    return str.replace(/\{\{([^}]+)\}\}/g, function (_, p) { var v = lookup(p, scope); return v == null ? '' : String(v); });
  }
  function styleObj(str) {
    var o = {};
    var depth = 0, cur = '', parts = [];
    for (var i = 0; i < str.length; i++) {
      var c = str[i];
      if (c === '(') depth++;
      if (c === ')') depth--;
      if (c === ';' && depth === 0) { parts.push(cur); cur = ''; } else cur += c;
    }
    parts.push(cur);
    parts.forEach(function (d) {
      var j = d.indexOf(':');
      if (j < 0) return;
      var k = d.slice(0, j).trim();
      var v = d.slice(j + 1).trim();
      if (!k) return;
      o[k.indexOf('--') === 0 ? k : camel(k)] = v;
    });
    return o;
  }
  function route(href) {
    if (!href) return href;
    return href;
  }

  var key = 0;
  function convert(node, scope) {
    if (node.nodeType === 3) {
      var t = node.nodeValue;
      if (!t.trim()) return t.indexOf('\n') >= 0 ? null : t;
      if (WHOLE.test(t) && !/^\s|\s$/.test(t)) return value(t, scope);
      return t.indexOf('{{') < 0 ? t : t.replace(/\{\{([^}]+)\}\}/g, function (_, q) { var v = lookup(q, scope); return v == null ? '' : String(v); });
    }
    if (node.nodeType !== 1) return null;
    var tag = node.tagName.toLowerCase();
    if (tag === 'sc-for') {
      var list = value(node.getAttribute('list'), scope) || [];
      var as = node.getAttribute('as') || 'item';
      return list.map(function (item, i) {
        var s = {}; s[as] = item; s.$index = i;
        return h(React.Fragment, { key: i }, kids(node, scope.concat([s])));
      });
    }
    if (tag === 'sc-if') {
      return value(node.getAttribute('value'), scope) ? h(React.Fragment, { key: key++ }, kids(node, scope)) : null;
    }
    var props = {};
    var comp = null;
    Array.prototype.forEach.call(node.attributes, function (a) {
      var n = a.name;
      if (n.indexOf('hint-') === 0) return;
      if (tag === 'x-import') {
        if (n === 'component-from-global-scope') {
          comp = a.value.split('.').reduce(function (o, p) { return o && o[p]; }, window);
          return;
        }
        if (n === 'style') return;
        props[camel(n)] = value(a.value, scope);
        return;
      }
      var v = value(a.value, scope);
      if (n === 'style') { props.style = styleObj(String(v)); return; }
      if (n === 'checked') { props.checked = !!v; return; }
      props[ATTR[n] || n] = v;
    });
    var children = kids(node, scope);
    if (tag === 'x-import') {
      if (!comp) return null;
      return h.apply(null, [comp, props].concat(children.length ? children : []));
    }
    if (tag === 'form') props.onSubmit = function (e) { e.preventDefault(); };
    if (tag === 'a' && typeof props.href === 'string' && /^https?:/.test(props.href)) { props.target = '_blank'; props.rel = 'noopener'; }
    if (tag === 'input' && props.checked !== undefined && !props.onChange) props.readOnly = true;
    if (tag === 'input' || tag === 'img' || tag === 'br') return h(tag, props);
    return h.apply(null, [tag, props].concat(children));
  }
  function kids(node, scope) {
    var out = [];
    node.childNodes.forEach(function (c) {
      var r = convert(c, scope);
      if (r === null || r === undefined) return;
      if (Array.isArray(r)) out.push(h(React.Fragment, { key: 'f' + out.length }, r));
      else out.push(typeof r === 'object' ? h(React.Fragment, { key: 'k' + out.length }, r) : r);
    });
    return out;
  }

  var parsed = {};
  function tpl(id) {
    if (!parsed[id]) {
      var t = document.createElement('template');
      t.innerHTML = PAGES[id].tpl;
      parsed[id] = t.content;
    }
    return parsed[id];
  }

  function makeLogic(id) {
    var DCLogic = function (props) { React.Component.call(this, props); this.state = {}; };
    DCLogic.prototype = Object.create(React.Component.prototype);
    DCLogic.prototype.constructor = DCLogic;
    DCLogic.prototype.render = function () {
      return h(React.Fragment, null, kids(tpl(id), [this.renderVals()]));
    };
    return PAGES[id].logic(DCLogic);
  }
  var classes = {};

  function current() {
    var hsh = (location.hash || '').replace('#', '');
    return PAGES[hsh] ? hsh : null;
  }
  function App() {
    var st = React.useState(current() || START);
    var page = st[0], setPage = st[1];
    React.useEffect(function () {
      function onHash() {
        var p = current();
        if (p) { setPage(p); window.scrollTo(0, 0); return; }
        var id = (location.hash || '').replace('#', '');
        var el = id && document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      window.addEventListener('hashchange', onHash);
      return function () { window.removeEventListener('hashchange', onHash); };
    }, []);
    React.useEffect(function () { document.title = PAGES[page].title; }, [page]);
    if (!classes[page]) classes[page] = makeLogic(page);
    return h(classes[page], { key: page });
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (a && a.getAttribute('href') === '#') e.preventDefault();
  });
  ReactDOM.createRoot(document.getElementById('app')).render(h(App));
})();
