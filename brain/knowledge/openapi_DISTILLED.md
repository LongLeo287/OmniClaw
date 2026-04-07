---
id: openapi
type: knowledge
owner: OA_Triage
---
# openapi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">OpenAPI Generator</h1>


<div align="center">

[![Stable releases in Maven Central](https://img.shields.io/maven-metadata/v/https/repo1.maven.org/maven2/org/openapitools/openapi-generator/maven-metadata.xml.svg)](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22org.openapitools%22%20AND%20a%3A%22openapi-generator%22)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-orange)](./LICENSE)
[![Open Collective backers](https://img.shields.io/opencollective/backers/openapi_generator?color=orange&label=OpenCollective%20Backers)](https://opencollective.com/openapi_generator)
[![Join the Slack chat room](https://img.shields.io/badge/Slack-Join%20the%20chat%20room-orange)](https://join.slack.com/t/openapi-generator/shared_invite/zt-36ucx4ybl-jYrN6euoYn6zxXNZdldoZA)
[![Follow OpenAPI Generator Twitter account to get the latest update](https://img.shields.io/twitter/follow/oas_generator.svg?style=social&label=Follow)](https://twitter.com/oas_generator)
[![Contribute with Gitpod](https://img.shields.io/badge/Contribute%20with-Gitpod-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/OpenAPITools/openapi-generator)
[![Conan Center](https://shields.io/conan/v/openapi-generator)](https://conan.io/center/recipes/openapi-generator)
[![Revved up by Develocity](https://img.shields.io/badge/Revved%20up%20by-Develocity-06A0CE?logo=Gradle&labelColor=02303A)](https://ge.openapi-generator.tech/scans)
</div>

<div align="center">

[Master](https://github.com/OpenAPITools/openapi-generator/tree/master) (`7.22.0`):
[![Integration Test2](https://circleci.com/gh/OpenAPITools/openapi-generator.svg?style=shield)](https://circleci.com/gh/OpenAPITools/openapi-generator)
[![Bitrise](https://img.shields.io/bitrise/4a2b10a819d12b67/master?label=bitrise%3A%20Swift+4,5&token=859FMDR8QHwabCzwvZK6vQ)](https://app.bitrise.io/app/4a2b10a819d12b67)

</div>

<div align="center">

:star::star::star: If you would like to contribute, please refer to [guidelines](CONTRIBUTING.md) and a list of [open tasks](https://github.com/openapitools/openapi-generator/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22). :star::star::star:

:bangbang: To migrate from Swagger Codegen to OpenAPI Generator, please refer to the [migration guide](docs/migration-from-swagger-codegen.md) :bangbang:

:notebook_with_decorative_cover: For more information, please refer to the [Wiki page](https://github.com/openapitools/openapi-generator/wiki) and [FAQ](https://github.com/openapitools/openapi-generator/wiki/FAQ) :notebook_with_decorative_cover:

:notebook_with_decorative_cover: The eBook [A Beginner's Guide to Code Generation for REST APIs](https://gum.co/openapi_generator_ebook) is a good starting point for beginners :notebook_with_decorative_cover:

:warning: If the OpenAPI spec, templates or any input (e.g. options, environment variables) is obtained from an untrusted source or environment, please make sure you've reviewed these inputs before using OpenAPI Generator to generate the API client, server stub or documentation to avoid potential security issues (e.g. [code injection](https://en.wikipedia.org/wiki/Code_injection)). For security vulnerabilities, please contact [team@openapitools.org](mailto:team@openapitools.org). :warning:

:bangbang: Both "OpenAPI Tools" (https://OpenAPITools.org - the parent organization of OpenAPI Generator) and "OpenAPI Generator" are not affiliated with OpenAPI Initiative (OAI) :bangbang:

</div>

## Sponsors

If you find OpenAPI Generator useful for work, please consider asking your company to support this Open Source project by [becoming a sponsor](https://opencollective.com/openapi_generator). You can also individually sponsor the project by [becoming a backer](https://opencollective.com/openapi_generator).

#### Thank you to our bronze sponsors!

[![NamSor](https://openapi-generator.tech/img/companies/namsor.png)](https://www.namsor.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[![LightBow](https://openapi-generator.tech/img/companies/lightbow.png)](https://www.lightbow.net/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/docspring.png" width="128" height="128">](https://docspring.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/datadog.png" width="128" height="128">](https://datadoghq.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/thales.jpg" width="128" height="128">](https://cpl.thalesgroup.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/apideck.jpg" width="128" height="128">](https://www.apideck.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/pexa.png" width="128" height="128">](https://www.pexa.com.au/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/numary.png" width="128" height="128">](https://www.numary.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/onesignal.png" width="128" height="128">](https://www.onesignal.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/virtualansoftware.png" width="128" height="128">](https://www.virtualansoftware.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/mergedev.jpeg" width="128" height="128">](https://www.merge.dev/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/burkert.jpg" width="128" height="128">](https://www.burkert.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/finbourne.png" width="128" height="128">](https://www.finbourne.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/bumpsh.png" width="128" height="128">](https://bump.sh/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/bileto.png" width="128" height="128">](https://www.bileto.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/bairesdev.png" width="128" height="128">](https://www.bairesdev.com/sponsoring-open-source-projects/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/dmtech.jpeg" width="128" height="128">](https://www.dmtech.de/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/adyen.png" width="128" height="128">](https://adyen.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/fornex.png" width="128" height="128">](https://fornex.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/alloyautomation.png" width="128" height="128">](https://runalloy.com/signup?utm_source=github&utm_medium=referral&utm_campaign=1524_openapigenerator)
[<img src="https://openapi-generator.tech/img/companies/ssstwitter.png" width="128" height="128">](https://ssstwitter.com/?utm_source=github&utm_medium=referral&utm_campaign=sponsor)
[<img src="https://openapi-generator.tech/img/companies/svix.png" width="128" height="128">](https://www.svix.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/litslink.png" width="128" height="128">](https://litslink.com/services/artificial-intelligence?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/designli.jpg" width="128" height="128">](https://designli.co?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/itm.png" width="128" height="128">](https://opensource.muenchen.de?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/kong.png" width="128" height="128">](https://konghq.com/products/kong-konnect?utm_medium=referral&utm_source=github&utm_campaign=platform&utm_content=openapi-generator)
[<img src="https://openapi-generator.tech/img/companies/route4me.png" width="128" height="128">](https://route4me.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/dm.png" width="128" height="128">](https://www.dotcom-monitor.com/sponsoring-open-source-projects/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/clickit.jpg" width="128" height="128">](https://www.clickittech.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/unified_to.jpg" width="128" height="128">](https://unified.to/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/savetwt.jpg" width="128" height="128">](https://savetwt.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/serpapi.png" width="128" height="128">](https://serpapi.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/socialwick.png" width="128" height="128">](https://socialwick.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/fbpostlikes.png" width="128" height="128">](https://fbpostlikes.com/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)
[<img src="https://openapi-generator.tech/img/companies/buyfans.png" width="128" height="128">](https://buy.fans/buy-tiktok-likes/?utm_source=openapi-generator&utm_medium=sponsorship&utm_campaign=oss-sponsorship)

#### Thank you GoDaddy for sponsoring the domain names, Linode for sponsoring the VPS, Checkly for sponsoring the API monitoring and Gradle for sponsoring Develocity

[<img src="https://openapi-generator.tech/img/companies/godaddy.png" width="150">](https://www.godaddy.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[![Linode](https://www.linode.com/media/images/logos/standard/light/linode-logo_standard_light_small.png)](https://www.linode.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRAhEYadUyZYzGUotZiSdXkVMqqLGuohyixLl4eUpUV6pAbUULL" width="150">](https://checklyhq.com/?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)
[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Gradle_logo.png/320px-Gradle_logo.png" width="150">](https://gradle.org?utm_source=openapi_generator&utm_medium=github_webpage&utm_campaign=sponsor)

## Overview

OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs,  documentation and configuration automatically given an [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification) (both 2.0 and 3.0 are supported). Currently, the following languages/frameworks are supported:

|                                  | Languages/Frameworks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **API clients**                  | **ActionScript**, **Ada**, **Apex**, **Bash**, **C**, **C#** (.net 2.0, 3.5 or later, .NET Standard 1.3 - 2.1, .NET Core 3.1, .NET 5.0. Libraries: RestSharp, GenericHo
... [TRUNCATED]
```

### File: website\package.json
```json
{
  "private": true,
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "publish-gh-pages": "docusaurus deploy",
    "write-translations": "docusaurus write-translations",
    "version": "docusaurus version",
    "rename-version": "docusaurus rename-version"
  },
  "devDependencies": {},
  "dependencies": {
    "@docusaurus/core": "^2.3.1",
    "@docusaurus/plugin-google-analytics": "^2.3.1",
    "@docusaurus/preset-classic": "^2.3.1",
    "@docusaurus/utils": "^2.3.1",
    "classnames": "^2.2.6",
    "js-yaml": "^4.1.1",
    "lodash.merge": "^4.6.2",
    "lodash.template": "^4.18.1",
    "prism-react-renderer": "^1.0.2",
    "react": "^16.10.2",
    "react-dom": "^16.10.2"
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
  }
}

```

### File: website\src\pages\index.js
```js
import React from 'react';
import classnames from 'classnames';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';
import CodeBlock from '@theme/CodeBlock'

const features = [
    {
        title: <>Easy to Use</>,
        imageUrl: `img/icons/plug.svg`,
        description: (
            <>
                <p>
                    With <em>50+</em> client generators, you can easily generate code to interact with any server which
                    exposes an OpenAPI document.
                </p>
                <p>
                    Maintainers of APIs may also automatically generate and distribute clients as part of official SDKs.
                </p>
                <p>
                    Each client supports different options and features, but all templates can be replaced with your own
                    Mustache-based templates.
                </p>
                See <a href="./docs/customization">Customization</a> for details.
            </>
        ),
    },
    {
        title: <>Servers</>,
        imageUrl: 'img/icons/exchange.svg',
        description: (
            <>
                <p>Getting started with server development can be tough, especially if you're evaluating technologies.
                    We can reduce the burden when you bring your own OpenAPI document.</p>
                <p>Generate server stubs for 40+ different languages and technologies, including Java, Kotlin, Go, and
                    PHP.</p>
                <p>Some generators support <em>Inversion of Control</em>, allowing you to iterate on design via your
                    OpenAPI document without worrying about blowing away your entire domain layer when you regenerate
                    code.</p>
            </>
        ),
    },
    {
        title: <>Schemas/Configs</>,
        imageUrl: 'img/icons/pencil.svg',
        description: (
            <>
                <p>Ever wanted to iteratively design a MySQL database, but writing table declarations was too
                    tedious?</p>
                <p>OpenAPI Generator offers some special generators such as Apache2 Configuration, MySQL and GraphQL
                    schema generators.</p>
                <p>You can easily extend these generators and their templates to create derivative generators!</p>
            </>
        ),
    },
    {
        title: <>Documentation</>,
        imageUrl: 'img/icons/newspaper-o.svg',
        description: (
            <>
                <p>OpenAPI documents allow you to convert the metadata about your API into some other format.</p>
                <p>We include documentation formats such as HTML and Cwiki, which allow you to distribute static
                    documentation to your consumers.</p>
                <p>We also support generating from OpenAPI 2.0 to newer JSON/YAML OpenAPI 3.x documents.</p>
            </>
        ),
    },
];


function stripMargin(template, ...expressions) {
    let result = template.reduce((accumulator, part, i) => {
        return accumulator + expressions[i - 1] + part
    });

    return result.replace(/\r?(\n)\s*\|/g, '$1');
}


const callouts = [
    {
        id: 'learn',
        imageUrl: 'img/color-logo.svg',
        title: <>Learn How</>,
        content: (
            <div><span><p>OpenAPI Generator supports many different integrations and use cases, including (but not limited to):</p>
            <ul>
            <li>Maven Plugin</li>
            <li>Gradle Plugin</li>
            <li>Bazel Plugin</li>
            <li>SBT Plugin</li>
            <li>Cake Plugin</li>
            <li>CLI via Homebrew</li>
            <li>CLI via Docker</li>
            <li>CLI via npm</li>
            <li>Generator SaaS</li>
            </ul>
            <p>For details, see  <a href="/docs/integrations">Workflow Integrations</a></p>
            <p>Generation also allows for easy customization via options, custom templates, or even custom generators on your classpath. See <a
                href="/docs/customization">Customization</a> for details.</p>
            </span></div>
        ),
    },
    {
        id: 'connectOnSlack',
        imageUrl: 'img/tools/Slack_Mark-256x256-3a29a6b.png',
        title: <>Active Community</>,
        content: (
            <>
                <p><strong>Connect</strong> with us on Slack!</p>
                <p>
                    We're a very community-oriented project. We have an active community of users, contributors, and
                    core team members on Slack. Slack is often a good
                    place to start if you're looking for guidance about where to begin contributing, if you have an idea
                    you're
                    not sure fits the project, or if you just want to ask a question or say hello.
                </p>
                <p>Slack is free to <a href="https://slack.com/downloads" className="href">download</a>, and our
                    workspace is free to <a
                        href="https://join.slack.com/t/openapi-generator/shared_invite/zt-36ucx4ybl-jYrN6euoYn6zxXNZdldoZA"
                        className="href">sign up</a>.
                </p>
            </>
        ),
    },
    {
        id: 'try',
        imageUrl: 'img/tools/npm.svg',
        title: <>Try via npm</>,
        content: (
            <>
                <p>
                    The <a href="https://github.com/openapitools/openapi-generator-cli" className="href">npm package
                    wrapper</a> is cross-platform wrapper around the .jar artifact.
                </p>
                <p>
                    <strong>Install</strong> globally, exposing the CLI on the command line:
                </p>

                {/* <!-- RELEASE_VERSION --> */}

                <p><CodeBlock className="bash">{stripMargin`
                   |# install the latest version of "openapi-generator-cli"
                   |npm install @openapitools/openapi-generator-cli -g
                   |
                   |# use a specific version of "openapi-generator-cli"
                   |openapi-generator-cli version-manager set 7.19.0
                   |
                   |# Or install it as dev-dependency in your node.js projects
                   |npm install @openapitools/openapi-generator-cli -D
                `}</CodeBlock></p>

                {/*  <!-- /RELEASE_VERSION --> */}

                <p>Then, <strong>generate</strong> a ruby client from a valid <a
                    href="https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml"
                    className="href">petstore.yaml</a> doc:</p>

                <p><CodeBlock className="bash">{`
                openapi-generator-cli generate -i petstore.yaml -g ruby -o /tmp/test/
                `}</CodeBlock></p>
            </>
        ),
    },
    {
        id: 'tryHomebrew',
        imageUrl: 'img/tools/homebrew-256x256.png',
        title: <>Try via Homebrew</>,
        content: (
            <>
                <p><strong>Install</strong> via <a href="https://brew.sh/" className="href">homebrew</a>:</p>

                <p><CodeBlock className="bash">{'brew install openapi-generator'}</CodeBlock></p>

                <p>
                    Then, <strong>generate</strong> a ruby client from a valid <a
                    href="https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml"
                    className="href">petstore.yaml</a> doc:
                </p>

                <p><CodeBlock className="bash">{'openapi-generator generate -i petstore.yaml -g ruby -o /tmp/test/'}</CodeBlock></p>
            </>
        ),
    },
    {
        id: 'tryDocker',
        imageUrl: 'img/tools/docker.png',
        title: <>Try via Docker</>,
        content: (
            <>
                <p>The OpenAPI Generator image acts as a standalone executable. It can be used as an alternative to
                    installing via homebrew, or for developers who are unable to install Java or upgrade the installed
                    version.</p>
                <p>To generate code from a valid <a
                    href="https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml">petstore.yaml</a> doc
                    with this image, you'll need to mount a local location as a volume.
                </p>
                <p>
                    <CodeBlock className="bash">
                        {stripMargin`
                |docker run --rm \\
                |    -v $PWD:/local openapitools/openapi-generator-cli generate \\
                |    -i /local/petstore.yaml \\
                |    -g go \\
                |    -o /local/out/go
                `}
                    </CodeBlock>
                </p>
                <p>For a full list of our docker images, check out <a
                    href="https://hub.docker.com/u/openapitools">u/openapitools</a> on Docker Hub.</p>
            </>
        ),
    }
];

function Callout({id, title, imageUrl, content}) {
    const imgUrl = useBaseUrl(imageUrl);
    let alt = `${id} logo`;

    return (
        <>
            <div id={id} className={classnames('row', styles.calloutRow)}>
                <div className={classnames('col col--3 blockImage')}>
                    <img className={'image'} src={imgUrl} alt={alt}/>
                </div>
                <div className={'col col--9'}>
                    <h2>{title}</h2>
                    {content}
                </div>
            </div>
        </>
    )
}

function Feature({imageUrl, title, description}) {
    const imgUrl = useBaseUrl(imageUrl);
    return (
        <div className={classnames('col col--6', styles.feature)}>
            {imgUrl && (
                <div className="text--center">
                    <img className={styles.featureImage} src={imgUrl} alt="logo"/>
                </div>
            )}
            <h3>{title}</h3>
            <div>{description}</div>
        </div>
    );
}

function ShowcaseUser({image, infoLink, caption}) {
    const imgUrl = useBaseUrl(image);
    return (
        <a href={infoLink} key={infoLink}>
            <img src={imgUrl} alt={caption} title={caption} className={styles.productShowcaseSectionLogo}/>
        </a>
    );
}
function Showcase({users}) {
    const context = useDocusaurusContext();
    const {siteConfig = {}} = context;
    return (
        <>
            <h2>Who is Using This?</h2>
            <p>Here are some users of OpenAPI Generator</p>
            <div className="logos">
                {users.filter(user => user.pinned).map((user, idx) => (
                    <ShowcaseUser key={idx} {...user} />
                ))}
            </div>
            <div className="more-users">
                <Link
                    className={classnames(
                        'button button--outline button--primary button--lg',
                        styles.productShowcaseSectionButton
                    )}
                    to={useBaseUrl('users')}>
                    More {siteConfig.title} Users
                </Link>
            </div>
        </>
    );
}

function Home() {
    const context = useDocusaurusContext();
    const {siteConfig = {}} = context;
    const {sponsors = {}, users = {}} = siteConfig.customFields;

    return (
        <Layout
            title={`Hello from ${siteConfig.title}`}
            description="Description will go into a meta tag in <head />">
            <header className={classnames('hero hero--primary', styles.heroBanner)}>
                <div className="container">
                    <h1 className="hero__title">{siteConfig.title}</h1>
                    <p className="hero__subtitle">{siteConfig.tagline}</p>
                    <div className={styles.buttons}>
                        <Link
                            className={classnames(
                                'button button--outline button--secondary button--lg',
                                styles.getStarted,
                            )}
                            to={useBaseUrl('#try')}>
                            Try It Out
                        </Link>
                        <Link
                            className={classnames(
                                'button button--outline button--secondary button--lg',
                                styles.getStarted,
                            )}
                            to={useBaseUrl('docs/installation')}>
                            Install
                        </Link>
                    </div>

                    <div className={styles.buttons}>
                        <Link
                            className={classnames(
                                'button button--outline button--secondary button--md',
                                styles.getStarted,
                            )}
                            to={useBaseUrl('docs/generators')}>
                            Generators
                        </Link>
                        <Link
                            className={classnames(
                                'button button--outline button--secondary button--md',
                                styles.getStarted,
                            )}
                            to={useBaseUrl('docs/customization')}>
                            Customization
                        </Link>
                        <Link
                            className={classnames(
                                'button button--outline button--secondary button--md',
                                styles.getStarted,
                            )}
                            to={useBaseUrl('docs/integrations')}>
                            Integrations
                        </Link>
                    </div>
                </div>
            </header>
            <div className={classnames(styles.announcement, styles.announcementDark)}>
                <div className={styles.announcementInner}>
                    <h2><b>Sponsors</b></h2>
                    <p>If you find OpenAPI Generator useful, please consider asking your company to <a
                        href="https://opencollective.com/openapi_generator">become a sponsor</a>.</p>
                    <p>You can also individually sponsor the project by <a
                        href="https://opencollective.com/openapi_generator">becoming a backer</a>.</p>
                    <h3>Thank you to our bronze sponsors!</h3>
                    <div className={classnames('avatar', styles.bronzeSponsorAvatars)}>
                        {sponsors
             
... [TRUNCATED]
```

### File: samples\schema\petstore\mysql\README.md
```md
# MySQL Schema Codegen

Main goal of this generator is to provide database structure file almost identical you usually generate with:
- PHPMyAdmin (Export structure only, SQL syntax)
- Adminer
- `mysqldump` function

[MySQL documentation](https://dev.mysql.com/doc/)

## Requirements
- MySQL Server ^5.7.8 (`JSON` column type added)

## Openapi Data Type to MySQL Data Type mapping

| Openapi Data Type | Openapi Data Format | Dependent properties | MySQL Data Types | Default MySQL Data Type |
| --- | --- | --- | --- | --- |
| `integer` | `int32` | `minimum` / `maximum` / `minimumExclusive` / `maximumExclusive` | `TINYINT` / `SMALLINT` / `MEDIUMINT`/ `INT` / `BIGINT` | `INT` |
| `integer` | `int64` | `minimum` / `maximum` / `minimumExclusive` / `maximumExclusive` | `TINYINT` / `SMALLINT` / `MEDIUMINT` / `INT` / `BIGINT` | `BIGINT` |
| `boolean` | | | `TINYINT` | `TINYINT` |
| `number` | `float` | | `DECIMAL` | `DECIMAL` |
| `number` | `double` | | `DECIMAL` | `DECIMAL` |
| `string` | | `minLength` / `maxLength` | `CHAR` / `VARCHAR` / `TEXT` / `MEDIUMTEXT` / `LONGTEXT` | `TEXT` |
| `string` | `byte` |  | `TEXT` | `TEXT` |
| `string` | `binary` |  | `MEDIUMBLOB` | `MEDIUMBLOB` |
| `file` | |  | `MEDIUMBLOB` | `MEDIUMBLOB` |
| `string` | `date` | | `DATE` | `DATE` |
| `string` | `date-time` | | `DATETIME` | `DATETIME` |
| `string` | `enum` | | `ENUM` | `ENUM` |
| `array` | | | `JSON` | `JSON` |
| `object` | | | `JSON` | `JSON` |
| `\Model\User` (referenced definition) | | | `TEXT` | `TEXT` |

## How to use

Produced file(`mysql_schema.sql`) contains every table definition. Current implementation doesn't drop or modify existed tables, if you want rewrite whole schema make sure they're not presented.

### PHPMyAdmin

1. Choose **Import** tab from the home screen
2. In section **File to import** click to **Choose File** and find generated `mysql_schema.sql`
3. Make sure **Format** selector set to **SQL**
4. Push **Go** button

### Adminer

1. Click **Import** link in left sidebar
2. In **File upload** fieldset click to **Choose Files** and find generated `mysql_schema.sql`
3. Push **Execute** button

### Prepared SQL queries

[Model folder](./Model) contains SQL queries(`SELECT *`,  `SELECT`, `INSERT`, `UPDATE`,  `DELETE`) usually suggested by `PHPMyAdmin` when you hit `SQL` tab. They are absolutely useless without adaptation to your needs. Copy-paste them then edit.

Important! Some of SQLs(`INSERT`/`UPDATE`) contains question marks(`?`) which are parameter placeholders. You need to bind values to these params to execute query.

If your MySQL driver doesn't support named parameters(`PHP PDO` supports while `PHP mysqli` doesn't) you need to make sure that `namedParametersEnabled` generator option is disabled.

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at team@openapitools.org. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

```

### File: CONTRIBUTING.md
```md
# Guidelines For Contributing

## Before submitting an issue

 - If you're not using the latest master to generate API clients or server stubs, please give it another try by pulling the latest master as the issue may have already been addressed. Ref: [Getting Started](https://github.com/openapitools/openapi-generator#getting-started)
 - Search the [open issue](https://github.com/openapitools/openapi-generator/issues) and [closed issue](https://github.com/openapitools/openapi-generator/issues?q=is%3Aissue+is%3Aclosed) to ensure no one else has reported something similar before.
 - File an [issue ticket](https://github.com/openapitools/openapi-generator/issues/new) by providing all the required information. Failure to provide enough detail may result in slow response from the community.
 - Test with the latest master by building the JAR locally to see if the issue has already been addressed.
 - You can also make a suggestion or ask a question by opening an "issue".

## Before submitting a PR

 - Search the [open issue](https://github.com/openapitools/openapi-generator/issues) to ensure no one else has reported something similar and no one is actively working on similar proposed change.
 - If no one has suggested something similar, open an ["issue"](https://github.com/openapitools/openapi-generator/issues) with your suggestion to gather feedback from the community.
 - If you're adding a new option to a generator, please consider using the `-t` option with customized templates instead or start a discussion first by opening an issue as we want to avoid adding too many options to the generator.
 - It's recommended to **create a new git branch** for the change so that the merge commit message looks nicer in the commit history.

## How to contribute

### git

If you're new to git, you may find the following FAQs useful:

https://github.com/openapitools/openapi-generator/wiki/FAQ#git

### Branches

Please file the pull request against the correct branch, e.g. `master` for non-breaking changes. See the [Git Branches](https://github.com/OpenAPITools/openapi-generator/wiki/Git-Branches) page for more information.

### Code generators

All the code generators can be found in [modules/openapi-generator/src/main/java/org/openapitools/codegen/languages](https://github.com/openapitools/openapi-generator/tree/master/modules/openapi-generator/src/main/java/org/openapitools/codegen/languages)

If you want to add a new generator, follow the [new-generator](https://openapi-generator.tech/docs/new-generator) guide.

### Templates

All the templates ([mustache](https://mustache.github.io/)) can be found in [modules/openapi-generator/src/main/resources](https://github.com/openapitools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources).

For a list of variables available in the template, please refer to this [page](https://github.com/openapitools/openapi-generator/wiki/Mustache-Template-Variables)


### Style guide
Code change should conform to the programming style guide of the respective languages:
- Ada: https://en.wikibooks.org/wiki/Ada_Style_Guide/Source_Code_Presentation
- Android: https://source.android.com/source/code-style.html
- Bash: https://github.com/bahamas10/bash-style-guide
- C#: https://msdn.microsoft.com/en-us/library/vstudio/ff926074.aspx
- C++: https://google.github.io/styleguide/cppguide.html
- C++ (Tizen): https://wiki.tizen.org/Native_Platform_Coding_Idiom_and_Style_Guide#C.2B.2B_Coding_Style
- C++ (Unreal Engine 4): https://docs.unrealengine.com/en-US/ProductionPipelines/DevelopmentSetup/CodingStandard/index.html
- Clojure: https://github.com/bbatsov/clojure-style-guide
- Crystal: https://crystal-lang.org/reference/conventions/coding_style.html
- Dart: https://www.dartlang.org/guides/language/effective-dart/style
- Eiffel: https://www.eiffel.org/doc/eiffel/Coding%20Standards
- Elixir: https://github.com/christopheradams/elixir_style_guide
- Erlang: https://github.com/inaka/erlang_guidelines
- Go: https://github.com/golang/go/wiki/CodeReviewComments
- Groovy: http://groovy-lang.org/style-guide.html
- Haskell: https://github.com/tibbe/haskell-style-guide/blob/master/haskell-style.md
- Java: https://google.github.io/styleguide/javaguide.html
- JavaScript: https://github.com/airbnb/javascript/
- Julia: https://docs.julialang.org/en/v1/manual/style-guide/
- Kotlin: https://kotlinlang.org/docs/reference/coding-conventions.html
- ObjC: https://github.com/NYTimes/objective-c-style-guide
- Perl: http://perldoc.perl.org/perlstyle.html
- PHP: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-12-extended-coding-style-guide.md
- PowerShell: https://msdn.microsoft.com/en-us/library/dd878270(v=vs.85).aspx
- Python: https://www.python.org/dev/peps/pep-0008/
- R: https://google.github.io/styleguide/Rguide.xml
- Ruby: https://github.com/bbatsov/ruby-style-guide
- Rust: https://github.com/rust-lang-nursery/fmt-rfcs/blob/master/guide/guide.md (the default [rustfmt](https://github.com/rust-lang-nursery/rustfmt) configuration)
- Scala: http://docs.scala-lang.org/style/
- Swift: [Apple Developer](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html)
- TypeScript: https://github.com/Microsoft/TypeScript/wiki/Coding-guidelines
- Xojo: https://documentation.xojo.com/topics/code_management/coding_guidelines.html

For other languages, feel free to suggest.

You may find the current code base not 100% conform to the coding style and we welcome contributions to fix those.

For [Vendor Extensions](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#vendorExtensions), please follow the naming convention below:
- For general vendor extension, use lower case and hyphen. e.g. `x-is-unique`, `x-content-type`
- For language-specified vendor extension, put it in the form of `x-{lang}-{extension-name}`. e.g. `x-objc-operation-id`, `x-java-feign-retry-limit`
- For a list of existing vendor extensions in use, please refer to https://github.com/openapitools/openapi-generator/wiki/Vendor-Extensions. If you've added new vendor extensions as part of your PR, please update the wiki page.

### Building

The `openapi-generator-cli` can be built using the following command. This will generate the `openapi-generator-cli.jar` in the `modules/openapi-generator-cli/target` directory without running the tests and generating the Javadocs.

```shell
./mvnw clean install -DskipTests -Dmaven.javadoc.skip=true
```

Or on Windows:

```shell
mvnw.cmd clean install -DskipTests -Dmaven.javadoc.skip=true
```

The binary can run via `java -jar`. For example:

```shell
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar help
```

### Testing

To add test cases (optional) covering the change in the code generator, please refer to [modules/openapi-generator/src/test/java/org/openapitools/codegen](https://github.com/openapitools/openapi-generator/tree/master/modules/openapi-generator/src/test/java/org/openapitools/codegen)

To test the templates, please perform the following:

- Update the Petstore sample by running the shell scripts under the `bin` folder. For example, run `./bin/generate-samples.sh ./bin/configs/python*` to update the Python-related samples under [`samples`](https://github.com/openapitools/openapi-generator/tree/master/samples). For Windows, please install [GIT bash](https://gitforwindows.org/). (If you find that there are new files generated or unexpected changes as a result of the update, that's not unusual as the test cases are added to the OpenAPI spec from time to time. If you've questions or concerns, please open a ticket to start a discussion)
- During development, it can be helpful to quickly regenerate the samples without recompiling all of openapi-generator, e.g. when you have only updated the mustache templates. This can be done by passing the `-t` parameter: `-t modules/openapi-generator/src/main/resources/python`.
- Run the tests in the sample folder using maven `mvn integration-test -f /path/to/pom.xml`, e.g. `mvn integration-test -f samples/client/petstore/python/pom.xml`. (some languages may not contain unit testing for Petstore and we're looking for contribution from the community to implement those tests). __Please notice:__ you must run a local instance of the Petstore server in order to perform the tests, as running them against petstore.swagger.io is not supported anymore. Please refer to item 3 of [Integration Tests - How to add integration tests for new Petstore samples](https://github.com/OpenAPITools/openapi-generator/wiki/Integration-Tests#how-to-add-integration-tests-for-new-petstore-samples) to learn how to quickly configure and run it.
- Finally, git commit the updated samples files: `git commit -a` (`git add -A` if added files with new test cases)
- For new test cases, please add to the [Fake Petstore spec](https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator/src/test/resources/3_0/petstore-with-fake-endpoints-models-for-testing.yaml)

To start the CI tests, you can:
- Run `mvn verify -Psamples`, assuming you have all the required tools installed to run tests for different languages.
- Leverage http://travis-ci.org to run the CI tests by adding your own openapi-generator repository.
- Run some of the CI tests in your local workspace.

See [OpenAPI Tools wiki](https://github.com/OpenAPITools/openapi-generator/wiki/Integration-Tests) for more information about the integration tests.

### Tips
- Smaller changes are easier to review
- [Optional] For bug fixes, provide a OpenAPI Spec to repeat the issue so that the reviewer can use it to confirm the fix
- Add test case(s) to cover the change
- Document the fix in the code to make the code more readable
- Make sure test cases passed after the change (one way is to leverage https://travis-ci.org/ to run the CI tests)
- File a PR with meaningful title, description and commit messages
- Make sure the option "Allow edits from maintainers" in the PR is selected so that the maintainers can update your PRs with minor fixes, if needed.
- Recommended git settings
   - `git config core.autocrlf input` to tell Git convert CRLF to LF on commit but not the other way around
- To close an issue (e.g. issue 1542) automatically after a PR is merged, use keywords "fix", "close", "resolve" in the PR description, e.g. `fix #1542`. (Ref: [closing issues using keywords](https://help.github.com/articles/closing-issues-using-keywords/))

```

### File: docker-entrypoint.sh
```sh
#!/usr/bin/env bash

set -euo pipefail

# GEN_DIR allows to share the entrypoint between Dockerfile and run-in-docker.sh (backward compatible)
GEN_DIR=${GEN_DIR:-/opt/openapi-generator}
JAVA_OPTS=${JAVA_OPTS:-"-DloggerPath=conf/log4j.properties"}

cli="${GEN_DIR}/modules/openapi-generator-cli"
codegen="${cli}/target/openapi-generator-cli.jar"

# We code in a list of commands here as source processing is potentially buggy (requires undocumented conventional use of annotations).
# A list of known commands helps us determine if we should compile CLI. There's an edge-case where a new command not added to this
# list won't be considered a "real" command. We can get around that a bit by checking CLI completions beforehand if it exists.
commands="config-help,generate,batch,help,list,meta,validate,version"

if [ $# == 0 ]; then
    echo "No command specified. Available commands:"
    for i in $(echo $commands | sed "s/,/ /g"); do
        echo "  $i"
    done
    exit
fi

# if CLI jar exists, check $1 against completions available in the CLI
if [[ -f "${codegen}" && -n "$(java ${JAVA_OPTS} -jar "${codegen}" completion | grep "^$1\$" )" ]]; then
    command=$1
    shift
    exec java ${JAVA_OPTS} -jar "${codegen}" "${command}" "$@"
elif [[ -n "$(echo $commands | tr ',' '\n' | grep "^$1\$" )" ]]; then
    # If CLI jar does not exist, and $1 is a known CLI command, build the CLI jar and run that command.
    if [[ ! -f "${codegen}" ]]; then
        (cd "${GEN_DIR}" && exec mvn -am -pl "modules/openapi-generator-cli" -Duser.home=$(dirname $MAVEN_CONFIG) package)
    fi
    command=$1
    shift
    exec java ${JAVA_OPTS} -jar "${codegen}" "${command}" "$@"
else
    # Pass args as linux commands. This allows us to do something like: docker run -it (-e…, -v…) image ls -la
    exec "$@"
fi

```

### File: new.sh
```sh
#!/usr/bin/env bash

set -euo pipefail
set -o noclobber

usage() {
cat <<EOF
Stubs out files for new generators

Usage:
$0 [options]
    Options:
$(grep "[[:space:]].)\ #" $0 | tr -d "#" | sed -E 's/( \| \*)//' | sed -E 's/([a-zA-Z])\)/-\1/')

Examples:
  Create a server generator for ktor:
  $0 -n kotlin -s

    Creates:
    modules/openapi-generator/src/main/java/org/openapitools/codegen/languages/KotlinServerCodegen.java
    modules/openapi-generator/src/main/resources/kotlin-server/README.mustache
    modules/openapi-generator/src/main/resources/kotlin-server/model.mustache
    modules/openapi-generator/src/main/resources/kotlin-server/api.mustache
    bin/configs/kotlin-server-petstore-new.yaml

  Create a generic C# server generator:
  $0 -n csharp -s -t
    Creates:
    modules/openapi-generator/src/main/java/org/openapitools/codegen/languages/CsharpServerCodegen.java
    modules/openapi-generator/src/main/resources/csharp-server/README.mustache
    modules/openapi-generator/src/main/resources/csharp-server/model.mustache
    modules/openapi-generator/src/main/resources/csharp-server/api.mustache
    bin/configs/csharp-server-petstore-new.yaml
    modules/openapi-generator/src/test/java/org/openapitools/codegen/csharp/CsharpServerCodegenTest.java
    modules/openapi-generator/src/test/java/org/openapitools/codegen/csharp/CsharpServerCodegenModelTest.java
    modules/openapi-generator/src/test/java/org/openapitools/codegen/csharp/CsharpServerCodegenOptionsTest.java
    modules/openapi-generator/src/test/java/org/openapitools/codegen/options/CsharpServerCodegenOptionsProvider.java
EOF
    exit 0;
}

declare os=${OSTYPE//[0-9.]/}
declare root=$(cd $(dirname "${BASH_SOURCE}") && pwd)
declare gen_type=
declare tests=0
declare gen_name

checkPreviousGenType() {
    if [ "a" != "a$gen_type" ]; then
        echo "[error] You may only set a single generator type at a time!" >&2
        usage >&2
        exit 1
    fi
}

[ $# -eq 0 ] && usage
while getopts ":hcsdtfHn:" arg; do
  case ${arg} in
    n) # Required. Specify generator name, should be kebab-cased.
      gen_name=${OPTARG}
      ;;
    c) # Create a client generator
        checkPreviousGenType
        gen_type=client
        ;;
    s) # Create a server generator
        checkPreviousGenType
        gen_type=server
        ;;
    d) # Create a documentation generator
        checkPreviousGenType
        gen_type=documentation
        ;;
    H) # Create a schema generator
        checkPreviousGenType
        gen_type=schema
        ;;
    f) # Create a config generator
        checkPreviousGenType
        gen_type=config
        ;;
    t) # When specified, creates test file(s) for the generator.
      tests=1
      ;;
    h | *) # Display help.
      usage
      exit 0
      ;;
  esac
done

if [ -z "$gen_type" ]; then
    echo "[error] You may set a generator type" >&2
    usage >&2
    exit 1
fi

[ -z "${gen_name}" ] && usage

titleCase() {
  if [ "$os" == "darwin" ]; then
    echo $1 | tr '-' ' ' | tr '_' ' ' | ruby -e "print STDIN.gets.split.map(&:capitalize).join(' ')" | tr -d ' '
  else
    read -ra words <<< $(echo $1 | tr '-' ' ' | tr '_' ' ')
    echo "${words[@]^}" | tr -d ' '
  fi
}

kebabCase() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '[:upper:]' '[:lower:]'
}

kebabCasePath() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '-' '/' | tr '[:upper:]' '[:lower:]'
}

kebabCasePathWin() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '-' '\\' | tr '[:upper:]' '[:lower:]'
}

kebabCasePkg() {
  echo $1 | tr '_' ' ' | tr ' ' '-' | tr '-' '.' | tr '[:upper:]' '[:lower:]'
}

upperCase() {
  echo $1 | tr '[[:lower:]]' '[[:upper:]]'
}

declare lang_classname=$(titleCase "${gen_name}-${gen_type}-Codegen")
declare gen_name_camel=$(kebabCase "${gen_name}")
declare gen_name_camel_path=$(kebabCasePath "${gen_name}")
declare gen_name_camel_pathwin=$(kebabCasePathWin "${gen_name}")
declare gen_name_camel_pkg=$(kebabCasePkg "${gen_name}")
declare codegen_type_enum=$(upperCase "${gen_type}")

# Step 1: Add Language Generator
[ -f "${root}/modules/openapi-generator/src/main/java/org/openapitools/codegen/languages/${lang_classname}.java" ] && \
    echo "${lang_classname} already exists" && exit 1;

echo "Creating modules/openapi-generator/src/main/java/org/openapitools/codegen/languages/${lang_classname}.java"
cat > "${root}/modules/openapi-generator/src/main/java/org/openapitools/codegen/languages/${lang_classname}.java" <<EOF
package org.openapitools.codegen.languages;

import org.openapitools.codegen.*;
import io.swagger.models.properties.ArrayProperty;
import io.swagger.models.properties.MapProperty;
import io.swagger.models.properties.Property;
import io.swagger.models.parameters.Parameter;

import java.io.File;
import java.util.*;

import org.apache.commons.lang3.StringUtils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ${lang_classname} extends DefaultCodegen implements CodegenConfig {
    public static final String PROJECT_NAME = "projectName";

    private final Logger LOGGER = LoggerFactory.getLogger(${lang_classname}.class);

    public CodegenType getTag() {
        return CodegenType.${codegen_type_enum};
    }

    public String getName() {
        return "${gen_name_camel}";
    }

    public String getHelp() {
        return "Generates a ${gen_name_camel} ${gen_type}.";
    }

    public ${lang_classname}() {
        super();

        outputFolder = "generated-code" + File.separator + "${gen_name_camel}";
        modelTemplateFiles.put("model.mustache", ".zz");
        apiTemplateFiles.put("api.mustache", ".zz");
        embeddedTemplateDir = templateDir = "${gen_name_camel}";
        apiPackage = "Apis";
        modelPackage = "Models";
        supportingFiles.add(new SupportingFile("README.mustache", "", "README.md"));
        // TODO: Fill this out.
    }
}
EOF

# Step 2: Register the new class with service loader
echo -e "\norg.openapitools.codegen.languages.${lang_classname}" >> "${root}/modules/openapi-generator/src/main/resources/META-INF/services/org.openapitools.codegen.CodegenConfig"

# Step 3: Create resource files
mkdir -p "${root}/modules/openapi-generator/src/main/resources/${gen_name_camel}"
echo "Creating modules/openapi-generator/src/main/resources/${gen_name_camel}/README.mustache" && \
    touch "${root}/modules/openapi-generator/src/main/resources/${gen_name_camel}/README.mustache"
echo "Creating modules/openapi-generator/src/main/resources/${gen_name_camel}/model.mustache" && \
    touch "${root}/modules/openapi-generator/src/main/resources/${gen_name_camel}/model.mustache"
echo "Creating modules/openapi-generator/src/main/resources/${gen_name_camel}/api.mustache" && \
    touch "${root}/modules/openapi-generator/src/main/resources/${gen_name_camel}/api.mustache"

# Step 4: Create generation config scripts
echo "Creating bin/configs/${gen_name_camel}-petstore-new.yaml"
cat > "${root}/bin/configs/${gen_name_camel}-petstore-new.yaml"<<EOF
generatorName: ${gen_name_camel}
outputDir: samples/${gen_type}/petstore/${gen_name_camel_path}
inputSpec: modules/openapi-generator/src/test/resources/3_0/petstore.yaml
templateDir: modules/openapi-generator/src/main/resources/${gen_name_camel}
additionalProperties:
  hideGenerationTimestamp: "true"
EOF

# Step 5: (optional) Create OpenAPI Generator test files
if [ "1" -eq "${tests}" ]; then
    mkdir -p "${root}/modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}"
    # Codegen
    echo "Creating modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}/${lang_classname}Test.java"
    cat > "${root}/modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}/${lang_classname}Test.java"<<EOF
package org.openapitools.codegen.${gen_name_camel_pkg};

import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.${lang_classname};
import io.swagger.models.*;
import io.swagger.parser.SwaggerParser;
import org.testng.Assert;
import org.testng.annotations.Test;

public class ${lang_classname}Test {

    ${lang_classname} codegen = new ${lang_classname}();

    @Test
    public void shouldSucceed() throws Exception {
        // TODO: Complete this test.
        Assert.fail("Not implemented.");
    }
}
EOF

    # Model
    echo "Creating modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}/${lang_classname}ModelTest.java"
    cat > "${root}/modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}/${lang_classname}ModelTest.java"<<EOF
package org.openapitools.codegen.${gen_name_camel_pkg};

import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.${lang_classname};
import io.swagger.models.*;
import io.swagger.models.properties.*;

import org.testng.Assert;
import org.testng.annotations.Test;

@SuppressWarnings("static-method")
public class ${lang_classname}ModelTest {

    @Test(description = "convert a simple java model")
    public void simpleModelTest() {
        final Model model = new ModelImpl()
                .description("a sample model")
                .property("id", new LongProperty())
                .property("name", new StringProperty())
                .required("id")
                .required("name");
        final DefaultCodegen codegen = new ${lang_classname}();

        // TODO: Complete this test.
        Assert.fail("Not implemented.");
    }

}

EOF

    # Options
    echo "Creating modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}/${lang_classname}OptionsTest.java"
    cat > "${root}/modules/openapi-generator/src/test/java/org/openapitools/codegen/${gen_name_camel_path}/${lang_classname}OptionsTest.java"<<EOF
package org.openapitools.codegen.${gen_name_camel_pkg};

import org.openapitools.codegen.AbstractOptionsTest;
import org.openapitools.codegen.CodegenConfig;
import org.openapitools.codegen.languages.${lang_classname};
import org.openapitools.codegen.options.${lang_classname}OptionsProvider;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;

public class ${lang_classname}OptionsTest extends AbstractOptionsTest {
    private ${lang_classname} codegen = mock(${lang_classname}.class, mockSettings);

    public ${lang_classname}OptionsTest() {
        super(new ${lang_classname}OptionsProvider());
    }

    @Override
    protected CodegenConfig getCodegenConfig() {
        return codegen;
    }

    @SuppressWarnings("unused")
    @Override
    protected void verifyOptions() {
        // TODO: Complete options using Mockito
        // verify(codegen).someMethod(arguments)
    }
}

EOF

    # Options Provider
    echo "Creating modules/openapi-generator/src/test/java/org/openapitools/codegen/options/${lang_classname}OptionsProvider.java"
    cat > "${root}/modules/openapi-generator/src/test/java/org/openapitools/codegen/options/${lang_classname}OptionsProvider.java"<<EOF
package org.openapitools.codegen.options;

import org.openapitools.codegen.CodegenConstants;
import org.openapitools.codegen.languages.${lang_classname};

import com.google.common.collect.ImmutableMap;

import java.util.Map;

public class ${lang_classname}OptionsProvider implements OptionsProvider {
    public static final String PROJECT_NAME_VALUE = "OpenAPI";

    @Override
    public String getLanguage() {
        return "${gen_name_camel}";
    }

    @Override
    public Map<String, String> createOptions() {
        ImmutableMap.Builder<String, String> builder = new ImmutableMap.Builder<String, String>();
        return builder
                .put(${lang_classname}.PROJECT_NAME, PROJECT_NAME_VALUE)
                .build();
    }

    @Override
    public boolean isServer() {
        return false;
    }
}

EOF
fi

echo "Finished."

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
