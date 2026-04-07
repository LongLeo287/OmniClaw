---
id: wifi
type: knowledge
owner: OA_Triage
---
# wifi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: README.md
```md
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

### File: src\index.js
```js
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

### File: .prettierrc.json
```json
{
  "trailingComma": "es5",
  "semi": true,
  "singleQuote": true
}

```

### File: LICENSE.md
```md
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

### File: public\index.html
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

### File: public\manifest.json
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

### File: public\robots.txt
```txt
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:

```

### File: src\App.js
```js
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

### File: src\i18n.js
```js
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

### File: src\style.css
```css
body {
  margin: 0 auto;
  max-width: 500px;
  padding: 1em;
}

```

### File: src\translations.js
```js
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
... [TRUNCATED]
```

### File: src\components\Settings.js
```js
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

### File: src\components\style.css
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

### File: src\components\WifiCard.js
```js
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

