---
id: github.com-bndw-wifi-card-644866f6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:35.680917
---

# KNOWLEDGE EXTRACT: github.com_bndw_wifi-card_644866f6
> **Extracted on:** 2026-04-01 12:42:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521975/github.com_bndw_wifi-card_644866f6

---

## File: `.dockerignore`
```
node_modules
```

## File: `.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `.prettierrc.json`
```json
{
  "trailingComma": "es5",
  "semi": true,
  "singleQuote": true
}
```

## File: `Dockerfile`
```
FROM node:22-alpine as builder

WORKDIR /tmp
COPY . .

RUN npx prettier --check ./src
RUN yarn && yarn build 

###
# production image
FROM nginx:stable-alpine
COPY --from=builder /tmp/build /usr/share/nginx/html
```

## File: `LICENSE.md`
```markdown
MIT License

Copyright (c) 2020 Ben Woodward

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `Makefile`
```
REPO ?= bndw/wifi-card
GITSHA=$(shell git rev-parse --short HEAD)
TAG_COMMIT=$(REPO):$(GITSHA)
TAG_LATEST=$(REPO):latest

all: dev

.PHONY: build
build:
	docker build -t $(TAG_LATEST) .

.PHONY: dev
dev:
	yarn
	yarn start

.PHONY: fmt
fmt:
	npx prettier --check ./src

.PHONY: fmt.write
fmt.write:
	npx prettier --write ./src

.PHONY: run
run:
	docker run --rm -p 8080:80 $(TAG_LATEST)

.PHONY: publish
publish:
	docker push $(TAG_LATEST)
	@docker tag $(TAG_LATEST) $(TAG_COMMIT)
	docker push $(TAG_COMMIT)
```

## File: `README.md`
```markdown
![ci](https://github.com/bndw/wifi-card/workflows/ci/badge.svg)

# <img width="32px" src="./public/images/wifi.png"> WiFi Card

https://wificard.io

Print a simple card with your WiFi login details. Tape it to the fridge, keep it in your wallet, hang on the wall for guests at home or in the hotel, etc.

<a href="https://wificard.io/">
   <img alt="wificard" src="https://user-images.githubusercontent.com/48166553/129261875-169841ab-e997-4596-af7f-ada0f68cd230.gif">
</a>

<a href="https://thiswebsitedoesnottrackyou.com/">
   <img width="402" alt="This website does not track you" src="https://user-images.githubusercontent.com/4248167/184430158-849d4b2c-de43-483f-86fe-0743b23bc40c.png">
</a>

## Running locally

Run the official Docker image on http://localhost:8080

```
make run
```

## Development

1. Make sure you have `yarn` installed
2. Run the live-reload server on http://localhost:3000
   ```
   make dev
   ```

This project uses [Prettier](https://prettier.io/) formatting. All pull requests must pass the automated lint checks before merging. Prettier format is run automatically as a pre-commit hook.

## Language Contribution Guide

We would love for you to contribute to different languages and help make it even better than it is today! As a language contributor, here are some steps we would like you to follow:

1. Add a translation to [`./src/translations.js`](./src/translations.js). Here's an example of the German translation:

   ```
   {
      id: 'de-DE',              // locale code
      name: 'German - Deutsch', // Display name in the format 'latinName - nativeName'
      rtl: false,               // Optional, true if this is a right-to-left language
      translation: {
         ...
      }
   }
   ```

2. Append an entry to the [Supported Languages](#supported-languages) table below.

## Supported Languages

| Language                     | Author Credit                                      |
| ---------------------------- | -------------------------------------------------- |
| Arabic                       | [Ahmed Tokyo](https://github.com/a-tokyo)          |
| Bangla                       | [Tarek Hasan](https://github.com/Tarek-Hasan)      |
| Catalan                      | [aniol](https://github.com/aniol)                  |
| Cantonese Simplified         | [ous50](https://github.com/ous50)                  |
| Chinese                      | [Baoyuantop](https://github.com/Baoyuantop)        |
| Chinese Traditional (Taiwan) | [Dxball](https://github.com/dxball)                |
| Danish                       | [dk90103](https://github.com/dk90103)              |
| Dutch                        | [wouterbrink](https://github.com/wouterbrink)      |
| English                      | [bndw](https://github.com/bndw)                    |
| Esperanto                    | [zeecho](https://github.com/zeecho)                |
| French                       | [Divlo](https://github.com/Divlo)                  |
| German                       | [devofthings](https://github.com/devofthings)      |
| German (Swiss)               | [NZehnder](https://github.com/NZehnder)            |
| Greek                        | [nautilus7](https://github.com/nautilus7)          |
| Hebrew                       | [Ido Bronfeld](https://github.com/HelloWorldIL)    |
| Hindi                        | [Pushpender](https://github.com/PushpenderSaini0)  |
| Hungarian                    | [munkacsimark](https://github.com/munkacsimark)    |
| Indonesia                    | [nyancodeid](https://github.com/nyancodeid)        |
| Italian                      | [Domenico Pascucci](https://github.com/pasmimmo)   |
| Japanese                     | [hatsu38](https://github.com/hatsu38)              |
| Korean                       | [Seungbin Oh](https://github.com/sboh1214)         |
| Malagasy                     | [mpilasy](https://github.com/mpilasy)              |
| Malay (Malaysia)             | [hh-shiung](https://github.com/hh-shiung)          |
| Norwegian                    | [tplive](https://github.com/tplive)                |
| Occitan                      | [ensag-dev](https://github.com/ensag-dev)          |
| Persian                      | [Ramin](https://github.com/raminr77)               |
| Polish                       | [olekstomek](https://github.com/olekstomek)        |
| Portuguese                   | [pedrorenan](https://github.com/pedrorenan)        |
| Portuguese (Brazil)          | [ismaelpereira](https://github.com/ismaelpereira)  |
| Punjabi                      | [phoenixgill34](https://github.com/phoenixgill34)  |
| Russian                      | [Teraskull](https://github.com/Teraskull)          |
| Serbian                      | [demanderbag](https://github.com/demanderbag)      |
| Slovak                       | [matejkubinec](https://github.com/matejkubinec)    |
| Spanish                      | [oscfdezdz](https://github.com/oscfdezdz)          |
| Swedish                      | [ddund](https://github.com/ddund)                  |
| Thai                         | [l2D](https://github.com/l2D)                      |
| Turkish                      | [Riza Ergun](https://github.com/rizaergun)         |
| Ukrainian                    | [Teraskull](https://github.com/Teraskull)          |
| Urdu                         | [mHassan11](https://github.com/mHassan11)          |
```

## File: `package.json`
```json
{
  "name": "wifi-card",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.2",
    "@testing-library/user-event": "^14.6.1",
    "evergreen-ui": "^7.1.9",
    "i18next": "^25.8.0",
    "i18next-browser-languagedetector": "^8.2.0",
    "qrcode.react": "^4.2.0",
    "react": "^19.2.3",
    "react-dom": "^19.2.3",
    "react-i18next": "^16.5.3",
    "react-scripts": "^5.0.1"
  },
  "devDependencies": {
    "husky": "^9.1.7",
    "prettier": "3.8.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "prepare": "husky install"
  },
  "eslintConfig": {
    "extends": "react-app"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "main": "index.js",
  "repository": "git@github.com:bndw/wifi-card.git",
  "author": "bndw <ben@bdw.to>",
  "license": "MIT"
}
```

## File: `public/index.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta name="description"
    content="Print a simple card with your WiFi login details. Tape it to the fridge, keep it in your wallet, etc." />
  <link rel="icon" href="./images/wifi.ico" />
  <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
  <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
  <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
  <title>WiFi Card</title>
</head>

<body>
  <noscript>You need to enable JavaScript to run this app. Feel free to view the
    <a href="https://github.com/bndw/wifi-card">source code</a>.</noscript>

  <div id="root"></div>
  <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  <script>
    // Internet Explorer 6-11
    const isIE = /*@cc_on!@*/ false || !!document.documentMode;

    if (isIE) {
      document.getElementById('root').innerHTML =
        'Internet Explorer is not supported. Download Firefox/Chrome/Opera.';
      document.body.style.fontSize = '50px';
    }
  </script>
</body>

</html>
```

## File: `public/manifest.json`
```json
{
  "short_name": "wifi-details",
  "name": "wifi-details",
  "icons": [
    {
      "src": "./images/wifi.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
```

## File: `public/robots.txt`
```
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:
```

## File: `src/App.js`
```javascript
import { Button, Heading, Link, Pane, Paragraph } from 'evergreen-ui';
import React, { useEffect, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import logo from '../src/images/wifi.png';
import { Settings } from './components/Settings';
import { WifiCard } from './components/WifiCard';
import './style.css';
import { Translations } from './translations';

function App() {
  const html = document.querySelector('html');

  const { t, i18n } = useTranslation();
  const firstLoad = useRef(true);
  const [settings, setSettings] = useState({
    ssid: '',
    password: '',
    encryptionMode: 'WPA',
    eapMethod: 'PWD',
    eapIdentity: '',
    hidePassword: false,
    hiddenSSID: false,
    portrait: false,
    additionalCards: 1,
    hideTip: false,
    lng: 'en-US',
  });

  const [errors, setErrors] = useState({
    ssidError: '',
    passwordError: '',
    eapIdentityError: '',
  });

  const htmlDirection = (languageID) => {
    languageID = languageID || i18n.language;
    const rtl = Translations.filter((t) => t.id === languageID)[0]?.rtl;
    return rtl ? 'rtl' : 'ltr';
  };

  const onChangeLanguage = (language) => {
    html.style.direction = htmlDirection(language);
    i18n.changeLanguage(language);

    setSettings({ ...settings, lng: language });
  };

  const onPrint = () => {
    if (!settings.ssid.length) {
      setErrors({
        ...errors,
        ssidError: t('wifi.alert.name'),
      });
      return;
    }
    if (settings.password.length < 8 && settings.encryptionMode === 'WPA') {
      setErrors({
        ...errors,
        passwordError: t('wifi.alert.password.length.8'),
      });
      return;
    }
    if (settings.password.length < 5 && settings.encryptionMode === 'WEP') {
      setErrors({
        ...errors,
        passwordError: t('wifi.alert.password.length.5'),
      });
      return;
    }
    if (
      settings.password.length < 1 &&
      settings.encryptionMode === 'WPA2-EAP'
    ) {
      setErrors({
        ...errors,
        passwordError: t('wifi.alert.password'),
      });
      return;
    }
    if (
      settings.eapIdentity.length < 1 &&
      settings.encryptionMode === 'WPA2-EAP'
    ) {
      setErrors({
        ...errors,
        eapIdentityError: t('wifi.alert.eapIdentity'),
      });
      return;
    }
    document.title = 'WiFi Card - ' + settings.ssid;
    window.print();
  };

  const onSSIDChange = (ssid) => {
    setErrors({ ...errors, ssidError: '' });
    setSettings({ ...settings, ssid });
  };
  const onPasswordChange = (password) => {
    setErrors({ ...errors, passwordError: '' });
    setSettings({ ...settings, password });
  };
  const onEncryptionModeChange = (encryptionMode) => {
    setErrors({ ...errors, passwordError: '' });
    setSettings({ ...settings, encryptionMode });
  };
  const onEapMethodChange = (eapMethod) => {
    setSettings({ ...settings, eapMethod });
  };
  const onEapIdentityChange = (eapIdentity) => {
    setErrors({ ...errors, eapIdentityError: '' });
    setSettings({ ...settings, eapIdentity });
  };
  const onOrientationChange = (portrait) => {
    setSettings({ ...settings, portrait });
  };
  const onHidePasswordChange = (hidePassword) => {
    setSettings({ ...settings, hidePassword });
  };
  const onHiddenSSIDChange = (hiddenSSID) => {
    setSettings({ ...settings, hiddenSSID });
  };
  const onAdditionalCardsChange = (additionalCardsStr) => {
    const amount = parseInt(additionalCardsStr);
    amount >= 1 && setSettings({ ...settings, additionalCards: amount });
  };
  const onHideTipChange = (hideTip) => {
    setSettings({ ...settings, hideTip });
  };
  const onFirstLoad = () => {
    html.style.direction = htmlDirection();
    firstLoad.current = false;
  };

  useEffect(() => {
    // Ensure the page direction is set properly on first load
    if (htmlDirection() === 'rtl') {
      html.style.direction = 'rtl';
    }
  }, []);

  return (
    <Pane>
      <Pane display="flex">
        <img alt="icon" src={logo} width="32" height="32" />
        <Heading size={900} paddingRight={16} paddingLeft={16}>
          {t('title')}
        </Heading>
      </Pane>
      <Pane>
        <Paragraph marginTop={12}>{t('desc.use')}</Paragraph>

        <Paragraph marginTop={12}>
          {t('desc.privacy')}{' '}
          <Link href="https://github.com/bndw/wifi-card">
            {t('desc.source')}
          </Link>
          .
        </Paragraph>
      </Pane>
      <Pane>
        <WifiCard
          settings={settings}
          ssidError={errors.ssidError}
          passwordError={errors.passwordError}
          eapIdentityError={errors.eapIdentityError}
          onSSIDChange={onSSIDChange}
          onEapIdentityChange={onEapIdentityChange}
          onPasswordChange={onPasswordChange}
        />
      </Pane>
      <Settings
        settings={settings}
        firstLoad={firstLoad}
        onFirstLoad={onFirstLoad}
        onLanguageChange={onChangeLanguage}
        onEncryptionModeChange={onEncryptionModeChange}
        onEapMethodChange={onEapMethodChange}
        onOrientationChange={onOrientationChange}
        onHidePasswordChange={onHidePasswordChange}
        onHiddenSSIDChange={onHiddenSSIDChange}
        onAdditionalCardsChange={onAdditionalCardsChange}
        onHideTipChange={onHideTipChange}
      />
      <Button
        id="print"
        appearance="primary"
        height={40}
        marginRight={16}
        onClick={onPrint}
      >
        {t('button.print')}
      </Button>
      <Pane id="print-area">
        {settings.additionalCards >= 1 &&
          [...Array(settings.additionalCards)].map((el, idx) => (
            <WifiCard
              keyid={idx}
              key={`card-nr-${idx}`}
              settings={settings}
              ssidError={errors.ssidError}
              passwordError={errors.passwordError}
              eapIdentityError={errors.eapIdentityError}
              onSSIDChange={onSSIDChange}
              onEapIdentityChange={onEapIdentityChange}
              onPasswordChange={onPasswordChange}
            />
          ))}
      </Pane>
    </Pane>
  );
}

export default App;
```

## File: `src/i18n.js`
```javascript
import i18n from 'i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import { initReactI18next } from 'react-i18next';
import { Translations } from './translations';

// i18n wants a single object in the following format:
// {
//   'en-US': {
//     translation: {
//       title: 'WiFi Card',,
//       ...
//     }
//   },
// }
const resources = Translations.reduce((obj, curr) => {
  obj[curr.id] = curr;
  return obj;
}, {});

i18n
  .use(initReactI18next)
  .use(LanguageDetector)
  .init({
    fallbackLng: 'en-US',
    resources,
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;
```

## File: `src/index.js`
```javascript
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './i18n';

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

## File: `src/style.css`
```css
body {
  margin: 0 auto;
  max-width: 500px;
  padding: 1em;
}
```

## File: `src/translations.js`
```javascript
export const Translations = [
  {
    id: 'en-US',
    name: 'English',
    translation: {
      title: 'WiFi Card',
      'desc.use':
        'Print a simple card with your WiFi login details. Tape it to the fridge, keep it in your wallet, etc.',
      'desc.privacy':
        'Your WiFi information is never sent to the server. No tracking, analytics, or fingerprinting are used on this website. View the',
      'desc.source': 'source code',
      'wifi.identity': 'Identity',
      'wifi.identity.placeholder': 'Username',
      'wifi.login': 'WiFi Login',
      'wifi.name': 'Network name',
      'wifi.name.hiddenSSID': 'Hidden SSID',
      'cards.additional': 'Number of cards to print',
      'cards.tip.hide': 'Hide tip (legend)',
      'wifi.name.placeholder': 'WiFi Network name',
      'wifi.password': 'Password',
      'wifi.password.placeholder': 'Password',
      'wifi.password.hide': 'Hide password',
      'wifi.password.encryption': 'Encryption',
      'wifi.password.encryption.none': 'None',
      'wifi.encryption.eapMethod': 'EAP method',
      'wifi.tip':
        "Point your phone's camera at the QR Code to connect automatically",
      'wifi.alert.name': 'Network name cannot be empty',
      'wifi.alert.password': 'Password cannot be empty',
      'wifi.alert.password.length.5':
        'Password must be at least 5 characters, or change the encryption to "None"',
      'wifi.alert.password.length.8':
        'Password must be at least 8 characters, or change the encryption to "None"',
      'wifi.alert.eapIdentity': 'Identity cannot be empty',
      'button.rotate': 'Rotate',
      'button.print': 'Print',
      select: 'Select Language',
    },
  },
  {
    id: 'he-IL',
    name: 'Hebrew - עברית',
    rtl: true,
    translation: {
      title: 'כרטיס WiFi',
      'desc.use':
        'הדפיסו כרטיס פשוט עם פרטי הכניסה שלכם לרשת ה-WiFi. הדביקו אותו למקרר, שמרו אותו בארנק וכו.',
      'desc.privacy':
        'פרטי ה WiFi שלכם לעולם לא נשלחים לשרת. אתר זה אינו עוקב, משתמש באנליטיקות או טביעות אצבע. צפה ב',
      'desc.source': 'קוד המקור',
      'wifi.identity': 'זהות',
      'wifi.identity.placeholder': 'שם משתמש',
      'wifi.login': 'פרטי WiFi',
      'wifi.name': 'שם רשת',
      'wifi.name.hiddenSSID': 'רשת נסתרת (SSID)',
      'cards.additional': 'מספר כרטיסים נוספים להדפסה',
      'cards.tip.hide': 'הסתרת טיפ (מקרא)',
      'wifi.name.placeholder': 'שם רשת WiFi',
      'wifi.password': 'סיסמה',
      'wifi.password.placeholder': 'סיסמה',
      'wifi.password.hide': 'הסתר סיסמה',
      'wifi.password.encryption': 'הצפנה',
      'wifi.password.encryption.none': 'None',
      'wifi.encryption.eapMethod': 'שיטת אימות EAP',
      'wifi.tip': 'כוונו את מצלמת הטלפון אל קוד ה-QR כדי להתחבר אוטומטית',
      'wifi.alert.name': 'שם רשת לא יכול להיות ריק',
      'wifi.alert.password': 'סיסמה לא יכולה להיות ריקה',
      'wifi.alert.password.length.5':
        'הסיסמה חייבת להיות באורך של לפחות 5 תווים, או שנה את ההצפנה ל "None"',
      'wifi.alert.password.length.8':
        'הסיסמה חייבת להיות באורך של לפחות 8 תווים, או שנה את ההצפנה ל "None"',
      'wifi.alert.eapIdentity': 'זהות לא יכולה להיות ריקה',
      'button.rotate': 'סובב',
      'button.print': 'הדפס',
      select: 'בחר שפה',
    },
  },
  {
    id: 'sv-SE',
    name: 'Swedish - Svenska',
    translation: {
      title: 'WiFi Kort',
      'desc.use':
        'Skriv ut ett enkelt kort med inloggningsuppgifter till ditt WiFI. Sätt upp det på kylskåpet eller ha det i din plånbok etc.',
      'desc.privacy':
        'Din WiFi information skickas aldrig till webbservern. Varken spårning, analys eller identifiering används på hemsidan. Se ',
      'desc.source': 'källkoden',
      'wifi.login': 'WiFi Inloggning',
      'wifi.name': 'Nätverksnamn',
      'wifi.name.hiddenSSID': 'Dolt SSID',
      'wifi.name.placeholder': 'WiFi Nätverksnamn',
      'wifi.password': 'Lösenord',
      'wifi.password.placeholder': 'Lösenord',
      'wifi.password.hide': 'Dölj lösenordet',
      'wifi.password.encryption': 'Kryptering',
      'wifi.password.encryption.none': 'Ingen',
      'wifi.tip':
        'Peka din telefons kamera mot QR-koden för att ansluta automatiskt',
      'wifi.alert.name': 'Nätverksnamn måste fyllas i',
      'wifi.alert.password.length.5':
        'Lösenordet måste bestå av minst 5 tecken eller ändra kryptering till "Ingen"',
      'wifi.alert.password.length.8':
        'Lösenordet måste bestå av minst 8 tecken eller ändra kryptering till "Ingen"',
      'button.rotate': 'Rotera',
      'button.print': 'Skriv ut',
      select: 'Välj språk',
    },
  },
  {
    id: 'no-NB',
    name: 'Norwegian - Norsk',
    translation: {
      title: 'WiFi Kort',
      'desc.use':
        'Skriver ut et enkelt kort med dine Wifi innloggingsdetaljer. Sett det på kjøleskapet, ha det i lommeboka el. lign.',
      'desc.privacy':
        'Din wifi-informasjon blir aldri sendt til våre servere. Ingen sporing, analyse eller identifisering brukes på dette nettstedet. Se vår',
      'desc.source': 'kildekode',
      'wifi.login': 'WiFi Innlogging',
      'wifi.name': 'Nettverksnavn',
      'wifi.name.hiddenSSID': 'Skjult SSID',
      'wifi.name.placeholder': 'WiFi Nettverksnavn',
      'wifi.password': 'Passord',
      'wifi.password.placeholder': 'Passord',
      'wifi.password.hide': 'Skjul passordfeltet',
      'wifi.password.encryption': 'Kryptering',
      'wifi.password.encryption.none': 'Ingen',
      'wifi.tip':
        'Pek telefonens kamera mot QR koden for å koble til automatisk',
      'wifi.alert.name': 'Nettverksnavnet kan ikke være tomt',
      'wifi.alert.password.length.5':
        'Passordet må være minst 5 karakterer, eller endre kryptering til "Ingen"',
      'wifi.alert.password.length.8':
        'Passordet må være minst 8 karakterer, eller endre kryptering til "Ingen"',
      'button.rotate': 'Roter',
      'button.print': 'Skriv ut',
      select: 'Velg språk',
    },
  },
  {
    id: 'nl-NL',
    name: 'Dutch - Nederlands',
    translation: {
      title: 'WiFi-Kaart',
      'desc.use':
        'Print een eenvoudige kaart met uw WiFi-inloggegevens. Plak het op je koelkast, stop het in je portemonnee, etc.',
      'desc.privacy':
        'Je WiFi-informatie wordt nooit naar de server verzonden. Tracking, analytics of fingerprinting wordt niet gebruikt op deze website. Bekijk de',
      'desc.source': 'broncode',
      'wifi.login': 'WiFi-login',
      'wifi.name': 'Netwerknaam',
      'wifi.name.placeholder': 'WiFi-netwerknaam',
      'wifi.password': 'Wachtwoord',
      'wifi.password.placeholder': 'Wachtwoord',
      'wifi.password.hide': 'Verberg wachtwoord',
      'wifi.name.hiddenSSID': 'Verborgen SSID',
      'wifi.password.encryption': 'Encryptie',
      'wifi.password.encryption.none': 'Geen',
      'wifi.tip':
        'Wijs met de camera van je telefoon naar de QR code om automatisch verbinding te maken',
      'wifi.alert.name': 'Netwerknaam kan niet leeg zijn',
      'wifi.alert.password.length.5':
        'Wachtwoord moet ten minste 5 tekens bevatten, of verander de encryptie naar "Geen"',
      'wifi.alert.password.length.8':
        'Wachtwoord moet ten minste 8 tekens bevatten, of verander de encryptie naar "Geen"',
      'button.rotate': 'Draai',
      'button.print': 'Print',
      select: 'Selecteer Taal',
    },
  },
  {
    id: 'zh-CN',
    name: 'Simplified Chinese - 简体中文',
    translation: {
      title: 'Wi-Fi 连接卡',
      'desc.use':
        '打印一张带有 Wi-Fi 详细信息的登录卡片，把它贴到冰箱上、放到你的钱包里...',
      'desc.privacy':
        '您的 WiFi 信息永远不会发送到服务端。本网站不使用追踪、分析或指纹识别。查看',
      'desc.source': '源码',
      'cards.additional': '额外打印卡片数量',
      'cards.tip.hide': '隐藏提示（图例）',
      'wifi.identity': '身份',
      'wifi.identity.placeholder': '用户名',
      'wifi.login': '连接 WiFi',
      'wifi.name': '网络名称',
      'wifi.name.hiddenSSID': '隐藏 SSID',
      'wifi.name.placeholder': 'WiFi 网络名称',
      'wifi.password': '密码',
      'wifi.password.placeholder': '密码',
      'wifi.password.hide': '隐藏密码',
      'wifi.password.encryption': '加密',
      'wifi.password.encryption.none': '无',
      'wifi.encryption.eapMethod': 'EAP 加密方式',
      'wifi.tip': '将手机摄像头对准二维码即可自动连接',
      'wifi.alert.name': '网络名称不能为空',
      'wifi.alert.password.length.5':
        '密码必须至少为 5 个字符，或将加密更改为“无”',
      'wifi.alert.password.length.8':
        '密码必须至少为 8 个字符，或将加密更改为“无”',
      'button.rotate': '翻转',
      'button.print': '打印',
      select: '选择语言',
    },
  },
  {
    id: 'zh-HK',
    name: 'Traditional Chinese - 繁體中文 香港',
    translation: {
      title: 'Wi-Fi 連接咭',
      'desc.use':
        '打印一張 Wi-Fi 詳細資料嘅連接卡，你可以將佢癡喺雪櫃上面、放喺銀包入面... ',
      'desc.privacy':
        '你嘅 Wi-Fi 資料永遠唔會傳送去網站伺服器。呢個網站唔會使用任何追蹤、分析或者裝置指紋辨識。',
      'desc.source': '撳呢度睇源代碼',
      'cards.additional': '要打印幾多張 Wi-Fi 卡片？',
      'cards.tip.hide': '隱藏提示（圖例）',
      'wifi.login': '連接 Wi-Fi',
      'wifi.name': '網絡名稱',
      'wifi.name.hiddenSSID': '隐藏 SSID',
      'wifi.name.placeholder': 'Wi-Fi 網絡名稱',
      'wifi.password': '密碼',
      'wifi.password.placeholder': '密碼',
      'wifi.password.hide': '隐藏密码',
      'wifi.password.encryption': '加密',
      'wifi.password.encryption.none': '没有任何',
      'wifi.tip': '打開相機指住嗰QR Code就可以連接 WiFi',
      'wifi.alert.name': '唔可以留空網絡名稱',
      'wifi.alert.password.length.5':
        '密碼必須至少有 5 个字串，你亦都可以将加密方式更改为“没有任何”',
      'wifi.alert.password.length.8':
        '密碼必須至少有 8 个字串，你亦都可以将加密方式更改为“没有任何”',
      'button.rotate': '翻轉',
      'button.print': '打印',
      select: '選擇語言',
    },
  },
  {
    id: 'yue-CN',
    name: 'Simplified Cantonese - 简体粤语',
    translation: {
      title: 'Wi-Fi 连接咭',
      'desc.use':
        '打印一张带有 Wi-Fi 详细信息嘅连接咭，你可以将佢黐喺冰箱上面，或者放喺银包入面...',
      'desc.privacy':
        '你嘅 Wi-Fi 信息永远不会发送到服务端。本网站不使用追踪、分析或指纹识别。',
      'desc.source': '喺度睇源代码',
      'cards.additional': '要*多打印*多少张 Wi-Fi 卡片？',
      'cards.tip.hide': '隐藏提示（图例）',
      'wifi.identity': '身份',
      'wifi.identity.placeholder': '用户名',
      'wifi.login': '连接 Wi-Fi',
      'wifi.name': '网络名称',
      'wifi.name.hiddenSSID': '呢个 Wi-Fi 嘅名收埋起身咗 ',
      'wifi.name.placeholder': 'Wi-Fi 网络名称',
      'wifi.password': '密码',
      'wifi.password.placeholder': '密码',
      'wifi.password.hide': '唔显示明文密码',
      'wifi.password.encryption': '加密',
      'wifi.password.encryption.none': '冇',
      'wifi.encryption.eapMethod': 'EAP 加密方式',
      'wifi.tip': '打开摄像头指住个二维码就可以连上呢个 Wi-Fi',
      'wifi.alert.name': '网络名称唔可以为空',
      'wifi.alert.password.length.5':
        '密码必须至少有 5 个字符，你亦可以将加密方式更改为“冇”',
      'wifi.alert.password.length.8':
        '密码必须至少有 8 个字符，你亦可以将加密方式更改为“冇”',
      'button.rotate': '翻转方向',
      'button.print': '打印',
      select: '选择语言',
    },
  },
  {
    id: 'zh-TW',
    name: 'Traditional Chinese - 繁體中文 台灣',
    translation: {
      title: 'Wi-Fi Card',
      'desc.use':
        '列印一張含有 Wi-Fi 連接資訊的卡片，將它貼在冰箱、放在你的錢包裡... ',
      'desc.privacy':
        '您的 Wi-Fi 訊息永遠不會被送到伺服器。本網站不使用追蹤、分析或指紋識別。查看',
      'desc.source': '原始碼',
      'cards.additional': '额外列印卡片數量',
      'cards.tip.hide': '隱藏提示（圖例）',
      'wifi.login': '連接 WiFi',
      'wifi.name': '網路名稱',
      'wifi.name.hiddenSSID': '隱藏 SSID',
      'wifi.name.placeholder': 'WiFi 網路名稱',
      'wifi.password': '密碼',
      'wifi.password.placeholder': '密碼',
      'wifi.password.hide': '隱藏密碼',
      'wifi.password.encryption': '加密',
      'wifi.password.encryption.none': '無',
      'wifi.tip': '將手機相機對準 QR Code 即可自動連接 WiFi',
      'wifi.alert.name': '網路名稱不可以留空',
      'wifi.alert.password.length.5':
        '密碼至少為 5 個字元以上，或將加密改為"無"',
      'wifi.alert.password.length.8':
        '密碼至少為 8 個字元以上，或將加密改為"無"',
      'button.rotate': '翻轉',
      'button.print': '列印',
      select: '選擇語言',
    },
  },
  {
    id: 'es',
    name: 'Spanish - Español',
    translation: {
      title: 'Tarjeta WiFi',
      'desc.use':
        'Imprima una sencilla tarjeta con sus datos de acceso a la WiFi. Pégela en la nevera, guárdela en la cartera, etc.',
      'desc.privacy':
        'Su información WiFi nunca se envía al servidor. En este sitio web no se utiliza ningún tipo de rastreo, análisis o huella digital. Ver el',
      'desc.source': 'código fuente',
      'wifi.login': 'Acceso WiFi',
      'wifi.name': 'Nombre de la red',
      'wifi.name.placeholder': 'Nombre de la red WiFi',
      'wifi.password': 'Contraseña',
      'wifi.password.placeholder': 'Contraseña',
      'wifi.name.hiddenSSID': 'SSID oculta',
      'wifi.password.hide': 'Ocultar contraseña',
      'wifi.password.encryption': 'Cifrado',
      'wifi.password.encryption.none': 'Ninguno',
      'wifi.tip':
        'Apunte la cámara de su teléfono al código QR para conectarse automáticamente',
      'wifi.alert.name': 'El nombre de la red no puede estar vacío',
      'wifi.alert.password.length.5':
        'La contraseña debe tener al menos 5 caracteres, o cambiar el cifrado a "Ninguno"',
      'wifi.alert.password.length.8':
        'La contraseña debe tener al menos 8 caracteres, o cambiar el cifrado a "Ninguno"',
      'button.rotate': 'Girar',
      'button.print': 'Imprimir',
      select: 'Seleccionar idioma',
    },
  },
  {
    id: 'pt',
    name: 'Portuguese - Português',
    translation: {
      title: 'Cartão WiFi',
      'desc.use':
        'Imprima um cartão com detalhes de autenticação da sua rede WiFi. Cole no frigorifico, na sala, etc.',
      'desc.privacy':
        'As informações da sua rede WiFi não são enviadas para o servidor. Nenhum dado é recolhido pelo website. Veja o',
      'desc.source': 'código fonte',
      'wifi.login': 'Autenticação WiFi ',
      'wifi.name': 'Nome da Rede',
      'wifi.name.placeholder': 'Nome da sua rede WiFi',
      'wifi.password': 'Senha',
      'wifi.password.placeholder': 'Senha da sua rede WiFi',
      'wifi.password.hide': 'Esconder o campo de senha antes da impressão',
      'wifi.name.hiddenSSID': 'Rede oculta',
      'wifi.password.encryption': 'Criptografia',
      'wifi.password.encryption.none': 'Nenhum',
      'wifi.tip':
        'Abra a aplicação da câmera no seu telemóvel e aponte para o QR Code para se ligar automaticamente.',
      'wifi.alert.name': 'O Nome da rede não pode ficar em branco',
      'wifi.alert.password.length.5':
        'A senha precisa ter no mínimo 5 dígitos, ou alterar a criptografia para "Nenhum"',
      'wifi.alert.password.length.8':
        'A senha precisa ter no mínimo 8 dígitos, ou alterar a criptografia para "Nenhum"',
      'button.rotate': 'Girar',
      'button.print': 'Imprimir',
      select: 'Selecionar Idioma',
    },
  },
  {
    id: 'ja',
    name: 'Japanese - 日本語',
    translation: {
      title: 'WiFi ログイン',
      'desc.use':
        'WiFiのログイン情報を記載したシンプルなカードを印刷します。冷蔵庫に貼ったり、お財布に入れたりしてください。',
      'desc.privacy':
        'お客様のWiFi情報がサーバーに送信されることはありません。このウェブサイトでは、トラッキング、アナリティクス、フィンガープリントは使用されていません。確認する',
      'desc.source': 'ソースコード',
      'wifi.login': ' WiFi ログイン',
      'wifi.name': 'ネットワーク名',
      'wifi.name.hiddenSSID': '隠しSSID',
      'wifi.name.placeholder': 'WiFi ネットワーク名',
      'wifi.password': 'パスワード',
      'wifi.password.placeholder': 'パスワード',
      'wifi.password.hide': 'パスワードを非表示にする',
      'wifi.password.encryption': '暗号化',
      'wifi.password.encryption.none': 'なし',
      'wifi.tip': '携帯電話のカメラをQRコードに向けると、自動的に接続されます',
      'wifi.alert.name': 'ネットワーク名は空にできません',
      'wifi.alert.password.length.5':
        'パスワードを5文字以上にするか、暗号化を「なし」に変更してください',
      'wifi.alert.password.length.8':
        'パスワードを8文字以上にするか、暗号化を「なし」に変更してください',
      'button.rotate': '回転する',
      'button.print': '印刷する',
      select: '言語を選択',
    },
  },
  {
    id: 'ru-RU',
    name: 'Russian - Русский',
    translation: {
      title: 'Карта WiFi',
      'desc.use':
        'Распечатайте простую карточку с данными для входа в WiFi. Приклейте ее на холодильник, храните в бумажнике и т.д.',
      'desc.privacy':
        'Информация о вашем WiFi никогда не отправляется на сервер. На этом сайте не используется отслеживание, аналитика или цифровые отпечатки. Посмотреть',
      'desc.source': 'исходный код',
      'wifi.login': 'Вход в WiFi',
      'wifi.name': 'Название сети',
      'wifi.name.hiddenSSID': 'Скрытый SSID',
      'wifi.name.placeholder': 'Название сети WiFi',
      'wifi.password': 'Пароль',
      'wifi.password.placeholder': 'Пароль',
      'wifi.password.hide': 'Скрыть поле пароля',
      'wifi.password.encryption': 'Шифрование',
      'wifi.password.encryption.none': 'Нет',
      'wifi.tip':
        'Наведите камеру телефона на QR-код для автоматического подключения',
      'wifi.alert.name': 'Название сети не может быть пустым',
      'wifi.alert.password.length.5':
        'Пароль должен состоять не менее чем из 5 символов, в противном случае измените шифрование на "Нет"',
      'wifi.alert.password.length.8':
        'Пароль должен состоять не менее чем из 8 символов, в противном случае измените шифрование на "Нет"',
      'button.rotate': 'Повернуть',
      'button.print': 'Распечатать',
      select: 'Выбор языка',
    },
  },
  {
    id: 'fa-IR',
    name: 'Persian Iran - فارسی',
    rtl: true,
    translation: {
      title: 'کارت WiFi',
      'desc.use':
        'توسط اطلاعات شبکه WiFi خود یک کارت ساده چاپ کنید و آن را به یخچال بچسبانید و یا در کیف پول خود نگه دارید.',
      'desc.privacy':
        'اطلاعات شبکه شما هرگز به سرور ارسال نمی‌شود و هیچگونه ردیابی، آنالیز و یا تحلیل در این وب سایت انجام نمی‌شود. مشاهده ',
      'desc.source': 'سورس کد',
      'wifi.login': 'اتصال به شبکه WiFi',
      'wifi.name': 'نام شبکه',
      'wifi.name.placeholder': 'نام شبکه خود را وارد کنید',
      'wifi.password': 'رمز‌عبور',
      'wifi.password.placeholder': 'رمز‌عبور شبکه خود را وارد کنید',
      'wifi.password.hide': 'رمز‌عبور را بعد از چاپ کارت مخفی کن.',
      'wifi.password.encryption': 'رمزنگاری',
      'wifi.password.encryption.none': 'هیچ یک',
      'wifi.tip':
        'دوربین تلفن خود را روی تصویر (QR Code) گرفته تا به صورت خودکار به شبکه متصل شوید.',
      'wifi.alert.name': 'اسم شبکه شما نباید خالی باشد.',
      'wifi.alert.password.length.5': 'رمز‌عبور باید حداقل ۵ حرف داشته باشد.',
      'wifi.alert.password.8': 'رمز‌عبور باید حداقل ۸ حرف داشته باشد.',
      'button.rotate': 'چرخاندن',
      'button.print': 'چاپ',
      select: 'انتخاب زبان',
    },
  },
  {
    id: 'uk-UA',
    name: 'Ukrainian - Українська',
    translation: {
      title: 'Карта WiFi',
      'desc.use':
        'Роздрукуйте просту картку з даними для входу в WiFi. Приклейте її на холодильник, зберігайте в гаманці і т.д.',
      'desc.privacy':
        'Інформація про ваш WiFi ніколи не відправляється на сервер. На цьому сайті не використовується відстеження, аналітика або цифрові відбитки. Переглянути',
      'desc.source': 'вихідний код',
      'wifi.login': 'Вхід в WiFi',
      'wifi.name': 'Назва мережі',
      'wifi.name.hiddenSSID': 'Прихований SSID',
      'wifi.name.placeholder': 'Назва мережі WiFi',
      'wifi.password': 'Пароль',
      'wifi.password.placeholder': 'Пароль',
      'wifi.password.hide': 'Приховати поле пароля',
      'wifi.password.encryption': 'Шифрування',
      'wifi.password.encryption.none': 'Немає',
      'wifi.tip':
        'Наведіть камеру телефону на QR-код, щоб автоматично підключитися',
      'wifi.alert.name': 'Назва мережі не може бути порожньою',
      'wifi.alert.password.length.5':
        'Пароль повинен складатися не менше ніж з 5 символів, в іншому випадку змініть шифрування на "Немає"',
      'wifi.alert.password.length.8':
        'Пароль повинен складатися не менше ніж з 8 символів, в іншому випадку змініть шифрування на "Немає"',
      'button.rotate': 'Повернути',
      'button.print': 'Друкувати',
      select: 'Вибір мови',
    },
  },
  {
    id: 'de-DE',
    name: 'German - Deutsch',
    translation: {
      title: 'WLAN-Karte',
      'desc.use':
        'Druck dir eine simple Karte mit deinen WLAN-Zugangsdaten aus. Klebe sie an deinen Kühlschrank, behalte sie in deinem Portemonnaie, etc.',
      'desc.privacy':
        'Deine Zugangsdaten werden niemals zum Server gesendet. Es gibt kein Tracking, Fingerprinting und auch keine Analytics auf dieser Website. Hier geht es zum',
      'desc.source': 'Quellcode',
      'wifi.identity': 'Identität',
      'wifi.identity.placeholder': 'Nutzername',
      'wifi.login': 'WLAN-Zugangsdaten',
      'wifi.name': 'WLAN-Netzwerkname (SSID)',
      'wifi.name.placeholder': 'WLAN-Netzwerkname (SSID)',
      'wifi.password': 'Passwort',
      'wifi.password.placeholder': 'Passwort',
      'wifi.password.hide': 'Passwort verstecken',
      'wifi.name.hiddenSSID': 'Versteckte SSID',
      'cards.additional': 'Anzahl',
      'cards.tip.hide': 'Hinweis verstecken (Legende)',
      'wifi.password.encryption': 'Verschlüsselung',
      'wifi.password.encryption.none': 'Keine',
      'wifi.encryption.eapMethod': 'EAP-Methode',
      'wifi.tip':
        'Zeige mit der Kamera deines Handys auf den QR-Code, um automatisch eine Verbindung herzustellen',
      'wifi.alert.name': 'Der Netzwerkname darf nicht leer sein',
      'wifi.alert.password': 'Das Passwort darf nicht leer sein',
      'wifi.alert.password.length.5':
        'Das Passwort muss mindestends 5 Zeichen lang sein, oder stelle die Verschlüsselung auf "Keine"',
      'wifi.alert.password.8':
        'Das Passwort muss mindestends 8 Zeichen lang sein, oder stelle die Verschlüsselung auf "Keine"',
      'wifi.alert.eapIdentity': 'Die Identität darf nicht leer sein',
      'button.rotate': 'Drehen',
      'button.print': 'Drucken',
      select: 'Sprache auswählen',
    },
  },
  {
    id: 'de-CH',
    name: 'German - Schwizerdütsch',
    translation: {
      title: 'simple.WiFi Card Creator',
      'desc.use':
        'Sie chönd met dem Tool en eifachi Charte mit ehrene WLAN-Date erstelle. Verwänded Sie die, om eifach ehres interne WLAN unter de Metarbeiter zteile oder om es GASCHT-WLAN mit em Chond zteile.',
      'desc.private': 'Dini Zugegangsdate werded nie zom Server gsändet.',
      'wifi.identity': 'Identität',
      'wifi.identity.placeholder': 'Notzername',
      'wifi.login': 'WLAN-Zugangsdate',
      'wifi.name': 'WLAN-Netzwärchname',
      'wifi.name.placeholder': 'WLAN-Netzwärchname',
      'wifi.password': 'Passwort',
      'wifi.password.placeholder': 'Passwort',
      'wifi.password.hide': 'Passwort verstecke',
      'wifi.name.hiddenSSID': 'Versteckti SSID',
      'wifi.password.encryption': 'Verschlösselig',
      'wifi.password.encryption.none': 'Keini',
      'wifi.encryption.eapMethod': 'EAP Methode',
      'wifi.tip':
        'Zeig mit dinere Kamera vom Handys auf de QR-Code, um automatisch en Verbindung herzstelle',
      'wifi.alert.name': 'De Netzwerkname dörf ned leer sii',
      'wifi.alert.password': 'Das Passwort dörf ned leer sii',
      'wifi.alert.password.length.5':
        'Das Passwort muss mendestends 5 Zeiche lang sii, oder stell d Verschlösselig auf "Keini"',
      'wifi.alert.password.8':
        'Das Passwort muss mindestends 8 Zeichen lang sii, oder stell d Verschlösselig auf "Keini"',
      'wifi.alert.eapIdentity': 'Die Identität darf ned leer sii',
      'button.rotate': 'Dreie',
      'button.print': 'Drocke',
      select: 'Sprach uswähle',
    },
  },
  {
    id: 'el-GR',
    name: 'Greek - Hellenic',
    translation: {
      title: 'WiFi Card',
      'desc.use':
        'Εκτυπώστε μια απλή κάρτα με τις πληροφορίες πρόσβασης στο WiFi δίκτυό σας. Κολλήστε την στο ψυγείο ή βάλτε τη στο πορτοφόλι σας, κτλ.',
      'desc.privacy':
        'Οι πληροφορίες που σχετίζονται με το δίκτυο WiFi δεν αποστέλλονται στον διακομιστή. Καμιά ιχνηλάτηση, στατιστική ανάλυση ή ταυτοποίηση δεν πραγματοποιείται από αυτή την ιστοσελίδα. Δείτε τον',
      'desc.source': 'πηγαίο κώδικα',
      'wifi.identity': 'Ταυτότητα',
      'wifi.identity.placeholder': 'όνομα χρήστη',
      'wifi.login': 'Πληροφορίες WiFi',
      'wifi.name': 'Όνομα δικτύου',
      'wifi.name.hiddenSSID': 'Κρυφό SSID',
      'wifi.name.placeholder': 'όνομα δικτύου',
      'wifi.password': 'Κωδικός πρόσβασης',
      'wifi.password.placeholder': 'κωδικός πρόσβασης',
      'wifi.password.hide': 'Απόκρυψη κωδικού πρόσβασης',
      'wifi.password.encryption': 'Κρυπτογράφηση',
      'wifi.password.encryption.none': 'Καμία',
      'wifi.encryption.eapMethod': 'Μέθοδος EAP',
      'wifi.tip':
        'Στρέψτε την κάμερα του κινητού σας προς τον κώδικα QR για να συνδεθείτε αυτόματα',
      'wifi.alert.name': 'Το όνομα δικτύου δεν μπορεί να είναι κενό',
      'wifi.alert.password': 'Ο κωδικός πρόσβασης δεν μπορεί να είναι κενός',
      'wifi.alert.password.length.5':
        'Ο κωδικός πρόσβασης πρέπει να αποτελείται από τουλάχιστον 5 χαρακτήρες, διαφορετικά αλλάξτε την κρυπτογράφηση σε "Καμία"',
      'wifi.alert.password.length.8':
        'Ο κωδικός πρόσβασης πρέπει να αποτελείται από τουλάχιστον 8 χαρακτήρες, διαφορετικά αλλάξτε την κρυπτογράφηση σε "Καμία"',
      'wifi.alert.eapIdentity': 'Η ταυτότητα δεν μπορεί να είναι κενή.',
      'button.rotate': 'Περιστροφή',
      'button.print': 'Εκτύπωση',
      select: 'Επιλέξτε γλώσσα',
    },
  },
  {
    id: 'pl-PL',
    name: 'Polish - Polski',
    translation: {
      title: 'Karta WiFi',
      'desc.use':
        'Wydrukuj prostą kartę z danymi logowania do sieci Wi-Fi. Przyklej go do lodówki, trzymaj w portfelu, itp.',
      'desc.privacy':
        'Twoje informacje o Wi-Fi nigdy nie są wysyłane na serwer. Na tej stronie nie stosuje się śledzenia, analiz ani odcisków palców. Zobacz',
      'desc.source': 'kod źródłowy',
      'wifi.login': 'Logowanie do WiFi',
      'wifi.size': 'Rozmiar',
      'wifi.size.small': 'Mały',
      'wifi.size.medium': 'Średni',
      'wifi.size.large': 'Duży',
      'wifi.name': 'Nazwa sieci',
      'wifi.name.hiddenSSID': 'Ukryj SSID sieci WiFi',
      'wifi.name.placeholder': 'Nazwa sieci WiFi',
      'wifi.password': 'Hasło',
      'wifi.password.placeholder': 'Hasło',
      'wifi.password.hide': 'Ukryj pole hasła przed wydrukowaniem',
      'wifi.password.encryption': 'Szyfrowanie',
      'wifi.password.encryption.none': 'Brak',
      'wifi.tip':
        'Skieruj aparat telefonu na kod QR, aby połączyć się automatycznie',
      'wifi.alert.name': 'Nazwa sieci nie może być pusta',
      'wifi.alert.password.length.5':
        'Hasło musi mieć co najmniej 5 znaków lub zmień szyfrowanie na „Brak”',
      'wifi.alert.password.8':
        'Hasło musi mieć co najmniej 8 znaków lub zmień szyfrowanie na „Brak”',
      'button.rotate': 'Obróć',
      'button.print': 'Drukuj',
      select: 'Wybierz język',
    },
  },
  {
    id: 'fr-FR',
    name: 'French - Français',
    translation: {
      title: 'Carte Wi-Fi',
      'desc.use':
        'Imprimez une carte simple avec vos informations de connexion Wi-Fi. Collez-la sur le réfrigérateur, gardez-la dans votre portefeuille, etc.',
      'desc.privacy':
        'Vos informations Wi-Fi ne sont jamais envoyées au serveur. Aucun suivi, analyse ou prise empreinte digitale ne sont utilisés sur ce site Web. Voir le',
      'desc.source': 'code source',
      'wifi.login': 'Connexion Wi-Fi',
      'wifi.name': 'Nom du réseau',
      'wifi.name.placeholder': 'Nom du réseau Wi-Fi',
      'wifi.name.hiddenSSID': 'SSID masqué',
      'cards.additional': 'Nombre de cartes a imprimer',
      'cards.tip.hide': 'Masquer la légende',
      'wifi.password': 'Mot de passe',
      'wifi.password.placeholder': 'Mot de passe',
      'wifi.password.hide': 'Masquer le mot de passe',
      'wifi.password.encryption': 'Chiffrement',
      'wifi.password.encryption.none': 'Aucun',
      'wifi.tip':
        "Dirigez l'appareil photo de votre téléphone vers le QR code pour vous connecter automatiquement",
      'wifi.alert.name': 'Le nom du réseau ne peut pas être vide',
      'wifi.alert.password.length.5':
        'Le mot de passe doit au moins faire 5 caractères, ou changez le chiffrement en "Aucun"',
      'wifi.alert.password.8':
        'Le mot de passe doit au moins faire 8 caractères, ou changez le chiffrement en "Aucun"',
      'button.rotate': 'Pivoter',
      'button.print': 'Imprimer',
      select: 'Choisir la langue',
    },
  },
  {
    id: 'oc',
    name: 'Occitan',
    translation: {
      title: 'Carta WiFi',
      'desc.use':
        'Imprimissètz una carta simpla amb vòstras informacions de connexion WiFi. Pegatz-la al refregidor, gardatz-la al pòrtafuèlha, etc.',
      'desc.privacy':
        "Vòstras informacions WiFi son pas jamai enviadas al servidor. Cap de seguiment, d'analisi o de generacion d'emprenta numerica son pas realizats sus aqueste site Web. Veire lo",
      'desc.source': 'còdi font',
      'wifi.identity': 'Identitat',
      'wifi.identity.placeholder': 'Nom d’utilizaire',
      'wifi.login': 'Connexion Wi-Fi',
      'wifi.name': 'Nom de la ret',
      'wifi.name.hiddenSSID': 'SSID amagat',
      'cards.additional': 'Carta suplementàrias d’imprimir',
      'cards.tip.hide': 'Rescondre astúcia (legenda)',
      'wifi.name.placeholder': 'Nom de la ret WiFi',
      'wifi.password': 'Senhal',
      'wifi.password.placeholder': 'Senhal',
      'wifi.password.hide': 'Rescondre lo senhal',
      'wifi.password.encryption': 'Chiframent',
      'wifi.password.encryption.none': 'Cap',
      'wifi.encryption.eapMethod': 'Metòde EAP',
      'wifi.tip':
        'Viratz vòstre aparelh fòto cap al còdi QR per vos connectar automaticament',
      'wifi.alert.name': 'Lo nom de la ret pòt pas èsser void',
      'wifi.alert.password': 'Lo senhal pòt pas èsser void',
      'wifi.alert.password.length.5':
        'Lo senhal deu conténer almens 5 caractèrs o cambiatz lo chiframent per « Cap »',
      'wifi.alert.password.8':
        'Lo senhal deu conténer almens 8 caractèrs o cambiatz lo chiframent per « Cap »',
      'wifi.alert.eapIdentity': 'L’identitat pòt pas èsser voide',
      'button.rotate': 'Pivotar',
      'button.print': 'Imprimir',
      select: 'Causir la lenga',
    },
  },
  {
    id: 'pt-BR',
    name: 'Portuguese - Português brasileiro',
    translation: {
      title: 'Cartão WiFi',
      'desc.use':
        'Imprime um simples cartão com os dados de login de sua WiFi. Cole na sua geladeira, guarde na sua carteira etc.',
      'desc.privacy':
        'As informações da sua WiFi nunca será enviada para o servidor. Nenhum serviço de tracking, analytics ou fingerprint é usado nesse site. Veja o',
      'desc.source': 'código fonte',
      'wifi.login': 'WiFi Login',
      'wifi.name': 'Nome da rede',
      'wifi.name.placeholder': 'Nome da Rede',
      'wifi.password': 'Senha',
      'wifi.password.placeholder': 'Senha',
      'wifi.password.hide': 'Esconder Senha',
      'wifi.name.hiddenSSID': 'Esconder SSID',
      'wifi.password.encryption': 'Tipo de Segurança',
      'wifi.password.encryption.none': 'Nenhum',
      'wifi.tip':
        'Aponte a camera do seu celular para o código QR para se conectar automaticamente.',
      'wifi.alert.name': 'Nome da rede não pode estar em branco',
      'wifi.alert.password.length.5':
        'Sua senha deve ter pelo menos 5 caracteres, ou  altere a criptografia para "Nenhum"',
      'wifi.alert.password.8':
        'Sua senha deve ter pelo menos 8 caracteres, ou  altere a criptografia para "Nenhum"',
      'button.rotate': 'Rotacionar',
      'button.print': 'Imprimir',
      select: 'Escolha o idioma',
    },
  },
  {
    id: 'it-IT',
    name: 'Italian',
    translation: {
      title: 'WiFi Card',
      'desc.use':
        'Stampa una scheda con le informazioni di accesso WiFi. Attaccala al frigo, tienila nel portafogli etc.',
      'desc.privacy':
        'Le informazioni del tuo WiFi non verranno mai inviate ai nostri server. Nessun tracciamento, analytics, o fingerprinting viene usato su questo sito. Visiona le',
      'desc.source': 'codice sorgente',
      'wifi.login': 'WiFi Login',
      'wifi.name': 'Nome della rete',
      'wifi.name.placeholder': 'Nome della rete wifi',
      'wifi.password': 'Password',
      'wifi.password.placeholder': 'Password',
      'wifi.password.hide': 'Nascondi password',
      'wifi.name.hiddenSSID': 'SSID nascosto',
      'wifi.password.encryption': 'Cifratura',
      'wifi.password.encryption.none': 'Nessuno',
      'wifi.tip':
        'Inquadra il codice QR con il tuo smartphone per collegarti automaticamente',
      'wifi.alert.name': 'Il nome della rete wifi non può essere vuoto',
      'wifi.alert.password.length.5':
        'La password deve contenere almeno 5 caratteri',
      'wifi.alert.password.length.8':
        'La password deve contenere almeno 8 caratteri',
      'button.rotate': 'Ruota',
      'button.print': 'Stampa',
      select: 'Seleziona una lingua',
    },
  },
  {
    id: 'tr-TR',
    name: 'Turkish - Türkçe',
    translation: {
      title: 'WiFi Kartı',
      'desc.use':
        'WiFi giriş bilgilerinizle basit bir kart yazdırın. Buzdolabına bantlayın, cüzdanınızda saklayın vb.',
      'desc.privacy':
        'WiFi bilgileriniz asla sunucuya gönderilmez. Bu web sitesinde hiçbir izleme, analiz veya parmak izi kullanılmamaktadır. Görüntüle',
      'desc.source': 'kaynak kodu',
      'wifi.login': 'WiFi Giriş',
      'wifi.name': 'Ağ adı',
      'wifi.name.placeholder': 'WiFi Ağ adı',
      'wifi.password': 'Parola',
      'wifi.password.placeholder': 'Parola',
      'wifi.password.hide': 'Şifreyi gizle',
      'wifi.name.hiddenSSID': 'Gizli SSID',
      'wifi.password.encryption': 'Şifreleme',
      'wifi.password.encryption.none': 'Hiçbiri',
      'wifi.tip':
        'Otomatik olarak bağlanmak için telefonunuzun kamerası ile QR kodunu okutun',
      'wifi.alert.name': 'Ağ adı boş olamaz',
      'wifi.alert.password.length.5':
        'Şifre en az 5 karakter olmalıdır veya şifrelemeyi "Yok" olarak değiştirin',
      'wifi.alert.password.length.8':
        'Şifre en az 8 karakter olmalıdır veya şifrelemeyi "Yok" olarak değiştirin',
      'button.rotate': 'Döndür',
      'button.print': 'Yazdır',
      select: 'Dil Seçin',
    },
  },
  {
    id: 'ar',
    name: 'Arabic - العربية',
    rtl: true,
    translation: {
      title: 'بطاقة واي فاي',
      'desc.use':
        'اطبع بطاقة بسيطة تحتوي على تفاصيل تسجيل الدخول إلى شبكة الواي فاي. إلصقها على الثلاجة، اوإحتفظ بها في محفظتك.',
      'desc.privacy':
        'لا يتم إرسال بيانات الشبكة الخاصة بك إلى الخادم او اي اماكن اخري. لا يتم استخدام التتبع أو التحليلات أو البصمات الإلكترونية أو حفظ البيانات على هذا الموقع. اعرض ملف',
      'desc.source': 'البرنامج',
      'wifi.login': 'تسجيل الدخول',
      'wifi.name': 'إسم الشبكة',
      'wifi.name.hiddenSSID': 'مخفي SSID',
      'wifi.name.placeholder': 'إسم الشبكة',
      'wifi.password': 'كلمه المرور',
      'wifi.password.placeholder': 'كلمه المرور',
      'wifi.password.hide': 'إخفاء حقل كلمة المرور قبل الطباعة',
      'wifi.password.encryption': 'التشفير',
      'wifi.password.encryption.none': 'لا يوجد',
      'wifi.tip':
        'وجّه كاميرا هاتفك إلى رمز الاستجابة السريعة للاتصال تلقائيًا',
      'wifi.alert.name': 'ًلا يمكن أن يكون اسم الشبكة فارغًا',
      'wifi.alert.password.length.5':
        'يجب أن تكون كلمة المرور مكونة من ٥ أحرف على الأقل',
      'wifi.alert.password.length.8':
        'يجب أن تكون كلمة المرور مكونة من ٨ أحرف على الأقل',
      'button.rotate': 'تدوير',
      'button.print': 'طباعة',
      select: 'اختر اللغة',
    },
  },
  {
    id: 'hi-IN',
    name: 'Hindi - हिन्दी',
    translation: {
      title: 'वाईफाई कार्ड',
      'desc.use':
        'अपने वाईफाई लॉगिन की जानकारी एक साधारण कार्ड पे प्रिंट करे। अपने फ्रिज पर लगाएं, अपने बटुए में रखें, आदि।',
      'desc.privacy':
        'आपके वाईफाई की जानकारी कभी किसी सर्वर पर नहीं भेजी जाती। इस वेबसाइट पर ट्रैकिंग , एनालिटिक्स या फिंगरप्रिंटिंग का इस्तेमाल नहीं होता।',
      'desc.source': 'सोर्स कोड देखो',
      'wifi.login': 'वाईफाई लॉगिन',
      'wifi.name': 'नेटवर्क का नाम',
      'wifi.name.placeholder': 'वाईफाई नेटवर्क का नाम',
      'wifi.password': 'पासवर्ड',
      'wifi.password.placeholder': 'पासवर्ड',
      'wifi.password.hide': 'पासवर्ड छुपाएं',
      'wifi.name.hiddenSSID': 'छिपा हुआ SSID',
      'wifi.password.encryption': 'एन्क्रिप्शन',
      'wifi.password.encryption.none': 'कोई नहीं',
      'wifi.tip':
        'अपने आप कनेक्ट होने के लिए अपने फ़ोन के कैमरे से QR कोड को स्कैन करें',
      'wifi.alert.name': 'नेटवर्क का नाम खाली नहीं हो सकता',
      'wifi.alert.password.length.5':
        'पासवर्ड कम से कम 5 अक्षरों का होना चाहिए, या एन्क्रिप्शन को "कोई नहीं" में बदलें',
      'wifi.alert.password.length.8':
        'पासवर्ड कम से कम 8 अक्षरों का होना चाहिए, या एन्क्रिप्शन को "कोई नहीं" में बदलें',
      'button.rotate': 'घुमाएँ',
      'button.print': 'प्रिंट करे',
      select: 'भाषा चुने',
    },
  },
  {
    id: 'ca',
    name: 'Catalan - Català',
    translation: {
      title: 'Targeta WiFi',
      'desc.use':
        'Imprimeix una targeta senzilla amb les teves dades per iniciar sessió WiFi. Enganxeu-ho a la nevera, guardeu-ho a la cartera, etc.',
      'desc.privacy':
        'La vostra informació de WiFi mai no s’envia al servidor. En aquest lloc web no s’utilitza cap rastreig, analítica ni empremta digital. Si vols pots veure el',
      'desc.source': 'codi font',
      'wifi.login': 'Inici de sessió WiFi',
      'wifi.name': 'Nom de la xarxa',
      'wifi.name.hiddenSSID': 'SSID amagat',
      'wifi.name.placeholder': 'Nom de la xarxa WiFi',
      'wifi.password': 'Contrasenya',
      'wifi.password.placeholder': 'Contrasenya',
      'wifi.password.hide': 'Amaga la contrasenya',
      'wifi.password.encryption': 'Encriptació',
      'wifi.password.encryption.none': 'Cap',
      'wifi.tip':
        'Apunteu la càmera del telèfon cap al codi QR per connectar-vos automàticament',
      'wifi.alert.name': 'El nom de la xarxa no pot estar buit',
      'wifi.alert.password.length.5':
        "La contrasenya ha de tenir com a mínim 5 caràcters o canvieu l'encriptació per « Cap »",
      'wifi.alert.password.length.8':
        "La contrasenya ha de tenir com a mínim 8 caràcters o canvieu l'encriptació per « Cap »",
      'button.rotate': 'Gira',
      'button.print': 'Imprimeix',
      select: 'Escolliu l’idioma',
    },
  },
  {
    id: 'id-ID',
    name: 'Indonesian',
    translation: {
      title: 'Kartu WiFi',
      'desc.use':
        'Cetak kartu sederhana ini dengan informasi login WiFi anda. Tempelkan di pintu lemari es, atau simpan di dompet anda, dll.',
      'desc.privacy':
        'Informasi WiFi anda tidak akan dikirim ke server manapun. Tidak ada pelacakan, analitik, atau sidik jari yang digunakan di situs website ini. Lihat',
      'desc.source': 'source code',
      'wifi.login': 'Login WiFi',
      'wifi.name': 'Nama Jaringan',
      'wifi.name.placeholder': 'Nama Jaringan WiFi',
      'wifi.password': 'Kata Sandi',
      'wifi.password.placeholder': 'Kata Sandi',
      'wifi.name.hiddenSSID': 'Sembunyikan SSID',
      'wifi.password.hide': 'Sembunyikan kata sandi',
      'wifi.password.encryption': 'Enkripsi',
      'wifi.password.encryption.none': 'Tidak ada',
      'wifi.tip':
        'Arahkan kamera ponsel anda ke Kode QR untuk terhubung ke WiFi secara otomatis',
      'wifi.alert.name': 'Nama jaringan tidak boleh kosong',
      'wifi.alert.password.length.5':
        'Kata sandi minimal harus 5 karakter, atau ubah enkripsi menjadi "Tidak ada"',
      'wifi.alert.password.length.8':
        'Kata sandi minimal harus 8 karakter, atau ubah enkripsi menjadi "Tidak ada"',
      'button.rotate': 'Putar',
      'button.print': 'Cetak',
      select: 'Pilih Bahasa',
    },
  },
  {
    id: 'ko',
    name: 'Korean - 한국어',
    translation: {
      title: 'WiFi 카드',
      'desc.use':
        'WiFi 로그인 정보를 알려주는 간단한 카드를 출력하세요. 냉장고에 붙이거나, 지갑에 소지하는 등 다양하게 이용하세요.',
      'desc.privacy':
        '입력한 WiFi 정보는 서버로 전송되지 않습니다. 이 웹사이트는 추적, 분석, 디지털 지문을 사용하지 않습니다. 소스 코드를 참조하세요',
      'desc.source': '소스 코드',
      'wifi.login': 'WiFi 로그인',
      'wifi.name': '네트워크 이름',
      'wifi.name.placeholder': 'WiFi 네트워크 이름',
      'wifi.name.hiddenSSID': '숨겨진 SSID',
      'wifi.password': '비밀번호',
      'wifi.password.placeholder': '비밀번호',
      'wifi.password.hide': '비밀번호 가리기',
      'wifi.password.encryption': '보안',
      'wifi.password.encryption.none': '없음',
      'wifi.tip': '휴대폰의 카메라를 QR 코드에 가져대어 자동으로 연결하세요',
      'wifi.alert.name': '네트워크 이름은 공백일 수 없습니다',
      'wifi.alert.password.length.5':
        '비밀번호를 5글자 이상 입력하시거나 보안을 "없음"으로 변경하세요.',
      'wifi.alert.password.length.8':
        '비밀번호를 8글자 이상 입력하시거나 보안을 "없음"으로 변경하세요.',
      'button.rotate': '회전',
      'button.print': '인쇄',
      select: '언어 선택',
    },
  },
  {
    id: 'hu-HU',
    name: 'Hungarian - Magyar',
    translation: {
      title: 'WiFi Kártya',
      'desc.use':
        'Nyomtass ki egy egyszerű kártyát a WiFi bejelentkezési adataiddal. Ragaszd fel a hűtőszekrényedre, tartsd a pénztárcádban, stb.',
      'desc.privacy':
        'A WiFi adataid sosem lesznek elküldve a szerverre. Ezen a weboldalon nincs követés, nincs analitika vagy digitális ujjlenyomatozás. Nézd meg a',
      'desc.source': 'forráskódot',
      'wifi.login': 'WiFi Bejelentkezés',
      'wifi.name': 'Hálózat neve',
      'wifi.name.placeholder': 'WiFi hálózat neve',
      'wifi.password': 'Jelszó',
      'wifi.password.placeholder': 'Jelszó',
      'wifi.name.hiddenSSID': 'Rejtett SSID',
      'wifi.password.hide': 'Jelszó elrejtése',
      'wifi.password.encryption': 'Titkosítás',
      'wifi.password.encryption.none': 'Nincs',
      'wifi.tip':
        'Olvasd be a QR kódot a telefonod kamerájával az automatikus csatlakozáshoz',
      'wifi.alert.name': 'A Hálózat neve nem lehet üres',
      'wifi.alert.password.length.5':
        'A jelszó minimum 5 karakter legyen, vagy állítsd a titkosítást "Nincs"-re',
      'wifi.alert.password.length.8':
        'A jelszó minimum 8 karakter legyen, vagy állítsd a titkosítást "Nincs"-re',
      'button.rotate': 'Forgatás',
      'button.print': 'Nyomtatás',
      select: 'Válassz nyelvet',
    },
  },
  {
    id: 'sr',
    name: 'Serbian - Srpski',
    translation: {
      title: 'WiFi Karta',
      'desc.use':
        'Odštampajte jednostavnu karticu sa Vašim WiFi podacima za prijavu. Zalepite je na frižideru, držite je u novčaniku, itd.',
      'desc.privacy':
        'Informacije o Vašoj WiFi mreži se nikada ne šalju na server. Nema nikakvog praćenja, analitike ili formi identifikacije na ovom sajtu.',
      'desc.source': 'Izvorni kod',
      'wifi.login': 'WiFi prijava',
      'wifi.name': 'Ime mreže',
      'wifi.name.placeholder': 'Ime WiFi mreže',
      'wifi.password': 'Šifra',
      'wifi.password.placeholder': 'Šifra',
      'wifi.name.hiddenSSID': 'Sakriven SSID ',
      'wifi.password.hide': 'Sakri šifru',
      'wifi.password.encryption': 'Enkripcija',
      'wifi.password.encryption.none': 'Nema',
      'wifi.tip':
        'Uperite kameru Vašeg telefona na QR kod da bi ste se povezali automatski na mrežu',
      'wifi.alert.name': 'Ime mreže ne može biti prazno',
      'wifi.alert.password.length.5':
        'Šifra mora imati minimum 5 karaktera ili promeni enkripciju na "Nema"',
      'wifi.alert.password.length.8':
        'Šifra mora imati minimum 8 karaktera ili promeni enkripciju na "Nema"',
      'button.rotate': 'Rotiraj',
      'button.print': 'Odštampaj',
      select: 'Odaberite jezik',
    },
  },
  {
    id: 'sr-Cyrl-CS',
    name: 'Serbian - Српски',
    translation: {
      title: 'WiFi карта',
      'desc.use':
        'Одштампајте једноставну картицу са Вашим WiFi подацима за пријаву. Залепите је на фрижидеру, држите је у новчанику, итд.',
      'desc.privacy':
        'Информације о Вашој WiFi мрежи се никада не саљу на сервер. Нема никаквог праћења, аналитике или форми индетификације на овом сајту.',
      'desc.source': 'Изворни код',
      'wifi.login': 'WiFi мрежа',
      'wifi.name': 'Име мреже',
      'wifi.name.placeholder': 'Име WiFi мреже',
      'wifi.password': 'Шифра',
      'wifi.password.placeholder': 'Шифра',
      'wifi.name.hiddenSSID': 'Сакривен SSID ',
      'wifi.password.hide': 'Сакри шифру',
      'wifi.password.encryption': 'Енкрипција',
      'wifi.password.encryption.none': 'Нема',
      'wifi.tip':
        'Уперите камеру Вашег телефона на QR код да би сте се повезали аутомацки на мрежу',
      'wifi.alert.name': 'Име мреже не може бити празно',
      'wifi.alert.password.length.5':
        'Шифра мора имати минимум 5 карактера или промени енкрипцију на "Нема"',
      'wifi.alert.password.length.8':
        'Шифра мора имати минимум 8 карактера или промени енкрипцију на "Нема"',
      'button.rotate': 'Ротирај',
      'button.print': 'Одштампај',
      select: 'Одаберите језик',
    },
  },
  {
    id: 'Ur',
    name: 'Urdu',
    translation: {
      title: 'وائی ​​فائی کارڈ',
      'desc.use':
        'اپنے وائی فائی لاگ ان کی تفصیلات کے ساتھ ایک سادہ کارڈ پرنٹ کریں۔ اسے فریج میں ٹیپ کریں ، اسے اپنے پرس میں رکھیں ، وغیرہ۔',
      'desc.privacy':
        'آپ کی وائی فائی معلومات کبھی بھی سرور کو نہیں بھیجی جاتی۔ اس ویب سائٹ پر کوئی ٹریکنگ ، تجزیات ، یا فنگر پرنٹنگ استعمال نہیں کی جاتی ہے۔ دیکھیں۔',
      'desc.source': 'سورس کوڈ',
      'wifi.login': 'وائی ​​فائی لاگ ان',
      'wifi.name': 'نیٹ ورک کا نام',
      'wifi.name.hiddenSSID': 'پوشیدہ SSID۔',
      'wifi.name.placeholder': 'وائی ​​فائی نیٹ ورک کا نام۔',
      'wifi.password': 'پاس ورڈ',
      'wifi.password.placeholder': 'پاس ورڈ',
      'wifi.password.hide': 'پاس ورڈ چھپائیں۔',
      'wifi.password.encryption': 'خفیہ کاری۔',
      'wifi.password.encryption.none': 'کوئی نہیں',
      'wifi.tip':
        'اپنے فون کے کیمرے کو QR کوڈ کی طرف اشارہ کریں تاکہ خود بخود جڑ جائے۔',
      'wifi.alert.name': 'نیٹ ورک کا نام خالی نہیں ہو سکتا۔',
      'wifi.alert.password.length.5':
        'پاس ورڈ کم از کم 5 حروف کا ہونا چاہیے ، یا خفیہ کاری کو "کوئی نہیں" میں تبدیل کرنا چاہیے',
      'wifi.alert.password.length.8':
        'پاس ورڈ کم از کم 8 حروف کا ہونا چاہیے ، یا خفیہ کاری کو "کوئی نہیں" میں تبدیل کرنا چاہیے',
      'button.rotate': 'گھمائیں',
      'button.print': 'پرنٹ کریں',
      select: 'زبان منتخب کریں۔',
    },
  },
  {
    id: 'th-TH',
    name: 'Thai - ภาษาไทย',
    translation: {
      title: 'การ์ด WiFi',
      'desc.use':
        'พิมพ์การ์ดอย่างง่ายพร้อมรายละเอียดการเข้าสู่ระบบ WiFi ของคุณ. ติดเทปไว้บนตู้เย็น, เก็บไว้ในกระเป๋าสตางค์ ฯลฯ',
      'desc.privacy':
        'ข้อมูล WiFi ของคุณจะไม่ถูกส่งไปยังเซิร์ฟเวอร์, ไม่มีการติดตาม, การวิเคราะห์, หรือลายนิ้วมือบนเว็บไซต์นี้. ดู',
      'desc.source': 'ซอร์ซโคด',
      'wifi.login': 'เข้าสู่ระบบ WiFi',
      'wifi.name': 'ชื่อเครือข่าย',
      'wifi.name.hiddenSSID': 'SSID ถูกซ่อนอยู่',
      'wifi.name.placeholder': 'ชื่อเครือข่าย WiFi',
      'wifi.password': 'รหัสผ่าน WiFi',
      'wifi.password.placeholder': 'รหัสผ่าน WiFi',
      'wifi.password.hide': 'ซ่อนรหัสผ่าน WiFi บนการ์ด',
      'wifi.password.encryption': 'การเข้ารหัส',
      'wifi.password.encryption.none': 'ไม่มี',
      'wifi.tip': 'หันกล้องของโทรศัพท์ไปที่ QR Code เพื่อเชื่อมต่อโดยอัตโนมัติ',
      'wifi.alert.name': 'ต้องระบุชื่อเครือข่าย',
      'wifi.alert.password.length.5':
        'รหัสผ่านต้องมีอักขระอย่างน้อย 5 ตัว หรือเปลี่ยนการเข้ารหัสเป็น "ไม่มี"',
      'wifi.alert.password.length.8':
        'รหัสผ่านต้องมีอักขระอย่างน้อย 8 ตัว หรือเปลี่ยนการเข้ารหัสเป็น "ไม่มี"',
      'button.rotate': 'หมุนแนวการ์ด',
      'button.print': 'พิมพ์',
      select: 'เลือกภาษา',
    },
  },
  {
    id: 'pb-IN',
    name: 'Punjabi - ਪੰਜਾਬੀ',
    translation: {
      title: 'ਵਾਈਫਾਈ ਕਾਰਡ',
      'desc.use':
        'ਆਪਣੇ ਫਾਈ ਲੌਗਇਨ ਵੇਰਵਿਆਂ ਦੇ ਨਾਲ ਇੱਕ ਸਧਾਰਨ ਕਾਰਡ ਪ੍ਰਿੰਟ ਕਰੋ। ਇਸਨੂੰ ਫਰਿੱਜ ਵਿੱਚ ਟੇਪ ਕਰੋ, ਇਸਨੂੰ ਆਪਣੇ ਬਟੂਏ ਵਿੱਚ ਰੱਖੋ, ਆਦਿ',
      'desc.privacy':
        'ਤੁਹਾਡੀ ਫਾਈ ਜਾਣਕਾਰੀ ਕਦੇ ਵੀ ਸਰਵਰ ਨੂੰ ਨਹੀਂ ਭੇਜੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਵੈੱਬਸਾਈਟ ਤੇ ਕੋਈ ਟਰੈਕਿੰਗ, ਵਿਸ਼ਲੇਸ਼ਣ ਜਾਂ ਫਿੰਗਰਪ੍ਰਿੰਟਿੰਗ ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ। ਵੇਖੋ',
      'desc.source': 'ਸੂਤਰ ਸੰਕੇਤਾਵਲੀ',
      'wifi.login': 'ਫਾਈ ਲਾਗਿਨ',
      'wifi.name': 'ਨੈੱਟਵਰਕ ਦਾ ਨਾਮ',
      'wifi.name.hiddenSSID': 'ਲੁਕਿਆ ਹੋਇਆ SSID',
      'wifi.name.placeholder': 'ਫਾਈ ਨੈੱਟਵਰਕ ਦਾ ਨਾਮ',
      'wifi.password': 'ਪਾਸਵਰਡ',
      'wifi.password.placeholder': 'ਪਾਸਵਰਡ',
      'wifi.password.hide': 'ਓਹਲੇ ਪਾਸਵਰਡ',
      'wifi.password.encryption': 'ਐਨਕ੍ਰਿਪਸ਼ਨ',
      'wifi.password.encryption.none': 'ਕੋਈ ਨਹੀਂ',
      'wifi.tip':
        'ਸਵੈਚਲਿਤ ਤੌਰ ਤੇ ਕਨੈਕਟ ਕਰਨ ਲਈ ਆਪਣੇ ਫ਼ੋਨ ਦੇ ਕੈਮਰੇ ਨੂੰ QR ਕੋਡ ਤੇ ਪੁਆਇੰਟ ਕਰੋ',
      'wifi.alert.name': 'ਨੈੱਟਵਰਕ ਨਾਮ ਖਾਲੀ ਨਹੀਂ ਹੋ ਸਕਦਾ ਹੈ',
      'wifi.alert.password.length.5':
        'ਪਾਸਵਰਡ ਘੱਟੋ-ਘੱਟ ਪੰਜ ਅੱਖਰਾਂ ਦਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਾਂ ਐਨਕ੍ਰਿਪਸ਼ਨ ਨੂੰ ਕੋਈ ਨਹੀਂ ਵਿੱਚ ਬਦਲਣਾ ਚਾਹੀਦਾ ਹੈ',
      'wifi.alert.password.length.8':
        'ਪਾਸਵਰਡ ਘੱਟੋ-ਘੱਟ ਅੱਠ ਅੱਖਰਾਂ ਦਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਾਂ ਐਨਕ੍ਰਿਪਸ਼ਨ ਨੂੰ ਕੋਈ ਨਹੀਂ ਵਿੱਚ ਬਦਲਣਾ ਚਾਹੀਦਾ ਹੈ',
      'button.rotate': 'ਘੁੰਮਾਓ',
      'button.print': 'ਛਾਪੋ',
      select: 'ਭਾਸ਼ਾ ਚੁਣੋ',
    },
  },
  {
    id: 'dk-DA',
    name: 'Danish - Dansk',
    translation: {
      title: 'WiFi Kort',
      'desc.use':
        'Udskriv et enkelt kort med dine Wifi login oplysninger. Sæt det på køleskapet, læg det i din pung eller lignende.',
      'desc.privacy':
        'Dine Wifi informationer bliver aldrig sendt til vores servere. Ingen sporing, analyse eller identifikation anvendes på dette website. Se vores',
      'desc.source': 'kildekode',
      'wifi.login': 'WiFi login',
      'wifi.name': 'Netværksnavn',
      'wifi.name.hiddenSSID': 'Skjult SSID',
      'wifi.name.placeholder': 'WiFi Netværksnavn',
      'wifi.password': 'Kodeord',
      'wifi.password.placeholder': 'Kodeord',
      'wifi.password.hide': 'Skjul kodeord',
      'wifi.password.encryption': 'Kryptering',
      'wifi.password.encryption.none': 'Ingen',
      'wifi.tip': 'Ret telefonens kamera mod QR koden for tilslutte automatisk',
      'wifi.alert.name': 'Netværksnavnet må ikke være tomt',
      'wifi.alert.password.length.5':
        'Kodeordet skal være på mindst 5 tegn, eller skift kryptering til "Ingen"',
      'wifi.alert.password.length.8':
        'Kodeordet skal være på mindst 8 tegn, eller skift kryptering til "Ingen"',
      'button.rotate': 'Roter',
      'button.print': 'Print ud',
      select: 'Vælg sprog',
    },
  },
  {
    id: 'sk-SK',
    name: 'Slovak - Slovenčina',
    translation: {
      title: 'WiFi Karta',
      'desc.use':
        'Vytlačte si jednoduchú kartu s prihlasovacími údajmi do siete Wi-Fi. Prilepte ju na chladničku, majte ju v peňaženke atď.',
      'desc.privacy':
        'Vaše Wi-Fi informácie sa nikdy neodošlú na server. Na tejto webovej stránke sa nepoužíva žiadne sledovanie, analytika ani fingerprinting. Zobraziť',
      'desc.source': 'zdrojový kód',
      'wifi.identity': 'Identita',
      'wifi.identity.placeholder': 'Uživateľské meno',
      'wifi.login': 'WiFi Login',
      'wifi.name': 'Názov siete',
      'wifi.name.hiddenSSID': 'Skryté SSID',
      'cards.additional': 'Počet ďalších kariet na tlač',
      'cards.tip.hide': 'Schovať nápovedu',
      'wifi.name.placeholder': 'Názov siete WiFi',
      'wifi.password': 'Heslo',
      'wifi.password.placeholder': 'Heslo',
      'wifi.password.hide': 'Schovať heslo',
      'wifi.password.encryption': 'Šifrovanie',
      'wifi.password.encryption.none': 'Žiadne',
      'wifi.encryption.eapMethod': 'Metóda EAP',
      'wifi.tip':
        'Namierte fotoaparát telefónu na QR kód a automaticky sa pripojte.',
      'wifi.alert.name': 'Názov siete nesmie byť prázdny',
      'wifi.alert.password': 'Heslo nesmie byť prázdne',
      'wifi.alert.password.length.5':
        'Heslo musí mať aspoň 5 znakov, alebo zmeňte šifrovanie na "Žiadne"',
      'wifi.alert.password.length.8':
        'Heslo musí mať aspoň 8 znakov, alebo zmeňte šifrovanie na "Žiadne"',
      'wifi.alert.eapIdentity': 'Identita nesmie byť prázdna',
      'button.rotate': 'Otočiť',
      'button.print': 'Vytlačiť',
      select: 'Vybrať jazyk',
    },
  },
  {
    id: 'mg-MG',
    name: 'Malagasy - Malagasy',
    translation: {
      title: 'Karatra Wifi',
      'desc.use':
        "Antontay ny karatra tsotra maneho ny mombamomba ny wifi-nao. Apetraho eran'ny trano, ataovy any anaty boky, sns",
      'desc.privacy':
        "Tsy tehirizinay na aiza na aiza izay zavatra ampidirinao eto. Tsy misy fanarahana na fitsikilovana eto amin'ity pejy ity. Misy fanazavana",
      'desc.source': 'source code',
      'wifi.identity': 'Anarana',
      'wifi.identity.placeholder': 'Anarana',
      'wifi.login': 'Momba ny WiFi',
      'wifi.name': 'SSID',
      'wifi.name.hiddenSSID': 'SSID miafina',
      'cards.additional': "Isan' ny karatra fanampiny atonta",
      'cards.tip.hide': 'Aza asiana fanazavana (legend)',
      'wifi.name.placeholder': "Anaran'ny tambajotra WiFi (SSID)",
      'wifi.password': 'Fanalahidy',
      'wifi.password.placeholder': 'Teny fanalahidy',
      'wifi.password.hide': 'Afeno ny fanalahidy',
      'wifi.password.encryption': 'Encryption',
      'wifi.password.encryption.none': 'Tsy misy',
      'wifi.encryption.eapMethod': 'EAP method',
      'wifi.tip':
        "Mba hidiranao malakilaky dia alaivo sary amin'ny fakantsarinao ilay QR Code",
      'wifi.alert.name': 'Tsy maintsy misy anarana ilay tambajotra',
      'wifi.alert.password': 'Tsy maintsy fenoina ny fanalahidy',
      'wifi.alert.password.length.5':
        "Tsy maintsy mihoatry ny litera 5 ny fanalahidy, na tsy maintsy ovaina ho 'Tsy Misy' ny Encryption",
      'wifi.alert.password.length.8':
        "Tsy maintsy mihoatry ny litera 8 ny fanalahidy, na tsy maintsy ovaina ho 'Tsy Misy' ny Encryption",
      'wifi.alert.eapIdentity': 'Tsy maintsy fenoina ny anarana',
      'button.rotate': 'Ahodino',
      'button.print': 'Antontay',
      select: 'Mifidiana fiteny hafa',
    },
  },
  {
    id: 'bn-BD',
    name: 'Bangla - বাংলা',
    translation: {
      title: 'ওয়াইফাই কার্ড',
      'desc.use':
        'আপনার ওয়াই-ফাই লগইন বিবরণ সহ একটি সাধারণ কার্ড প্রিন্ট করুন। এটি ফ্রিজে টেপ দিয়ে লাগান, আপনার ওয়ালেটে রাখুন, ইত্যাদি।',
      'desc.privacy':
        'আপনার ওয়াই-ফাই তথ্য কখনই সার্ভারে পাঠানো হয় না। এই ওয়েবসাইটে কোন ট্র্যাকিং, অ্যানালিটিক্স বা ফিঙ্গারপ্রিন্টিং ব্যবহার করা হয় না। দেখুন',
      'desc.source': 'সোর্স কোড',
      'wifi.login': 'ওয়াই-ফাই লগইন',
      'wifi.name': 'নেটওয়ার্কের নাম',
      'wifi.name.hiddenSSID': 'লুকানো SSID',
      'cards.additional': 'অতিরিক্ত কার্ড প্রিন্ট করা হবে',
      'cards.tip.hide': 'নির্দেশ (টীকা) লুকান',
      'wifi.name.placeholder': 'ওয়াই-ফাই নেটওয়ার্কের নাম',
      'wifi.password': 'পাসওয়ার্ড',
      'wifi.password.placeholder': 'পাসওয়ার্ড',
      'wifi.password.hide': 'পাসওয়ার্ড লুকান',
      'wifi.password.encryption': 'এনক্রিপশন',
      'wifi.password.encryption.none': 'নেই',
      'wifi.tip':
        'স্বয়ংক্রিয়ভাবে সংযোগ করতে আপনার ফোনের ক্যামেরা QR কোডে নির্দেশ করুন',
      'wifi.alert.name': 'নেটওয়ার্কের নাম খালি হতে পারে না',
      'wifi.alert.password': 'পাসওয়ার্ড খালি হতে পারে না',
      'wifi.alert.password.length.5':
        'পাসওয়ার্ড কমপক্ষে ৫ অক্ষরের হতে হবে, অথবা এনক্রিপশন পরিবর্তন করে "নেই" দিন',
      'wifi.alert.password.length.8':
        'পাসওয়ার্ড কমপক্ষে ৮ অক্ষরের হতে হবে, অথবা এনক্রিপশন পরিবর্তন করে "নেই" দিন',
      'button.rotate': 'ঘুরান',
      'button.print': 'প্রিন্ট',
      select: 'ভাষা নির্বাচন করুন',
    },
  },
  {
    id: 'eo',
    name: 'Esperanto',
    translation: {
      title: 'Vifia karto',
      'desc.use':
        'Presu simplan karton kun viaj vifiaj ensalutaj detaloj. Bendu ĝin al la fridujo, konservu ĝin en via monujo, ktp.',
      'desc.privacy':
        'Viaj vifiaj informoj neniam estas senditaj al la servilo. Neniu spurado, analizo aŭ fingrospurado estas uzataj en ĉi tiu retejo. Vidi la',
      'desc.source': 'fontokodon',
      'wifi.identity': 'Identeco',
      'wifi.identity.placeholder': 'Uzantnomo',
      'wifi.login': 'Vifia ensaluto',
      'wifi.name': 'Retnomo',
      'wifi.name.hiddenSSID': 'Kaŝita SSID',
      'cards.additional': 'Pliaj kartoj por presi',
      'cards.tip.hide': 'Kaŝi konsileton (klarigeto)',
      'wifi.name.placeholder': 'Nomo de vifia reto',
      'wifi.password': 'Pasvorto',
      'wifi.password.placeholder': 'Pasvorto',
      'wifi.password.hide': 'Kaŝi pasvorton',
      'wifi.password.encryption': 'Ĉifrado',
      'wifi.password.encryption.none': 'Nenio',
      'wifi.encryption.eapMethod': 'EAP-metodo',
      'wifi.tip':
        'Metu la fotilon de via telefono antaŭ la QR-kodo por aŭtomate konektiĝi',
      'wifi.alert.name': 'Retnomo ne povas esti malplena',
      'wifi.alert.password': 'Pasvorto ne povas esti malplena',
      'wifi.alert.password.length.5':
        'Pasvorto devas enhavi almenaŭ 5 signoj, aŭ ŝanĝu la ĉifradon al "Neniu"',
      'wifi.alert.password.length.8':
        'Pasvorto devas enhavi almenaŭ 8 signoj, aŭ ŝanĝu la ĉifradon al "Neniu"',
      'wifi.alert.eapIdentity': 'Identeco ne povas esti malplena',
      'button.rotate': 'Rotacii',
      'button.print': 'Presi',
      select: 'Elektu lingvon',
    },
  },
  {
    id: 'ms-MY',
    name: 'Malay - Malaysia',
    translation: {
      title: 'Kad WiFi',
      'desc.use':
        'Cetak kad ringkas dengan butiran login anda. Tampal pada peti sejuk, simpan dalam dompet anda, dan sebagainya.',
      'desc.privacy':
        'Informasi WiFi anda tidak dihantar ke server. Tiada penjejakan, analitik, atau pencetakan cap jari digunakan di laman web ini. Lihat',
      'desc.source': 'kod sumber',
      'wifi.identity': 'Identiti',
      'wifi.identity.placeholder': 'Nama Pengguna',
      'wifi.login': 'Login WiFi',
      'wifi.name': 'Nama Rangkaian',
      'wifi.name.hiddenSSID': 'SSID Tersembunyi',
      'cards.additional': 'Bilangan kad untuk dicetak',
      'cards.tip.hide': 'Sembunyikan panduan (legenda)',
      'wifi.name.placeholder': 'Nama Rangkaian WiFi',
      'wifi.password': 'Kata Laluan',
      'wifi.password.placeholder': 'Kata Laluan',
      'wifi.password.hide': 'Sembunyikan kata laluan',
      'wifi.password.encryption': 'Enkripsi',
      'wifi.password.encryption.none': 'Tiada',
      'wifi.encryption.eapMethod': 'Kaedah EAP',
      'wifi.tip': 'Imbas Kod QR untuk menyambung ke WiFi secara automatik',
      'wifi.alert.name': 'Nama rangkaian tidak boleh kosong',
      'wifi.alert.password': 'Kata laluan tidak boleh kosong',
      'wifi.alert.password.length.5':
        'Kata laluan mesti sekurang-kurangnya 5 aksara, atau tukar enkripsi kepada "Tiada"',
      'wifi.alert.password.length.8':
        'Kata laluan mesti sekurang-kurangnya 8 aksara, atau tukar enkripsi kepada "Tiada"',
      'wifi.alert.eapIdentity': 'Identiti tidak boleh kosong',
      'button.rotate': 'Putar',
      'button.print': 'Cetak',
      select: 'Pilih Bahasa',
    },
  },
].sort((a, b) => {
  return a.name.toLowerCase() < b.name.toLowerCase() ? -1 : 1;
});
```

## File: `src/components/Settings.js`
```javascript
import {
  Checkbox,
  Pane,
  RadioGroup,
  SelectField,
  TextInputField,
} from 'evergreen-ui';
import { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import i18n from '../i18n';
import { Translations } from '../translations';
import './style.css';

export const Settings = (props) => {
  const { t } = useTranslation();
  const encryptionModes = [
    { label: t('wifi.password.encryption.none'), value: '' },
    { label: 'WPA/WPA2/WPA3', value: 'WPA' },
    { label: 'WPA2-EAP', value: 'WPA2-EAP' },
    { label: 'WEP', value: 'WEP' },
  ];
  const eapMethods = [{ label: 'PWD', value: 'PWD' }];

  const langSelectDefaultValue = () => {
    const t = Translations.filter((t) => t.id === i18n.language);
    if (t.length !== 1) {
      return 'en-US';
    }
    return t[0].id;
  };

  useEffect(() => {
    if (props.firstLoad.current && window.innerWidth < 500) {
      props.onFirstLoad();
      props.onOrientationChange(true);
    }
  });

  return (
    <Pane id="settings" maxWidth={props.settings.portrait ? '350px' : '100%'}>
      <SelectField
        width={300}
        inputHeight={38}
        label={t('select')}
        onChange={(e) => props.onLanguageChange(e.target.value)}
        defaultValue={langSelectDefaultValue()}
      >
        {Translations.map((t) => (
          <option key={t.id} value={t.id}>
            {t.name}
          </option>
        ))}
      </SelectField>

      <Checkbox
        label={t('button.rotate')}
        checked={props.settings.portrait}
        onChange={() => props.onOrientationChange(!props.settings.portrait)}
      />
      <Checkbox
        label={t('wifi.password.hide')}
        checked={props.settings.hidePassword}
        onChange={() =>
          props.onHidePasswordChange(!props.settings.hidePassword)
        }
      />
      <Checkbox
        label={t('wifi.name.hiddenSSID')}
        checked={props.settings.hiddenSSID}
        onChange={() => props.onHiddenSSIDChange(!props.settings.hiddenSSID)}
      />

      <Checkbox
        label={t('cards.tip.hide')}
        checked={props.settings.hideTip}
        onChange={() => props.onHideTipChange(!props.settings.hideTip)}
      />
      <TextInputField
        type="number"
        width={300}
        label={t('cards.additional')}
        value={props.settings.additionalCards}
        onChange={(e) => props.onAdditionalCardsChange(e.target.value)}
      />
      <RadioGroup
        label={t('wifi.password.encryption')}
        size={16}
        value={props.settings.encryptionMode}
        options={encryptionModes}
        onChange={(e) => props.onEncryptionModeChange(e.target.value)}
      />
      <RadioGroup
        label={t('wifi.encryption.eapMethod')}
        size={16}
        value={props.settings.eapMethod}
        options={eapMethods}
        className={`
          ${props.settings.encryptionMode !== 'WPA2-EAP' && 'hidden'}
        `}
        onChange={(e) => props.onEapMethodChange(e.target.value)}
      />
    </Pane>
  );
};
```

## File: `src/components/WifiCard.js`
```javascript
import {
  CameraIcon,
  Card,
  Heading,
  MobilePhoneIcon,
  Pane,
  Paragraph,
  Text,
  TextareaField,
} from 'evergreen-ui';
import { QRCodeSVG as QRCode } from 'qrcode.react';
import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import logo from '../../src/images/wifi.png';
import './style.css';

export const WifiCard = (props) => {
  const { t } = useTranslation();
  const [qrvalue, setQrvalue] = useState('');

  const escape = (v) => {
    const needsEscape = ['"', ';', ',', ':', '\\'];

    let escaped = '';
    for (const c of v) {
      if (needsEscape.includes(c)) {
        escaped += `\\${c}`;
      } else {
        escaped += c;
      }
    }
    return escaped;
  };

  useEffect(() => {
    let opts = {};

    opts.T = props.settings.encryptionMode || 'nopass';
    if (props.settings.encryptionMode === 'WPA2-EAP') {
      opts.E = props.settings.eapMethod;
      opts.I = props.settings.eapIdentity;
    }
    opts.S = escape(props.settings.ssid);
    opts.P = escape(props.settings.password);
    opts.H = props.settings.hiddenSSID;

    let data = '';
    Object.entries(opts).forEach(([k, v]) => (data += `${k}:${v};`));
    const qrval = `WIFI:${data};`;

    setQrvalue(qrval);
  }, [props.settings]);

  const portraitWidth = () => {
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    return isMobile ? '100%' : '280px';
  };

  const passwordFieldLabel = () => {
    const hiddenPassword =
      props.settings.hidePassword || !props.settings.encryptionMode;
    return hiddenPassword ? '' : t('wifi.password');
  };

  const eapIdentityFieldLabel = () => {
    const hiddenIdentity = props.settings.encryptionMode !== 'WPA2-EAP';
    return hiddenIdentity ? '' : t('wifi.identity');
  };

  const eapMethodFieldLabel = () => {
    return !eapIdentityFieldLabel() ? '' : t('wifi.encryption.eapMethod');
  };

  const keyid = props.keyid || '';
  const suffixKeyID = (prefix) => `${prefix}-${keyid}`;

  return (
    <Card
      className="card-print"
      elevation={3}
      style={{ maxWidth: props.settings.portrait ? portraitWidth() : '100%' }}
    >
      <Pane display="flex" paddingBottom={12}>
        <img alt="icon" src={logo} width="24" height="24" />
        <Heading
          size={700}
          paddingRight={10}
          paddingLeft={10}
          textAlign={props.settings.portrait ? 'center' : 'unset'}
        >
          {t('wifi.login')}
        </Heading>
      </Pane>

      <Pane
        className="details"
        style={{ flexDirection: props.settings.portrait ? 'column' : 'row' }}
      >
        <QRCode
          className="qrcode"
          style={{ marginBottom: props.settings.portrait ? '1em' : '0' }}
          value={qrvalue}
          size={150}
        />

        <Pane width={'100%'}>
          <TextareaField
            id={suffixKeyID('ssid')}
            type="text"
            marginBottom={5}
            autoComplete="off"
            autoCorrect="off"
            autoCapitalize="none"
            spellCheck={false}
            maxLength="32"
            label={t('wifi.name')}
            placeholder={t('wifi.name.placeholder')}
            value={props.settings.ssid}
            onChange={(e) => props.onSSIDChange(e.target.value)}
            isInvalid={!!props.ssidError}
            validationMessage={!!props.ssidError && props.ssidError}
          />
          {props.settings.encryptionMode === 'WPA2-EAP' && (
            <>
              <TextareaField
                id={suffixKeyID('eapmethod')}
                type="text"
                marginBottom={5}
                readOnly={true}
                spellCheck={false}
                label={eapMethodFieldLabel()}
                value={props.settings.eapMethod}
              />

              <TextareaField
                id={suffixKeyID('identity')}
                type="text"
                marginBottom={5}
                autoComplete="off"
                autoCorrect="off"
                autoCapitalize="none"
                spellCheck={false}
                label={eapIdentityFieldLabel()}
                placeholder={t('wifi.identity.placeholder')}
                value={props.settings.eapIdentity}
                onChange={(e) => props.onEapIdentityChange(e.target.value)}
                isInvalid={!!props.eapIdentityError}
                validationMessage={
                  !!props.eapIdentityError && props.eapIdentityError
                }
              />
            </>
          )}
          {!(props.settings.hidePassword || !props.settings.encryptionMode) && (
            <TextareaField
              id={suffixKeyID('password')}
              type="text"
              maxLength="63"
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="none"
              spellCheck={false}
              height={
                props.settings.portrait && props.settings.password.length > 40
                  ? '5em'
                  : 'auto'
              }
              marginBottom={5}
              label={passwordFieldLabel()}
              placeholder={t('wifi.password.placeholder')}
              value={props.settings.password}
              onChange={(e) => props.onPasswordChange(e.target.value)}
              isInvalid={!!props.passwordError}
              validationMessage={!!props.passwordError && props.passwordError}
            />
          )}
        </Pane>
      </Pane>
      {!props.settings.hideTip && (
        <>
          <hr />
          <Paragraph>
            <CameraIcon />
            <MobilePhoneIcon />
            <Text size={300} paddingRight={8} paddingLeft={8}>
              {t('wifi.tip')}
            </Text>
          </Paragraph>
        </>
      )}
    </Card>
  );
};
```

## File: `src/components/style.css`
```css
@font-face {
  font-family: 'Source Serif';
  src: url(./SourceSerif4-Semibold.otf);
}

.card-print {
  border-color: #aaa;
  margin-bottom: 1em;
  margin-top: 2em;
  padding: 1em;
}

#print-area {
  display: none;
}

.details {
  display: flex;
  align-items: center;
}

.qrcode {
  max-width: 175px;
  padding: 1em;
}

.hidden {
  display: none;
}
textarea {
  background-color: #fff;
  border: solid 1px #ddd;
  font-family: 'Source Serif', serif !important;
  font-size: 1.2em !important;
  margin-bottom: 0;
  height: 40px !important;
  min-height: 0px !important;
  overflow: hidden;
  resize: none;
}
textarea#password {
  height: 60px !important;
}

hr {
  margin-top: 0;
}

button {
  height: 50px;
  width: 180px;
}

#settings {
  margin-bottom: 1em;
  padding: 1em;
}

#settings label span {
  margin-right: 8px;
}

@media print {
  body * {
    visibility: hidden;
  }
  #print-area,
  #print-area * {
    visibility: visible;
    /* For printing, use a font stack that prioritizes system fonts 
       to ensure CJK characters are rendered correctly in Chrome. */
    font-family:
      'PingFang SC', 'Noto Sans SC', 'Noto Sans TC', 'Noto Sans JP',
      'Noto Sans KR', 'Microsoft YaHei', serif;
    font-weight: 500;
    font-style: semibold;
  }
  #print-area {
    position: absolute;
    left: 0;
    top: 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    row-gap: 0em;
  }
  .card-print {
    border-style: dashed;
    box-shadow: none;
    margin-bottom: 0;
    margin-top: 0;
    break-inside: avoid;
    page-break-inside: avoid;
  }
}
```

