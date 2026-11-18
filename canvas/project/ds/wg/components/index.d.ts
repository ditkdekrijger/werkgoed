import type * as React from 'react';

export type BeroepSleutel = 'las' | 'straat' | 'bouw' | 'techniek' | 'magazijn' | 'chauffeur' | 'groen' | 'schilder';
export type IcoonNaam = BeroepSleutel | 'vonk' | 'hitte' | 'regen' | 'kou' | 'zicht' | 'lawaai' | 'stof' | 'snijden' | 'chemie' | 'knielen' | 'hoogte' | 'pijl' | 'check';

export interface ButtonProps { variant?: 'signal' | 'ink' | 'outline' | 'light' | 'outline-light' | 'link'; arrow?: boolean; href?: string; onClick?: () => void; disabled?: boolean; className?: string; children?: React.ReactNode }
export declare function Button(props: ButtonProps): React.ReactElement;

export interface TagProps { active?: boolean; dot?: boolean; onClick?: () => void; className?: string; children?: React.ReactNode }
export declare function Tag(props: TagProps): React.ReactElement;

export interface BadgeProps { tone?: 'vlam' | 'risico' | 'norm' | 'outline' | 'signal' | 'marine'; icoon?: IcoonNaam; className?: string; children?: React.ReactNode }
export declare function Badge(props: BadgeProps): React.ReactElement;

export interface IcoonProps { naam: IcoonNaam; size?: number; stroke?: number; label?: string; className?: string }
export declare function Icoon(props: IcoonProps): React.ReactElement;

export interface HeadingProps { size?: 'mega' | 'display' | 'h1' | 'h2' | 'h3'; as?: string; accent?: string; tone?: 'surface' | 'night'; className?: string; children?: React.ReactNode }
export declare function Heading(props: HeadingProps): React.ReactElement;

export interface CardProps { tone?: 'sunken' | 'canvas' | 'surface' | 'marine' | 'night' | 'signal' | 'vlam'; beroep?: BeroepSleutel; className?: string; children?: React.ReactNode }
export declare function Card(props: CardProps): React.ReactElement;

export interface StreepProps { height?: number }
export declare function Streep(props: StreepProps): React.ReactElement;

export interface ProductKaartProps { merk?: string; naam: string; prijsEx: string; prijsIn?: string; voorraad?: boolean; image?: string; href?: string; badge?: string }
export declare function ProductKaart(props: ProductKaartProps): React.ReactElement;

export interface BeroepKaartProps { beroep: BeroepSleutel; naam: string; regel?: string; risicos?: IcoonNaam[]; icoon?: IcoonNaam; href?: string; className?: string }
export declare function BeroepKaart(props: BeroepKaartProps): React.ReactElement;

export interface Zone { zone: 'hoofd' | 'ogen' | 'gehoor' | 'adem' | 'romp' | 'handen' | 'benen' | 'knieen' | 'voeten'; titel: string; eis: string; product?: string; normen?: string[] }
export interface LichaamskaartProps { zones: Zone[]; beroep?: BeroepSleutel; defaultIndex?: number; className?: string }
export declare function Lichaamskaart(props: LichaamskaartProps): React.ReactElement;

export interface Moment { tijd: string; titel: string; tekst?: string; risicos?: IcoonNaam[]; goed?: string[] }
export interface WerkdagProps { momenten: Moment[]; beroep?: BeroepSleutel; className?: string }
export declare function Werkdag(props: WerkdagProps): React.ReactElement;

export interface Beroep { naam: string; beroep?: BeroepSleutel; regel: string; eisen: string[]; pakket: string[]; href?: string }
export interface BeroepKiezerProps { beroepen: Beroep[]; defaultIndex?: number; href?: string; knop?: string }
export declare function BeroepKiezer(props: BeroepKiezerProps): React.ReactElement;

declare global { interface Window { Werkgoed: { Button: typeof Button; Tag: typeof Tag; Badge: typeof Badge; Icoon: typeof Icoon; Heading: typeof Heading; Card: typeof Card; Streep: typeof Streep; ProductKaart: typeof ProductKaart; BeroepKaart: typeof BeroepKaart; Lichaamskaart: typeof Lichaamskaart; Werkdag: typeof Werkdag; BeroepKiezer: typeof BeroepKiezer } } }
