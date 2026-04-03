---
id: bold-brew-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:59.032837
---

# KNOWLEDGE EXTRACT: bold-brew
> **Extracted on:** 2026-03-30 17:31:12
> **Source:** bold-brew

---

## File: `.env`
```
APP_NAME=bbrew
APP_VERSION=0.0.1-local
CONTAINER_IMAGE_NAME=bbrew
BUILD_GOVERSION=1.25
BUILD_GOOS=darwin
BUILD_GOARCH=arm64
```

## File: `.gitignore`
```
/dist/
bbrew
node_modules
```

## File: `.golangci.yaml`
```yaml
version: "2"
run:
  concurrency: 4
  go: "1.25"
  tests: true
  allow-parallel-runners: true
output:
  formats:
    text:
      path: stdout
      print-linter-name: true
      print-issued-lines: true
linters:
  default: none
  enable:
    - gosec
    - govet
    - revive
    - staticcheck
    - unused
  exclusions:
    generated: lax
    presets:
      - comments
      - common-false-positives
      - legacy
      - std-error-handling
formatters:
  enable:
    - gofmt
```

## File: `.goreleaser.yaml`
```yaml
version: 2
project_name: bbrew

builds:
  - id: bbrew
    main: ./cmd/bbrew
    binary: bbrew
    goos:
      - darwin
      - linux
    goarch:
      - amd64
      - arm64
    env:
      - CGO_ENABLED=0
    ldflags:
      - -s -w
      - -X 'bbrew/internal/services.AppVersion={{ .Version }}'

archives:
  - format: tar.gz
    name_template: "{{ .ProjectName }}_{{ .Version }}_{{ .Os }}_{{ .Arch }}"

checksum:
  name_template: "checksums.txt"
  algorithm: sha256

release:
  github:
    owner: Valkyrie00
    name: bold-brew
  draft: false
  prerelease: auto
  header: |
    ## Bold Brew {{ .Version }}
    
    Install or upgrade:
    ```bash
    brew upgrade bbrew
    # or
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/install.sh)"
    ```

brews:
  - name: bbrew
    homepage: "https://bold-brew.com"
    description: "Modern TUI for managing Homebrew packages and casks on macOS and Linux"
    license: "MIT"
    url_template: "https://github.com/Valkyrie00/bold-brew/releases/download/{{ .Tag }}/{{ .ArtifactName }}"
    commit_author:
      name: goreleaserbot
      email: bot@goreleaser.com
    commit_msg_template: "Brew formula update for {{ .ProjectName }} version {{ .Tag }}"
    directory: Formula
    test: |
      assert_match "Usage", shell_output("#{bin}/bbrew -h")
    install: |
      bin.install "bbrew"
    repository:
      owner: Valkyrie00
      name: homebrew-bbrew
      branch: main
      token: "{{ .Env.GITHUB_TOKEN }}"

changelog:
  use: github
  sort: asc
  filters:
    exclude:
      - "^docs:"
      - "^test:"
      - "^ci:"
      - "^chore:"
      - "^style:"
      - "Merge pull request"
      - "Merge branch"
  groups:
    - title: "⚠️ Breaking Changes"
      regexp: "^.*!:.+$"
      order: 0
    - title: "✨ Features"
      regexp: "^.*feat[(\\w)]*:.*$"
      order: 1
    - title: "🐛 Bug Fixes"
      regexp: "^.*fix[(\\w)]*:.*$"
      order: 2
    - title: "♻️ Refactoring"
      regexp: "^.*refactor[(\\w)]*:.*$"
      order: 3
    - title: "⚡️ Performance"
      regexp: "^.*perf[(\\w)]*:.*$"
      order: 4
    - title: "🔒 Security"
      regexp: "^.*security[(\\w)]*:.*$"
      order: 5
```

## File: `build.js`
```javascript
const ejs = require('ejs');
const fs = require('fs');
const path = require('path');
const marked = require('marked');
const frontMatter = require('front-matter');
const ejsLayouts = require('ejs-layouts');

// Configuration
const config = {
    srcDir: 'site',
    distDir: 'docs',
    templatesDir: 'site/templates',
    contentDir: 'site/content',
    site: {
        name: 'Bold Brew',
        description: 'A modern TUI for Homebrew',
        url: 'https://bold-brew.com'
    }
};

// Function to generate a page
async function generatePage(template, data, outputPath) {
    const templatePath = path.join(config.templatesDir, template);
    const templateContent = fs.readFileSync(templatePath, 'utf-8');
    const layoutPath = path.join(config.templatesDir, 'layout.ejs');
    const layoutContent = fs.readFileSync(layoutPath, 'utf-8');
    
    // Render the template content
    const content = ejs.render(templateContent, {
        ...data,
        filename: templatePath
    });

    // Render the layout with the content
    const html = ejs.render(layoutContent, {
        ...data,
        filename: layoutPath,
        content
    });

    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
    fs.writeFileSync(outputPath, html);
}

// Function to generate the homepage
async function generateHomepage() {
    const posts = getBlogPosts();
    await generatePage('index.ejs', {
        title: 'Bold Brew (bbrew) - Modern Homebrew TUI Manager for macOS and Linux',
        description: 'Bold Brew (bbrew) is the modern Terminal User Interface for Homebrew on macOS and Linux. Install, update, and manage packages and casks with an elegant TUI.',
        keywords: 'bbrew, Bold Brew, Homebrew TUI, macOS package manager, Linux package manager, Homebrew casks, Homebrew GUI, terminal package manager, Homebrew alternative, Project Bluefin, macOS development tools, Linux development tools',
        canonicalUrl: config.site.url,
        ogType: 'website',
        posts,
        site: config.site
    }, path.join(config.distDir, 'index.html'));
}

// Function to generate the blog
async function generateBlog() {
    // Generate the main blog page
    await generatePage('blog/index.ejs', {
        title: 'Blog | Bold Brew (bbrew)',
        description: 'Tips, tutorials, and guides for managing Homebrew packages on macOS',
        keywords: 'Homebrew blog, macOS tutorials, package management, Bold Brew guides',
        canonicalUrl: `${config.site.url}/blog/`,
        ogType: 'website',
        breadcrumb: [
            { text: 'Home', url: '/' },
            { text: 'Blog', url: '/blog/' }
        ],
        posts: getBlogPosts(),
        site: config.site
    }, path.join(config.distDir, 'blog/index.html'));

    // Generate article pages
    const blogDir = path.join(__dirname, config.contentDir, 'blog');
    if (fs.existsSync(blogDir)) {
        const files = fs.readdirSync(blogDir)
            .filter(file => file.endsWith('.md'));

        for (const file of files) {
            const filePath = path.join(blogDir, file);
            const content = fs.readFileSync(filePath, 'utf8');
            const { attributes, body } = frontMatter(content);
            const htmlContent = marked.parse(body);
            const outputFile = file.replace('.md', '.html');

            await generatePage('blog/post.ejs', {
                title: attributes.title || '',
                description: attributes.description || '',
                keywords: attributes.keywords || 'Homebrew, macOS, package management, Bold Brew, bbrew, terminal, development tools',
                date: attributes.date || '',
                content: htmlContent,
                canonicalUrl: `${config.site.url}/blog/${outputFile}`,
                ogType: 'article',
                breadcrumb: [
                    { text: 'Home', url: '/' },
                    { text: 'Blog', url: '/blog/' },
                    { text: attributes.title || '', url: `/blog/${outputFile}` }
                ],
                site: config.site
            }, path.join(config.distDir, 'blog', outputFile));
        }
    }
}

function getBlogPosts() {
    const blogDir = path.join(__dirname, config.contentDir, 'blog');
    const posts = [];
    
    if (!fs.existsSync(blogDir)) {
        return posts;
    }

    const files = fs.readdirSync(blogDir)
        .filter(file => file.endsWith('.md'));

    for (const file of files) {
        const content = fs.readFileSync(path.join(blogDir, file), 'utf8');
        const { attributes } = frontMatter(content);
        const outputFile = file.replace('.md', '.html');

        if (attributes.title && attributes.date) {
            posts.push({
                title: attributes.title,
                date: attributes.date,
                url: `/blog/${outputFile}`,
                excerpt: attributes.description || ''
            });
        }
    }

    return posts.sort((a, b) => new Date(b.date) - new Date(a.date));
}

// Function to generate the sitemap
async function generateSitemap() {
    const posts = getBlogPosts();
    const baseUrl = config.site.url;
    const today = new Date().toISOString().split('T')[0];

    // Static pages
    const staticPages = [
        {
            url: '/',
            lastmod: today,
            changefreq: 'weekly',
            priority: '1.0'
        },
        {
            url: '/blog/',
            lastmod: today,
            changefreq: 'weekly',
            priority: '0.9'
        }
    ];

    // Blog pages
    const blogPages = posts.map(post => ({
        url: post.url,
        lastmod: post.date,
        changefreq: 'monthly',
        priority: '0.8'
    }));

    // Combine all pages
    const allPages = [...staticPages, ...blogPages];

    // Generate XML content
    const sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allPages.map(page => `  <url>
    <loc>${baseUrl}${page.url}</loc>
    <lastmod>${page.lastmod}</lastmod>
    ${page.changefreq ? `<changefreq>${page.changefreq}</changefreq>` : ''}
    ${page.priority ? `<priority>${page.priority}</priority>` : ''}
  </url>`).join('\n')}
</urlset>`;

    // Write the sitemap.xml file
    fs.writeFileSync(path.join(config.distDir, 'sitemap.xml'), sitemapContent);
}

// Main function
async function build() {
    try {
        // Clean the output directory while preserving assets, .git and other static files
        if (fs.existsSync(config.distDir)) {
            // Read all files in the docs directory
            const files = fs.readdirSync(config.distDir);
            
            // List of files/directories to preserve
            const preserveFiles = [
                'assets',
                '.git',
                'manifest.json',
                'robots.txt',
                'CNAME'
            ];
            
            // Remove only dynamically generated files
            for (const file of files) {
                if (!preserveFiles.includes(file)) {
                    const filePath = path.join(config.distDir, file);
                    // Check if it's a dynamically generated HTML file
                    if (file.endsWith('.html')) {
                        fs.rmSync(filePath, { recursive: true, force: true });
                    }
                }
            }
        } else {
            fs.mkdirSync(config.distDir);
        }
        
        // Generate pages
        await generateHomepage();
        await generateBlog();
        await generateSitemap();
        
        console.log('Build completed successfully!');
    } catch (error) {
        console.error('Build failed:', error);
        process.exit(1);
    }
}

build(); 
```

## File: `Containerfile`
```
FROM golang:1.25

# Install dependencies
RUN curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b $(go env GOPATH)/bin v2.5.0
RUN go install github.com/goreleaser/goreleaser/v2@latest

# Install security tools
RUN go install golang.org/x/vuln/cmd/govulncheck@latest
RUN go install github.com/securego/gosec/v2/cmd/gosec@latest

WORKDIR /app
```

## File: `go.mod`
```
module bbrew

go 1.25

require (
	github.com/gdamore/tcell/v2 v2.8.1
	github.com/rivo/tview v0.0.0-20250625164341-a4a78f1e05cb
	golang.org/x/text v0.27.0
)

require (
	github.com/adrg/xdg v0.5.3 // indirect
	github.com/gdamore/encoding v1.0.1 // indirect
	github.com/lucasb-eyer/go-colorful v1.2.0 // indirect
	github.com/mattn/go-runewidth v0.0.16 // indirect
	github.com/rivo/uniseg v0.4.7 // indirect
	golang.org/x/sys v0.34.0 // indirect
	golang.org/x/term v0.33.0 // indirect
)
```

## File: `go.sum`
```
github.com/adrg/xdg v0.5.3 h1:xRnxJXne7+oWDatRhR1JLnvuccuIeCoBu2rtuLqQB78=
github.com/adrg/xdg v0.5.3/go.mod h1:nlTsY+NNiCBGCK2tpm09vRqfVzrc2fLmXGpBLF0zlTQ=
github.com/gdamore/encoding v1.0.1 h1:YzKZckdBL6jVt2Gc+5p82qhrGiqMdG/eNs6Wy0u3Uhw=
github.com/gdamore/encoding v1.0.1/go.mod h1:0Z0cMFinngz9kS1QfMjCP8TY7em3bZYeeklsSDPivEo=
github.com/gdamore/tcell/v2 v2.8.1 h1:KPNxyqclpWpWQlPLx6Xui1pMk8S+7+R37h3g07997NU=
github.com/gdamore/tcell/v2 v2.8.1/go.mod h1:bj8ori1BG3OYMjmb3IklZVWfZUJ1UBQt9JXrOCOhGWw=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/lucasb-eyer/go-colorful v1.2.0 h1:1nnpGOrhyZZuNyfu1QjKiUICQ74+3FNCN69Aj6K7nkY=
github.com/lucasb-eyer/go-colorful v1.2.0/go.mod h1:R4dSotOR9KMtayYi1e77YzuveK+i7ruzyGqttikkLy0=
github.com/mattn/go-runewidth v0.0.16 h1:E5ScNMtiwvlvB5paMFdw9p4kSQzbXFikJ5SQO6TULQc=
github.com/mattn/go-runewidth v0.0.16/go.mod h1:Jdepj2loyihRzMpdS35Xk/zdY8IAYHsh153qUoGf23w=
github.com/rivo/tview v0.0.0-20250625164341-a4a78f1e05cb h1:n7UJ8X9UnrTZBYXnd1kAIBc067SWyuPIrsocjketYW8=
github.com/rivo/tview v0.0.0-20250625164341-a4a78f1e05cb/go.mod h1:cSfIYfhpSGCjp3r/ECJb+GKS7cGJnqV8vfjQPwoXyfY=
github.com/rivo/uniseg v0.2.0/go.mod h1:J6wj4VEh+S6ZtnVlnTBMWIodfgj8LQOQFoIToxlJtxc=
github.com/rivo/uniseg v0.4.3/go.mod h1:FN3SvrM+Zdj16jyLfmOkMNblXMcoc8DfTHruCPUcx88=
github.com/rivo/uniseg v0.4.7 h1:WUdvkW8uEhrYfLC4ZzdpI2ztxP1I582+49Oc5Mq64VQ=
github.com/rivo/uniseg v0.4.7/go.mod h1:FN3SvrM+Zdj16jyLfmOkMNblXMcoc8DfTHruCPUcx88=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.13.0/go.mod h1:y6Z2r+Rw4iayiXXAIxJIDAJ1zMW4yaTpebo8fPOliYc=
golang.org/x/crypto v0.19.0/go.mod h1:Iy9bg/ha4yyC70EfRS8jz+B6ybOBKMaSxLj6P6oBDfU=
golang.org/x/crypto v0.23.0/go.mod h1:CKFgDieR+mRhux2Lsu27y0fO304Db0wZe70UKqHu0v8=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.8.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.12.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.15.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20220722155237-a158d28d115b/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.6.0/go.mod h1:2Tu9+aMcznHK/AK1HMvgo6xiTLG5rD5rZLDS+rp2Bjs=
golang.org/x/net v0.10.0/go.mod h1:0qNGK6F8kojg2nk9dLZ2mShWaEBan6FAoqfSigmmuDg=
golang.org/x/net v0.15.0/go.mod h1:idbUs1IY1+zTqbi8yxTbhexhEEk5ur9LInksu6HrEpk=
golang.org/x/net v0.21.0/go.mod h1:bIjVDfnllIU7BJ2DNgfnXvpSvtn8VRwhlsaeUTyUS44=
golang.org/x/net v0.25.0/go.mod h1:JkAGAh7GEvH74S6FOH42FLoXpXbE/aqXSrIQjXgsiwM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.1.0/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.3.0/go.mod h1:FU7BRWz2tNW+3quACPkgCx/L+uEAv1htQ0V83Z9Rj+Y=
golang.org/x/sync v0.6.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.10.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220722155257-8c9f86f7a55f/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.5.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.8.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.12.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.17.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.20.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.29.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.34.0 h1:H5Y5sJ2L2JRdyv7ROF1he/lPdvFsd0mJHFw2ThKHxLA=
golang.org/x/sys v0.34.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2/go.mod h1:TeRTkGYfJXctD9OcfyVLyj2J3IxLnKwHJR8f4D8a3YE=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.0.0-20210927222741-03fcf44c2211/go.mod h1:jbD1KX2456YbFQfuXm/mYQcufACuNUgVhRMnK/tPxf8=
golang.org/x/term v0.5.0/go.mod h1:jMB1sMXY+tzblOD4FWmEbocvup2/aLOaQEp7JmGp78k=
golang.org/x/term v0.8.0/go.mod h1:xPskH00ivmX89bAKVGSKKtLOWNx2+17Eiy94tnKShWo=
golang.org/x/term v0.12.0/go.mod h1:owVbMEjm3cBLCHdkQu9b1opXd4ETQWc3BhuQGKgXgvU=
golang.org/x/term v0.17.0/go.mod h1:lLRBjIVuehSbZlaOtGMbcMncT+aqLLLmKrsjNrUguwk=
golang.org/x/term v0.20.0/go.mod h1:8UkIAJTvZgivsXaD6/pH6U9ecQzZ45awqEOzuCvwpFY=
golang.org/x/term v0.28.0/go.mod h1:Sw/lC2IAUZ92udQNf3WodGtn4k/XoLyZoh8v/8uiwek=
golang.org/x/term v0.33.0 h1:NuFncQrRcaRvVmgRkvM3j/F00gWIAlcmlB8ACEKmGIg=
golang.org/x/term v0.33.0/go.mod h1:s18+ql9tYWp1IfpV9DmCtQDDSRBUjKaw9M1eAv5UeF0=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/text v0.7.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.9.0/go.mod h1:e1OnstbJyHTd6l/uOt8jFFHp6TRDWZR/bV3emEE/zU8=
golang.org/x/text v0.13.0/go.mod h1:TvPlkZtksWOMsz7fbANvkp4WM8x/WCo/om8BMLbz+aE=
golang.org/x/text v0.14.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/text v0.15.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/text v0.21.0/go.mod h1:4IBbMaMmOPCJ8SecivzSH54+73PCFmPWxNTLm+vZkEQ=
golang.org/x/text v0.27.0 h1:4fGWRpyh641NLlecmyl4LOe6yDdfaYNrGb2zdfo4JV4=
golang.org/x/text v0.27.0/go.mod h1:1D28KMCvyooCX9hBiosv5Tz/+YLxj0j7XhWjpSUF7CU=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.6.0/go.mod h1:Xwgl3UAJ/d3gWutnCtw505GrjyAbvKui8lOU390QaIU=
golang.org/x/tools v0.13.0/go.mod h1:HvlwmtVNQAhOuCjW7xxvovg8wbNq7LwfXh/k7wXUl58=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
```

## File: `install.sh`
```bash
#!/bin/bash
#
# Bold Brew Installer
# https://github.com/Valkyrie00/bold-brew
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/install.sh | bash
#
# This script will:
#   1. Install Homebrew (if not already installed)
#   2. Install Bold Brew via Homebrew
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Logging functions
info() {
    echo -e "${BLUE}==>${NC} ${BOLD}$1${NC}"
}

success() {
    echo -e "${GREEN}==>${NC} ${BOLD}$1${NC}"
}

warn() {
    echo -e "${YELLOW}Warning:${NC} $1"
}

error() {
    echo -e "${RED}Error:${NC} $1" >&2
    exit 1
}

# Print banner
print_banner() {
    echo -e "${CYAN}"
    echo "  ____        _     _   ____                    "
    echo " | __ )  ___ | | __| | | __ ) _ __ _____      __"
    echo " |  _ \\ / _ \\| |/ _\` | |  _ \\| '__/ _ \\ \\ /\\ / /"
    echo " | |_) | (_) | | (_| | | |_) | | |  __/\\ V  V / "
    echo " |____/ \\___/|_|\\__,_| |____/|_|  \\___| \\_/\\_/  "
    echo -e "${NC}"
    echo -e "${BOLD}The Modern Homebrew TUI${NC}"
    echo ""
}

# Detect OS
detect_os() {
    OS="$(uname -s)"
    ARCH="$(uname -m)"
    
    case "$OS" in
        Darwin)
            OS_TYPE="macos"
            if [ "$ARCH" = "arm64" ]; then
                BREW_PREFIX="/opt/homebrew"
            else
                BREW_PREFIX="/usr/local"
            fi
            ;;
        Linux)
            OS_TYPE="linux"
            BREW_PREFIX="/home/linuxbrew/.linuxbrew"
            ;;
        *)
            error "Unsupported operating system: $OS"
            ;;
    esac
    
    info "Detected: $OS ($ARCH)"
}

# Check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Install Linux dependencies required by Homebrew
install_linux_deps() {
    info "Installing required dependencies..."
    
    # Use sudo if available and not root
    SUDO=""
    if [ "$(id -u)" -ne 0 ] && command_exists sudo; then
        SUDO="sudo"
    fi
    
    if command_exists apt-get; then
        # Debian/Ubuntu
        $SUDO apt-get update -qq
        $SUDO apt-get install -y -qq build-essential procps curl file git > /dev/null
    elif command_exists dnf; then
        # Fedora/RHEL
        $SUDO dnf install -y -q procps-ng curl file git gcc make > /dev/null
    elif command_exists pacman; then
        # Arch
        $SUDO pacman -Sy --noconfirm --quiet base-devel procps-ng curl file git > /dev/null
    else
        warn "Could not detect package manager. Please install: git, curl, build-essential"
    fi
    
    success "Dependencies installed"
}

# Get Homebrew binary path
get_brew_path() {
    if [ -x "$BREW_PREFIX/bin/brew" ]; then
        echo "$BREW_PREFIX/bin/brew"
    elif command_exists brew; then
        command -v brew
    else
        echo ""
    fi
}

# Setup Homebrew environment
setup_brew_env() {
    local brew_bin="$1"
    if [ -n "$brew_bin" ] && [ -x "$brew_bin" ]; then
        eval "$("$brew_bin" shellenv)"
    fi
}

# Install Homebrew
install_homebrew() {
    # On Linux, ensure dependencies are installed first
    if [ "$OS_TYPE" = "linux" ]; then
        install_linux_deps
    fi
    
    info "Installing Homebrew..."
    echo ""
    
    # Use Homebrew's official installer
    NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Setup environment after installation
    local brew_bin
    brew_bin=$(get_brew_path)
    
    if [ -z "$brew_bin" ]; then
        error "Homebrew installation failed. Please install manually: https://brew.sh"
    fi
    
    setup_brew_env "$brew_bin"
    success "Homebrew installed successfully!"
}

# Install Bold Brew
install_boldbrew() {
    info "Installing Bold Brew..."
    
    brew install Valkyrie00/homebrew-bbrew/bbrew
    
    success "Bold Brew installed successfully!"
}

# Print post-install instructions
print_instructions() {
    echo ""
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║${NC}  ${BOLD}✅ Installation Complete!${NC}                                 ${GREEN}║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "  Run ${CYAN}${BOLD}bbrew${NC} to start managing your Homebrew packages!"
    echo ""
    echo -e "  ${BOLD}Quick Start:${NC}"
    echo -e "    ${CYAN}bbrew${NC}                    # Browse all packages"
    echo -e "    ${CYAN}bbrew -f ~/Brewfile${NC}      # Use a Brewfile"
    echo -e "    ${CYAN}bbrew --help${NC}             # Show all options"
    echo ""
    echo -e "  ${BOLD}Documentation:${NC} ${BLUE}https://bold-brew.com${NC}"
    echo -e "  ${BOLD}GitHub:${NC}        ${BLUE}https://github.com/Valkyrie00/bold-brew${NC}"
    echo ""
    
    # Shell configuration reminder for Linux
    if [ "$OS_TYPE" = "linux" ]; then
        echo -e "  ${YELLOW}Note:${NC} You may need to restart your terminal or run:"
        echo -e "    ${CYAN}eval \"\$(${BREW_PREFIX}/bin/brew shellenv)\"${NC}"
        echo ""
    fi
}

# Main installation flow
main() {
    print_banner
    detect_os
    
    # Check for curl
    if ! command_exists curl; then
        error "curl is required but not installed. Please install curl first."
    fi
    
    # Check/Install Homebrew
    local brew_bin
    brew_bin=$(get_brew_path)
    
    if [ -n "$brew_bin" ]; then
        success "Homebrew is already installed"
        setup_brew_env "$brew_bin"
    else
        install_homebrew
    fi
    
    # Check if bbrew is already installed
    if command_exists bbrew; then
        warn "Bold Brew is already installed. Upgrading..."
        brew upgrade bbrew 2>/dev/null || brew install Valkyrie00/homebrew-bbrew/bbrew
    else
        install_boldbrew
    fi
    
    print_instructions
}

# Run main
main "$@"

```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Vito

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
##############################
# VARIABLES
##############################
# Load .env if exists (loaded first so defaults can override if not set)
-include .env

# Default values (can be overridden by .env or command line)
APP_NAME ?= bbrew
APP_VERSION ?= 0.0.1-local
CONTAINER_IMAGE_NAME ?= bbrew
BUILD_GOVERSION ?= 1.25
BUILD_GOOS ?= $(shell go env GOOS)
BUILD_GOARCH ?= $(shell go env GOARCH)

# Container runtime command
CONTAINER_RUN = podman run --rm -v $(PWD):/app $(CONTAINER_IMAGE_NAME)

##############################
# HELP
##############################
.PHONY: help
help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

.DEFAULT_GOAL := help

##############################
# CONTAINER
##############################
.PHONY: container-build-image
container-build-image: ## Build container image
	@podman build -f Containerfile -t $(CONTAINER_IMAGE_NAME) .

.PHONY: container-build-force
container-build-force: ## Force rebuild container image (no cache)
	@podman build --no-cache -f Containerfile -t $(CONTAINER_IMAGE_NAME) .

.PHONY: container-clean
container-clean: ## Remove container image
	@podman rmi $(CONTAINER_IMAGE_NAME) 2>/dev/null || true

##############################
# RELEASE
##############################
.PHONY: release-snapshot
release-snapshot: container-build-image ## Build and release snapshot (testing)
	@$(CONTAINER_RUN) goreleaser release --snapshot --clean

.PHONY: build-snapshot
build-snapshot: container-build-image ## Build snapshot without release
	@$(CONTAINER_RUN) goreleaser build --snapshot --clean

##############################
# BUILD
##############################
.PHONY: build
build: container-build-image ## Build the application binary
	@$(CONTAINER_RUN) env GOOS=$(BUILD_GOOS) GOARCH=$(BUILD_GOARCH) \
		go build -o $(APP_NAME) ./cmd/$(APP_NAME)

.PHONY: build-local
build-local: ## Build locally without container (requires Go installed)
	@go build -o $(APP_NAME) ./cmd/$(APP_NAME)

.PHONY: run
run: build ## Build and run the application
	@./$(APP_NAME)

.PHONY: clean
clean: ## Clean build artifacts
	@rm -f $(APP_NAME)
	@rm -rf dist/

##############################
# QUALITY
##############################
.PHONY: quality
quality: container-build-image ## Run linter checks
	@$(CONTAINER_RUN) golangci-lint run

.PHONY: quality-local
quality-local: ## Run linter locally (requires golangci-lint installed)
	@golangci-lint run

.PHONY: test
test: ## Run tests
	@go test -v ./...

.PHONY: test-coverage
test-coverage: ## Run tests with coverage
	@go test -v -coverprofile=coverage.out ./...
	@go tool cover -html=coverage.out -o coverage.html

##############################
# SECURITY
##############################
.PHONY: security
security: security-vuln security-scan ## Run all security checks

.PHONY: security-vuln
security-vuln: container-build-image ## Check for known vulnerabilities
	@$(CONTAINER_RUN) govulncheck ./...

.PHONY: security-vuln-local
security-vuln-local: ## Check vulnerabilities locally (requires govulncheck)
	@govulncheck ./...

.PHONY: security-scan
security-scan: container-build-image ## Run security scanner
	@$(CONTAINER_RUN) gosec ./...

.PHONY: security-scan-local
security-scan-local: ## Run security scanner locally (requires gosec)
	@gosec ./...

##############################
# WEBSITE
##############################
.PHONY: build-site
build-site: ## Build the static website
	@node build.js

.PHONY: serve-site
serve-site: ## Serve the website locally
	@npx http-server docs -p 3000

.PHONY: dev-site
dev-site: build-site serve-site ## Build and serve the website

##############################
# UTILITY
##############################
.PHONY: install
install: build-local ## Install binary to $GOPATH/bin
	@go install ./cmd/$(APP_NAME)

.PHONY: deps
deps: ## Download and tidy dependencies
	@go mod download
	@go mod tidy

.PHONY: deps-update
deps-update: ## Update all dependencies
	@go get -u ./...
	@go mod tidy
```

## File: `package.json`
```json
{
  "name": "bold-brew-website",
  "version": "1.0.0",
  "description": "Website for Bold Brew - A modern TUI for Homebrew",
  "scripts": {
    "build": "node build.js",
    "dev": "nodemon build.js"
  },
  "dependencies": {
    "ejs": "^3.1.10",
    "ejs-layouts": "^0.0.1",
    "front-matter": "^4.0.2",
    "marked": "^12.0.2"
  },
  "devDependencies": {
    "nodemon": "^3.1.0"
  }
}
```

## File: `README.md`
```markdown
<div align="center">
  <img src="brain/knowledge/docs_legacy/assets/logo/bbrew-logo-rounded.png" alt="Bold Brew Logo" width="200" height="200">
  <h1>Bold Brew (bbrew)</h1>
  <p>A modern Terminal UI for managing Homebrew packages and casks</p>
</div>

<div align="center">

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Valkyrie00/bold-brew)
![GitHub](https://img.shields.io/github/license/Valkyrie00/bold-brew)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Valkyrie00/bold-brew/release.yml)
![GolangCI-Lint](https://github.com/Valkyrie00/bold-brew/workflows/Quality/badge.svg)
![Security](https://github.com/Valkyrie00/bold-brew/workflows/Security/badge.svg)
![GitHub all releases](https://img.shields.io/github/downloads/Valkyrie00/bold-brew/total)

[![GitHub stars](https://img.shields.io/github/stars/Valkyrie00/bold-brew?style=social)](https://github.com/Valkyrie00/bold-brew/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Valkyrie00/bold-brew?style=social)](https://github.com/Valkyrie00/bold-brew/network/members)

[Website](https://bold-brew.com/) • [Changelog](https://github.com/Valkyrie00/bold-brew/releases)

</div>

---

<div align="center">

### 🌟 Official Homebrew TUI for Project Bluefin

Bold Brew is the **official Terminal UI** for managing Homebrew in [**Project Bluefin**](https://projectbluefin.io/) and [**Aurora**](https://getaurora.dev), next-generation Linux desktops that serve tens of thousands of users worldwide.

*"This application features full package management for homebrew in a nice nerdy interface"*  
— [Bluefin Documentation](https://docs.projectbluefin.io/command-line/)

[![Project Bluefin](https://img.shields.io/badge/Featured_in-Project_Bluefin-0091e2?style=for-the-badge&logo=linux)](https://projectbluefin.io/)
[![Aurora](https://img.shields.io/badge/Featured_in-Aurora-9b59b6?style=for-the-badge&logo=linux)](https://getaurora.dev)
[![Universal Blue](https://img.shields.io/badge/Part_of-Universal_Blue-5865f2?style=for-the-badge)](https://universal-blue.org/)

</div>

---

## ✨ Features

- 🚀 **Modern TUI Interface** - Clean and responsive terminal user interface
- 📦 **Complete Package Management** - Manage both Homebrew formulae and casks
- 📋 **Brewfile Mode** - Curated package collections from local or remote Brewfiles
- 🔍 **Advanced Search** - Fast fuzzy search across all packages
- 🎯 **Smart Filters** - Filter by installed, outdated, leaves, or casks
- 📊 **Analytics Integration** - See popular packages based on 90-day download stats
- 🔄 **Real-time Updates** - Live feedback during package operations
- ⌨️ **Keyboard Shortcuts** - Intuitive keybindings for all operations
- 🎨 **Type Indicators** - Visual distinction between formulae [F] and casks [C]
- 🗂️ **XDG Compliance** - Follows XDG Base Directory Specification for cache storage
- 🔒 **Security Scanning** - Automated vulnerability and security checks

## 🛠️ Installation

### Quick Install (Recommended)
Install Homebrew + Bold Brew with a single command:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/install.sh)"
```

### Via Homebrew
If you already have Homebrew installed:
```sh
brew install Valkyrie00/homebrew-bbrew/bbrew
```

### Manually
Download the latest version from the [releases page](https://github.com/Valkyrie00/bold-brew/releases)

## 📖 Quick Start

### Standard Mode
Launch the application to browse all Homebrew packages:
```sh
bbrew
```

### Brewfile Mode
Launch with a curated Brewfile to show only specific packages:
```sh
# Local Brewfile
bbrew -f /path/to/Brewfile

# Remote Brewfile (HTTPS)
bbrew -f https://raw.githubusercontent.com/user/repo/main/Brewfile
```

In Brewfile mode, you can:
- View only packages from the Brewfile
- Pick and choose what to install individually
- Use all standard features (search, filters, etc.)
- Load Brewfiles directly from URLs (great for sharing configurations!)

Perfect for creating themed collections like IDE choosers, dev tools, AI tools, K8s tools, etc.

See the `examples/` directory for ready-to-use Brewfiles.

### CLI Options

```sh
bbrew [options]

Options:
  -f <path|url>   Path or URL to Brewfile (local file or HTTPS URL)
  -v, --version   Show version information
  -h, --help      Show help message
```

### Keyboard Shortcuts

#### Navigation & Search
- `/` - Search packages
- `↑/↓` or `j/k` - Navigate package list
- `Enter` - View package details
- `Esc` - Clear search / Back to table
- `?` - Show help screen

#### Filters
- `f` - Filter installed packages
- `o` - Filter outdated packages
- `l` - Filter leaves (explicitly installed)
- `c` - Filter casks only

#### Package Operations
- `i` - Install selected package
- `u` - Update selected package
- `r` - Remove selected package
- `Ctrl+U` - Update all outdated packages

#### Brewfile Mode Only
- `Ctrl+A` - Install all packages from Brewfile
- `Ctrl+R` - Remove all packages from Brewfile

#### Other
- `q` - Quit application

## 🖼️ Screenshots

<div align="center">
  <img src="brain/knowledge/docs_legacy/assets/screenshots/bbrew-installed-screenshot.png" alt="Installed Packages Screenshot" width="800">
  <p><em>Filtered view showing installed packages</em></p>
  
  <img src="brain/knowledge/docs_legacy/assets/screenshots/bbrew-search-screenshot.png" alt="Search Screenshot" width="800">
  <p><em>Fuzzy search in action</em></p>
  
  <img src="brain/knowledge/docs_legacy/assets/screenshots/bbrew-brewfile-screenshot.png" alt="Brewfile Mode Screenshot" width="800">
  <p><em>Brewfile mode with curated package selection</em></p>
</div>

## 📊 Platform Support

| Platform | Support | Notes |
|----------|---------|-------|
| 🍎 **macOS** | ✅ Full | Native Homebrew support |
| 🐧 **Linux** | ✅ Full | Linuxbrew/Homebrew support |

## 🛡️ Security

Security is a priority for Bold Brew. We use:
- **govulncheck** - Go vulnerability database scanning
- **gosec** - Static security analysis
- **Automated CI/CD** - Security checks on every PR and push

Found a security issue? Please report it privately via [GitHub Security Advisories](https://github.com/Valkyrie00/bold-brew/security/advisories).

## 🔧 Development

### Prerequisites
- Go 1.25+
- Homebrew (for testing)
- Podman (optional, for containerized builds)

### Building from Source
```sh
# Clone the repository
git clone https://github.com/Valkyrie00/bold-brew.git
cd bold-brew

# Build locally
make build-local

# Run tests
make test

# Run linter
make quality-local

# Run security scans
make security
```

### Project Structure
```
bold-brew/
├── cmd/bbrew/           # Main application entry point
├── internal/
│   ├── models/          # Data models (Formula, Cask, Package)
│   ├── services/        # Business logic (Brew, App, Search, Input, Brewfile)
│   └── ui/              # TUI components and layout
├── .github/workflows/   # CI/CD pipelines
└── Makefile             # Build automation
```

## 🤝 Contributing

Contributions are welcome! Please:

1. 🍴 Fork the project
2. 🔨 Create your feature branch (`git checkout -b feat/amazing-feature`)
3. 📝 Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
4. 🧪 Run tests and linters (`make test quality-local`)
5. 🚀 Push to the branch (`git push origin feat/amazing-feature`)
6. 📬 Open a Pull Request

## 🦸Contributors
Bold Brew exists thanks to the efforts of these wonderful people

<a href="https://github.com/Valkyrie00/bold-brew/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Valkyrie00/bold-brew" />
</a>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💖 Support

- 🌟 [Star the project](https://github.com/Valkyrie00/bold-brew)
- 🐛 [Report a bug](https://github.com/Valkyrie00/bold-brew/issues/new?labels=bug)
- 💡 [Request a feature](https://github.com/Valkyrie00/bold-brew/issues/new?labels=enhancement)
- 📣 Share the project with your friends

---

<div align="center">
  <sub>Built with ❤️ for the community and for all developers</sub>
</div>
```

## File: `cmd/bbrew/main.go`
```go
package main

import (
	"bbrew/internal/services"
	"flag"
	"fmt"
	"log"
	"os"
)

func main() {
	// Define flags
	brewfilePath := flag.String("f", "", "Path to Brewfile (show only packages from this Brewfile)")
	showVersion := flag.Bool("v", false, "Show version information")
	flag.Bool("version", false, "Show version information")

	// Custom usage message
	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Bold Brew - A TUI for Homebrew package management\n\n")
		fmt.Fprintf(os.Stderr, "Usage: bbrew [options]\n\n")
		fmt.Fprintf(os.Stderr, "Options:\n")
		fmt.Fprintf(os.Stderr, "  -f <path|url> Path or URL to Brewfile\n")
		fmt.Fprintf(os.Stderr, "  -v, --version Show version information\n")
		fmt.Fprintf(os.Stderr, "  -h, --help    Show this help message\n")
		fmt.Fprintf(os.Stderr, "\nExamples:\n")
		fmt.Fprintf(os.Stderr, "  bbrew                    Launch the TUI with all packages\n")
		fmt.Fprintf(os.Stderr, "  bbrew -f ~/Brewfile      Launch with packages from local Brewfile\n")
		fmt.Fprintf(os.Stderr, "  bbrew -f https://...     Launch with packages from remote Brewfile\n")
	}

	flag.Parse()

	// Handle --version flag (check both -v and --version)
	if *showVersion || isFlagPassed("version") {
		fmt.Printf("Bold Brew %s\n", services.AppVersion)
		os.Exit(0)
	}

	// Resolve Brewfile path (handles both local and remote URLs)
	var cleanup func()
	if *brewfilePath != "" {
		localPath, cleanupFn, err := services.ResolveBrewfilePath(*brewfilePath)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}
		*brewfilePath = localPath
		cleanup = cleanupFn
		defer cleanup()
	}

	// Initialize app service
	appService := services.NewAppService()
	// Configure Brewfile mode if path was provided
	if *brewfilePath != "" {
		appService.SetBrewfilePath(*brewfilePath)
	}

	// Boot the application (load Homebrew data)
	if err := appService.Boot(); err != nil {
		log.Fatalf("Failed to initialize: %v", err)
	}

	// Build and run the TUI
	appService.BuildApp()
	if err := appService.GetApp().Run(); err != nil {
		log.Fatalf("Application error: %v", err)
	}
}

// isFlagPassed checks if a flag was explicitly passed on the command line.
func isFlagPassed(name string) bool {
	found := false
	flag.Visit(func(f *flag.Flag) {
		if f.Name == name {
			found = true
		}
	})
	return found
}
```

## File: `brain/knowledge/docs_legacy/CNAME`
```
bold-brew.com
```

## File: `brain/knowledge/docs_legacy/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bold Brew (bbrew) - Modern Homebrew TUI Manager for macOS and Linux</title>
    <meta name="description" content="Bold Brew (bbrew) is the modern Terminal User Interface for Homebrew on macOS and Linux. Install, update, and manage packages and casks with an elegant TUI.">
    <meta name="keywords" content="bbrew, Bold Brew, Homebrew TUI, macOS package manager, Linux package manager, Homebrew casks, Homebrew GUI, terminal package manager, Homebrew alternative, Project Bluefin, macOS development tools, Linux development tools">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Bold Brew (bbrew) - Modern Homebrew TUI Manager for macOS and Linux">
    <meta property="og:description" content="Bold Brew (bbrew) is the modern Terminal User Interface for Homebrew on macOS and Linux. Install, update, and manage packages and casks with an elegant TUI.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Bold Brew (bbrew) - Modern Homebrew TUI Manager for macOS and Linux">
    <meta name="twitter:description" content="Bold Brew (bbrew) is the modern Terminal User Interface for Homebrew on macOS and Linux. Install, update, and manage packages and casks with an elegant TUI.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main>
    <section class="hero-section" aria-label="Hero">
        <div class="hero-bg-overlay"></div>
        <div class="container">
            <div class="hero-content">
                <img src="assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" class="logo-img animate-pulse" width="120" height="120">
                <h1 class="display-4">Bold Brew</h1>
                <h2 class="tagline"><code>bbrew</code></h2>
                <p class="lead">The modern Terminal UI for managing Homebrew packages and casks on macOS and Linux.</p>
                <div class="badges">
                    <img src="https://img.shields.io/github/v/release/Valkyrie00/bold-brew" alt="Version" width="100" height="20">
                    <img src="https://img.shields.io/github/license/Valkyrie00/bold-brew" alt="License" width="100" height="20">
                    <img src="https://img.shields.io/github/actions/workflow/status/Valkyrie00/bold-brew/release.yml" alt="Build Status" width="100" height="20">
                    <img src="https://github.com/Valkyrie00/bold-brew/workflows/Security/badge.svg" alt="Security" width="100" height="20">
                    <img src="https://img.shields.io/github/downloads/Valkyrie00/bold-brew/total" alt="Downloads" width="100" height="20">
                    <img src="https://img.shields.io/badge/Featured_in-Project_Bluefin-0091e2" alt="Project Bluefin" width="140" height="20">
                </div>
                <div class="hero-cta">
                    <a href="#install" class="btn-primary">Start Now</a>
                    <a href="https://github.com/Valkyrie00/bold-brew" class="btn-secondary" target="_blank">View on GitHub</a>
                </div>
            </div>
        </div>
    </section>

    <section class="install-section" id="install" aria-label="Installation">
        <div class="container">
            <h2>Installation</h2>
            <p class="lead text-center mb-4">Get started with Bold Brew in just one command</p>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="install-card">
                        <div class="install-step">
                            <div class="step-header">
                                <div class="step-number">⚡</div>
                                <h3>Quick Install</h3>
                            </div>
                            <div class="code-block">
                                <pre><code><span class="prompt">></span> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/install.sh)"</code></pre>
                                <button class="copy-btn" onclick="copyToClipboard(this)" aria-label="Copy command">
                                    <span class="copy-icon">⧉</span>
                                    <span class="copy-text">Copy</span>
                                </button>
                            </div>
                            <p class="install-note"><i>This installs Homebrew (if needed) + Bold Brew in one step</i></p>
                        </div>

                        <div class="install-step">
                            <div class="step-header">
                                <div class="step-number">▶</div>
                                <h3>Run Bold Brew</h3>
                            </div>
                            <div class="code-block">
                                <pre><code><span class="prompt">></span> bbrew</code></pre>
                                <button class="copy-btn" onclick="copyToClipboard(this)" aria-label="Copy command">
                                    <span class="copy-icon">⧉</span>
                                    <span class="copy-text">Copy</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="alternative-install">
                        <div class="divider">
                            <span>OR</span>
                        </div>
                        <p class="text-center">Already have Homebrew? Install directly:</p>
                        <div class="code-block" style="max-width: 500px; margin: 0 auto 1rem;">
                            <pre><code><span class="prompt">></span> brew install Valkyrie00/homebrew-bbrew/bbrew</code></pre>
                            <button class="copy-btn" onclick="copyToClipboard(this)" aria-label="Copy command">
                                <span class="copy-icon">⧉</span>
                                <span class="copy-text">Copy</span>
                            </button>
                        </div>
                        <p class="text-center" style="margin-top: 1rem;">Or download from GitHub</p>
                        <div class="text-center">
                            <a class="btn-download" href="https://github.com/Valkyrie00/bold-brew/releases" target="_blank" rel="noopener noreferrer">
                                <span class="download-icon">↓</span>
                                Download Latest Release
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="screenshots-section" aria-label="Screenshots">
        <div class="container">
            <h2>Screenshots</h2>
            <p class="lead text-center mb-4">Explore the Bold Brew interface and its features</p>

            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <figure class="screenshot-card">
                        <img src="assets/screenshots/bbrew-brewfile-screenshot.png" alt="Brewfile Mode showing package management interface" class="img-fluid" loading="lazy" width="400" height="300">
                        <figcaption class="screenshot-caption">
                            <p>Main Dashboard</p>
                        </figcaption>
                    </figure>
                </div>
                <div class="col-md-4 mb-4">
                    <figure class="screenshot-card">
                        <img src="assets/screenshots/bbrew-installed-screenshot.png" alt="Installed packages management view" class="img-fluid" loading="lazy" width="400" height="300">
                        <figcaption class="screenshot-caption">
                            <p>Handle Installed Packages</p>
                        </figcaption>
                    </figure>
                </div>
                <div class="col-md-4 mb-4">
                    <figure class="screenshot-card">
                        <img src="assets/screenshots/bbrew-search-screenshot.png" alt="Package search interface" class="img-fluid" loading="lazy" width="400" height="300">
                        <figcaption class="screenshot-caption">
                            <p>Search for Packages</p>
                        </figcaption>
                    </figure>
                </div>
            </div>
        </div>
    </section>

    <section class="bluefin-banner" style="background: linear-gradient(135deg, #0091e2 0%, #5865f2 100%); color: white; padding: 3rem 0; margin: 2rem 0;">
        <div class="container text-center">
            <h2 style="color: white; margin-bottom: 1rem;">🌟 Official Homebrew TUI for Project Bluefin</h2>
            <p class="lead" style="color: rgba(255,255,255,0.95); margin-bottom: 1.5rem;">
                Bold Brew is the official Terminal UI for managing Homebrew in <strong>Project Bluefin</strong>, 
                a next-generation Linux desktop serving tens of thousands of users worldwide.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="https://projectbluefin.io/" target="_blank" class="btn" style="background: white; color: #0091e2; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600;">
                    Learn About Bluefin →
                </a>
                <a href="blog/bold-brew-official-project-bluefin-tui.html" class="btn" style="background: rgba(255,255,255,0.2); color: white; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; border: 2px solid white;">
                    Read Announcement →
                </a>
            </div>
        </div>
    </section>

    <section id="features" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">Features</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-cube"></i>
                        <h3>Formulae & Casks</h3>
                        <p>Manage both CLI tools and GUI applications. Full support for Homebrew formulae and casks in one interface.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-filter"></i>
                        <h3>Smart Filters</h3>
                        <p>Filter by installed, outdated, leaves (explicitly installed), or casks. Find what you need instantly.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-search"></i>
                        <h3>Fuzzy Search</h3>
                        <p>Fast fuzzy search across all packages with real-time results and analytics integration.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-rocket"></i>
                        <h3>Real-time Updates</h3>
                        <p>Live feedback during installations, updates, and removals with detailed progress information.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-shield-alt"></i>
                        <h3>Secure & Compliant</h3>
                        <p>XDG Base Directory compliant with automated security scanning and vulnerability checks.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-keyboard"></i>
                        <h3>Keyboard Shortcuts</h3>
                        <p>Intuitive keybindings for all operations. Navigate and manage packages without touching the mouse.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-file-alt"></i>
                        <h3>Brewfile Mode</h3>
                        <p>Load curated package collections from local or remote Brewfiles. Perfect for team configs and themed installers.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-link"></i>
                        <h3>Remote Brewfiles</h3>
                        <p>Load Brewfiles directly from HTTPS URLs. Share configurations via GitHub, team repos, or any web server.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="latest-posts" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">Latest Articles</h2>
            <div class="row">
                
                    <div class="col-md-4">
                        <div class="blog-card">
                            <div class="post-meta">
                                <span class="date">2025-12-29</span>
                            </div>
                            <h3><a href="/blog/brewfile-mode-remote-support.html">Brewfile Mode: Curated Package Collections &amp; Remote URL Support</a></h3>
                            <p>Bold Brew now supports Brewfile mode for curated package collections, plus the ability to load Brewfiles directly from HTTPS URLs. Perfect for team configurations and themed installers.</p>
                            <a href="/blog/brewfile-mode-remote-support.html" class="read-more">Read more →</a>
                        </div>
                    </div>
                
                    <div class="col-md-4">
                        <div class="blog-card">
                            <div class="post-meta">
                                <span class="date">2025-10-13</span>
                            </div>
                            <h3><a href="/blog/bold-brew-2-0-cask-support.html">Bold Brew 2.0: Complete Homebrew Management with Cask Support</a></h3>
                            <p>Bold Brew 2.0 brings major new features including full Cask support, Leaves filter, XDG compliance, and enhanced security. Manage both CLI tools and GUI applications seamlessly.</p>
                            <a href="/blog/bold-brew-2-0-cask-support.html" class="read-more">Read more →</a>
                        </div>
                    </div>
                
                    <div class="col-md-4">
                        <div class="blog-card">
                            <div class="post-meta">
                                <span class="date">2025-10-13</span>
                            </div>
                            <h3><a href="/blog/bold-brew-official-project-bluefin-tui.html">Bold Brew Named Official Homebrew TUI for Project Bluefin</a></h3>
                            <p>Bold Brew becomes the official Terminal UI for managing Homebrew in Project Bluefin, a next-generation Linux desktop serving tens of thousands of users worldwide.</p>
                            <a href="/blog/bold-brew-official-project-bluefin-tui.html" class="read-more">Read more →</a>
                        </div>
                    </div>
                
            </div>
            <div class="text-center mt-4">
                <a href="blog/" class="btn btn-primary">View All Articles</a>
            </div>
        </div>
    </section>

    <section class="seo-content" aria-label="Additional Information">
        <div class="container">
            <h2>Manage Homebrew Packages and Casks with Bold Brew</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <p><strong>Bold Brew</strong> transforms the way developers manage <strong>Homebrew packages and casks</strong> across macOS and Linux with its elegant Terminal User Interface. Stop struggling with complex command-line syntax and enjoy a streamlined package management experience for both CLI tools and GUI applications.</p>

                    <h3>Why Developers Choose Bold Brew</h3>
                    <p>Managing your <strong>Homebrew ecosystem</strong> has never been easier. Bold Brew 2.0 provides complete support for both formulae (command-line tools) and casks (GUI applications), with real-time visual feedback for installations, updates, and package removals—all while maintaining the speed and efficiency you expect from terminal-based applications.</p>

                    <h3>Key Benefits for Developers</h3>
                    <ul>
                        <li><strong>Complete package management</strong> for both CLI tools and GUI applications</li>
                        <li><strong>Brewfile Mode</strong> for curated package collections from local or remote URLs</li>
                        <li><strong>Smart filtering</strong> by installed, outdated, leaves, or casks</li>
                        <li><strong>Faster package discovery</strong> with fuzzy search and analytics</li>
                        <li><strong>XDG Base Directory compliance</strong> for clean cache management</li>
                        <li><strong>Streamlined updates</strong> for all Homebrew packages with visual progress</li>
                        <li><strong>Keyboard-driven workflow</strong> without memorizing complex commands</li>
                    </ul>

                    <p>Trusted by <strong>Project Bluefin</strong> and used by <strong>tens of thousands of developers</strong>, Bold Brew integrates perfectly with your workflow while reducing cognitive load and increasing productivity on macOS and Linux.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="about-section" id="about" aria-label="About">
        <div class="container">
            <h2>About Bold Brew</h2>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <p class="lead">The modern Homebrew TUI that developers trust—from macOS to Linux</p>

                    <h3>The Bold Brew Advantage</h3>
                    <p>Bold Brew was designed from the ground up to address the limitations of traditional Homebrew management. By providing a Terminal User Interface (TUI), Bold Brew combines the efficiency of command-line operations with intuitive visual feedback. Version 2.0 brings complete support for both formulae (CLI tools) and casks (GUI applications).</p>

                    <h3>Complete Homebrew Integration</h3>
                    <p>As the official Homebrew TUI for Project Bluefin, Bold Brew seamlessly integrates with your existing Homebrew installation. All operations—from searching packages to managing casks, filtering leaves, and updating dependencies—are visualized through an elegant interface while preserving the speed and reliability of Homebrew's core functionality.</p>

                    <div class="compatibility-info">
                        <h4>Platform Support</h4>
                        <ul>
                            <li><strong>macOS:</strong> Full support (10.15 Catalina or newer)</li>
                            <li><strong>Linux:</strong> Full support (Project Bluefin, Linuxbrew, Homebrew on Linux)</li>
                            <li>Requires: Homebrew installation, Terminal with true color support</li>
                        </ul>
                    </div>

                    <h3>Trusted by the Community</h3>
                    <p>Bold Brew is pre-installed in Project Bluefin, serving tens of thousands of developers worldwide. Whether you're a seasoned developer or new to package management, Bold Brew streamlines your workflow and makes Homebrew more accessible than ever before.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="faq-section" aria-label="FAQ">
        <div class="container">
            <h2>FAQ</h2>
            <p class="lead text-center mb-5">Frequently asked questions about Bold Brew</p>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="accordion faq-accordion" id="faqAccordion">
                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq1">
                                <h3>What is Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq1" class="faq-answer collapse show" data-bs-parent="#faqAccordion">
                                <p>Bold Brew (bbrew) is a modern Terminal User Interface for managing Homebrew packages and casks on macOS and Linux. It provides an elegant and intuitive way to install, update, and manage both command-line tools (formulae) and GUI applications (casks) without memorizing complex commands. It's the official Homebrew TUI for Project Bluefin.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq2">
                                <h3>How do I install Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq2" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>You can install Bold Brew in two ways:</p>
                                <ol>
                                    <li>Using Homebrew: <code>brew install Valkyrie00/homebrew-bbrew/bbrew</code></li>
                                    <li>Downloading the latest release from our GitHub repository</li>
                                </ol>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq3">
                                <h3>How do I update Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq3" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Run <code>brew upgrade bbrew</code> to update the application to the latest version.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq4">
                                <h3>How do I remove Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq4" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Use <code>brew remove bbrew</code> if you need to uninstall it from your system.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq5">
                                <h3>Does it work on Linux or Windows?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq5" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Yes! Bold Brew has full support for Linux (it's the official TUI for Project Bluefin). It works anywhere Homebrew is installed.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq7">
                                <h3>What's new in Bold Brew 2.0?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq7" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Version 2.0 introduces full Homebrew Casks support (GUI applications), a Leaves filter (explicitly installed packages), XDG Base Directory compliance, enhanced security scanning, and many performance improvements. <a href="blog/bold-brew-2-0-cask-support.html">Read the full announcement</a>.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq8">
                                <h3>What is Brewfile Mode?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq8" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Brewfile Mode lets you launch Bold Brew with a curated list of packages instead of the full catalog. Use <code>bbrew -f /path/to/Brewfile</code> for local files or <code>bbrew -f https://...</code> for remote URLs. Perfect for team configurations, themed installers, and project-specific setups. <a href="blog/brewfile-mode-remote-support.html">Learn more</a>.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq6">
                                <h3>Where can I report issues or request features?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq6" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Feel free to open an issue on our <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub repository</a>.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/manifest.json`
```json
{
    "name": "Bold Brew",
    "short_name": "bbrew",
    "description": "Modern Homebrew TUI Manager for macOS and Linux",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#1a1a1a",
    "theme_color": "#1a1a1a",
    "orientation": "portrait",
    "icons": [
        {
            "src": "assets/ico/bbrew-16.ico",
            "sizes": "16x16",
            "type": "image/x-icon"
        },
        {
            "src": "assets/ico/bbrew-24.ico",
            "sizes": "24x24",
            "type": "image/x-icon"
        },
        {
            "src": "assets/ico/bbrew-32.ico",
            "sizes": "32x32",
            "type": "image/x-icon"
        },
        {
            "src": "assets/ico/bbrew-48.ico",
            "sizes": "48x48",
            "type": "image/x-icon"
        }
    ],
    "categories": ["developer tools", "utilities"],
    "screenshots": [
        {
            "src": "assets/screenshots/bbrew-brewfile-screenshot.png",
            "sizes": "400x300",
            "type": "image/png",
            "platform": "macOS",
            "label": "Main Dashboard"
        },
        {
            "src": "assets/screenshots/bbrew-installed-screenshot.png",
            "sizes": "400x300",
            "type": "image/png",
            "platform": "macOS",
            "label": "Installed Packages"
        },
        {
            "src": "assets/screenshots/bbrew-search-screenshot.png",
            "sizes": "400x300",
            "type": "image/png",
            "platform": "macOS",
            "label": "Package Search"
        }
    ]
} 
```

## File: `brain/knowledge/docs_legacy/robots.txt`
```
User-agent: *
Allow: /
Allow: /assets/
Allow: /screenshots/
Allow: /sitemap.xml

Disallow: /admin/
Disallow: /private/
Disallow: /tmp/

Sitemap: https://bold-brew.com/sitemap.xml
```

## File: `brain/knowledge/docs_legacy/sitemap.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://bold-brew.com/</loc>
    <lastmod>2025-12-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/</loc>
    <lastmod>2025-12-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/brewfile-mode-remote-support.html</loc>
    <lastmod>2025-12-29</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/bold-brew-2-0-cask-support.html</loc>
    <lastmod>2025-10-13</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/bold-brew-official-project-bluefin-tui.html</loc>
    <lastmod>2025-10-13</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/top-homebrew-packages-for-developers.html</loc>
    <lastmod>2025-04-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/essential-homebrew-commands.html</loc>
    <lastmod>2025-03-29</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/install-homebrew-macos.html</loc>
    <lastmod>2025-03-29</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://bold-brew.com/blog/managing-homebrew-packages.html</loc>
    <lastmod>2025-03-29</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

## File: `brain/knowledge/docs_legacy/assets/css/styles.css`
```css
@import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

body {
    font-family: "Atkinson Hyperlegible", serif;
    background-color: #0A1622;
    color: #e0e0e0;
}

a {
    color: #4EA1FF;
    text-decoration: none;
    transition: color 0.3s ease;
}

a:hover {
    color: #90B8E3;
}

footer {
    background: linear-gradient(180deg, #0A1622, #0D1D2D);
    padding: 2rem 0;
    text-align: center;
}

footer p {
    color: #496480;
}

footer a {
    color: #496480;
    text-decoration: none;
    transition: color 0.3s ease;
}

footer a:hover {
    color: #4EA1FF;
}

/** Hero Section */
.hero-section {
    min-height: 100vh;
    padding: 2rem 0;
    background: radial-gradient(ellipse at top, #0D1D2D, #0A1622);
    border-bottom: 1px solid #1E3449;
    text-align: center;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-bg-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    /*background: url('assets/grid-pattern.png') repeat;*/
    opacity: 0.05;
    z-index: 0;
}

.hero-content {
    position: relative;
    z-index: 1;
    width: 100%;
}

.hero-section .logo-img {
    width: 200px;
    height: 200px;
    margin-bottom: 1.5rem;
    filter: drop-shadow(0 0 20px rgba(78, 161, 255, 0.3));
    transition: transform 0.5s ease;
}

.hero-section .logo-img:hover {
    transform: scale(1.05);
}

.animate-pulse {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { filter: drop-shadow(0 0 15px rgba(78, 161, 255, 0.2)); }
    50% { filter: drop-shadow(0 0 25px rgba(78, 161, 255, 0.5)); }
    100% { filter: drop-shadow(0 0 15px rgba(78, 161, 255, 0.2)); }
}

.hero-section .display-4 {
    color: #4EA1FF;
    font-weight: bold;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 10px rgba(78, 161, 255, 0.2);
}

.hero-section .tagline {
    color: #90B8E3;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.hero-section .lead {
    color: #90B8E3;
    margin-bottom: 2rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.6;
}

.hero-section .badges {
    margin-bottom: 2.5rem;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.hero-section .badges img {
    margin: 0 0.2rem;
    filter: brightness(1.1);
    transition: transform 0.3s ease;
}

.hero-section .badges img:hover {
    transform: translateY(-2px);
}

.hero-cta {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1rem;
}

.btn-primary, .btn-secondary {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    border-radius: 6px;
    font-weight: bold;
    transition: all 0.3s ease;
    text-decoration: none;
}

.btn-primary {
    background: linear-gradient(135deg, #4EA1FF, #3D7FCC);
    color: white;
    border: none;
    box-shadow: 0 4px 12px rgba(78, 161, 255, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(78, 161, 255, 0.4);
    color: white;
}

.btn-secondary {
    background: transparent;
    border: 2px solid #4EA1FF;
    color: #4EA1FF;
}

.btn-secondary:hover {
    background-color: rgba(78, 161, 255, 0.1);
    transform: translateY(-2px);
    color: #4EA1FF;
}

@media (max-width: 768px) {
    .hero-section {
        padding: 4rem 0;
    }

    .hero-section .logo-img {
        width: 150px;
        height: 150px;
    }

    .hero-cta {
        flex-direction: column;
        gap: 0.75rem;
    }
}

/* Install section */
.install-section {
    background: linear-gradient(180deg, #0D1D2D, #0A1622);
    padding: 5rem 0;
    text-align: center;
}

.install-section h2 {
    color: #4EA1FF;
    margin-bottom: 1rem;
}

.install-section .lead {
    color: #90B8E3;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.install-card {
    background-color: #15202B;
    border-radius: 10px;
    border: 1px solid #1E3449;
    padding: 2rem;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    margin-bottom: 2.5rem;
}

.install-step {
    position: relative;
    padding-bottom: 2rem;
    text-align: left;
}

.install-step:last-child {
    padding-bottom: 0;
}

.step-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
}

.step-number {
    background: linear-gradient(135deg, #4EA1FF, #3D7FCC);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    box-shadow: 0 3px 10px rgba(78, 161, 255, 0.3);
    flex-shrink: 0;
}

.install-step h5 {
    color: #4EA1FF;
    margin: 0;
}

.code-block {
    position: relative;
    margin: 1.5rem 0;
    border-radius: 8px;
    overflow: hidden;
}

.code-block .prompt {
    color: #4EA1FF;
    margin-right: 8px;
    font-weight: bold;
    user-select: none;
}

.code-block pre {
    background-color: #0A1622;
    border: 1px solid #1E3449;
    border-radius: 8px;
    padding: 1rem;
    margin: 0;
    color: #90B8E3;
    text-align: left;
    overflow-x: auto;
}

.code-block code {
    color: #90B8E3;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
}

.copy-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    background-color: rgba(14, 30, 46, 0.7);
    color: #4EA1FF;
    border: 1px solid #1E3449;
    border-radius: 4px;
    padding: 5px 10px;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: all 0.2s ease;
    opacity: 0;
}

.code-block:hover .copy-btn {
    opacity: 1;
}

.copy-btn:hover {
    background-color: rgba(78, 161, 255, 0.1);
}

.copy-icon {
    margin-right: 5px;
}

.install-note {
    color: #496480;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

.alternative-install {
    margin-top: 3rem;
}

.divider {
    display: flex;
    align-items: center;
    text-align: center;
    margin-bottom: 1.5rem;
}

.divider::before,
.divider::after {
    content: "";
    flex: 1;
    border-bottom: 1px solid #1E3449;
}

.divider span {
    padding: 0 1rem;
    color: #496480;
    font-size: 0.9rem;
    font-weight: bold;
}

.btn-download {
    display: inline-flex;
    align-items: center;
    background: linear-gradient(135deg, #4EA1FF, #3D7FCC);
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 6px;
    font-weight: bold;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(78, 161, 255, 0.3);
    margin-top: 1rem;
}

.btn-download:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(78, 161, 255, 0.4);
    color: white;
}

.download-icon {
    margin-right: 8px;
    font-size: 1.2rem;
}

@media (max-width: 768px) {
    .install-section {
        padding: 3rem 0;
    }

    .install-card {
        padding: 1.5rem;
    }
}

/* Screenshots Section */
.screenshots-section {
    background: linear-gradient(180deg, #0A1622, #0D1D2D);
    padding: 4rem 0;
    text-align: center;
}

.screenshots-section h2 {
    color: #4EA1FF;
    margin-bottom: 1rem;
}

.screenshots-section .lead {
    color: #90B8E3;
    margin-bottom: 2rem;
}

.screenshot-card {
    background-color: #15202B;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #1E3449;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}

.screenshot-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.screenshot-card img {
    border-radius: 8px 8px 0 0;
    border-bottom: 1px solid #1E3449;
    width: 100%;
}

.screenshot-caption {
    padding: 0.75rem 1rem;
}

.screenshot-caption p {
    color: #4EA1FF;
    font-weight: bold;
    margin: 0;
}

@media (max-width: 768px) {
    .screenshots-section {
        padding: 2rem 0;
    }
}

/* Features section */
.features-section {
    background: linear-gradient(180deg, #0A1622, #0D1D2D);
    padding: 5rem 0;
    text-align: center;
}

.features-section h2 {
    color: #4EA1FF;
    margin-bottom: 1rem;
}

.features-section .lead {
    color: #90B8E3;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.feature-card {
    background-color: #15202B;
    border: 1px solid #1E3449;
    border-radius: 10px;
    padding: 2rem 1.5rem;
    height: 100%;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    z-index: 1;
}

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
    border-color: #4EA1FF;
}

.feature-card:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #4EA1FF, #3D7FCC);
    transform: scaleX(0);
    transition: transform 0.3s ease;
    z-index: 2;
}

.feature-card:hover:before {
    transform: scaleX(1);
}

.feature-icon {
    margin-bottom: 1.5rem;
}

.feature-icon .icon {
    font-size: 2.5rem;
    background: linear-gradient(135deg, #4EA1FF, #3D7FCC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    filter: drop-shadow(0 0 15px rgba(78, 161, 255, 0.2));
}

.feature-card h3 {
    color: #4EA1FF;
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.feature-card p {
    color: #90B8E3;
    font-size: 0.95rem;
    margin-bottom: 0;
}

.feature-summary {
    background-color: rgba(14, 30, 46, 0.5);
    border: 1px solid #1E3449;
    border-radius: 10px;
    padding: 1.5rem;
    margin-top: 2rem;
}

.feature-summary p {
    color: #90B8E3;
    margin-bottom: 0;
}

@media (max-width: 992px) {
    .features-section {
        padding: 4rem 0;
    }
}

@media (max-width: 768px) {
    .features-section {
        padding: 3rem 0;
    }

    .feature-card {
        padding: 1.5rem;
    }
}

/* SEO Content Section */
.seo-content {
    background: linear-gradient(180deg, #0D1D2D, #0A1622);
    padding: 5rem 0;
}

.seo-content h2 {
    color: #4EA1FF;
    margin-bottom: 2rem;
    text-align: center;
}

.seo-content h3 {
    color: #4EA1FF;
    font-size: 1.35rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.seo-content p {
    color: #90B8E3;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.seo-content ul {
    color: #90B8E3;
    padding-left: 1.2rem;
    margin-bottom: 1.5rem;
}

.seo-content ul li {
    margin-bottom: 0.75rem;
    line-height: 1.5;
}

.seo-content strong {
    color: #4EA1FF;
    font-weight: 600;
}

/* About Section */
.about-section {
    background: linear-gradient(180deg, #0A1622, #0D1D2D);
    padding: 5rem 0;
}

.about-section h2 {
    color: #4EA1FF;
    margin-bottom: 1rem;
    text-align: center;
}

.about-section .lead {
    color: #90B8E3;
    text-align: center;
    margin-bottom: 2.5rem;
    font-style: italic;
}

.about-section h3 {
    color: #4EA1FF;
    font-size: 1.35rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.about-section p {
    color: #90B8E3;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.compatibility-info {
    background-color: #15202B;
    border: 1px solid #1E3449;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.compatibility-info h4 {
    color: #4EA1FF;
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

.compatibility-info ul {
    color: #90B8E3;
    padding-left: 1.2rem;
    margin-bottom: 0;
}

.compatibility-info ul li {
    margin-bottom: 0.5rem;
    line-height: 1.5;
}

@media (max-width: 768px) {
    .seo-content, .about-section {
        padding: 3rem 0;
    }

    .seo-content h2, .about-section h2 {
        font-size: 1.75rem;
    }

    .seo-content h3, .about-section h3 {
        font-size: 1.25rem;
    }
}

/* FAQ Section */
.faq-section {
    background: linear-gradient(180deg, #0D1D2D, #0A1622);
    padding: 5rem 0;
    text-align: center;
}

.faq-section h2 {
    color: #4EA1FF;
    margin-bottom: 1rem;
}

.faq-section .lead {
    color: #90B8E3;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.faq-accordion {
    text-align: left;
}

.faq-item {
    background-color: #15202B;
    border: 1px solid #1E3449;
    border-radius: 10px;
    margin-bottom: 1rem;
    overflow: hidden;
    transition: all 0.3s ease;
}

.faq-item:hover {
    border-color: #4EA1FF;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.faq-question {
    padding: 1.25rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
}

.faq-question h5 {
    color: #4EA1FF;
    margin: 0;
    font-weight: 600;
}

.faq-icon {
    color: #4EA1FF;
    font-size: 1.5rem;
    line-height: 1;
    font-weight: 300;
    width: 24px;
    height: 24px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.faq-icon .plus,
.faq-icon .minus {
    position: absolute;
    transition: all 0.3s ease;
}

.faq-icon .minus {
    opacity: 0;
}

.faq-question[aria-expanded="true"] .faq-icon .plus {
    opacity: 0;
}

.faq-question[aria-expanded="true"] .faq-icon .minus {
    opacity: 1;
}

.faq-answer {
    border-top: 1px solid #1E3449;
    padding: 0;
}

.faq-answer p {
    padding: 1.25rem;
    margin: 0;
    color: #90B8E3;
}

.faq-answer code {
    background-color: #0A1622;
    color: #4EA1FF;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 0.9em;
}

.link-accent {
    color: #4EA1FF;
    text-decoration: none;
    transition: all 0.2s ease;
}

.link-accent:hover {
    color: #90B8E3;
    text-decoration: underline;
}

@media (max-width: 768px) {
    .faq-section {
        padding: 3rem 0;
    }

    .faq-question h5 {
        font-size: 1.05rem;
    }
}

/* Blog Styles */
.blog-posts {
    margin-bottom: 3rem;
    position: relative;
}

.blog-posts::after {
    content: '';
    position: absolute;
    right: -2rem;
    top: 0;
    bottom: 0;
    width: 1px;
    background: linear-gradient(to bottom, transparent, #1E3449, transparent);
}

.blog-post {
    padding: 2rem;
    background: #15202B;
    border: 1px solid #1E3449;
    border-radius: 8px;
    transition: all 0.3s ease;
    margin-bottom: 2rem;
    position: relative;
}

.blog-post:last-child {
    margin-bottom: 0;
}

.blog-post:hover {
    transform: translateY(-2px);
    border-color: #4EA1FF;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.blog-post::after {
    content: '';
    position: absolute;
    bottom: -1rem;
    left: 2rem;
    right: 2rem;
    height: 1px;
    background: linear-gradient(to right, transparent, #1E3449, transparent);
}

.blog-post:last-child::after {
    display: none;
}

.post-meta {
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin-bottom: 1rem;
}

.post-meta .date,
.post-meta .author {
    margin-right: 1rem;
}

.blog-post h2 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
}

.blog-post h2 a {
    color: var(--text-primary);
    text-decoration: none;
    transition: color 0.2s ease;
}

.blog-post h2 a:hover {
    color: var(--accent-color);
}

.excerpt {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.tag {
    background: var(--bg-primary);
    color: var(--text-secondary);
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.9rem;
    text-decoration: none;
    transition: all 0.2s ease;
}

.tag:hover {
    background: var(--accent-color);
    color: var(--text-primary);
}

.read-more {
    color: var(--accent-color);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
}

.read-more:hover {
    color: var(--accent-hover);
}

/* Sidebar Styles */
.sidebar {
    position: sticky;
    top: 2rem;
    padding-left: 2rem;
}

.widget {
    background: #15202B;
    border: 1px solid #1E3449;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    transition: all 0.3s ease;
}

.widget:hover {
    border-color: #4EA1FF;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.widget:last-child {
    margin-bottom: 0;
}

.widget h3 {
    font-size: 1.4rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.social-links {
    display: flex;
    gap: 1rem;
}

.social-links a {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.2s ease;
}

.social-links a:hover {
    color: var(--accent-color);
}

/* Responsive Adjustments */
@media (max-width: 992px) {
    .blog-posts::after {
        display: none;
    }
    
    .sidebar {
        padding-left: 0;
    }
}

@media (max-width: 768px) {
    article header h1 {
        font-size: 2rem;
    }
    
    article .content {
        font-size: 1rem;
    }
    
    article .content h2 {
        font-size: 1.6rem;
    }
    
    article .content h3 {
        font-size: 1.3rem;
    }
}

/* Article Page Improvements */
article {
    max-width: 800px;
    margin: 0 auto;
}

article header {
    margin-bottom: 3rem;
    text-align: center;
}

article header h1 {
    color: #4EA1FF;
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

article .meta {
    color: #90B8E3;
    font-size: 0.9rem;
}

article .meta span {
    margin: 0 0.5rem;
}

article .content {
    font-size: 1.1rem;
    line-height: 1.8;
}

article .content h2 {
    color: #4EA1FF;
    margin: 2.5rem 0 1.5rem;
    font-size: 1.8rem;
}

article .content h3 {
    color: #4EA1FF;
    margin: 2rem 0 1rem;
    font-size: 1.4rem;
}

article .content p {
    margin-bottom: 1.5rem;
    color: #e0e0e0;
}

article .content ul, 
article .content ol {
    margin-bottom: 1.5rem;
    padding-left: 1.5rem;
}

article .content li {
    margin-bottom: 0.5rem;
}

article .content pre {
    background: #0A1622;
    border: 1px solid #1E3449;
    border-radius: 8px;
    padding: 1rem;
    margin: 1.5rem 0;
    overflow-x: auto;
}

article .content code {
    color: #4EA1FF;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
}

article .content .cta {
    background: #15202B;
    border: 1px solid #1E3449;
    border-radius: 8px;
    padding: 2rem;
    margin: 3rem 0;
    text-align: center;
}

article .content .cta p {
    color: #4EA1FF;
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

article footer {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid #1E3449;
}

article .tags {
    margin-bottom: 2rem;
}

/* Remove share section */
.share {
    display: none;
}

/* Latest Articles Section */
#latest-posts {
    background: linear-gradient(180deg, #0D1D2D, #0A1622);
    padding: 5rem 0;
    border-top: 1px solid #1E3449;
    border-bottom: 1px solid #1E3449;
    position: relative;
    z-index: 1;
}

#latest-posts::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(180deg, #0D1D2D, #0A1622);
    z-index: -1;
}

#latest-posts h2 {
    color: #4EA1FF;
    margin-bottom: 3rem;
}

#latest-posts .lead {
    color: #90B8E3;
    margin-bottom: 3rem;
}

.blog-card {
    background: #15202B;
    border: 1px solid #1E3449;
    padding: 1.5rem;
    border-radius: 8px;
    height: 100%;
    transition: all 0.3s ease;
    position: relative;
    z-index: 2;
}

.blog-card:hover {
    transform: translateY(-2px);
    border-color: #4EA1FF;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.blog-card h3 {
    font-size: 1.4rem;
    margin: 1rem 0;
}

.blog-card h3 a {
    color: #4EA1FF;
    text-decoration: none;
    transition: color 0.2s ease;
}

.blog-card h3 a:hover {
    color: #90B8E3;
}

.blog-card p {
    color: #90B8E3;
    margin-bottom: 1rem;
    line-height: 1.6;
}

.blog-card .read-more {
    color: #4EA1FF;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
}

.blog-card .read-more:hover {
    color: #90B8E3;
}

/* Breadcrumb Styles */
.breadcrumb {
    background: #15202B;
    border: 1px solid #1E3449;
    border-radius: 8px;
    padding: 1rem 1.5rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.breadcrumb-item {
    display: flex;
    align-items: center;
    color: #90B8E3;
    font-size: 0.9rem;
}

.breadcrumb-item:not(:last-child)::after {
    content: '/';
    margin-left: 0.5rem;
    color: #4EA1FF;
}

.breadcrumb-item a {
    color: #4EA1FF;
    text-decoration: none;
    transition: color 0.2s ease;
}

.breadcrumb-item a:hover {
    color: #90B8E3;
}

.breadcrumb-item.active {
    color: #90B8E3;
}

.navbar .nav-link {
    color: #ffffff !important;
    transition: all 0.3s ease;
    position: relative;
    padding-bottom: 2px;
}

.navbar .nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(90deg, #4EA1FF, #90B8E3);
    transition: width 0.3s ease;
}

.navbar .nav-link:hover {
    color: #ffffff !important;
    transform: translateY(-1px);
}

.navbar .nav-link:hover::after {
    width: 100%;
}

.navbar .navbar-brand {
    color: #ffffff !important;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.navbar .navbar-brand:hover {
    color: #ffffff !important;
    transform: translateY(-1px);
}

.navbar .navbar-brand img {
    transition: transform 0.3s ease;
}

.navbar .navbar-brand:hover img {
    transform: scale(1.1);
}

/* Mobile menu alignment */
@media (max-width: 991px) {
    .navbar-collapse {
        text-align: right;
    }
    
    .navbar-nav {
        align-items: flex-end;
    }
    
    .nav-item {
        width: 100%;
        text-align: right;
    }
    
    .nav-link {
        padding-right: 1rem;
    }
}

/* Back to top button */
.back-to-top {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    background: linear-gradient(135deg, #4EA1FF, #3D7FCC);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    border: none;
    box-shadow: 0 4px 12px rgba(78, 161, 255, 0.3);
    z-index: 1000;
}

.back-to-top.visible {
    opacity: 1;
    visibility: visible;
}

.back-to-top:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(78, 161, 255, 0.4);
}

.back-to-top svg {
    width: 1.5rem;
    height: 1.5rem;
    transition: transform 0.3s ease;
}

.back-to-top:hover svg {
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .back-to-top {
        bottom: 1.5rem;
        right: 1.5rem;
        width: 2.5rem;
        height: 2.5rem;
    }
}
```

## File: `brain/knowledge/docs_legacy/blog/bold-brew-2-0-cask-support.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bold Brew 2.0: Complete Homebrew Management with Cask Support</title>
    <meta name="description" content="Bold Brew 2.0 brings major new features including full Cask support, Leaves filter, XDG compliance, and enhanced security. Manage both CLI tools and GUI applications seamlessly.">
    <meta name="keywords" content="Bold Brew 2.0, Homebrew casks, TUI package manager, leaves filter, XDG compliance, Homebrew GUI, terminal UI, package management, macOS apps, Linux apps">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Bold Brew 2.0: Complete Homebrew Management with Cask Support">
    <meta property="og:description" content="Bold Brew 2.0 brings major new features including full Cask support, Leaves filter, XDG compliance, and enhanced security. Manage both CLI tools and GUI applications seamlessly.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/bold-brew-2-0-cask-support.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Bold Brew 2.0: Complete Homebrew Management with Cask Support">
    <meta name="twitter:description" content="Bold Brew 2.0 brings major new features including full Cask support, Leaves filter, XDG compliance, and enhanced security. Manage both CLI tools and GUI applications seamlessly.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/bold-brew-2-0-cask-support.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/bold-brew-2-0-cask-support.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/bold-brew-2-0-cask-support.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        Bold Brew 2.0: Complete Homebrew Management with Cask Support
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>Bold Brew 2.0: Complete Homebrew Management with Cask Support</h1>
            <div class="meta">
                <span class="date">2025-10-13</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>Bold Brew 2.0: Complete Homebrew Management with Cask Support</h1>
<p>We&#39;re thrilled to announce <strong>Bold Brew 2.0</strong>, the biggest update since launch! This release transforms Bold Brew from a formula-only manager into a <strong>complete Homebrew management solution</strong> that handles both command-line tools and GUI applications.</p>
<h2>🎉 What&#39;s New</h2>
<h3>Full Homebrew Casks Support</h3>
<p>The most requested feature is finally here! Bold Brew now provides <strong>complete support for Homebrew Casks</strong>, allowing you to manage GUI applications and binaries directly from the same intuitive interface you love.</p>
<p><strong>What are Casks?</strong> Homebrew Casks extend Homebrew&#39;s package management to include macOS and Linux GUI applications. Instead of just installing command-line tools like <code>git</code> or <code>node</code>, you can now manage apps like Google Chrome, Visual Studio Code, Docker Desktop, and thousands more.</p>
<h4>Visual Type Indicators</h4>
<p>Never wonder what type of package you&#39;re looking at! Bold Brew 2.0 introduces clear visual indicators:</p>
<ul>
<li><code>[F]</code> - Formula (command-line tool)</li>
<li><code>[C]</code> - Cask (GUI application or binary)</li>
</ul>
<p>These tags appear throughout the interface, making it instantly clear whether you&#39;re working with a CLI tool or a desktop application.</p>
<h3>Smart Leaves Filter</h3>
<p>Tired of seeing all those dependency packages cluttering your installed list? The new <strong>Leaves Filter</strong> (press <code>L</code>) shows only packages you explicitly installed, hiding all the dependencies that came along for the ride.</p>
<p><strong>Perfect for:</strong></p>
<ul>
<li>Cleaning up your system by identifying what you actually need</li>
<li>Creating reproducible development environments</li>
<li>Understanding your actual package footprint</li>
<li>Selective updates of only your core tools</li>
</ul>
<h3>XDG Base Directory Compliance</h3>
<p>Bold Brew 2.0 now follows the <a href="https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html">XDG Base Directory Specification</a>, providing a cleaner, more standards-compliant cache management:</p>
<ul>
<li><strong>Linux</strong>: <code>~/.cache/bbrew</code> or <code>$XDG_CACHE_HOME/bbrew</code></li>
<li><strong>macOS</strong>: <code>~/Library/Caches/bbrew</code> (native macOS location!)</li>
<li><strong>Windows</strong> (WSL2): Windows Known Folders support</li>
</ul>
<p>No more random dotfiles in your home directory—everything is where it should be.</p>
<h2>🔧 Technical Improvements</h2>
<h3>Go 1.25 and Modern Tooling</h3>
<ul>
<li><strong>Updated to Go 1.25</strong> for better performance and latest language features</li>
<li><strong>Migrated to Podman</strong> and OCI-compliant Containerfile for better security</li>
<li><strong>Enhanced Makefile</strong> with 15+ new targets including <code>make test</code>, <code>make security</code>, and <code>make install</code></li>
<li><strong>Improved build system</strong> with local and containerized build options</li>
</ul>
<h3>Enhanced Security</h3>
<p>Security is a priority. Bold Brew 2.0 includes:</p>
<ul>
<li><strong>govulncheck</strong> - Automated Go vulnerability scanning</li>
<li><strong>gosec</strong> - Static security analysis</li>
<li><strong>GitHub Security integration</strong> - SARIF reports uploaded to Security tab</li>
<li><strong>Fixed memory aliasing issues</strong> - Cleaner, safer code</li>
<li><strong>Better permission handling</strong> - Secure cache directory permissions (0750)</li>
</ul>
<h3>Better User Experience</h3>
<ul>
<li><strong>Enhanced keyboard shortcuts</strong> - More intuitive navigation and filtering</li>
<li><strong>Improved error messages</strong> - Better debugging and user feedback</li>
<li><strong>Analytics integration</strong> - See popular packages based on 90-day download stats</li>
<li><strong>Real-time feedback</strong> - Live updates during package operations</li>
<li><strong>Fixed rendering issues</strong> - Proper display of all UI elements</li>
</ul>
<h2>🐛 Bug Fixes</h2>
<ul>
<li>Fixed cask analytics endpoint (now correctly fetches download statistics)</li>
<li>Corrected installed casks detection (properly identifies locally installed casks)</li>
<li>Fixed tview special character rendering for type tags</li>
<li>Improved directory permission handling for cache</li>
<li>Enhanced error handling throughout the application</li>
</ul>
<h2>🚀 Getting Started</h2>
<h3>For Existing Users</h3>
<p>Update to the latest version:</p>
<pre><code class="language-bash">brew update
brew upgrade bbrew
</code></pre>
<h3>For New Users</h3>
<p>Install Bold Brew via Homebrew:</p>
<pre><code class="language-bash">brew install Valkyrie00/homebrew-bbrew/bbrew
</code></pre>
<p>Or download from the <a href="https://github.com/Valkyrie00/bold-brew/releases">releases page</a>.</p>
<h2>📖 Using the New Features</h2>
<h3>Managing Casks</h3>
<ol>
<li><strong>Filter Casks Only</strong>: Press <code>C</code> to show only Cask packages</li>
<li><strong>Search Casks</strong>: Type <code>/</code> and search for your favorite GUI app (e.g., &quot;chrome&quot;, &quot;vscode&quot;, &quot;docker&quot;)</li>
<li><strong>Install a Cask</strong>: Select it and press <code>I</code></li>
<li><strong>Update Casks</strong>: Press <code>U</code> on any outdated Cask, or <code>Ctrl+U</code> to update all</li>
</ol>
<h3>Using the Leaves Filter</h3>
<ol>
<li>Press <code>L</code> to activate the Leaves filter</li>
<li>Browse only the packages you explicitly installed</li>
<li>Identify packages you no longer need</li>
<li>Press <code>R</code> to remove unwanted packages</li>
</ol>
<h3>Keyboard Shortcuts Reference</h3>
<h4>Filters</h4>
<ul>
<li><code>F</code> - Filter installed packages</li>
<li><code>O</code> - Filter outdated packages</li>
<li><code>L</code> - Filter leaves (explicitly installed, no dependencies)</li>
<li><code>C</code> - Filter casks only</li>
</ul>
<h4>Package Operations</h4>
<ul>
<li><code>I</code> - Install selected package</li>
<li><code>U</code> - Update selected package</li>
<li><code>R</code> - Remove selected package</li>
<li><code>Ctrl+U</code> - Update all outdated packages</li>
</ul>
<h2>🌐 Cross-Platform Support</h2>
<p>Bold Brew 2.0 provides excellent support across platforms:</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Support</th>
<th>Notes</th>
</tr>
</thead>
<tbody><tr>
<td>🍎 <strong>macOS</strong></td>
<td>✅ Full</td>
<td>Native Homebrew support with macOS-specific cache location</td>
</tr>
<tr>
<td>🐧 <strong>Linux</strong></td>
<td>✅ Full</td>
<td>Linuxbrew/Homebrew support with XDG compliance</td>
</tr>
<tr>
<td>🪟 <strong>Windows</strong></td>
<td>⚠️ Partial</td>
<td>Via WSL2 with Homebrew</td>
</tr>
</tbody></table>
<h2>🎯 What&#39;s Next</h2>
<p>We&#39;re not stopping here! Future plans include:</p>
<ul>
<li><strong>Formulae pinning</strong> - Pin specific package versions</li>
<li><strong>Backup/restore</strong> - Export and import your package lists</li>
<li><strong>Themes</strong> - Customizable color schemes</li>
<li><strong>Plugin system</strong> - Extend Bold Brew with custom functionality</li>
</ul>
<blockquote>
<p><strong>Update:</strong> Tap management and Brewfile Mode with remote URL support are now available! <a href="/blog/brewfile-mode-remote-support.html">Read more</a></p>
</blockquote>
<h2>🙏 Acknowledgments</h2>
<p>A huge thank you to:</p>
<ul>
<li>The Homebrew team for the excellent package management system</li>
<li>Project Bluefin for adopting Bold Brew as their official Homebrew TUI</li>
<li>All contributors who submitted issues, PRs, and feature requests</li>
<li>The community for their continued support and feedback</li>
</ul>
<h2>📣 Spread the Word</h2>
<p>If you love Bold Brew 2.0:</p>
<ul>
<li>⭐ <a href="https://github.com/Valkyrie00/bold-brew">Star the project on GitHub</a></li>
<li>🐦 Share on social media</li>
<li>📝 Write about it on your blog</li>
<li>💬 Tell your developer friends</li>
</ul>
<h2>🔗 Resources</h2>
<ul>
<li><a href="https://github.com/Valkyrie00/bold-brew">GitHub Repository</a></li>
<li><a href="https://bold-brew.com">Documentation</a></li>
<li><a href="https://github.com/Valkyrie00/bold-brew/releases">Release Notes</a></li>
<li><a href="https://github.com/Valkyrie00/bold-brew/issues">Report Issues</a></li>
</ul>
<hr>
<p><strong>Happy brewing! 🍺</strong></p>
<p><em>The Bold Brew Team</em></p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/bold-brew-official-project-bluefin-tui.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bold Brew Named Official Homebrew TUI for Project Bluefin</title>
    <meta name="description" content="Bold Brew becomes the official Terminal UI for managing Homebrew in Project Bluefin, a next-generation Linux desktop serving tens of thousands of users worldwide.">
    <meta name="keywords" content="Bold Brew, Project Bluefin, Universal Blue, Fedora Silverblue, atomic desktop, official TUI, Linux desktop, Homebrew Linux, immutable OS, cloud-native desktop">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Bold Brew Named Official Homebrew TUI for Project Bluefin">
    <meta property="og:description" content="Bold Brew becomes the official Terminal UI for managing Homebrew in Project Bluefin, a next-generation Linux desktop serving tens of thousands of users worldwide.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/bold-brew-official-project-bluefin-tui.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Bold Brew Named Official Homebrew TUI for Project Bluefin">
    <meta name="twitter:description" content="Bold Brew becomes the official Terminal UI for managing Homebrew in Project Bluefin, a next-generation Linux desktop serving tens of thousands of users worldwide.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/bold-brew-official-project-bluefin-tui.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/bold-brew-official-project-bluefin-tui.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/bold-brew-official-project-bluefin-tui.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        Bold Brew Named Official Homebrew TUI for Project Bluefin
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>Bold Brew Named Official Homebrew TUI for Project Bluefin</h1>
            <div class="meta">
                <span class="date">2025-10-13</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>Bold Brew Named Official Homebrew TUI for Project Bluefin</h1>
<p>We&#39;re incredibly proud to announce that <strong>Bold Brew has been selected as the official Terminal UI</strong> for managing Homebrew in <a href="https://projectbluefin.io/"><strong>Project Bluefin</strong></a>, a next-generation Linux desktop that serves tens of thousands of users worldwide!</p>
<h2>🌊 What is Project Bluefin?</h2>
<p><a href="https://projectbluefin.io/">Project Bluefin</a> is a cutting-edge Linux desktop distribution that&#39;s part of the <a href="https://universal-blue.org/">Universal Blue</a> ecosystem. Built on Fedora Atomic Desktop (formerly Silverblue), Bluefin represents the future of cloud-native desktop computing.</p>
<h3>Key Features of Bluefin</h3>
<ul>
<li><strong>Atomic Updates</strong> - System updates are atomic and can be rolled back</li>
<li><strong>Immutable Base</strong> - Core system is read-only for enhanced security</li>
<li><strong>Container-First</strong> - Development happens in containers, keeping the host clean</li>
<li><strong>Modern Tooling</strong> - Ships with the latest development tools and workflows</li>
<li><strong>Cloud-Native</strong> - Designed for modern cloud-native development practices</li>
</ul>
<p>Bluefin is perfect for developers, DevOps engineers, and anyone who wants a reliable, cutting-edge Linux desktop that &quot;just works.&quot;</p>
<h2>🎯 Why Bold Brew?</h2>
<p>Bluefin&#39;s philosophy emphasizes <strong>quality over quantity</strong> and <strong>user experience</strong> above all else. The project carefully curates every tool and application that ships with the distribution, ensuring they meet high standards for usability and reliability.</p>
<p>From the <a href="https://docs.projectbluefin.io/command-line/">Bluefin documentation</a>:</p>
<blockquote>
<p><strong>Bold Brew</strong> is included as a text based user interface (TUI) to Brew. This application features full package management for homebrew in a nice nerdy interface.</p>
</blockquote>
<p>Bold Brew was selected because it:</p>
<ul>
<li><strong>Simplifies Homebrew management</strong> with an intuitive TUI</li>
<li><strong>Aligns with Bluefin&#39;s design philosophy</strong> of modern, user-friendly tools</li>
<li><strong>Enhances the terminal experience</strong> that Bluefin is passionate about</li>
<li><strong>Works seamlessly</strong> with Bluefin&#39;s container-first workflow</li>
<li><strong>Provides both power and simplicity</strong> for all user levels</li>
</ul>
<h2>🚀 Bold Brew on Bluefin</h2>
<h3>Pre-installed and Ready</h3>
<p>Bold Brew comes <strong>pre-installed</strong> on every Bluefin system. Users can launch it simply by typing:</p>
<pre><code class="language-bash">bbrew
</code></pre>
<p>No installation, no configuration—it just works.</p>
<h3>Perfect Integration</h3>
<p>Bold Brew fits perfectly into Bluefin&#39;s command-line ecosystem, which includes:</p>
<ul>
<li><strong>Homebrew</strong> - Package manager for command-line tools</li>
<li><strong>Flatpak</strong> - GUI application management</li>
<li><strong>Podman</strong> - Container management</li>
<li><strong>ujust</strong> - System configuration and automation</li>
</ul>
<p>Together, these tools provide a complete, modern package management experience.</p>
<h3>The Bluefin CLI Experience</h3>
<p>Bluefin offers an optional enhanced CLI experience called <code>bluefin-cli</code>, which includes modern terminal tools like:</p>
<ul>
<li><code>atuin</code> for shell history</li>
<li><code>eza</code> as a modern <code>ls</code> replacement</li>
<li><code>fd</code> for finding files</li>
<li><code>ripgrep</code> for search</li>
<li><code>zoxide</code> as a smarter <code>cd</code></li>
</ul>
<p>Bold Brew complements these tools by providing visual, interactive Homebrew management that&#39;s faster and more intuitive than typing commands.</p>
<h2>📊 Impact and Reach</h2>
<p>Being adopted by Project Bluefin means Bold Brew now reaches:</p>
<ul>
<li><strong>Tens of thousands</strong> of active Bluefin users</li>
<li><strong>Developers and DevOps professionals</strong> worldwide</li>
<li><strong>Cloud-native engineers</strong> building modern applications</li>
<li><strong>Linux enthusiasts</strong> who want cutting-edge desktop experiences</li>
</ul>
<p>This partnership significantly expands Bold Brew&#39;s user base and validates our approach to TUI package management.</p>
<h2>🤝 Community and Ecosystem</h2>
<h3>Universal Blue Ecosystem</h3>
<p>Project Bluefin is part of the broader <strong>Universal Blue</strong> ecosystem, which includes:</p>
<ul>
<li><strong><a href="https://getaurora.dev/">Aurora</a></strong> - KDE Plasma variant of Bluefin</li>
<li><strong><a href="https://bazzite.gg/">Bazzite</a></strong> - Gaming-focused Linux desktop</li>
<li><strong><a href="https://projectbluefin.io/cayo">Cayo</a></strong> - Bluefin for developers</li>
</ul>
<p>Bold Brew&#39;s adoption in Bluefin opens doors to potential integration across the entire Universal Blue ecosystem, bringing our TUI to even more users and use cases.</p>
<h3>Growing Together</h3>
<p>This partnership benefits both projects:</p>
<p><strong>For Bluefin:</strong></p>
<ul>
<li>Enhanced user experience for Homebrew management</li>
<li>Modern, intuitive tool that matches their design philosophy</li>
<li>Active maintenance and feature development</li>
<li>Community-driven improvements</li>
</ul>
<p><strong>For Bold Brew:</strong></p>
<ul>
<li>Significant user base and real-world testing</li>
<li>Valuable feedback from power users</li>
<li>Integration with a respected Linux distribution</li>
<li>Increased visibility in the Linux community</li>
</ul>
<h2>🎓 What This Means for Users</h2>
<h3>Bluefin Users</h3>
<p>If you&#39;re a Bluefin user, you already have Bold Brew installed! Here&#39;s how to get started:</p>
<ol>
<li><strong>Launch Bold Brew</strong>: Just type <code>bbrew</code> in your terminal</li>
<li><strong>Explore packages</strong>: Press <code>/</code> to search for any package</li>
<li><strong>Filter views</strong>: Use <code>F</code> for installed, <code>O</code> for outdated, <code>L</code> for leaves, <code>C</code> for casks</li>
<li><strong>Manage packages</strong>: Press <code>I</code> to install, <code>U</code> to update, <code>R</code> to remove</li>
<li><strong>Stay updated</strong>: Bold Brew updates are automatically delivered with Bluefin</li>
</ol>
<h3>Bold Brew Users on Other Systems</h3>
<p>This partnership validates Bold Brew as a production-ready tool trusted by a major Linux distribution. Whether you&#39;re on macOS or Linux, you can benefit from the same tool that Bluefin trusts.</p>
<h2>🔮 Future Collaboration</h2>
<p>We&#39;re excited to deepen our collaboration with Project Bluefin:</p>
<ul>
<li><strong>Feature requests</strong> from Bluefin users will help shape Bold Brew&#39;s roadmap</li>
<li><strong>Integration improvements</strong> to make Bold Brew even more native to Bluefin</li>
<li><strong>Documentation</strong> tailored for Bluefin users</li>
<li><strong>Joint community events</strong> and user support</li>
<li><strong>Possible expansion</strong> to other Universal Blue distributions</li>
</ul>
<h2>🙏 Thank You</h2>
<p>We want to thank:</p>
<ul>
<li><strong>The Bluefin team</strong> for recognizing Bold Brew&#39;s potential and making it their official choice</li>
<li><strong>Jorge Castro</strong> and the <strong>Universal Blue</strong> community for building amazing cloud-native desktops</li>
<li><strong>The Bluefin community</strong> for welcoming Bold Brew and providing valuable feedback</li>
<li><strong>Our contributors</strong> who made Bold Brew worthy of this recognition</li>
<li><strong>The Homebrew team</strong> for creating the excellent package manager we&#39;re building on top of</li>
</ul>
<h2>📣 Try Bluefin Today</h2>
<p>Interested in experiencing the future of Linux desktops?</p>
<ol>
<li><strong>Visit</strong> <a href="https://projectbluefin.io/">projectbluefin.io</a></li>
<li><strong>Download</strong> the latest ISO</li>
<li><strong>Install</strong> and experience Bold Brew out of the box</li>
<li><strong>Join</strong> the <a href="https://universal-blue.discourse.group/">Bluefin community</a> on Discourse</li>
</ol>
<h2>🔗 Resources</h2>
<h3>Bold Brew</h3>
<ul>
<li><a href="https://github.com/Valkyrie00/bold-brew">GitHub Repository</a></li>
<li><a href="https://bold-brew.com">Documentation</a></li>
<li><a href="https://github.com/Valkyrie00/bold-brew/releases">Releases</a></li>
</ul>
<h3>Project Bluefin</h3>
<ul>
<li><a href="https://projectbluefin.io/">Official Website</a></li>
<li><a href="https://docs.projectbluefin.io/">Documentation</a></li>
<li><a href="https://docs.projectbluefin.io/command-line/">Command Line Guide</a></li>
<li><a href="https://github.com/ublue-os/bluefin">GitHub</a></li>
</ul>
<h3>Universal Blue</h3>
<ul>
<li><a href="https://universal-blue.org/">Website</a></li>
<li><a href="https://universal-blue.discourse.group/">Discourse Community</a></li>
<li><a href="https://github.com/ublue-os">GitHub Organization</a></li>
</ul>
<hr>
<p><strong>This is just the beginning of an exciting partnership!</strong> 🎉</p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/brewfile-mode-remote-support.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brewfile Mode: Curated Package Collections &amp; Remote URL Support</title>
    <meta name="description" content="Bold Brew now supports Brewfile mode for curated package collections, plus the ability to load Brewfiles directly from HTTPS URLs. Perfect for team configurations and themed installers.">
    <meta name="keywords" content="Brewfile mode, remote Brewfile, HTTPS URL, curated packages, team configuration, Homebrew TUI, package collections, IDE installer, dev tools, Bold Brew">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Brewfile Mode: Curated Package Collections &amp; Remote URL Support">
    <meta property="og:description" content="Bold Brew now supports Brewfile mode for curated package collections, plus the ability to load Brewfiles directly from HTTPS URLs. Perfect for team configurations and themed installers.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/brewfile-mode-remote-support.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Brewfile Mode: Curated Package Collections &amp; Remote URL Support">
    <meta name="twitter:description" content="Bold Brew now supports Brewfile mode for curated package collections, plus the ability to load Brewfiles directly from HTTPS URLs. Perfect for team configurations and themed installers.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/brewfile-mode-remote-support.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/brewfile-mode-remote-support.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/brewfile-mode-remote-support.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        Brewfile Mode: Curated Package Collections &amp; Remote URL Support
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>Brewfile Mode: Curated Package Collections &amp; Remote URL Support</h1>
            <div class="meta">
                <span class="date">2025-12-29</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>Brewfile Mode: Curated Package Collections &amp; Remote URL Support</h1>
<p>We&#39;re excited to announce a major new capability in Bold Brew: <strong>Brewfile Mode</strong> with full support for <strong>remote Brewfiles via HTTPS URLs</strong>. This feature transforms how teams and individuals manage their Homebrew package collections.</p>
<h2>🎯 What is Brewfile Mode?</h2>
<p>Brewfile Mode allows you to launch Bold Brew with a curated list of packages instead of the full Homebrew catalog. This is perfect for:</p>
<ul>
<li><strong>Themed installers</strong> (IDE tools, AI/ML packages, DevOps tools)</li>
<li><strong>Team onboarding</strong> (share your team&#39;s essential tools)</li>
<li><strong>Project-specific setups</strong> (install only what a project needs)</li>
<li><strong>Personal collections</strong> (your favorite tools in one place)</li>
</ul>
<h3>How It Works</h3>
<pre><code class="language-bash"># Local Brewfile
bbrew -f ~/Brewfile

# Remote Brewfile (NEW!)
bbrew -f https://raw.githubusercontent.com/your-org/configs/main/dev-tools.Brewfile
</code></pre>
<p>When you launch in Brewfile mode, Bold Brew shows <strong>only</strong> the packages defined in that Brewfile. You get the full Bold Brew experience—search, filters, install/remove—but focused on your curated selection.</p>
<h2>🌐 Remote Brewfiles via HTTPS</h2>
<p>The latest update adds support for loading Brewfiles directly from URLs. This opens up exciting possibilities:</p>
<h3>Share Team Configurations</h3>
<pre><code class="language-bash"># Everyone on the team uses the same dev tools
bbrew -f https://github.com/acme-corp/dotfiles/raw/main/Brewfile
</code></pre>
<h3>Create Themed Installers</h3>
<pre><code class="language-bash"># AI/ML development environment
bbrew -f https://example.com/brewfiles/ai-ml-toolkit.Brewfile

# Kubernetes tools collection
bbrew -f https://example.com/brewfiles/k8s-essentials.Brewfile

# Frontend development stack
bbrew -f https://example.com/brewfiles/frontend-dev.Brewfile
</code></pre>
<h3>Quick Setup for New Machines</h3>
<p>Share a single URL with colleagues or include it in your README:</p>
<pre><code class="language-markdown">## Development Setup

Install our recommended tools:
\`\`\`bash
brew install Valkyrie00/homebrew-bbrew/bbrew
bbrew -f https://our-company.com/dev-setup.Brewfile
\`\`\`
</code></pre>
<h2>📦 Third-Party Tap Support</h2>
<p>Brewfile Mode also includes full support for <strong>third-party taps</strong>. Your Brewfile can include packages from any Homebrew tap:</p>
<pre><code class="language-ruby"># Brewfile example
tap &quot;homebrew/cask-fonts&quot;
tap &quot;ublue-os/homebrew-tap&quot;

# Core tools
brew &quot;git&quot;
brew &quot;gh&quot;
brew &quot;jq&quot;

# Fonts
cask &quot;font-fira-code&quot;
cask &quot;font-jetbrains-mono&quot;

# From third-party tap
cask &quot;some-custom-package&quot;
</code></pre>
<p>Bold Brew automatically:</p>
<ol>
<li><strong>Installs missing taps</strong> at startup</li>
<li><strong>Caches tap package info</strong> for faster subsequent loads</li>
<li><strong>Shows real-time progress</strong> during tap installation</li>
</ol>
<h2>🔒 Security First</h2>
<p>Remote Brewfiles are loaded securely:</p>
<ul>
<li><strong>HTTPS only</strong> — HTTP URLs are rejected for security</li>
<li><strong>Temporary storage</strong> — Downloaded files are automatically cleaned up</li>
<li><strong>No persistence</strong> — Remote content isn&#39;t cached between sessions</li>
</ul>
<h2>🎨 Use Cases</h2>
<h3>1. IDE Chooser for Teams</h3>
<p>Create a Brewfile with all supported IDEs and let developers pick:</p>
<pre><code class="language-ruby"># ide-chooser.Brewfile
cask &quot;visual-studio-code&quot;
cask &quot;sublime-text&quot;
cask &quot;jetbrains-toolbox&quot;
cask &quot;zed&quot;
cask &quot;cursor&quot;
</code></pre>
<pre><code class="language-bash">bbrew -f https://team.example.com/ide-chooser.Brewfile
</code></pre>
<h3>2. Project Onboarding</h3>
<p>Include a Brewfile in your project repo:</p>
<pre><code class="language-ruby"># project/.Brewfile
brew &quot;node&quot;
brew &quot;pnpm&quot;
brew &quot;docker&quot;
cask &quot;docker&quot;
</code></pre>
<p>New contributors run one command to get all dependencies.</p>
<h3>3. Personal Dotfiles</h3>
<p>Keep your Brewfile in your dotfiles repo and access it from anywhere:</p>
<pre><code class="language-bash">bbrew -f https://github.com/username/dotfiles/raw/main/Brewfile
</code></pre>
<h2>📋 Example Brewfiles</h2>
<p>Bold Brew includes example Brewfiles in the <code>examples/</code> directory:</p>
<ul>
<li><strong><code>all.brewfile</code></strong> — Comprehensive package collection</li>
<li><strong><code>ide.Brewfile</code></strong> — Popular IDEs and editors</li>
</ul>
<p>Check them out for inspiration!</p>
<h2>🚀 Getting Started</h2>
<ol>
<li><p><strong>Update Bold Brew</strong> to the latest version:</p>
<pre><code class="language-bash">brew upgrade bbrew
</code></pre>
</li>
<li><p><strong>Try a local Brewfile</strong>:</p>
<pre><code class="language-bash">bbrew -f ~/path/to/Brewfile
</code></pre>
</li>
<li><p><strong>Try a remote Brewfile</strong>:</p>
<pre><code class="language-bash">bbrew -f https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/examples/all.brewfile
</code></pre>
</li>
</ol>
<h2>🎹 Brewfile Mode Shortcuts</h2>
<p>When running in Brewfile mode, you get additional keyboard shortcuts:</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Action</th>
</tr>
</thead>
<tbody><tr>
<td><code>Ctrl+A</code></td>
<td>Install all packages from Brewfile</td>
</tr>
<tr>
<td><code>Ctrl+R</code></td>
<td>Remove all packages from Brewfile</td>
</tr>
</tbody></table>
<p>All standard shortcuts (search, filters, individual install/remove) work exactly as expected.</p>
<h2>💡 Tips &amp; Best Practices</h2>
<ol>
<li><strong>Version your Brewfiles</strong> — Keep them in git for change tracking</li>
<li><strong>Use comments</strong> — Document why each package is included</li>
<li><strong>Organize by category</strong> — Group related packages together</li>
<li><strong>Test before sharing</strong> — Verify packages exist and install correctly</li>
</ol>
<h2>🔗 Resources</h2>
<ul>
<li><a href="https://github.com/Homebrew/homebrew-bundle">Homebrew Brewfile documentation</a></li>
<li><a href="https://github.com/Valkyrie00/bold-brew">Bold Brew on GitHub</a></li>
<li><a href="https://github.com/Valkyrie00/bold-brew/tree/main/examples">Example Brewfiles</a></li>
</ul>
<hr>
<p><strong>Happy brewing with curated collections! 🍺</strong></p>
<p><em>The Bold Brew Team</em></p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/essential-homebrew-commands.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>10 Essential Homebrew Commands You Should Know</title>
    <meta name="description" content="Master the most important Homebrew commands for macOS package management. Learn how to install, update, and manage packages efficiently.">
    <meta name="keywords" content="Homebrew commands, brew commands, macOS package management, brew update, brew install, brew upgrade, brew search, essential commands">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="10 Essential Homebrew Commands You Should Know">
    <meta property="og:description" content="Master the most important Homebrew commands for macOS package management. Learn how to install, update, and manage packages efficiently.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/essential-homebrew-commands.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="10 Essential Homebrew Commands You Should Know">
    <meta name="twitter:description" content="Master the most important Homebrew commands for macOS package management. Learn how to install, update, and manage packages efficiently.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/essential-homebrew-commands.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/essential-homebrew-commands.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/essential-homebrew-commands.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        10 Essential Homebrew Commands You Should Know
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>10 Essential Homebrew Commands You Should Know</h1>
            <div class="meta">
                <span class="date">2025-03-29</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>10 Essential Homebrew Commands You Should Know</h1>
<p>Homebrew is the most popular package manager for macOS, and mastering its commands is essential for efficient package management. In this guide, we&#39;ll explore the 10 most important Homebrew commands that every macOS user should know.</p>
<h2>1. Install Packages</h2>
<p>The most basic and commonly used command is <code>brew install</code>:</p>
<pre><code class="language-bash">brew install package_name
</code></pre>
<p>You can also install multiple packages at once:</p>
<pre><code class="language-bash">brew install package1 package2 package3
</code></pre>
<h2>2. Update Homebrew</h2>
<p>Keep your Homebrew installation up to date:</p>
<pre><code class="language-bash">brew update
</code></pre>
<p>This command updates Homebrew&#39;s package database to the latest version.</p>
<h2>3. Upgrade Packages</h2>
<p>Upgrade all installed packages:</p>
<pre><code class="language-bash">brew upgrade
</code></pre>
<p>Or upgrade a specific package:</p>
<pre><code class="language-bash">brew upgrade package_name
</code></pre>
<h2>4. Remove Packages</h2>
<p>Uninstall a package:</p>
<pre><code class="language-bash">brew uninstall package_name
</code></pre>
<h2>5. Get Package Information</h2>
<p>View detailed information about a package:</p>
<pre><code class="language-bash">brew info package_name
</code></pre>
<h2>6. List Installed Packages</h2>
<p>See all currently installed packages:</p>
<pre><code class="language-bash">brew list
</code></pre>
<h2>7. Search for Packages</h2>
<p>Find packages in the Homebrew repository:</p>
<pre><code class="language-bash">brew search package_name
</code></pre>
<h2>8. Check System Status</h2>
<p>Diagnose your Homebrew installation:</p>
<pre><code class="language-bash">brew doctor
</code></pre>
<h2>9. Clean Up</h2>
<p>Remove old versions and clean the cache:</p>
<pre><code class="language-bash">brew cleanup
</code></pre>
<h2>10. Manage Taps</h2>
<p>List tapped repositories:</p>
<pre><code class="language-bash">brew tap
</code></pre>
<p>Add a new tap:</p>
<pre><code class="language-bash">brew tap user/repo
</code></pre>
<h2>Pro Tips</h2>
<ol>
<li>Combine update and upgrade:</li>
</ol>
<pre><code class="language-bash">brew update &amp;&amp; brew upgrade
</code></pre>
<ol start="2">
<li><p>Use <code>brew doctor</code> regularly to maintain a healthy Homebrew installation.</p>
</li>
<li><p>Consider using Bold Brew for a more intuitive package management experience.</p>
</li>
</ol>
<h2>Conclusion</h2>
<p>These commands form the foundation of Homebrew usage. While mastering the command line is important, tools like Bold Brew can make package management more intuitive and efficient.</p>
<p>Remember to check the <a href="https://bold-brew.com">Bold Brew documentation</a> for more tips and tricks on managing your Homebrew packages. </p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog | Bold Brew (bbrew)</title>
    <meta name="description" content="Tips, tutorials, and guides for managing Homebrew packages on macOS">
    <meta name="keywords" content="Homebrew blog, macOS tutorials, package management, Bold Brew guides">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Blog | Bold Brew (bbrew)">
    <meta property="og:description" content="Tips, tutorials, and guides for managing Homebrew packages on macOS">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Blog | Bold Brew (bbrew)">
    <meta name="twitter:description" content="Tips, tutorials, and guides for managing Homebrew packages on macOS">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        Blog
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <header class="mb-5">
        <h1>Bold Brew Blog</h1>
        <p class="lead">Tips, tutorials, and guides for managing Homebrew packages and casks</p>
    </header>

    <div class="row">
        <div class="col-lg-8">
            <div class="blog-posts">
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-12-29</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/brewfile-mode-remote-support.html">Brewfile Mode: Curated Package Collections &amp; Remote URL Support</a></h2>
                        <p class="excerpt">Bold Brew now supports Brewfile mode for curated package collections, plus the ability to load Brewfiles directly from HTTPS URLs. Perfect for team configurations and themed installers.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/brewfile-mode-remote-support.html" class="read-more">Read more →</a>
                    </article>
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-10-13</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/bold-brew-2-0-cask-support.html">Bold Brew 2.0: Complete Homebrew Management with Cask Support</a></h2>
                        <p class="excerpt">Bold Brew 2.0 brings major new features including full Cask support, Leaves filter, XDG compliance, and enhanced security. Manage both CLI tools and GUI applications seamlessly.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/bold-brew-2-0-cask-support.html" class="read-more">Read more →</a>
                    </article>
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-10-13</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/bold-brew-official-project-bluefin-tui.html">Bold Brew Named Official Homebrew TUI for Project Bluefin</a></h2>
                        <p class="excerpt">Bold Brew becomes the official Terminal UI for managing Homebrew in Project Bluefin, a next-generation Linux desktop serving tens of thousands of users worldwide.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/bold-brew-official-project-bluefin-tui.html" class="read-more">Read more →</a>
                    </article>
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-04-12</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/top-homebrew-packages-for-developers.html">Top 20 Homebrew Packages for Developers in 2024</a></h2>
                        <p class="excerpt">Discover essential Homebrew packages for macOS developers. A curated list of the best development tools every programmer should install.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/top-homebrew-packages-for-developers.html" class="read-more">Read more →</a>
                    </article>
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-03-29</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/essential-homebrew-commands.html">10 Essential Homebrew Commands You Should Know</a></h2>
                        <p class="excerpt">Master the most important Homebrew commands for macOS package management. Learn how to install, update, and manage packages efficiently.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/essential-homebrew-commands.html" class="read-more">Read more →</a>
                    </article>
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-03-29</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/install-homebrew-macos.html">How to Install and Configure Homebrew on macOS</a></h2>
                        <p class="excerpt">Learn how to install and configure Homebrew on macOS. A step-by-step guide to setting up the most popular package manager for macOS.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/install-homebrew-macos.html" class="read-more">Read more →</a>
                    </article>
                
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date">2025-03-29</span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="/blog/managing-homebrew-packages.html">Managing Homebrew Packages on macOS with Bold Brew</a></h2>
                        <p class="excerpt">Learn how to efficiently manage Homebrew packages on macOS using Bold Brew. Discover best practices, tips, and tricks for package management.</p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="/blog/managing-homebrew-packages.html" class="read-more">Read more →</a>
                    </article>
                
            </div>
        </div>

        <aside class="col-lg-4">
            <div class="sidebar">
                <div class="widget mb-4">
                    <h3>About Bold Brew</h3>
                    <p>Bold Brew is a modern Terminal User Interface (TUI) for managing Homebrew packages and casks on macOS and Linux.</p>
                    <a href="/#install" class="btn btn-primary">Install Now</a>
                </div>

                <div class="widget mb-4">
                    <h3>Popular Tags</h3>
                    <div class="tags">
                        <a href="#" class="tag">Homebrew</a>
                        <a href="#" class="tag">TUI</a>
                        <a href="#" class="tag">Casks</a>
                        <a href="#" class="tag">Brewfile</a>
                        <a href="#" class="tag">Package Management</a>
                        <a href="#" class="tag">Project Bluefin</a>
                    </div>
                </div>

                <div class="widget mb-4">
                    <h3>Follow Us</h3>
                    <div class="social-links">
                        <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </div>
                </div>
            </div>
        </aside>
    </div>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/install-homebrew-macos.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>How to Install and Configure Homebrew on macOS</title>
    <meta name="description" content="Learn how to install and configure Homebrew on macOS. A step-by-step guide to setting up the most popular package manager for macOS.">
    <meta name="keywords" content="Homebrew installation, macOS package manager, brew install, Homebrew setup, macOS development, package manager installation, brew configuration">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="How to Install and Configure Homebrew on macOS">
    <meta property="og:description" content="Learn how to install and configure Homebrew on macOS. A step-by-step guide to setting up the most popular package manager for macOS.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/install-homebrew-macos.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Install and Configure Homebrew on macOS">
    <meta name="twitter:description" content="Learn how to install and configure Homebrew on macOS. A step-by-step guide to setting up the most popular package manager for macOS.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/install-homebrew-macos.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/install-homebrew-macos.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/install-homebrew-macos.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        How to Install and Configure Homebrew on macOS
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>How to Install and Configure Homebrew on macOS</h1>
            <div class="meta">
                <span class="date">2025-03-29</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>How to Install and Configure Homebrew on macOS</h1>
<p>Homebrew is the most popular package manager for macOS, making it easy to install and manage software packages. In this guide, we&#39;ll walk you through the process of installing and configuring Homebrew on your Mac.</p>
<h2>Prerequisites</h2>
<p>Before installing Homebrew, make sure you have:</p>
<ul>
<li>macOS 10.15 or later</li>
<li>Command Line Tools for Xcode installed</li>
<li>A stable internet connection</li>
</ul>
<h2>Installation Steps</h2>
<ol>
<li>First, install the Command Line Tools for Xcode:</li>
</ol>
<pre><code class="language-bash">xcode-select --install
</code></pre>
<ol start="2">
<li>Install Homebrew by running this command in Terminal:</li>
</ol>
<pre><code class="language-bash">/bin/bash -c &quot;$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)&quot;
</code></pre>
<ol start="3">
<li>Add Homebrew to your PATH (if prompted):</li>
</ol>
<pre><code class="language-bash">echo &#39;eval &quot;$(/opt/homebrew/bin/brew shellenv)&quot;&#39; &gt;&gt; ~/.zshrc
eval &quot;$(/opt/homebrew/bin/brew shellenv)&quot;
</code></pre>
<h2>Verify Installation</h2>
<p>Check if Homebrew is installed correctly:</p>
<pre><code class="language-bash">brew --version
</code></pre>
<h2>Basic Configuration</h2>
<ol>
<li>Update Homebrew:</li>
</ol>
<pre><code class="language-bash">brew update
</code></pre>
<ol start="2">
<li>Upgrade all packages:</li>
</ol>
<pre><code class="language-bash">brew upgrade
</code></pre>
<ol start="3">
<li>Check system status:</li>
</ol>
<pre><code class="language-bash">brew doctor
</code></pre>
<h2>Common Issues and Solutions</h2>
<ol>
<li><p><strong>Permission Issues</strong></p>
<ul>
<li>If you encounter permission errors, run:</li>
</ul>
<pre><code class="language-bash">sudo chown -R $(whoami) /opt/homebrew
</code></pre>
</li>
<li><p><strong>Slow Downloads</strong></p>
<ul>
<li>Consider using a mirror:</li>
</ul>
<pre><code class="language-bash">export HOMEBREW_BREW_GIT_REMOTE=&quot;https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git&quot;
export HOMEBREW_CORE_GIT_REMOTE=&quot;https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git&quot;
</code></pre>
</li>
<li><p><strong>Network Issues</strong></p>
<ul>
<li>Check your internet connection</li>
<li>Try using a VPN if needed</li>
</ul>
</li>
</ol>
<h2>Next Steps</h2>
<p>Now that you have Homebrew installed, you can:</p>
<ol>
<li>Install packages using <code>brew install</code></li>
<li>Search for packages using <code>brew search</code></li>
<li>Update packages using <code>brew upgrade</code></li>
<li>Remove packages using <code>brew uninstall</code></li>
</ol>
<p>For a more intuitive package management experience, consider using <a href="https://bold-brew.com">Bold Brew</a>, a modern Terminal User Interface (TUI) for Homebrew.</p>
<h2>Conclusion</h2>
<p>Homebrew is an essential tool for macOS users, making it easy to install and manage software packages. With proper installation and configuration, you&#39;ll have a powerful package manager at your disposal.</p>
<p>Remember to keep Homebrew updated and run <code>brew doctor</code> regularly to maintain a healthy installation. </p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/managing-homebrew-packages.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Managing Homebrew Packages on macOS with Bold Brew</title>
    <meta name="description" content="Learn how to efficiently manage Homebrew packages on macOS using Bold Brew. Discover best practices, tips, and tricks for package management.">
    <meta name="keywords" content="Homebrew, package management, macOS, Bold Brew, bbrew, terminal, package manager, TUI, terminal user interface, brew packages">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Managing Homebrew Packages on macOS with Bold Brew">
    <meta property="og:description" content="Learn how to efficiently manage Homebrew packages on macOS using Bold Brew. Discover best practices, tips, and tricks for package management.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/managing-homebrew-packages.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Managing Homebrew Packages on macOS with Bold Brew">
    <meta name="twitter:description" content="Learn how to efficiently manage Homebrew packages on macOS using Bold Brew. Discover best practices, tips, and tricks for package management.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/managing-homebrew-packages.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/managing-homebrew-packages.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/managing-homebrew-packages.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        Managing Homebrew Packages on macOS with Bold Brew
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>Managing Homebrew Packages on macOS with Bold Brew</h1>
            <div class="meta">
                <span class="date">2025-03-29</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>Managing Homebrew Packages on macOS with Bold Brew</h1>
<p>Managing Homebrew packages through the command line can be challenging, especially when dealing with multiple packages or complex dependencies. Bold Brew provides a modern Terminal User Interface (TUI) that makes package management more intuitive and efficient.</p>
<h2>Why Use Bold Brew?</h2>
<p>Bold Brew offers several advantages over traditional command-line package management:</p>
<ol>
<li><p><strong>Visual Interface</strong></p>
<ul>
<li>Easy-to-read package lists</li>
<li>Clear dependency visualization</li>
<li>Intuitive navigation</li>
</ul>
</li>
<li><p><strong>Efficient Workflow</strong></p>
<ul>
<li>Quick package search</li>
<li>One-click installation/removal</li>
<li>Batch operations</li>
</ul>
</li>
<li><p><strong>Better Organization</strong></p>
<ul>
<li>Group packages by category</li>
<li>Track package status</li>
<li>Monitor system health</li>
</ul>
</li>
</ol>
<h2>Installation</h2>
<p>Install Bold Brew using Homebrew:</p>
<pre><code class="language-bash">brew install Valkyrie00/homebrew-bbrew/bbrew
</code></pre>
<h2>Key Features</h2>
<h3>1. Package Search</h3>
<ul>
<li>Real-time search as you type</li>
<li>Filter by name, description, or category</li>
<li>View package details before installation</li>
</ul>
<h3>2. Package Management</h3>
<ul>
<li>Install/remove packages with a single keypress</li>
<li>Update packages individually or in bulk</li>
<li>View package dependencies</li>
</ul>
<h3>3. System Monitoring</h3>
<ul>
<li>Check Homebrew system status</li>
<li>Monitor disk usage</li>
<li>View installation logs</li>
</ul>
<h3>4. User Interface</h3>
<ul>
<li>Keyboard-driven navigation</li>
<li>Color-coded status indicators</li>
<li>Contextual help</li>
</ul>
<h2>Best Practices</h2>
<ol>
<li><p><strong>Regular Updates</strong></p>
<ul>
<li>Keep packages up to date</li>
<li>Monitor for outdated packages</li>
<li>Check system health regularly</li>
</ul>
</li>
<li><p><strong>Package Organization</strong></p>
<ul>
<li>Group related packages</li>
<li>Track package purposes</li>
<li>Maintain a clean system</li>
</ul>
</li>
<li><p><strong>Dependency Management</strong></p>
<ul>
<li>Review dependencies before installation</li>
<li>Clean up orphaned packages</li>
<li>Monitor disk usage</li>
</ul>
</li>
</ol>
<h2>Tips and Tricks</h2>
<ol>
<li><p><strong>Keyboard Shortcuts</strong></p>
<ul>
<li><code>?</code> - Show help</li>
<li><code>q</code> - Quit</li>
<li><code>space</code> - Select/deselect</li>
<li><code>enter</code> - Execute action</li>
</ul>
</li>
<li><p><strong>Search Tips</strong></p>
<ul>
<li>Use partial matches</li>
<li>Filter by category</li>
<li>Sort by various criteria</li>
</ul>
</li>
<li><p><strong>Maintenance</strong></p>
<ul>
<li>Regular cleanup</li>
<li>System health checks</li>
<li>Package updates</li>
</ul>
</li>
</ol>
<h2>Conclusion</h2>
<p>Bold Brew transforms Homebrew package management from a command-line chore into an intuitive, visual experience. Whether you&#39;re a casual user or a power user, Bold Brew can help you manage your Homebrew packages more efficiently.</p>
<p>For more information, visit the <a href="https://bold-brew.com">Bold Brew documentation</a> or check out our other guides on Homebrew management. </p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `brain/knowledge/docs_legacy/blog/top-homebrew-packages-for-developers.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 20 Homebrew Packages for Developers in 2024</title>
    <meta name="description" content="Discover essential Homebrew packages for macOS developers. A curated list of the best development tools every programmer should install.">
    <meta name="keywords" content="Homebrew packages, macOS developer tools, best Homebrew packages, CLI tools, developer tools, Bold Brew, bbrew">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="Top 20 Homebrew Packages for Developers in 2024">
    <meta property="og:description" content="Discover essential Homebrew packages for macOS developers. A curated list of the best development tools every programmer should install.">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="https://bold-brew.com/blog/top-homebrew-packages-for-developers.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Top 20 Homebrew Packages for Developers in 2024">
    <meta name="twitter:description" content="Discover essential Homebrew packages for macOS developers. A curated list of the best development tools every programmer should install.">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="https://bold-brew.com/blog/top-homebrew-packages-for-developers.html">
    <link rel="alternate" hreflang="en" href="https://bold-brew.com/blog/top-homebrew-packages-for-developers.html">
    <link rel="alternate" hreflang="x-default" href="https://bold-brew.com/blog/top-homebrew-packages-for-developers.html">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>

    <main class="container my-5">
    
        <div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            
                <div class="breadcrumb-item ">
                    
                        <a href="/">Home</a>
                    
                </div>
            
                <div class="breadcrumb-item ">
                    
                        <a href="/blog/">Blog</a>
                    
                </div>
            
                <div class="breadcrumb-item active">
                    
                        Top 20 Homebrew Packages for Developers in 2024
                    
                </div>
            
        </div>
    </nav>
</div> 
    

    <article>
        <header class="mb-5">
            <h1>Top 20 Homebrew Packages for Developers in 2024</h1>
            <div class="meta">
                <span class="date">2025-04-12</span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <h1>Top 20 Homebrew Packages for Developers in 2024</h1>
<p>Homebrew has revolutionized how developers install and manage software on macOS. In this article, we&#39;ll explore the 20 most useful Homebrew packages for developers in 2024, and how Bold Brew can make their management even easier.</p>
<h2>Version Control and Management Tools</h2>
<h3>1. git</h3>
<p>The most widely used version control system in the world, essential for any developer.</p>
<pre><code class="language-bash">brew install git
</code></pre>
<h3>2. git-lfs</h3>
<p>Git extension for managing large files.</p>
<pre><code class="language-bash">brew install git-lfs
</code></pre>
<h3>3. tig</h3>
<p>A text interface for navigating Git repositories.</p>
<pre><code class="language-bash">brew install tig
</code></pre>
<h2>Shell and Terminal</h2>
<h3>4. zsh</h3>
<p>A powerful shell with numerous additional features compared to bash.</p>
<pre><code class="language-bash">brew install zsh
</code></pre>
<h3>5. tmux</h3>
<p>A terminal multiplexer that allows you to manage multiple sessions in a single window.</p>
<pre><code class="language-bash">brew install tmux
</code></pre>
<h3>6. oh-my-zsh</h3>
<p>Framework for managing zsh configuration (installable after zsh).</p>
<pre><code class="language-bash">sh -c &quot;$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)&quot;
</code></pre>
<h2>Databases</h2>
<h3>7. postgresql</h3>
<p>A powerful open-source SQL database.</p>
<pre><code class="language-bash">brew install postgresql
</code></pre>
<h3>8. mysql</h3>
<p>The popular relational database management system.</p>
<pre><code class="language-bash">brew install mysql
</code></pre>
<h3>9. redis</h3>
<p>In-memory NoSQL database for high-performance caching.</p>
<pre><code class="language-bash">brew install redis
</code></pre>
<h2>Programming Languages and Runtimes</h2>
<h3>10. node</h3>
<p>JavaScript runtime based on Chrome&#39;s V8 for backend development.</p>
<pre><code class="language-bash">brew install node
</code></pre>
<h3>11. python</h3>
<p>Versatile programming language for data science, web development, and automation.</p>
<pre><code class="language-bash">brew install python
</code></pre>
<h3>12. go</h3>
<p>Google&#39;s language known for performance and efficiency.</p>
<pre><code class="language-bash">brew install go
</code></pre>
<h2>Network Utilities</h2>
<h3>13. wget</h3>
<p>Utility for downloading content from the web.</p>
<pre><code class="language-bash">brew install wget
</code></pre>
<h3>14. curl</h3>
<p>Tool for transferring data with URLs.</p>
<pre><code class="language-bash">brew install curl
</code></pre>
<h3>15. nmap</h3>
<p>Powerful network scanning tool.</p>
<pre><code class="language-bash">brew install nmap
</code></pre>
<h2>Productivity Tools</h2>
<h3>16. fzf</h3>
<p>Command-line fuzzy finder for quick searches.</p>
<pre><code class="language-bash">brew install fzf
</code></pre>
<h3>17. ripgrep (rg)</h3>
<p>An incredibly fast alternative to grep.</p>
<pre><code class="language-bash">brew install ripgrep
</code></pre>
<h3>18. htop</h3>
<p>Enhanced interactive system monitor.</p>
<pre><code class="language-bash">brew install htop
</code></pre>
<h2>Containerization</h2>
<h3>19. docker</h3>
<p>Platform for developing, shipping, and running containerized applications.</p>
<pre><code class="language-bash">brew install --cask docker
</code></pre>
<h3>20. kubernetes-cli</h3>
<p>CLI tool for managing Kubernetes clusters.</p>
<pre><code class="language-bash">brew install kubernetes-cli
</code></pre>
<h2>The Package Management Challenge</h2>
<p>While these tools are powerful, managing a growing number of Homebrew packages through the command line can become complicated:</p>
<ul>
<li>Forgetting which packages are installed</li>
<li>Losing track of available updates</li>
<li>Difficulty finding and removing unused packages</li>
<li>Confusion between dependencies and main packages</li>
</ul>
<h2>Bold Brew: An Elegant Solution</h2>
<p>Bold Brew (bbrew) solves these challenges by offering an elegant TUI (Terminal User Interface) for managing your Homebrew packages:</p>
<h3>Advantages of Bold Brew</h3>
<ol>
<li><strong>Intuitive Visualization</strong> - See all installed packages in an organized interface</li>
<li><strong>Simplified Updates</strong> - Update single or multiple packages with a few keystrokes</li>
<li><strong>Instant Search</strong> - Find new packages in real-time as you type</li>
<li><strong>Clear Dependencies</strong> - Graphical display of package relationships</li>
<li><strong>Efficient Management</strong> - Install and uninstall packages without memorizing commands</li>
</ol>
<h3>Installing Bold Brew</h3>
<p>You can install Bold Brew with a simple command:</p>
<pre><code class="language-bash">brew install Valkyrie00/homebrew-bbrew/bbrew
</code></pre>
<p>Once installed, simply run:</p>
<pre><code class="language-bash">bbrew
</code></pre>
<h2>Installation Workflow with Bold Brew</h2>
<p>With Bold Brew, installing the 20 packages mentioned above becomes incredibly simple:</p>
<ol>
<li>Start Bold Brew with <code>bbrew</code></li>
<li>Press <code>/</code> to search for a package</li>
<li>Navigate with arrows and select with <code>space</code></li>
<li>Press <code>i</code> to install selected packages</li>
</ol>
<p>With this intuitive interface, you can manage dozens of packages in half the time required by the traditional command line.</p>
<h2>Conclusion</h2>
<p>The Homebrew packages listed in this article are essential tools for any macOS developer in 2024. To manage them efficiently, Bold Brew offers a superior user experience that will save you time and frustration.</p>
<p>If you haven&#39;t already, try Bold Brew today:</p>
<pre><code class="language-bash">brew install Valkyrie00/homebrew-bbrew/bbrew
</code></pre>
<p>Discover a more elegant and productive way to interact with Homebrew, and focus on what really matters: writing exceptional code.</p>
<p><strong>Do you have other favorite Homebrew packages that you think should be on the list? Share them in the comments below!</strong></p>

        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>

    <footer>
    <div class="container">
        <p>&copy; 2025 Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `examples/all.brewfile`
```
# Test Brewfile for bbrew
# A simple example to test Brewfile mode functionality
# Usage: bbrew -f test.brewfile

# Command-line utilities (lightweight and common)
brew "wget"
brew "curl"
brew "tree"
brew "htop"
brew "jq"

# Development tools
brew "git"
brew "node"

# Popular editors and IDEs
cask "visual-studio-code"
cask "sublime-text"

# Alternative browsers (for testing)
cask "firefox"
cask "brave-browser"

```

## File: `examples/ide.Brewfile`
```
tap "ublue-os/tap"

cask "jetbrains-toolbox-linux"
cask "lm-studio-linux"
cask "visual-studio-code-linux"
cask "vscodium-linux"
```

## File: `internal/models/brewfile.go`
```go
package models

// BrewfileEntry represents a single entry from a Brewfile
type BrewfileEntry struct {
	Name   string
	IsCask bool
}

// BrewfileResult contains all parsed entries from a Brewfile
type BrewfileResult struct {
	Taps     []string        // List of taps to install
	Packages []BrewfileEntry // List of packages (formulae and casks)
}
```

## File: `internal/models/cask.go`
```go
package models

// Cask represents a Homebrew cask (GUI application).
type Cask struct {
	Token                 string             `json:"token"`
	FullToken             string             `json:"full_token"`
	OldTokens             []string           `json:"old_tokens"`
	Tap                   string             `json:"tap"`
	Name                  []string           `json:"name"`
	Description           string             `json:"desc"`
	Homepage              string             `json:"homepage"`
	URL                   string             `json:"url"`
	Version               string             `json:"version"`
	Installed             *string            `json:"installed"`      // Null if not installed, version string if installed
	InstalledTime         *int64             `json:"installed_time"` // Unix timestamp
	Outdated              bool               `json:"outdated"`
	SHA256                string             `json:"sha256"`
	Deprecated            bool               `json:"deprecated"`
	DeprecationDate       interface{}        `json:"deprecation_date"`
	DeprecationReason     interface{}        `json:"deprecation_reason"`
	Disabled              bool               `json:"disabled"`
	DisableDate           interface{}        `json:"disable_date"`
	DisableReason         interface{}        `json:"disable_reason"`
	TapGitHead            string             `json:"tap_git_head"`
	RubySourcePath        string             `json:"ruby_source_path"`
	RubySourceChecksum    RubySourceChecksum `json:"ruby_source_checksum"`
	Analytics90dRank      int                // Internal: Populated from analytics
	Analytics90dDownloads int                // Internal: Populated from analytics
	LocallyInstalled      bool               `json:"-"` // Internal flag
	IsCask                bool               `json:"-"` // Internal flag to distinguish from formulae
}
```

## File: `internal/models/formula.go`
```go
package models

//type Formulae []Formula

type Formula struct {
	Name                    string        `json:"name"`
	FullName                string        `json:"full_name"`
	Tap                     string        `json:"tap"`
	OldNames                []string      `json:"oldnames"`
	Aliases                 []string      `json:"aliases"`
	VersionedFormulae       []string      `json:"versioned_formulae"`
	Description             string        `json:"desc"`
	License                 string        `json:"license"`
	Homepage                string        `json:"homepage"`
	Versions                Versions      `json:"versions"`
	Urls                    Urls          `json:"urls"`
	Revision                int           `json:"revision"`
	VersionScheme           int           `json:"version_scheme"`
	Bottle                  Bottle        `json:"bottle"`
	PourBottleOnlyIf        interface{}   `json:"pour_bottle_only_if"`
	KegOnly                 bool          `json:"keg_only"`
	KegOnlyReason           interface{}   `json:"keg_only_reason"`
	Options                 []interface{} `json:"options"`
	BuildDependencies       []string      `json:"build_dependencies"`
	Dependencies            []string      `json:"dependencies"`
	TestDependencies        []interface{} `json:"test_dependencies"`
	RecommendedDependencies []interface{} `json:"recommended_dependencies"`
	OptionalDependencies    []interface{} `json:"optional_dependencies"`
	//UsesFromMacOS           []string              `json:"uses_from_macos"`
	//UsesFromMacOSBounds     []UsesFromMacOSBounds `json:"uses_from_macos_bounds"`
	Requirements           []interface{}      `json:"requirements"`
	ConflictsWith          []interface{}      `json:"conflicts_with"`
	ConflictsWithReasons   []interface{}      `json:"conflicts_with_reasons"`
	LinkOverwrite          []interface{}      `json:"link_overwrite"`
	Caveats                interface{}        `json:"caveats"`
	Installed              []Installed        `json:"installed"`
	LinkedKeg              string             `json:"linked_keg"`
	Pinned                 bool               `json:"pinned"`
	Outdated               bool               `json:"outdated"`
	Deprecated             bool               `json:"deprecated"`
	DeprecationDate        interface{}        `json:"deprecation_date"`
	DeprecationReason      interface{}        `json:"deprecation_reason"`
	DeprecationReplacement interface{}        `json:"deprecation_replacement"`
	Disabled               bool               `json:"disabled"`
	DisableDate            interface{}        `json:"disable_date"`
	DisableReason          interface{}        `json:"disable_reason"`
	DisableReplacement     interface{}        `json:"disable_replacement"`
	PostInstallDefined     bool               `json:"post_install_defined"`
	Service                interface{}        `json:"service"`
	TapGitHead             string             `json:"tap_git_head"`
	RubySourcePath         string             `json:"ruby_source_path"`
	RubySourceChecksum     RubySourceChecksum `json:"ruby_source_checksum"`
	Analytics90dRank       int
	Analytics90dDownloads  int
	LocallyInstalled       bool   `json:"-"` // Internal flag to indicate if the formula is installed locally [internal use]
	LocalPath              string `json:"-"` // Internal path to the formula in the local Homebrew Cellar [internal use]
}

type Analytics struct {
	Category   string          `json:"category"`
	TotalItems int             `json:"total_items"`
	StartDate  interface{}     `json:"start_date"`
	EndDate    interface{}     `json:"end_date"`
	TotalCount int             `json:"total_count"`
	Items      []AnalyticsItem `json:"items"`
}

type AnalyticsItem struct {
	Number  int    `json:"number"`
	Formula string `json:"formula"` // For formula analytics
	Cask    string `json:"cask"`    // For cask analytics
	Count   string `json:"count"`
	Percent string `json:"percent"`
}

type Versions struct {
	Stable string `json:"stable"`
	Head   string `json:"head"`
	Bottle bool   `json:"bottle"`
}

type Urls struct {
	Stable URL `json:"stable"`
	Head   URL `json:"head"`
}

type URL struct {
	URL      string      `json:"url"`
	Tag      interface{} `json:"tag"`
	Revision interface{} `json:"revision"`
	Using    interface{} `json:"using"`
	Checksum string      `json:"checksum"`
	Branch   string      `json:"branch"`
}

type Bottle struct {
	Stable BottleStable `json:"stable"`
}

type BottleStable struct {
	Rebuild int                   `json:"rebuild"`
	RootURL string                `json:"root_url"`
	Files   map[string]BottleFile `json:"files"`
}

type BottleFile struct {
	Cellar string `json:"cellar"`
	URL    string `json:"url"`
	Sha256 string `json:"sha256"`
}

type UsesFromMacOSBounds struct {
}

type Installed struct {
	Version               string              `json:"version"`
	UsedOptions           []interface{}       `json:"used_options"`
	BuiltAsBottle         bool                `json:"built_as_bottle"`
	PouredFromBottle      bool                `json:"poured_from_bottle"`
	Time                  int64               `json:"time"`
	RuntimeDependencies   []RuntimeDependency `json:"runtime_dependencies"`
	InstalledAsDependency bool                `json:"installed_as_dependency"`
	InstalledOnRequest    bool                `json:"installed_on_request"`
}

type RuntimeDependency struct {
	FullName         string `json:"full_name"`
	Version          string `json:"version"`
	Revision         int    `json:"revision"`
	PkgVersion       string `json:"pkg_version"`
	DeclaredDirectly bool   `json:"declared_directly"`
}

type RubySourceChecksum struct {
	Sha256 string `json:"sha256"`
}
```

## File: `internal/models/package.go`
```go
package models

// PackageType distinguishes between formulae and casks.
type PackageType string

const (
	PackageTypeFormula PackageType = "formula"
	PackageTypeCask    PackageType = "cask"
)

// Package represents a unified view of both Formula and Cask for UI display.
type Package struct {
	// Common fields
	Name                  string      // Formula.Name or Cask.Token
	DisplayName           string      // Formula.FullName or Cask.Name[0]
	Description           string      // desc
	Homepage              string      // homepage
	Version               string      // versions.stable or version
	LocallyInstalled      bool        // Is installed locally
	Outdated              bool        // Needs update
	Type                  PackageType // formula or cask
	Analytics90dRank      int
	Analytics90dDownloads int

	// Original data (for operations)
	Formula *Formula `json:"-"` // nil if Type == cask
	Cask    *Cask    `json:"-"` // nil if Type == formula

	// For leaves filter (only meaningful for formulae)
	InstalledOnRequest bool
}

// NewPackageFromFormula creates a Package from a Formula.
func NewPackageFromFormula(f *Formula) Package {
	installedOnRequest := false
	if len(f.Installed) > 0 {
		installedOnRequest = f.Installed[0].InstalledOnRequest
	}

	return Package{
		Name:                  f.Name,
		DisplayName:           f.FullName,
		Description:           f.Description,
		Homepage:              f.Homepage,
		Version:               f.Versions.Stable,
		LocallyInstalled:      f.LocallyInstalled,
		Outdated:              f.Outdated,
		Type:                  PackageTypeFormula,
		Analytics90dRank:      f.Analytics90dRank,
		Analytics90dDownloads: f.Analytics90dDownloads,
		Formula:               f,
		Cask:                  nil,
		InstalledOnRequest:    installedOnRequest,
	}
}

// NewPackageFromCask creates a Package from a Cask.
func NewPackageFromCask(c *Cask) Package {
	displayName := c.Token
	if len(c.Name) > 0 {
		displayName = c.Name[0]
	}

	return Package{
		Name:                  c.Token,
		DisplayName:           displayName,
		Description:           c.Description,
		Homepage:              c.Homepage,
		Version:               c.Version,
		LocallyInstalled:      c.LocallyInstalled,
		Outdated:              c.Outdated,
		Type:                  PackageTypeCask,
		Analytics90dRank:      c.Analytics90dRank,
		Analytics90dDownloads: c.Analytics90dDownloads,
		Formula:               nil,
		Cask:                  c,
		InstalledOnRequest:    true, // Casks are always explicitly installed
	}
}
```

## File: `internal/services/app.go`
```go
package services

import (
	"bbrew/internal/models"
	"bbrew/internal/ui"
	"bbrew/internal/ui/theme"
	"context"
	"fmt"
	"os"
	"time"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

var (
	AppName    = "Bold Brew"
	AppVersion = "0.0.1"
)

type AppServiceInterface interface {
	GetApp() *tview.Application
	GetLayout() ui.LayoutInterface
	Boot() (err error)
	BuildApp()
	SetBrewfilePath(path string)
	IsBrewfileMode() bool
	GetBrewfilePackages() *[]models.Package
}

// AppService manages the application state, Homebrew integration, and UI components.
type AppService struct {
	app    *tview.Application
	theme  *theme.Theme
	layout ui.LayoutInterface

	packages         *[]models.Package
	filteredPackages *[]models.Package
	activeFilter     FilterType
	brewVersion      string

	// Brewfile support
	brewfilePath     string
	brewfilePackages *[]models.Package
	brewfileTaps     []string // Taps required by the Brewfile

	brewService       BrewServiceInterface
	dataProvider      DataProviderInterface // Direct access for Brewfile operations
	selfUpdateService SelfUpdateServiceInterface
	inputService      InputServiceInterface
}

// NewAppService creates a new instance of AppService with initialized components.
var NewAppService = func() AppServiceInterface {
	app := tview.NewApplication()
	themeService := theme.NewTheme()
	layout := ui.NewLayout(themeService)

	s := &AppService{
		app:    app,
		theme:  themeService,
		layout: layout,

		packages:         new([]models.Package),
		filteredPackages: new([]models.Package),
		activeFilter:     FilterNone,
		brewVersion:      "-",

		brewfilePath:     "",
		brewfilePackages: new([]models.Package),
	}

	// Initialize services
	s.dataProvider = NewDataProvider()
	s.brewService = NewBrewService()
	s.inputService = NewInputService(s, s.brewService)
	s.selfUpdateService = NewSelfUpdateService()

	return s
}

func (s *AppService) GetApp() *tview.Application             { return s.app }
func (s *AppService) GetLayout() ui.LayoutInterface          { return s.layout }
func (s *AppService) SetBrewfilePath(path string)            { s.brewfilePath = path }
func (s *AppService) IsBrewfileMode() bool                   { return s.brewfilePath != "" }
func (s *AppService) GetBrewfilePackages() *[]models.Package { return s.brewfilePackages }

// Boot initializes the application by setting up Homebrew and loading formulae data.
func (s *AppService) Boot() (err error) {
	if s.brewVersion, err = s.brewService.GetBrewVersion(); err != nil {
		// This error is critical, as we need Homebrew to function
		return fmt.Errorf("failed to get Homebrew version: %v", err)
	}

	// Load Homebrew data from cache for fast startup
	// Installation status might be stale but will be refreshed in background by updateHomeBrew()
	if err = s.dataProvider.SetupData(false); err != nil {
		// Log error but don't fail - app can work with empty/partial data
		fmt.Fprintf(os.Stderr, "Warning: failed to load Homebrew data (will retry in background): %v\n", err)
	}

	// Initialize packages and filteredPackages
	s.packages = s.dataProvider.GetPackages()
	*s.filteredPackages = *s.packages

	// If Brewfile is specified, parse it and filter packages
	if s.IsBrewfileMode() {
		if err = s.loadBrewfilePackages(); err != nil {
			return fmt.Errorf("failed to load Brewfile: %v", err)
		}
	}

	return nil
}

// updateHomeBrew updates the Homebrew formulae and refreshes the results in the UI.
func (s *AppService) updateHomeBrew() {
	s.app.QueueUpdateDraw(func() {
		s.layout.GetNotifier().ShowWarning("Updating Homebrew formulae...")
	})
	if err := s.brewService.UpdateHomebrew(); err != nil {
		s.app.QueueUpdateDraw(func() {
			s.layout.GetNotifier().ShowError("Could not update Homebrew formulae")
		})
		return
	}
	// Clear loading message and update results
	s.app.QueueUpdateDraw(func() {
		s.layout.GetNotifier().ShowSuccess("Homebrew formulae updated successfully")
	})
	s.forceRefreshResults()
}

// BuildApp builds the application layout, sets up event handlers, and initializes the UI components.
func (s *AppService) BuildApp() {
	// Build the layout
	s.layout.Setup()

	// Update header and enable Brewfile mode features if needed
	headerName := AppName
	if s.IsBrewfileMode() {
		headerName = fmt.Sprintf("%s [Brewfile Mode]", AppName)
		s.layout.GetSearch().Field().SetLabel("Search (Brewfile): ")
		s.inputService.EnableBrewfileMode() // Add Install All action
	}
	s.layout.GetHeader().Update(headerName, AppVersion, s.brewVersion)

	// Evaluate if there is a new version available
	// This is done in a goroutine to avoid blocking the UI during startup
	// In the future, this could be replaced with a more sophisticated update check, and update
	// the user if a new version is available instantly instead of waiting for the next app start
	go func() {
		ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
		defer cancel()

		if latestVersion, err := s.selfUpdateService.CheckForUpdates(ctx); err == nil && latestVersion != AppVersion {
			s.app.QueueUpdateDraw(func() {
				AppVersion = fmt.Sprintf("%s ([orange]New Version Available: %s[-])", AppVersion, latestVersion)
				headerName := AppName
				if s.IsBrewfileMode() {
					headerName = fmt.Sprintf("%s [Brewfile Mode]", AppName)
				}
				s.layout.GetHeader().Update(headerName, AppVersion, s.brewVersion)
			})
		}
	}()

	// Table handler to update the details view when a table row is selected
	tableSelectionChangedFunc := func(row, _ int) {
		if row > 0 && row-1 < len(*s.filteredPackages) {
			s.layout.GetDetails().SetContent(&(*s.filteredPackages)[row-1])
		}
	}
	s.layout.GetTable().View().SetSelectionChangedFunc(tableSelectionChangedFunc)

	// Search input handlers
	inputDoneFunc := func(key tcell.Key) {
		if key == tcell.KeyEnter || key == tcell.KeyEscape {
			s.app.SetFocus(s.layout.GetTable().View()) // Set focus back to the table on Enter or Escape
		}
	}
	changedFunc := func(text string) { // Each time the search input changes
		s.search(text, true) // Perform search and scroll to top
	}
	s.layout.GetSearch().SetHandlers(inputDoneFunc, changedFunc)

	// Add key event handler
	s.app.SetInputCapture(s.inputService.HandleKeyEventInput)

	// Set the root of the application to the layout's root and focus on the table view
	s.app.SetRoot(s.layout.Root(), true)
	s.app.SetFocus(s.layout.GetTable().View())

	// Start background tasks: install taps first (if Brewfile mode), then update Homebrew
	go func() {
		// In Brewfile mode, install missing taps first
		if s.IsBrewfileMode() && len(s.brewfileTaps) > 0 {
			s.installBrewfileTapsAtStartup()
		}
		// Then update Homebrew (which will reload all data including new taps)
		s.updateHomeBrew()
	}()

	// Set initial results based on mode
	if s.IsBrewfileMode() {
		*s.filteredPackages = *s.brewfilePackages // Sync filteredPackages
		s.setResults(s.brewfilePackages, true)    // Show only Brewfile packages
	} else {
		s.setResults(s.packages, true) // Show all packages
	}
}
```

## File: `internal/services/brew.go`
```go
package services

import (
	"bbrew/internal/models"
	"fmt"
	"io"
	"os/exec"
	"strings"
	"sync"

	"github.com/rivo/tview"
)

// BrewServiceInterface defines the contract for Homebrew operations.
// BrewService is a pure executor of brew commands - it does NOT hold data.
// For data retrieval, use DataProviderInterface.
type BrewServiceInterface interface {
	// Core info
	GetBrewVersion() (string, error)

	// Package operations
	UpdateHomebrew() error
	UpdateAllPackages(app *tview.Application, outputView *tview.TextView) error
	UpdatePackage(info models.Package, app *tview.Application, outputView *tview.TextView) error
	RemovePackage(info models.Package, app *tview.Application, outputView *tview.TextView) error
	InstallPackage(info models.Package, app *tview.Application, outputView *tview.TextView) error

	// Tap support
	InstallTap(tapName string, app *tview.Application, outputView *tview.TextView) error
	IsTapInstalled(tapName string) bool
}

// BrewService provides methods to execute Homebrew commands.
// It is a pure executor - no data storage. Use DataProvider for data.
type BrewService struct {
	brewVersion string
}

// NewBrewService creates a new instance of BrewService.
var NewBrewService = func() BrewServiceInterface {
	return &BrewService{}
}

// GetBrewVersion retrieves the version of Homebrew installed on the system, caching it for future calls.
func (s *BrewService) GetBrewVersion() (string, error) {
	if s.brewVersion != "" {
		return s.brewVersion, nil
	}

	cmd := exec.Command("brew", "--version")
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}

	s.brewVersion = strings.TrimSpace(string(output))
	return s.brewVersion, nil
}

// UpdateHomebrew updates the Homebrew package manager by running the `brew update` command.
func (s *BrewService) UpdateHomebrew() error {
	cmd := exec.Command("brew", "update")
	return cmd.Run()
}

// UpdateAllPackages upgrades all outdated packages.
func (s *BrewService) UpdateAllPackages(app *tview.Application, outputView *tview.TextView) error {
	cmd := exec.Command("brew", "upgrade") // #nosec G204
	return s.executeCommand(app, cmd, outputView)
}

// UpdatePackage upgrades a specific package.
func (s *BrewService) UpdatePackage(info models.Package, app *tview.Application, outputView *tview.TextView) error {
	var cmd *exec.Cmd
	if info.Type == models.PackageTypeCask {
		cmd = exec.Command("brew", "upgrade", "--cask", info.Name) // #nosec G204
	} else {
		cmd = exec.Command("brew", "upgrade", info.Name) // #nosec G204
	}
	return s.executeCommand(app, cmd, outputView)
}

// RemovePackage uninstalls a package.
func (s *BrewService) RemovePackage(info models.Package, app *tview.Application, outputView *tview.TextView) error {
	var cmd *exec.Cmd
	if info.Type == models.PackageTypeCask {
		cmd = exec.Command("brew", "uninstall", "--cask", info.Name) // #nosec G204
	} else {
		cmd = exec.Command("brew", "uninstall", info.Name) // #nosec G204
	}
	return s.executeCommand(app, cmd, outputView)
}

// InstallPackage installs a package.
func (s *BrewService) InstallPackage(info models.Package, app *tview.Application, outputView *tview.TextView) error {
	var cmd *exec.Cmd
	if info.Type == models.PackageTypeCask {
		cmd = exec.Command("brew", "install", "--cask", info.Name) // #nosec G204
	} else {
		cmd = exec.Command("brew", "install", info.Name) // #nosec G204
	}
	return s.executeCommand(app, cmd, outputView)
}

// InstallTap installs a Homebrew tap.
func (s *BrewService) InstallTap(tapName string, app *tview.Application, outputView *tview.TextView) error {
	cmd := exec.Command("brew", "tap", tapName) // #nosec G204
	return s.executeCommand(app, cmd, outputView)
}

// IsTapInstalled checks if a tap is already installed.
func (s *BrewService) IsTapInstalled(tapName string) bool {
	cmd := exec.Command("brew", "tap")
	output, err := cmd.Output()
	if err != nil {
		return false
	}

	taps := strings.Split(strings.TrimSpace(string(output)), "\n")
	for _, tap := range taps {
		if strings.TrimSpace(tap) == tapName {
			return true
		}
	}
	return false
}

// executeCommand runs a command and captures its output, updating the provided TextView.
func (s *BrewService) executeCommand(
	app *tview.Application,
	cmd *exec.Cmd,
	outputView *tview.TextView,
) error {
	stdoutPipe, stdoutWriter := io.Pipe()
	stderrPipe, stderrWriter := io.Pipe()
	cmd.Stdout = stdoutWriter
	cmd.Stderr = stderrWriter

	if err := cmd.Start(); err != nil {
		return err
	}

	var wg sync.WaitGroup
	wg.Add(3)

	cmdErrCh := make(chan error, 1)

	go func() {
		defer wg.Done()
		defer stdoutWriter.Close()
		defer stderrWriter.Close()
		cmdErrCh <- cmd.Wait()
	}()

	go func() {
		defer wg.Done()
		defer stdoutPipe.Close()
		buf := make([]byte, 1024)
		for {
			n, err := stdoutPipe.Read(buf)
			if n > 0 {
				output := make([]byte, n)
				copy(output, buf[:n])
				app.QueueUpdateDraw(func() {
					_, _ = outputView.Write(output) // #nosec G104
					outputView.ScrollToEnd()
				})
			}
			if err != nil {
				if err != io.EOF {
					app.QueueUpdateDraw(func() {
						fmt.Fprintf(outputView, "\nError: %v\n", err)
					})
				}
				break
			}
		}
	}()

	go func() {
		defer wg.Done()
		defer stderrPipe.Close()
		buf := make([]byte, 1024)
		for {
			n, err := stderrPipe.Read(buf)
			if n > 0 {
				output := make([]byte, n)
				copy(output, buf[:n])
				app.QueueUpdateDraw(func() {
					_, _ = outputView.Write(output) // #nosec G104
					outputView.ScrollToEnd()
				})
			}
			if err != nil {
				if err != io.EOF {
					app.QueueUpdateDraw(func() {
						fmt.Fprintf(outputView, "\nError: %v\n", err)
					})
				}
				break
			}
		}
	}()

	wg.Wait()

	return <-cmdErrCh
}
```

## File: `internal/services/brewfile.go`
```go
// Package services provides Brewfile support for Bold Brew.
//
// This file handles parsing Brewfile entries (taps, formulae, casks),
// loading packages from third-party taps, and installing missing taps
// at application startup.
//
// NOTE: These methods are only active in Brewfile mode (bbrew -f <file>).
// In normal mode, these functions are not called.
//
// Execution sequence (Brewfile mode only):
//
//  1. Boot() → loadBrewfilePackages()
//     Initial load using cached tap data for fast startup.
//
//  2. BuildApp() → goroutine:
//     a) installBrewfileTapsAtStartup()
//     Installs any missing taps from the Brewfile.
//     b) updateHomeBrew() → forceRefreshResults()
//     Refreshes Homebrew data and reloads packages.
//
//  3. forceRefreshResults() → fetchTapPackages() + loadBrewfilePackages()
//     Fetches fresh tap package info and rebuilds the package list.
package services

import (
	"bbrew/internal/models"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

// ResolveBrewfilePath resolves a Brewfile path which can be local or a remote URL.
// Returns the local file path and a cleanup function to call when done.
// For local files, cleanup is a no-op. For remote files, cleanup removes the temp file.
func ResolveBrewfilePath(pathOrURL string) (localPath string, cleanup func(), err error) {
	// Check if it's a remote URL (HTTPS only for security)
	if strings.HasPrefix(pathOrURL, "https://") {
		localPath, err = downloadBrewfile(pathOrURL)
		if err != nil {
			return "", nil, err
		}
		// Return cleanup function that removes the temp file
		cleanup = func() { os.Remove(localPath) }
		return localPath, cleanup, nil
	}

	// Local file - validate it exists
	if _, err := os.Stat(pathOrURL); os.IsNotExist(err) {
		return "", nil, fmt.Errorf("brewfile not found: %s", pathOrURL)
	} else if err != nil {
		return "", nil, fmt.Errorf("cannot access Brewfile: %w", err)
	}

	// No cleanup needed for local files
	return pathOrURL, func() {}, nil
}

// downloadBrewfile downloads a remote Brewfile to a temporary file.
func downloadBrewfile(url string) (string, error) {
	fmt.Fprintf(os.Stderr, "Downloading Brewfile from %s...\n", url)

	resp, err := http.Get(url) // #nosec G107 - URL is user-provided, HTTPS enforced
	if err != nil {
		return "", fmt.Errorf("failed to fetch URL: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("HTTP %d: %s", resp.StatusCode, resp.Status)
	}

	// Create temp file
	tempFile, err := os.CreateTemp(os.TempDir(), "bbrew-remote-*.brewfile")
	if err != nil {
		return "", fmt.Errorf("failed to create temp file: %w", err)
	}
	defer tempFile.Close()

	// Copy content
	if _, err = io.Copy(tempFile, resp.Body); err != nil {
		os.Remove(tempFile.Name())
		return "", fmt.Errorf("failed to save Brewfile: %w", err)
	}

	return filepath.Clean(tempFile.Name()), nil
}

// parseBrewfileWithTaps parses a Brewfile and returns taps and packages separately.
func parseBrewfileWithTaps(filepath string) (*models.BrewfileResult, error) {
	// #nosec G304 -- filepath is user-provided via CLI flag
	data, err := os.ReadFile(filepath)
	if err != nil {
		return nil, fmt.Errorf("failed to read Brewfile: %w", err)
	}

	result := &models.BrewfileResult{
		Taps:     []string{},
		Packages: []models.BrewfileEntry{},
	}
	lines := strings.Split(string(data), "\n")

	for _, line := range lines {
		line = strings.TrimSpace(line)

		// Skip empty lines and comments
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}

		// Parse tap entries: tap "user/repo"
		if strings.HasPrefix(line, "tap ") {
			start := strings.Index(line, "\"")
			end := strings.LastIndex(line, "\"")
			if start != -1 && end != -1 && start < end {
				tapName := line[start+1 : end]
				result.Taps = append(result.Taps, tapName)
			}
		}

		// Parse brew entries: brew "package-name"
		if strings.HasPrefix(line, "brew ") {
			start := strings.Index(line, "\"")
			end := strings.LastIndex(line, "\"")
			if start != -1 && end != -1 && start < end {
				packageName := line[start+1 : end]
				result.Packages = append(result.Packages, models.BrewfileEntry{
					Name:   packageName,
					IsCask: false,
				})
			}
		}

		// Parse cask entries: cask "package-name"
		if strings.HasPrefix(line, "cask ") {
			start := strings.Index(line, "\"")
			end := strings.LastIndex(line, "\"")
			if start != -1 && end != -1 && start < end {
				packageName := line[start+1 : end]
				result.Packages = append(result.Packages, models.BrewfileEntry{
					Name:   packageName,
					IsCask: true,
				})
			}
		}
	}

	return result, nil
}

// loadBrewfilePackages parses the Brewfile and creates a filtered package list.
// Uses the DataProvider to load tap packages from cache or fetch via brew info.
func (s *AppService) loadBrewfilePackages() error {
	result, err := parseBrewfileWithTaps(s.brewfilePath)
	if err != nil {
		return err
	}

	// Store taps for later installation
	s.brewfileTaps = result.Taps

	// Create a map for quick lookup of Brewfile entries
	packageMap := make(map[string]models.PackageType)
	for _, entry := range result.Packages {
		if entry.IsCask {
			packageMap[entry.Name] = models.PackageTypeCask
		} else {
			packageMap[entry.Name] = models.PackageTypeFormula
		}
	}

	// Track which packages were found (to avoid duplicates)
	foundPackages := make(map[string]bool)

	// Get actual installed packages (2 calls total, much faster than per-package checks)
	installedCasks := s.dataProvider.FetchInstalledCaskNames()
	installedFormulae := s.dataProvider.FetchInstalledFormulaNames()

	// Filter packages to only include those in the Brewfile
	*s.brewfilePackages = []models.Package{}
	for _, pkg := range *s.packages {
		if pkgType, exists := packageMap[pkg.Name]; exists && pkgType == pkg.Type {
			// Skip if already added (prevent duplicates)
			if foundPackages[pkg.Name] {
				continue
			}
			// Verify installation status against actual installed lists
			if pkgType == models.PackageTypeCask {
				pkg.LocallyInstalled = installedCasks[pkg.Name]
			} else {
				pkg.LocallyInstalled = installedFormulae[pkg.Name]
			}
			*s.brewfilePackages = append(*s.brewfilePackages, pkg)
			foundPackages[pkg.Name] = true
		}
	}

	// Collect entries not found in main list (tap packages)
	var tapEntries []models.BrewfileEntry
	for _, entry := range result.Packages {
		if !foundPackages[entry.Name] {
			tapEntries = append(tapEntries, entry)
		}
	}

	// Load tap packages from cache (fast startup)
	if len(tapEntries) > 0 {
		// Build existing packages map
		existingPackages := make(map[string]models.Package)
		for _, pkg := range *s.packages {
			existingPackages[pkg.Name] = pkg
		}

		// Use DataProvider to load tap packages (from cache only at startup, no fetch)
		tapPackages, _ := s.dataProvider.GetTapPackages(tapEntries, existingPackages, false)

		// Add tap packages to brewfilePackages, updating installed status (avoid duplicates)
		for _, pkg := range tapPackages {
			if foundPackages[pkg.Name] {
				continue // Already added
			}
			if pkg.Type == models.PackageTypeCask {
				pkg.LocallyInstalled = installedCasks[pkg.Name]
			} else {
				pkg.LocallyInstalled = installedFormulae[pkg.Name]
			}
			*s.brewfilePackages = append(*s.brewfilePackages, pkg)
			foundPackages[pkg.Name] = true
		}
	}

	// Sort by name for consistent display
	sort.Slice(*s.brewfilePackages, func(i, j int) bool {
		return (*s.brewfilePackages)[i].Name < (*s.brewfilePackages)[j].Name
	})

	return nil
}

// fetchTapPackages fetches info for packages from third-party taps and adds them to s.packages.
// This is called after taps are installed so that loadBrewfilePackages can find them.
// Uses the DataProvider to fetch and cache tap package data.
func (s *AppService) fetchTapPackages() {
	if !s.IsBrewfileMode() || len(s.brewfileTaps) == 0 {
		return
	}

	result, err := parseBrewfileWithTaps(s.brewfilePath)
	if err != nil {
		return
	}

	// Build a map of existing packages for quick lookup
	existingPackages := make(map[string]models.Package)
	for _, pkg := range *s.packages {
		existingPackages[pkg.Name] = pkg
	}

	// Use DataProvider to fetch all tap packages (force download to get fresh data)
	tapPackages, _ := s.dataProvider.GetTapPackages(result.Packages, existingPackages, true)

	// Add tap packages to s.packages (avoiding duplicates)
	for _, pkg := range tapPackages {
		if _, exists := existingPackages[pkg.Name]; !exists {
			*s.packages = append(*s.packages, pkg)
		}
	}
}

// installBrewfileTapsAtStartup installs any missing taps from the Brewfile at app startup.
// This runs before updateHomeBrew, which will then reload all data including the new taps.
func (s *AppService) installBrewfileTapsAtStartup() {
	// Check which taps need to be installed
	var tapsToInstall []string
	for _, tap := range s.brewfileTaps {
		if !s.brewService.IsTapInstalled(tap) {
			tapsToInstall = append(tapsToInstall, tap)
		}
	}

	if len(tapsToInstall) == 0 {
		return // All taps already installed
	}

	// Install missing taps
	for _, tap := range tapsToInstall {
		tap := tap // Create local copy for closures
		s.app.QueueUpdateDraw(func() {
			s.layout.GetNotifier().ShowWarning(fmt.Sprintf("Installing tap %s...", tap))
			fmt.Fprintf(s.layout.GetOutput().View(), "[TAP] Installing %s...\n", tap)
		})

		if err := s.brewService.InstallTap(tap, s.app, s.layout.GetOutput().View()); err != nil {
			s.app.QueueUpdateDraw(func() {
				s.layout.GetNotifier().ShowError(fmt.Sprintf("Failed to install tap %s", tap))
				fmt.Fprintf(s.layout.GetOutput().View(), "[ERROR] Failed to install tap %s\n", tap)
			})
		} else {
			s.app.QueueUpdateDraw(func() {
				s.layout.GetNotifier().ShowSuccess(fmt.Sprintf("Tap %s installed", tap))
				fmt.Fprintf(s.layout.GetOutput().View(), "[SUCCESS] tap %s installed\n", tap)
			})
		}
	}

	s.app.QueueUpdateDraw(func() {
		s.layout.GetNotifier().ShowSuccess("All taps installed")
	})
}
```

## File: `internal/services/cache.go`
```go
package services

import (
	"os"
	"path/filepath"

	"github.com/adrg/xdg"
)

// getCacheDir returns the cache directory following XDG Base Directory Specification.
func getCacheDir() string {
	return filepath.Join(xdg.CacheHome, "bbrew")
}

// ensureCacheDir creates the cache directory if it doesn't exist.
func ensureCacheDir() error {
	cacheDir := getCacheDir()
	if _, err := os.Stat(cacheDir); os.IsNotExist(err) {
		return os.MkdirAll(cacheDir, 0750)
	}
	return nil
}

// readCacheFile reads a cached file if it exists and meets minimum size requirements.
// Returns nil if cache should not be used.
func readCacheFile(filename string, minSize int64) []byte {
	cacheFile := filepath.Join(getCacheDir(), filename)
	fileInfo, err := os.Stat(cacheFile)
	if err != nil || fileInfo.Size() < minSize {
		return nil
	}
	// #nosec G304 -- cacheFile path is safely constructed from getCacheDir
	data, err := os.ReadFile(cacheFile)
	if err != nil || len(data) == 0 {
		return nil
	}
	return data
}

// writeCacheFile saves data to a cache file.
func writeCacheFile(filename string, data []byte) {
	cacheFile := filepath.Join(getCacheDir(), filename)
	_ = os.WriteFile(cacheFile, data, 0600)
}
```

## File: `internal/services/dataprovider.go`
```go
package services

import (
	"bbrew/internal/models"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os/exec"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
)

// API URLs for Homebrew data
const (
	formulaeAPIURL      = "https://formulae.brew.sh/api/formula.json"
	caskAPIURL          = "https://formulae.brew.sh/api/cask.json"
	analyticsAPIURL     = "https://formulae.brew.sh/api/analytics/install-on-request/90d.json"
	caskAnalyticsAPIURL = "https://formulae.brew.sh/api/analytics/cask-install/90d.json"
)

// Cache file names
const (
	cacheFileInstalled      = "installed.json"
	cacheFileInstalledCasks = "installed-casks.json"
	cacheFileFormulae       = "formula.json"
	cacheFileCasks          = "cask.json"
	cacheFileAnalytics      = "analytics.json"
	cacheFileCaskAnalytics  = "cask-analytics.json"
	cacheFileTapPackages    = "tap-packages.json"
)

// DataProviderInterface defines the contract for data operations.
// DataProvider is the central repository for all Homebrew package data.
type DataProviderInterface interface {
	// Setup and retrieval
	SetupData(forceRefresh bool) error
	GetPackages() *[]models.Package

	// Installation status checks (runs brew list command)
	FetchInstalledCaskNames() map[string]bool
	FetchInstalledFormulaNames() map[string]bool

	// Tap packages - gets from cache or fetches via brew info
	GetTapPackages(entries []models.BrewfileEntry, existingPackages map[string]models.Package, forceRefresh bool) ([]models.Package, error)
}

// DataProvider implements DataProviderInterface.
// It is the central repository for all Homebrew package data.
type DataProvider struct {
	// Formula lists
	installedFormulae *[]models.Formula
	remoteFormulae    *[]models.Formula
	formulaeAnalytics map[string]models.AnalyticsItem

	// Cask lists
	installedCasks *[]models.Cask
	remoteCasks    *[]models.Cask
	caskAnalytics  map[string]models.AnalyticsItem

	// Unified package list
	allPackages *[]models.Package

	prefixPath string
}

// NewDataProvider creates a new DataProvider instance with initialized data structures.
func NewDataProvider() *DataProvider {
	return &DataProvider{
		installedFormulae: new([]models.Formula),
		remoteFormulae:    new([]models.Formula),
		installedCasks:    new([]models.Cask),
		remoteCasks:       new([]models.Cask),
		allPackages:       new([]models.Package),
	}
}

// fetchFromAPI downloads data from a URL.
func fetchFromAPI(url string) ([]byte, error) {
	resp, err := http.Get(url) // #nosec G107 - URLs are internal constants
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	return io.ReadAll(resp.Body)
}

// getPrefixPath returns the Homebrew prefix path, caching it.
func (d *DataProvider) getPrefixPath() string {
	if d.prefixPath != "" {
		return d.prefixPath
	}
	cmd := exec.Command("brew", "--prefix")
	output, err := cmd.Output()
	if err != nil {
		d.prefixPath = "Unknown"
		return d.prefixPath
	}
	d.prefixPath = strings.TrimSpace(string(output))
	return d.prefixPath
}

// GetInstalledFormulae retrieves installed formulae, optionally using cache.
func (d *DataProvider) GetInstalledFormulae(forceRefresh bool) ([]models.Formula, error) {
	if err := ensureCacheDir(); err != nil {
		return nil, err
	}

	if !forceRefresh {
		if data := readCacheFile(cacheFileInstalled, 10); data != nil {
			var formulae []models.Formula
			if err := json.Unmarshal(data, &formulae); err == nil {
				d.markFormulaeAsInstalled(&formulae)
				return formulae, nil
			}
		}
	}

	cmd := exec.Command("brew", "info", "--json=v1", "--installed")
	output, err := cmd.Output()
	if err != nil {
		return nil, err
	}

	var formulae []models.Formula
	if err := json.Unmarshal(output, &formulae); err != nil {
		return nil, err
	}

	d.markFormulaeAsInstalled(&formulae)
	writeCacheFile(cacheFileInstalled, output)
	return formulae, nil
}

// markFormulaeAsInstalled sets LocallyInstalled and LocalPath for formulae.
func (d *DataProvider) markFormulaeAsInstalled(formulae *[]models.Formula) {
	prefix := d.getPrefixPath()
	for i := range *formulae {
		(*formulae)[i].LocallyInstalled = true
		(*formulae)[i].LocalPath = filepath.Join(prefix, "Cellar", (*formulae)[i].Name)
	}
}

// GetInstalledCasks retrieves installed casks, optionally using cache.
func (d *DataProvider) GetInstalledCasks(forceRefresh bool) ([]models.Cask, error) {
	if err := ensureCacheDir(); err != nil {
		return nil, err
	}

	if !forceRefresh {
		if data := readCacheFile(cacheFileInstalledCasks, 10); data != nil {
			var response struct {
				Casks []models.Cask `json:"casks"`
			}
			if err := json.Unmarshal(data, &response); err == nil {
				d.markCasksAsInstalled(&response.Casks)
				return response.Casks, nil
			}
		}
	}

	// Get list of installed cask names
	listCmd := exec.Command("brew", "list", "--cask")
	listOutput, err := listCmd.Output()
	if err != nil {
		return []models.Cask{}, nil // No casks installed
	}

	caskNames := strings.Split(strings.TrimSpace(string(listOutput)), "\n")
	if len(caskNames) == 0 || (len(caskNames) == 1 && caskNames[0] == "") {
		return []models.Cask{}, nil
	}

	// Get info for each installed cask
	args := append([]string{"info", "--json=v2", "--cask"}, caskNames...)
	infoCmd := exec.Command("brew", args...)
	infoOutput, err := infoCmd.Output()
	if err != nil {
		return []models.Cask{}, nil
	}

	var response struct {
		Casks []models.Cask `json:"casks"`
	}
	if err := json.Unmarshal(infoOutput, &response); err != nil {
		return nil, err
	}

	d.markCasksAsInstalled(&response.Casks)
	writeCacheFile(cacheFileInstalledCasks, infoOutput)
	return response.Casks, nil
}

// markCasksAsInstalled sets LocallyInstalled and IsCask for casks.
func (d *DataProvider) markCasksAsInstalled(casks *[]models.Cask) {
	for i := range *casks {
		(*casks)[i].LocallyInstalled = true
		(*casks)[i].IsCask = true
	}
}

// GetRemoteFormulae retrieves remote formulae from API, optionally using cache.
func (d *DataProvider) GetRemoteFormulae(forceRefresh bool) ([]models.Formula, error) {
	if err := ensureCacheDir(); err != nil {
		return nil, err
	}

	if !forceRefresh {
		if data := readCacheFile(cacheFileFormulae, 1000); data != nil {
			var formulae []models.Formula
			if err := json.Unmarshal(data, &formulae); err == nil && len(formulae) > 0 {
				return formulae, nil
			}
		}
	}

	body, err := fetchFromAPI(formulaeAPIURL)
	if err != nil {
		return nil, err
	}

	var formulae []models.Formula
	if err := json.Unmarshal(body, &formulae); err != nil {
		return nil, err
	}

	writeCacheFile(cacheFileFormulae, body)
	return formulae, nil
}

// GetRemoteCasks retrieves remote casks from API, optionally using cache.
func (d *DataProvider) GetRemoteCasks(forceRefresh bool) ([]models.Cask, error) {
	if err := ensureCacheDir(); err != nil {
		return nil, err
	}

	if !forceRefresh {
		if data := readCacheFile(cacheFileCasks, 1000); data != nil {
			var casks []models.Cask
			if err := json.Unmarshal(data, &casks); err == nil && len(casks) > 0 {
				return casks, nil
			}
		}
	}

	body, err := fetchFromAPI(caskAPIURL)
	if err != nil {
		return nil, err
	}

	var casks []models.Cask
	if err := json.Unmarshal(body, &casks); err != nil {
		return nil, err
	}

	writeCacheFile(cacheFileCasks, body)
	return casks, nil
}

// GetFormulaeAnalytics retrieves formulae analytics from API, optionally using cache.
func (d *DataProvider) GetFormulaeAnalytics(forceRefresh bool) (map[string]models.AnalyticsItem, error) {
	if err := ensureCacheDir(); err != nil {
		return nil, err
	}

	if !forceRefresh {
		if data := readCacheFile(cacheFileAnalytics, 100); data != nil {
			analytics := models.Analytics{}
			if err := json.Unmarshal(data, &analytics); err == nil && len(analytics.Items) > 0 {
				result := make(map[string]models.AnalyticsItem)
				for _, f := range analytics.Items {
					result[f.Formula] = f
				}
				return result, nil
			}
		}
	}

	body, err := fetchFromAPI(analyticsAPIURL)
	if err != nil {
		return nil, err
	}

	analytics := models.Analytics{}
	if err := json.Unmarshal(body, &analytics); err != nil {
		return nil, err
	}

	result := make(map[string]models.AnalyticsItem)
	for _, f := range analytics.Items {
		result[f.Formula] = f
	}

	writeCacheFile(cacheFileAnalytics, body)
	return result, nil
}

// GetCaskAnalytics retrieves cask analytics from API, optionally using cache.
func (d *DataProvider) GetCaskAnalytics(forceRefresh bool) (map[string]models.AnalyticsItem, error) {
	if err := ensureCacheDir(); err != nil {
		return nil, err
	}

	if !forceRefresh {
		if data := readCacheFile(cacheFileCaskAnalytics, 100); data != nil {
			analytics := models.Analytics{}
			if err := json.Unmarshal(data, &analytics); err == nil && len(analytics.Items) > 0 {
				result := make(map[string]models.AnalyticsItem)
				for _, c := range analytics.Items {
					if c.Cask != "" {
						result[c.Cask] = c
					}
				}
				return result, nil
			}
		}
	}

	body, err := fetchFromAPI(caskAnalyticsAPIURL)
	if err != nil {
		return nil, err
	}

	analytics := models.Analytics{}
	if err := json.Unmarshal(body, &analytics); err != nil {
		return nil, err
	}

	result := make(map[string]models.AnalyticsItem)
	for _, c := range analytics.Items {
		if c.Cask != "" {
			result[c.Cask] = c
		}
	}

	writeCacheFile(cacheFileCaskAnalytics, body)
	return result, nil
}

// GetTapPackages retrieves package info for third-party tap entries.
// It checks cache first, then fetches missing packages via `brew info`.
// Results are cached for faster subsequent lookups.
func (d *DataProvider) GetTapPackages(entries []models.BrewfileEntry, existingPackages map[string]models.Package, forceRefresh bool) ([]models.Package, error) {
	if len(entries) == 0 {
		return nil, nil
	}

	result := make([]models.Package, 0)
	foundPackages := make(map[string]bool)

	// 1. Get from cache (if not forceRefresh)
	cachedPackages := make(map[string]models.Package)
	if !forceRefresh {
		if data := readCacheFile(cacheFileTapPackages, 10); data != nil {
			var packages []models.Package
			if err := json.Unmarshal(data, &packages); err == nil {
				for _, pkg := range packages {
					cachedPackages[pkg.Name] = pkg
				}
			}
		}
	}

	// 2. Collect packages from existingPackages (already loaded from APIs)
	// and packages from cache, tracking what we still need to fetch
	var missingCasks []string
	var missingFormulae []string

	for _, entry := range entries {
		// Check if already in existingPackages (from API)
		if pkg, exists := existingPackages[entry.Name]; exists {
			result = append(result, pkg)
			foundPackages[entry.Name] = true
			continue
		}

		// Check if in cache
		if pkg, exists := cachedPackages[entry.Name]; exists {
			result = append(result, pkg)
			foundPackages[entry.Name] = true
			continue
		}

		// Need to fetch this package
		if entry.IsCask {
			missingCasks = append(missingCasks, entry.Name)
		} else {
			missingFormulae = append(missingFormulae, entry.Name)
		}
	}

	// 3. Fetch missing packages via brew info
	if len(missingCasks) > 0 {
		fetched := d.fetchPackagesInfo(missingCasks, true)
		for _, name := range missingCasks {
			if pkg, exists := fetched[name]; exists {
				result = append(result, pkg)
			} else {
				// Fallback for packages that couldn't be fetched
				result = append(result, models.Package{
					Name:        name,
					DisplayName: name,
					Description: "(unable to load package info)",
					Type:        models.PackageTypeCask,
				})
			}
		}
	}

	if len(missingFormulae) > 0 {
		fetched := d.fetchPackagesInfo(missingFormulae, false)
		for _, name := range missingFormulae {
			if pkg, exists := fetched[name]; exists {
				result = append(result, pkg)
			} else {
				// Fallback for packages that couldn't be fetched
				result = append(result, models.Package{
					Name:        name,
					DisplayName: name,
					Description: "(unable to load package info)",
					Type:        models.PackageTypeFormula,
				})
			}
		}
	}

	// 4. Save all tap packages to cache
	if len(result) > 0 {
		if err := ensureCacheDir(); err == nil {
			if data, err := json.Marshal(result); err == nil {
				writeCacheFile(cacheFileTapPackages, data)
			}
		}
	}

	return result, nil
}

// fetchPackagesInfo retrieves package info via brew info command.
func (d *DataProvider) fetchPackagesInfo(names []string, isCask bool) map[string]models.Package {
	result := make(map[string]models.Package)
	if len(names) == 0 {
		return result
	}

	var cmd *exec.Cmd
	if isCask {
		args := append([]string{"info", "--json=v2", "--cask"}, names...)
		cmd = exec.Command("brew", args...)
	} else {
		args := append([]string{"info", "--json=v1"}, names...)
		cmd = exec.Command("brew", args...)
	}

	output, err := cmd.Output()
	if err != nil {
		// Try individual fetches as fallback
		for _, name := range names {
			if pkg := d.fetchSinglePackageInfo(name, isCask); pkg != nil {
				result[name] = *pkg
			}
		}
		return result
	}

	if isCask {
		var response struct {
			Casks []models.Cask `json:"casks"`
		}
		if err := json.Unmarshal(output, &response); err == nil {
			for _, cask := range response.Casks {
				c := cask
				pkg := models.NewPackageFromCask(&c)
				result[c.Token] = pkg
			}
		}
	} else {
		var formulae []models.Formula
		if err := json.Unmarshal(output, &formulae); err == nil {
			for _, formula := range formulae {
				f := formula
				pkg := models.NewPackageFromFormula(&f)
				result[f.Name] = pkg
			}
		}
	}

	return result
}

// fetchSinglePackageInfo fetches info for a single package.
func (d *DataProvider) fetchSinglePackageInfo(name string, isCask bool) *models.Package {
	var cmd *exec.Cmd
	if isCask {
		cmd = exec.Command("brew", "info", "--json=v2", "--cask", name)
	} else {
		cmd = exec.Command("brew", "info", "--json=v1", name)
	}

	output, err := cmd.Output()
	if err != nil {
		return nil
	}

	if isCask {
		var response struct {
			Casks []models.Cask `json:"casks"`
		}
		if err := json.Unmarshal(output, &response); err != nil || len(response.Casks) == 0 {
			return nil
		}
		pkg := models.NewPackageFromCask(&response.Casks[0])
		return &pkg
	}

	var formulae []models.Formula
	if err := json.Unmarshal(output, &formulae); err != nil || len(formulae) == 0 {
		return nil
	}
	pkg := models.NewPackageFromFormula(&formulae[0])
	return &pkg
}

// SetupData initializes the DataProvider by loading all package data.
func (d *DataProvider) SetupData(forceRefresh bool) error {
	// Get installed formulae
	installed, err := d.GetInstalledFormulae(forceRefresh)
	if err != nil {
		return fmt.Errorf("failed to get installed formulae: %w", err)
	}
	*d.installedFormulae = installed

	// Get remote formulae
	remote, err := d.GetRemoteFormulae(forceRefresh)
	if err != nil {
		return fmt.Errorf("failed to get remote formulae: %w", err)
	}
	*d.remoteFormulae = remote

	// Get formulae analytics
	analytics, err := d.GetFormulaeAnalytics(forceRefresh)
	if err != nil {
		return fmt.Errorf("failed to get formulae analytics: %w", err)
	}
	d.formulaeAnalytics = analytics

	// Get installed casks
	installedCasks, err := d.GetInstalledCasks(forceRefresh)
	if err != nil {
		return fmt.Errorf("failed to get installed casks: %w", err)
	}
	*d.installedCasks = installedCasks

	// Get remote casks
	remoteCasks, err := d.GetRemoteCasks(forceRefresh)
	if err != nil {
		return fmt.Errorf("failed to get remote casks: %w", err)
	}
	*d.remoteCasks = remoteCasks

	// Get cask analytics
	caskAnalytics, err := d.GetCaskAnalytics(forceRefresh)
	if err != nil {
		return fmt.Errorf("failed to get cask analytics: %w", err)
	}
	d.caskAnalytics = caskAnalytics

	return nil
}

// GetPackages retrieves all packages (formulae + casks), merging remote and installed.
func (d *DataProvider) GetPackages() *[]models.Package {
	packageMap := make(map[string]models.Package)

	for _, formula := range *d.remoteFormulae {
		if _, exists := packageMap[formula.Name]; !exists {
			f := formula
			pkg := models.NewPackageFromFormula(&f)
			if a, exists := d.formulaeAnalytics[formula.Name]; exists && a.Number > 0 {
				downloads, _ := strconv.Atoi(strings.ReplaceAll(a.Count, ",", ""))
				pkg.Analytics90dRank = a.Number
				pkg.Analytics90dDownloads = downloads
			}
			packageMap[formula.Name] = pkg
		}
	}

	for _, formula := range *d.installedFormulae {
		f := formula
		pkg := models.NewPackageFromFormula(&f)
		if a, exists := d.formulaeAnalytics[formula.Name]; exists && a.Number > 0 {
			downloads, _ := strconv.Atoi(strings.ReplaceAll(a.Count, ",", ""))
			pkg.Analytics90dRank = a.Number
			pkg.Analytics90dDownloads = downloads
		}
		packageMap[formula.Name] = pkg
	}

	for _, cask := range *d.remoteCasks {
		if _, exists := packageMap[cask.Token]; !exists {
			c := cask
			pkg := models.NewPackageFromCask(&c)
			if a, exists := d.caskAnalytics[cask.Token]; exists && a.Number > 0 {
				downloads, _ := strconv.Atoi(strings.ReplaceAll(a.Count, ",", ""))
				pkg.Analytics90dRank = a.Number
				pkg.Analytics90dDownloads = downloads
			}
			packageMap[cask.Token] = pkg
		}
	}

	for _, cask := range *d.installedCasks {
		c := cask
		pkg := models.NewPackageFromCask(&c)
		if a, exists := d.caskAnalytics[cask.Token]; exists && a.Number > 0 {
			downloads, _ := strconv.Atoi(strings.ReplaceAll(a.Count, ",", ""))
			pkg.Analytics90dRank = a.Number
			pkg.Analytics90dDownloads = downloads
		}
		packageMap[cask.Token] = pkg
	}

	*d.allPackages = make([]models.Package, 0, len(packageMap))
	for _, pkg := range packageMap {
		*d.allPackages = append(*d.allPackages, pkg)
	}

	sort.Slice(*d.allPackages, func(i, j int) bool {
		return (*d.allPackages)[i].Name < (*d.allPackages)[j].Name
	})

	return d.allPackages
}

// fetchInstalledNames returns a map of installed package names for the given type.
func (d *DataProvider) fetchInstalledNames(packageType string) map[string]bool {
	result := make(map[string]bool)
	cmd := exec.Command("brew", "list", packageType)
	output, err := cmd.Output()
	if err != nil {
		return result
	}
	for _, name := range strings.Split(strings.TrimSpace(string(output)), "\n") {
		if name != "" {
			result[name] = true
		}
	}
	return result
}

// FetchInstalledCaskNames returns a map of installed cask names for quick lookup.
// Note: This runs `brew list --cask` each time it's called.
func (d *DataProvider) FetchInstalledCaskNames() map[string]bool {
	return d.fetchInstalledNames("--cask")
}

// FetchInstalledFormulaNames returns a map of installed formula names for quick lookup.
// Note: This runs `brew list --formula` each time it's called.
func (d *DataProvider) FetchInstalledFormulaNames() map[string]bool {
	return d.fetchInstalledNames("--formula")
}
```

## File: `internal/services/input.go`
```go
package services

import (
	"bbrew/internal/models"
	"bbrew/internal/ui"
	"fmt"

	"github.com/gdamore/tcell/v2"
)

// FilterType represents the active package filter state.
type FilterType int

const (
	FilterNone FilterType = iota
	FilterInstalled
	FilterOutdated
	FilterLeaves
	FilterCasks
)

// InputAction represents a user action that can be triggered by a key event.
type InputAction struct {
	Key            tcell.Key
	Rune           rune
	Name           string
	KeySlug        string
	Action         func()
	HideFromLegend bool // If true, this action won't appear in the legend bar
}

// InputServiceInterface defines the interface for handling user input actions.
type InputServiceInterface interface {
	HandleKeyEventInput(event *tcell.EventKey) *tcell.EventKey
	EnableBrewfileMode()
}

// InputService implements the InputServiceInterface and handles key events for the application.
type InputService struct {
	appService    *AppService
	layout        ui.LayoutInterface
	brewService   BrewServiceInterface
	keyActions    []*InputAction
	legendEntries []struct{ KeySlug, Name string }

	// Actions for each key input
	ActionSearch          *InputAction
	ActionFilterInstalled *InputAction
	ActionFilterOutdated  *InputAction
	ActionFilterLeaves    *InputAction
	ActionFilterCasks     *InputAction
	ActionInstall         *InputAction
	ActionUpdate          *InputAction
	ActionRemove          *InputAction
	ActionUpdateAll       *InputAction
	ActionInstallAll      *InputAction
	ActionRemoveAll       *InputAction
	ActionHelp            *InputAction
	ActionBack            *InputAction
	ActionQuit            *InputAction
}

var NewInputService = func(appService *AppService, brewService BrewServiceInterface) InputServiceInterface {
	s := &InputService{
		appService:  appService,
		layout:      appService.GetLayout(),
		brewService: brewService,
	}

	// Initialize actions with key bindings and handlers
	s.ActionSearch = &InputAction{
		Key: tcell.KeyRune, Rune: '/', KeySlug: "/", Name: "Search",
		Action: s.handleSearchFieldEvent,
	}
	s.ActionFilterInstalled = &InputAction{
		Key: tcell.KeyRune, Rune: 'f', KeySlug: "f", Name: "Installed",
		Action: s.handleFilterPackagesEvent,
	}
	s.ActionFilterOutdated = &InputAction{
		Key: tcell.KeyRune, Rune: 'o', KeySlug: "o", Name: "Outdated",
		Action: s.handleFilterOutdatedPackagesEvent, HideFromLegend: true,
	}
	s.ActionFilterLeaves = &InputAction{
		Key: tcell.KeyRune, Rune: 'l', KeySlug: "l", Name: "Leaves",
		Action: s.handleFilterLeavesEvent, HideFromLegend: true,
	}
	s.ActionFilterCasks = &InputAction{
		Key: tcell.KeyRune, Rune: 'c', KeySlug: "c", Name: "Casks",
		Action: s.handleFilterCasksEvent, HideFromLegend: true,
	}
	s.ActionInstall = &InputAction{
		Key: tcell.KeyRune, Rune: 'i', KeySlug: "i", Name: "Install",
		Action: s.handleInstallPackageEvent,
	}
	s.ActionUpdate = &InputAction{
		Key: tcell.KeyRune, Rune: 'u', KeySlug: "u", Name: "Update",
		Action: s.handleUpdatePackageEvent,
	}
	s.ActionRemove = &InputAction{
		Key: tcell.KeyRune, Rune: 'r', KeySlug: "r", Name: "Remove",
		Action: s.handleRemovePackageEvent,
	}
	s.ActionUpdateAll = &InputAction{
		Key: tcell.KeyCtrlU, Rune: 0, KeySlug: "ctrl+u", Name: "Update All",
		Action: s.handleUpdateAllPackagesEvent, HideFromLegend: true,
	}
	s.ActionInstallAll = &InputAction{
		Key: tcell.KeyCtrlA, Rune: 0, KeySlug: "ctrl+a", Name: "Install All (Brewfile)",
		Action: s.handleInstallAllPackagesEvent,
	}
	s.ActionRemoveAll = &InputAction{
		Key: tcell.KeyCtrlR, Rune: 0, KeySlug: "ctrl+r", Name: "Remove All (Brewfile)",
		Action: s.handleRemoveAllPackagesEvent,
	}
	s.ActionHelp = &InputAction{
		Key: tcell.KeyRune, Rune: '?', KeySlug: "?", Name: "Help",
		Action: s.handleHelpEvent,
	}
	s.ActionBack = &InputAction{
		Key: tcell.KeyEsc, Rune: 0, KeySlug: "esc", Name: "Back to Table",
		Action: s.handleBack, HideFromLegend: true,
	}
	s.ActionQuit = &InputAction{
		Key: tcell.KeyRune, Rune: 'q', KeySlug: "q", Name: "Quit",
		Action: s.handleQuitEvent, HideFromLegend: true,
	}

	// Build keyActions slice (InstallAll/RemoveAll added dynamically in Brewfile mode)
	s.keyActions = []*InputAction{
		s.ActionSearch, s.ActionFilterInstalled, s.ActionFilterOutdated,
		s.ActionFilterLeaves, s.ActionFilterCasks, s.ActionInstall,
		s.ActionUpdate, s.ActionRemove, s.ActionUpdateAll,
		s.ActionHelp, s.ActionBack, s.ActionQuit,
	}

	// Convert keyActions to legend entries
	s.updateLegendEntries()
	return s
}

// updateLegendEntries updates the legend entries based on current keyActions
func (s *InputService) updateLegendEntries() {
	s.legendEntries = make([]struct{ KeySlug, Name string }, 0, len(s.keyActions))
	for _, input := range s.keyActions {
		if !input.HideFromLegend {
			s.legendEntries = append(s.legendEntries, struct{ KeySlug, Name string }{KeySlug: input.KeySlug, Name: input.Name})
		}
	}
	s.layout.GetLegend().SetLegend(s.legendEntries, "")
}

// EnableBrewfileMode enables Brewfile mode, adding Install All and Remove All actions to the legend
func (s *InputService) EnableBrewfileMode() {
	// Add Install All and Remove All actions after Update All
	newActions := []*InputAction{}
	for _, action := range s.keyActions {
		newActions = append(newActions, action)
		if action == s.ActionUpdateAll {
			newActions = append(newActions, s.ActionInstallAll, s.ActionRemoveAll)
		}
	}
	s.keyActions = newActions
	s.updateLegendEntries()
}

// HandleKeyEventInput processes key events and triggers the corresponding actions.
func (s *InputService) HandleKeyEventInput(event *tcell.EventKey) *tcell.EventKey {
	if s.layout.GetSearch().Field().HasFocus() {
		return event
	}

	for _, input := range s.keyActions {
		if event.Modifiers() == tcell.ModNone && input.Key == event.Key() && input.Rune == event.Rune() { // Check Rune
			if input.Action != nil {
				input.Action()
				return nil
			}
		} else if event.Modifiers() != tcell.ModNone && input.Key == event.Key() { // Check Key only
			if input.Action != nil {
				input.Action()
				return nil
			}
		}
	}

	return event
}

// handleBack is called when the user presses the back key (Esc).
func (s *InputService) handleBack() {
	s.appService.GetApp().SetRoot(s.layout.Root(), true)
	s.appService.GetApp().SetFocus(s.layout.GetTable().View())
}

// handleSearchFieldEvent is called when the user presses the search key (/).
func (s *InputService) handleSearchFieldEvent() {
	s.appService.GetApp().SetFocus(s.layout.GetSearch().Field())
}

// handleQuitEvent is called when the user presses the quit key (q).
func (s *InputService) handleQuitEvent() {
	s.appService.GetApp().Stop()
}

// handleHelpEvent shows the help screen with all keyboard shortcuts.
func (s *InputService) handleHelpEvent() {
	helpScreen := s.layout.GetHelpScreen()
	helpScreen.SetBrewfileMode(s.appService.IsBrewfileMode())
	helpPages := helpScreen.Build(s.layout.Root())

	// Set up key handler to close help on any key press
	helpPages.SetInputCapture(func(_ *tcell.EventKey) *tcell.EventKey {
		// Close help and return to main view
		s.appService.GetApp().SetRoot(s.layout.Root(), true)
		s.appService.GetApp().SetFocus(s.layout.GetTable().View())
		return nil
	})

	s.appService.GetApp().SetRoot(helpPages, true)
}

// handleFilterEvent toggles the filter for packages based on the provided filter type.
func (s *InputService) handleFilterEvent(filterType FilterType) {
	// Toggle: if same filter is active, turn it off; otherwise switch to new filter
	if s.appService.activeFilter == filterType {
		s.appService.activeFilter = FilterNone
	} else {
		s.appService.activeFilter = filterType
	}

	// Update UI based on active filter
	s.updateFilterUI()
	s.appService.search(s.layout.GetSearch().Field().GetText(), true)
}

// updateFilterUI updates the search label and legend based on the current filter state.
func (s *InputService) updateFilterUI() {
	s.layout.GetLegend().SetLegend(s.legendEntries, "")

	// Map filter types to their display config
	filterConfig := map[FilterType]struct {
		suffix  string
		keySlug string
	}{
		FilterInstalled: {"Installed", s.ActionFilterInstalled.KeySlug},
		FilterOutdated:  {"Outdated", s.ActionFilterOutdated.KeySlug},
		FilterLeaves:    {"Leaves", s.ActionFilterLeaves.KeySlug},
		FilterCasks:     {"Casks", s.ActionFilterCasks.KeySlug},
	}

	baseLabel := "Search"
	if s.appService.IsBrewfileMode() {
		baseLabel = "Search (Brewfile"
	}

	if cfg, exists := filterConfig[s.appService.activeFilter]; exists {
		if s.appService.IsBrewfileMode() {
			s.layout.GetSearch().Field().SetLabel(baseLabel + " - " + cfg.suffix + "): ")
		} else {
			s.layout.GetSearch().Field().SetLabel("Search (" + cfg.suffix + "): ")
		}
		s.layout.GetLegend().SetLegend(s.legendEntries, cfg.keySlug)
		return
	}

	// No filter active (FilterNone)
	if s.appService.IsBrewfileMode() {
		s.layout.GetSearch().Field().SetLabel(baseLabel + "): ")
	} else {
		s.layout.GetSearch().Field().SetLabel("Search (All): ")
	}
}

// handleFilterPackagesEvent toggles the filter for installed packages
func (s *InputService) handleFilterPackagesEvent() {
	s.handleFilterEvent(FilterInstalled)
}

// handleFilterOutdatedPackagesEvent toggles the filter for outdated packages
func (s *InputService) handleFilterOutdatedPackagesEvent() {
	s.handleFilterEvent(FilterOutdated)
}

// handleFilterLeavesEvent toggles the filter for leaf packages (installed on request)
func (s *InputService) handleFilterLeavesEvent() {
	s.handleFilterEvent(FilterLeaves)
}

// handleFilterCasksEvent toggles the filter for cask packages only
func (s *InputService) handleFilterCasksEvent() {
	s.handleFilterEvent(FilterCasks)
}

// showModal displays a modal dialog with the specified text and confirmation/cancellation actions.
// This is used for actions like installing, removing, or updating packages, invoking user confirmation.
func (s *InputService) showModal(text string, confirmFunc func(), cancelFunc func()) {
	modal := s.layout.GetModal().Build(text, confirmFunc, cancelFunc)
	s.appService.app.SetRoot(modal, true)
}

// closeModal closes the currently displayed modal dialog and returns focus to the main table view.
func (s *InputService) closeModal() {
	s.appService.app.SetRoot(s.layout.Root(), true)
	s.appService.app.SetFocus(s.layout.GetTable().View())
}

// handleInstallPackageEvent is called when the user presses the installation key (i).
func (s *InputService) handleInstallPackageEvent() {
	row, _ := s.layout.GetTable().View().GetSelection()
	if row > 0 {
		info := (*s.appService.filteredPackages)[row-1]
		s.showModal(
			fmt.Sprintf("Are you sure you want to install the package: %s?", info.Name),
			func() {
				s.closeModal()
				s.layout.GetOutput().Clear()
				go func() {
					s.layout.GetNotifier().ShowWarning(fmt.Sprintf("Installing %s...", info.Name))
					if err := s.brewService.InstallPackage(info, s.appService.app, s.layout.GetOutput().View()); err != nil {
						s.layout.GetNotifier().ShowError(fmt.Sprintf("Failed to install %s", info.Name))
						return
					}
					s.layout.GetNotifier().ShowSuccess(fmt.Sprintf("Installed %s", info.Name))
					s.appService.forceRefreshResults()
				}()
			}, s.closeModal)
	}
}

// handleRemovePackageEvent is called when the user presses the removal key (r).
func (s *InputService) handleRemovePackageEvent() {
	row, _ := s.layout.GetTable().View().GetSelection()
	if row > 0 {
		info := (*s.appService.filteredPackages)[row-1]
		s.showModal(
			fmt.Sprintf("Are you sure you want to remove the package: %s?", info.Name),
			func() {
				s.closeModal()
				s.layout.GetOutput().Clear()
				go func() {
					s.layout.GetNotifier().ShowWarning(fmt.Sprintf("Removing %s...", info.Name))
					if err := s.brewService.RemovePackage(info, s.appService.app, s.layout.GetOutput().View()); err != nil {
						s.layout.GetNotifier().ShowError(fmt.Sprintf("Failed to remove %s", info.Name))
						return
					}
					s.layout.GetNotifier().ShowSuccess(fmt.Sprintf("Removed %s", info.Name))
					s.appService.forceRefreshResults()
				}()
			}, s.closeModal)
	}
}

// handleUpdatePackageEvent is called when the user presses the update key (u).
func (s *InputService) handleUpdatePackageEvent() {
	row, _ := s.layout.GetTable().View().GetSelection()
	if row > 0 {
		info := (*s.appService.filteredPackages)[row-1]
		s.showModal(
			fmt.Sprintf("Are you sure you want to update the package: %s?", info.Name),
			func() {
				s.closeModal()
				s.layout.GetOutput().Clear()
				go func() {
					s.layout.GetNotifier().ShowWarning(fmt.Sprintf("Updating %s...", info.Name))
					if err := s.brewService.UpdatePackage(info, s.appService.app, s.layout.GetOutput().View()); err != nil {
						s.layout.GetNotifier().ShowError(fmt.Sprintf("Failed to update %s", info.Name))
						return
					}
					s.layout.GetNotifier().ShowSuccess(fmt.Sprintf("Updated %s", info.Name))
					s.appService.forceRefreshResults()
				}()
			}, s.closeModal)
	}
}

// handleUpdateAllPackagesEvent is called when the user presses the update all key (Ctrl+U).
func (s *InputService) handleUpdateAllPackagesEvent() {
	s.showModal("Are you sure you want to update all Packages?", func() {
		s.closeModal()
		s.layout.GetOutput().Clear()
		go func() {
			s.layout.GetNotifier().ShowWarning("Updating all Packages...")
			if err := s.brewService.UpdateAllPackages(s.appService.app, s.layout.GetOutput().View()); err != nil {
				s.layout.GetNotifier().ShowError("Failed to update all Packages")
				return
			}
			s.layout.GetNotifier().ShowSuccess("Updated all Packages")
			s.appService.forceRefreshResults()
		}()
	}, s.closeModal)
}

// batchOperation defines the configuration for a batch package operation.
type batchOperation struct {
	actionVerb    string // "Installing" or "Removing"
	actionTag     string // "INSTALL" or "REMOVE"
	skipCondition func(pkg models.Package) bool
	skipReason    string
	execute       func(pkg models.Package) error
}

// handleBatchPackageOperation processes multiple packages with progress notifications.
func (s *InputService) handleBatchPackageOperation(op batchOperation) {
	if !s.appService.IsBrewfileMode() {
		return
	}

	packages := *s.appService.GetBrewfilePackages()
	if len(packages) == 0 {
		s.layout.GetNotifier().ShowError("No packages found in Brewfile")
		return
	}

	// Count relevant packages
	actionable := 0
	for _, pkg := range packages {
		if !op.skipCondition(pkg) {
			actionable++
		}
	}

	if actionable == 0 {
		s.layout.GetNotifier().ShowWarning(fmt.Sprintf("No packages to process (%s)", op.skipReason))
		return
	}

	message := fmt.Sprintf("%s all packages from Brewfile?\n\nTotal: %d packages\nTo process: %d",
		op.actionVerb, len(packages), actionable)

	s.showModal(message, func() {
		s.closeModal()
		s.layout.GetOutput().Clear()
		go func() {
			current := 0
			total := len(packages)

			for _, pkg := range packages {
				current++
				pkgName := pkg.Name // Capture for closures

				if op.skipCondition(pkg) {
					s.layout.GetNotifier().ShowWarning(fmt.Sprintf("[%d/%d] Skipping %s (%s)", current, total, pkgName, op.skipReason))
					s.appService.app.QueueUpdateDraw(func() {
						fmt.Fprintf(s.layout.GetOutput().View(), "[SKIP] %s (%s)\n", pkgName, op.skipReason)
					})
					continue
				}

				s.layout.GetNotifier().ShowWarning(fmt.Sprintf("[%d/%d] %s %s...", current, total, op.actionVerb, pkgName))
				s.appService.app.QueueUpdateDraw(func() {
					fmt.Fprintf(s.layout.GetOutput().View(), "\n[%s] %s %s...\n", op.actionTag, op.actionVerb, pkgName)
				})

				if err := op.execute(pkg); err != nil {
					s.layout.GetNotifier().ShowError(fmt.Sprintf("[%d/%d] Failed to process %s", current, total, pkgName))
					s.appService.app.QueueUpdateDraw(func() {
						fmt.Fprintf(s.layout.GetOutput().View(), "[ERROR] Failed to process %s: %v\n", pkgName, err)
					})
					continue
				}

				s.appService.app.QueueUpdateDraw(func() {
					fmt.Fprintf(s.layout.GetOutput().View(), "[SUCCESS] %s processed successfully\n", pkgName)
				})
			}

			s.layout.GetNotifier().ShowSuccess(fmt.Sprintf("Completed! Processed %d packages", total))
			s.appService.forceRefreshResults()
		}()
	}, s.closeModal)
}

// handleInstallAllPackagesEvent is called when the user presses the install all key (Ctrl+A).
func (s *InputService) handleInstallAllPackagesEvent() {
	s.handleBatchPackageOperation(batchOperation{
		actionVerb:    "Installing",
		actionTag:     "INSTALL",
		skipCondition: func(pkg models.Package) bool { return pkg.LocallyInstalled },
		skipReason:    "already installed",
		execute: func(pkg models.Package) error {
			return s.brewService.InstallPackage(pkg, s.appService.app, s.layout.GetOutput().View())
		},
	})
}

// handleRemoveAllPackagesEvent is called when the user presses the remove all key (Ctrl+R).
func (s *InputService) handleRemoveAllPackagesEvent() {
	s.handleBatchPackageOperation(batchOperation{
		actionVerb:    "Removing",
		actionTag:     "REMOVE",
		skipCondition: func(pkg models.Package) bool { return !pkg.LocallyInstalled },
		skipReason:    "not installed",
		execute: func(pkg models.Package) error {
			return s.brewService.RemovePackage(pkg, s.appService.app, s.layout.GetOutput().View())
		},
	})
}
```

## File: `internal/services/search.go`
```go
package services

import (
	"bbrew/internal/models"
	"fmt"
	"sort"
	"strings"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

// search filters the packages based on the search text and the current filter state.
func (s *AppService) search(searchText string, scrollToTop bool) {
	var filteredList []models.Package
	uniquePackages := make(map[string]bool)

	// Determine the source list based on the current filter state
	// If Brewfile mode is active, use brewfilePackages as the base source
	sourceList := s.packages
	if s.IsBrewfileMode() {
		sourceList = s.brewfilePackages
	}

	// Apply active filter on the source list
	sourceList = s.applyFilter(sourceList)

	if searchText == "" {
		// Reset to the appropriate list when the search string is empty
		filteredList = *sourceList
	} else {
		// Apply the search filter
		searchTextLower := strings.ToLower(searchText)
		for _, info := range *sourceList {
			if strings.Contains(strings.ToLower(info.Name), searchTextLower) ||
				strings.Contains(strings.ToLower(info.Description), searchTextLower) {
				if !uniquePackages[info.Name] {
					filteredList = append(filteredList, info)
					uniquePackages[info.Name] = true
				}
			}
		}

		// sort by analytics rank
		sort.Slice(filteredList, func(i, j int) bool {
			if filteredList[i].Analytics90dRank == 0 {
				return false
			}
			if filteredList[j].Analytics90dRank == 0 {
				return true
			}
			return filteredList[i].Analytics90dRank < filteredList[j].Analytics90dRank
		})
	}

	*s.filteredPackages = filteredList
	s.setResults(s.filteredPackages, scrollToTop)
}

// applyFilter filters packages based on the active filter type.
func (s *AppService) applyFilter(sourceList *[]models.Package) *[]models.Package {
	if s.activeFilter == FilterNone {
		return sourceList
	}

	filteredSource := &[]models.Package{}
	for _, info := range *sourceList {
		include := false
		switch s.activeFilter {
		case FilterInstalled:
			include = info.LocallyInstalled
		case FilterOutdated:
			include = info.LocallyInstalled && info.Outdated
		case FilterLeaves:
			include = info.LocallyInstalled && info.InstalledOnRequest
		case FilterCasks:
			include = info.Type == models.PackageTypeCask
		}
		if include {
			*filteredSource = append(*filteredSource, info)
		}
	}
	return filteredSource
}

// forceRefreshResults forces a refresh of the Homebrew formulae and cask data and updates the results in the UI.
func (s *AppService) forceRefreshResults() {
	// Force refresh all data to get up-to-date versions and installed status
	_ = s.dataProvider.SetupData(true)
	s.packages = s.dataProvider.GetPackages()

	// If in Brewfile mode, load tap packages and verify installed status
	if s.IsBrewfileMode() {
		s.fetchTapPackages()
		_ = s.loadBrewfilePackages() // Gets fresh installed status via FetchInstalledCaskNames/FormulaNames
		*s.filteredPackages = *s.brewfilePackages
	} else {
		// For non-Brewfile mode, get fresh installed status
		installedCasks := s.dataProvider.FetchInstalledCaskNames()
		installedFormulae := s.dataProvider.FetchInstalledFormulaNames()
		for i := range *s.packages {
			pkg := &(*s.packages)[i]
			if pkg.Type == models.PackageTypeCask {
				pkg.LocallyInstalled = installedCasks[pkg.Name]
			} else {
				pkg.LocallyInstalled = installedFormulae[pkg.Name]
			}
		}
		*s.filteredPackages = *s.packages
	}

	s.app.QueueUpdateDraw(func() {
		s.search(s.layout.GetSearch().Field().GetText(), false)
	})
}

// setResults updates the results table with the provided data and optionally scrolls to the top.
func (s *AppService) setResults(data *[]models.Package, scrollToTop bool) {
	s.layout.GetTable().Clear()
	s.layout.GetTable().SetTableHeaders("Type", "Name", "Version", "Description", "Downloads")

	for i, info := range *data {
		// Type cell with escaped brackets
		typeTag := tview.Escape("[F]") // Formula
		if info.Type == models.PackageTypeCask {
			typeTag = tview.Escape("[C]") // Cask
		}
		typeCell := tview.NewTableCell(typeTag).SetSelectable(true).SetAlign(tview.AlignLeft)

		// Version handling - truncate if too long
		version := info.Version
		const maxVersionLen = 15
		if len(version) > maxVersionLen {
			version = version[:maxVersionLen-1] + "…"
		}

		// Name cell
		nameCell := tview.NewTableCell(info.Name).SetSelectable(true)
		if info.LocallyInstalled {
			nameCell.SetTextColor(tcell.ColorGreen)
		}

		// Version cell
		versionCell := tview.NewTableCell(version).SetSelectable(true)
		if info.LocallyInstalled && info.Outdated {
			versionCell.SetTextColor(tcell.ColorOrange)
		}

		// Downloads cell
		downloadsCell := tview.NewTableCell(fmt.Sprintf("%d", info.Analytics90dDownloads)).SetSelectable(true).SetAlign(tview.AlignRight)

		// Set cells with new column order: Type, Name, Version, Description, Downloads
		s.layout.GetTable().View().SetCell(i+1, 0, typeCell.SetExpansion(0))
		s.layout.GetTable().View().SetCell(i+1, 1, nameCell.SetExpansion(0))
		s.layout.GetTable().View().SetCell(i+1, 2, versionCell.SetExpansion(0))
		s.layout.GetTable().View().SetCell(i+1, 3, tview.NewTableCell(info.Description).SetSelectable(true).SetExpansion(1))
		s.layout.GetTable().View().SetCell(i+1, 4, downloadsCell.SetExpansion(0))
	}

	// Update the details view with the first item in the list
	if len(*data) > 0 && scrollToTop {
		s.layout.GetTable().View().Select(1, 0)
		s.layout.GetTable().View().ScrollToBeginning()
		s.layout.GetDetails().SetContent(&(*data)[0])
	} else if len(*data) == 0 {
		s.layout.GetDetails().SetContent(nil) // Clear details if no results
	}

	// Update the filter counter
	// In Brewfile mode, show total Brewfile packages instead of all packages
	totalCount := len(*s.packages)
	if s.IsBrewfileMode() {
		totalCount = len(*s.brewfilePackages)
	}
	s.layout.GetSearch().UpdateCounter(totalCount, len(*s.filteredPackages))
}
```

## File: `internal/services/selfupdate.go`
```go
package services

import (
	"context"
	"encoding/json"
	"fmt"
	"os/exec"
)

type SelfUpdateServiceInterface interface {
	CheckForUpdates(ctx context.Context) (string, error)
}

type SelfUpdateService struct{}

type boldBrewStatusInfo struct {
	Versions struct {
		Stable string `json:"stable"`
	} `json:"versions"`
}

var NewSelfUpdateService = func() SelfUpdateServiceInterface {
	return &SelfUpdateService{}
}

// CheckForUpdates checks for the latest version of the Bold Brew package using Homebrew.
func (s *SelfUpdateService) CheckForUpdates(ctx context.Context) (string, error) {
	cmd := exec.CommandContext(ctx, "brew", "info", "--json=v1", "valkyrie00/bbrew/bbrew")
	output, err := cmd.CombinedOutput()
	if err != nil {
		if ctx.Err() != nil {
			return "", fmt.Errorf("context cancelled")
		}
		return "", fmt.Errorf("failed to fetch latest version from tap: %v", err)
	}

	var info []boldBrewStatusInfo
	if err := json.Unmarshal(output, &info); err != nil {
		return "", fmt.Errorf("failed to parse version info: %v", err)
	}

	if len(info) == 0 {
		return "", fmt.Errorf("no version information found")
	}

	return info[0].Versions.Stable, nil
}
```

## File: `internal/ui/layout.go`
```go
package ui

import (
	"bbrew/internal/ui/components"
	"bbrew/internal/ui/theme"

	"github.com/rivo/tview"
)

type LayoutInterface interface {
	Setup()
	Root() tview.Primitive

	GetHeader() *components.Header
	GetSearch() *components.Search
	GetTable() *components.Table
	GetDetails() *components.Details
	GetOutput() *components.Output
	GetLegend() *components.Legend
	GetNotifier() *components.Notifier
	GetModal() *components.Modal
	GetHelpScreen() *components.HelpScreen
}

type Layout struct {
	mainContent *tview.Grid
	header      *components.Header
	search      *components.Search
	table       *components.Table
	details     *components.Details
	output      *components.Output
	legend      *components.Legend
	notifier    *components.Notifier
	modal       *components.Modal
	helpScreen  *components.HelpScreen
	theme       *theme.Theme
}

func NewLayout(theme *theme.Theme) LayoutInterface {
	return &Layout{
		mainContent: tview.NewGrid(),
		header:      components.NewHeader(theme),
		search:      components.NewSearch(theme),
		table:       components.NewTable(theme),
		details:     components.NewDetails(theme),
		output:      components.NewOutput(theme),
		legend:      components.NewLegend(theme),
		notifier:    components.NewNotifier(theme),
		modal:       components.NewModal(theme),
		helpScreen:  components.NewHelpScreen(theme),
		theme:       theme,
	}
}

func (l *Layout) setupLayout() {
	// Header
	headerContent := tview.NewFlex().SetDirection(tview.FlexColumn).
		AddItem(l.header.View(), 0, 1, false).
		AddItem(l.notifier.View(), 0, 1, false)

	// Search and filters
	searchRow := tview.NewFlex().SetDirection(tview.FlexColumn).
		AddItem(l.search.Field(), 0, 1, false).
		AddItem(l.search.Counter(), 0, 1, false)

	filtersArea := tview.NewFrame(searchRow).
		SetBorders(0, 0, 0, 0, 3, 3)

	tableFrame := tview.NewFrame(l.table.View()).
		SetBorders(0, 0, 0, 0, 3, 3)

	// Left column with search and table
	leftColumn := tview.NewFlex().SetDirection(tview.FlexRow).
		AddItem(filtersArea, 2, 0, false).
		AddItem(tableFrame, 0, 4, false)

	// Right column with details and output
	rightColumn := tview.NewFlex().SetDirection(tview.FlexRow).
		AddItem(l.details.View(), 0, 2, false).
		AddItem(l.output.View(), 0, 1, false)

	// Central content (left 75%, right 25%)
	mainContent := tview.NewFlex().SetDirection(tview.FlexColumn).
		AddItem(leftColumn, 0, 3, false).
		AddItem(rightColumn, 0, 1, false)

	// Footer
	footerContent := tview.NewFlex().SetDirection(tview.FlexRow).
		AddItem(l.legend.View(), 0, 1, false)

	// Final layout
	l.mainContent.
		SetRows(1, 0, 1).
		SetColumns(0).
		SetBorders(true).
		AddItem(headerContent, 0, 0, 1, 1, 0, 0, false).
		AddItem(mainContent, 1, 0, 1, 1, 0, 0, true).
		AddItem(footerContent, 2, 0, 1, 1, 0, 0, false)
}

func (l *Layout) Setup() {
	l.setupLayout()
}

func (l *Layout) Root() tview.Primitive {
	return l.mainContent
}

func (l *Layout) GetHeader() *components.Header         { return l.header }
func (l *Layout) GetSearch() *components.Search         { return l.search }
func (l *Layout) GetTable() *components.Table           { return l.table }
func (l *Layout) GetDetails() *components.Details       { return l.details }
func (l *Layout) GetOutput() *components.Output         { return l.output }
func (l *Layout) GetLegend() *components.Legend         { return l.legend }
func (l *Layout) GetNotifier() *components.Notifier     { return l.notifier }
func (l *Layout) GetModal() *components.Modal           { return l.modal }
func (l *Layout) GetHelpScreen() *components.HelpScreen { return l.helpScreen }
```

## File: `internal/ui/components/details.go`
```go
package components

import (
	"bbrew/internal/models"
	"bbrew/internal/ui/theme"
	"fmt"
	"strings"

	"github.com/rivo/tview"
	"golang.org/x/text/language"
	"golang.org/x/text/message"
)

type Details struct {
	view  *tview.TextView
	theme *theme.Theme
}

func NewDetails(theme *theme.Theme) *Details {
	details := &Details{
		view:  tview.NewTextView(),
		theme: theme,
	}

	details.view.SetDynamicColors(true)
	details.view.SetTextAlign(tview.AlignLeft)
	details.view.SetTitle("Details")
	details.view.SetTitleColor(theme.TitleColor)
	details.view.SetTitleAlign(tview.AlignLeft)
	details.view.SetBorder(true)
	details.view.SetBorderPadding(0, 0, 1, 1)
	return details
}

func (d *Details) SetContent(pkg *models.Package) {
	if pkg == nil {
		d.view.SetText("")
		return
	}

	// Installation status with colors
	installedStatus := "[red]Not installed[-]"
	if pkg.LocallyInstalled {
		installedStatus = "[green]Installed[-]"
		if pkg.Outdated {
			installedStatus = "[orange]Update available[-]"
		}
	}

	// Type tag with escaped brackets
	typeTag := tview.Escape("[F]") // Formula
	typeLabel := "Formula"
	if pkg.Type == models.PackageTypeCask {
		typeTag = tview.Escape("[C]") // Cask
		typeLabel = "Cask"
	}

	// Section separator
	separator := "[dim]────────────────────────[-]"

	// Basic information with status
	basicInfo := fmt.Sprintf(
		"[yellow::b]%s[-]\n%s\n"+
			"[blue]• Type:[-] %s %s\n"+
			"[blue]• Name:[-] %s\n"+
			"[blue]• Display Name:[-] %s\n"+
			"[blue]• Version:[-] %s\n"+
			"[blue]• Status:[-] %s\n"+
			"[blue]• Homepage:[-] %s\n\n"+
			"[yellow::b]Description[-]\n%s\n%s",
		pkg.Name, separator,
		typeTag, typeLabel,
		pkg.Name,
		pkg.DisplayName,
		pkg.Version,
		installedStatus,
		pkg.Homepage,
		separator,
		pkg.Description,
	)

	// Installation details
	installDetails := d.getPackageInstallationDetails(pkg)

	// Dependencies (only for formulae)
	dependenciesInfo := ""
	if pkg.Type == models.PackageTypeFormula && pkg.Formula != nil {
		dependenciesInfo = d.getDependenciesInfo(pkg.Formula)
	}

	analyticsInfo := d.getAnalyticsInfo(pkg)

	parts := []string{basicInfo, installDetails}
	if dependenciesInfo != "" {
		parts = append(parts, dependenciesInfo)
	}
	parts = append(parts, analyticsInfo)

	d.view.SetText(strings.Join(parts, "\n\n"))
}

func (d *Details) getPackageInstallationDetails(pkg *models.Package) string {
	separator := "[dim]────────────────────────[-]"

	if !pkg.LocallyInstalled {
		return fmt.Sprintf("[yellow::b]Installation[-]\n%s\nNot installed", separator)
	}

	// For formulae, show detailed installation info
	if pkg.Type == models.PackageTypeFormula && pkg.Formula != nil && len(pkg.Formula.Installed) > 0 {
		packagePrefix := pkg.Formula.LocalPath

		installedOnRequest := "No"
		if pkg.Formula.Installed[0].InstalledOnRequest {
			installedOnRequest = "Yes"
		}

		installedAsDependency := "No"
		if pkg.Formula.Installed[0].InstalledAsDependency {
			installedAsDependency = "Yes"
		}

		return fmt.Sprintf(
			"[yellow::b]Installation Details[-]\n%s\n"+
				"[blue]• Path:[-] %s\n"+
				"[blue]• Installed on request:[-] %s\n"+
				"[blue]• Installed as dependency:[-] %s\n"+
				"[blue]• Installed version:[-] %s",
			separator,
			packagePrefix,
			installedOnRequest,
			installedAsDependency,
			pkg.Formula.Installed[0].Version,
		)
	}

	// For casks, show simpler installation info
	if pkg.Type == models.PackageTypeCask && pkg.Cask != nil {
		installedVersion := "Unknown"
		if pkg.Cask.Installed != nil {
			installedVersion = *pkg.Cask.Installed
		}

		return fmt.Sprintf(
			"[yellow::b]Installation Details[-]\n%s\n"+
				"[blue]• Type:[-] Desktop Application\n"+
				"[blue]• Installed version:[-] %s",
			separator,
			installedVersion,
		)
	}

	return fmt.Sprintf("[yellow::b]Installation[-]\n%s\nInstalled", separator)
}

func (d *Details) getDependenciesInfo(info *models.Formula) string {
	separator := "[dim]────────────────────────[-]"
	title := fmt.Sprintf("[yellow::b]Dependencies[-]\n%s\n", separator)

	if len(info.Dependencies) == 0 {
		return title + "No dependencies"
	}

	// Format dependencies in multiple columns or with separators
	deps := ""
	for i, dep := range info.Dependencies {
		deps += dep
		if i < len(info.Dependencies)-1 {
			if (i+1)%3 == 0 {
				deps += "\n"
			} else {
				deps += ", "
			}
		}
	}

	return title + deps
}

func (d *Details) getAnalyticsInfo(pkg *models.Package) string {
	separator := "[dim]────────────────────────[-]"
	p := message.NewPrinter(language.English)

	return fmt.Sprintf(
		"[yellow::b]Analytics[-]\n%s\n"+
			"[blue]• 90d Global Rank:[-] %s\n"+
			"[blue]• 90d Downloads:[-] %s",
		separator,
		p.Sprintf("%d", pkg.Analytics90dRank),
		p.Sprintf("%d", pkg.Analytics90dDownloads),
	)
}

func (d *Details) View() *tview.TextView {
	return d.view
}

func (d *Details) Clear() {
	d.view.Clear()
}
```

## File: `internal/ui/components/header.go`
```go
package components

import (
	"bbrew/internal/ui/theme"
	"fmt"
	"github.com/rivo/tview"
)

type Header struct {
	view  *tview.TextView
	theme *theme.Theme
}

func NewHeader(theme *theme.Theme) *Header {
	header := &Header{
		view:  tview.NewTextView(),
		theme: theme,
	}

	header.view.SetDynamicColors(true)
	header.view.SetTextAlign(tview.AlignLeft)
	return header
}

func (h *Header) Update(name, version, brewVersion string) {
	h.view.SetText(fmt.Sprintf(" %s %s - %s", name, version, brewVersion))
}

func (h *Header) View() *tview.TextView {
	return h.view
}
```

## File: `internal/ui/components/help.go`
```go
package components

import (
	"bbrew/internal/ui/theme"
	"fmt"
	"strings"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

// HelpScreen displays a modal overlay with all keyboard shortcuts
type HelpScreen struct {
	pages      *tview.Pages
	theme      *theme.Theme
	isBrewfile bool
}

// NewHelpScreen creates a new help screen component
func NewHelpScreen(theme *theme.Theme) *HelpScreen {
	return &HelpScreen{
		theme: theme,
	}
}

// View returns the help screen pages (for overlay functionality)
func (h *HelpScreen) View() *tview.Pages {
	return h.pages
}

// SetBrewfileMode sets whether Brewfile-specific commands should be shown
func (h *HelpScreen) SetBrewfileMode(enabled bool) {
	h.isBrewfile = enabled
}

// Build creates the help screen as an overlay on top of the main content
func (h *HelpScreen) Build(mainContent tview.Primitive) *tview.Pages {
	content := h.buildHelpContent()

	textView := tview.NewTextView().
		SetDynamicColors(true).
		SetText(content).
		SetTextAlign(tview.AlignLeft)

	textView.SetBackgroundColor(h.theme.ModalBgColor)
	textView.SetTextColor(h.theme.DefaultTextColor)

	// Create a frame around the text
	frame := tview.NewFrame(textView).
		SetBorders(1, 1, 1, 1, 2, 2)
	frame.SetBackgroundColor(h.theme.ModalBgColor)
	frame.SetBorderColor(h.theme.BorderColor)
	frame.SetBorder(true).
		SetTitle(" Help ").
		SetTitleAlign(tview.AlignCenter)

	// Calculate box dimensions
	boxHeight := 22
	boxWidth := 55
	if h.isBrewfile {
		boxHeight = 26 // Extra space for Brewfile section
	}

	// Center the frame in a flex layout
	centered := tview.NewFlex().
		AddItem(nil, 0, 1, false).
		AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
			AddItem(nil, 0, 1, false).
			AddItem(frame, boxHeight, 0, true).
			AddItem(nil, 0, 1, false),
			boxWidth, 0, true).
		AddItem(nil, 0, 1, false)

	// Create pages with main content as background and help as overlay
	h.pages = tview.NewPages().
		AddPage("main", mainContent, true, true).
		AddPage("help", centered, true, true)

	return h.pages
}

// buildHelpContent generates the formatted help text
func (h *HelpScreen) buildHelpContent() string {
	var sb strings.Builder

	// Navigation section
	sb.WriteString(h.formatSection("NAVIGATION"))
	sb.WriteString(h.formatKey("↑/↓, j/k", "Navigate list"))
	sb.WriteString(h.formatKey("/", "Focus search"))
	sb.WriteString(h.formatKey("Esc", "Back to table"))
	sb.WriteString(h.formatKey("q", "Quit"))
	sb.WriteString("\n")

	// Filters section
	sb.WriteString(h.formatSection("FILTERS"))
	sb.WriteString(h.formatKey("f", "Toggle installed"))
	sb.WriteString(h.formatKey("o", "Toggle outdated"))
	sb.WriteString(h.formatKey("l", "Toggle leaves"))
	sb.WriteString(h.formatKey("c", "Toggle casks"))
	sb.WriteString("\n")

	// Actions section
	sb.WriteString(h.formatSection("ACTIONS"))
	sb.WriteString(h.formatKey("i", "Install selected"))
	sb.WriteString(h.formatKey("u", "Update selected"))
	sb.WriteString(h.formatKey("r", "Remove selected"))
	sb.WriteString(h.formatKey("Ctrl+U", "Update all"))

	// Brewfile section (only if in Brewfile mode)
	if h.isBrewfile {
		sb.WriteString("\n")
		sb.WriteString(h.formatSection("BREWFILE"))
		sb.WriteString(h.formatKey("Ctrl+A", "Install all"))
		sb.WriteString(h.formatKey("Ctrl+R", "Remove all"))
	}

	sb.WriteString("\n")
	sb.WriteString(fmt.Sprintf("[%s]Press any key to close[-]", h.getColorTag(h.theme.LegendColor)))

	return sb.String()
}

// formatSection formats a section header
func (h *HelpScreen) formatSection(title string) string {
	return fmt.Sprintf("[%s::b]%s[-:-:-]\n", h.getColorTag(h.theme.SuccessColor), title)
}

// formatKey formats a key-description pair
func (h *HelpScreen) formatKey(key, description string) string {
	return fmt.Sprintf("  [%s]%-12s[-] %s\n", h.getColorTag(h.theme.WarningColor), key, description)
}

// getColorTag converts a tcell.Color to a tview color tag
func (h *HelpScreen) getColorTag(color tcell.Color) string {
	return fmt.Sprintf("#%06x", color.Hex())
}
```

## File: `internal/ui/components/legend.go`
```go
package components

import (
	"bbrew/internal/ui/theme"
	"fmt"
	"github.com/rivo/tview"
	"strings"
)

type Legend struct {
	view  *tview.TextView
	theme *theme.Theme
}

func NewLegend(theme *theme.Theme) *Legend {
	legendView := tview.NewTextView().
		SetDynamicColors(true).
		SetTextAlign(tview.AlignCenter).
		SetTextColor(theme.LegendColor)

	return &Legend{
		view:  legendView,
		theme: theme,
	}
}

func (l *Legend) View() *tview.TextView {
	return l.view
}

func (l *Legend) GetFormattedLabel(keySlug, label string, active bool) string {
	if active {
		return fmt.Sprintf("[yellow::b]%s[-]", tview.Escape(fmt.Sprintf("[%s] %s", keySlug, label)))
	}

	return tview.Escape(fmt.Sprintf("[%s] %s", keySlug, label))
}

func (l *Legend) SetLegend(legend []struct{ KeySlug, Name string }, activeKey string) {
	var builder strings.Builder
	for i, item := range legend {
		active := item.KeySlug == activeKey
		builder.WriteString(l.GetFormattedLabel(item.KeySlug, item.Name, active))
		if i < len(legend)-1 {
			builder.WriteString(" | ")
		}
	}

	l.SetText(builder.String())
}

func (l *Legend) SetText(text string) {
	l.view.SetText(text)
}

func (l *Legend) Clear() {
	l.view.Clear()
}
```

## File: `internal/ui/components/modal.go`
```go
package components

import (
	"bbrew/internal/ui/theme"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

type Modal struct {
	view  *tview.Modal
	theme *theme.Theme
}

func NewModal(theme *theme.Theme) *Modal {
	// Use green background with black text for activated button
	// Black text ensures consistent visibility across all terminal themes
	activatedStyle := tcell.StyleDefault.
		Background(theme.SuccessColor).
		Foreground(tcell.ColorBlack).
		Bold(true)

	modal := tview.NewModal().
		SetBackgroundColor(theme.ModalBgColor).
		SetTextColor(theme.DefaultTextColor).
		SetButtonBackgroundColor(theme.ButtonBgColor).
		SetButtonTextColor(theme.ButtonTextColor).
		SetButtonActivatedStyle(activatedStyle)

	return &Modal{
		view:  modal,
		theme: theme,
	}
}

func (m *Modal) View() *tview.Modal {
	return m.view
}

func (m *Modal) Build(text string, confirmFunc func(), cancelFunc func()) *tview.Modal {
	m.view.ClearButtons()
	m.view.
		SetText(text).
		// Add padding to button labels with spaces for better visual appearance
		AddButtons([]string{"  Confirm  ", "  Cancel  "}).
		SetDoneFunc(func(buttonIndex int, _ string) {
			switch buttonIndex {
			case 0:
				confirmFunc()
			case 1:
				cancelFunc()
			}
		})

	return m.view
}
```

## File: `internal/ui/components/notifier.go`
```go
package components

import (
	"bbrew/internal/ui/theme"
	"fmt"
	"github.com/rivo/tview"
)

type Notifier struct {
	view  *tview.TextView
	theme *theme.Theme
}

func NewNotifier(theme *theme.Theme) *Notifier {
	notifierView := tview.NewTextView().
		SetDynamicColors(true).
		SetTextAlign(tview.AlignRight)

	return &Notifier{
		view:  notifierView,
		theme: theme,
	}
}

func (n *Notifier) View() *tview.TextView {
	return n.view
}

func (n *Notifier) ShowSuccess(message string) {
	n.view.SetTextColor(n.theme.SuccessColor).SetText(fmt.Sprintf(" %s ", message))
}

func (n *Notifier) ShowWarning(message string) {
	n.view.SetTextColor(n.theme.WarningColor).SetText(fmt.Sprintf(" %s ", message))
}

func (n *Notifier) ShowError(message string) {
	n.view.SetTextColor(n.theme.ErrorColor).SetText(fmt.Sprintf(" %s ", message))
}

func (n *Notifier) Clear() {
	n.view.Clear()
}
```

## File: `internal/ui/components/ouput.go`
```go
package components

import (
	"bbrew/internal/ui/theme"
	"github.com/rivo/tview"
)

type Output struct {
	view  *tview.TextView
	theme *theme.Theme
}

func NewOutput(theme *theme.Theme) *Output {
	output := &Output{
		view:  tview.NewTextView(),
		theme: theme,
	}

	output.view.SetDynamicColors(true)
	output.view.SetScrollable(true)
	output.view.SetWrap(true)
	output.view.SetTextAlign(tview.AlignLeft)
	output.view.SetBorder(true)
	output.view.SetTitle("Output")
	output.view.SetTitleColor(theme.TitleColor)
	output.view.SetTitleAlign(tview.AlignLeft)
	output.view.SetBorderPadding(0, 0, 1, 1)
	return output
}

func (o *Output) View() *tview.TextView {
	return o.view
}

func (o *Output) Clear() {
	o.view.Clear()
}

func (o *Output) Write(text string) {
	o.view.SetText(text)
}

func (o *Output) Append(text string) {
	currentText := o.view.GetText(true)
	o.view.SetText(currentText + text)
}

func (o *Output) ScrollToEnd() {
	o.view.ScrollToEnd()
}
```

## File: `internal/ui/components/search.go`
```go
package components

import (
	"bbrew/internal/ui/theme"
	"fmt"
	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

type Search struct {
	field   *tview.InputField
	counter *tview.TextView
	theme   *theme.Theme
}

func NewSearch(theme *theme.Theme) *Search {
	search := &Search{
		field:   tview.NewInputField(),
		counter: tview.NewTextView(),
		theme:   theme,
	}

	search.field.SetLabel(tview.Escape("Search (All): "))
	search.field.SetLabelColor(theme.SearchLabelColor)
	search.field.SetFieldStyle(tcell.StyleDefault.Italic(true).Underline(true))
	search.field.SetFieldBackgroundColor(theme.DefaultBgColor)
	search.field.SetFieldTextColor(theme.DefaultTextColor)
	search.counter.SetDynamicColors(true)
	search.counter.SetTextAlign(tview.AlignRight)
	return search
}

func (s *Search) SetHandlers(done func(key tcell.Key), changed func(text string)) {
	s.field.SetDoneFunc(done)
	s.field.SetChangedFunc(changed)
}

func (s *Search) UpdateCounter(total, filtered int) {
	s.counter.SetText(fmt.Sprintf("Total: %d | Filtered: %d", total, filtered))
}

func (s *Search) Field() *tview.InputField {
	return s.field
}

func (s *Search) Counter() *tview.TextView {
	return s.counter
}
```

## File: `internal/ui/components/table.go`
```go
package components

import (
	"bbrew/internal/ui/theme"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

type Table struct {
	view  *tview.Table
	theme *theme.Theme
}

func NewTable(theme *theme.Theme) *Table {
	table := &Table{
		view:  tview.NewTable(),
		theme: theme,
	}
	table.view.SetBorders(false)
	table.view.SetSelectable(true, false)
	table.view.SetFixed(1, 0)

	// Use reverse video for selection to ensure visibility on any terminal theme
	table.view.SetSelectedStyle(tcell.StyleDefault.Reverse(true))

	return table
}

func (t *Table) SetSelectionHandler(handler func(row, column int)) {
	t.view.SetSelectionChangedFunc(handler)
}

func (t *Table) View() *tview.Table {
	return t.view
}

func (t *Table) Clear() {
	t.view.Clear()
}

func (t *Table) SetTableHeaders(headers ...string) {
	for i, header := range headers {
		t.view.SetCell(0, i, &tview.TableCell{
			Text:            header,
			NotSelectable:   true,
			Align:           tview.AlignLeft,
			Color:           t.theme.TableHeaderColor,
			BackgroundColor: t.theme.DefaultBgColor,
		})
	}
}
```

## File: `internal/ui/theme/theme.go`
```go
package theme

import (
	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

type Theme struct {
	// Application-specific colors
	DefaultTextColor tcell.Color
	DefaultBgColor   tcell.Color
	WarningColor     tcell.Color
	SuccessColor     tcell.Color
	ErrorColor       tcell.Color

	TitleColor      tcell.Color
	LabelColor      tcell.Color
	ButtonBgColor   tcell.Color
	ButtonTextColor tcell.Color

	ModalBgColor     tcell.Color
	LegendColor      tcell.Color
	TableHeaderColor tcell.Color
	SearchLabelColor tcell.Color

	// tview global styles (mapped to tview.Styles)
	PrimitiveBackgroundColor    tcell.Color
	ContrastBackgroundColor     tcell.Color
	MoreContrastBackgroundColor tcell.Color
	BorderColor                 tcell.Color
	GraphicsColor               tcell.Color
	PrimaryTextColor            tcell.Color
	SecondaryTextColor          tcell.Color
	TertiaryTextColor           tcell.Color
	InverseTextColor            tcell.Color
	ContrastSecondaryTextColor  tcell.Color
}

func NewTheme() *Theme {
	theme := &Theme{
		// Application-specific colors
		DefaultTextColor: tcell.ColorDefault,
		DefaultBgColor:   tcell.ColorDefault,

		// Use standard ANSI colors that work well on both light and dark themes
		WarningColor: tcell.ColorYellow,
		SuccessColor: tcell.ColorGreen,
		ErrorColor:   tcell.ColorRed,

		// Component colors
		TitleColor:      tcell.ColorPurple,
		LabelColor:      tcell.ColorYellow,
		ButtonBgColor:   tcell.ColorDefault,
		ButtonTextColor: tcell.ColorDefault,

		ModalBgColor:     tcell.ColorDefault,
		LegendColor:      tcell.ColorDefault,
		TableHeaderColor: tcell.ColorBlue,
		SearchLabelColor: tcell.ColorPurple,

		// tview global styles - use terminal default colors for better compatibility
		// By default, tview uses hardcoded colors (like tcell.ColorBlack) which don't
		// adapt to the terminal's theme. We set them all to ColorDefault.
		PrimitiveBackgroundColor:    tcell.ColorDefault,
		ContrastBackgroundColor:     tcell.ColorDefault,
		MoreContrastBackgroundColor: tcell.ColorDefault,
		BorderColor:                 tcell.ColorDefault,
		GraphicsColor:               tcell.ColorDefault,
		PrimaryTextColor:            tcell.ColorDefault,
		SecondaryTextColor:          tcell.ColorDefault,
		TertiaryTextColor:           tcell.ColorDefault,
		InverseTextColor:            tcell.ColorDefault,
		ContrastSecondaryTextColor:  tcell.ColorDefault,
	}

	// Apply theme to tview global styles
	tview.Styles.PrimitiveBackgroundColor = theme.PrimitiveBackgroundColor
	tview.Styles.ContrastBackgroundColor = theme.ContrastBackgroundColor
	tview.Styles.MoreContrastBackgroundColor = theme.MoreContrastBackgroundColor
	tview.Styles.BorderColor = theme.BorderColor
	tview.Styles.TitleColor = theme.TitleColor
	tview.Styles.GraphicsColor = theme.GraphicsColor
	tview.Styles.PrimaryTextColor = theme.PrimaryTextColor
	tview.Styles.SecondaryTextColor = theme.SecondaryTextColor
	tview.Styles.TertiaryTextColor = theme.TertiaryTextColor
	tview.Styles.InverseTextColor = theme.InverseTextColor
	tview.Styles.ContrastSecondaryTextColor = theme.ContrastSecondaryTextColor

	return theme
}
```

## File: `site/content/blog/bold-brew-2-0-cask-support.md`
```markdown
---
title: "Bold Brew 2.0: Complete Homebrew Management with Cask Support"
date: "2025-10-13"
description: "Bold Brew 2.0 brings major new features including full Cask support, Leaves filter, XDG compliance, and enhanced security. Manage both CLI tools and GUI applications seamlessly."
keywords: "Bold Brew 2.0, Homebrew casks, TUI package manager, leaves filter, XDG compliance, Homebrew GUI, terminal UI, package management, macOS apps, Linux apps"
---

# Bold Brew 2.0: Complete Homebrew Management with Cask Support

We're thrilled to announce **Bold Brew 2.0**, the biggest update since launch! This release transforms Bold Brew from a formula-only manager into a **complete Homebrew management solution** that handles both command-line tools and GUI applications.

## 🎉 What's New

### Full Homebrew Casks Support

The most requested feature is finally here! Bold Brew now provides **complete support for Homebrew Casks**, allowing you to manage GUI applications and binaries directly from the same intuitive interface you love.

**What are Casks?** Homebrew Casks extend Homebrew's package management to include macOS and Linux GUI applications. Instead of just installing command-line tools like `git` or `node`, you can now manage apps like Google Chrome, Visual Studio Code, Docker Desktop, and thousands more.

#### Visual Type Indicators

Never wonder what type of package you're looking at! Bold Brew 2.0 introduces clear visual indicators:
- `[F]` - Formula (command-line tool)
- `[C]` - Cask (GUI application or binary)

These tags appear throughout the interface, making it instantly clear whether you're working with a CLI tool or a desktop application.

### Smart Leaves Filter

Tired of seeing all those dependency packages cluttering your installed list? The new **Leaves Filter** (press `L`) shows only packages you explicitly installed, hiding all the dependencies that came along for the ride.

**Perfect for:**
- Cleaning up your system by identifying what you actually need
- Creating reproducible development environments
- Understanding your actual package footprint
- Selective updates of only your core tools

### XDG Base Directory Compliance

Bold Brew 2.0 now follows the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html), providing a cleaner, more standards-compliant cache management:

- **Linux**: `~/.cache/bbrew` or `$XDG_CACHE_HOME/bbrew`
- **macOS**: `~/Library/Caches/bbrew` (native macOS location!)
- **Windows** (WSL2): Windows Known Folders support

No more random dotfiles in your home directory—everything is where it should be.

## 🔧 Technical Improvements

### Go 1.25 and Modern Tooling

- **Updated to Go 1.25** for better performance and latest language features
- **Migrated to Podman** and OCI-compliant Containerfile for better security
- **Enhanced Makefile** with 15+ new targets including `make test`, `make security`, and `make install`
- **Improved build system** with local and containerized build options

### Enhanced Security

Security is a priority. Bold Brew 2.0 includes:
- **govulncheck** - Automated Go vulnerability scanning
- **gosec** - Static security analysis
- **GitHub Security integration** - SARIF reports uploaded to Security tab
- **Fixed memory aliasing issues** - Cleaner, safer code
- **Better permission handling** - Secure cache directory permissions (0750)

### Better User Experience

- **Enhanced keyboard shortcuts** - More intuitive navigation and filtering
- **Improved error messages** - Better debugging and user feedback
- **Analytics integration** - See popular packages based on 90-day download stats
- **Real-time feedback** - Live updates during package operations
- **Fixed rendering issues** - Proper display of all UI elements

## 🐛 Bug Fixes

- Fixed cask analytics endpoint (now correctly fetches download statistics)
- Corrected installed casks detection (properly identifies locally installed casks)
- Fixed tview special character rendering for type tags
- Improved directory permission handling for cache
- Enhanced error handling throughout the application

## 🚀 Getting Started

### For Existing Users

Update to the latest version:

```bash
brew update
brew upgrade bbrew
```

### For New Users

Install Bold Brew via Homebrew:

```bash
brew install Valkyrie00/homebrew-bbrew/bbrew
```

Or download from the [releases page](https://github.com/Valkyrie00/bold-brew/releases).

## 📖 Using the New Features

### Managing Casks

1. **Filter Casks Only**: Press `C` to show only Cask packages
2. **Search Casks**: Type `/` and search for your favorite GUI app (e.g., "chrome", "vscode", "docker")
3. **Install a Cask**: Select it and press `I`
4. **Update Casks**: Press `U` on any outdated Cask, or `Ctrl+U` to update all

### Using the Leaves Filter

1. Press `L` to activate the Leaves filter
2. Browse only the packages you explicitly installed
3. Identify packages you no longer need
4. Press `R` to remove unwanted packages

### Keyboard Shortcuts Reference

#### Filters
- `F` - Filter installed packages
- `O` - Filter outdated packages
- `L` - Filter leaves (explicitly installed, no dependencies)
- `C` - Filter casks only

#### Package Operations
- `I` - Install selected package
- `U` - Update selected package
- `R` - Remove selected package
- `Ctrl+U` - Update all outdated packages

## 🌐 Cross-Platform Support

Bold Brew 2.0 provides excellent support across platforms:

| Platform | Support | Notes |
|----------|---------|-------|
| 🍎 **macOS** | ✅ Full | Native Homebrew support with macOS-specific cache location |
| 🐧 **Linux** | ✅ Full | Linuxbrew/Homebrew support with XDG compliance |
| 🪟 **Windows** | ⚠️ Partial | Via WSL2 with Homebrew |

## 🎯 What's Next

We're not stopping here! Future plans include:
- **Formulae pinning** - Pin specific package versions
- **Backup/restore** - Export and import your package lists
- **Themes** - Customizable color schemes
- **Plugin system** - Extend Bold Brew with custom functionality

> **Update:** Tap management and Brewfile Mode with remote URL support are now available! [Read more](/blog/brewfile-mode-remote-support.html)

## 🙏 Acknowledgments

A huge thank you to:
- The Homebrew team for the excellent package management system
- Project Bluefin for adopting Bold Brew as their official Homebrew TUI
- All contributors who submitted issues, PRs, and feature requests
- The community for their continued support and feedback

## 📣 Spread the Word

If you love Bold Brew 2.0:
- ⭐ [Star the project on GitHub](https://github.com/Valkyrie00/bold-brew)
- 🐦 Share on social media
- 📝 Write about it on your blog
- 💬 Tell your developer friends

## 🔗 Resources

- [GitHub Repository](https://github.com/Valkyrie00/bold-brew)
- [Documentation](https://bold-brew.com)
- [Release Notes](https://github.com/Valkyrie00/bold-brew/releases)
- [Report Issues](https://github.com/Valkyrie00/bold-brew/issues)

---

**Happy brewing! 🍺**

*The Bold Brew Team*

```

## File: `site/content/blog/bold-brew-official-project-bluefin-tui.md`
```markdown
---
title: "Bold Brew Named Official Homebrew TUI for Project Bluefin"
date: "2025-10-13"
description: "Bold Brew becomes the official Terminal UI for managing Homebrew in Project Bluefin, a next-generation Linux desktop serving tens of thousands of users worldwide."
keywords: "Bold Brew, Project Bluefin, Universal Blue, Fedora Silverblue, atomic desktop, official TUI, Linux desktop, Homebrew Linux, immutable OS, cloud-native desktop"
---

# Bold Brew Named Official Homebrew TUI for Project Bluefin

We're incredibly proud to announce that **Bold Brew has been selected as the official Terminal UI** for managing Homebrew in [**Project Bluefin**](https://projectbluefin.io/), a next-generation Linux desktop that serves tens of thousands of users worldwide!

## 🌊 What is Project Bluefin?

[Project Bluefin](https://projectbluefin.io/) is a cutting-edge Linux desktop distribution that's part of the [Universal Blue](https://universal-blue.org/) ecosystem. Built on Fedora Atomic Desktop (formerly Silverblue), Bluefin represents the future of cloud-native desktop computing.

### Key Features of Bluefin

- **Atomic Updates** - System updates are atomic and can be rolled back
- **Immutable Base** - Core system is read-only for enhanced security
- **Container-First** - Development happens in containers, keeping the host clean
- **Modern Tooling** - Ships with the latest development tools and workflows
- **Cloud-Native** - Designed for modern cloud-native development practices

Bluefin is perfect for developers, DevOps engineers, and anyone who wants a reliable, cutting-edge Linux desktop that "just works."

## 🎯 Why Bold Brew?

Bluefin's philosophy emphasizes **quality over quantity** and **user experience** above all else. The project carefully curates every tool and application that ships with the distribution, ensuring they meet high standards for usability and reliability.

From the [Bluefin documentation](https://docs.projectbluefin.io/command-line/):

> **Bold Brew** is included as a text based user interface (TUI) to Brew. This application features full package management for homebrew in a nice nerdy interface.

Bold Brew was selected because it:
- **Simplifies Homebrew management** with an intuitive TUI
- **Aligns with Bluefin's design philosophy** of modern, user-friendly tools
- **Enhances the terminal experience** that Bluefin is passionate about
- **Works seamlessly** with Bluefin's container-first workflow
- **Provides both power and simplicity** for all user levels

## 🚀 Bold Brew on Bluefin

### Pre-installed and Ready

Bold Brew comes **pre-installed** on every Bluefin system. Users can launch it simply by typing:

```bash
bbrew
```

No installation, no configuration—it just works.

### Perfect Integration

Bold Brew fits perfectly into Bluefin's command-line ecosystem, which includes:

- **Homebrew** - Package manager for command-line tools
- **Flatpak** - GUI application management
- **Podman** - Container management
- **ujust** - System configuration and automation

Together, these tools provide a complete, modern package management experience.

### The Bluefin CLI Experience

Bluefin offers an optional enhanced CLI experience called `bluefin-cli`, which includes modern terminal tools like:

- `atuin` for shell history
- `eza` as a modern `ls` replacement
- `fd` for finding files
- `ripgrep` for search
- `zoxide` as a smarter `cd`

Bold Brew complements these tools by providing visual, interactive Homebrew management that's faster and more intuitive than typing commands.

## 📊 Impact and Reach

Being adopted by Project Bluefin means Bold Brew now reaches:

- **Tens of thousands** of active Bluefin users
- **Developers and DevOps professionals** worldwide
- **Cloud-native engineers** building modern applications
- **Linux enthusiasts** who want cutting-edge desktop experiences

This partnership significantly expands Bold Brew's user base and validates our approach to TUI package management.

## 🤝 Community and Ecosystem

### Universal Blue Ecosystem

Project Bluefin is part of the broader **Universal Blue** ecosystem, which includes:

- **[Aurora](https://getaurora.dev/)** - KDE Plasma variant of Bluefin
- **[Bazzite](https://bazzite.gg/)** - Gaming-focused Linux desktop
- **[Cayo](https://projectbluefin.io/cayo)** - Bluefin for developers

Bold Brew's adoption in Bluefin opens doors to potential integration across the entire Universal Blue ecosystem, bringing our TUI to even more users and use cases.

### Growing Together

This partnership benefits both projects:

**For Bluefin:**
- Enhanced user experience for Homebrew management
- Modern, intuitive tool that matches their design philosophy
- Active maintenance and feature development
- Community-driven improvements

**For Bold Brew:**
- Significant user base and real-world testing
- Valuable feedback from power users
- Integration with a respected Linux distribution
- Increased visibility in the Linux community

## 🎓 What This Means for Users

### Bluefin Users

If you're a Bluefin user, you already have Bold Brew installed! Here's how to get started:

1. **Launch Bold Brew**: Just type `bbrew` in your terminal
2. **Explore packages**: Press `/` to search for any package
3. **Filter views**: Use `F` for installed, `O` for outdated, `L` for leaves, `C` for casks
4. **Manage packages**: Press `I` to install, `U` to update, `R` to remove
5. **Stay updated**: Bold Brew updates are automatically delivered with Bluefin

### Bold Brew Users on Other Systems

This partnership validates Bold Brew as a production-ready tool trusted by a major Linux distribution. Whether you're on macOS or Linux, you can benefit from the same tool that Bluefin trusts.

## 🔮 Future Collaboration

We're excited to deepen our collaboration with Project Bluefin:

- **Feature requests** from Bluefin users will help shape Bold Brew's roadmap
- **Integration improvements** to make Bold Brew even more native to Bluefin
- **Documentation** tailored for Bluefin users
- **Joint community events** and user support
- **Possible expansion** to other Universal Blue distributions

## 🙏 Thank You

We want to thank:

- **The Bluefin team** for recognizing Bold Brew's potential and making it their official choice
- **Jorge Castro** and the **Universal Blue** community for building amazing cloud-native desktops
- **The Bluefin community** for welcoming Bold Brew and providing valuable feedback
- **Our contributors** who made Bold Brew worthy of this recognition
- **The Homebrew team** for creating the excellent package manager we're building on top of

## 📣 Try Bluefin Today

Interested in experiencing the future of Linux desktops?

1. **Visit** [projectbluefin.io](https://projectbluefin.io/)
2. **Download** the latest ISO
3. **Install** and experience Bold Brew out of the box
4. **Join** the [Bluefin community](https://universal-blue.discourse.group/) on Discourse

## 🔗 Resources

### Bold Brew
- [GitHub Repository](https://github.com/Valkyrie00/bold-brew)
- [Documentation](https://bold-brew.com)
- [Releases](https://github.com/Valkyrie00/bold-brew/releases)

### Project Bluefin
- [Official Website](https://projectbluefin.io/)
- [Documentation](https://docs.projectbluefin.io/)
- [Command Line Guide](https://docs.projectbluefin.io/command-line/)
- [GitHub](https://github.com/ublue-os/bluefin)

### Universal Blue
- [Website](https://universal-blue.org/)
- [Discourse Community](https://universal-blue.discourse.group/)
- [GitHub Organization](https://github.com/ublue-os)

---

**This is just the beginning of an exciting partnership!** 🎉

```

## File: `site/content/blog/brewfile-mode-remote-support.md`
```markdown
---
title: "Brewfile Mode: Curated Package Collections & Remote URL Support"
date: "2025-12-29"
description: "Bold Brew now supports Brewfile mode for curated package collections, plus the ability to load Brewfiles directly from HTTPS URLs. Perfect for team configurations and themed installers."
keywords: "Brewfile mode, remote Brewfile, HTTPS URL, curated packages, team configuration, Homebrew TUI, package collections, IDE installer, dev tools, Bold Brew"
---

# Brewfile Mode: Curated Package Collections & Remote URL Support

We're excited to announce a major new capability in Bold Brew: **Brewfile Mode** with full support for **remote Brewfiles via HTTPS URLs**. This feature transforms how teams and individuals manage their Homebrew package collections.

## 🎯 What is Brewfile Mode?

Brewfile Mode allows you to launch Bold Brew with a curated list of packages instead of the full Homebrew catalog. This is perfect for:

- **Themed installers** (IDE tools, AI/ML packages, DevOps tools)
- **Team onboarding** (share your team's essential tools)
- **Project-specific setups** (install only what a project needs)
- **Personal collections** (your favorite tools in one place)

### How It Works

```bash
# Local Brewfile
bbrew -f ~/Brewfile

# Remote Brewfile (NEW!)
bbrew -f https://raw.githubusercontent.com/your-org/configs/main/dev-tools.Brewfile
```

When you launch in Brewfile mode, Bold Brew shows **only** the packages defined in that Brewfile. You get the full Bold Brew experience—search, filters, install/remove—but focused on your curated selection.

## 🌐 Remote Brewfiles via HTTPS

The latest update adds support for loading Brewfiles directly from URLs. This opens up exciting possibilities:

### Share Team Configurations

```bash
# Everyone on the team uses the same dev tools
bbrew -f https://github.com/acme-corp/dotfiles/raw/main/Brewfile
```

### Create Themed Installers

```bash
# AI/ML development environment
bbrew -f https://example.com/brewfiles/ai-ml-toolkit.Brewfile

# Kubernetes tools collection
bbrew -f https://example.com/brewfiles/k8s-essentials.Brewfile

# Frontend development stack
bbrew -f https://example.com/brewfiles/frontend-dev.Brewfile
```

### Quick Setup for New Machines

Share a single URL with colleagues or include it in your README:

```markdown
## Development Setup

Install our recommended tools:
\`\`\`bash
brew install Valkyrie00/homebrew-bbrew/bbrew
bbrew -f https://our-company.com/dev-setup.Brewfile
\`\`\`
```

## 📦 Third-Party Tap Support

Brewfile Mode also includes full support for **third-party taps**. Your Brewfile can include packages from any Homebrew tap:

```ruby
# Brewfile example
tap "homebrew/cask-fonts"
tap "ublue-os/homebrew-tap"

# Core tools
brew "git"
brew "gh"
brew "jq"

# Fonts
cask "font-fira-code"
cask "font-jetbrains-mono"

# From third-party tap
cask "some-custom-package"
```

Bold Brew automatically:
1. **Installs missing taps** at startup
2. **Caches tap package info** for faster subsequent loads
3. **Shows real-time progress** during tap installation

## 🔒 Security First

Remote Brewfiles are loaded securely:

- **HTTPS only** — HTTP URLs are rejected for security
- **Temporary storage** — Downloaded files are automatically cleaned up
- **No persistence** — Remote content isn't cached between sessions

## 🎨 Use Cases

### 1. IDE Chooser for Teams

Create a Brewfile with all supported IDEs and let developers pick:

```ruby
# ide-chooser.Brewfile
cask "visual-studio-code"
cask "sublime-text"
cask "jetbrains-toolbox"
cask "zed"
cask "cursor"
```

```bash
bbrew -f https://team.example.com/ide-chooser.Brewfile
```

### 2. Project Onboarding

Include a Brewfile in your project repo:

```ruby
# project/.Brewfile
brew "node"
brew "pnpm"
brew "docker"
cask "docker"
```

New contributors run one command to get all dependencies.

### 3. Personal Dotfiles

Keep your Brewfile in your dotfiles repo and access it from anywhere:

```bash
bbrew -f https://github.com/username/dotfiles/raw/main/Brewfile
```

## 📋 Example Brewfiles

Bold Brew includes example Brewfiles in the `examples/` directory:

- **`all.brewfile`** — Comprehensive package collection
- **`ide.Brewfile`** — Popular IDEs and editors

Check them out for inspiration!

## 🚀 Getting Started

1. **Update Bold Brew** to the latest version:
   ```bash
   brew upgrade bbrew
   ```

2. **Try a local Brewfile**:
   ```bash
   bbrew -f ~/path/to/Brewfile
   ```

3. **Try a remote Brewfile**:
   ```bash
   bbrew -f https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/examples/all.brewfile
   ```

## 🎹 Brewfile Mode Shortcuts

When running in Brewfile mode, you get additional keyboard shortcuts:

| Key | Action |
|-----|--------|
| `Ctrl+A` | Install all packages from Brewfile |
| `Ctrl+R` | Remove all packages from Brewfile |

All standard shortcuts (search, filters, individual install/remove) work exactly as expected.

## 💡 Tips & Best Practices

1. **Version your Brewfiles** — Keep them in git for change tracking
2. **Use comments** — Document why each package is included
3. **Organize by category** — Group related packages together
4. **Test before sharing** — Verify packages exist and install correctly

## 🔗 Resources

- [Homebrew Brewfile documentation](https://github.com/Homebrew/homebrew-bundle)
- [Bold Brew on GitHub](https://github.com/Valkyrie00/bold-brew)
- [Example Brewfiles](https://github.com/Valkyrie00/bold-brew/tree/main/examples)

---

**Happy brewing with curated collections! 🍺**

*The Bold Brew Team*

```

## File: `site/content/blog/essential-homebrew-commands.md`
```markdown
---
title: "10 Essential Homebrew Commands You Should Know"
date: "2025-03-29"
description: "Master the most important Homebrew commands for macOS package management. Learn how to install, update, and manage packages efficiently."
keywords: "Homebrew commands, brew commands, macOS package management, brew update, brew install, brew upgrade, brew search, essential commands"
---

# 10 Essential Homebrew Commands You Should Know

Homebrew is the most popular package manager for macOS, and mastering its commands is essential for efficient package management. In this guide, we'll explore the 10 most important Homebrew commands that every macOS user should know.

## 1. Install Packages

The most basic and commonly used command is `brew install`:

```bash
brew install package_name
```

You can also install multiple packages at once:

```bash
brew install package1 package2 package3
```

## 2. Update Homebrew

Keep your Homebrew installation up to date:

```bash
brew update
```

This command updates Homebrew's package database to the latest version.

## 3. Upgrade Packages

Upgrade all installed packages:

```bash
brew upgrade
```

Or upgrade a specific package:

```bash
brew upgrade package_name
```

## 4. Remove Packages

Uninstall a package:

```bash
brew uninstall package_name
```

## 5. Get Package Information

View detailed information about a package:

```bash
brew info package_name
```

## 6. List Installed Packages

See all currently installed packages:

```bash
brew list
```

## 7. Search for Packages

Find packages in the Homebrew repository:

```bash
brew search package_name
```

## 8. Check System Status

Diagnose your Homebrew installation:

```bash
brew doctor
```

## 9. Clean Up

Remove old versions and clean the cache:

```bash
brew cleanup
```

## 10. Manage Taps

List tapped repositories:

```bash
brew tap
```

Add a new tap:

```bash
brew tap user/repo
```

## Pro Tips

1. Combine update and upgrade:
```bash
brew update && brew upgrade
```

2. Use `brew doctor` regularly to maintain a healthy Homebrew installation.

3. Consider using Bold Brew for a more intuitive package management experience.

## Conclusion

These commands form the foundation of Homebrew usage. While mastering the command line is important, tools like Bold Brew can make package management more intuitive and efficient.

Remember to check the [Bold Brew documentation](https://bold-brew.com) for more tips and tricks on managing your Homebrew packages. 
```

## File: `site/content/blog/install-homebrew-macos.md`
```markdown
---
title: "How to Install and Configure Homebrew on macOS"
date: "2025-03-29"
description: "Learn how to install and configure Homebrew on macOS. A step-by-step guide to setting up the most popular package manager for macOS."
keywords: "Homebrew installation, macOS package manager, brew install, Homebrew setup, macOS development, package manager installation, brew configuration"
---

# How to Install and Configure Homebrew on macOS

Homebrew is the most popular package manager for macOS, making it easy to install and manage software packages. In this guide, we'll walk you through the process of installing and configuring Homebrew on your Mac.

## Prerequisites

Before installing Homebrew, make sure you have:
- macOS 10.15 or later
- Command Line Tools for Xcode installed
- A stable internet connection

## Installation Steps

1. First, install the Command Line Tools for Xcode:
```bash
xcode-select --install
```

2. Install Homebrew by running this command in Terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Add Homebrew to your PATH (if prompted):
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Verify Installation

Check if Homebrew is installed correctly:
```bash
brew --version
```

## Basic Configuration

1. Update Homebrew:
```bash
brew update
```

2. Upgrade all packages:
```bash
brew upgrade
```

3. Check system status:
```bash
brew doctor
```

## Common Issues and Solutions

1. **Permission Issues**
   - If you encounter permission errors, run:
   ```bash
   sudo chown -R $(whoami) /opt/homebrew
   ```

2. **Slow Downloads**
   - Consider using a mirror:
   ```bash
   export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
   export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
   ```

3. **Network Issues**
   - Check your internet connection
   - Try using a VPN if needed

## Next Steps

Now that you have Homebrew installed, you can:
1. Install packages using `brew install`
2. Search for packages using `brew search`
3. Update packages using `brew upgrade`
4. Remove packages using `brew uninstall`

For a more intuitive package management experience, consider using [Bold Brew](https://bold-brew.com), a modern Terminal User Interface (TUI) for Homebrew.

## Conclusion

Homebrew is an essential tool for macOS users, making it easy to install and manage software packages. With proper installation and configuration, you'll have a powerful package manager at your disposal.

Remember to keep Homebrew updated and run `brew doctor` regularly to maintain a healthy installation. 
```

## File: `site/content/blog/managing-homebrew-packages.md`
```markdown
---
title: "Managing Homebrew Packages on macOS with Bold Brew"
date: "2025-03-29"
description: "Learn how to efficiently manage Homebrew packages on macOS using Bold Brew. Discover best practices, tips, and tricks for package management."
keywords: "Homebrew, package management, macOS, Bold Brew, bbrew, terminal, package manager, TUI, terminal user interface, brew packages"
---

# Managing Homebrew Packages on macOS with Bold Brew

Managing Homebrew packages through the command line can be challenging, especially when dealing with multiple packages or complex dependencies. Bold Brew provides a modern Terminal User Interface (TUI) that makes package management more intuitive and efficient.

## Why Use Bold Brew?

Bold Brew offers several advantages over traditional command-line package management:

1. **Visual Interface**
   - Easy-to-read package lists
   - Clear dependency visualization
   - Intuitive navigation

2. **Efficient Workflow**
   - Quick package search
   - One-click installation/removal
   - Batch operations

3. **Better Organization**
   - Group packages by category
   - Track package status
   - Monitor system health

## Installation

Install Bold Brew using Homebrew:

```bash
brew install Valkyrie00/homebrew-bbrew/bbrew
```

## Key Features

### 1. Package Search
- Real-time search as you type
- Filter by name, description, or category
- View package details before installation

### 2. Package Management
- Install/remove packages with a single keypress
- Update packages individually or in bulk
- View package dependencies

### 3. System Monitoring
- Check Homebrew system status
- Monitor disk usage
- View installation logs

### 4. User Interface
- Keyboard-driven navigation
- Color-coded status indicators
- Contextual help

## Best Practices

1. **Regular Updates**
   - Keep packages up to date
   - Monitor for outdated packages
   - Check system health regularly

2. **Package Organization**
   - Group related packages
   - Track package purposes
   - Maintain a clean system

3. **Dependency Management**
   - Review dependencies before installation
   - Clean up orphaned packages
   - Monitor disk usage

## Tips and Tricks

1. **Keyboard Shortcuts**
   - `?` - Show help
   - `q` - Quit
   - `space` - Select/deselect
   - `enter` - Execute action

2. **Search Tips**
   - Use partial matches
   - Filter by category
   - Sort by various criteria

3. **Maintenance**
   - Regular cleanup
   - System health checks
   - Package updates

## Conclusion

Bold Brew transforms Homebrew package management from a command-line chore into an intuitive, visual experience. Whether you're a casual user or a power user, Bold Brew can help you manage your Homebrew packages more efficiently.

For more information, visit the [Bold Brew documentation](https://bold-brew.com) or check out our other guides on Homebrew management. 
```

## File: `site/content/blog/top-homebrew-packages-for-developers.md`
```markdown
---
title: "Top 20 Homebrew Packages for Developers in 2024"
date: "2025-04-12"
description: "Discover essential Homebrew packages for macOS developers. A curated list of the best development tools every programmer should install."
keywords: "Homebrew packages, macOS developer tools, best Homebrew packages, CLI tools, developer tools, Bold Brew, bbrew"
---

# Top 20 Homebrew Packages for Developers in 2024

Homebrew has revolutionized how developers install and manage software on macOS. In this article, we'll explore the 20 most useful Homebrew packages for developers in 2024, and how Bold Brew can make their management even easier.

## Version Control and Management Tools

### 1. git
The most widely used version control system in the world, essential for any developer.

```bash
brew install git
```

### 2. git-lfs
Git extension for managing large files.

```bash
brew install git-lfs
```

### 3. tig
A text interface for navigating Git repositories.

```bash
brew install tig
```

## Shell and Terminal

### 4. zsh
A powerful shell with numerous additional features compared to bash.

```bash
brew install zsh
```

### 5. tmux
A terminal multiplexer that allows you to manage multiple sessions in a single window.

```bash
brew install tmux
```

### 6. oh-my-zsh
Framework for managing zsh configuration (installable after zsh).

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Databases

### 7. postgresql
A powerful open-source SQL database.

```bash
brew install postgresql
```

### 8. mysql
The popular relational database management system.

```bash
brew install mysql
```

### 9. redis
In-memory NoSQL database for high-performance caching.

```bash
brew install redis
```

## Programming Languages and Runtimes

### 10. node
JavaScript runtime based on Chrome's V8 for backend development.

```bash
brew install node
```

### 11. python
Versatile programming language for data science, web development, and automation.

```bash
brew install python
```

### 12. go
Google's language known for performance and efficiency.

```bash
brew install go
```

## Network Utilities

### 13. wget
Utility for downloading content from the web.

```bash
brew install wget
```

### 14. curl
Tool for transferring data with URLs.

```bash
brew install curl
```

### 15. nmap
Powerful network scanning tool.

```bash
brew install nmap
```

## Productivity Tools

### 16. fzf
Command-line fuzzy finder for quick searches.

```bash
brew install fzf
```

### 17. ripgrep (rg)
An incredibly fast alternative to grep.

```bash
brew install ripgrep
```

### 18. htop
Enhanced interactive system monitor.

```bash
brew install htop
```

## Containerization

### 19. docker
Platform for developing, shipping, and running containerized applications.

```bash
brew install --cask docker
```

### 20. kubernetes-cli
CLI tool for managing Kubernetes clusters.

```bash
brew install kubernetes-cli
```

## The Package Management Challenge

While these tools are powerful, managing a growing number of Homebrew packages through the command line can become complicated:

- Forgetting which packages are installed
- Losing track of available updates
- Difficulty finding and removing unused packages
- Confusion between dependencies and main packages

## Bold Brew: An Elegant Solution

Bold Brew (bbrew) solves these challenges by offering an elegant TUI (Terminal User Interface) for managing your Homebrew packages:

### Advantages of Bold Brew

1. **Intuitive Visualization** - See all installed packages in an organized interface
2. **Simplified Updates** - Update single or multiple packages with a few keystrokes
3. **Instant Search** - Find new packages in real-time as you type
4. **Clear Dependencies** - Graphical display of package relationships
5. **Efficient Management** - Install and uninstall packages without memorizing commands

### Installing Bold Brew

You can install Bold Brew with a simple command:

```bash
brew install Valkyrie00/homebrew-bbrew/bbrew
```

Once installed, simply run:

```bash
bbrew
```

## Installation Workflow with Bold Brew

With Bold Brew, installing the 20 packages mentioned above becomes incredibly simple:

1. Start Bold Brew with `bbrew`
2. Press `/` to search for a package
3. Navigate with arrows and select with `space`
4. Press `i` to install selected packages

With this intuitive interface, you can manage dozens of packages in half the time required by the traditional command line.

## Conclusion

The Homebrew packages listed in this article are essential tools for any macOS developer in 2024. To manage them efficiently, Bold Brew offers a superior user experience that will save you time and frustration.

If you haven't already, try Bold Brew today:

```bash
brew install Valkyrie00/homebrew-bbrew/bbrew
```

Discover a more elegant and productive way to interact with Homebrew, and focus on what really matters: writing exceptional code.

**Do you have other favorite Homebrew packages that you think should be on the list? Share them in the comments below!**
```

## File: `site/templates/index.ejs`
```
<main>
    <section class="hero-section" aria-label="Hero">
        <div class="hero-bg-overlay"></div>
        <div class="container">
            <div class="hero-content">
                <img src="assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" class="logo-img animate-pulse" width="120" height="120">
                <h1 class="display-4">Bold Brew</h1>
                <h2 class="tagline"><code>bbrew</code></h2>
                <p class="lead">The modern Terminal UI for managing Homebrew packages and casks on macOS and Linux.</p>
                <div class="badges">
                    <img src="https://img.shields.io/github/v/release/Valkyrie00/bold-brew" alt="Version" width="100" height="20">
                    <img src="https://img.shields.io/github/license/Valkyrie00/bold-brew" alt="License" width="100" height="20">
                    <img src="https://img.shields.io/github/actions/workflow/status/Valkyrie00/bold-brew/release.yml" alt="Build Status" width="100" height="20">
                    <img src="https://github.com/Valkyrie00/bold-brew/workflows/Security/badge.svg" alt="Security" width="100" height="20">
                    <img src="https://img.shields.io/github/downloads/Valkyrie00/bold-brew/total" alt="Downloads" width="100" height="20">
                    <img src="https://img.shields.io/badge/Featured_in-Project_Bluefin-0091e2" alt="Project Bluefin" width="140" height="20">
                </div>
                <div class="hero-cta">
                    <a href="#install" class="btn-primary">Start Now</a>
                    <a href="https://github.com/Valkyrie00/bold-brew" class="btn-secondary" target="_blank">View on GitHub</a>
                </div>
            </div>
        </div>
    </section>

    <section class="install-section" id="install" aria-label="Installation">
        <div class="container">
            <h2>Installation</h2>
            <p class="lead text-center mb-4">Get started with Bold Brew in just one command</p>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="install-card">
                        <div class="install-step">
                            <div class="step-header">
                                <div class="step-number">⚡</div>
                                <h3>Quick Install</h3>
                            </div>
                            <div class="code-block">
                                <pre><code><span class="prompt">></span> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/install.sh)"</code></pre>
                                <button class="copy-btn" onclick="copyToClipboard(this)" aria-label="Copy command">
                                    <span class="copy-icon">⧉</span>
                                    <span class="copy-text">Copy</span>
                                </button>
                            </div>
                            <p class="install-note"><i>This installs Homebrew (if needed) + Bold Brew in one step</i></p>
                        </div>

                        <div class="install-step">
                            <div class="step-header">
                                <div class="step-number">▶</div>
                                <h3>Run Bold Brew</h3>
                            </div>
                            <div class="code-block">
                                <pre><code><span class="prompt">></span> bbrew</code></pre>
                                <button class="copy-btn" onclick="copyToClipboard(this)" aria-label="Copy command">
                                    <span class="copy-icon">⧉</span>
                                    <span class="copy-text">Copy</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="alternative-install">
                        <div class="divider">
                            <span>OR</span>
                        </div>
                        <p class="text-center">Already have Homebrew? Install directly:</p>
                        <div class="code-block" style="max-width: 500px; margin: 0 auto 1rem;">
                            <pre><code><span class="prompt">></span> brew install Valkyrie00/homebrew-bbrew/bbrew</code></pre>
                            <button class="copy-btn" onclick="copyToClipboard(this)" aria-label="Copy command">
                                <span class="copy-icon">⧉</span>
                                <span class="copy-text">Copy</span>
                            </button>
                        </div>
                        <p class="text-center" style="margin-top: 1rem;">Or download from GitHub</p>
                        <div class="text-center">
                            <a class="btn-download" href="https://github.com/Valkyrie00/bold-brew/releases" target="_blank" rel="noopener noreferrer">
                                <span class="download-icon">↓</span>
                                Download Latest Release
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="screenshots-section" aria-label="Screenshots">
        <div class="container">
            <h2>Screenshots</h2>
            <p class="lead text-center mb-4">Explore the Bold Brew interface and its features</p>

            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <figure class="screenshot-card">
                        <img src="assets/screenshots/bbrew-brewfile-screenshot.png" alt="Brewfile Mode showing package management interface" class="img-fluid" loading="lazy" width="400" height="300">
                        <figcaption class="screenshot-caption">
                            <p>Main Dashboard</p>
                        </figcaption>
                    </figure>
                </div>
                <div class="col-md-4 mb-4">
                    <figure class="screenshot-card">
                        <img src="assets/screenshots/bbrew-installed-screenshot.png" alt="Installed packages management view" class="img-fluid" loading="lazy" width="400" height="300">
                        <figcaption class="screenshot-caption">
                            <p>Handle Installed Packages</p>
                        </figcaption>
                    </figure>
                </div>
                <div class="col-md-4 mb-4">
                    <figure class="screenshot-card">
                        <img src="assets/screenshots/bbrew-search-screenshot.png" alt="Package search interface" class="img-fluid" loading="lazy" width="400" height="300">
                        <figcaption class="screenshot-caption">
                            <p>Search for Packages</p>
                        </figcaption>
                    </figure>
                </div>
            </div>
        </div>
    </section>

    <section class="bluefin-banner" style="background: linear-gradient(135deg, #0091e2 0%, #5865f2 100%); color: white; padding: 3rem 0; margin: 2rem 0;">
        <div class="container text-center">
            <h2 style="color: white; margin-bottom: 1rem;">🌟 Official Homebrew TUI for Project Bluefin</h2>
            <p class="lead" style="color: rgba(255,255,255,0.95); margin-bottom: 1.5rem;">
                Bold Brew is the official Terminal UI for managing Homebrew in <strong>Project Bluefin</strong>, 
                a next-generation Linux desktop serving tens of thousands of users worldwide.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="https://projectbluefin.io/" target="_blank" class="btn" style="background: white; color: #0091e2; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600;">
                    Learn About Bluefin →
                </a>
                <a href="blog/bold-brew-official-project-bluefin-tui.html" class="btn" style="background: rgba(255,255,255,0.2); color: white; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; border: 2px solid white;">
                    Read Announcement →
                </a>
            </div>
        </div>
    </section>

    <section id="features" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">Features</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-cube"></i>
                        <h3>Formulae & Casks</h3>
                        <p>Manage both CLI tools and GUI applications. Full support for Homebrew formulae and casks in one interface.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-filter"></i>
                        <h3>Smart Filters</h3>
                        <p>Filter by installed, outdated, leaves (explicitly installed), or casks. Find what you need instantly.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-search"></i>
                        <h3>Fuzzy Search</h3>
                        <p>Fast fuzzy search across all packages with real-time results and analytics integration.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-rocket"></i>
                        <h3>Real-time Updates</h3>
                        <p>Live feedback during installations, updates, and removals with detailed progress information.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-shield-alt"></i>
                        <h3>Secure & Compliant</h3>
                        <p>XDG Base Directory compliant with automated security scanning and vulnerability checks.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-keyboard"></i>
                        <h3>Keyboard Shortcuts</h3>
                        <p>Intuitive keybindings for all operations. Navigate and manage packages without touching the mouse.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-file-alt"></i>
                        <h3>Brewfile Mode</h3>
                        <p>Load curated package collections from local or remote Brewfiles. Perfect for team configs and themed installers.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <i class="fas fa-link"></i>
                        <h3>Remote Brewfiles</h3>
                        <p>Load Brewfiles directly from HTTPS URLs. Share configurations via GitHub, team repos, or any web server.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="latest-posts" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">Latest Articles</h2>
            <div class="row">
                <% posts.slice(0, 3).forEach(post => { %>
                    <div class="col-md-4">
                        <div class="blog-card">
                            <div class="post-meta">
                                <span class="date"><%= post.date %></span>
                            </div>
                            <h3><a href="<%= post.url %>"><%= post.title %></a></h3>
                            <p><%= post.excerpt %></p>
                            <a href="<%= post.url %>" class="read-more">Read more →</a>
                        </div>
                    </div>
                <% }); %>
            </div>
            <div class="text-center mt-4">
                <a href="blog/" class="btn btn-primary">View All Articles</a>
            </div>
        </div>
    </section>

    <section class="seo-content" aria-label="Additional Information">
        <div class="container">
            <h2>Manage Homebrew Packages and Casks with Bold Brew</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <p><strong>Bold Brew</strong> transforms the way developers manage <strong>Homebrew packages and casks</strong> across macOS and Linux with its elegant Terminal User Interface. Stop struggling with complex command-line syntax and enjoy a streamlined package management experience for both CLI tools and GUI applications.</p>

                    <h3>Why Developers Choose Bold Brew</h3>
                    <p>Managing your <strong>Homebrew ecosystem</strong> has never been easier. Bold Brew 2.0 provides complete support for both formulae (command-line tools) and casks (GUI applications), with real-time visual feedback for installations, updates, and package removals—all while maintaining the speed and efficiency you expect from terminal-based applications.</p>

                    <h3>Key Benefits for Developers</h3>
                    <ul>
                        <li><strong>Complete package management</strong> for both CLI tools and GUI applications</li>
                        <li><strong>Brewfile Mode</strong> for curated package collections from local or remote URLs</li>
                        <li><strong>Smart filtering</strong> by installed, outdated, leaves, or casks</li>
                        <li><strong>Faster package discovery</strong> with fuzzy search and analytics</li>
                        <li><strong>XDG Base Directory compliance</strong> for clean cache management</li>
                        <li><strong>Streamlined updates</strong> for all Homebrew packages with visual progress</li>
                        <li><strong>Keyboard-driven workflow</strong> without memorizing complex commands</li>
                    </ul>

                    <p>Trusted by <strong>Project Bluefin</strong> and used by <strong>tens of thousands of developers</strong>, Bold Brew integrates perfectly with your workflow while reducing cognitive load and increasing productivity on macOS and Linux.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="about-section" id="about" aria-label="About">
        <div class="container">
            <h2>About Bold Brew</h2>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <p class="lead">The modern Homebrew TUI that developers trust—from macOS to Linux</p>

                    <h3>The Bold Brew Advantage</h3>
                    <p>Bold Brew was designed from the ground up to address the limitations of traditional Homebrew management. By providing a Terminal User Interface (TUI), Bold Brew combines the efficiency of command-line operations with intuitive visual feedback. Version 2.0 brings complete support for both formulae (CLI tools) and casks (GUI applications).</p>

                    <h3>Complete Homebrew Integration</h3>
                    <p>As the official Homebrew TUI for Project Bluefin, Bold Brew seamlessly integrates with your existing Homebrew installation. All operations—from searching packages to managing casks, filtering leaves, and updating dependencies—are visualized through an elegant interface while preserving the speed and reliability of Homebrew's core functionality.</p>

                    <div class="compatibility-info">
                        <h4>Platform Support</h4>
                        <ul>
                            <li><strong>macOS:</strong> Full support (10.15 Catalina or newer)</li>
                            <li><strong>Linux:</strong> Full support (Project Bluefin, Linuxbrew, Homebrew on Linux)</li>
                            <li>Requires: Homebrew installation, Terminal with true color support</li>
                        </ul>
                    </div>

                    <h3>Trusted by the Community</h3>
                    <p>Bold Brew is pre-installed in Project Bluefin, serving tens of thousands of developers worldwide. Whether you're a seasoned developer or new to package management, Bold Brew streamlines your workflow and makes Homebrew more accessible than ever before.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="faq-section" aria-label="FAQ">
        <div class="container">
            <h2>FAQ</h2>
            <p class="lead text-center mb-5">Frequently asked questions about Bold Brew</p>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="accordion faq-accordion" id="faqAccordion">
                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq1">
                                <h3>What is Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq1" class="faq-answer collapse show" data-bs-parent="#faqAccordion">
                                <p>Bold Brew (bbrew) is a modern Terminal User Interface for managing Homebrew packages and casks on macOS and Linux. It provides an elegant and intuitive way to install, update, and manage both command-line tools (formulae) and GUI applications (casks) without memorizing complex commands. It's the official Homebrew TUI for Project Bluefin.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq2">
                                <h3>How do I install Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq2" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>You can install Bold Brew in two ways:</p>
                                <ol>
                                    <li>Using Homebrew: <code>brew install Valkyrie00/homebrew-bbrew/bbrew</code></li>
                                    <li>Downloading the latest release from our GitHub repository</li>
                                </ol>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq3">
                                <h3>How do I update Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq3" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Run <code>brew upgrade bbrew</code> to update the application to the latest version.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq4">
                                <h3>How do I remove Bold Brew?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq4" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Use <code>brew remove bbrew</code> if you need to uninstall it from your system.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq5">
                                <h3>Does it work on Linux or Windows?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq5" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Yes! Bold Brew has full support for Linux (it's the official TUI for Project Bluefin). It works anywhere Homebrew is installed.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq7">
                                <h3>What's new in Bold Brew 2.0?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq7" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Version 2.0 introduces full Homebrew Casks support (GUI applications), a Leaves filter (explicitly installed packages), XDG Base Directory compliance, enhanced security scanning, and many performance improvements. <a href="blog/bold-brew-2-0-cask-support.html">Read the full announcement</a>.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq8">
                                <h3>What is Brewfile Mode?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq8" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Brewfile Mode lets you launch Bold Brew with a curated list of packages instead of the full catalog. Use <code>bbrew -f /path/to/Brewfile</code> for local files or <code>bbrew -f https://...</code> for remote URLs. Perfect for team configurations, themed installers, and project-specific setups. <a href="blog/brewfile-mode-remote-support.html">Learn more</a>.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq6">
                                <h3>Where can I report issues or request features?</h3>
                                <div class="faq-icon">
                                    <span class="plus">+</span>
                                    <span class="minus">−</span>
                                </div>
                            </div>
                            <div id="faq6" class="faq-answer collapse" data-bs-parent="#faqAccordion">
                                <p>Feel free to open an issue on our <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub repository</a>.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>
```

## File: `site/templates/layout.ejs`
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%= title %></title>
    <meta name="description" content="<%= description %>">
    <meta name="keywords" content="<%= keywords %>">
    <meta name="author" content="Valkyrie00">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#1a1a1a">

    <!-- DNS Prefetch & Preconnect for Performance -->
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>

    <!-- OpenGraph Tags -->
    <meta property="og:title" content="<%= title %>">
    <meta property="og:description" content="<%= description %>">
    <meta property="og:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta property="og:image:width" content="200">
    <meta property="og:image:height" content="200">
    <meta property="og:image:alt" content="Bold Brew Logo">
    <meta property="og:url" content="<%= canonicalUrl %>">
    <meta property="og:type" content="<%= ogType || 'website' %>">
    <meta property="og:site_name" content="Bold Brew">

    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="<%= title %>">
    <meta name="twitter:description" content="<%= description %>">
    <meta name="twitter:image" content="https://bold-brew.com/assets/logo/bbrew-logo-rounded.png">
    <meta name="twitter:image:alt" content="Bold Brew Logo">
    <meta name="twitter:creator" content="@Valkyrie00">
    <meta name="twitter:site" content="@Valkyrie00">

    <!-- Additional SEO Meta Tags -->
    <meta name="application-name" content="Bold Brew">
    <meta name="apple-mobile-web-app-title" content="Bold Brew">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#1a1a1a">
    <meta name="msapplication-config" content="none">

    <link rel="canonical" href="<%= canonicalUrl %>">
    <link rel="alternate" hreflang="en" href="<%= canonicalUrl %>">
    <link rel="alternate" hreflang="x-default" href="<%= canonicalUrl %>">
    
    <!-- Stylesheets -->
    <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" as="stylesheet">
    <link rel="preload" href="/assets/css/styles.css" as="stylesheet">
    <link rel="preload" href="/assets/bbrew-logo-nobg.png" as="image">
    
    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/styles.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="icon" href="/assets/ico/bbrew-16.ico" sizes="16x16" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-24.ico" sizes="24x24" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-32.ico" sizes="32x32" type="image/x-icon">
    <link rel="icon" href="/assets/ico/bbrew-48.ico" sizes="48x48" type="image/x-icon">
    <link rel="manifest" href="/manifest.json">

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Bold Brew (bbrew)",
      "operatingSystem": ["macOS", "Linux"],
      "applicationCategory": "DeveloperApplication",
      "description": "Bold Brew: A modern TUI interface for managing Homebrew packages and casks on macOS and Linux. Effortlessly install, search, update, and remove packages with an elegant and intuitive interface.",
      "url": "https://bold-brew.com",
      "author": {
        "@type": "Person",
        "name": "Valkyrie00"
      },
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
    </script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MM4FCW9XZM"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MM4FCW9XZM');
    </script>
</head>
<body>
    <%- include('partials/header') %>

    <%- content %>

    <%- include('partials/footer') %>

    <!-- Back to top button -->
    <button class="back-to-top" aria-label="Torna in alto">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>

    <!-- Scripts -->
    <script>
        function copyToClipboard(button) {
            const preEl = button.parentElement.querySelector('pre');
            const codeText = preEl.textContent;
            const cleanText = codeText.replace(/^>\s/, '');
        
            navigator.clipboard.writeText(cleanText).then(() => {
                const copyText = button.querySelector('.copy-text');
                copyText.textContent = 'Copied!';
        
                setTimeout(() => {
                    copyText.textContent = 'Copy';
                }, 2000);
            });
        }

        // Chiudi il menu mobile quando si clicca su un link
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            const menuToggle = document.getElementById('navbarNav');
            const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle: false});

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 992) { // Solo su mobile
                        bsCollapse.hide();
                    }
                });
            });

            // Gestione del pulsante back-to-top
            const backToTop = document.querySelector('.back-to-top');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('visible');
                } else {
                    backToTop.classList.remove('visible');
                }
            });

            backToTop.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>

</body>
</html> 
```

## File: `site/templates/blog/index.ejs`
```
<main class="container my-5">
    <% if (locals.breadcrumb) { %>
        <%- include('../partials/breadcrumb') %>
    <% } %>

    <header class="mb-5">
        <h1>Bold Brew Blog</h1>
        <p class="lead">Tips, tutorials, and guides for managing Homebrew packages and casks</p>
    </header>

    <div class="row">
        <div class="col-lg-8">
            <div class="blog-posts">
                <% posts.forEach(post => { %>
                    <article class="blog-post mb-5">
                        <div class="post-meta">
                            <span class="date"><%= post.date %></span>
                            <span class="author">By Valkyrie00</span>
                        </div>
                        <h2><a href="<%= post.url %>"><%= post.title %></a></h2>
                        <p class="excerpt"><%= post.excerpt %></p>
                        <div class="tags">
                            <span class="tag">Homebrew</span>
                            <span class="tag">TUI</span>
                            <span class="tag">Command Line</span>
                        </div>
                        <a href="<%= post.url %>" class="read-more">Read more →</a>
                    </article>
                <% }); %>
            </div>
        </div>

        <aside class="col-lg-4">
            <div class="sidebar">
                <div class="widget mb-4">
                    <h3>About Bold Brew</h3>
                    <p>Bold Brew is a modern Terminal User Interface (TUI) for managing Homebrew packages and casks on macOS and Linux.</p>
                    <a href="/#install" class="btn btn-primary">Install Now</a>
                </div>

                <div class="widget mb-4">
                    <h3>Popular Tags</h3>
                    <div class="tags">
                        <a href="#" class="tag">Homebrew</a>
                        <a href="#" class="tag">TUI</a>
                        <a href="#" class="tag">Casks</a>
                        <a href="#" class="tag">Brewfile</a>
                        <a href="#" class="tag">Package Management</a>
                        <a href="#" class="tag">Project Bluefin</a>
                    </div>
                </div>

                <div class="widget mb-4">
                    <h3>Follow Us</h3>
                    <div class="social-links">
                        <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </div>
                </div>
            </div>
        </aside>
    </div>
</main>
```

## File: `site/templates/blog/post.ejs`
```
<main class="container my-5">
    <% if (locals.breadcrumb) { %>
        <%- include('../partials/breadcrumb') %>
    <% } %>

    <article>
        <header class="mb-5">
            <h1><%= title %></h1>
            <div class="meta">
                <span class="date"><%= date %></span>
                <span class="author">By Valkyrie00</span>
            </div>
        </header>

        <div class="content">
            <%- content %>
        </div>

        <footer class="mt-5">
            <div class="tags">
                <span class="tag">Homebrew</span>
                <span class="tag">macOS</span>
                <span class="tag">Command Line</span>
                <span class="tag">Development Tools</span>
            </div>
        </footer>
    </article>
</main>
```

## File: `site/templates/partials/breadcrumb.ejs`
```
<div class="container my-4">
    <nav aria-label="breadcrumb">
        <div class="breadcrumb">
            <% breadcrumb.forEach((item, index) => { %>
                <div class="breadcrumb-item <%= index === breadcrumb.length - 1 ? 'active' : '' %>">
                    <% if (index === breadcrumb.length - 1) { %>
                        <%= item.text %>
                    <% } else { %>
                        <a href="<%= item.url %>"><%= item.text %></a>
                    <% } %>
                </div>
            <% }); %>
        </div>
    </nav>
</div> 
```

## File: `site/templates/partials/footer.ejs`
```
<footer>
    <div class="container">
        <p>&copy; <%= new Date().getFullYear() %> Bold Brew | <a href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a></p>
    </div>
</footer>
```

## File: `site/templates/partials/header.ejs`
```
<header>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <img src="/assets/bbrew-logo-nobg.png" alt="Bold Brew Logo" width="32" height="32">
                <span>Bold Brew</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#install">Install</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Valkyrie00/bold-brew" target="_blank" rel="noopener noreferrer">GitHub</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>
```

