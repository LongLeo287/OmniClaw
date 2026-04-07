---
id: irminsul
type: knowledge
owner: OA_Triage
---
# irminsul
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "irminsul-gg-v2",
    "version": "0.1.0",
    "private": true,
    "scripts": {
        "dev": "cmd.exe /c start chrome.exe http://localhost:8080 && next dev --port 8080",
        "build": "next build",
        "start": "next start",
        "lint": "eslint"
    },
    "dependencies": {
        "@dnd-kit/core": "^6.3.1",
        "@dnd-kit/modifiers": "^9.0.0",
        "@dnd-kit/sortable": "^10.0.0",
        "@emotion/cache": "^11.14.0",
        "@emotion/react": "^11.14.0",
        "@emotion/styled": "^11.14.1",
        "@fullcalendar/core": "^6.1.15",
        "@fullcalendar/daygrid": "^6.1.15",
        "@fullcalendar/react": "^6.1.15",
        "@fullcalendar/rrule": "^6.1.15",
        "@mui/icons-material": "^7.3.4",
        "@mui/material": "^7.3.4",
        "@mui/material-nextjs": "^7.3.6",
        "@next/eslint-plugin-next": "16.1.0",
        "@reduxjs/toolkit": "^2.9.0",
        "html-react-parser": "^5.1.18",
        "match-sorter": "^8.0.0",
        "next": "16.1.0",
        "react": "19.2.3",
        "react-dom": "19.2.3",
        "react-xarrows": "^2.0.2",
        "swr": "^2.3.6",
        "zustand": "^5.0.8"
    },
    "devDependencies": {
        "@eslint/eslintrc": "^3",
        "@eslint/js": "^9.37.0",
        "@types/node": "^20",
        "@types/react": "19.2.7",
        "@types/react-dom": "19.2.3",
        "eslint": "^9",
        "eslint-config-next": "16.1.0",
        "eslint-config-prettier": "^10.1.8",
        "eslint-plugin-react": "^7.37.5",
        "eslint-plugin-react-refresh": "^0.4.23",
        "globals": "^15.11.0",
        "typescript": "^5"
    },
    "overrides": {
        "@types/react": "19.2.7",
        "@types/react-dom": "19.2.3"
    }
}
```

### File: README.md
```md
# <img src="https://assets.irminsul.gg/v2/_common/logo/logo_red.png" alt="Irminsul.GG" width="48" /> **[IRMINSUL.GG](https://irminsul.gg/)**

**IRMINSUL.GG** is a database and companion website for various gacha games.

**Irminsul.GG** branches:

-   [**Genshin Impact**](https://irminsul.gg/genshin)

-   [**Honkai: Star Rail**](https://irminsul.gg/hsr)

-   [**Wuthering Waves**](https://irminsul.gg/wuwa)

-   [**Zenless Zone Zero**](https://irminsul.gg/zzz)

-   [**Umamusume: Pretty Derby**](https://irminsul.gg/uma)

-   [**Arknights: Endfield**](https://irminsul.gg/endfield)

## **Previews**

**Genshin Impact**:
![preview](https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/genshin/preview.png)

**Honkai: Star Rail**:
![preview](https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/hsr/preview.png)

**Wuthering Waves**:
![preview](https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/wuwa/preview.png)

**Zenless Zone Zero**:
![preview](https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/zzz/preview.png)

**Umamusume: Pretty Derby**:
![preview](https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/uma/preview.png)

**Arknights: Endfield**:
![preview](https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/endfield/preview.png)

---

**IRMINSUL.GG** is not affiliated with the developers of the games featured.
Game contents are trademarks and copyrights of their respective developers.

```

### File: next.config.ts
```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    /* config options here */
    images: {
        remotePatterns: [
            {
                protocol: "https",
                hostname: "assets.irminsul.gg",
                port: "",
                pathname: "/**",
                search: "",
            },
            {
                protocol: "https",
                hostname: "raw.githubusercontent.com",
                port: "",
                pathname: "bcheung98/irminsul-gg/**",
                search: "",
            },
        ],
    },
    experimental: {
        serverActions: {
            bodySizeLimit: "4mb",
        },
        webpackMemoryOptimizations: true,
    },
};

export default nextConfig;

```

### File: tsconfig.json
```json
{
    "compilerOptions": {
        "target": "ES2017",
        "lib": ["dom", "dom.iterable", "esnext"],
        "allowJs": true,
        "skipLibCheck": true,
        "strict": true,
        "noEmit": true,
        "esModuleInterop": true,
        "module": "esnext",
        "moduleResolution": "bundler",
        "resolveJsonModule": true,
        "isolatedModules": true,
        "jsx": "react-jsx",
        "incremental": true,
        "plugins": [
            {
                "name": "next"
            }
        ],
        "paths": {
            "@/*": ["./src/*"]
        }
    },
    "include": [
        "next-env.d.ts",
        "**/*.ts",
        "**/*.tsx",
        ".next/types/**/*.ts",
        ".next/dev/types/**/*.ts"
    ],
    "exclude": ["**/*.js", "node_modules"]
}

```

### File: src\app\globals.css
```css
:root {
    color-scheme: dark;
    scrollbar-gutter: stable;
    background-color: inherit;
}

body {
    margin: 0;
    padding-right: 0 !important;
    background-color: transparent;
    font-family: Geist, "Segoe UI", Roboto, Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

body:has(.lock-scroll):not(.nav-mobile) {
    overflow: hidden;
}

code {
    font-family: Consolas, "Courier New", Menlo, Monaco, monospace;
}

a {
    color: inherit;
    text-decoration: none;
}

span > a {
    color: rgb(30, 175, 255);
}

ul {
    margin: 0;
    padding-left: 18px;
}

img,
video {
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -o-user-select: none;
    user-select: none;
    -webkit-user-drag: none;
    -khtml-user-drag: none;
    -moz-user-drag: none;
    -o-user-drag: none;
}

.background-image {
    object-fit: cover;
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    scale: 1.05;
    z-index: -1;
    transition: opacity 0.5s;
}

.background-image.inactive {
    opacity: 0;
}

.background-image.active {
    opacity: 1;
}

.background-video {
    transition: opacity 1s;
}

.background-video.inactive {
    opacity: 0;
}

#global-error {
    background-color: rgba(16, 16, 16, 0.75);
    border-radius: 8px;
}

.global-error-text,
.global-error-code-text {
    color: white;
}

.global-error-text {
    font-family: Geist;
    font-weight: 600;
}

.global-error-code-text {
    font-size: 11pt;
}

```

### File: src\app\manifest.ts
```ts
import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
    return {
        name: "Irminsul.GG",
        short_name: "Irminsul.GG",
        description:
            "Irminsul.GG - A database and companion website for various gacha games.",
        start_url: "/",
        display: "minimal-ui",
        background_color: "rgb(40, 40, 40)",
        theme_color: "rgb(8, 8, 8)",
        icons: [
            {
                src: "icon-72.png",
                sizes: "72x72",
                type: "image/png",
                purpose: "maskable",
            },
            {
                src: "icon-128.png",
                sizes: "128x128",
                type: "image/png",
                purpose: "maskable",
            },
            {
                src: "icon-144.png",
                sizes: "144x144",
                type: "image/png",
                purpose: "maskable",
            },
            {
                src: "icon-192.png",
                sizes: "192x192",
                type: "image/png",
                purpose: "maskable",
            },
            {
                src: "icon-512.png",
                sizes: "512x512",
                type: "image/png",
                purpose: "maskable",
            },
        ],
        shortcuts: [
            {
                name: "Gacha Calendar",
                short_name: "Calendar",
                url: "/calendar",
            },
            {
                name: "Genshin Impact",
                short_name: "Genshin",
                url: "/genshin",
                icons: [
                    {
                        src: "https://assets.irminsul.gg/v2/genshin/_common/Icon.png",
                        sizes: "any",
                        type: "image/png",
                    },
                ],
            },
            {
                name: "Honkai: Star Rail",
                short_name: "HSR",
                url: "/hsr",
                icons: [
                    {
                        src: "https://assets.irminsul.gg/v2/hsr/_common/Icon.png",
                        sizes: "any",
                        type: "image/png",
                    },
                ],
            },
            {
                name: "Wuthering Waves",
                short_name: "WuWa",
                url: "/wuwa",
                icons: [
                    {
                        src: "https://assets.irminsul.gg/v2/wuwa/_common/Icon.png",
                        sizes: "any",
                        type: "image/png",
                    },
                ],
            },
            {
                name: "Zenless Zone Zero",
                short_name: "ZZZ",
                url: "/zzz",
                icons: [
                    {
                        src: "https://assets.irminsul.gg/v2/zzz/_common/Icon.png",
                        sizes: "any",
                        type: "image/png",
                    },
                ],
            },
            {
                name: "Umamusume",
                short_name: "Uma",
                url: "/uma",
                icons: [
                    {
                        src: "https://assets.irminsul.gg/v2/uma/_common/Icon.png",
                        sizes: "any",
                        type: "image/png",
                    },
                ],
            },
        ],
    };
}

```

### File: src\context\index.ts
```ts
import { createContext, useContext } from "react";
import { Game, GameInfo } from "@/types";
import { CharacterSkillsList, SkillKeyword } from "@/types/skill";
import { CharacterBuffs } from "@/types/character";
import { UmaSkill } from "@/types/uma/skill";
import { EventList, Events } from "@/types/uma/event";
import { UmaCharacterProfile } from "@/types/uma/character";

const defaultGameInfo = {
    tag: "" as Game,
    name: "",
    shortName: "",
    enabled: true,
    color: "rgb(11, 110, 175)",
    dev: "",
};

const defaultCharacterBuff = {
    versions: [{ value: "v1", label: "Original" }],
    value: "v1",
};

interface UmaContext {
    skills: UmaSkill[];
    events: Partial<EventList>;
    profiles: UmaCharacterProfile[];
}

export const GameListContext = createContext<GameInfo[]>([]);
export const GameContext = createContext<GameInfo>(defaultGameInfo);
export const DataContext = createContext<any[]>([]);
export const SkillContext = createContext<CharacterSkillsList | null>(null);
export const SkillVersionContext =
    createContext<CharacterBuffs>(defaultCharacterBuff);
export const SearchContext = createContext<string>("");
export const TCGKeywordContext = createContext<SkillKeyword[]>([]);
export const CharIDContext = createContext<number | string>(0);
export const CardIDContext = createContext<number>(0);
export const UmaContext = createContext<UmaContext>({
    skills: [],
    events: {},
    profiles: [],
});

export function useGameList() {
    return useContext(GameListContext);
}

export function useGame() {
    return useContext(GameContext);
}

export function useGameTag() {
    const context = useGame();
    return (context ? context.tag : "") as Game;
}

export function useDataContext() {
    return useContext(DataContext);
}

export function useSkillContext() {
    return useContext(SkillContext);
}

export function useSkillVersionContext() {
    return useContext(SkillVersionContext);
}

export function useSearchContext() {
    return useContext(SearchContext);
}

export function useTCGKeywordContext() {
    return useContext(TCGKeywordContext);
}

export function useCharIDContext() {
    return useContext(CharIDContext);
}

export function useCardIDContext() {
    return useContext(CardIDContext);
}

export function useUmaContext() {
    return useContext(UmaContext);
}

```

### File: src\data\banners.ts
```ts
import { ToggleButtonProps } from "@/components/ToggleButtons/ToggleButtons.types";
import { GameData } from "@/types";

export const banners: GameData<ToggleButtonProps[]> = {
    genshin: [
        {
            value: "character",
            label: "Character",
        },
        {
            value: "weapon",
            label: "Weapon",
        },
        {
            value: "chronicled",
            label: "Chronicled",
        },
    ],
    hsr: [
        {
            value: "character",
            label: "Character",
        },
        {
            value: "weapon",
            label: "Light Cone",
        },
    ],
    wuwa: [
        {
            value: "character",
            label: "Resonator",
        },
        {
            value: "weapon",
            label: "Weapon",
        },
    ],
    zzz: [
        {
            value: "character",
            label: "Agent",
        },
        {
            value: "weapon",
            label: "W-Engine",
        },
    ],
    uma: [
        {
            value: "character",
            label: "Character",
        },
        {
            value: "weapon",
            label: "Support Card",
        },
    ],
    endfield: [
        {
            value: "character",
            label: "Operator",
        },
        {
            value: "weapon",
            label: "Weapon",
        },
    ],
};

```

### File: src\data\blog-list.ts
```ts
export const blogList = [
    {
        slug: "endfield-update",
        title: "Arknights: Endfield is here!",
        description: "Check out the new Endfield site for Irminsul.GG.",
        date: "2026-01-21 10:00:00",
        image: "endfield/_common/wallpapers/Endfield_1.0",
    },
    {
        slug: "irminsul-gg-v2-release-notes",
        title: "Irminsul.GG v2.0 Release Notes",
        description: "Check out what's new in Irminsul.GG v2.0.",
        date: "2025-12-21 10:00:00",
        image: "https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/genshin/preview.png",
    },
    {
        slug: "uma-update",
        title: "Umamusume: Pretty Derby is here!",
        description: "Check out the new Umamusume site for Irminsul.GG.",
        date: "2025-08-24 10:00:00",
        image: "uma/_common/wallpapers/Uma_1.0",
    },
    {
        slug: "new-calendar-and-search",
        title: "New features - Calendar and Site Search",
        description:
            "Learn more about the new Gacha Calendar and Site Search features.",
        date: "2025-02-01 10:00:00",
        image: "https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/calendar-img.png",
    },
    {
        slug: "irminsul-gg-v1-release-notes",
        title: "Irminsul.GG v1.0 Release Notes",
        description: "Check out what's new in Irminsul.GG v1.0.",
        date: "2025-01-16 10:00:00",
        lastEdit: "2025-12-21 10:00:00",
        image: "https://raw.githubusercontent.com/bcheung98/irminsul-gg/refs/heads/main/.docs/_v1/genshin/preview.png",
    },
    {
        slug: "irminsul-gg-v0.6-release-notes",
        title: "Irminsul.GG v0.6 Release Notes",
        description: "Check out what's new in Irminsul.GG v0.6.",
        date: "2024-11-22 10:00:00",
        lastEdit: "2025-12-21 10:00:00",
    },
    {
        slug: "1.0-roadmap",
        title: "Roadmap to v1.0",
        description: "Find out what's coming in the next major release.",
        date: "2024-09-23 10:00:00",
    },
    {
        slug: "the-story-of-irminsul-gg",
        title: "The Story of Irminsul.GG",
        description: "Learn about the origins of Irminsul.GG.",
        date: "2024-09-21 10:00:00",
        lastEdit: "2025-12-21 10:00:00",
    },
];

export interface BlogPost {
    slug: string;
    title: string;
    description: string;
    date: string;
    lastEdit?: string;
    image?: string;
}

```

### File: src\data\categories.ts
```ts
export const categories: Record<string, string> = {
    "genshin/characters": "Characters",
    "genshin/weapons": "Weapons",
    "genshin/equipment": "Artifacts",
    "genshin/cards": "TCG Cards",
    "hsr/characters": "Characters",
    "hsr/weapons": "Light Cones",
    "hsr/equipment": "Relics",
    "wuwa/characters": "Resonators",
    "wuwa/weapons": "Weapons",
    "wuwa/equipment": "Echoes",
    "zzz/characters": "Agents",
    "zzz/weapons": "W-Engines",
    "zzz/equipment": "Drive Discs",
    "zzz/bangboos": "Bangboos",
    "uma/characters": "Characters",
    "uma/supports": "Support Cards",
    "endfield/characters": "Operators",
    "endfield/operators": "Operators",
    "endfield/weapons": "Weapons",
};

export const categoryURLs: Record<string, string> = {
    "genshin/characters": "genshin/characters",
    "genshin/weapons": "genshin/weapons",
    "genshin/equipment": "genshin/artifacts",
    "genshin/cards": "genshin/tcg",
    "hsr/characters": "hsr/characters",
    "hsr/weapons": "hsr/lightcones",
    "hsr/equipment": "hsr/relics",
    "wuwa/characters": "wuwa/resonators",
    "wuwa/weapons": "wuwa/weapons",
    "wuwa/equipment": "wuwa/echoes",
    "zzz/characters": "zzz/agents",
    "zzz/weapons": "zzz/w-engines",
    "zzz/equipment": "zzz/drive-discs",
    "zzz/bangboos": "zzz/bangboos",
    "uma/characters": "uma/characters",
    "uma/weapons": "uma/supports", // Need this for category sorting
    "uma/supports": "uma/supports",
    "endfield/characters": "endfield/operators",
    "endfield/operators": "endfield/operators",
    "endfield/weapons": "endfield/weapons",
};

export const categoryImgURLs: Record<
    string,
    (args0?: any, args1?: any) => string
> = {
    "genshin/characters": (id: number) => `genshin/characters/${id}`,
    "genshin/weapons": (id: number) => `genshin/weapons/${id}`,
    "genshin/equipment": (id: number, name: string) =>
        `genshin/artifacts/${id}${name.startsWith("Prayers") ? "_5" : "_1"}`,
    "genshin/cards": (id: number) => `genshin/tcg/cards/${id}`,
    "hsr/characters": (id: number) => `hsr/characters/${id}`,
    "hsr/weapons": (id: number) => `hsr/lightcones/${id}_icon`,
    "hsr/equipment": (id: number) => `hsr/relics/${id}`,
    "wuwa/characters": (id: number) => `wuwa/resonators/${id}`,
    "wuwa/weapons": (id: number) => `wuwa/weapons/${id}`,
    "wuwa/equipment": (id: number) => `wuwa/echoes/${id}`,
    "zzz/characters": (id: number) => `zzz/agents/${id}`,
    "zzz/weapons": (id: number) => `zzz/w-engines/${id}`,
    "zzz/equipment": (id: number) => `zzz/drive-discs/${id}`,
    "zzz/bangboos": (id: number) => `zzz/bangboos/${id}`,
    "uma/characters": (id: number) => `uma/characters/${id}`,
    "uma/weapons": (id: number) => `uma/supports/${id}_icon`, // Need this for category sorting
    "uma/supports": (id: number) => `uma/supports/${id}_icon`,
    "endfield/characters": (id: number) => `endfield/operators/${id}`,
    "endfield/operators": (id: number) => `endfield/operators/${id}`,
    "endfield/weapons": (id: number) => `endfield/weapons/${id}`,
};

```

### File: src\data\equipment.ts
```ts
import { GameData } from "@/types";

export const equipmentTags: GameData<string> = {
    genshin: "artifacts",
    hsr: "relics",
    wuwa: "echoes",
    zzz: "drive-discs",
    uma: "",
    endfield: "",
};

export const equipmentPieceType: GameData<Record<string, string>> = {
    genshin: {
        flower: "Flower of Life",
        feather: "Plume of Death",
        sands: "Sands of Eon",
        goblet: "Goblet of Eonothem",
        circlet: "Circlet of Logos",
    },
    hsr: {
        head: "Head",
        hand: "Hands",
        body: "Body",
        feet: "Feet",
        orb: "Planar Sphere",
        rope: "Link Rope",
    },
    wuwa: {},
    zzz: {},
    uma: {},
    endfield: {},
};

```

### File: src\data\filters.ts
```ts
import { FilterGroups, FilterGroupsProps, Filters, GameData } from "@/types";
import { endfieldFilters } from "./endfield/filters";
import { genshinFilters } from "./genshin/filters";
import { hsrFilters } from "./hsr/filters";
import { umaFilters } from "./uma/filters";
import { wuwaFilters } from "./wuwa/filters";
import { zzzFilters } from "./zzz/filters";

export function filterGroups<T extends Filters>(
    props: FilterGroupsProps<T>
): GameData<FilterGroups> {
    return {
        genshin: genshinFilters(props),
        hsr: hsrFilters(props),
        wuwa: wuwaFilters(props),
        zzz: zzzFilters(props),
        uma: umaFilters(props),
        endfield: endfieldFilters(props),
    };
}

```

### File: src\data\games.ts
```ts
import { Game, GameInfo } from "@/types";

export const gameNames = [
    "genshin",
    "hsr",
    "wuwa",
    "zzz",
    "uma",
    "endfield",
] as const;

export const games: Record<Game, GameInfo> = {
    genshin: {
        tag: "genshin",
        name: "Genshin Impact",
        shortName: "Genshin",
        enabled: true,
        color: "rgb(11, 110, 175)",
        dev: "HoYoverse",
    },
    hsr: {
        tag: "hsr",
        name: "Honkai: Star Rail",
        shortName: "HSR",
        enabled: true,
        color: "rgb(168, 53, 179)",
        dev: "HoYoverse",
    },
    wuwa: {
        tag: "wuwa",
        name: "Wuthering Waves",
        shortName: "WuWa",
        enabled: true,
        color: "rgb(131, 106, 53)",
        dev: "Kuro Games",
    },
    zzz: {
        tag: "zzz",
        name: "Zenless Zone Zero",
        shortName: "ZZZ",
        enabled: true,
        color: "rgb(209, 111, 12)",
        dev: "HoYoverse",
    },
    uma: {
        tag: "uma",
        name: "Umamusume: Pretty Derby",
        shortName: "Uma",
        enabled: true,
        color: "rgb(44, 159, 4)",
        dev: "Cygames",
    },
    endfield: {
        tag: "endfield",
        name: "Arknights: Endfield",
        shortName: "Endfield",
        enabled: true,
        color: "rgb(255, 241, 0)",
        dev: "Gryphline",
    },
} as const;

```

### File: src\data\levels.ts
```ts
import { GameData } from "@/types";
import { genshinLevels } from "./genshin/levels";
import { hsrLevels } from "./hsr/levels";
import { wuwaLevels } from "./wuwa/levels";
import { zzzLevels } from "./zzz/levels";
import { endfieldLevels } from "./endfield/levels";

const levels: GameData<(key: string, rarity?: number) => (string | number)[]> =
    {
        genshin: genshinLevels,
        hsr: hsrLevels,
        wuwa: wuwaLevels,
        zzz: zzzLevels,
        uma: function (key: string): (string | number)[] {
            throw new Error("Function not implemented.");
        },
        endfield: endfieldLevels,
    };

export default levels;

```

### File: src\data\navItems.ts
```ts
import { GameData } from "@/types";

export interface NavItem {
    icon: string;
    title: string;
    href: string;
}

export const navItems: GameData<NavItem[]> = {
    genshin: [
        {
            icon: "icons/Home",
            title: "Home",
            href: "",
        },
        {
            icon: "icons/Aether",
            title: "Characters",
            href: "characters",
        },
        {
            icon: "icons/Weapons",
            title: "Weapons",
            href: "weapons",
        },
        {
            icon: "icons/Artifact",
            title: "Artifacts",
            href: "artifacts",
        },
        // {
        //     icon: "icons/TCG",
        //     title: "TCG",
        //     href: "tcg",
        // },
        {
            icon: "icons/Ascension",
            title: "Ascension Planner",
            href: "planner",
        },
        {
            icon: "icons/Wish",
            title: "Banner Archive",
            href: "banners",
        },
    ],
    hsr: [
        {
            icon: "icons/Home",
            title: "Home",
            href: "",
        },
        {
            icon: "icons/Character",
            title: "Characters",
            href: "characters",
        },
        {
            icon: "icons/Lightcone",
            title: "Light Cones",
            href: "lightcones",
        },
        {
            icon: "icons/Relic",
            title: "Relics",
            href: "relics",
        },
        {
            icon: "icons/Ascension",
            title: "Ascension Planner",
            href: "planner",
        },
        {
            icon: "icons/Warp",
            title: "Banner Archive",
            href: "banners",
        },
    ],
    wuwa: [
        {
            icon: "icons/Home",
            title: "Home",
            href: "",
        },
        {
            icon: "icons/Character",
            title: "Resonators",
            href: "resonators",
        },
        {
            icon: "icons/Weapon",
            title: "Weapons",
            href: "weapons",
        },
        {
            icon: "icons/Echo",
            title: "Echoes",
            href: "echoes",
        },
        {
            icon: "icons/Ascension",
            title: "Ascension Planner",
            href: "planner",
        },
        {
            icon: "icons/Convene",
            title: "Banner Archive",
            href: "banners",
        },
    ],
    zzz: [
        {
            icon: "icons/Home",
            title: "Home",
            href: "",
        },
        {
            icon: "icons/Agents",
            title: "Agents",
            href: "agents",
        },
        {
            icon: "icons/W-Engine",
            title: "W-Engines",
            href: "w-engines",
        },
        {
            icon: "icons/Drive_Disc",
            title: "Drive Discs",
            href: "drive-discs",
        },
        {
            icon: "icons/Bangboo",
            title: "Bangboos",
            href: "bangboos",
        },
        {
            icon: "icons/Check",
            title: "Ascension Planner",
            href: "planner",
        },
        {
            icon: "icons/Signal_Search",
            title: "Banner Archive",
            href: "banners",
        },
    ],
    uma: [
        {
            icon: "icons/Home",
            title: "Home",
            href: "",
        },
        {
            icon: "icons/Horse",
            title: "Characters",
            href: "characters",
        },
        {
            icon: "icons/Card",
            title: "Support Cards",
            href: "supports",
        },
        {
            icon: "icons/Skill",
            title: "Skills",
            href: "skills",
        },
        {
            icon: "icons/Training",
            title: "Training Event Helper",
            href: "training-event-helper",
        },
        {
            icon: "icons/Ticket",
            title: "Banner Archive",
            href: "banners",
        },
    ],
    endfield: [
        {
            icon: "icons/World",
            title: "Home",
            href: "",
        },
        {
            icon: "icons/Operators",
            title: "Operators",
            href: "operators",
        },
        {
            icon: "icons/Weapons",
            title: "Weapons",
            href: "weapons",
        },
        {
            icon: "icons/Upgrade",
            title: "Ascension Planner",
            href: "planner",
        },
        {
            icon: "icons/Headhunt",
            title: "Banner Archive",
            href: "banners",
        },
    ],
};

```

### File: src\data\settings.ts
```ts
import { ToggleButtonProps } from "@/components/ToggleButtons/ToggleButtons.types";
import { themeList } from "@/themes/theme";
import { Game } from "@/types";

export const themeButtons: ToggleButtonProps[] = themeList.map((theme) => ({
    value: theme.id,
    label: theme.name,
}));

export const statDisplayButtons: ToggleButtonProps[] = [
    { value: "slider", label: "Slider" },
    { value: "table", label: "Table" },
];

export const serverButtons: ToggleButtonProps[] = [
    { value: "NA", label: "NA" },
    { value: "EU", label: "EU" },
    { value: "Asia", label: "Asia" },
];

export const serverButtonsUma: ToggleButtonProps[] = [
    { value: "NA", label: "Global" },
    { value: "Asia", label: "JP" },
];

export const serverButtonsEndfield: ToggleButtonProps[] = [
    { value: "NA", label: "NA/EU" },
    { value: "Asia", label: "Asia" },
];

export const forbiddenKnowledge: ToggleButtonProps[] = [
    // The boolean determines if unreleased content should be hidden,
    // but the label determines if unreleased content should be shown,
    // hence why the value and label seem paradoxical.
    { value: true, label: "Disable" },
    { value: false, label: "Enable" },
];

export function getServerButtons(game: Game) {
    switch (game) {
        case "genshin":
        case "hsr":
        case "wuwa":
        case "zzz":
        default:
            return serverButtons;
        case "uma":
            return serverButtonsUma;
        case "endfield":
            return serverButtonsEndfield;
    }
}

```

### File: src\data\skills.ts
```ts
import { GameData } from "@/types";

export const skillKeys: GameData<Record<string, string>> = {
    genshin: {
        attack: "Normal Attack",
        skill: "Elemental Skill",
        ultimate: "Elemental Burst",
        altsprint: "Alternate Sprint",
        a1: "1st Ascension Passive",
        a4: "4th Ascension Passive",
        util: "Passive Talent",
        nightsoul: "Night Realm's Gift Passive",
        moon: "Moonsign Benediction",
        special: "",
        "": "Passive Talent",
    },
    hsr: {
        attack: "Basic ATK",
        skill: "Skill",
        ultimate: "Ultimate",
        talent: "Talent",
        technique: "Technique",
        "memo-skill": "Memosprite Skill",
        "memo-talent": "Memosprite Talent",
        elation: "Elation Skill",
    },
    wuwa: {
        attack: "Basic Attack",
        skill: "Resonance Skill",
        ultimate: "Resonance Liberation",
        forte: "Forte Circuit",
        intro: "Intro Skill",
        outro: "Outro Skill",
        break: "Tune Break",
    },
    zzz: {
        attack: "Basic Attack",
        dodge: "Dodge",
        assist: "Assist",
        special: "Special Attack",
        chain: "Chain Attack",
        core: "Core Skill",
    },
    uma: {},
    endfield: {
        attack: "Basic Attack",
        skill: "Battle Skill",
        combo: "Combo Skill",
        ultimate: "Ultimate",
    },
};

export const skillIconURLs: GameData<Record<string, string>> = {
    genshin: {
        attack: "genshin/skills/Attack_{weaponType}",
        skill: "genshin/skills/{id}_skill",
        ultimate: "genshin/skills/{id}_ultimate",
        altsprint: "genshin/skills/{id}_altsprint",
        a1: "genshin/skills/{id}_passive_a1",
        a4: "genshin/skills/{id}_passive_a4",
        util: "genshin/skills/{id}_passive_util",
        nightsoul: "genshin/skills/{id}_passive_nightsoul",
        moon: "genshin/skills/{id}_passive_moon",
        special: "genshin/skills/{id}_passive_special",
        "": "genshin/skills/{id}_passive",
    },
    hsr: {
        attack: "hsr/skills/{id}_attack",
        skill: "hsr/skills/{id}_skill",
        ultimate: "hsr/skills/{id}_ultimate",
        talent: "hsr/skills/{id}_talent",
        technique: "hsr/skills/{id}_technique",
        "memo-skill": "hsr/skills/{id}_memo_skill",
        "memo-talent": "hsr/skills/{id}_memo_talent",
        elation: "hsr/skills/{id}_elation",
    },
    wuwa: {
        attack: "wuwa/skills/Attack_{weaponType}",
        skill: "wuwa/skills/{id}_skill",
        ultimate: "wuwa/skills/{id}_ultimate",
        forte: "wuwa/skills/{id}_forte",
        passive1: "wuwa/skills/{id}_passive1",
        passive2: "wuwa/skills/{id}_passive2",
        intro: "wuwa/skills/{id}_intro",
        outro: "wuwa/skills/{id}_outro",
        break: "wuwa/skills/Break_{weaponType}",
    },
    zzz: {
        attack: "zzz/skills/Attack",
        dodge: "zzz/skills/Dodge",
        assist: "zzz/skills/Assist",
        special: "zzz/skills/SpecialEX",
        chain: "zzz/skills/Ultimate",
        core: "zzz/skills/Core",
        A: "zzz/skills/Bangboo_A",
        B: "zzz/skills/Bangboo_B",
        C: "zzz/skills/Bangboo_C",
    },
    uma: {},
    endfield: {
        attack: "endfield/skills/Attack_{weaponType}",
        skill: "endfield/skills/{id}_skill",
        combo: "endfield/skills/{id}_combo",
        ultimate: "endfield/skills/{id}_ultimate",
        passive: "endfield/skills/{id}_talent",
    },
};

```

### File: src\data\versions.ts
```ts
import { GameData } from "@/types";
import { VersionInfo } from "@/types/version";
import { endfieldVersions } from "./endfield/versions";
import { genshinVersions } from "./genshin/versions";
import { hsrVersions } from "./hsr/versions";
import { umaVersions } from "./uma/versions";
import { wuwaVersions } from "./wuwa/versions";
import { zzzVersions } from "./zzz/versions";

const versions: GameData<VersionInfo[]> = {
    genshin: genshinVersions,
    hsr: hsrVersions,
    wuwa: wuwaVersions,
    zzz: zzzVersions,
    uma: umaVersions,
    endfield: endfieldVersions,
};

export default versions;

```

### File: src\helpers\calendar.ts
```ts
import { getVersionDates } from "@/components/BannerArchive/BannerArchive.utils";
import DateObject from "./dates";
import { games } from "@/data/games";
import { Game, Server } from "@/types";
import { Banner } from "@/types/banner";
import { CalendarVersionInfo, EventObject } from "@/types/calendar";

function incrementVersionNumber(version: string, game: Game) {
    let main: number | string;
    let sub: number | string;
    let versionNumber: string;
    // Genshin specific
    if (game === "genshin" && version.startsWith("Luna")) {
        const arr = version.split(" ");
        main = arr[0];
        const index = numerals.findIndex((i) => i === arr[1].split(".")[0]);
        sub = numerals[index + 1];
        versionNumber = `${main} ${sub}`;
    } else {
        const arr = version.split(".");
        main = parseInt(arr[0]);
        sub = parseInt(arr[1]);
        if (sub < 8) {
            sub += 1;
        } else {
            main += 1;
            sub = 0;
        }
        versionNumber = `${main}.${sub}`;
    }

    // Game specific adjustments
    if (game === "genshin" && versionNumber === "Luna X") {
        return "7.0";
    }

    return versionNumber;
}

const numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];

export function createEventSourceObject({
    tag,
    banners,
    server,
    showFullDuration,
}: {
    tag: string;
    banners: Banner[];
    server: Server;
    showFullDuration: boolean;
}): EventObject[] {
    const game = tag.split("/")[0] as Game;
    if (game === "uma" && server === "NA") {
        banners = banners.filter((banner) => banner.start !== "");
    }
    return createVersionInfo({ game, banners }).map((version) => {
        const { versionStart, versionEnd } = getVersionDates(
            version,
            server,
            game,
        );
        const start = new DateObject(versionStart, server, game).date;
        const end = new DateObject(versionEnd, server, game).date;
        return {
            id: `${game}-${version.id}`,
            title: `${games[game].shortName} ${version.version}`,
            start: start.toISOString(),
            end: showFullDuration ? end.toISOString() : undefined,
            extendedProps: {
                game,
                color: games[game].color,
                isCurrent: DateObject.inRange(start, end),
                ...version,
            },
        };
    });
}

export function createVersionInfo({
    game,
    banners,
}: {
    game: Game;
    banners: Banner[];
}): CalendarVersionInfo[] {
    const versions: CalendarVersionInfo[] = [...banners];

    // Create future version info
    // TODO: Remove Endfield from list once consistent banner schedule is known
    if (!["uma", "endfield"].includes(game)) {
        const lastVersion = versions.slice(-1)[0];
        let { id, version } = lastVersion;
        let start = new DateObject(lastVersion.end).date;
        let end = new DateObject(lastVersion.end).date;
        let startTime, startUTC, endTime, endUTC;
        id++;
        for (let i = 0; i < 32; i++) {
            if (["genshin", "wuwa"].includes(game) && i % 2 === 1) {
                start.setDate(end.getDate());
            } else {
                start.setDate(end.getDate() + 1);
            }
            if (lastVersion.version.endsWith(".1")) {
                end.setDate(end.getDate() + 42);
            } else {
                if (game === "wuwa") {
                    if (i % 2 === 0) {
                        end.setDate(end.getDate() + 22);
                    } else {
                        end.setDate(end.getDate() + 20);
                    }
                } else {
                    end.setDate(end.getDate() + 21);
                }
            }
            // Phase 1
            if (i % 2 === 0) {
                version = incrementVersionNumber(version, game);
                startTime = "11:00:00";
                startUTC = " UTC+8";
                switch (game) {
                    case "genshin":
                        endTime = "17:59:59";
                        break;
                    case "hsr":
                        endTime = "11:59:59";
                        break;
                    case "wuwa":
                        endTime = "09:59:59";
                        break;
                    case "zzz":
                        endTime = "11:59:59";
                        break;
                    default:
                        endTime = "17:59:59";
                        break;
                }
                endUTC = "";
            }
            // Phase 2
            else {
                switch (game) {
                    case "genshin":
                        startTime = "18:00:00";
                        endTime = "14:59:59";
                        break;
                    case "hsr":
                        startTime = "12:00:00";
                        endTime = "14:59:59";
                        break;
                    case "wuwa":
                        startTime = "10:00:00";
                        endTime = "11:59:59";
                        break;
                    case "zzz":
                        startTime = "12:00:00";
                        endTime = "14:59:59";
                        break;
                    default:
                        startTime = "18:00:00";
                        endTime = "14:59:59";
                        break;
                }
                startUTC = "";
                endUTC = "";
            }
            const newStartString = `${
                start.toISOString().split("T")[0]
            } ${startTime}${startUTC}`;
            const newEndString = `${
                end.toISOString().split("T")[0]
            } ${endTime}${endUTC}`;
            versions.push({
                id: id,
                version: `${version}.${(i % 2) + 1}`,
                start: newStartString,
                end: newEndString,
                rateUps: [],
                isFuture: true,
            });
            start = new DateObject(newEndString).date;
            end = new DateObject(newEndString).date;
            id++;
        }
    }
    return versions;
}

```

### File: src\helpers\costs.ts
```ts
import { GameData } from "@/types";
import { CostArray, CostValue } from "@/types/costs";
import {
    getCharacterLevelCost as getGenshinCharacterLevelCost,
    getCharacterSkillCost as getGenshinCharacterSkillCost,
    getWeaponLevelCost as getGenshinWeaponLevelCost,
} from "./genshin/getLevelUpCosts";
import {
    getCharacterLevelCost as getHSRCharacterLevelCost,
    getCharacterSkillCost as getHSRCharacterSkillCost,
    getWeaponLevelCost as getHSRWeaponLevelCost,
    getCharacterMemosprite as getHSRCharacterMemosprite,
    getCharacterTraceMain as getHSRCharacterTraceMain,
    getCharacterTraceSmall as getHSRCharacterTraceSmall,
} from "./hsr/getLevelUpCosts";
import {
    getCharacterLevelCost as getWuWaCharacterLevelCost,
    getCharacterSkillCost as getWuWaCharacterSkillCost,
    getCharacterPassiveCost as getWuWaCharacterPassiveCost,
    getCharacterBonusStatCost as getWuWaCharacterBonusStatCost,
    getWeaponLevelCost as getWuWaWeaponLevelCost,
} from "./wuwa/getLevelUpCosts";
import {
    getCharacterLevelCost as getZZZCharacterLevelCost,
    getCharacterSkillCost as getZZZCharacterSkillCost,
    getCharacterCoreSkillCost as getZZZCharacterCoreSkillCost,
    getWeaponLevelCost as getZZZWeaponLevelCost,
} from "./zzz/getLevelUpCosts";
import {
    getCharacterLevelCost as getEndfieldCharacterLevelCost,
    getCharacterSkillCost as getEndfieldCharacterSkillCost,
    getCharacterAttributeCost as getEndfieldCharacterAttributeCost,
    getCharacterTalentCost as getEndfieldCharacterTalentCost,
    getCharacterBaseSkillCost as getEndfieldCharacterBaseSkillCost,
    getCharacterOutfittingCost as getEndfieldCharacterOutfittingCost,
    getWeaponLevelCost as getEndfieldWeaponLevelCost,
} from "./endfield/getLevelUpCosts";

interface Costs {
    [tag: string]: (arg0: any) => { [key: string]: CostValue };
}

export const costs: GameData<Costs> = {
    genshin: {
        characterLevel: getGenshinCharacterLevelCost,
        characterSkill: getGenshinCharacterSkillCost,
        weaponLevel: getGenshinWeaponLevelCost,
    },
    hsr: {
        characterLevel: getHSRCharacterLevelCost,
        characterSkill: getHSRCharacterSkillCost,
        characterMemosprite: getHSRCharacterMemosprite,
        characterTraceMain: getHSRCharacterTraceMain,
        characterTraceSmall: getHSRCharacterTraceSmall,
        weaponLevel: getHSRWeaponLevelCost,
    },
    wuwa: {
        characterLevel: getWuWaCharacterLevelCost,
        characterSkill: getWuWaCharacterSkillCost,
        characterPassive: getWuWaCharacterPassiveCost,
        characterBonusStat: getWuWaCharacterBonusStatCost,
        weaponLevel: getWuWaWeaponLevelCost,
    },
    zzz: {
        characterLevel: getZZZCharacterLevelCost,
        characterSkill: getZZZCharacterSkillCost,
        characterCoreSkill: getZZZCharacterCoreSkillCost,
        weaponLevel: getZZZWeaponLevelCost,
    },
    uma: {},
    endfield: {
        characterLevel: getEndfieldCharacterLevelCost,
        characterSkill: getEndfieldCharacterSkillCost,
        characterAttribute: getEndfieldCharacterAttributeCost,
        characterTalent: getEndfieldCharacterTalentCost,
        characterBaseSkill: getEndfieldCharacterBaseSkillCost,
        characterOutfitting: getEndfieldCharacterOutfittingCost,
        weaponLevel: getEndfieldWeaponLevelCost,
    },
};

export function calculateCosts(costs: CostArray, start: number, stop: number) {
    return Object.values(costs).map((arr) =>
        arr.slice(start, stop).reduce((a, c) => a + c),
    );
}

```

### File: src\helpers\createBannerData.ts
```ts
import { Banner, BannerOption, BannerProps } from "@/types/banner";

export function createBannerData<
    T extends BannerOption,
    U extends BannerOption
>({
    id,
    name = "TBA",
    characters,
    weapons,
}: {
    id?: number;
    name?: string;
    characters: T[];
    weapons: U[];
}) {
    let data: BannerOption = {
        category: "characters",
        id: -1,
        name: name,
        displayName: name,
        rarity: 3,
        weaponType: "",
        url: "",
    };
    const character = characters.find(
        (char) => char.name === name || char.id === id
    );
    const weapon = weapons.find((wep) => wep.name === name || wep.id === id);
    if (character && weapon) {
        console.warn(`Two entries with ID ${id} were found`);
        return data;
    }

    if (character) {
        data.id = character.id;
        data.name = character.name;
        data.displayName = character.displayName || character.name;
        data.rarity = character.rarity;
        data.element = character.element;
        data.weaponType = character.weaponType;
        if (character.outfit) data.outfit = character.outfit;
        data.url = character.url;
    } else if (weapon) {
        data.category = "weapons";
        data.id = weapon.id;
        data.name = weapon.name;
        data.displayName = weapon.displayName || weapon.name;
        data.rarity = weapon.rarity;
        data.weaponType = weapon.weaponType;
        if (weapon.specialty) data.specialty = weapon.specialty;
        data.url = weapon.url;
    } else {
        name !== "TBA" && console.warn(`Could not find an entry with ID ${id}`);
    }
    return data;
}

export function createBannerOptions<
    T extends BannerOption,
    U extends BannerOption
>(banners: BannerProps, characters: T[], weapons: U[]) {
    const options: BannerOption[] = [];
    Object.values(banners).forEach((value) => {
        value.forEach((banner: Banner) => {
            banner.rateUps.forEach((item) => {
                if (item !== "TBA") {
                    options.push(
                        createBannerData({
                            id: typeof item === "number" ? item : undefined,
                            name: `${item}`,
                            characters,
                            weapons,
                        })
                    );
                }
            });
        });
    });
    return options.filter(
        (o1, index, arr) => arr.findIndex((o2) => o1.id === o2.id) === index
    );
}

```

### File: src\helpers\createBannerList.ts
```ts
// Type imports
import { Banner, BannerProps, BannerType } from "@/types/banner";
import { Game, Server } from "@/types";

export function getBannerData(
    banners: BannerProps,
    game: Game,
    server: Server
) {
    const res: BannerProps = {
        character: [],
        weapon: [],
    };
    Object.entries(banners).forEach(
        ([key, value]) =>
            (res[key as BannerType] = value.filter((banner: Banner) => {
                if (game === "uma" && server === "NA")
                    return banner.start !== "";
                else return banner;
            }))
    );
    return res;
}

```

### File: src\helpers\dataIcon.ts
```ts
import {
    GenshinWeaponSubStat,
    weaponSubStats as genshinWeaponSubStats,
} from "@/data/genshin/weaponStats";
import { formatWeaponStats, WuWaWeaponSubStat } from "@/data/wuwa/weaponStats";
import {
    ZZZWeaponSubStat,
    weaponSubStats as zzzWeaponSubStats,
} from "@/data/zzz/weaponStats";
import { sonataEffects } from "@/data/wuwa/sonataEffects";
import { AttributeDataKey, Game } from "@/types";
import { CharacterColors } from "@/types/character";
import { splitJoin } from "@/utils";

interface Props {
    game: Game;
    key: AttributeDataKey;
    value?: string | number | (string | number)[] | CharacterColors;
}

export function getDataIconURL({ game, key, value }: Props) {
    let src = "";
    let tooltip = "";
    if (game === "genshin") {
        if (key === "element" && value) {
            src = `genshin/elements/${value}`;
            tooltip = `${value}`;
        }
        if (key === "weaponType" && value) {
            src = `genshin/skills/Attack_${value}`;
            tooltip = `${value}`;
        }
        if (key === "subStat" && value) {
            src = `genshin/icons/stat-icons/${value}`;
            tooltip = `${
                genshinWeaponSubStats[value as GenshinWeaponSubStat].title
            }`;
        }
        if (key === "arkhe") {
            src = `genshin/tcg/icons/factions/${value}`;
            tooltip = `${value}`;
        }
    }
    if (game === "hsr") {
        if (key === "element" && value) {
            src = `hsr/elements/${value}`;
            tooltip = `${value}`;
        }
        if (key === "weaponType" && value) {
            src = `hsr/paths/${value}`;
            tooltip = `${value}`;
        }
    }
    if (game === "wuwa") {
        if (key === "element" && value) {
            src = `wuwa/icons/elements/${value}`;
            tooltip = `${value}`;
        }
        if (key === "weaponType" && value) {
            src = `wuwa/skills/Attack_${value}`;
            tooltip = `${value}`;
        }
        if (key === "subStat" && value) {
            src = `wuwa/icons/stat-icons/${value}`;
            tooltip = `${formatWeaponStats(value as WuWaWeaponSubStat)}`;
        }
        if (key === "sonata" && value) {
            src = `wuwa/sonata/${value}`;
            tooltip = `${
                sonataEffects.find((sonata) => sonata.id === value)
                    ?.displayName || "???"
            }`;
        }
    }
    if (game === "zzz") {
        if (key === "element" && value) {
            src = `zzz/elements/${value}`;
            tooltip = `${value}`;
        }
        if (key === "weaponType" && value) {
            src = `zzz/icons/specialties/${value}`;
            tooltip = `${value}`;
        }
        if (key === "attackType" && value) {
            src = `zzz/icons/attack-types/${value}`;
            tooltip = `${value}`;
        }
        if (key === "subStat" && value) {
            src = `zzz/icons/stat-icons/${value}`;
            tooltip = `${zzzWeaponSubStats[value as ZZZWeaponSubStat].title}`;
        }
    }
    if (game === "uma") {
        if (key === "specialty") {
            src = `uma/icons/specialties/${value}`;
            tooltip = `${value}`;
        }
    }
    if (game === "endfield") {
        if (key === "element" && value) {
            src = `endfield/elements/${value}`;
            tooltip = `${value}`;
        }
        if (key === "weaponType" && value) {
            src = `endfield/icons/weapons/${splitJoin(`${value}`)}`;
            tooltip = `${value}`;
        }
        if (key === "specialty" && value) {
            src = `endfield/classes/${value}`;
            tooltip = `${value}`;
        }
    }
    return { src, tooltip };
}

```

### File: src\helpers\dates.ts
```ts
import type { Game, Server } from "@/types";

export const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
] as const;

export type Month = (typeof months)[number];

export const days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
] as const;

export type Day = (typeof days)[number];

export const servers = {
    NA: "-5",
    EU: "+1",
    Asia: "+8",
};

function formatDate(date: string, offset: string) {
    return `${date
        .split(" ")
        .slice(0, 2)
        .join(" ")
        .replace(/-/g, "/")}${offset}`;
}

export default class DateObject {
    value: string;
    server: Server;
    game: Game | undefined;

    /**
     * @param value - A string representing a date.
     * The string must be formatted in the following way: `YYYY-MM-DD HH:MM:SS UTC+Z`.
     * @param server - The current server (NA / EU / Asia).
     * @param game - The current game.
     */
    constructor(value: string, server?: Server, game?: Game) {
        this.value = value;
        this.server = server || "NA";
        this.game = game || "genshin";
    }

    /**
     * @private
     * Creates a new Date object from the given input.
     */
    private createDateObject() {
        let dateObject;
        if (this.value) {
            if (this.value.includes("UTC")) {
                dateObject = new Date(
                    formatDate(this.value, `+${this.value.split("+")[1]}`)
                );
            } else {
                let offset = servers[this.server];
                if (this.game === "uma" && this.server === "Asia") {
                    offset = "-5";
                }
                dateObject = new Date(formatDate(this.value, offset));
            }
        } else {
            dateObject = new Date();
        }
        return dateObject;
    }

    /**
     * @private
     * Splits a Date object into an array.
     */
    private createDateArray() {
        // Must set locale to "en-US" to ensure proper formatting
        return this.createDateObject().toLocaleString("en-US").split(",");
    }

    /**
     * Returns the Date object.
     */
    get date() {
        return this.createDateObject();
    }

    /**
     * Returns the date in the `Month Day, Year` format.
     */
    get string() {
        const arr = this.createDateArray()[0].split("/");
        const month = months[Number(arr[0]) - 1];
        const day = parseInt(arr[1], 10).toString();
        const year = arr[2];
        return `${month} ${day}, ${year}`;
    }

    /**
     * Returns the timestamp of the date in the `HH:MM:SS` format.
     */
    get time() {
        const arr = this.createDateArray()[1].trim().split(" ");
        return `${arr[0].split(":").splice(0, 2).join(":")} ${arr[1]}`;
    }

    /**
     * Returns both the formatted date and time strings.
     */
    get timeString() {
        return `${this.string} ${this.time}`;
    }

    /**
     * Determines if the date is in the past, future, or today.
     * @returns
     * `-1` if the date is in the past.
     *
     * `0` if the date is today.
     *
     * `1` if the date is in the future.
     */
    get checkDate() {
        const date = this.createDateObject();
        const today = new Date();
        if (today > date) return -1;
        else if (today === date) return 0;
        else return 1;
    }

    /**
     * Returns true if today's date is between two given dates; otherwise, returns false.
     * @param start - Start date
     * @param end - End date
     */
    static inRange(start: Date, end: Date) {
        const today = new Date();
        return today >= start && today < end;
    }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
