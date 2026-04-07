---
id: elementor
type: knowledge
owner: OA_Triage
---
# elementor
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "elementor",
  "slug": "elementor",
  "version": "4.1.0",
  "packageManager": "npm@10.0.0",
  "author": "Elementor Team",
  "homepage": "https://elementor.com/",
  "scripts": {
    "create-release-branch": "node scripts/create-version-change.js",
    "start": "npm run composer:no-dev && npm run build:packages && npm run styles && npm run scripts",
    "watch": "npm run build:tools && npm run composer:no-dev && npx concurrently \"npm run watch:packages\" \"npm run styles:watch\" \"npm run scripts:watch\"",
    "watch:packages": "concurrently 'turbo dev --parallel' 'tsc -w --project packages/tsconfig.json'",
    "build": "npm run build:packages && grunt build",
    "build:docker": "rm -rf docker-output && docker build --target output --output type=local,dest=./docker-output . && cd docker-output/elementor && zip -r elementor.zip . && echo 'Build output available in ./docker-output/elementor/elementor.zip'",
    "build:packages": "turbo build",
    "build:tools": "turbo build --filter='./packages/packages/tools/*'",
    "build:ci": "turbo build --concurrency 1 && npx grunt webpack:production",
    "install": "npm ci --ignore-scripts && composer install",
    "install:ci": "npm ci --ignore-scripts",
    "composer:no-dev": "composer install --optimize-autoloader --prefer-dist && composer install --no-scripts --no-dev && composer dump-autoload",
    "reinstall": "rm -rf node_modules && npm cache clean --force && npm ci",
    "hard-reinstall": "rm -rf node_modules **/node_modules package-lock.json && npm cache clean --force && npm i --ignore-scripts",
    "env:setup": "bash scripts/setup-test-environment.sh",
    "env:setup:with-playwright": "bash scripts/setup-test-environment.sh && npx playwright install chromium",
    "wp-env": "wp-env",
    "test:linux": "node ./run-on-linux.js",
    "setup-templates": "rm -rf ./templates && mkdir -p ./templates/playwright && mkdir -p ./templates/lighthouse && cp ./tests/playwright/templates/* ./templates/playwright && cp ./tests/lighthouse/templates/* ./templates/lighthouse",
    "start-local-server": "npm run setup-templates && wp-lite-env start --config=./tests/playwright/.playwright-wp-lite-env.json --port=8888 && wp-lite-env start --config=./tests/playwright/.playwright-wp-lite-env.json --port=8889",
    "test:php": "docker-compose run --rm wordpress_phpunit phpunit",
    "test:php_multisite": "docker-compose run -e WP_MULTISITE=1 --rm wordpress_phpunit phpunit",
    "test:setup:playwright": "wp-lite-env cli --config=./tests/playwright/.playwright-wp-lite-env.json --port=8888 --command=\"bash elementor-config/setup.sh\" && wp-lite-env cli --config=./tests/playwright/.playwright-wp-lite-env.json --port=8889 --command=\"bash elementor-config/setup.sh\"",
    "test:playwright": "playwright test -c tests/playwright/playwright.config.ts",
    "test:playwright:debug": "npm run test:playwright -- --debug",
    "test:playwright:elements-regression": "playwright test -c tests/elements-regression/playwright.config.ts",
    "test:playwright:elements-regression:core": "playwright test -c tests/elements-regression/playwright.config.ts tests/elements-regression/tests/elements-regression.test.ts",
    "test:playwright:elements-regression:atomic": "playwright test -c tests/elements-regression/playwright.config.ts tests/elements-regression/tests/atomic-elements-regression.test.ts",
    "test:playwright:elements-regression:linux": "node ./tests/elements-regression/scripts/run-on-linux.js",
    "test:playwright:elements-regression:linux:update-snapshots": "npm run test:playwright:elements-regression:linux -- -u",
    "test:jest": "jest --config='./tests/jest/jest.config.js'",
    "test:packages": "jest --config='./packages/jest.config.js'",
    "test": "npm run test:jest && npm run test:packages",
    "scripts": "grunt scripts",
    "scripts:watch": "grunt watch_scripts",
    "styles": "grunt styles",
    "styles:watch": "grunt watch_styles",
    "lint": "eslint . && npm run lint -w elementor-packages",
    "format": "eslint . --fix && npm run format:packages",
    "format:packages": "npm run format -w elementor-packages",
    "setup:testing": "bash scripts/setup-testing.sh",
    "restart:testing": "bash scripts/setup-testing.sh --restart",
    "packages:version": "npm run version -w elementor-packages",
    "packages:release": "turbo build && npm run release -w elementor-packages",
    "wp-playground": "npx -y @wp-playground/cli server --mount=.:/wordpress/wp-content/plugins/elementor --blueprint=./tests/playwright/blueprints/local.json",
    "wp-playground:ci": "npx -y @wp-playground/cli server --mount=./build:/wordpress/wp-content/plugins/elementor --blueprint=./tests/playwright/blueprints/ci.json",
    "full-e2e-local": "npx concurrently \"npm run watch\" \"npm run wp-playground\" \"npm run test:playwright -- --ui\"",
    "prepare": "husky"
  },
  "engines": {
    "node": ">=20.19.0",
    "npm": ">=10.0.0"
  },
  "workspaces": [
    "packages",
    "packages/packages/tools/*",
    "packages/packages/libs/*",
    "packages/packages/core/*",
    "packages/apps/*"
  ],
  "devDependencies": {
    "@actions/core": "^1.11.1",
    "@axe-core/playwright": "^4.10.1",
    "@babel/core": "^7.26.0",
    "@babel/eslint-parser": "^7.25.7",
    "@babel/plugin-syntax-import-assertions": "^7.26.0",
    "@babel/plugin-transform-modules-commonjs": "^7.26.3",
    "@babel/plugin-transform-react-jsx": "^7.25.9",
    "@babel/plugin-transform-runtime": "^7.25.9",
    "@babel/preset-env": "^7.26.0",
    "@babel/preset-react": "^7.26.3",
    "@babel/preset-typescript": "^7.26.0",
    "@babel/runtime-corejs3": "^7.26.0",
    "@elementor/wp-lite-env": "^0.0.20",
    "@jest/globals": "~29.7.0",
    "@lodder/grunt-postcss": "^3.1.1",
    "@playwright/test": "~1.54.1",
    "@swc/core": "^1.10.1",
    "@swc/jest": "^0.2.37",
    "@tanstack/eslint-plugin-query": "^5.81.2",
    "@testing-library/dom": "^10.4.0",
    "@testing-library/jest-dom": "^6.6.3",
    "@testing-library/react": "^16.1.0",
    "@types/glob": "^8.1.0",
    "@types/jest": "^29.5.14",
    "@types/react-dom": "^18.3.1",
    "@wordpress/babel-plugin-import-jsx-pragma": "^5.9.0",
    "@wordpress/babel-preset-default": "^3.0.2",
    "@wordpress/eslint-plugin": "^17.2.0",
    "@wp-playground/client": "^2.0.13",
    "allure-playwright": "^2.10.0",
    "autoprefixer": "^10.4.20",
    "babel-jest": "^29.7.0",
    "babel-loader": "^9.2.1",
    "baseline-browser-mapping": "^2.9.19",
    "chalk": "^5.3.0",
    "commander": "^14.0.0",
    "concurrently": "^9.2.0",
    "cross-env": "^7.0.3",
    "cspell": "^8.17.1",
    "cssnano": "^7.0.6",
    "dotenv": "^16.4.7",
    "eslint": "^8.57.1",
    "eslint-import-resolver-typescript": "^3.6.3",
    "eslint-plugin-babel": "^5.3.1",
    "eslint-plugin-import": "^2.31.0",
    "eslint-plugin-jest-dom": "^5.4.0",
    "eslint-plugin-local-rules": "^3.0.2",
    "eslint-plugin-no-jquery": "^2.7.0",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-compiler": "latest",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "eslint-plugin-testing-library": "^7.2.0",
    "eslint-plugin-unicorn": "^56.0.1",
    "eslint-webpack-plugin": "^4.0.1",
    "glob": "^11.0.3",
    "grunt": "^1.5.3",
    "grunt-banner": "~0.6.0",
    "grunt-checktextdomain": "~1.0.1",
    "grunt-cli": "^1.5.0",
    "grunt-concurrent": "^3.0.0",
    "grunt-contrib-clean": "~2.0.1",
    "grunt-contrib-copy": "~1.0.0",
    "grunt-contrib-sass": "~2.0.0",
    "grunt-contrib-watch": "^1.1.0",
    "grunt-karma": "4.0.2",
    "grunt-sass": "^3.1.0",
    "grunt-webpack": "^7.0.0",
    "husky": "^9.1.7",
    "jest": "^29.7.0",
    "jest-environment-jsdom": "^29.7.0",
    "karma": "^6.4.4",
    "karma-chrome-launcher": "^3.2.0",
    "karma-coverage": "^2.2.1",
    "karma-coverage-istanbul-reporter": "3.0.3",
    "karma-fail-fast-reporter": "1.0.5",
    "karma-fixture": "0.2.6",
    "karma-html2js-preprocessor": "1.1.0",
    "karma-qunit": "^4.2.1",
    "karma-remap-coverage": "0.1.5",
    "knip": "^5.54.1",
    "lighthouse": "^12.3.0",
    "lint-staged": "^16.2.7",
    "load-grunt-tasks": "^5.1.0",
    "mini-css-extract-plugin": "^2.9.2",
    "msw": "^2.6.8",
    "path": "^0.12.7",
    "playwright-lighthouse": "^4.0.0",
    "prettier": "npm:wp-prettier@^3.0.3",
    "qunit": "^2.23.1",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-query": "^3.39.1",
    "sass": "^1.83.0",
    "semver": "^7.7.2",
    "styled-components": "^6.1.13",
    "terser-webpack-plugin": "^5.3.11",
    "ts-node": "^10.9.2",
    "tsup": "^8.3.5",
    "turbo": "^2.3.3",
    "typescript": "^5.7.2",
    "webpack": "^5.97.1",
    "write": "^2.0.0"
  },
  "dependencies": {
    "@elementor/elementor-one-assets": "0.4.33",
    "@elementor/icons": "1.72.0",
    "@elementor/ui": "1.36.17",
    "@reach/router": "1.3.4",
    "@reduxjs/toolkit": "^1.8.3",
    "@woocommerce/admin-layout": "^1.1.0",
    "@wordpress/components": "^27.4.0",
    "@wordpress/core-data": "^7.5.0",
    "@wordpress/data": "^10.5.0",
    "@wordpress/dom-ready": "^3.45.0",
    "@wordpress/element": "^5.22.0",
    "@wordpress/plugins": "^7.5.0",
    "dayjs": "^1.11.18",
    "dompurify": "^3.2.6",
    "html-to-image": "^1.11.11",
    "mime": "^3.0.0",
    "mixpanel-browser": "^2.50.0",
    "prop-types": "^15.8.1",
    "reach-router-hash-history": "0.0.3",
    "react-avatar-editor": "^13.0.0",
    "react-draggable": "^4.4.5",
    "react-infinite-scroller": "^1.2.6",
    "react-markdown": "^8.0.5",
    "react-redux": "^8.1.3",
    "react-sketch-canvas": "^6.2.0",
    "validator": "^13.11.0"
  },
  "overrides": {
    "nwsapi": "2.2.13",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-redux": "^8.1.3",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.3.1",
    "date-fns": "^3.6.0",
    "scheduler": "^0.20.0",
    "form-data": "4.0.4",
    "baseline-browser-mapping": "^2.9.19"
  },
  "lint-staged": {
    "packages/**/*.{js,jsx,ts,tsx}": [
      "node scripts/lint-packages-staged.js"
    ],
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix"
    ]
  }
}

```

### File: README.md
```md
# <a href="https://elemn.to/gh-to-elementor"><img src="/.github/assets/elementor-logo--gh-repo.svg" alt="Elementor Website Builder"></a>

Welcome to the Elementor GitHub repository!

**Elementor is the most advanced front-end drag-and-drop website builder. Create high-end, pixel-perfect websites at record speeds. Build any theme, any page, and any design with no code.**

<br>

<p><a href="https://elemn.to/gh-to-elementor"><img src="/.github/assets/elementor-github-cover.gif" alt="Elementor Website Builder"></a></p>

<br>

Introducing a WordPress website builder with no limits of design. A website builder that delivers high-end page designs and advanced capabilities never before seen on WordPress.

**It's time for [Elementor Website Builder](https://elemn.to/gh-to-elementor)**.

### The leading website builder for any purpose

Whether you are a web designer looking for a way to achieve pixel-perfect websites, a marketer looking to get online fast, or a developer who wants to expand their capabilities, Elementor's website builder has what you need - intuitive drag-and-drop Editor, advanced design features and a complete open-source approach.

There are many other [features](https://elemn.to/gh-to-features) to help you build better websites. Join the elite web professionals who enjoy [Elementor One](https://elemn.to/gh-to-elementor-pro)!

## Elementor Roadmap

Discover what's Next in Elementor. Visit the [Elementor Roadmap](https://elemn.to/gh-to-roadmap) and learn about the status of upcoming or newly-released features.

## Developer API

Elementor website builder is free and open source. It's the perfect plugin to extend and integrate further. It was envisioned with the developer in mind, and we have already seen some truly remarkable addons created by many skilled developers.

To help you get started and learn just how to integrate with Elementor, we have created the official [Elementor Developers Center](https://elemn.to/gh-to-dev-center).

Check the [Developers Blog](https://elemn.to/gh-to-dev-blog) to discover the latest information from our engineers working on the newest Elementor versions, or visit the [Developers Documentation](https://elemn.to/gh-to-dev-docs) to learn how to extend Elementor and create your Addons.

#### Developers Community

[Join our Developers Community](https://elemn.to/dev-community) and share tips, tricks, and knowledge with other developers about extending and developing Addons for Elementor.

## Be a Contributor

Community contributions are always welcomed and help us remain the Number 1 WordPress Website Builder. Feel free to answer questions on GitHub and within the various Elementor communities.

There are many ways to contribute to Elementor:

### Contribution Guidelines

Please read our [Contribution Guidelines](https://elemn.to/gh-contributing) to learn the best practices for contributing to Elementor.

### Bug Report

If you found a bug in the source code and can reproduce it consistently after troubleshooting it, you can help us by [submitting a Bug Report](https://elemn.to/gh-new-bug-report).

Even better, you can [submit a Pull Request](https://elemn.to/gh-new-pr) with a fix, and we will happily review it.

### Security Report

Join our community-driven [Bug Bounty programs](https://elemn.to/gh-to-bounty-programs).

We leverage the collective expertise of our community, offering round-the-clock crowdsourced vulnerability detection. The programs provide a comprehensive overview of features and endpoints considered 'in scope,' reward specifics where relevant, and our complete terms and conditions.

To learn more about our security efforts, visit our [Trust Center](https://elemn.to/gh-to-trust-center). Security issues can be reported through our dedicated [Bug Bounty Programs page](https://elemn.to/gh-to-bounty-programs).

### Feature Request

Do you have a brilliant idea, enhancement, or feature you would love to see in Elementor? We're all ears!

Suggest new ideas, features, or enhancements by [submitting a Feature Request](https://elemn.to/gh-new-feature-request).
<br>You can also support existing ideas by [voting for your favorite requests](https://elemn.to/gh-feature-requests).

### Translate

The Elementor User Interface was designed with a global audience in mind. It supports a wide range of languages and is also RTL compatible. Out of the box, we offer support for over 60 languages.

Want to make a difference? <br>We would appreciate your contribution by adding a new language or helping translate existing ones at [translate.wordpress.org](https://elemn.to/translate-repo). To assist you, we've built a short guide explaining [how to translate and localize the plugin](https://elemn.to/gh-to-help-localize-elementor).

## Support

### Need Help, Guidance, Assistance, or Support?

Use one of the support channels below to find solutions to your questions and get assistance.

#### Note that we are unable to offer any support through this repository.

Please **DO NOT** open issues or discussions to request support.
<br>For those, use the appropriate channels.

#### Find out how to [submit a Support Ticket here](https://elemn.to/support-ticket).

Alternatively, you can visit one of these resources:

-   **Help Center** <br>Visit the [Elementor Help Center](https://elemn.to/gh-to-help-center) to find solutions to the most frequent problems, or read the documentation about Elementor's many features.
-   **Academy** <br>Grow your Web Creator skills and learn to make the most of Elementor in the [Elementor Academy](https://elemn.to/gh-to-academy).
-   **Global Community** <br>Join the [Elementor Global Community](https://elemn.to/community-on-fb) on Facebook. Where all kinds of users come together to help each other.
-   **Support Forum** <br>If you have more questions, visit the free [Support Forum](https://elemn.to/wp-support-forum) on our WordPress plugin page.
-   **Elementor Website** <br>For more information about features, FAQs, and documentation, check out our website at [Elementor Website Builder](https://elemn.to/gh-to-elementor).

**If you have an active [Elementor Pro](https://elemn.to/gh-to-elementor-pro) subscription, you are entitled to personal support. Please see your purchase email or visit your [Elementor Account page](https://elemn.to/my-elementor) for details.**

## Liked Elementor?

-   Join the [Elementor Global Community](https://elemn.to/community-on-fb) on Facebook.
-   Learn from our tutorials on [Elementor's YouTube Channel](https://elemn.to/yt).
-   Or [rate us on WordPress](https://elemn.to/gh-to-wp-new-review). It would mean the world to us! :)
```

### File: readme.txt
```txt
=== Elementor Website Builder - more than just a page builder ===
Contributors: elemntor
Tags: page builder, editor, landing page, drag-and-drop, elementor,
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
Stable tag: 3.34.2
Beta tag: 3.34.0-beta3
License: GPLv3
License URI: https://www.gnu.org/licenses/gpl-3.0.html

The Elementor Website Builder has it all: drag and drop page builder, Atomic Editor, pixel perfect design, global and reusable style systems, mobile responsive editing, and more. Get started now!

== Description ==

https://www.youtube.com/watch?v=ROEC0CPRO3w

= THE #1 NO CODE DRAG & DROP WORDPRESS WEBSITE BUILDER POWERING 22M+ WEBSITES WORLDWIDE, NOW WITH AI. =

Elementor, the leading WordPress website creation platform, empowers you to build professional, pixel-perfect websites seamlessly with its no-code, drag-and-drop Atomic Editor.

Supporting the full website lifecycle, Elementor enables you to confidently build, optimize, and manage your website with extended capabilities such as AI-powered creation, image optimization, transactional email delivery, accessibility tools, performance boosters, and more.

Now in version 4 - the Atomic Editor! Introducing a new generation of performance-first atomic building blocks that allow you to control every atomic part with no limits or locked layouts. Define your global design systems and reusable components once, and they apply everywhere instantly - turning hours or even days of work into single clicks.

Unlock all features with **[Elementor One](https://go.elementor.com/wp-repo-description-tab-elementor-pro-pro-features/)**.

Need fast and secure cloud hosting for your Elementor site? Try out **[Elementor Host](https://elemn.to/repo-hosting)** Powered by Google Cloud & Cloudflare. 4.9/5 TrustPilot score.

### 🌟 Create Professional Stunning Websites

- **[Intuitive Drag & Drop Builder](https://go.elementor.com/feature-page-editor/)**: Build any website with our no-code, drag-and-drop Editor. Achieve design precision with full control over layout and style.
- **[Pixel-Perfect Design Tools](https://go.elementor.com/wp-repo-description-tab-pro-features-feature-page/)**: Upload SVGs, apply masks, gradients, box shadows, headline effects, shape dividers, and use built-in CSS controls for advanced customization.
- **[Template Library](https://go.elementor.com/wp-repo-description-tab-library-full-website-kit/)**: Apply complete website kits for instant setups, or choose from a vast library of single pages, blocks, and pop-up templates.
- **[Advanced Widgets](https://go.elementor.com/feature-page-editor/)**: Access over 40 FREE widgets, including heading, image, text editor, video, button, gallery, carousels, and more.
- **[AI Capabilities](https://go.elementor.com/wp-repo-description-tab-elementor-ai/)**: Revolutionize your design and content creation process with native AI integration. Instantly create sections, text, code, and images.

= 🗝️ Key features: =

- **[Design System](https://go.elementor.com/feature-page-global-settings/)**: Use Variables and Classes for consistent colors, typography, and design elements, ensuring a cohesive, professional look that updates everywhere globally.
- **[Responsive Design](https://go.elementor.com/feature-page-responsive-design/)**: Optimize your design for every device with custom breakpoints, ensuring a seamless desktop, tablet, and mobile experience.
- **Mask Shapes**: Turning any element, like an image or video, into whatever shape you desire to create standout designs.
- **CSS Transform**: Use CSS Transform to rotate, scale, and skew elements, adding dynamic styling to your site.
- **Entrance Animations**: Add entrance animations to elements to create engaging and interactive user experiences.
- **[Revision History](https://elementor.com/features/#SaveBackup)**: Elementor’s Revision History feature enables users to track and revert to previous versions of their designs, providing peace of mind and flexibility during the creative process.
- **[Developer-Friendly](https://go.elementor.com/wp-repo-description-tab-developers-developers-website/)**: Equipped with extensive documentation, API, developer tools, and custom code areas, Elementor offers a conducive environment for developers to extend its capabilities and create custom solutions.
- **[Floating Buttons](https://elementor.com/features/contact-button/)**: Enhance user interaction with customizable, floating action buttons that stay in view as users scroll.
- **Components [Pro]**: Reuse the same building blocks across pages and sites, and update them everywhere they appear. Including controlled content editing, allowing collaborators and clients to update only exposed content properties without breaking layout or styling.
- **[Theme Builder](https://go.elementor.com/wp-repo-description-tab-pro-features-industry-leading-theme-builder/) [Pro]**: Design every part of your site—headers, footers, posts, and archives—for complete control over appearance.
- **[Popup Builder](https://go.elementor.com/wp-repo-description-tab-pro-features-popup-builder/) [Pro]**: Create eye-catching popups with Elementor’s Popup Builder, equipped with advanced targeting and triggering options to optimize user engagement and conversions.
- **[Forms](https://go.elementor.com/wp-repo-description-tab-pro-features-professional-form-builder-and-submission-log/) [Pro]**: Design and integrate custom forms, utilizing advanced features and integrations to capture and manage submissions effectively.
- **[WooCommerce Builder](https://go.elementor.com/wp-repo-description-tab-pro-features-woocommerce-builder/) [Pro]**:  Integrate Elementor with WooCommerce to design custom product pages, shop layouts, archives, carts, checkout pages, my account, and more, enhancing your store’s visual appeal and functionality.
- **[Dynamic Content](https://go.elementor.com/wp-repo-description-tab-pro-features-dynamic-content/) [Pro]**: Leverage dynamic content capabilities to create personalized and interactive web experiences by connecting your designs to various data sources.
- **[Notes](https://go.elementor.com/features-page-notes/) [Pro]**: Enhance team collaboration by using Elementor’s Notes feature to leave feedback and comments directly on the design interface.
- **Custom Code [Pro]**: Insert custom code to extend the functionality of your site, offering flexibility for advanced customizations.
- **Custom CSS [Pro]**: Apply Custom CSS to fine-tune the styling of elements, ensuring precise control over the design aspects.
- **[Motion Effects](https://go.elementor.com/wp-repo-description-tab-pro-features-motion-effects/) [Pro]**: Add advanced motion effects to elements for a more dynamic and engaging user experience.
- **Custom Fonts & Icons [Pro]**: Upload and use custom fonts and icons to match your brand’s identity.

= 😍 Elementor FREE widgets =

Unlock the potential of Elementor with our comprehensive suite of free widgets and tools, designed to empower your website creation process and elevate your design capabilities:

- **Heading**. Add eye-catching headlines.
- **Image**. Control the size, opacity and more.
- **Text Editor**. Just like the WordPress text editor.
- **Video**. Add YouTube, Vimeo, VideoPress, Dailymotion or self-hosted videos.
- **Button**. Create interactive buttons.
- **Link in Bio**. Build link in bio components to promote your business / services.
- **Image Box**. A box with image, headline and text.
- **Testimonials**. Customer testimonials.
- **Icon**. Place one or more of 600+ icons available.
- **Icon Box**. An icon, headline, and text with one widget.
- **Social Icons**. Link to your social pages with the Facebook/X (formerly Twitter) icons.
- **Image Gallery**. Display your images in a grid.
- **Image Carousel**. Create rotating carousels or sliders for chosen images.
- **Icon List**. Use any icon to create a bullet list.
- **Counter**. Show numbers in an escalating manner.
- **Progress Bar**. Include an escalating progress bar.
- **Nested Tabs**. Display content in vertical or horizontal tabs.
- **Nested Accordion**. Display any type of content in collapsible sections.
- **Rating**. Display how many stars (or another icon) other visitors gave.
- **Alert**. Include a colored alert box to draw visitor’s attention.
- **HTML**. Insert code into the page.
- **Shortcode**. Insert shortcodes from any plugin into the page.
- **Menu Anchor**. Link any menu to this anchor.
- **Read More**. Set the Read More cut-off for the excerpt in archive pages.
- **Sidebar**. Add sidebars onto the page.
- **Google Maps**. Embed maps into the page.
- **SoundCloud**. Add SoundCloud audio bits.
- **Divider**. Separate content with a designed divider.
- **Spacer**. Add space between elements.
- **Text Path**. Attach your text to a path.
- **And counting...**

### 🚀 Enhance Your Website

**[High-Performing Websites](https://go.elementor.com/wp-repo-description-tab-performance-performance-page/)**: Website performance impacts your visitor’s experience and search result ranking. Elementor, in partnership with Google Chrome, continuously enhances performance without compromising design.

**Key features include:**

- **Reduced DOM Output**: Streamlined HTML structure for faster rendering.
- **Improved Media File Loading**: Optimized loading of images, videos, and other media assets.
- **Reduced CSS and JS Files**: Minimized stylesheets and scripts individually loaded only on demand for quicker loading times.
- **Lazy Loading**: Deferred loading of non-critical resources to improve initial page load speed.
- **Faster Font Loading**: Efficient delivery of web fonts to enhance text rendering speed.
- **Optimized Front-End Asset Loading**: Efficient loading of assets like JavaScript and CSS to minimize render-blocking.
- **Element Caching**: Cache frequently accessed design elements to reduce server response time and enhance overall performance.

### 🔥 Elementor Editor Pro Features

Create unparalleled websites while saving time, money and resources with [Elementor Editor Pro](https://go.elementor.com/wp-repo-description-tab-elementor-pro-elementor-pro/)’s full website builder. Get access to 100+ professional widgets, features, and tools.

**Editor Pro Design Widgets:**

1. **Posts**: Display your blog posts with customizable layouts and styles.
1. **Share Buttons**: Allow visitors to easily share your content on various social media platforms.
1. **Portfolio**: Showcase your work or projects with stunning portfolio layouts.
1. **Slides**: Create dynamic slideshows with custom animations and transitions.
1. **Form**: Design and customize advanced forms for user interaction and data collection.
1. **Login**: Add a login form or user registration module to your website.
1. **Nav Menu**: Customize and style your website's navigation menu for better user experience.
1. **Animated Headline**: Create attention-grabbing headlines with animated effects.
1. **Price Table**: Display pricing plans or packages in a structured and visually appealing format.
1. **Price List**: Showcase a list of prices or services with customizable styling options.
1. **Gallery**: Create beautiful image galleries with various layout options and lightbox support.
1. **Flip Box**: Add interactive flip animations to highlight content or features.
1. **Call to Action**: Encourage user interaction and conversions with compelling call-to-action sections.
1. **Media Carousel**: Showcase a carousel of media files such as images or videos.
1. **Testimonial Carousel**: Display client testimonials in a carousel format for social proof.
1. **Nested Carousel**: Create nested carousels for more complex content organization.
1. **Loop Carousel**: Display content in a looped carousel for continuous viewing.
1. **Table Of Content**: Generate a table of contents for longer articles or guides to improve navigation.
1. **Countdown**: Add countdown timers to create urgency for promotions or events.
1. **Facebook Page**: Embed your Facebook page feed or content onto your website.
1. **Blockquote**: Highlight quotes or testimonials with stylish formatting options.
1. **Template**: Save and reuse design templates for consistent branding and layout.
1. **Reviews**: Showcase customer reviews and ratings to build trust and credibility.
1. **Facebook Button**: Add buttons to promote interactions with your Facebook page or content.
1. **Facebook Embed**: Embed Facebook posts or content onto your website.
1. **Facebook Comments**: Enable Facebook comments on your website's pages or posts.
1. **PayPal Button**: Integrate PayPal buttons for easy online payments.
1. **Stripe Button**: Integrate Stripe payment buttons to facilitate secure online transactions.
1. **Lottie Widget**: Add Lottie animations to enhance visual appeal and engagement.
1. **Code Highlight**: Display code snippets with syntax highlighting for better readability.
1. **Video Playlist**: Create and customize playlists for video content on your website.
1. **Mega Menu**: Customize advanced menus for better navigation and displaying complex content.
1. **Off Canvas**: Create off-canvas areas that slide in to show extra info or menus without cluttering the main layout.

**Editor Pro Theme Widgets:**

Build and customize all the key parts of your website including headers, footers, 404 page, global archives, and more...

1. **Post Title**: Customize the title of individual blog posts or pages.
1. **Post Excerpt**: Display a brief summary or teaser of your blog posts.
1. **Post Content**: Customize the main content area of your blog posts or pages.
1. **Featured Image**: Set and customize featured images for blog posts or pages.
1. **Author Box**: Display author information and bios on blog posts.
1. **Post Comments**: Customize the appearance and functionality of comments sections on your website.
1. **Post Navigation**: Add navigation links to adjacent posts for easy browsing.
1. **Post Info**: Display additional information about blog posts, such as author and date.
1. **Site Logo**: Upload and customize your website's logo for branding purposes.
1. **Site Title**: Customize the title of your website.
1. **Page Title**: Customize the title of individual pages.
1. **Search Bar**: Add a search bar to allow users to search your website's content.
1. **Breadcrumbs**: Display hierarchical navigation paths for better user navigation.
1. **Sitemap**: Generate a sitemap for better search engine indexing and user navigation.
1. **Loop Grid**: Design and customize grid layouts for blog post archives or product listings.

**Editor Pro WooCommerce Widgets:**

Design and customize a complete online shopping experience across your entire website.

1. **Product**: Display individual products with customizable layouts and styles.
1. **Breadcrumbs**: Display hierarchical navigation paths for better user navigation within your store.
1. **Product Title**: Customize the title of individual products.
1. **Product Images**:
... [TRUNCATED]
```

### File: .cursor\README.md
```md
# Cursor AI Configuration

This directory contains AI agent configuration for test generation and code assistance.

## File Structure

### Rules (`/rules/`)
- **`tests-code-style.mdc`** - Technical testing rules and code quality standards
  - Code quality, test reliability, browser/environment rules
  - Applies only to test files (`globs: *test*`)

### System Prompts (`/system-prompts/`)
- **`test-gen/`** - Test generation specific prompts
  - `agent-rules.md` - High-level testing process and strategy
  - `elementor-specific.md` - Elementor platform implementation details  
  - `mcp-rules.md` - Model Context Protocol integration rules
  - See `/test-gen/README.md` for detailed documentation

## Rule Hierarchy

1. **General code style** (workspace-wide rules) - applies to all files
2. **Technical testing rules** (tests-code-style.mdc) - applies to test files only  
3. **Test generation prompts** (system-prompts/test-gen/) - AI agent guidance
   - Process & strategy (agent-rules.md) - high-level workflow guidance
   - Platform specifics (elementor-specific.md) - implementation details
   - Tool integration (mcp-rules.md) - MCP usage patterns

This hierarchy prevents rule duplication and ensures clear separation of concerns.


```

### File: docs\README.md
```md
# Documentation Developers Docs has Moved

The developers docs are now available on the new [Elementor Developers](https://developers.elementor.com/) websites.

## Quick Links

### Getting Started

* [Getting Started](https://developers.elementor.com/docs/getting-started/)
* [Your First Addon](https://developers.elementor.com/docs/getting-started/first-addon/)
* [Building Addons](https://developers.elementor.com/docs/addons/)

### Internals

* [The Editor](https://developers.elementor.com/docs/editor/)
* [Editor Controls](https://developers.elementor.com/docs/editor-controls/)
* [Data Structure](https://developers.elementor.com/docs/data-structure/)
* [Elementor Managers](https://developers.elementor.com/docs/managers/)
* [Scripts & Styles](https://developers.elementor.com/docs/scripts-styles/)
* [Elementor Deprecations](https://developers.elementor.com/docs/deprecations/)
* [Elementor CLI](https://developers.elementor.com/docs/cli/)

### Components

* [Widgets](https://developers.elementor.com/docs/widgets/)
* [Controls](https://developers.elementor.com/docs/controls/)
* [Dynamic Tags](https://developers.elementor.com/docs/dynamic-tags/)
* [Form Actions](https://developers.elementor.com/docs/form-actions/)
* [Form Fields](https://developers.elementor.com/docs/form-fields/)
* [Themes Conditions](https://developers.elementor.com/docs/theme-conditions/)
* [Themes Locations](https://developers.elementor.com/docs/themes/)
* [Context Menu](https://developers.elementor.com/docs/context-menu/)
* [Finder](https://developers.elementor.com/docs/finder/)

```

### File: packages\package.json
```json
{
  "name": "elementor-packages",
  "author": "Elementor Team",
  "license": "GPL-3.0-or-later",
  "engines": {
    "node": ">=20.19.0",
    "npm": ">=10.0.0"
  },
  "devDependencies": {
    "@typescript-eslint/eslint-plugin": "^8.6.0",
    "@typescript-eslint/parser": "^8.6.0",
    "@wordpress/eslint-plugin": "^21.1.0",
    "tsup": "^8.3.5"
  },
  "scripts": {
    "test": "jest --config='./jest.config.js'",
    "test:coverage": "npm run test -- --coverage",
    "lint": "concurrently -n eslint,tsc -c magenta,blue \"eslint . --report-unused-disable-directives-severity error\" \"tsc\"",
    "lint:fix": "eslint . --fix --report-unused-disable-directives-severity error",
    "check-unused": "knip",
    "spell-check": "cspell . --quiet",
    "format": "eslint . --fix",
    "version": "node scripts/version-manager/index.js set",
    "version:list": "node scripts/version-manager/index.js list",
    "version:validate": "node scripts/version-manager/index.js validate",
    "version:bump": "node scripts/version-manager/index.js bump",
    "version:set": "node scripts/version-manager/index.js set",
    "release": "node scripts/version-manager/index.js publish"
  }
}

```

### File: .cursor\system-prompts\README.md
```md
# System Prompts Directory

This directory contains AI agent system prompts organized by purpose and domain.

## Structure

### Test Generation (`/test-gen/`)
Specialized prompts for automated test generation and QA workflows:
- **Process & Strategy** - High-level testing workflows and standards
- **Platform Implementation** - Elementor-specific testing patterns
- **Tool Integration** - MCP usage for interactive analysis

See `/test-gen/README.md` for detailed documentation.

## Usage Principle
**Analyze → Understand → Act → Verify**

These prompts work together to provide comprehensive guidance for AI-assisted test generation, from planning through implementation to debugging.

```

### File: packages\scripts\README.md
```md
# Version Manager Script

A comprehensive tool for managing versions and publishing packages in the Elementor monorepo.

## Architecture

The version manager is organized into a modular structure for better maintainability:

```
scripts/version-manager/
├── index.js              # Main entry point
├── cli.js                # CLI interface and argument parsing
├── constants.js          # Constants and configuration
├── logger.js             # Logging utilities
├── package-discovery.js  # Package discovery and filtering
├── version-utils.js      # Version manipulation utilities
├── version-operations.js # Version setting and bumping operations
├── validation.js         # Package validation logic
├── publishing.js         # Publishing functionality
└── listing.js           # Package listing and display
```

## Features

- **Version Management**: Set, bump, and validate package versions across the workspace
- **Publishing**: Publish packages to npm with validation and safety checks
- **Workspace Support**: Handles monorepo structure with multiple packages
- **Validation**: Comprehensive validation before publishing
- **Dry Run**: Preview changes without making them

## Commands

### Version Management

#### Set Version
Set an exact version for all packages:

```bash
node scripts/version-manager/index.js set <version> [options]
```

Examples:
```bash
# Set all packages to version 3.31.0
node scripts/version-manager/index.js set 3.31.0

# Set with pre-release tag
node scripts/version-manager/index.js set 3.31.0 --tag beta.1

# Dry run to see what would change
node scripts/version-manager/index.js set 3.31.0 --dry-run

# Set only specific packages
node scripts/version-manager/index.js set 3.31.0 --packages "packages/core/*"
```

#### Bump Version
Increment version using semantic versioning:

```bash
node scripts/version-manager/index.js bump <type> [options]
```

Types: `patch`, `minor`, `major`

Examples:
```bash
# Bump patch version
node scripts/version-manager/index.js bump patch

# Bump minor version with release candidate tag
node scripts/version-manager/index.js bump minor --tag rc.1

# Bump from specific base version
node scripts/version-manager/index.js bump patch --base-version 3.30.0
```

#### List Packages
List all packages and their versions:

```bash
node scripts/version-manager/index.js list [options]
```

Examples:
```bash
# List all packages
node scripts/version-manager/index.js list

# List only publishable packages
node scripts/version-manager/index.js list --publishable

# List specific packages
node scripts/version-manager/index.js list --packages "packages/libs/*"
```

#### Get Package Version
Get version of a package matching a regex pattern with clean output (useful for scripts):

```bash
node scripts/version-manager/index.js get-version <pattern> [options]
```

Options:
- `--release-type <type>`: Calculate new version by release type (patch, minor, major)

Examples:
```bash
# Get version of a specific package
node scripts/version-manager/index.js get-version "@elementor/editor-controls"

# Get version of first package matching pattern
node scripts/version-manager/index.js get-version "editor-.*"

# Get next patch version of a package
node scripts/version-manager/index.js get-version "@elementor/editor-controls" --release-type patch

# Get next minor version of first matching package
node scripts/version-manager/index.js get-version "editor-.*" --release-type minor

# Use in scripts
VERSION=$(node scripts/version-manager/index.js get-version "@elementor/.*")
NEXT_VERSION=$(node scripts/version-manager/index.js get-version "@elementor/.*" --release-type patch)
```

The command outputs only the version number without any formatting, making it ideal for use in scripts. It returns:
- The version number if a match is found (incremented if --release-type is specified)
- Empty string if no match is found
- Exit code 1 if no match is found or an error occurs

#### Validate Versions
Check that all packages have consistent versioning:

```bash
node scripts/version-manager/index.js validate [options]
```

### Publishing

#### Publish Packages
Publish packages to npm (only non-private packages):

```bash
node scripts/version-manager/index.js publish [options]
```

**Important**: Only packages with `"private": false` in their `package.json` will be published.

Examples:
```bash
# Publish all packages (with confirmation)
node scripts/version-manager/index.js publish

# Publish without confirmation
node scripts/version-manager/index.js publish --yes

# Dry run to see what would be published
node scripts/version-manager/index.js publish --dry-run

# Publish specific packages
node scripts/version-manager/index.js publish --packages "packages/libs/*"

# Publish with specific access level
node scripts/version-manager/index.js publish --access public

# Publish with two-factor authentication
node scripts/version-manager/index.js publish --otp <token>
```

## Publishing Validation

Before publishing, the script performs comprehensive validation:

### Required Checks (Errors)
- Package name and version are present
- `dist` directory exists and contains files
- Package.json is valid and readable

### Recommended Checks (Warnings)
- README.md file exists
- CHANGELOG.md file exists
- Entry point specified (main, module, or exports)
- License field is present
- Repository field is present
- Scoped packages have publishConfig.access specified

### Safety Checks
- Checks if package is already published at current version
- Validates package structure before attempting to publish
- Provides detailed error messages for failed validations

## Options

### Global Options
- `--dry-run`: Show what would be changed without making changes
- `--packages <pattern>`: Glob pattern for packages to process (default: all)
- `--tag <suffix>`: Add version suffix (e.g., beta, rc, alpha)

### Publishing Options
- `--yes`: Assume "yes" to prompts and confirmations
- `--access <public|restricted>`: Access level for published packages
- `--otp <token>`: Two-factor authentication token for npm

### Version Options
- `--base-version <version>`: Base version to bump from (for bump command)

## Package Configuration

### Making a Package Publishable

To make a package publishable, ensure its `package.json` has:

```json
{
  "name": "@elementor/your-package",
  "version": "1.0.0",
  "private": false,
  "publishConfig": {
    "access": "public"
  },
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "types": "dist/index.d.ts",
  "files": [
    "README.md",
    "CHANGELOG.md",
    "/dist",
    "/src",
    "!**/__tests__"
  ]
}
```

### Private Packages

To keep a package private, set:

```json
{
  "private": true
}
```

## Workflow Examples

### Release Process

1. **Build packages**:
   ```bash
   npm run build
   ```

2. **Bump versions**:
   ```bash
   node scripts/version-manager/index.js bump patch
   ```

3. **Validate**:
   ```bash
   node scripts/version-manager/index.js validate
   ```

4. **Preview publishing**:
   ```bash
   node scripts/version-manager/index.js publish --dry-run
   ```

5. **Publish**:
   ```bash
   node scripts/version-manager/index.js publish --yes
   ```

### Pre-release Process

1. **Set pre-release version**:
   ```bash
   node scripts/version-manager/index.js set 3.31.0 --tag beta.1
   ```

2. **Publish pre-release**:
   ```bash
   node scripts/version-manager/index.js publish --tag beta --yes
   ```

## Integration with npm Scripts

The version manager integrates with existing npm scripts:

```json
{
  "scripts": {
    "version": "node scripts/version-manager/index.js set",
    "version:list": "node scripts/version-manager/index.js list",
    "version:validate": "node scripts/version-manager/index.js validate",
    "version:bump": "node scripts/version-manager/index.js bump",
    "version:set": "node scripts/version-manager/index.js set",
    "version:get": "node scripts/version-manager/index.js get-version",
    "release": "npm run build && node scripts/version-manager/index.js publish"
  }
}
```

## Error Handling

The script provides clear error messages and exits with appropriate codes:

- **Exit 0**: Success
- **Exit 1**: Error (validation failures, publishing errors, etc.)

## Best Practices

1. **Always use dry-run first** to preview changes
2. **Build packages** before publishing
3. **Validate versions** before publishing
4. **Use semantic versioning** for version bumps
5. **Include README and CHANGELOG** files
6. **Test publishing** with a single package first

## Troubleshooting

### Common Issues

1. **"Missing dist directory"**: Run `npm run build` first
2. **"Package already published"**: Bump version or use different tag
3. **"Authentication failed"**: Check npm login and 2FA settings
4. **"Permission denied"**: Check npm registry permissions

### Debug Mode

For detailed debugging, you can add console.log statements or use Node.js debugger:

```bash
node --inspect scripts/version-manager/index.js publish --dry-run
``` 
```

### File: .cursor\system-prompts\test-gen\README.md
```md
# Test Generation System Prompts

This directory contains AI agent prompts specifically for automated test generation and QA workflows.

## Files Overview

### Core Process & Strategy
- **`agent-rules.md`** - High-level testing process and workflow strategy
  - Two-phase workflow (Planning → Implementation)
  - Testing coverage and quality standards
  - Definition of Done and file structure

### Platform Implementation
- **`elementor-specific.md`** - Elementor platform implementation details
  - Editor API usage and widget interactions
  - Helper functions and responsive testing patterns
  - Elementor-specific constants and best practices

### Tool Integration  
- **`mcp-rules.md`** - Model Context Protocol integration rules
  - When and how to use Playwright MCP for app behavior analysis
  - Debugging workflows and tool usage guidelines

## Usage Context

These prompts are designed to work together for comprehensive test generation:

1. **Planning Phase**: Use `agent-rules.md` for test plan creation
2. **Implementation Phase**: Apply `elementor-specific.md` for platform details
3. **Debugging Phase**: Follow `mcp-rules.md` for interactive analysis

## Integration with Technical Rules

These system prompts work in conjunction with:
- `/.cursor/rules/tests-code-style.mdc` - Technical testing standards
- `/.cursor/rules/general-code-style.mdc` - General code quality rules

```

### File: .grunt-config\plugins\watch-time\index.js
```js
/**
 * Extracted from https://github.com/sca-/webpack-watch-time-plugin
 */

function WatchTimePlugin() {}

WatchTimePlugin.prototype.onWatchRun = function onWatchRun( watching, callback ) {
	console.log( '\x1b[35m', ' ' + ( new Date() ).toLocaleString() );
	callback();
}

WatchTimePlugin.prototype.apply = function ( compiler ) {
	compiler.hooks.watchRun.tapAsync( 'watch-time', this.onWatchRun.bind( this ) );
}

module.exports = WatchTimePlugin;

```

### File: app\assets\js\index.js
```js
import ReactUtils from 'elementor-utils/react';
import App from './app';
import ImportExport from '../../modules/import-export/assets/js/module';
import ImportExportCustomization from '../../modules/import-export-customization/assets/js/module';
import KitLibrary from '../../modules/kit-library/assets/js/module';
import Onboarding from '../../modules/onboarding/assets/js/module';
import SiteBuilder from '../../modules/site-builder/assets/js/module';
import { Module as SiteEditor } from '@elementor/site-editor';

import AppProvider from './app-context';

new ImportExport();
new KitLibrary();
new SiteEditor();

if ( elementorCommon?.config?.experimentalFeatures?.[ 'site-builder' ] ) {
	new SiteBuilder();
}

new Onboarding();

if ( elementorCommon?.config?.experimentalFeatures?.[ 'import-export-customization' ] ) {
	new ImportExportCustomization();
}

const AppWrapper = React.Fragment;

ReactUtils.render( (
	<AppWrapper>
		<AppProvider>
			<App />
		</AppProvider>
	</AppWrapper>
), document.getElementById( 'e-app' ) );

```

### File: packages\apps\onboarding\package.json
```json
{
  "name": "@elementor/onboarding",
  "description": "Onboarding wizard for Elementor",
  "version": "4.1.0",
  "private": true,
  "author": "Elementor Team",
  "homepage": "https://elementor.com/",
  "license": "GPL-3.0-or-later",
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.js"
    },
    "./package.json": "./package.json"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/elementor/elementor.git",
    "directory": "packages/apps/onboarding"
  },
  "bugs": {
    "url": "https://github.com/elementor/elementor/issues"
  },
  "files": [
    "README.md",
    "CHANGELOG.md",
    "/dist",
    "/src",
    "!**/__tests__"
  ],
  "scripts": {
    "build": "tsup --config=../../tsup.build.ts",
    "dev": "tsup --config=../../tsup.dev.ts"
  },
  "dependencies": {
    "@elementor/events": "4.1.0",
    "@elementor/icons": "1.68.0",
    "@elementor/query": "4.1.0",
    "@elementor/store": "4.1.0",
    "@elementor/ui": "1.36.17",
    "@elementor/utils": "4.1.0"
  },
  "peerDependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "tsup": "^8.3.5"
  }
}

```

### File: packages\apps\onboarding\README.md
```md
# @elementor/onboarding

Onboarding wizard for Elementor.

## Installation

```bash
npm install @elementor/onboarding
```

## Usage

```typescript
import { App, registerOnboardingSlice } from '@elementor/onboarding';

// Register the store slice
registerOnboardingSlice();

// Render the app
<App onComplete={() => console.log('Done!')} onClose={() => console.log('Closed')} />
```

## Steps

The onboarding wizard has 7 steps:

1. **account** - Let's get to work (connect/login)
2. **building_for** - Who are you building for?
3. **site_about** - What is your site about?
4. **experience** - Have you worked with Elementor before?
5. **theme_select** - Choose a theme that fits your needs
6. **theme_confirm** - Continue with Hello theme
7. **site_features** - What do you want to include in your site?

## Hooks

### useOnboarding

```typescript
import { useOnboarding } from '@elementor/onboarding';

function MyComponent() {
  const { stepId, stepIndex, isFirst, isLast, actions } = useOnboarding();
  
  return (
    <button onClick={actions.nextStep}>Next</button>
  );
}
```

### useUpdateProgress

```typescript
import { useUpdateProgress } from '@elementor/onboarding';

function MyComponent() {
  const updateProgress = useUpdateProgress();
  
  const handleComplete = () => {
    updateProgress.mutate({ complete_step: 'account' });
  };
  
  return (
    <button onClick={handleComplete}>Complete Step</button>
  );
}
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
