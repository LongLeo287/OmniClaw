---
id: netflix
type: knowledge
owner: OA_Triage
---
# netflix
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "netflix-clone",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.11.4",
    "@testing-library/react": "^11.1.0",
    "@testing-library/user-event": "^12.1.10",
    "classnames": "^2.3.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.3.0",
    "react-scripts": "4.0.3",
    "sass": "^1.93.3",
    "url-search-params": "^1.1.0",
    "web-vitals": "^1.0.1"
  },
  "scripts": {
    "start": "cross-env NODE_OPTIONS=--openssl-legacy-provider react-scripts start",
    "build": "cross-env NODE_OPTIONS=--openssl-legacy-provider react-scripts build",
    "test": "cross-env NODE_OPTIONS=--openssl-legacy-provider react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
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
  "devDependencies": {
    "cross-env": "^10.1.0"
  }
}

```

### File: README.md
```md
# Netflix Clone
    Netflix Clone using React JS


![image](https://user-images.githubusercontent.com/61585443/185205338-c20bb089-618f-49e2-b740-1c02838030a4.png)



<h3>Stargazers</h3>

[![Stargazers repo roster for @Yashkapure06/netflix-clone](https://reporoster.com/stars/dark/Yashkapure06/netflix-clone)](https://github.com/Yashkapure06/netflix-clone/stargazers)
        
        
***
#### How to install ReactJs?

``` npx create-react-app@latest app-name ```
***
#### Fetched Data of All the movies from [TMDB](https://www.themoviedb.org/)
    1. Create an account in 
[TMDB](https://www.themoviedb.org/)

    2. Go to settings
    3. You will find API Option, u can create A new api by reading the guide lines.
***
* ### Installation

    *
     ```
     git clone https://github.com/Yashkapure06/netflix-clone.git
    ```
    *  ```cd netflix-clone```
    * ``` npm install ``` - To install all the dependencies

```

### File: src\index.js
```js
import React from 'react';
import ReactDOM from 'react-dom';

import App from './App';

import './index.scss';


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

```

### File: jsconfig.json
```json
{
  "compilerOptions": {
    "baseUrl": "src"
  },
  "include": [
    "src"
  ]
}
```

### File: public\index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Netflix Clone. A React.js Clone that allows you to watch Netflix movies and TV shows. Here you will find the latest trailers of new movies and webseries. "
    />
    <meta name="keywords" content="Netflix Clone, Yash Kapure Netflix Clone, github, git, yash kapure, yash kapure portfolio, projects, yash kapure github, git, yash kapure "/>
    <meta name="author" content="Yash Kapure"/>
    <meta name="robots" content="index, follow"/>
    <meta name="revisit-after" content="1 days"/>
    <meta name="googlebot" content="index, follow"/>
    <meta name="googlebot-news" content="index, follow"/>
    <meta name="googlebot-image" content="index, follow"/>
    <meta name="googlebot-video" content="index, follow"/>
    <meta name="googlebot-mobile" content="index, follow"/>
    <meta name="googlebot-ads" content="index, follow"/>
    <meta name="rating" content="general"/>
    <meta name="distribution" content="global"/>
    <meta name="expires" content="never"/>
    <meta name="language" content="en-US"/>
    <meta name="doc-type" content="Clone"/>
    <meta name="doc-class" content="Completed"/>
    <meta name="doc-rights" content="Public"/>
    <meta name="doc-publisher" content="Yash Kapure"/>
    <meta name="doc-author" content="Yash Kapure"/>
    <meta property="og:image" content="./images/metaimg.png">
    <meta property="og:image:secure_url" content="./images/metaimg.png">
    <meta property="og:image:type" content="image/jpeg" />
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    
    <title>Netflix</title>
    <style>
      ::-webkit-scrollbar {
        width: 10px;
        background-color: #000000;
      }
      ::-webkit-scrollbar-thumb {
        background-color: #ff1c0b;
      }
    </style>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
   
  </body>
</html>

```

### File: public\manifest.json
```json
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
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
import React from "react";
import HomePage from "./pages/HomePage";

const App = () =>  {
  return (
    <div className="app">
      <HomePage/>
    </div>
  );
}

export default App;

```

### File: src\secrets.json
```json
{
  "TMDB_API_KEY": "039bfd3babb13485045791cbbd18c638"
}
```

### File: src\api\tmdb.js
```js
import Api from "../utils/api";

const API_BASE = "https://api.themoviedb.org/3";
// Create React App replaces process.env.REACT_APP_* at build time with actual values
// Fallback to direct API key if env var is not set (for development/local builds)
const API_KEY =
  process.env.REACT_APP_TMDB_API_KEY || "039bfd3babb13485045791cbbd18c638";

const tmdb = new Api({
  baseUrl: API_BASE,
  searchParams: { api_key: API_KEY },
});

export default tmdb;

```

### File: src\components\Banner.js
```js
import React, { useState, useEffect } from 'react';


import { generateImageUrl, ImageSizes } from '../utils/tmdb';
import tmdbApi from '../api/tmdb';

const Banner = () => {

    const [movie, setMovie] = useState({});

  useEffect(() => {
    const fetchBannerMovie = async () => {
      const json = await tmdbApi.get("/discover/tv", { with_networks: 213 });
      setMovie(
        json.results[
          Math.floor(Math.random() * json.results.length - 1)
        ]
      );
    };
    fetchBannerMovie();
    
  }, []);

  return (
    <div
      className="banner"
      style={{
        backgroundImage: `url(${generateImageUrl(movie?.backdrop_path || '', ImageSizes.backdrop)})`,
      }}
    >
      <div className="banner__contents">
        <h1 className="banner__title">
          {movie?.title || movie?.name || movie?.original_name}
        </h1>
        <div className="banner__buttons">
          <button className="banner__button">Play</button>
          <button className="banner__button">My List</button>
        </div>
        <h1 className="banner__description">
          {movie?.overview}
        </h1>
      </div>
      <div className="banner__cover" />
    </div>
  );
}

export default Banner;

```

### File: src\components\Cards.js
```js
import React, { useState } from 'react';
import classNames from 'classnames';


import { generateImageUrl, ImageSizes } from "../utils/tmdb";
import TrailerModal from './TrailerModal';


const Cards = ({ media, mediaType, isLarge }) => {

    const [ isTrailerOpen, setTrailerOpen ] = useState(false);

    return (
        <>
            <div
                key={media.id}
                className="media-card"
                onClick={() => setTrailerOpen(true)}
            >
                <img
                className={classNames(
                    'media-card__poster',
                    { 'media-card__poster--large': isLarge },
                )}
                src={
                    isLarge
                    ? generateImageUrl(media.poster_path, ImageSizes.poster)
                    : generateImageUrl(media.backdrop_path, ImageSizes.card)
                }
                alt={media.original_title}
                />
                <div className="media-card__cover">
                    <div className="media-card__name">
                        {media.title || media.name || media.original_name}
                    </div>
                    <div className="media-card__description">
                        {media.overview}
                    </div>
                </div>
            </div>
            {isTrailerOpen && (
                <TrailerModal
                    mediaType={mediaType}
                    mediaId={media.id}
                    media={media}
                    onClose={() => setTrailerOpen(false)}
                />
            )}
        </>
    );
}

export default Cards;

```

### File: src\components\Header.js
```js
import React, { useState, useEffect } from 'react';
import classNames from 'classnames';



import logo from '../assets/logo-full.png';
import smallLogo from '../assets/logo.png';

const Header = () => {

    const [ floating, setFloating ] = useState(false);

    useEffect(()=>{
        function handleScroll() {
            if( window.scrollY > 100 ) {
                setFloating(true);
            } else {
                setFloating(false);
            }
        }

        window.addEventListener("scroll",handleScroll);
        return () => {
            window.removeEventListener("scroll",handleScroll);
        }

    },[])



    return (
        <div
            className={classNames(
                "header",
                { 'header--float': floating }
            )}
            >
            <img
                className="header__logo"
                src={logo}
                alt="Netflix logo"
            />
            <img
                className="header__avatar"
                src={smallLogo}
                alt="Netflix avatar"
            />
        </div>
    );
}

export default Header;

```

### File: src\components\Slider.js
```js
import React, { useState, useEffect } from "react";

import tmdbApi from "../api/tmdb";
import Cards from "./Cards";

const Slider = ({ mediaType, title, path, params = {}, isLarge }) => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const json = await tmdbApi.get(path, params);
      setItems(json.results);
    };
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="media-slider">
      <h3 className="media-slider__title">{title}</h3>
      <div className="media-slider__cards">
        {items.map((media) => (
          <Cards
            isLarge={isLarge}
            key={media.id}
            media={media}
            mediaType={media.media_type || mediaType}
          />
        ))}
      </div>
    </div>
  );
};

export default Slider;

```

### File: src\components\TrailerModal.js
```js
import React, { useEffect, useState } from 'react';
import tmdbApi from '../api/tmdb';

const TrailerModal = ({ mediaType, mediaId, onClose }) => {
    
    const [videoId, setVideoId ] = useState(null);
    
    
    useEffect(()=>{
        const fetchTrailer  = async () => {
            const json  = await tmdbApi.get(`/${mediaType}/${mediaId}/videos`);
            const video = json.results.find(o => o.site === 'YouTube');
            setVideoId(video?.key);
        }

        fetchTrailer();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    },[])

    return (
        <>
            <div className="trailer-modal-backdrop" onClick={onClose} />
            <div className="trailer-modal">
            {videoId && (
                <iframe
                    width="100%"
                    height="100%"
                    src={`https://www.youtube.com/embed/${videoId}`}
                    title="YouTube video player"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                />
            )}
                <button
                    className="trailer-modal__close"
                    onClick={onClose}
                >
                    ✕
                </button>
            </div>
        </>
    );
}

export default TrailerModal;

```

### File: src\pages\HomePage.js
```js
import React from 'react';

import Header from '../components/Header';
import Banner from '../components/Banner';
import Slider from '../components/Slider';

const HomePage = () => {
    return (
        <div>
            <Header/>
            <Banner/>
            <Slider
                mediaType="tv"
                title="NETFLIX ORIGINALS"
                path="/discover/tv"
                params={{ with_networks: 213 }}
                isLarge
            />
            <Slider
                title="TRENDING NOW"
                path="/trending/all/week"
            />
            <Slider
                mediaType="movie"
                title="TOP RATED"
                path="/movie/top_rated"
            />
            <Slider
                mediaType="movie"
                title="ACTION MOVIES"
                path="/discover/movie"
                params={{ with_genres: 28 }}
            />


        </div>
    );
}

export default HomePage;

```

### File: src\utils\api.js
```js
// import path from 'path';
// import qs from 'query-string';
import URLSearchParams from 'url-search-params';

class Api {
  constructor({ baseUrl, searchParams }) {
    this._baseUrl = baseUrl;
    this._baseSearchParams = searchParams || {};
  }

  async get(endpoint, params) {
    const hitUrl = this._generateUrl(endpoint, params);
    const response = await fetch(hitUrl, {
      method: 'GET',
    });

    return this._parseJsonResponse(response);
  }

  async _parseJsonResponse(response) {
    let json = null;
    try {
      json = await response.json();
    } catch (e) {
      console.log(e);
    }

    if (response.ok) {
      return json;
    } else {
      const error = new Error(response.statusText);
      error.isFromServer = true;
      error.response = response;
      error.responseJson = json;

      throw error;
    }
  }

  _generateUrl(endpoint, params) {
    const search = new URLSearchParams(this._baseSearchParams);
    // const search = qs.stringify({ ...this._baseSearchParams, ...params });
    // const url = path.join(this._baseUrl, endpoint);
    const url = `${this._baseUrl}${endpoint}`;
    return `${url}?${search}`;
    // return [url, search].join('?');
  }
}

export default Api;

```

### File: src\utils\tmdb.js
```js
// import path from 'path';

const IMAGE_BASE_URL = "https://image.tmdb.org/t/p";

export const ImageSizes = {
  poster: 'w500',
  card: 'w300',
  backdrop: 'w1280',
};

export function generateImageUrl(imagePath, size) {
  return `${IMAGE_BASE_URL}/${size}${imagePath}`;
  // return path.join(IMAGE_BASE_URL, size, imagePath);
}

export function filterPreferredResults(results) {
  return results.filter((o) => ['movie', 'tv'].includes(o.media_type));
}

```

