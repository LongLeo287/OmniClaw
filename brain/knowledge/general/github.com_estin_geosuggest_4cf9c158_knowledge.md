---
id: github.com-estin-geosuggest-4cf9c158-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.644206
---

# KNOWLEDGE EXTRACT: github.com_estin_geosuggest_4cf9c158
> **Extracted on:** 2026-04-01 14:44:17
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524093/github.com_estin_geosuggest_4cf9c158

---

## File: `.gitignore`
```
.vim
/target
examples/*/target
**/dist
Cargo.lock
```

## File: `Cargo.toml`
```
[workspace]
resolver = "2"
members = [
  "geosuggest",
  "geosuggest-*",
]

[workspace.package]
version = "0.8.2"
authors = ["geosuggest contributors"]
license = "MIT"

[workspace.dependencies]
anyhow             = "1"
tracing            = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter", "fmt"] }
test-log           = { version = "0.2", default-features = false, features = ["trace"] }

# core
serde      = { version = "1", features = ["derive"] }
serde_json = "1"
config     = "0.15"
csv        = "1"
rayon      = "1"
strsim     = "0.11"
kiddo      = { version = "5.2", default-features = false, features = ["rkyv_08"] }
geoip2     = "0.1.7"

rkyv      = { version = "0.8" }
itertools = "0.14"

# service
oaph       = { version = "0.2" }
ntex       = { version = "3.0.0-pre.9", features=["tokio"] }
ntex-files = "3"
ntex-cors  = "3"

# utils
zip = "7"
reqwest = { version = "0.12", features = [
  "rustls-tls",
], default-features = false }
tokio = { version = "1", features = ["macros", "net", "rt-multi-thread"] }
futures = "0.3"
clap = { version = "4.5", features = ["derive"] }
```

## File: `LICENSE`
```
Copyright (c) 2021 geosuggest contributors

Permission is hereby granted, free of charge, to any
person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the
Software without restriction, including without
limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
<div align="center">
  <p><h1>geosuggest</h1> </p>
  <p><strong>Library/Service to suggest and to find nearest by coordinates cities</strong></p>
  <p></p>
</div>

[Live demo](https://geosuggest.etatarkin.ru/) with [sources](https://github.com/estin/geosuggest/tree/master/geosuggest-demo)

Main features:
 - library or service modes
 - build index by free gazetteer data from [geonames.org](https://www.geonames.org/)
 - suggest city by name
 - find nearest city by coordinates
 - MaxMind GeoIP2(Lite) city database support
 - multi-language (based on configured index options)
 - simple REST http [api](https://geosuggest.etatarkin.ru/swagger)
 - no external services used

### Based on:
 - [strsim](https://crates.io/crates/strsim)
 - [kiddo](https://crates.io/crates/kiddo)
 - [geoip2](https://crates.io/crates/geoip2)
 - [rkyv](https://crates.io/crates/rkyv)
 - [ntex](https://crates.io/crates/ntex)


## Library

Crate usage [example](https://github.com/estin/geosuggest/blob/master/geosuggest-examples/src/simple.rs)

```console
$ cargo run -p geosuggest-examples --release --bin simple
```


## Service

Install from sources (preferred).

```console
$ git clone https://github.com/estin/geosuggest.git
$ cd geosuggest
$ cargo build --release
```

Build index file

```console
$ cargo run -p geosuggest-utils --bin geosuggest-build-index --release --features=cli,tracing -- \
    from-urls \
    --languages=ru,uk,be,zh,ja \
    --output=/tmp/geosuggest-index.rkyv
```

Run

```console
$ GEOSUGGEST__INDEX_FILE=/tmp/geosuggest-index.rkyv \
    GEOSUGGEST__HOST=127.0.0.1 \
    GEOSUGGEST__PORT=8080 \
    GEOSUGGEST__URL_PATH_PREFIX="/" \
    cargo run -p geosuggest --bin geosuggest --release
```

Check

```console
$ curl -s "http://127.0.0.1:8080/api/city/suggest?pattern=Voronezh&limit=1" | jq
```

```json
{
  "items": [
    {
      "id": 472045,
      "name": "Voronezh",
      "country": {
        "id": 2017370,
        "code": "RU",
        "name": "Russia"
      },
      "admin_division": {
        "id": 472039,
        "code": "RU.86",
        "name": "Voronezj"
      },
      "admin2_division": null,
      "timezone": "Europe/Moscow",
      "latitude": 51.67204,
      "longitude": 39.1843,
      "population": 848752
    }
  ],
  "time": 24
}
```

See also demo [Dockerfile](https://github.com/estin/geosuggest/blob/master/geosuggest-demo/Dockerfile)

## Test

```console
$ cargo test --workspace
```

## License

This project is licensed under

* MIT license ([LICENSE](LICENSE) or [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT))
```

## File: `geosuggest/Cargo.toml`
```
[package]
name = "geosuggest"
version.workspace = true
authors.workspace = true
description = "HTTP service to suggest cities by name or find nearest by coordinates"
readme = "README.md"
keywords = ["geocoding", "service"]
repository = "https://github.com/estin/geosuggest.git"
documentation = "https://docs.rs/geosuggest/"
categories = ["web-programming::http-server"]
license = "MIT"
edition = "2021"

default-run = "geosuggest"

[[bin]]
name = "geosuggest"
path = "src/main.rs"

[features]
default = ["tokio", "geoip2", "tracing"]
geoip2 = ["geosuggest-core/geoip2"]
neon = ["ntex/neon"]
tokio = ["ntex/tokio"]
tracing = ["dep:tracing", "dep:tracing-subscriber", "geosuggest-core/tracing"]

[dependencies]
tracing = { workspace = true, optional = true }
tracing-subscriber = { workspace = true, optional = true }
serde.workspace = true
ntex.workspace = true
ntex-files.workspace = true
ntex-cors.workspace = true
config.workspace = true

geosuggest-core = { path = "../geosuggest-core", version = "0.8", features = ["oaph"] }

# openapi3
oaph.workspace = true 

[dev-dependencies]
serde_json = "1"
test-log.workspace = true
```

## File: `geosuggest/README.md`
```markdown
../README.md
```

## File: `geosuggest/defaults.toml`
```
host = "127.0.0.1"
port = "8090"
url_path_prefix = "/"
index_file = "./geosuggest-index.json"
```

## File: `geosuggest/src/main.rs`
```rust
use std::boxed::Box;
use std::sync::Arc;
use std::time::Instant;

#[cfg(feature = "tracing")]
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

#[cfg(feature = "geoip2")]
use std::net::IpAddr;
#[cfg(feature = "geoip2")]
use std::str::FromStr;

use ntex::web::{self, middleware, App, HttpRequest, HttpResponse};
use ntex_cors::Cors;
use ntex_files as fs;
use serde::{Deserialize, Serialize};

use geosuggest_core::{index::ArchivedCitiesRecord, storage, Engine};

// openapi3
use oaph::{
    schemars::{self, JsonSchema},
    OpenApiPlaceHolder,
};

mod settings;

const DEFAULT_K: f32 = 0.000000005;
const DEFAULT_NEAREST_CITIES_LIMIT: usize = 10;
const VERSION: &str = env!("CARGO_PKG_VERSION");

pub struct StaticEngine(Engine<'static>);

impl std::ops::Deref for StaticEngine {
    type Target = Engine<'static>;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

pub type SharedEngine = Arc<&'static mut Engine<'static>>;

#[derive(Debug, Deserialize, JsonSchema)]
pub struct GetCityQuery {
    /// geonameid of the City
    id: u32,
    /// isolanguage code
    lang: Option<String>,
}

#[derive(Debug, Deserialize, JsonSchema)]
pub struct GetCapitalQuery {
    lat: Option<f32>,
    lng: Option<f32>,
    /// IP to check, if not declared then `Forwarded` header will used or peer ip as last chance
    #[cfg(feature = "geoip2")]
    ip: Option<String>,
    /// geonameid of the City
    country_code: Option<String>,
    /// isolanguage code
    lang: Option<String>,
}

pub enum GetCapitalLookup<'a> {
    Coords {
        lat: f32,
        lng: f32,
    },
    CountryCode(&'a str),
    #[cfg(feature = "geoip2")]
    Ip(&'a str),
}

impl GetCapitalQuery {
    fn lookups<'a>(&'a self) -> impl Iterator<Item = GetCapitalLookup<'a>> {
        [
            self.lat
                .zip(self.lng)
                .map(|(lat, lng)| GetCapitalLookup::Coords { lat, lng }),
            #[cfg(feature = "geoip2")]
            self.ip.as_deref().map(GetCapitalLookup::Ip),
            self.country_code
                .as_deref()
                .map(GetCapitalLookup::CountryCode),
        ]
        .into_iter()
        .flatten()
    }
}

// TODO self.countries.split(",").as_slice()
// https://github.com/rust-lang/rust/issues/96137
fn get_countries_filter(countries: &Option<String>) -> Option<Vec<&str>> {
    countries.as_deref().map(|c| c.split(',').collect())
}

#[derive(Debug, Deserialize, JsonSchema)]
pub struct SuggestQuery {
    pattern: String,
    limit: Option<usize>,
    /// isolanguage code
    lang: Option<String>,
    /// min score of Jaro Winkler similarity (by default 0.8)
    min_score: Option<f32>,
    /// comma separated country code (2-letter) to pre-filter search
    countries: Option<String>,
}

#[derive(Debug, Deserialize, JsonSchema)]
pub struct ReverseQuery {
    lat: f32,
    lng: f32,
    limit: Option<usize>,
    /// isolanguage code
    lang: Option<String>,
    /// distance correction coefficient by city population `score(item) = item.distance - k * item.city.population`
    /// by default `0.000000005`
    k: Option<f32>,
    /// neareset cities to apply distance correction coefficient by population
    /// by default 10
    nearest_limit: Option<usize>,
    /// comma separated country code (2-letter) to pre-filter search
    countries: Option<String>,
}

#[cfg(feature = "geoip2")]
#[derive(Debug, Deserialize, JsonSchema)]
pub struct GeoIP2Query {
    /// IP to check, if not declared then `Forwarded` header will used or peer ip as last chance
    ip: Option<String>,
    /// isolanguage code
    lang: Option<String>,
}

#[derive(Serialize, JsonSchema)]
pub struct GetCityResult<'a> {
    city: Option<CityResultItem<'a>>,
    /// elapsed time in ms
    time: usize,
}

#[derive(Serialize, JsonSchema)]
pub struct GetCapitalResult<'a> {
    city: Option<CityResultItem<'a>>,
    /// elapsed time in ms
    time: usize,
}

#[derive(Serialize, JsonSchema)]
pub struct SuggestResult<'a> {
    items: Vec<CityResultItem<'a>>,
    /// elapsed time in ms
    time: usize,
}

#[derive(Serialize, JsonSchema)]
pub struct ReverseResult<'a> {
    items: Vec<ReverseResultItem<'a>>,
    /// elapsed time in ms
    time: usize,
}

#[derive(Serialize, JsonSchema)]
pub struct ReverseResultItem<'a> {
    city: CityResultItem<'a>,
    distance: f32,
    score: f32,
}

#[derive(Serialize, JsonSchema)]
pub struct CountryItem<'a> {
    id: u32,
    code: &'a str,
    name: &'a str,
}

#[derive(Serialize, JsonSchema)]
pub struct AdminDivisionItem<'a> {
    id: u32,
    code: &'a str,
    name: &'a str,
}

#[derive(Serialize, JsonSchema)]
pub struct CityResultItem<'a> {
    id: u32,
    name: &'a str,
    country: Option<CountryItem<'a>>,
    admin_division: Option<AdminDivisionItem<'a>>,
    admin2_division: Option<AdminDivisionItem<'a>>,
    timezone: &'a str,
    latitude: f32,
    longitude: f32,
    population: u32,
}

#[cfg(feature = "geoip2")]
#[derive(Serialize, JsonSchema)]
pub struct GeoIP2Result<'a> {
    city: Option<CityResultItem<'a>>,
    for_ip: String,
    /// elapsed time in ms
    time: usize,
}

impl<'a> CityResultItem<'a> {
    pub fn from_city(item: &'a ArchivedCitiesRecord, lang: Option<&'a str>) -> Self {
        let name = match (lang, item.names.as_ref()) {
            (Some(lang), Some(names)) => names.get(lang).unwrap_or(&item.name),
            _ => &item.name,
        };

        let country = if let Some(country) = item.country.as_ref() {
            let country_name = match (lang, item.country_names.as_ref()) {
                (Some(lang), Some(names)) => names
                    .get(lang)
                    .map(|v| v.as_str())
                    .unwrap_or(country.name.as_str()),
                _ => &country.name,
            };
            Some(CountryItem {
                id: country.id.to_native(),
                code: &country.code,
                name: country_name,
            })
        } else {
            None
        };

        let admin_division = if let Some(admin1) = item.admin_division.as_ref() {
            let admin1_name = match (lang, item.admin1_names.as_ref()) {
                (Some(lang), Some(names)) => names.get(lang).unwrap_or(&admin1.name),
                _ => &admin1.name,
            };
            Some(AdminDivisionItem {
                id: admin1.id.to_native(),
                code: &admin1.code,
                name: admin1_name,
            })
        } else {
            None
        };

        let admin2_division = if let Some(admin2) = item.admin2_division.as_ref() {
            let admin2_name = match (lang, item.admin2_names.as_ref()) {
                (Some(lang), Some(names)) => names.get(lang).unwrap_or(&admin2.name),
                _ => &admin2.name,
            };
            Some(AdminDivisionItem {
                id: admin2.id.to_native(),
                code: &admin2.code,
                name: admin2_name,
            })
        } else {
            None
        };

        CityResultItem {
            id: item.id.to_native(),
            name,
            country,
            admin_division,
            admin2_division,
            timezone: &item.timezone,
            latitude: item.latitude.to_native(),
            longitude: item.longitude.to_native(),
            population: item.population.to_native(),
        }
    }
}

pub async fn city_get(
    engine: web::types::State<SharedEngine>,
    web::types::Query(query): web::types::Query<GetCityQuery>,
    _req: HttpRequest,
) -> HttpResponse {
    let now = Instant::now();

    let city = engine
        .get(&query.id)
        .map(|city| CityResultItem::from_city(city, query.lang.as_deref()));

    HttpResponse::Ok().json(&GetCityResult {
        time: now.elapsed().as_millis() as usize,
        city,
    })
}

#[cfg(feature = "geoip2")]
fn extract_ip_addr(ip_param: Option<&str>, req: &HttpRequest) -> Result<IpAddr, String> {
    let conn_info = req.connection_info();
    ip_param
        .filter(|ip| *ip != "client")
        .or_else(|| {
            req.headers()
                .get(ntex::http::header::FORWARDED)
                .and_then(|val| val.to_str().ok())
        })
        .or_else(|| {
            conn_info
                .remote()
                .and_then(|remote| remote.split(':').take(1).next())
        })
        .map(|ip_str| {
            IpAddr::from_str(ip_str)
                .map_err(|err| format!("Invalid ip addr: {ip_str} error: {err}"))
        })
        .or_else(|| req.peer_addr().map(|addr| Ok(addr.ip())))
        .ok_or_else(|| "IP address not provided".to_owned())
        .flatten()
}

fn get_country_code<'a>(
    engine: &'a SharedEngine,
    lookup: GetCapitalLookup<'a>,
    req: &'a HttpRequest,
) -> Result<Option<&'a str>, String> {
    Ok(match lookup {
        GetCapitalLookup::Coords { lat, lng } => engine
            .reverse::<&str>((lat, lng), 1, None, None)
            .and_then(|items| items.into_iter().next())
            .and_then(|item| item.city.country.as_ref())
            .map(|country| country.code.as_str()),
        #[cfg(feature = "geoip2")]
        GetCapitalLookup::Ip(ip) => {
            let addr = extract_ip_addr(Some(ip), req)?;

            engine
                .geoip2_lookup(addr)
                .and_then(|city| city.country.as_ref())
                .map(|country| country.code.as_str())
        }
        GetCapitalLookup::CountryCode(country_code) => Some(country_code),
    })
}

pub async fn capital(
    engine: web::types::State<SharedEngine>,
    web::types::Query(query): web::types::Query<GetCapitalQuery>,
    req: HttpRequest,
) -> HttpResponse {
    let now = Instant::now();

    let mut err = None;

    for lookup in query.lookups() {
        let country_code = match get_country_code(&engine, lookup, &req) {
            Ok(Some(country_code)) => country_code,
            Ok(None) => continue,
            Err(e) => {
                err = Some(e);
                continue;
            }
        };

        let Some(city) = engine.capital(country_code) else {
            continue;
        };

        return HttpResponse::Ok().json(&GetCapitalResult {
            time: now.elapsed().as_millis() as usize,
            city: Some(CityResultItem::from_city(city, query.lang.as_deref())),
        });
    }

    if let Some(err) = err {
        return HttpResponse::BadRequest().body(err);
    }

    HttpResponse::Ok().json(&GetCapitalResult {
        time: now.elapsed().as_millis() as usize,
        city: None,
    })
}

pub async fn suggest(
    engine: web::types::State<SharedEngine>,
    web::types::Query(query): web::types::Query<SuggestQuery>,
    _req: HttpRequest,
) -> HttpResponse {
    let now = Instant::now();

    let result = engine
        .suggest(
            query.pattern.as_str(),
            query.limit.unwrap_or(10),
            query.min_score,
            get_countries_filter(&query.countries).as_deref(),
        )
        .iter()
        .map(|item| CityResultItem::from_city(item, query.lang.as_deref()))
        .collect::<Vec<CityResultItem>>();

    HttpResponse::Ok().json(&SuggestResult {
        time: now.elapsed().as_millis() as usize,
        items: result,
    })
}

pub async fn reverse(
    engine: web::types::State<SharedEngine>,
    web::types::Query(query): web::types::Query<ReverseQuery>,
    _req: HttpRequest,
) -> HttpResponse {
    let now = Instant::now();

    let items = engine
        .reverse(
            (query.lat, query.lng),
            query.nearest_limit.unwrap_or(DEFAULT_NEAREST_CITIES_LIMIT),
            Some(query.k.unwrap_or(DEFAULT_K)),
            get_countries_filter(&query.countries).as_deref(),
        )
        .unwrap_or_default();

    HttpResponse::Ok().json(&ReverseResult {
        time: now.elapsed().as_millis() as usize,
        items: items
            .iter()
            .take(query.limit.unwrap_or(DEFAULT_NEAREST_CITIES_LIMIT))
            .map(|item| ReverseResultItem {
                city: CityResultItem::from_city(item.city, query.lang.as_deref()),
                distance: item.distance,
                score: item.score,
            })
            .collect(),
    })
}

#[cfg(feature = "geoip2")]
pub async fn geoip2(
    engine: web::types::State<SharedEngine>,
    web::types::Query(query): web::types::Query<GeoIP2Query>,
    req: HttpRequest,
) -> HttpResponse {
    let now = Instant::now();

    let addr = match extract_ip_addr(query.ip.as_deref(), &req) {
        Ok(addr) => addr,
        Err(err) => return HttpResponse::BadRequest().body(err),
    };

    let result = engine.geoip2_lookup(addr);

    HttpResponse::Ok().json(&GeoIP2Result {
        time: now.elapsed().as_millis() as usize,
        for_ip: addr.to_string(),
        city: result.map(|item| CityResultItem::from_city(item, query.lang.as_deref())),
    })
}

fn generate_openapi_files(settings: &settings::Settings) -> Result<(), Box<dyn std::error::Error>> {
    let openapi3_yaml_path = std::env::temp_dir().join("openapi3.yaml");

    // render openapi3 yaml to temporary file
    let aoph = OpenApiPlaceHolder::new()
        .substitute("version", VERSION)
        .substitute("url_path_prefix", &settings.url_path_prefix)
        .query_params::<GetCityQuery>("GetCityQuery")?
        .query_params::<GetCapitalQuery>("GetCapitalQuery")?
        .query_params::<SuggestQuery>("SuggestQuery")?
        .query_params::<ReverseQuery>("ReverseQuery")?
        .schema::<GetCityResult>("GetCityResult")?
        .schema::<GetCapitalResult>("GetCapitalResult")?
        .schema::<SuggestResult>("SuggestResult")?
        .schema::<ReverseResult>("ReverseResult")?;

    #[cfg(feature = "geoip2")]
    let aoph = {
        aoph.query_params::<GeoIP2Query>("GeoIP2Query")?
            .schema::<GeoIP2Result>("GeoIP2Result")?
    };

    aoph.render_to_file(include_str!("openapi3.yaml"), &openapi3_yaml_path)?;

    #[cfg(feature = "tracing")]
    tracing::info!("openapi3 file: {:?}", openapi3_yaml_path.to_str());

    let title = format!("geosuggest v{}", VERSION);

    let openapi3_url_path = std::path::Path::new(&settings.url_path_prefix).join("openapi3.yaml");
    let openapi3_url_path = openapi3_url_path
        .to_str()
        .ok_or("Failed to build openapi3 url")?;

    // render swagger ui html to temporary file
    OpenApiPlaceHolder::swagger_ui_html_to_file(
        openapi3_url_path,
        &title,
        std::env::temp_dir().join("swagger-ui.html"),
    )?;

    // render redoc ui html to temporary file
    OpenApiPlaceHolder::redoc_ui_html_to_file(
        openapi3_url_path,
        &title,
        std::env::temp_dir().join("redoc-ui.html"),
    )?;

    Ok(())
}

#[ntex::main]
async fn main() -> std::io::Result<()> {
    // logging
    #[cfg(feature = "tracing")]
    {
        let subscriber = tracing_subscriber::registry()
            .with(tracing_subscriber::EnvFilter::new(
                std::env::var("RUST_LOG").unwrap_or_else(|_| "info".into()),
            ))
            .with(tracing_subscriber::fmt::layer());
        subscriber.init();
    }

    let settings = settings::Settings::new().expect("On read settings");
    #[cfg(feature = "tracing")]
    tracing::info!("Settings are:\n{:#?}", settings);

    // generate files for openapi3.yaml and swagger ui
    generate_openapi_files(&settings).expect("On generate openapi3 files");

    if settings.index_file.is_empty() {
        panic!("Please set `index_file`");
    }

    let storage = storage::Storage::new();

    let mut engine_data = storage
        .load_from(&settings.index_file)
        .unwrap_or_else(|e| panic!("On build engine from file: {} - {}", settings.index_file, e));

    #[cfg(feature = "geoip2")]
    if let Some(geoip2_file) = settings.geoip2_file.as_ref() {
        engine_data
            .load_geoip2(geoip2_file)
            .unwrap_or_else(|_| panic!("On read geoip2 file from {}", geoip2_file));
    }

    // build static engine
    let engine_data = Box::new(engine_data);
    let engine_data = Box::leak(engine_data);
    let engine = engine_data
        .as_engine()
        .expect("Failed to initialize engine");
    let engine = Box::new(engine);
    let static_engine = Box::leak(engine);
    let shared_engine = Arc::new(static_engine);
    let shared_engine_clone = shared_engine.clone();

    let settings_clone = settings.clone();

    let listen_on = format!("{}:{}", settings.host, settings.port);
    #[cfg(feature = "tracing")]
    tracing::info!("Listen on {}", listen_on);

    web::server(async move || {
        let shared_engine = shared_engine_clone.clone();
        let settings = settings_clone.clone();

        App::new()
            .state(shared_engine)
            // enable logger
            .wrap(middleware::Logger::default())
            .wrap(Cors::default())
            .service(
                web::scope(&settings.url_path_prefix)
                    .service((
                        // api
                        web::resource("/api/city/get").to(city_get),
                        web::resource("/api/city/capital").to(capital),
                        web::resource("/api/city/suggest").to(suggest),
                        web::resource("/api/city/reverse").to(reverse),
                        #[cfg(feature = "geoip2")]
                        web::resource("/api/city/geoip2").to(geoip2),
                        // serve openapi3 yaml and ui from files
                        fs::Files::new("/openapi3.yaml", std::env::temp_dir())
                            .index_file("openapi3.yaml"),
                        fs::Files::new("/swagger", std::env::temp_dir())
                            .index_file("swagger-ui.html"),
                        fs::Files::new("/redoc", std::env::temp_dir()).index_file("redoc-ui.html"),
                    ))
                    .configure(move |cfg: &mut web::ServiceConfig| {
                        if let Some(static_dir) = settings.static_dir.as_ref() {
                            cfg.service(fs::Files::new("/", static_dir).index_file("index.html"));
                        }
                    }),
            )
    })
    .bind(listen_on)?
    .run()
    .await
}

#[cfg(test)]
mod tests;
```

## File: `geosuggest/src/openapi3.yaml`
```yaml
openapi: 3.0.0
info:
  title: geosuggest
  version: {{version}}
servers:
  - url: {{url_path_prefix}}
paths:
  /api/city/get:
    get:
      tags:
      - get
      description: retrieve city by geonameid
      parameters:
        {{GetCityQuery}}
      responses:
        '200':
          content:
            application/json:
              schema:
                {{GetCityResult}}
  /api/city/capital:
    get:
      tags:
      - capital
      description: retrieve country capital 
      parameters:
        {{GetCapitalQuery}}
      responses:
        '200':
          content:
            application/json:
              schema:
                {{GetCapitalResult}}
  /api/city/suggest:
    get:
      tags:
      - suggest
      description: suggest city by text input
      parameters:
        {{SuggestQuery}}
      responses:
        '200':
          content:
            application/json:
              schema:
                {{SuggestResult}}
  /api/city/reverse:
    get:
      tags:
      - reverse
      description: find city by coordinates
      parameters:
        {{ReverseQuery}}
      responses:
        '200':
          content:
            application/json:
              schema:
                {{ReverseResult}}
  /api/city/geoip2:
    get:
      tags:
      - geoip2
      description: find city by IP address
      parameters:
        {{GeoIP2Query}}
      responses:
        '200':
          content:
            application/json:
              schema:
                {{GeoIP2Result}}
definitions:
  {{oaph::definitions}}
```

## File: `geosuggest/src/settings.rs`
```rust
use config::{Config, ConfigError, Environment, File};
use serde::Deserialize;
use std::path::Path;

const CONFIG_PREFIX: &str = "GEOSUGGEST";
const CONFIG_FILE_PATH: &str = "./defaults.toml";
const CONFIG_FILE_ENV_PATH_KEY: &str = "GEOSUGGEST_CONFIG_FILE";

#[derive(Debug, Deserialize, Clone)]
pub struct Settings {
    pub host: String,
    pub port: usize,
    pub index_file: String,
    pub static_dir: Option<String>,
    pub url_path_prefix: String,
    #[cfg(feature = "geoip2")]
    pub geoip2_file: Option<String>,
}

impl Settings {
    pub fn new() -> Result<Self, ConfigError> {
        let mut s = Config::builder();

        #[cfg(feature = "tracing")]
        tracing::info!("Try read config from: {}", CONFIG_FILE_PATH);
        if Path::new(CONFIG_FILE_PATH).exists() {
            s = s.add_source(File::with_name(CONFIG_FILE_PATH).required(false))
        }

        #[cfg(feature = "tracing")]
        tracing::info!(
            "Try read and merge in config from file by environment variable: {}",
            CONFIG_FILE_ENV_PATH_KEY
        );
        if let Ok(config_path) = std::env::var(CONFIG_FILE_ENV_PATH_KEY) {
            s = s.add_source(File::with_name(&config_path));
        };

        #[cfg(feature = "tracing")]
        tracing::info!(
            "Try read and merge in config from environment variables with prefix {}",
            CONFIG_PREFIX
        );
        s = s.add_source(Environment::with_prefix(CONFIG_PREFIX).separator("__"));

        s.build()?.try_deserialize()
    }
}

impl Default for Settings {
    fn default() -> Self {
        Settings {
            host: "localhost".to_owned(),
            port: 8080,
            index_file: "".to_string(),
            static_dir: None,
            url_path_prefix: "/".to_string(),
            #[cfg(feature = "geoip2")]
            geoip2_file: None,
        }
    }
}
```

## File: `geosuggest/src/tests.rs`
```rust
use geosuggest_core::{
    index::{IndexData, SourceFileOptions},
    EngineData,
};
use ntex::web::{test, App, Error, ServiceConfig};
use ntex::{http, web};

use std::sync::Arc;

fn app_config(cfg: &mut ServiceConfig) {
    let data = IndexData::new_from_files(SourceFileOptions {
        cities: "../geosuggest-core/tests/misc/cities.txt",
        names: Some("../geosuggest-core/tests/misc/names.txt"),
        countries: Some("../geosuggest-core/tests/misc/country-info.txt"),
        filter_languages: vec!["ru"],
        admin1_codes: Some("../geosuggest-core/tests/misc/admin1-codes.txt"),
        admin2_codes: Some("../geosuggest-core/tests/misc/admin2-codes.txt"),
    })
    .unwrap();

    let mut engine_data = EngineData::try_from(data).unwrap();

    #[cfg(feature = "geoip2")]
    engine_data
        .load_geoip2("../geosuggest-core/tests/misc/GeoLite2-City-Test.mmdb")
        .unwrap();

    // build static engine
    let engine_data = Box::new(engine_data);
    let engine_data = Box::leak(engine_data);
    let engine = engine_data
        .as_engine()
        .expect("Failed to initialize engine");
    let engine = Box::new(engine);
    let static_engine = Box::leak(engine);
    let shared_engine = Arc::new(static_engine);

    cfg.state(shared_engine).service((
        web::resource("/get").to(super::city_get),
        web::resource("/capital").to(super::capital),
        web::resource("/suggest").to(super::suggest),
        web::resource("/reverse").to(super::reverse),
        #[cfg(feature = "geoip2")]
        web::resource("/geoip2").to(super::geoip2),
    ));
}

#[test_log::test(ntex::test)]
async fn api_get() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get().uri("/get?id=472045").to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city");
    assert!(city.is_some());
    let city = city.unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "Voronezh");

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_capital_country_code() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/capital?country_code=RU")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city");
    assert!(city.is_some());
    let city = city.unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "Moscow");

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_capital_coordinates() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/capital?lat=55.7558&lng=37.6173&country_code=GB")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;
    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city").unwrap().as_object().unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "Moscow");

    Ok(())
}

#[cfg(feature = "geoip2")]
#[test_log::test(ntex::test)]
async fn api_capital_ip() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/capital?ip=81.2.69.142&country_code=RU")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;
    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city").unwrap().as_object().unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "London");

    Ok(())
}

#[cfg(feature = "geoip2")]
#[test_log::test(ntex::test)]
async fn api_capital_ip_client() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/capital?ip=client&country_code=RU")
        .header(ntex::http::header::FORWARDED, "81.2.69.142")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;
    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city").unwrap().as_object().unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "London");

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_get_lang() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/get?id=472045&lang=ru")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city");
    assert!(city.is_some());
    let city = city.unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "Воронеж");

    assert_eq!(
        city.get("country")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Россия"
    );
    assert_eq!(
        city.get("admin_division")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Воронежская область"
    );

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_suggest() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/suggest?pattern=Voronezh&countries=RU,JP")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert!(!items.is_empty());
    assert_eq!(items[0].get("name").unwrap().as_str().unwrap(), "Voronezh");

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_suggest_lang() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/suggest?pattern=Voronezh&lang=ru&limit=1")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert!(!items.is_empty());
    assert_eq!(items[0].get("name").unwrap().as_str().unwrap(), "Воронеж");
    assert_eq!(
        items[0]
            .get("country")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Россия"
    );
    assert_eq!(
        items[0]
            .get("admin_division")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Воронежская область"
    );

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_reverse() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/reverse?lat=51.6372&lng=39.1937&limit=1&countries=RU,JP")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert_eq!(items.len(), 1);
    assert_eq!(
        items[0]
            .get("city")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Voronezh"
    );

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_reverse_lang() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/reverse?lat=51.6372&lng=39.1937&lang=ru&limit=1")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert_eq!(items.len(), 1);
    assert_eq!(
        items[0]
            .get("city")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Воронеж"
    );
    assert_eq!(
        items[0]
            .get("city")
            .unwrap()
            .as_object()
            .unwrap()
            .get("country")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Россия"
    );
    assert_eq!(
        items[0]
            .get("city")
            .unwrap()
            .as_object()
            .unwrap()
            .get("admin_division")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Воронежская область"
    );

    Ok(())
}

#[cfg(feature = "geoip2")]
#[test_log::test(ntex::test)]
async fn api_geoip2_lang() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/geoip2?ip=81.2.69.142&lang=ru")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let city = result.get("city").unwrap().as_object().unwrap();
    assert_eq!(city.get("name").unwrap().as_str().unwrap(), "Лондон");

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_suggest_admin2_lang() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/suggest?pattern=Beverley&lang=ru&limit=1")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert!(!items.is_empty());
    assert_eq!(items[0].get("name").unwrap().as_str().unwrap(), "Beverley");
    assert_eq!(
        items[0]
            .get("admin2_division")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Ист-Райдинг-оф-Йоркшир"
    );

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_reverse_admin2_lang() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/reverse?lat=53.84587&lng=-0.42332&lang=ru&limit=1")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert_eq!(items.len(), 1);
    assert_eq!(
        items[0]
            .get("city")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Beverley"
    );
    assert_eq!(
        items[0]
            .get("city")
            .unwrap()
            .as_object()
            .unwrap()
            .get("admin2_division")
            .unwrap()
            .as_object()
            .unwrap()
            .get("name")
            .unwrap()
            .as_str()
            .unwrap(),
        "Ист-Райдинг-оф-Йоркшир"
    );

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_suggest_filter_by_countries() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/suggest?pattern=Voronezh&countries=JP,KR")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert!(items.is_empty());

    Ok(())
}

#[test_log::test(ntex::test)]
async fn api_reverse_filter_by_countries() -> Result<(), Error> {
    let app = test::init_service(App::new().configure(app_config)).await;

    let req = test::TestRequest::get()
        .uri("/reverse?lat=51.6372&lng=39.1937&limit=1&countries=JP,KR")
        .to_request();
    let resp = app.call(req).await.unwrap();

    assert_eq!(resp.status(), http::StatusCode::OK);

    let bytes = test::read_body(resp).await;

    let result: serde_json::Value = serde_json::from_slice(bytes.as_ref())?;
    let items = result.get("items").unwrap().as_array().unwrap();
    assert!(items.is_empty());

    Ok(())
}
```

## File: `geosuggest-core/Cargo.toml`
```
[package]
name = "geosuggest-core"
version.workspace = true
authors.workspace = true
description = "Suggest by name or find nearest by coordinates cities"
readme = "README.md"
keywords = ["geocoding", "service"]
repository = "https://github.com/estin/geosuggest.git"
documentation = "https://docs.rs/geosuggest-core/"
categories = ["web-programming::http-server"]
license = "MIT"
edition = "2021"

[features]
default = []
oaph = ["dep:oaph"]
geoip2 = ["dep:geoip2"]
tracing = ["dep:tracing"]

[dependencies]
tracing = { workspace = true, optional = true }
csv.workspace = true
serde.workspace = true
rayon.workspace = true
strsim.workspace = true
kiddo.workspace = true
rkyv.workspace = true
itertools.workspace = true

geoip2 = { workspace = true, optional = true}
oaph = { workspace = true, optional = true }

[dev-dependencies]
anyhow.workspace = true
tokio.workspace = true
test-log.workspace = true
tracing-subscriber.workspace = true
geosuggest-utils = { path = "../geosuggest-utils" }
```

## File: `geosuggest-core/README.md`
```markdown
<div align="center">
  <p><h1>geosuggest-core</h1></p>
  <p><strong>Library to suggest and to find nearest by coordinates cities</strong></p>
  <p></p>
</div>

[Live demo](https://geosuggest.etatarkin.ru/) with [sources](https://github.com/estin/geosuggest/tree/master/geosuggest-demo)

[HTTP service](https://github.com/estin/geosuggest)

[Examples](https://github.com/estin/geosuggest/tree/master/examples/src)

Usage example
```rust
use tokio;

use geosuggest_core::{EngineData, storage};
use geosuggest_utils::{IndexUpdater, IndexUpdaterSettings};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Build index...");
    let engine_data = load_engine_data().await?;

    println!("Initialize engine...");
    let engine = engine_data.as_engine()?;

    println!(
        "Suggest result: {:#?}",
        engine.suggest::<&str>("Beverley", 1, None, Some(&["US"]))
    );
    println!(
        "Reverse result: {:#?}",
        engine.reverse::<&str>((11.138298, 57.510973), 1, None, None)
    );

    Ok(())
}

async fn load_engine_data() -> Result<EngineData, Box<dyn std::error::Error>> {
    let index_file = std::path::Path::new("/tmp/geosuggest-index.rkyv");

    let updater = IndexUpdater::new(IndexUpdaterSettings {
        names: None, // no multilang support
        ..Default::default()
    })?;

    let storage = storage::Storage::new();

    Ok(if index_file.exists() {
        // load existed index
        let metadata = storage
            .read_metadata(index_file)
            .map_err(|e| format!("On load index metadata from {index_file:?}: {e}"))?;

        match metadata {
            Some(m) if updater.has_updates(&m).await? => {
                let engine = updater.build().await?;
                storage
                    .dump_to(index_file, &engine)
                    .map_err(|e| format!("Failed dump to {index_file:?}: {e}"))?;
                engine
            }
            _ => storage
                .load_from(index_file)
                .map_err(|e| format!("On load index from {index_file:?}: {e}"))?,
        }
    } else {
        // initial
        let engine = updater.build().await?;
        storage
            .dump_to(index_file, &engine)
            .map_err(|e| format!("Failed dump to {index_file:?}: {e}"))?;
        engine
    })

}
```
```

## File: `geosuggest-core/src/index.rs`
```rust
use itertools::Itertools;
use rayon::prelude::*;
use std::collections::{HashMap, HashSet};
use std::error::Error;

#[cfg(feature = "oaph")]
use oaph::schemars::{self, JsonSchema};

use kiddo::immutable::float::kdtree::ImmutableKdTree;
use rkyv::collections::swiss_table::ArchivedHashMap;
use rkyv::option::ArchivedOption;
use rkyv::rend::{f32_le, u32_le};
use rkyv::string::ArchivedString;
use serde::ser::{SerializeMap, Serializer};

#[cfg(feature = "tracing")]
use std::time::Instant;

pub fn skip_comment_lines(content: &str) -> String {
    content.lines().filter(|l| !l.starts_with('#')).join("\n")
}

fn split_content_to_n_parts(content: &str, n: usize) -> Vec<String> {
    if n == 0 || n == 1 {
        return vec![content.to_owned()];
    }

    let lines: Vec<&str> = content.lines().collect();
    lines.chunks(n).map(|chunk| chunk.join("\n")).collect()
}

pub struct SourceFileOptions<'a, P: AsRef<std::path::Path>> {
    pub cities: P,
    pub names: Option<P>,
    pub countries: Option<P>,
    pub admin1_codes: Option<P>,
    pub admin2_codes: Option<P>,
    pub filter_languages: Vec<&'a str>,
}

pub struct SourceFileContentOptions<'a> {
    pub cities: String,
    pub names: Option<String>,
    pub countries: Option<String>,
    pub admin1_codes: Option<String>,
    pub admin2_codes: Option<String>,
    pub filter_languages: Vec<&'a str>,
}

#[derive(Clone, rkyv::Deserialize, rkyv::Serialize, rkyv::Archive)]
pub struct IndexData {
    pub entries: Vec<Entry>,
    pub geonames: HashMap<u32, CitiesRecord>,
    pub capitals: HashMap<String, u32>,
    pub country_info_by_code: HashMap<String, CountryRecord>,
    pub tree: ImmutableKdTree<f32, u32, 2, 32>,
    pub tree_index_to_geonameid: HashMap<usize, u32>,
}

#[derive(Clone, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive)]
pub struct Entry {
    pub id: u32,                 // geoname id
    pub value: String,           // searchable value
    pub country_id: Option<u32>, // geoname country id
}

// code, name, name ascii, geonameid
#[derive(Debug, Clone, serde::Deserialize)]
struct Admin1CodeRecordRaw {
    code: String,
    name: String,
    _asciiname: String,
    geonameid: u32,
}

// code, name, name ascii, geonameid
#[derive(Debug, Clone, serde::Deserialize)]
struct Admin2CodeRecordRaw {
    code: String,
    name: String,
    _asciiname: String,
    geonameid: u32,
}

#[derive(Debug, Clone, serde::Serialize, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive)]
#[cfg_attr(feature = "oaph", derive(JsonSchema))]
#[rkyv(derive(serde::Serialize, Debug))]
pub struct AdminDivision {
    #[rkyv(attr(serde(serialize_with = "serialize_archived_u32")))]
    pub id: u32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub code: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub name: String,
}

// The main 'geoname' table has the following fields :
// ---------------------------------------------------
// geonameid         : integer id of record in geonames database
// name              : name of geographical point (utf8) varchar(200)
// asciiname         : name of geographical point in plain ascii characters, varchar(200)
// alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
// latitude          : latitude in decimal degrees (wgs84)
// longitude         : longitude in decimal degrees (wgs84)
// feature class     : see http://www.geonames.org/export/codes.html, char(1)
// feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
// country code      : ISO-3166 2-letter country code, 2 characters
// cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
// admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
// admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
// admin3 code       : code for third level administrative division, varchar(20)
// admin4 code       : code for fourth level administrative division, varchar(20)
// population        : bigint (8 byte int)
// elevation         : in meters, integer
// dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
// timezone          : the iana timezone id (see file timeZone.txt) varchar(40)
// modification date : date of last modification in yyyy-MM-dd format

#[derive(Debug, serde::Deserialize)]
struct CitiesRecordRaw {
    geonameid: u32,
    name: String,
    asciiname: String,
    alternatenames: String,
    latitude: f32,
    longitude: f32,
    _feature_class: String,
    feature_code: String,
    country_code: String,
    _cc2: String,
    admin1_code: String,
    admin2_code: String,
    _admin3_code: String,
    _admin4_code: String,
    population: u32,
    _elevation: String,
    _dem: String,
    timezone: String,
    _modification_date: String,
}

// CounntryInfo
// http://download.geonames.org/export/dump/countryInfo.txt
// ISO	ISO3	ISO-Numeric	fips	Country	Capital	Area(in sq km)	Population	Continent	tld	CurrencyCode	CurrencyName	Phone	Postal Code Format	Postal Code Regex	Languages	geonameid	neighbours	EquivalentFipsCode
#[derive(Debug, Clone, serde::Deserialize, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive)]
#[rkyv(derive(serde::Serialize, Debug))]
pub struct CountryRecordRaw {
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub iso: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub iso3: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub iso_numeric: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub fips: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub name: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub capital: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub area: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_u32")))]
    pub population: u32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub continent: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub tld: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub currency_code: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub currency_name: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub phone: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub postal_code_format: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub postal_code_regex: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub languages: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_u32")))]
    pub geonameid: u32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub neighbours: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub equivalent_fips_code: String,
}

#[derive(Debug, Clone, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive)]
#[rkyv(derive(Debug, serde::Serialize))]
pub struct CountryRecord {
    /// geonames country info
    pub info: CountryRecordRaw,

    /// Country name translation
    #[rkyv(attr(serde(serialize_with = "serialize_archived_optional_map")))]
    pub names: Option<HashMap<String, String>>,

    /// Capital name translation
    #[rkyv(attr(serde(serialize_with = "serialize_archived_optional_map")))]
    pub capital_names: Option<HashMap<String, String>>,
}

// The table 'alternate names' :
// -----------------------------
// alternateNameId   : the id of this alternate name, int
// geonameid         : geonameId referring to id in table 'geoname', int
// isolanguage       : iso 639 language code 2- or 3-characters; 4-characters 'post' for postal codes and 'iata','icao' and faac for airport codes, fr_1793 for French Revolution names,  abbr for abbreviation, link to a website (mostly to wikipedia), wkdt for the wikidataid, varchar(7)
// alternate name    : alternate name or name variant, varchar(400)
// isPreferredName   : '1', if this alternate name is an official/preferred name
// isShortName       : '1', if this is a short name like 'California' for 'State of California'
// isColloquial      : '1', if this alternate name is a colloquial or slang term. Example: 'Big Apple' for 'New York'.
// isHistoric        : '1', if this alternate name is historic and was used in the past. Example 'Bombay' for 'Mumbai'.
// from		  : from period when the name was used
// to		  : to period when the name was used
#[derive(Debug, serde::Deserialize)]
struct AlternateNamesRaw {
    _alternate_name_id: u32,
    geonameid: u32,
    isolanguage: String,
    alternate_name: String,
    is_preferred_name: String,
    is_short_name: String,
    is_colloquial: String,
    is_historic: String,
    _from: String,
    _to: String,
}

#[cfg_attr(feature = "oaph", derive(JsonSchema))]
#[derive(Debug, Clone, serde::Serialize, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive)]
#[rkyv(derive(serde::Serialize, Debug))]
pub struct Country {
    #[rkyv(attr(serde(serialize_with = "serialize_archived_u32")))]
    pub id: u32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub code: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub name: String,
}

impl From<&CountryRecordRaw> for Country {
    fn from(c: &CountryRecordRaw) -> Self {
        Country {
            id: c.geonameid,
            code: c.iso.clone(),
            name: c.name.clone(),
        }
    }
}

#[cfg_attr(feature = "oaph", derive(JsonSchema))]
#[derive(Debug, Clone, serde::Serialize, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive)]
#[rkyv(derive(serde::Serialize, Debug))]
pub struct CitiesRecord {
    #[rkyv(attr(serde(serialize_with = "serialize_archived_u32")))]
    pub id: u32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub name: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_f32")))]
    pub latitude: f32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_f32")))]
    pub longitude: f32,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_option")))]
    pub country: Option<Country>,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_option")))]
    pub admin_division: Option<AdminDivision>,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_option")))]
    pub admin2_division: Option<AdminDivision>,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_string")))]
    pub timezone: String,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_optional_map")))]
    pub names: Option<HashMap<String, String>>,
    // todo try reuse country info
    #[rkyv(attr(serde(serialize_with = "serialize_archived_optional_map")))]
    pub country_names: Option<HashMap<String, String>>,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_optional_map")))]
    pub admin1_names: Option<HashMap<String, String>>,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_optional_map")))]
    pub admin2_names: Option<HashMap<String, String>>,
    #[rkyv(attr(serde(serialize_with = "serialize_archived_u32")))]
    pub population: u32,
}

impl IndexData {
    pub fn new_from_files<P: AsRef<std::path::Path>>(
        SourceFileOptions {
            cities,
            names,
            countries,
            filter_languages,
            admin1_codes,
            admin2_codes,
        }: SourceFileOptions<P>,
    ) -> Result<Self, Box<dyn Error>> {
        Self::new_from_files_content(SourceFileContentOptions {
            cities: std::fs::read_to_string(cities)?,
            names: if let Some(p) = names {
                Some(std::fs::read_to_string(p)?)
            } else {
                None
            },
            countries: if let Some(p) = countries {
                Some(std::fs::read_to_string(p)?)
            } else {
                None
            },
            admin1_codes: if let Some(p) = admin1_codes {
                Some(std::fs::read_to_string(p)?)
            } else {
                None
            },
            admin2_codes: if let Some(p) = admin2_codes {
                Some(std::fs::read_to_string(p)?)
            } else {
                None
            },
            filter_languages,
        })
    }
    pub fn new_from_files_content(
        SourceFileContentOptions {
            cities,
            names,
            countries,
            filter_languages,
            admin1_codes,
            admin2_codes,
        }: SourceFileContentOptions,
    ) -> Result<Self, Box<dyn Error>> {
        #[cfg(feature = "tracing")]
        let now = Instant::now();

        let records = split_content_to_n_parts(&cities, rayon::current_num_threads())
            .par_iter()
            .map(|chunk| {
                let mut rdr = csv::ReaderBuilder::new()
                    .has_headers(false)
                    .delimiter(b'\t')
                    .from_reader(chunk.as_bytes());

                rdr.deserialize()
                    .filter_map(|row| {
                        let record: CitiesRecordRaw = row.ok()?;
                        Some(record)
                    })
                    .collect::<Vec<CitiesRecordRaw>>()
            })
            .reduce(Vec::new, |mut m1, ref mut m2| {
                m1.append(m2);
                m1
            });

        let mut geonames: Vec<CitiesRecord> = Vec::with_capacity(records.len());
        let mut entries: Vec<Entry> = Vec::with_capacity(
            records.len()
                * if filter_languages.is_empty() {
                    1
                } else {
                    filter_languages.len()
                },
        );

        #[cfg(feature = "tracing")]
        tracing::info!(
            "Engine read {} cities took {}ms",
            records.len(),
            now.elapsed().as_millis(),
        );

        // load country info
        let country_by_code: Option<HashMap<String, CountryRecordRaw>> = match countries {
            Some(contents) => {
                #[cfg(feature = "tracing")]
                let now = Instant::now();

                let contents = skip_comment_lines(&contents);

                let mut rdr = csv::ReaderBuilder::new()
                    .has_headers(false)
                    .delimiter(b'\t')
                    .from_reader(contents.as_bytes());

                let countries = rdr
                    .deserialize()
                    .filter_map(|row| {
                        let record: CountryRecordRaw = row
                            .map_err(|e| {
                                #[cfg(feature = "tracing")]
                                tracing::error!("On read country row: {e}");

                                e
                            })
                            .ok()?;
                        Some((record.iso.clone(), record))
                    })
                    .collect::<HashMap<String, CountryRecordRaw>>();

                #[cfg(feature = "tracing")]
                tracing::info!(
                    "Engine read {} countries took {}ms",
                    countries.len(),
                    now.elapsed().as_millis(),
                );

                Some(countries)
            }
            None => None,
        };

        // load admin1 code info
        let admin1_by_code: Option<HashMap<String, AdminDivision>> = match admin1_codes {
            Some(contents) => {
                #[cfg(feature = "tracing")]
                let now = Instant::now();

                let mut rdr = csv::ReaderBuilder::new()
                    .has_headers(false)
                    .delimiter(b'\t')
                    .from_reader(contents.as_bytes());

                let admin_division = rdr
                    .deserialize()
                    .filter_map(|row| {
                        let record: Admin1CodeRecordRaw = row.ok()?;
                        Some((
                            record.code.clone(),
                            AdminDivision {
                                id: record.geonameid,
                                code: record.code,
                                name: record.name,
                            },
                        ))
                    })
                    .collect::<HashMap<String, AdminDivision>>();

                #[cfg(feature = "tracing")]
                tracing::info!(
                    "Engine read {} admin1 codes took {}ms",
                    admin_division.len(),
                    now.elapsed().as_millis(),
                );

                Some(admin_division)
            }
            None => None,
        };

        // load admin2 code info
        let admin2_by_code: Option<HashMap<String, AdminDivision>> = match admin2_codes {
            Some(contents) => {
                #[cfg(feature = "tracing")]
                let now = Instant::now();

                let mut rdr = csv::ReaderBuilder::new()
                    .has_headers(false)
                    .delimiter(b'\t')
                    .from_reader(contents.as_bytes());

                let admin_division = rdr
                    .deserialize()
                    .filter_map(|row| {
                        let record: Admin2CodeRecordRaw = row.ok()?;
                        Some((
                            record.code.clone(),
                            AdminDivision {
                                id: record.geonameid,
                                code: record.code,
                                name: record.name,
                            },
                        ))
                    })
                    .collect::<HashMap<String, AdminDivision>>();

                #[cfg(feature = "tracing")]
                tracing::info!(
                    "Engine read {} admin2 codes took {}ms",
                    admin_division.len(),
                    now.elapsed().as_millis(),
                );

                Some(admin_division)
            }
            None => None,
        };

        let mut names_by_id: Option<HashMap<u32, HashMap<String, String>>> = match names {
            Some(contents) => {
                #[cfg(feature = "tracing")]
                let now = Instant::now();

                // collect ids for cities
                let city_geoids = records
                    .iter()
                    .map(|item| item.geonameid)
                    .collect::<HashSet<u32>>();

                let country_geoids = if let Some(ref country_by_code) = country_by_code {
                    country_by_code
                        .values()
                        .map(|item| item.geonameid)
                        .collect::<HashSet<u32>>()
                } else {
                    HashSet::<u32>::new()
                };

                let admin1_geoids = if let Some(ref admin_codes) = admin1_by_code {
                    admin_codes
                        .values()
                        .map(|item| item.id)
                        .collect::<HashSet<u32>>()
                } else {
                    HashSet::<u32>::new()
                };

                let admin2_geoids = if let Some(ref admin_codes) = admin2_by_code {
                    admin_codes
                        .values()
                        .map(|item| item.id)
                        .collect::<HashSet<u32>>()
                } else {
                    HashSet::<u32>::new()
                };

                // TODO: split to N parts can split one geonameid and build not accurate index
                // use rayon::current_num_threads() instead of 1
                let names_by_id = split_content_to_n_parts(&contents, 1)
                    .par_iter()
                    .map(move |chunk| {
                        let mut rdr = csv::ReaderBuilder::new()
                            .has_headers(false)
                            .delimiter(b'\t')
                            .from_reader(chunk.as_bytes());

                        let mut names_by_id: HashMap<u32, HashMap<String, AlternateNamesRaw>> =
                            HashMap::new();

                        for row in rdr.deserialize() {
                            let record: AlternateNamesRaw = if let Ok(r) = row {
                                r
                            } else {
                                continue;
                            };

                            let is_city_name = city_geoids.contains(&record.geonameid);
                            let mut skip = !is_city_name;

                            if skip {
                                skip = !country_geoids.contains(&record.geonameid)
                            }

                            if skip {
                                skip = !admin1_geoids.contains(&record.geonameid)
                            }

                            if skip {
                                skip = !admin2_geoids.contains(&record.geonameid)
                            }

                            // entry not used
                            if skip {
                                continue;
                            }

                            // skip short not preferred names for cities
                            if is_city_name
                                && record.is_short_name == "1"
                                && record.is_preferred_name != "1"
                            {
                                continue;
                            }

                            if record.is_colloquial == "1" {
                                continue;
                            }
                            if record.is_historic == "1" {
                                continue;
                            }

                            // filter by languages
                            if !filter_languages.contains(&record.isolanguage.as_str()) {
                                continue;
                            }

                            let lang = record.isolanguage.to_owned();

                            if let Some(item) = names_by_id.get_mut(&record.geonameid) {
                                // don't overwrite preferred name
                                let is_current_preferred_name = item
                                    .get(&record.isolanguage)
                                    .map(|i| i.is_preferred_name == "1")
                                    .unwrap_or(false);

                                if !is_current_preferred_name {
                                    item.insert(lang, record);
                                }
                            } else {
                                let mut map: HashMap<String, AlternateNamesRaw> = HashMap::new();
                                let geonameid = record.geonameid;
                                map.insert(lang.to_owned(), record);
                                names_by_id.insert(geonameid, map);
                            }
                        }

                        // convert names to simple struct
                        let result: HashMap<u32, HashMap<String, String>> =
                            names_by_id.iter().fold(HashMap::new(), |mut acc, c| {
                                let (geonameid, names) = c;
                                acc.insert(
                                    *geonameid,
                                    names.iter().fold(
                                        HashMap::new(),
                                        |mut accn: HashMap<String, String>, n| {
                                            let (isolanguage, n) = n;
                                            accn.insert(
                                                isolanguage.to_owned(),
                                                n.alternate_name.to_owned(),
                                            );
                                            accn
                                        },
                                    ),
                                );
                                acc
                            });
                        result
                    })
                    .reduce(HashMap::new, |mut m1, m2| {
                        m1.extend(m2);
                        m1
                    });

                #[cfg(feature = "tracing")]
                tracing::info!(
                    "Engine read {} names took {}ms",
                    records.len(),
                    now.elapsed().as_millis(),
                );

                Some(names_by_id)
            }
            None => None,
        };

        let mut capitals: HashMap<String, u32> =
            HashMap::with_capacity(if let Some(items) = &country_by_code {
                items.len()
            } else {
                0
            });

        for record in records {
            // INCLUDE:
            // PPL	populated place	a city, town, village, or other agglomeration of buildings where people live and work
            // PPLA	seat of a first-order administrative division	seat of a first-order administrative division (PPLC takes precedence over PPLA)
            // PPLA2	seat of a second-order administrative division
            // PPLA3	seat of a third-order administrative division
            // PPLA4	seat of a fourth-order administrative division
            // PPLA5	seat of a fifth-order administrative division
            // PPLC	capital of a political entity
            // PPLS	populated places	cities, towns, villages, or other agglomerations of buildings where people live and work
            // PPLG	seat of government of a political entity
            // PPLCH	historical capital of a political entity	a former capital of a political entity
            //
            // EXCLUDE:
            // PPLF farm village	a populated place where the population is largely engaged in agricultural activities
            // PPLL	populated locality	an area similar to a locality but with a small group of dwellings or other buildings
            // PPLQ	abandoned populated place
            // PPLW	destroyed populated place	a village, town or city destroyed by a natural disaster, or by war
            // PPLX	section of populated place
            // STLMT israeli settlement

            let feature_code = record.feature_code.as_str();
            match feature_code {
                "PPLA3" | "PPLA4" | "PPLA5" | "PPLF" | "PPLL" | "PPLQ" | "PPLW" | "PPLX"
                | "STLMT" => continue,
                _ => {}
            };

            let is_capital = feature_code == "PPLC";

            let country_id = country_by_code
                .as_ref()
                .and_then(|m| m.get(&record.country_code).map(|c| c.geonameid));

            entries.push(Entry {
                id: record.geonameid,
                value: record.name.to_lowercase().to_owned(),
                country_id,
            });

            if record.name != record.asciiname {
                entries.push(Entry {
                    id: record.geonameid,
                    value: record.asciiname.to_lowercase().to_owned(),
                    country_id,
                });
            }

            for altname in record.alternatenames.split(',') {
                entries.push(Entry {
                    id: record.geonameid,
                    value: altname.to_lowercase(),
                    country_id,
                });
            }

            let country = if let Some(ref c) = country_by_code {
                if is_capital {
                    capitals.insert(record.country_code.to_string(), record.geonameid);
                }
                c.get(&record.country_code).cloned()
            } else {
                None
            };

            let country_names = if let Some(ref c) = country {
                match names_by_id {
                    Some(ref names) => names.get(&c.geonameid).cloned(),
                    None => None,
                }
            } else {
                None
            };

            let admin_division = if let Some(ref a) = admin1_by_code {
                a.get(&format!("{}.{}", record.country_code, record.admin1_code))
                    .cloned()
            } else {
                None
            };

            let admin1_names = if let Some(ref a) = admin_division {
                match names_by_id {
                    Some(ref names) => names.get(&a.id).cloned(),
                    None => None,
                }
            } else {
                None
            };

            let admin2_division = if let Some(ref a) = admin2_by_code {
                a.get(&format!(
                    "{}.{}.{}",
                    record.country_code, record.admin1_code, record.admin2_code
                ))
                .cloned()
            } else {
                None
            };

            let admin2_names = if let Some(ref a) = admin2_division {
                match names_by_id {
                    Some(ref names) => names.get(&a.id).cloned(),
                    None => None,
                }
            } else {
                None
            };
            geonames.push(CitiesRecord {
                id: record.geonameid,
                name: record.name,
                country: country.as_ref().map(Country::from),
                admin_division,
                admin2_division,
                latitude: record.latitude,
                longitude: record.longitude,
                timezone: record.timezone,
                names: match names_by_id {
                    Some(ref mut names) => {
                        if is_capital {
                            names.get(&record.geonameid).cloned()
                        } else {
                            // don't hold unused data
                            names.remove(&record.geonameid)
                        }
                    }
                    None => None,
                },
                country_names,
                admin1_names,
                admin2_names,
                population: record.population,
            });
        }

        geonames.sort_unstable_by_key(|item| item.id);
        geonames.dedup_by_key(|item| item.id);

        let tree_index_to_geonameid = HashMap::from_iter(
            geonames
                .iter()
                .enumerate()
                .map(|(index, item)| (index, item.id)),
        );
        let tree = ImmutableKdTree::new_from_slice(
            geonames
                .iter()
                .map(|item| [item.latitude, item.longitude])
                .collect::<Vec<_>>()
                .as_slice(),
        );

        let data = IndexData {
            tree,
            tree_index_to_geonameid,
            entries,
            geonames: HashMap::from_iter(geonames.into_iter().map(|item| (item.id, item))),
            country_info_by_code: if let Some(country_by_code) = country_by_code {
                HashMap::from_iter(country_by_code.into_iter().map(|(code, country)| {
                    let country_record = CountryRecord {
                        names: names_by_id
                            .as_ref()
                            .and_then(|names| names.get(&country.geonameid).cloned()),
                        capital_names: match names_by_id {
                            Some(ref names) => {
                                if let Some(city_id) = capitals.get(&country.iso) {
                                    names.get(city_id).cloned()
                                } else {
                                    None
                                }
                            }
                            None => None,
                        },
                        info: country,
                    };

                    (code, country_record)
                }))
            } else {
                HashMap::new()
            },
            capitals,
        };

        #[cfg(feature = "tracing")]
        tracing::info!(
            "Index data ready (entries {}, geonames {}, capitals {}). took {}ms",
            data.entries.len(),
            data.geonames.len(),
            data.capitals.len(),
            now.elapsed().as_millis()
        );
        Ok(data)
    }
}

fn serialize_archived_string<S>(value: &ArchivedString, s: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    s.serialize_str(value.as_str())
}

fn serialize_archived_u32<S>(value: &u32_le, s: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    s.serialize_u32(value.to_native())
}

fn serialize_archived_f32<S>(value: &f32_le, s: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    s.serialize_f32(value.to_native())
}

fn serialize_archived_option<S, T>(value: &ArchivedOption<T>, s: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
    T: serde::Serialize,
{
    if let Some(v) = value.as_ref() {
        s.serialize_some(v)
    } else {
        s.serialize_none()
    }
}

fn serialize_archived_optional_map<S>(
    value: &ArchivedOption<ArchivedHashMap<ArchivedString, ArchivedString>>,
    s: S,
) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    if let Some(v) = value.as_ref() {
        let mut map = s.serialize_map(v.len().into())?;
        for (key, value) in v.iter() {
            map.serialize_entry(key.as_str(), value.as_str())?;
        }
        map.end()
    } else {
        s.serialize_none()
    }
}
```

## File: `geosuggest-core/src/lib.rs`
```rust
#![doc = include_str!("../README.md")]
use std::collections::HashMap;

use itertools::Itertools;

use kiddo::{self, SquaredEuclidean};

use rayon::prelude::*;
use rkyv::rend::{f32_le, u32_le};
use strsim::jaro_winkler;

#[cfg(feature = "geoip2")]
use std::net::IpAddr;

#[cfg(feature = "geoip2")]
use geoip2::{City, Reader};

#[cfg(feature = "oaph")]
use oaph::schemars::{self, JsonSchema};

pub mod index;
pub mod storage;

use index::{
    ArchivedCitiesRecord, ArchivedCountryRecord, ArchivedEntry, ArchivedIndexData, IndexData,
};

#[cfg_attr(feature = "oaph", derive(JsonSchema))]
#[derive(Debug, serde::Serialize)]
pub struct ReverseItem<'a> {
    pub city: &'a index::CitiesRecord,
    pub distance: f32,
    pub score: f32,
}

#[derive(Debug, serde::Serialize)]
pub struct ArchivedReverseItem<'a> {
    pub city: &'a index::ArchivedCitiesRecord,
    pub distance: f32,
    pub score: f32,
}

#[derive(
    Debug, Default, Clone, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive, serde::Serialize,
)]
pub struct EngineSourceMetadata {
    pub cities: String,
    pub names: Option<String>,
    pub countries: Option<String>,
    pub admin1_codes: Option<String>,
    pub admin2_codes: Option<String>,
    pub filter_languages: Vec<String>,
    pub etag: HashMap<String, String>,
}

#[derive(Debug, Clone, rkyv::Serialize, rkyv::Deserialize, rkyv::Archive, serde::Serialize)]
pub struct EngineMetadata {
    /// Index was built on version
    pub geosuggest_version: String,
    /// Creation time
    #[rkyv(with = rkyv::with::AsUnixTime)]
    pub created_at: std::time::SystemTime,
    /// Sources metadata
    pub source: EngineSourceMetadata,
    /// Custom metadata info
    pub extra: HashMap<String, String>,
}

impl Default for EngineMetadata {
    fn default() -> Self {
        Self {
            created_at: std::time::SystemTime::now(),
            geosuggest_version: env!("CARGO_PKG_VERSION").to_owned(),
            source: EngineSourceMetadata::default(),
            extra: HashMap::default(),
        }
    }
}

pub struct EngineData {
    pub data: rkyv::util::AlignedVec,
    pub metadata: Option<EngineMetadata>,
    #[cfg(feature = "geoip2")]
    pub geoip2: Option<Vec<u8>>,
}

impl EngineData {
    #[cfg(feature = "geoip2")]
    pub fn load_geoip2<P: AsRef<std::path::Path>>(
        &mut self,
        path: P,
    ) -> Result<(), Box<dyn std::error::Error>> {
        self.geoip2 = std::fs::read(path)?.into();
        Ok(())
    }

    pub fn as_engine(&self) -> Result<Engine<'_>, Box<dyn std::error::Error>> {
        Ok(Engine {
            data: rkyv::access::<_, rkyv::rancor::Error>(&self.data)?,
            #[cfg(feature = "geoip2")]
            geoip2: if let Some(geoip2) = &self.geoip2 {
                Reader::<City>::from_bytes(geoip2)
                    .map_err(|e| format!("Geoip2 error: {e:?}"))?
                    .into()
            } else {
                None
            },
        })
    }
}

pub struct Engine<'a> {
    pub data: &'a ArchivedIndexData,
    #[cfg(feature = "geoip2")]
    geoip2: Option<Reader<'a, City<'a>>>,
}

impl Engine<'_> {
    pub fn get(&self, id: &u32) -> Option<&ArchivedCitiesRecord> {
        self.data.geonames.get(&u32_le::from_native(*id))
    }

    /// Get capital by uppercase country code
    pub fn capital(&self, country_code: &str) -> Option<&ArchivedCitiesRecord> {
        if let Some(city_id) = self.data.capitals.get(country_code) {
            self.data.geonames.get(city_id)
        } else {
            None
        }
    }

    /// Suggest cities by pattern (multilang).
    ///
    /// Optional: filter by Jaro–Winkler distance via min_score
    ///
    /// Optional: prefilter by countries
    pub fn suggest<T: AsRef<str>>(
        &self,
        pattern: &str,
        limit: usize,
        min_score: Option<f32>,
        countries: Option<&[T]>,
    ) -> Vec<&ArchivedCitiesRecord> {
        if limit == 0 {
            return Vec::new();
        }

        let min_score = min_score.unwrap_or(0.8);
        let normalized_pattern = pattern.to_lowercase();

        let filter_by_pattern = |item: &ArchivedEntry| -> Option<(&ArchivedCitiesRecord, f32)> {
            let score = if item.value.starts_with(&normalized_pattern) {
                1.0
            } else {
                jaro_winkler(&item.value, &normalized_pattern) as f32
            };
            if score >= min_score {
                self.data.geonames.get(&item.id).map(|city| (city, score))
            } else {
                None
            }
        };

        let mut result: Vec<(&ArchivedCitiesRecord, f32)> = match &countries {
            Some(countries) => {
                let country_ids = countries
                    .iter()
                    .filter_map(|code| {
                        self.data
                            .country_info_by_code
                            .get(code.as_ref())
                            .map(|c| &c.info.geonameid)
                    })
                    .collect::<Vec<_>>();
                self.data
                    .entries
                    .par_iter()
                    .filter(|item| {
                        item.country_id
                            .as_ref()
                            .map(|id| country_ids.contains(&id))
                            .unwrap_or_default()
                    })
                    .filter_map(filter_by_pattern)
                    .collect()
            }
            None => self
                .data
                .entries
                .par_iter()
                .filter_map(filter_by_pattern)
                .collect(),
        };

        // sort by score desc, population desc
        result.sort_unstable_by(|lhs, rhs| {
            if (lhs.1 - rhs.1).abs() < f32::EPSILON {
                rhs.0
                    .population
                    .partial_cmp(&lhs.0.population)
                    .unwrap_or(std::cmp::Ordering::Equal)
            } else {
                rhs.1
                    .partial_cmp(&lhs.1)
                    .unwrap_or(std::cmp::Ordering::Equal)
            }
        });

        result
            .iter()
            .unique_by(|item| item.0.id)
            .take(limit)
            .map(|item| item.0)
            .collect::<Vec<_>>()
    }

    /// Find the nearest cities by coordinates.
    ///
    /// Optional: score results by `k` as `distance - k * city.population` and sort by score.
    ///
    /// Optional: prefilter by countries. It's a very expensive case; consider building an index for concrete countries and not applying this filter at all.
    pub fn reverse<T: AsRef<str>>(
        &self,
        loc: (f32, f32),
        limit: usize,
        k: Option<f32>,
        countries: Option<&[T]>,
    ) -> Option<Vec<ArchivedReverseItem<'_>>> {
        if limit == 0 {
            return None;
        }

        let nearest_limit = std::num::NonZero::new(if countries.is_some() {
            // ugly hack try to fetch nearest cities in requested countries
            // much better is to build index for concrete countries
            self.data.geonames.len()
        } else {
            limit
        })?;

        let mut i1;
        let mut i2;

        let items = &mut self
            .data
            .tree
            .nearest_n::<SquaredEuclidean>(&[loc.0, loc.1], nearest_limit);

        let items: &mut dyn Iterator<Item = (_, &ArchivedCitiesRecord)> =
            if let Some(countries) = countries {
                // normalize
                let countries = countries
                    .iter()
                    .map(|code| code.as_ref())
                    .collect::<Vec<_>>();

                i1 = items.iter_mut().filter_map(move |nearest| {
                    let geonameid = self
                        .data
                        .tree_index_to_geonameid
                        .get(&u32_le::from(nearest.item))?;
                    let city = self.data.geonames.get(geonameid)?;
                    let country = city.country.as_ref()?;
                    if countries.contains(&country.code.as_str()) {
                        Some((nearest, city))
                    } else {
                        None
                    }
                });
                &mut i1
            } else {
                i2 = items.iter_mut().filter_map(|nearest| {
                    let geonameid = self
                        .data
                        .tree_index_to_geonameid
                        .get(&u32_le::from(nearest.item))?;
                    let city = self.data.geonames.get(geonameid)?;
                    Some((nearest, city))
                });
                &mut i2
            };

        if let Some(k) = k.map(f32_le::from_native) {
            let mut points = items
                .map(|item| {
                    (
                        item.0.distance,
                        item.0.distance - k * (item.1.population.to_native() as f32),
                        item.1,
                    )
                })
                .take(limit)
                .collect::<Vec<_>>();

            points.sort_unstable_by(|a, b| {
                a.1.partial_cmp(&b.1).unwrap_or(std::cmp::Ordering::Equal)
            });

            Some(
                points
                    .iter()
                    .map(|p| ArchivedReverseItem {
                        distance: p.0,
                        score: p.1,
                        city: p.2,
                    })
                    .collect(),
            )
        } else {
            Some(
                items
                    .map(|item| ArchivedReverseItem {
                        distance: item.0.distance,
                        score: item.0.distance,
                        city: item.1,
                    })
                    .take(limit)
                    .collect(),
            )
        }
    }

    /// Get country info by iso 2-letter country code.
    pub fn country_info(&self, country_code: &str) -> Option<&ArchivedCountryRecord> {
        self.data.country_info_by_code.get(country_code)
    }

    #[cfg(feature = "geoip2")]
    pub fn geoip2_lookup(&self, addr: IpAddr) -> Option<&ArchivedCitiesRecord> {
        match self.geoip2.as_ref() {
            Some(reader) => {
                let result = reader.lookup(addr).ok()?;
                let city = result.city?;
                let id = city.geoname_id?;
                self.data.geonames.get(&u32_le::from_native(id))
            }
            None => {
                #[cfg(feature = "tracing")]
                tracing::warn!("Geoip2 reader is't configured!");
                None
            }
        }
    }
}

impl TryFrom<IndexData> for EngineData {
    type Error = rkyv::rancor::Error;
    fn try_from(data: IndexData) -> Result<EngineData, Self::Error> {
        Ok(EngineData {
            data: rkyv::to_bytes(&data)?,
            metadata: None,
            #[cfg(feature = "geoip2")]
            geoip2: None,
        })
    }
}

impl TryFrom<rkyv::util::AlignedVec> for EngineData {
    type Error = rkyv::rancor::Error;
    fn try_from(bytes: rkyv::util::AlignedVec) -> Result<EngineData, Self::Error> {
        Ok(EngineData {
            data: bytes,
            metadata: None,
            #[cfg(feature = "geoip2")]
            geoip2: None,
        })
    }
}
```

## File: `geosuggest-core/src/storage.rs`
```rust
use crate::ArchivedEngineMetadata;
use crate::EngineMetadata;
use rkyv;
use rkyv::{deserialize, option::ArchivedOption, rancor::Error};
use std::fs::OpenOptions;
use std::io::Read;
use std::io::SeekFrom;
use std::path::Path;

#[cfg(feature = "tracing")]
use std::time::Instant;

/// rkyv storage in len-prefix format `<4-bytes metadata length><metadata><payload>`
pub struct Storage {}

impl Storage {
    pub fn new() -> Self {
        Self {}
    }
}

impl Default for Storage {
    fn default() -> Self {
        Self::new()
    }
}

impl Storage {
    /// Serialize
    pub fn dump<W>(
        &self,
        buf: &mut W,
        engine_data: &crate::EngineData,
    ) -> Result<(), Box<dyn std::error::Error>>
    where
        W: std::io::Write,
    {
        let metadata = rkyv::to_bytes::<Error>(&engine_data.metadata)?;

        buf.write_all(&(metadata.len() as u32).to_be_bytes())?;
        #[cfg(feature = "tracing")]
        buf.write_all(&metadata)?;

        buf.write_all(&engine_data.data)?;
        Ok(())
    }

    /// Deserialize
    pub fn load<R>(&self, buf: &mut R) -> Result<crate::EngineData, Box<dyn std::error::Error>>
    where
        R: std::io::Read + std::io::Seek,
    {
        // skip metadata
        let mut metadata_len = [0; 4];
        buf.read_exact(&mut metadata_len)?;
        let metadata_len = u32::from_be_bytes(metadata_len);
        let _ = buf.seek(SeekFrom::Current(metadata_len as i64))?;

        let mut bytes = rkyv::util::AlignedVec::new();
        bytes.extend_from_reader(buf)?;

        Ok(bytes.try_into()?)
    }

    /// Read engine metadata and don't load whole engine
    pub fn read_metadata<P: AsRef<Path>>(
        &self,
        path: P,
    ) -> Result<Option<EngineMetadata>, Box<dyn std::error::Error>> {
        let mut file = OpenOptions::new()
            .create(false)
            .read(true)
            .truncate(false)
            .open(&path)?;

        let mut metadata_len = [0; 4];
        file.read_exact(&mut metadata_len)?;

        let metadata_len = u32::from_be_bytes(metadata_len);
        if metadata_len == 0 {
            return Ok(None);
        }
        let mut raw_metadata = vec![0; metadata_len as usize];
        file.read_exact(&mut raw_metadata)?;

        let archived =
            rkyv::access::<ArchivedOption<ArchivedEngineMetadata>, Error>(&raw_metadata[..])?;

        Ok(deserialize::<Option<EngineMetadata>, Error>(archived)?)
    }

    /// Dump whole index to file
    pub fn dump_to<P: AsRef<Path>>(
        &self,
        path: P,
        engine_data: &crate::EngineData,
    ) -> Result<(), Box<dyn std::error::Error>> {
        #[cfg(feature = "tracing")]
        tracing::info!("Start dump index to file...");
        #[cfg(feature = "tracing")]
        let now = Instant::now();

        let mut file = OpenOptions::new()
            .create(true)
            .write(true)
            .truncate(true)
            .open(&path)?;

        self.dump(&mut file, engine_data)?;

        #[cfg(feature = "tracing")]
        tracing::info!("Dump index to file. took {}ms", now.elapsed().as_millis(),);

        Ok(())
    }
    /// Load whole index from file
    pub fn load_from<P: AsRef<std::path::Path>>(
        &self,
        path: P,
    ) -> Result<crate::EngineData, Box<dyn std::error::Error>> {
        #[cfg(feature = "tracing")]
        tracing::info!("Loading index...");
        #[cfg(feature = "tracing")]
        let now = Instant::now();

        let mut file = OpenOptions::new()
            .create(false)
            .read(true)
            .truncate(false)
            .open(&path)?;

        let index = self.load(&mut file)?;

        #[cfg(feature = "tracing")]
        tracing::info!(
            "Loaded from file done. took {}ms",
            now.elapsed().as_millis(),
        );

        Ok(index)
    }
}
```

## File: `geosuggest-core/tests/lib.rs`
```rust
use geosuggest_core::{
    index::{IndexData, SourceFileOptions},
    storage, EngineData, EngineMetadata,
};
use std::{env::temp_dir, error::Error};

#[cfg(feature = "geoip2")]
use std::{net::IpAddr, str::FromStr};

fn get_engine_data(
    cities: Option<&str>,
    names: Option<&str>,
    countries: Option<&str>,
    filter_languages: Vec<&str>,
) -> Result<geosuggest_core::EngineData, Box<dyn Error>> {
    let data = IndexData::new_from_files(SourceFileOptions {
        cities: cities.unwrap_or("tests/misc/cities.txt"),
        names: Some(names.unwrap_or("tests/misc/names.txt")),
        countries: Some(countries.unwrap_or("tests/misc/country-info.txt")),
        filter_languages,
        admin1_codes: Some("tests/misc/admin1-codes.txt"),
        admin2_codes: Some("tests/misc/admin2-codes.txt"),
    })?;

    let mut engine_data = EngineData::try_from(data)?;

    engine_data.metadata = Some(EngineMetadata::default());
    Ok(engine_data)
}

#[test_log::test]
fn suggest() -> Result<(), Box<dyn Error>> {
    let engine_data = get_engine_data(None, None, None, vec![])?;
    let engine = engine_data.as_engine()?;

    let items = engine.suggest::<&str>("voronezh", 1, None, None);
    assert_eq!(items.len(), 1);
    assert_eq!(items[0].name, "Voronezh");
    assert_eq!(items[0].country.as_ref().unwrap().name, "Russia");
    assert_eq!(items[0].admin_division.as_ref().unwrap().name, "Voronezj");

    let items = engine.suggest::<&str>("Beverley", 1, None, None);
    tracing::info!("Items {items:#?}");
    assert_eq!(items[0].name, "Beverley");
    assert_eq!(
        items[0].admin2_division.as_ref().unwrap().name,
        "East Riding of Yorkshire"
    );

    let items = engine.suggest("Beverley", 1, None, Some(&["RU"]));
    assert_eq!(items.len(), 0);

    let items = engine.suggest("Beverley", 1, None, Some(&["GB"]));
    assert_eq!(items.len(), 1);

    Ok(())
}

#[test_log::test]
fn reverse() -> Result<(), Box<dyn Error>> {
    let engine_data = get_engine_data(None, None, None, vec![])?;
    let engine = engine_data.as_engine()?;
    let result = engine.reverse::<&str>((51.6372, 39.1937), 1, None, None);
    assert!(result.is_some());
    let items = result.unwrap();
    assert_eq!(items.len(), 1);
    assert_eq!(items[0].city.name, "Voronezh");
    assert_eq!(items[0].city.country.as_ref().unwrap().name, "Russia");
    assert_eq!(
        items[0].city.admin_division.as_ref().unwrap().name,
        "Voronezj"
    );

    let result = engine.reverse::<&str>((53.84587, -0.42332), 1, None, None);
    assert!(result.is_some());
    let items = result.unwrap();
    assert_eq!(items.len(), 1);
    assert_eq!(items[0].city.name, "Beverley");
    assert_eq!(
        items[0].city.admin2_division.as_ref().unwrap().name,
        "East Riding of Yorkshire"
    );

    let result = engine.reverse((53.84587, -0.42332), 1, None, Some(&["AR"]));
    assert_eq!(result.unwrap().len(), 0);

    let result = engine.reverse((53.84587, -0.42332), 1, None, Some(&["GB"]));
    assert_eq!(result.unwrap().len(), 1);

    Ok(())
}

#[test_log::test]
fn capital() -> Result<(), Box<dyn Error>> {
    let engine_data = get_engine_data(None, None, None, vec![])?;
    let engine = engine_data.as_engine()?;
    let result = engine.capital("RU");
    assert!(result.is_some());
    let city = result.unwrap();
    assert_eq!(city.name, "Moscow");
    assert_eq!(city.country.as_ref().unwrap().name, "Russia");
    Ok(())
}

#[test_log::test]
#[cfg(feature = "geoip2")]
fn geoip2_lookup() -> Result<(), Box<dyn Error>> {
    let mut engine_data = get_engine_data(None, None, None, vec![])?;
    engine_data.load_geoip2("tests/misc/GeoLite2-City-Test.mmdb")?;

    let engine = engine_data.as_engine()?;

    let result = engine.geoip2_lookup(IpAddr::from_str("81.2.69.142")?);
    assert!(result.is_some());
    let item = result.unwrap();
    assert_eq!(item.name, "London");

    Ok(())
}

#[test_log::test]
fn build_dump_load() -> Result<(), Box<dyn Error>> {
    let filepath = temp_dir().join("test-engine.rkyv");
    let storage = storage::Storage::new();
    // build
    let engine_data = get_engine_data(None, None, None, vec![])?;
    let engine = engine_data.as_engine()?;

    // dump
    storage.dump_to(&filepath, &engine_data)?;

    // check metadata
    let metadata = storage.read_metadata(&filepath)?;
    assert!(metadata.is_some());

    // load
    let from_dump = storage.load_from(&filepath)?;

    let from_dump_engine = from_dump.as_engine()?;

    assert_eq!(
        engine.suggest::<&str>("voronezh", 100, None, None).len(),
        from_dump_engine
            .suggest::<&str>("voronezh", 100, None, None)
            .len(),
    );

    let coords = (51.6372, 39.1937);
    assert_eq!(
        engine.reverse::<&str>(coords, 1, None, None).unwrap()[0]
            .city
            .id,
        from_dump_engine
            .reverse::<&str>(coords, 1, None, None)
            .unwrap()[0]
            .city
            .id,
    );

    Ok(())
}

#[test_log::test]
fn population_weight() -> Result<(), Box<dyn Error>> {
    let engine_data =
        get_engine_data(Some("tests/misc/population-weight.txt"), None, None, vec![])?;

    let engine = engine_data.as_engine()?;

    let population_weight = 0.000000005;

    // {
    //  "id": 532535,
    //  "name": "Lyublino",
    //  "country_code": "RU",
    //  "timezone": "Europe/Moscow",
    //  "latitude": 55.67738,
    //  "longitude": 37.76005
    // }

    // without weight coefficient
    let result = engine.reverse::<&str>((55.67738, 37.76006), 5, None, None);
    assert!(result.is_some());
    let items = result.unwrap();
    assert_eq!(items.len(), 3);
    tracing::trace!("Reverse result: {:#?}", items);
    assert_eq!(items[0].city.name, "Lyublino");

    // with weight coefficient
    let result = engine.reverse::<&str>((55.67738, 37.76006), 5, Some(population_weight), None);
    assert!(result.is_some());
    let items = result.unwrap();
    assert_eq!(items.len(), 3);
    tracing::trace!("Reverse result: {:#?}", items);
    assert_eq!(items[0].city.name, "Moscow");

    // {
    //   "id": 532615,
    //   "name": "Lyubertsy",
    //   "country_code": "RU",
    //   "timezone": "Europe/Moscow",
    //   "latitude": 55.67719,
    //   "longitude": 37.89322
    // }

    // with weight coefficient
    let result = engine.reverse::<&str>((55.67719, 37.89322), 5, Some(population_weight), None);
    assert!(result.is_some());
    let items = result.unwrap();
    tracing::trace!("Reverse result: {:#?}", items);
    assert_eq!(items.len(), 3);
    assert_eq!(items[0].city.name, "Lyubertsy");

    Ok(())
}

#[test_log::test]
fn country_info() -> Result<(), Box<dyn Error>> {
    let engine_data = get_engine_data(None, None, None, vec!["ru", "sr"])?;
    let engine = engine_data.as_engine()?;

    let country1 = engine.country_info("RS").unwrap();

    assert_eq!(country1.info.name, "Serbia");
    assert_eq!(
        country1.names.as_ref().unwrap().get("ru").unwrap(),
        "Сербия"
    );
    assert_eq!(
        country1.capital_names.as_ref().unwrap().get("ru").unwrap(),
        "Белград"
    );

    Ok(())
}
```

## File: `geosuggest-core/tests/misc/admin1-codes.txt`
```
RU.88	Yaroslavl Oblast	Yaroslavl Oblast	468898
RU.86	Voronezj	Voronezj	472039
RU.85	Vologda	Vologda	472454
RU.84	Volgograd Oblast	Volgograd Oblast	472755
RU.81	Ulyanovsk	Ulyanovsk	479119
RU.80	Udmurtiya Republic	Udmurtiya Republic	479613
RU.77	Tver’ Oblast	Tver' Oblast	480041
RU.76	Tula	Tula	480508
RU.73	Tatarstan Republic	Tatarstan Republic	484048
RU.72	Tambov	Tambov	484638
RU.70	Stavropol’ Kray	Stavropol' Kray	487839
RU.69	Smolenskaya Oblast’	Smolenskaya Oblast'	491684
RU.67	Saratovskaya Oblast	Saratovskaya Oblast	498671
RU.65	Samara Oblast	Samara Oblast	499068
RU.62	Ryazan Oblast	Ryazan Oblast	500059
RU.61	Rostov	Rostov	501165
RU.60	Pskov Oblast	Pskov Oblast	504338
RU.90	Perm	Perm	511180
RU.57	Penza	Penza	511555
RU.56	Orel Oblast	Orel Oblast	514801
RU.55	Orenburg Oblast	Orenburg Oblast	515001
RU.52	Novgorod Oblast	Novgorod Oblast	519324
RU.68	North Ossetia	North Ossetia	519969
RU.50	Nenets	Nenets	522652
RU.49	Murmansk	Murmansk	524304
RU.48	Moscow	Moscow	524894
RU.47	Moscow Oblast	Moscow Oblast	524925
RU.46	Mordoviya Republic	Mordoviya Republic	525369
RU.45	Mariy-El Republic	Mariy-El Republic	529352
RU.43	Lipetsk Oblast	Lipetsk Oblast	535120
RU.42	Leningradskaya Oblast'	Leningradskaya Oblast'	536199
RU.66	St.-Petersburg	St.-Petersburg	536203
RU.41	Kursk	Kursk	538555
RU.38	Krasnodarskiy	Krasnodarskiy	542415
RU.37	Kostroma Oblast	Kostroma Oblast	543871
RU.34	Komi	Komi	545854
RU.33	Kirov	Kirov	548389
RU.28	Karelia	Karelia	552548
RU.27	Karachayevo-Cherkesiya Republic	Karachayevo-Cherkesiya Republic	552927
RU.25	Kaluga	Kaluga	553899
RU.24	Kalmykiya Republic	Kalmykiya Republic	553972
RU.23	Kaliningrad	Kaliningrad	554230
RU.22	Kabardino-Balkariya Republic	Kabardino-Balkariya Republic	554667
RU.21	Ivanovo	Ivanovo	555235
RU.19	Ingushetiya Republic	Ingushetiya Republic	556349
RU.51	Nizhny Novgorod Oblast	Nizhny Novgorod Oblast	559838
RU.17	Dagestan	Dagestan	567293
RU.16	Chuvashia	Chuvashia	567395
RU.12	Chechnya	Chechnya	569665
RU.10	Bryansk Oblast	Bryansk Oblast	571473
RU.09	Belgorod Oblast	Belgorod Oblast	578071
RU.08	Bashkortostan Republic	Bashkortostan Republic	578853
RU.07	Astrakhan	Astrakhan	580491
RU.06	Arkhangelskaya	Arkhangelskaya	581043
RU.01	Adygeya Republic	Adygeya Republic	584222
RU.83	Vladimir	Vladimir	826294
RU.87	Yamalo-Nenets	Yamalo-Nenets	1486462
RU.78	Tyumen’ Oblast	Tyumen' Oblast	1488747
RU.79	Republic of Tyva	Republic of Tyva	1488873
RU.75	Tomsk Oblast	Tomsk Oblast	1489421
RU.71	Sverdlovsk	Sverdlovsk	1490542
RU.54	Omsk	Omsk	1496152
RU.53	Novosibirsk Oblast	Novosibirsk Oblast	1496745
RU.40	Kurgan Oblast	Kurgan Oblast	1501312
RU.91	Krasnoyarskiy	Krasnoyarskiy	1502020
RU.32	Khanty-Mansia	Khanty-Mansia	1503773
RU.31	Khakasiya Republic	Khakasiya Republic	1503834
RU.29	Kemerovo Oblast	Kemerovo Oblast	1503900
RU.03	Altai	Altai	1506272
RU.13	Chelyabinsk	Chelyabinsk	1508290
RU.04	Altai Krai	Altai Krai	1511732
RU.63	Sakha	Sakha	2013162
RU.59	Primorskiy (Maritime) Kray	Primorskiy (Maritime) Kray	2017623
RU.30	Khabarovsk	Khabarovsk	2022888
RU.20	Irkutsk Oblast	Irkutsk Oblast	2023468
RU.89	Jewish Autonomous Oblast	Jewish Autonomous Oblast	2026639
RU.05	Amur Oblast	Amur Oblast	2027748
RU.11	Buryatiya Republic	Buryatiya Republic	2050915
RU.64	Sakhalin Oblast	Sakhalin Oblast	2121529
RU.44	Magadan Oblast	Magadan Oblast	2123627
RU.92	Kamchatka	Kamchatka	2125072
RU.15	Chukotka	Chukotka	2126099
RU.93	Transbaikal Territory	Transbaikal Territory	7779061
```

## File: `geosuggest-core/tests/misc/admin2-codes.txt`
```
GB.ENG.E1	East Riding of Yorkshire	East Riding of Yorkshire	2650345
```

## File: `geosuggest-core/tests/misc/cities.txt`
```
472045	Voronezh	Voronezh	VOZ,Voronej,Voronez,Voroneza,Voronezas,Voronezh,Voronezhskaja oblast',Voronezj,Voroneĵ,Voronež,Voronežas,Voroněž,Voroņeža,Woronesch,Woronesh,Woronez,Woroneż,bolonesi,vu~oroneji,Воронеж,Воронежская область,ヴォロネジ,보로네시	51.67204	39.1843	P	PPLA	RU		86				848752		156	Europe/Moscow	2019-09-04
2643743	London	London	ILondon,LON,Lakana,Landan,Landen,Ljondan,Llundain,Lodoni,Londain,Londan,Londar,Londe,Londen,Londin,Londinium,Londino,Londn,London,London osh,Londona,Londonas,Londoni,Londono,Londons,Londonu,Londra,Londres,Londrez,Londri,Londro,Londye,Londyn,Londýn,Lonn,Lontoo,Loundres,Luan GJon,Lun-tun,Lunden,Lundra,Lundun,Lundunir,Lundúnir,Lung-dung,Lunnainn,Lunnin,Lunnon,Luân Đôn,Lùn-tûn,Lùng-dŭng,Lûn-tun,Lākana,Lůndůn,Lọndọnu,Ranana,Rānana,ilantan,ladana,landan,landana,leondeon,lndn,london,londoni,lun dui,lun dun,lwndwn,lxndxn,rondon,Łondra,Λονδίνο,Лондан,Лондон,Лондон ош,Лондонъ,Лёндан,Լոնդոն,לאנדאן,לונדון,لأندأن,لندن,لوندون,لەندەن,ܠܘܢܕܘܢ,लंडन,लंदन,लण्डन,लन्डन्,लन्दन,লন্ডন,ਲੰਡਨ,લંડન,ଲଣ୍ଡନ,இலண்டன்,లండన్,ಲಂಡನ್,ലണ്ടൻ,ලන්ඩන්,ลอนดอน,ລອນດອນ,ལོན་ཊོན།,လန်ဒန်မြို့,ლონდონი,ለንደን,ᎫᎴ ᏗᏍᎪᏂᎯᏱ,ロンドン,伦敦,倫敦,런던	51.50853	-0.12574	P	PPLC	GB		ENG	GLA			7556900		25	Europe/London	2019-09-18
524901	Moscow	Moscow	MOW,Maeskuy,Maskav,Maskava,Maskva,Mat-xco-va,Matxcova,Matxcơva,Mosca,Moscfa,Moscha,Mosco,Moscou,Moscova,Moscovo,Moscow,Moscoƿ,Moscu,Moscua,Moscòu,Moscó,Moscù,Moscú,Moskva,Moska,Moskau,Mosko,Moskokh,Moskou,Moskov,Moskova,Moskovu,Moskow,Moskowa,Mosku,Moskuas,Moskva,Moskvo,Moskwa,Moszkva,Muskav,Musko,Mát-xcơ-va,Mòskwa,Məskeu,Məskəү,masko,maskw,mo si ke,moseukeuba,mosko,mosukuwa,mskw,mwskva,mwskw,mwsqbh,mx s ko,Μόσχα,Мæскуы,Маскав,Масква,Москва,Москова,Москох,Москъва,Мускав,Муско,Мәскеу,Мәскәү,Մոսկվա,מאָסקװע,מאסקווע,מוסקבה,ماسکو,مسکو,موسكو,موسكۋا,ܡܘܣܩܒܐ,मास्को,मॉस्को,মস্কো,மாஸ்கோ,มอสโก,མོ་སི་ཁོ།,მოსკოვი,ሞስኮ,モスクワ,莫斯科,모스크바	55.75222	37.61556	P	PPLC	RU		48				10381222		144	Europe/Moscow	2020-03-31
2655785	Beverley	Beverley	Beverley,Bevurli,bebeolli,bei fu li,bwrly,Бевърли,بورلی,貝弗利,베벌리	53.84587	-0.42332	P	PPLA2	GB		ENG	E1	00FB166		30587		10	Europe/London	2017-06-12
792680	Belgrade	Belgrade	BEG,Belehrad,Belgrad,Belgrada,Belgradas,Belgrade,Belgrado,Belgradu,Belgrau,Belgrað,Belgrád,Belgráu,Beligradi,Belogradum,Belohrod,Beograd,Beogradi,Beogrado,Bèlgrade,Bělehrad,Běłohród,Nandorfehervar,Nándorfehérvár,Singidunum,be-ogeuladeu,bei er ge lai de,belgradi,beogurado,blghrad,blgrd,pelkiret,Βελιγράδι,Белград,Београд,Бѣлъ Градъ · Срьбїи,Բելգրադ,בלגרד,بلغراد,بېلگراد,பெல்கிறேட்,ბელგრადი,በልግራድ,ベオグラード,贝尔格莱德,베오그라드	44.80401	20.46513	P	PPLC	RS		SE	0			1273651		120	Europe/Belgrade	2020-01-31
```

## File: `geosuggest-core/tests/misc/country-info.txt`
```
# ================================
#
#
# CountryCodes:
# ============
#
# The official ISO country code for the United Kingdom is 'GB'. The code 'UK' is reserved.
#
# A list of dependent countries is available here:
# https://spreadsheets.google.com/ccc?key=pJpyPy-J5JSNhe7F_KxwiCA&hl=en
#
#
# The countrycode XK temporarily stands for Kosvo:
# http://geonames.wordpress.com/2010/03/08/xk-country-code-for-kosovo/								
#
#
# CS (Serbia and Montenegro) with geonameId = 8505033 no longer exists.
# AN (the Netherlands Antilles) with geonameId = 8505032 was dissolved on 10 October 2010.
#
#
# Currencies :
# ============
#
# A number of territories are not included in ISO 4217, because their currencies are not per se an independent currency,															
# but a variant of another currency. These currencies are:
#
# 1. FO : Faroese krona (1:1 pegged to the Danish krone)				
# 2. GG : Guernsey pound (1:1 pegged to the pound sterling)
# 3. JE : Jersey pound (1:1 pegged to the pound sterling)			
# 4. IM : Isle of Man pound (1:1 pegged to the pound sterling)																		
# 5. TV : Tuvaluan dollar (1:1 pegged to the Australian dollar).											
# 6. CK : Cook Islands dollar (1:1 pegged to the New Zealand dollar).				
#	
# The following non-ISO codes are, however, sometimes used: GGP for the Guernsey pound, 																		
# JEP for the Jersey pound and IMP for the Isle of Man pound (http://en.wikipedia.org/wiki/ISO_4217)																		
#	
#																		
# A list of currency symbols is available here : http://forum.geonames.org/gforum/posts/list/437.page																		
# another list with fractional units is here: http://forum.geonames.org/gforum/posts/list/1961.page																		
#																		
#																		
# Languages :																		
# ===========																		
#																		
# The column 'languages' lists the languages spoken in a country ordered by the number of speakers. The language code is a 'locale' 																		
# where any two-letter primary-tag is an ISO-639 language abbreviation and any two-letter initial subtag is an ISO-3166 country code.																		
#																		
# Example : es-AR is the Spanish variant spoken in Argentina.																		
#																		
#ISO	ISO3	ISO-Numeric	fips	Country	Capital	Area(in sq km)	Population	Continent	tld	CurrencyCode	CurrencyName	Phone	Postal Code Format	Postal Code Regex	Languages	geonameid	neighbours	EquivalentFipsCode
AD	AND	020	AN	Andorra	Andorra la Vella	468	77006	EU	.ad	EUR	Euro	376	AD###	^(?:AD)*(\d{3})$	ca	3041565	ES,FR	
AE	ARE	784	AE	United Arab Emirates	Abu Dhabi	82880	9630959	AS	.ae	AED	Dirham	971			ar-AE,fa,en,hi,ur	290557	SA,OM	
AF	AFG	004	AF	Afghanistan	Kabul	647500	37172386	AS	.af	AFN	Afghani	93			fa-AF,ps,uz-AF,tk	1149361	TM,CN,IR,TJ,PK,UZ	
AG	ATG	028	AC	Antigua and Barbuda	St. John's	443	96286	NA	.ag	XCD	Dollar	+1-268			en-AG	3576396		
AI	AIA	660	AV	Anguilla	The Valley	102	13254	NA	.ai	XCD	Dollar	+1-264			en-AI	3573511		
AL	ALB	008	AL	Albania	Tirana	28748	2866376	EU	.al	ALL	Lek	355	####	^(\d{4})$	sq,el	783754	MK,GR,ME,RS,XK	
AM	ARM	051	AM	Armenia	Yerevan	29800	2951776	AS	.am	AMD	Dram	374	######	^(\d{6})$	hy	174982	GE,IR,AZ,TR	
AO	AGO	024	AO	Angola	Luanda	1246700	30809762	AF	.ao	AOA	Kwanza	244			pt-AO	3351879	CD,NA,ZM,CG	
AQ	ATA	010	AY	Antarctica		14000000	0	AN	.aq							6697173		
AR	ARG	032	AR	Argentina	Buenos Aires	2766890	44494502	SA	.ar	ARS	Peso	54	@####@@@	^[A-Z]?\d{4}[A-Z]{0,3}$	es-AR,en,it,de,fr,gn	3865483	CL,BO,UY,PY,BR	
AS	ASM	016	AQ	American Samoa	Pago Pago	199	55465	OC	.as	USD	Dollar	+1-684	#####-####	96799	en-AS,sm,to	5880801		
AT	AUT	040	AU	Austria	Vienna	83858	8847037	EU	.at	EUR	Euro	43	####	^(\d{4})$	de-AT,hr,hu,sl	2782113	CH,DE,HU,SK,CZ,IT,SI,LI	
AU	AUS	036	AS	Australia	Canberra	7686850	24992369	OC	.au	AUD	Dollar	61	####	^(\d{4})$	en-AU	2077456		
AW	ABW	533	AA	Aruba	Oranjestad	193	105845	NA	.aw	AWG	Guilder	297			nl-AW,pap,es,en	3577279		
AX	ALA	248		Aland Islands	Mariehamn	1580	26711	EU	.ax	EUR	Euro	+358-18	#####	^(?:FI)*(\d{5})$	sv-AX	661882		FI
AZ	AZE	031	AJ	Azerbaijan	Baku	86600	9942334	AS	.az	AZN	Manat	994	AZ ####	^(?:AZ)*(\d{4})$	az,ru,hy	587116	GE,IR,AM,TR,RU	
BA	BIH	070	BK	Bosnia and Herzegovina	Sarajevo	51129	3323929	EU	.ba	BAM	Marka	387	#####	^(\d{5})$	bs,hr-BA,sr-BA	3277605	HR,ME,RS	
BB	BRB	052	BB	Barbados	Bridgetown	431	286641	NA	.bb	BBD	Dollar	+1-246	BB#####	^(?:BB)*(\d{5})$	en-BB	3374084		
BD	BGD	050	BG	Bangladesh	Dhaka	144000	161356039	AS	.bd	BDT	Taka	880	####	^(\d{4})$	bn-BD,en	1210997	MM,IN	
BE	BEL	056	BE	Belgium	Brussels	30510	11422068	EU	.be	EUR	Euro	32	####	^(\d{4})$	nl-BE,fr-BE,de-BE	2802361	DE,NL,LU,FR	
BF	BFA	854	UV	Burkina Faso	Ouagadougou	274200	19751535	AF	.bf	XOF	Franc	226			fr-BF,mos	2361809	NE,BJ,GH,CI,TG,ML	
BG	BGR	100	BU	Bulgaria	Sofia	110910	7000039	EU	.bg	BGN	Lev	359	####	^(\d{4})$	bg,tr-BG,rom	732800	MK,GR,RO,TR,RS	
BH	BHR	048	BA	Bahrain	Manama	665	1569439	AS	.bh	BHD	Dinar	973	####|###	^(\d{3}\d?)$	ar-BH,en,fa,ur	290291		
BI	BDI	108	BY	Burundi	Gitega	27830	11175378	AF	.bi	BIF	Franc	257			fr-BI,rn	433561	TZ,CD,RW	
BJ	BEN	204	BN	Benin	Porto-Novo	112620	11485048	AF	.bj	XOF	Franc	229			fr-BJ	2395170	NE,TG,BF,NG	
BL	BLM	652	TB	Saint Barthelemy	Gustavia	21	8450	NA	.gp	EUR	Euro	590	#####	^(\d{5})$	fr	3578476		
BM	BMU	060	BD	Bermuda	Hamilton	53	63968	NA	.bm	BMD	Dollar	+1-441	@@ ##	^([A-Z]{2}\d{2})$	en-BM,pt	3573345		
BN	BRN	096	BX	Brunei	Bandar Seri Begawan	5770	428962	AS	.bn	BND	Dollar	673	@@####	^([A-Z]{2}\d{4})$	ms-BN,en-BN	1820814	MY	
BO	BOL	068	BL	Bolivia	Sucre	1098580	11353142	SA	.bo	BOB	Boliviano	591			es-BO,qu,ay	3923057	PE,CL,PY,BR,AR	
BQ	BES	535		Bonaire, Saint Eustatius and Saba 		328	18012	NA	.bq	USD	Dollar	599			nl,pap,en	7626844		
BR	BRA	076	BR	Brazil	Brasilia	8511965	209469333	SA	.br	BRL	Real	55	#####-###	^\d{5}-\d{3}$	pt-BR,es,en,fr	3469034	SR,PE,BO,UY,GY,PY,GF,VE,CO,AR	
BS	BHS	044	BF	Bahamas	Nassau	13940	385640	NA	.bs	BSD	Dollar	+1-242			en-BS	3572887		
BT	BTN	064	BT	Bhutan	Thimphu	47000	754394	AS	.bt	BTN	Ngultrum	975			dz	1252634	CN,IN	
BV	BVT	074	BV	Bouvet Island		49	0	AN	.bv	NOK	Krone					3371123		
BW	BWA	072	BC	Botswana	Gaborone	600370	2254126	AF	.bw	BWP	Pula	267			en-BW,tn-BW	933860	ZW,ZA,NA	
BY	BLR	112	BO	Belarus	Minsk	207600	9485386	EU	.by	BYN	Belarusian ruble	375	######	^(\d{6})$	be,ru	630336	PL,LT,UA,RU,LV	
BZ	BLZ	084	BH	Belize	Belmopan	22966	383071	NA	.bz	BZD	Dollar	501			en-BZ,es	3582678	GT,MX	
CA	CAN	124	CA	Canada	Ottawa	9984670	37058856	NA	.ca	CAD	Dollar	1	@#@ #@#	^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) ?(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$ 	en-CA,fr-CA,iu	6251999	US	
CC	CCK	166	CK	Cocos Islands	West Island	14	628	AS	.cc	AUD	Dollar	61			ms-CC,en	1547376		
CD	COD	180	CG	Democratic Republic of the Congo	Kinshasa	2345410	84068091	AF	.cd	CDF	Franc	243			fr-CD,ln,ktu,kg,sw,lua	203312	TZ,CF,SS,RW,ZM,BI,UG,CG,AO	
CF	CAF	140	CT	Central African Republic	Bangui	622984	4666377	AF	.cf	XAF	Franc	236			fr-CF,sg,ln,kg	239880	TD,SD,CD,SS,CM,CG	
CG	COG	178	CF	Republic of the Congo	Brazzaville	342000	5244363	AF	.cg	XAF	Franc	242			fr-CG,kg,ln-CG	2260494	CF,GA,CD,CM,AO	
CH	CHE	756	SZ	Switzerland	Bern	41290	8516543	EU	.ch	CHF	Franc	41	####	^(\d{4})$	de-CH,fr-CH,it-CH,rm	2658434	DE,IT,LI,FR,AT	
CI	CIV	384	IV	Ivory Coast	Yamoussoukro	322460	25069229	AF	.ci	XOF	Franc	225			fr-CI	2287781	LR,GH,GN,BF,ML	
CK	COK	184	CW	Cook Islands	Avarua	240	21388	OC	.ck	NZD	Dollar	682			en-CK,mi	1899402		
CL	CHL	152	CI	Chile	Santiago	756950	18729160	SA	.cl	CLP	Peso	56	#######	^(\d{7})$	es-CL	3895114	PE,BO,AR	
CM	CMR	120	CM	Cameroon	Yaounde	475440	25216237	AF	.cm	XAF	Franc	237			en-CM,fr-CM	2233387	TD,CF,GA,GQ,CG,NG	
CN	CHN	156	CH	China	Beijing	9596960	1411778724	AS	.cn	CNY	Yuan Renminbi	86	######	^(\d{6})$	zh-CN,yue,wuu,dta,ug,za	1814991	LA,BT,TJ,KZ,MN,AF,NP,MM,KG,PK,KP,RU,VN,IN	
CO	COL	170	CO	Colombia	Bogota	1138910	49648685	SA	.co	COP	Peso	57	######	^(\d{6})$	es-CO	3686110	EC,PE,PA,BR,VE	
CR	CRI	188	CS	Costa Rica	San Jose	51100	4999441	NA	.cr	CRC	Colon	506	#####	^(\d{5})$	es-CR,en	3624060	PA,NI	
CU	CUB	192	CU	Cuba	Havana	110860	11338138	NA	.cu	CUP	Peso	53	CP #####	^(?:CP)*(\d{5})$	es-CU,pap	3562981	US	
CV	CPV	132	CV	Cabo Verde	Praia	4033	543767	AF	.cv	CVE	Escudo	238	####	^(\d{4})$	pt-CV	3374766		
CW	CUW	531	UC	Curacao	 Willemstad	444	159849	NA	.cw	ANG	Guilder	599			nl,pap	7626836		
CX	CXR	162	KT	Christmas Island	Flying Fish Cove	135	1500	OC	.cx	AUD	Dollar	61	####	^(\d{4})$	en,zh,ms-CX	2078138		
CY	CYP	196	CY	Cyprus	Nicosia	9250	1189265	EU	.cy	EUR	Euro	357	####	^(\d{4})$	el-CY,tr-CY,en	146669		
CZ	CZE	203	EZ	Czechia	Prague	78866	10625695	EU	.cz	CZK	Koruna	420	### ##	^\d{3}\s?\d{2}$	cs,sk	3077311	PL,DE,SK,AT	
DE	DEU	276	GM	Germany	Berlin	357021	82927922	EU	.de	EUR	Euro	49	#####	^(\d{5})$	de	2921044	CH,PL,NL,DK,BE,CZ,LU,FR,AT	
DJ	DJI	262	DJ	Djibouti	Djibouti	23000	958920	AF	.dj	DJF	Franc	253			fr-DJ,ar,so-DJ,aa	223816	ER,ET,SO	
DK	DNK	208	DA	Denmark	Copenhagen	43094	5797446	EU	.dk	DKK	Krone	45	####	^(\d{4})$	da-DK,en,fo,de-DK	2623032	DE	
DM	DMA	212	DO	Dominica	Roseau	754	71625	NA	.dm	XCD	Dollar	+1-767			en-DM	3575830		
DO	DOM	214	DR	Dominican Republic	Santo Domingo	48730	10627165	NA	.do	DOP	Peso	+1-809 and 1-829	#####	^(\d{5})$	es-DO	3508796	HT	
DZ	DZA	012	AG	Algeria	Algiers	2381740	42228429	AF	.dz	DZD	Dinar	213	#####	^(\d{5})$	ar-DZ	2589581	NE,EH,LY,MR,TN,MA,ML	
EC	ECU	218	EC	Ecuador	Quito	283560	17084357	SA	.ec	USD	Dollar	593	@####@	^([a-zA-Z]\d{4}[a-zA-Z])$	es-EC	3658394	PE,CO	
EE	EST	233	EN	Estonia	Tallinn	45226	1320884	EU	.ee	EUR	Euro	372	#####	^(\d{5})$	et,ru	453733	RU,LV	
EG	EGY	818	EG	Egypt	Cairo	1001450	98423595	AF	.eg	EGP	Pound	20	#####	^(\d{5})$	ar-EG,en,fr	357994	LY,SD,IL,PS	
EH	ESH	732	WI	Western Sahara	El-Aaiun	266000	273008	AF	.eh	MAD	Dirham	212			ar,mey	2461445	DZ,MR,MA	
ER	ERI	232	ER	Eritrea	Asmara	121320	6209262	AF	.er	ERN	Nakfa	291			aa-ER,ar,tig,kun,ti-ER	338010	ET,SD,DJ	
ES	ESP	724	SP	Spain	Madrid	504782	46723749	EU	.es	EUR	Euro	34	#####	^(\d{5})$	es-ES,ca,gl,eu,oc	2510769	AD,PT,GI,FR,MA	
ET	ETH	231	ET	Ethiopia	Addis Ababa	1127127	109224559	AF	.et	ETB	Birr	251	####	^(\d{4})$	am,en-ET,om-ET,ti-ET,so-ET,sid	337996	ER,KE,SD,SS,SO,DJ	
FI	FIN	246	FI	Finland	Helsinki	337030	5518050	EU	.fi	EUR	Euro	358	#####	^(?:FI)*(\d{5})$	fi-FI,sv-FI,smn	660013	NO,RU,SE	
FJ	FJI	242	FJ	Fiji	Suva	18270	883483	OC	.fj	FJD	Dollar	679			en-FJ,fj	2205218		
FK	FLK	238	FK	Falkland Islands	Stanley	12173	2638	SA	.fk	FKP	Pound	500			en-FK	3474414		
FM	FSM	583	FM	Micronesia	Palikir	702	112640	OC	.fm	USD	Dollar	691	#####	^(\d{5})$	en-FM,chk,pon,yap,kos,uli,woe,nkr,kpg	2081918		
FO	FRO	234	FO	Faroe Islands	Torshavn	1399	48497	EU	.fo	DKK	Krone	298	###	^(?:FO)*(\d{3})$	fo,da-FO	2622320		
FR	FRA	250	FR	France	Paris	547030	66987244	EU	.fr	EUR	Euro	33	#####	^(\d{5})$	fr-FR,frp,br,co,ca,eu,oc	3017382	CH,DE,BE,LU,IT,AD,MC,ES	
GA	GAB	266	GB	Gabon	Libreville	267667	2119275	AF	.ga	XAF	Franc	241			fr-GA	2400553	CM,GQ,CG	
GB	GBR	826	UK	United Kingdom	London	244820	66488991	EU	.uk	GBP	Pound	44	@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA	^([Gg][Ii][Rr]\s?0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z]))))\s?[0-9][A-Za-z]{2})$	en-GB,cy-GB,gd	2635167	IE	
GD	GRD	308	GJ	Grenada	St. George's	344	111454	NA	.gd	XCD	Dollar	+1-473			en-GD	3580239		
GE	GEO	268	GG	Georgia	Tbilisi	69700	3731000	AS	.ge	GEL	Lari	995	####	^(\d{4})$	ka,ru,hy,az	614540	AM,AZ,TR,RU	
GF	GUF	254	FG	French Guiana	Cayenne	91000	195506	SA	.gf	EUR	Euro	594	#####	^((97|98)3\d{2})$	fr-GF	3381670	SR,BR	
GG	GGY	831	GK	Guernsey	St Peter Port	78	65228	EU	.gg	GBP	Pound	+44-1481	@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA	^((?:(?:[A-PR-UWYZ][A-HK-Y]\d[ABEHMNPRV-Y0-9]|[A-PR-UWYZ]\d[A-HJKPS-UW0-9])\s\d[ABD-HJLNP-UW-Z]{2})|GIR\s?0AA)$	en,nrf	3042362		
GH	GHA	288	GH	Ghana	Accra	239460	29767108	AF	.gh	GHS	Cedi	233			en-GH,ak,ee,tw	2300660	CI,TG,BF	
GI	GIB	292	GI	Gibraltar	Gibraltar	6.5	33718	EU	.gi	GIP	Pound	350			en-GI,es,it,pt	2411586	ES	
GL	GRL	304	GL	Greenland	Nuuk	2166086	56025	NA	.gl	DKK	Krone	299	####	^(\d{4})$	kl,da-GL,en	3425505		
GM	GMB	270	GA	Gambia	Banjul	11300	2280102	AF	.gm	GMD	Dalasi	220			en-GM,mnk,wof,wo,ff	2413451	SN	
GN	GIN	324	GV	Guinea	Conakry	245857	12414318	AF	.gn	GNF	Franc	224			fr-GN	2420477	LR,SN,SL,CI,GW,ML	
GP	GLP	312	GP	Guadeloupe	Basse-Terre	1780	443000	NA	.gp	EUR	Euro	590	#####	^((97|98)\d{3})$	fr-GP	3579143		
GQ	GNQ	226	EK	Equatorial Guinea	Malabo	28051	1308974	AF	.gq	XAF	Franc	240			es-GQ,fr,pt	2309096	GA,CM	
GR	GRC	300	GR	Greece	Athens	131940	10727668	EU	.gr	EUR	Euro	30	### ##	^(\d{5})$	el-GR,en,fr	390903	AL,MK,TR,BG	
GS	SGS	239	SX	South Georgia and the South Sandwich Islands	Grytviken	3903	30	AN	.gs	GBP	Pound				en	3474415		
GT	GTM	320	GT	Guatemala	Guatemala City	108890	17247807	NA	.gt	GTQ	Quetzal	502	#####	^(\d{5})$	es-GT	3595528	MX,HN,BZ,SV	
GU	GUM	316	GQ	Guam	Hagatna	549	165768	OC	.gu	USD	Dollar	+1-671	969##	^(969\d{2})$	en-GU,ch-GU	4043988		
GW	GNB	624	PU	Guinea-Bissau	Bissau	36120	1874309	AF	.gw	XOF	Franc	245	####	^(\d{4})$	pt-GW,pov	2372248	SN,GN	
GY	GUY	328	GY	Guyana	Georgetown	214970	779004	SA	.gy	GYD	Dollar	592			en-GY	3378535	SR,BR,VE	
HK	HKG	344	HK	Hong Kong	Hong Kong	1092	7451000	AS	.hk	HKD	Dollar	852			zh-HK,yue,zh,en	1819730		
HM	HMD	334	HM	Heard Island and McDonald Islands		412	0	AN	.hm	AUD	Dollar	 				1547314		
HN	HND	340	HO	Honduras	Tegucigalpa	112090	9587522	NA	.hn	HNL	Lempira	504	@@####	^([A-Z]{2}\d{4})$	es-HN,cab,miq	3608932	GT,NI,SV	
HR	HRV	191	HR	Croatia	Zagreb	56542	3871833	EU	.hr	EUR	Euro	385	#####	^(?:HR)*(\d{5})$	hr-HR,sr	3202326	HU,SI,BA,ME,RS	
HT	HTI	332	HA	Haiti	Port-au-Prince	27750	11123176	NA	.ht	HTG	Gourde	509	HT####	^(?:HT)*(\d{4})$	ht,fr-HT	3723988	DO	
HU	HUN	348	HU	Hungary	Budapest	93030	9768785	EU	.hu	HUF	Forint	36	####	^(\d{4})$	hu-HU	719819	SK,SI,RO,UA,HR,AT,RS	
ID	IDN	360	ID	Indonesia	Jakarta	1919440	267663435	AS	.id	IDR	Rupiah	62	#####	^(\d{5})$	id,en,nl,jv	1643084	PG,TL,MY	
IE	IRL	372	EI	Ireland	Dublin	70280	4853506	EU	.ie	EUR	Euro	353	@@@ @@@@	^(D6W|[AC-FHKNPRTV-Y][0-9]{2})\s?([AC-FHKNPRTV-Y0-9]{4})	en-IE,ga-IE	2963597	GB	
IL	ISR	376	IS	Israel	Jerusalem	20770	8883800	AS	.il	ILS	Shekel	972	#######	^(\d{7}|\d{5})$	he,ar-IL,en-IL,	294640	SY,JO,LB,EG,PS	
IM	IMN	833	IM	Isle of Man	Douglas	572	84077	EU	.im	GBP	Pound	+44-1624	@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA	^((?:(?:[A-PR-UWYZ][A-HK-Y]\d[ABEHMNPRV-Y0-9]|[A-PR-UWYZ]\d[A-HJKPS-UW0-9])\s\d[ABD-HJLNP-UW-Z]{2})|GIR\s?0AA)$	en,gv	3042225		
IN	IND	356	IN	India	New Delhi	3287590	1352617328	AS	.in	INR	Rupee	91	######	^(\d{6})$	en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc	1269750	CN,NP,MM,BT,PK,BD	
IO	IOT	086	IO	British Indian Ocean Territory	Diego Garcia	60	4000	AS	.io	USD	Dollar	246			en-IO	1282588		
IQ	IRQ	368	IZ	Iraq	Baghdad	437072	38433600	AS	.iq	IQD	Dinar	964	#####	^(\d{5})$	ar-IQ,ku,hy	99237	SY,SA,IR,JO,TR,KW	
IR	IRN	364	IR	Iran	Tehran	1648000	81800269	AS	.ir	IRR	Rial	98	##########	^(\d{10})$	fa-IR,ku	130758	TM,AF,IQ,AM,PK,AZ,TR	
IS	ISL	352	IC	Iceland	Reykjavik	103000	353574	EU	.is	ISK	Krona	354	###	^(\d{3})$	is,en,de,da,sv,no	2629691		
IT	ITA	380	IT	Italy	Rome	301230	60431283	EU	.it	EUR	Euro	39	#####	^(\d{5})$	it-IT,de-IT,fr-IT,sc,ca,co,sl	3175395	CH,VA,SI,SM,FR,AT	
JE	JEY	832	JE	Jersey	Saint Helier	116	90812	EU	.je	GBP	Pound	+44-1534	@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA	^((?:(?:[A-PR-UWYZ][A-HK-Y]\d[ABEHMNPRV-Y0-9]|[A-PR-UWYZ]\d[A-HJKPS-UW0-9])\s\d[ABD-HJLNP-UW-Z]{2})|GIR\s?0AA)$	en,fr,nrf	3042142		
JM	JAM	388	JM	Jamaica	Kingston	10991	2934855	NA	.jm	JMD	Dollar	+1-876			en-JM	3489940		
JO	JOR	400	JO	Jordan	Amman	92300	9956011	AS	.jo	JOD	Dinar	962	#####	^(\d{5})$	ar-JO,en	248816	SY,SA,IQ,IL,PS	
JP	JPN	392	JA	Japan	Tokyo	377835	126529100	AS	.jp	JPY	Yen	81	###-####	^\d{3}-\d{4}$	ja	1861060		
KE	KEN	404	KE	Kenya	Nairobi	582650	51393010	AF	.ke	KES	Shilling	254	#####	^(\d{5})$	en-KE,sw-KE	192950	ET,TZ,SS,SO,UG	
KG	KGZ	417	KG	Kyrgyzstan	Bishkek	198500	6315800	AS	.kg	KGS	Som	996	######	^(\d{6})$	ky,uz,ru	1527747	CN,TJ,UZ,KZ	
KH	KHM	116	CB	Cambodia	Phnom Penh	181040	16249798	AS	.kh	KHR	Riels	855	#####	^(\d{5})$	km,fr,en	1831722	LA,TH,VN	
KI	KIR	296	KR	Kiribati	Tarawa	811	115847	OC	.ki	AUD	Dollar	686			en-KI,gil	4030945		
KM	COM	174	CN	Comoros	Moroni	2170	832322	AF	.km	KMF	Franc	269			ar,fr-KM	921929		
KN	KNA	659	SC	Saint Kitts and Nevis	Basseterre	261	52441	NA	.kn	XCD	Dollar	+1-869			en-KN	3575174		
KP	PRK	408	KN	North Korea	Pyongyang	120540	25549819	AS	.kp	KPW	Won	850	###-###	^(\d{6})$	ko-KP	1873107	CN,KR,RU	
KR	KOR	410	KS	South Korea	Seoul	98480	51635256	AS	.kr	KRW	Won	82	#####	^(\d{5})$	ko-KR,en	1835841	KP	
XK	XKX	0	KV	Kosovo	Pristina	10908	1845300	EU		EUR	Euro				sq,sr	831053	RS,AL,MK,ME	
KW	KWT	414	KU	Kuwait	Kuwait City	17820	4137309	AS	.kw	KWD	Dinar	965	#####	^(\d{5})$	ar-KW,en	285570	SA,IQ	
KY	CYM	136	CJ	Cayman Islands	George Town	262	64174	NA	.ky	KYD	Dollar	+1-345			en-KY	3580718		
KZ	KAZ	398	KZ	Kazakhstan	Nur-Sultan	2717300	18276499	AS	.kz	KZT	Tenge	7	######	^(\d{6})$	kk,ru	1522867	TM,CN,KG,UZ,RU	
LA	LAO	418	LA	Laos	Vientiane	236800	7061507	AS	.la	LAK	Kip	856	#####	^(\d{5})$	lo,fr,en	1655842	CN,MM,KH,TH,VN	
LB	LBN	422	LE	Lebanon	Beirut	10400	6848925	AS	.lb	LBP	Pound	961	#### ####|####	^(\d{4}(\d{4})?)$	ar-LB,fr-LB,en,hy	272103	SY,IL	
LC	LCA	662	ST	Saint Lucia	Castries	616	181889	NA	.lc	XCD	Dollar	+1-758			en-LC	3576468		
LI	LIE	438	LS	Liechtenstein	Vaduz	160	37910	EU	.li	CHF	Franc	423	####	^(\d{4})$	de-LI	3042058	CH,AT	
LK	LKA	144	CE	Sri Lanka	Colombo	65610	21670000	AS	.lk	LKR	Rupee	94	#####	^(\d{5})$	si,ta,en	1227603		
LR	LBR	430	LI	Liberia	Monrovia	111370	4818977	AF	.lr	LRD	Dollar	231	####	^(\d{4})$	en-LR	2275384	SL,CI,GN	
LS	LSO	426	LT	Lesotho	Maseru	30355	2108132	AF	.ls	LSL	Loti	266	###	^(\d{3})$	en-LS,st,zu,xh	932692	ZA	
LT	LTU	440	LH	Lithuania	Vilnius	65200	2789533	EU	.lt	EUR	Euro	370	LT-#####	^(?:LT)*(\d{5})$	lt,ru,pl	597427	PL,BY,RU,LV	
LU	LUX	442	LU	Luxembourg	Luxembourg	2586	607728	EU	.lu	EUR	Euro	352	L-####	^(?:L-)?\d{4}$	lb,de-LU,fr-LU	2960313	DE,BE,FR	
LV	LVA	428	LG	Latvia	Riga	64589	1926542	EU	.lv	EUR	Euro	371	LV-####	^(?:LV)*(\d{4})$	lv,ru,lt	458258	LT,EE,BY,RU	
LY	LBY	434	LY	Libya	Tripoli	1759540	6678567	AF	.ly	LYD	Dinar	218			ar-LY,it,en	2215636	TD,NE,DZ,SD,TN,EG	
MA	MAR	504	MO	Morocco	Rabat	446550	36029138	AF	.ma	MAD	Dirham	212	#####	^(\d{5})$	ar-MA,ber,fr	2542007	DZ,EH,ES	
MC	MCO	492	MN	Monaco	Monaco	1.95	38682	EU	.mc	EUR	Euro	377	#####	^(\d{5})$	fr-MC,en,it	2993457	FR	
MD	MDA	498	MD	Moldova	Chisinau	33843	3545883	EU	.md	MDL	Leu	373	MD-####	^MD-\d{4}$	ro,ru,gag,tr	617790	RO,UA	
ME	MNE	499	MJ	Montenegro	Podgorica	14026	622345	EU	.me	EUR	Euro	382	#####	^(\d{5})$	sr,hu,bs,sq,hr,rom	3194884	AL,HR,BA,RS,XK	
MF	MAF	663	RN	Saint Martin	Marigot	53	37264	NA	.gp	EUR	Euro	590	#####	^(\d{5})$	fr	3578421	SX	
MG	MDG	450	MA	Madagascar	Antananarivo	587040	26262368	AF	.mg	MGA	Ariary	261	###	^(\d{3})$	fr-MG,mg	1062947		
MH	MHL	584	RM	Marshall Islands	Majuro	181.3	58413	OC	.mh	USD	Dollar	692	#####-####	^969\d{2}(-\d{4})$	mh,en-MH	2080185		
MK	MKD	807	MK	North Macedonia	Skopje	25333	2082958	EU	.mk	MKD	Denar	389	####	^(\d{4})$	mk,sq,tr,rmm,sr	718075	AL,GR,BG,RS,XK	
ML	MLI	466	ML	Mali	Bamako	1240000	19077690	AF	.ml	XOF	Franc	223			fr-ML,bm	2453866	SN,NE,DZ,CI,GN,MR,BF	
MM	MMR	104	BM	Myanmar	Nay Pyi Taw	678500	53708395	AS	.mm	MMK	Kyat	95	#####	^(\d{5})$	my	1327865	CN,LA,TH,BD,IN	
MN	MNG	496	MG	Mongolia	Ulaanbaatar	1565000	3170208	AS	.mn	MNT	Tugrik	976	######	^(\d{6})$	mn,ru	2029969	CN,RU	
MO	MAC	446	MC	Macao	Macao	254	631636	AS	.mo	MOP	Pataca	853			zh,zh-MO,pt	1821275		
MP	MNP	580	CQ	Northern Mariana Islands	Saipan	477	56882	OC	.mp	USD	Dollar	+1-670	#####	^9695\d{1}$	fil,tl,zh,ch-MP,en-MP	4041468		
MQ	MTQ	474	MB	Martinique	Fort-de-France	1100	432900	NA	.mq	EUR	Euro	596	#####	^(\d{5})$	fr-MQ	3570311		
MR	MRT	478	MR	Mauritania	Nouakchott	1030700	4403319	AF	.mr	MRU	Ouguiya	222			ar-MR,fuc,snk,fr,mey,wo	2378080	SN,DZ,EH,ML	
MS	MSR	500	MH	Montserrat	Plymouth	102	9341	NA	.ms	XCD	Dollar	+1-664			en-MS	3578097		
MT	MLT	470	MT	Malta	Valletta	316	483530	EU	.mt	EUR	Euro	356	@@@ ####	^[A-Z]{3}\s?\d{4}$	mt,en-MT	2562770		
MU	MUS	480	MP	Mauritius	Port Louis	2040	1265303	AF	.mu	MUR	Rupee	230			en-MU,bho,fr	934292		
MV	MDV	462	MV	Maldives	Male	300	515696	AS	.mv	MVR	Rufiyaa	960	#####	^(\d{5})$	dv,en	1282028		
MW	MWI	454	MI	Malawi	Lilongwe	118480	17563749	AF	.mw	MWK	Kwacha	265	######	^(\d{6})$	ny,yao,tum,swk	927384	TZ,MZ,ZM	
MX	MEX	484	MX	Mexico	Mexico City	1972550	126190788	NA	.mx	MXN	Peso	52	#####	^(\d{5})$	es-MX	3996063	GT,US,BZ	
MY	MYS	458	MY	Malaysia	Kuala Lumpur	329750	31528585	AS	.my	MYR	Ringgit	60	#####	^(\d{5})$	ms-MY,en,zh,ta,te,ml,pa,th	1733045	BN,TH,ID	
MZ	MOZ	508	MZ	Mozambique	Maputo	801590	29495962	AF	.mz	MZN	Metical	258	####	^(\d{4})$	pt-MZ,vmw	1036973	ZW,TZ,SZ,ZA,ZM,MW	
NA	NAM	516	WA	Namibia	Windhoek	825418	2448255	AF	.na	NAD	Dollar	264			en-NA,af,de,hz,naq	3355338	ZA,BW,ZM,AO	
NC	NCL	540	NC	New Caledonia	Noumea	19060	284060	OC	.nc	XPF	Franc	687	#####	^(\d{5})$	fr-NC	2139685		
NE	NER	562	NG	Niger	Niamey	1267000	22442948	AF	.ne	XOF	Franc	227	####	^(\d{4})$	fr-NE,ha,kr,dje	2440476	TD,BJ,DZ,LY,BF,NG,ML	
NF	NFK	574	NF	Norfolk Island	Kingston	34.6	1828	OC	.nf	AUD	Dollar	672	####	^(\d{4})$	en-NF	2155115		
NG	NGA	566	NI	Nigeria	Abuja	923768	195874740	AF	.ng	NGN	Naira	234	######	^(\d{6})$	en-NG,ha,yo,ig,ff	2328926	TD,NE,BJ,CM	
NI	NIC	558	NU	Nicaragua	Managua	129494	6465513	NA	.ni	NIO	Cordoba	505	###-###-#	^(\d{7})$	es-NI,en	3617476	CR,HN	
NL	NLD	528	NL	Netherlands	Amsterdam	41526	17231017	EU	.nl	EUR	Euro	31	#### @@	^(\d{4}\s?[a-zA-Z]{2})$	nl-NL,fy-NL	2750405	DE,BE	
NO	NOR	578	NO	Norway	Oslo	324220	5314336	EU	.no	NOK	Krone	47	####	^(\d{4})$	no,nb,nn,se,fi	3144096	FI,RU,SE	
NP	NPL	524	NP	Nepal	Kathmandu	140800	28087871	AS	.np	NPR	Rupee	977	#####	^(\d{5})$	ne,en	1282988	CN,IN	
NR	NRU	520	NR	Nauru	Yaren	21	12704	OC	.nr	AUD	Dollar	674			na,en-NR	2110425		
NU	NIU	570	NE	Niue	Alofi	260	2166	OC	.nu	NZD	Dollar	683			niu,en-NU	4036232		
NZ	NZL	554	NZ	New Zealand	Wellington	268680	4885500	OC	.nz	NZD	Dollar	64	####	^(\d{4})$	en-NZ,mi	2186224		
OM	OMN	512	MU	Oman	Muscat	212460	4829483	AS	.om	OMR	Rial	968	###	^(\d{3})$	ar-OM,en,bal,ur	286963	SA,YE,AE	
PA	PAN	591	PM	Panama	Panama City	78200	4176873	NA	.pa	PAB	Balboa	507			es-PA,en	3703430	CR,CO	
PE	PER	604	PE	Peru	Lima	1285220	31989256	SA	.pe	PEN	Sol	51	#####	^(\d{5})$	es-PE,qu,ay	3932488	EC,CL,BO,BR,CO	
PF	PYF	258	FP	French Polynesia	Papeete	4167	277679	OC	.pf	XPF	Franc	689	#####	^((97|98)7\d{2})$	fr-PF,ty	4030656		
PG	PNG	598	PP	Papua New Guinea	Port Moresby	462840	8606316	OC	.pg	PGK	Kina	675	###	^(\d{3})$	en-PG,ho,meu,tpi	2088628	ID	
PH	PHL	608	RP	Philippines	Manila	300000	106651922	AS	.ph	PHP	Peso	63	####	^(\d{4})$	tl,en-PH,fil,ceb,ilo,hil,war,pam,bik,bcl,pag,mrw,tsg,mdh,cbk,krj,sgd,msb,akl,ibg,yka,mta,abx	1694008		
PK	PAK	586	PK	Pakistan	Islamabad	803940	212215030	AS	.pk	PKR	Rupee	92	#####	^(\d{5})$	ur-PK,en-PK,pa,sd,ps,brh	1168579	CN,AF,IR,IN	
PL	POL	616	PL	Poland	Warsaw	312685	37978548	EU	.pl	PLN	Zloty	48	##-###	^\d{2}-\d{3}$	pl	798544	DE,LT,SK,CZ,BY,UA,RU	
PM	SPM	666	SB	Saint Pierre and Miquelon	Saint-Pierre	242	7012	NA	.pm	EUR	Euro	508	#####	^(97500)$	fr-PM	3424932		
PN	PCN	612	PC	Pitcairn	Adamstown	47	46	OC	.pn	NZD	Dollar	870			en-PN	4030699		
PR	PRI	630	RQ	Puerto Rico	San Juan	9104	3195153	NA	.pr	USD	Dollar	+1-787 and 1-939	#####-####	^00[679]\d{2}(?:-\d{4})?$	en-PR,es-PR	4566966		
PS	PSE	275	WE	Palestinian Territory	East Jerusalem	5970	4569087	AS	.ps	ILS	Shekel	970			ar-PS	6254930	JO,IL,EG	
PT	PRT	620	PO	Portugal	Lisbon	92391	10281762	EU	.pt	EUR	Euro	351	####-###	^\d{4}-\d{3}\s?[a-zA-Z]{0,25}$	pt-PT,mwl	2264397	ES	
PW	PLW	585	PS	Palau	Melekeok	458	17907	OC	.pw	USD	Dollar	680	96940	^(96940)$	pau,sov,en-PW,tox,ja,fil,zh	1559582		
PY	PRY	600	PA	Paraguay	Asuncion	406750	6956071	SA	.py	PYG	Guarani	595	####	^(\d{4})$	es-PY,gn	3437598	BO,BR,AR	
QA	QAT	634	QA	Qatar	Doha	11437	2781677	AS	.qa	QAR	Rial	974			ar-QA,es	289688	SA	
RE	REU	638	RE	Reunion	Saint-Denis	2517	776948	AF	.re	EUR	Euro	262	#####	^((97|98)(4|7|8)\d{2})$	fr-RE	935317		
RO	ROU	642	RO	Romania	Bucharest	237500	19473936	EU	.ro	RON	Leu	40	######	^(\d{6})$	ro,hu,rom	798549	MD,HU,UA,BG,RS	
RS	SRB	688	RI	Serbia	Belgrade	88361	6982084	EU	.rs	RSD	Dinar	381	######	^(\d{6})$	sr,hu,bs,rom	6290252	AL,HU,MK,RO,HR,BA,BG,ME,XK	
RU	RUS	643	RS	Russia	Moscow	17100000	144478050	EU	.ru	RUB	Ruble	7	######	^(\d{6})$	ru,tt,xal,cau,ady,kv,ce,tyv,cv,udm,tut,mns,bua,myv,mdf,chm,ba,inh,kbd,krc,av,sah,nog	2017370	GE,CN,BY,UA,KZ,LV,PL,EE,LT,FI,MN,NO,AZ,KP	
RW	RWA	646	RW	Rwanda	Kigali	26338	12301939	AF	.rw	RWF	Franc	250			rw,en-RW,fr-RW,sw	49518	TZ,CD,BI,UG	
SA	SAU	682	SA	Saudi Arabia	Riyadh	1960582	33699947	AS	.sa	SAR	Rial	966	#####	^(\d{5})$	ar-SA	102358	QA,OM,IQ,YE,JO,AE,KW	
SB	SLB	090	BP	Solomon Islands	Honiara	28450	652858	OC	.sb	SBD	Dollar	677			en-SB,tpi	2103350		
SC	SYC	690	SE	Seychelles	Victoria	455	96762	AF	.sc	SCR	Rupee	248			en-SC,fr-SC	241170		
SD	SDN	729	SU	Sudan	Khartoum	1861484	41801533	AF	.sd	SDG	Pound	249	#####	^(\d{5})$	ar-SD,en,fia	366755	SS,TD,EG,ET,ER,LY,CF	
SS	SSD	728	OD	South Sudan	Juba	644329	8260490	AF	.ss	SSP	Pound	211			en	7909807	CD,CF,ET,KE,SD,UG	
SE	SWE	752	SW	Sweden	Stockholm	449964	10183175	EU	.se	SEK	Krona	46	### ##	^(?:SE)?\d{3}\s\d{2}$	sv-SE,se,sma,fi-SE	2661886	NO,FI	
SG	SGP	702	SN	Singapore	Singapore	692.7	5638676	AS	.sg	SGD	Dollar	65	######	^(\d{6})$	cmn,en-SG,ms-SG,ta-SG,zh-SG	1880251		
SH	SHN	654	SH	Saint Helena	Jamestown	410	7460	AF	.sh	SHP	Pound	290	STHL 1ZZ	^(STHL1ZZ)$	en-SH	3370751		
SI	SVN	705	SI	Slovenia	Ljubljana	20273	2067372	EU	.si	EUR	Euro	386	####	^(?:SI)*(\d{4})$	sl,sh	3190538	HU,IT,HR,AT	
SJ	SJM	744	SV	Svalbard and Jan Mayen	Longyearbyen	62049	2550	EU	.sj	NOK	Krone	47	####	^(\d{4})$	no,ru	607072		
SK	SVK	703	LO	Slovakia	Bratislava	48845	5447011	EU	.sk	EUR	Euro	421	### ##	^\d{3}\s?\d{2}$	sk,hu	3057568	PL,HU,CZ,UA,AT	
SL	SLE	694	SL	Sierra Leone	Freetown	71740	7650154	AF	.sl	SLL	Leone	232			en-SL,men,tem	2403846	LR,GN	
SM	SMR	674	SM	San Marino	San Marino	61.2	33785	EU	.sm	EUR	Euro	378	4789#	^(4789\d)$	it-SM	3168068	IT	
SN	SEN	686	SG	Senegal	Dakar	196190	15854360	AF	.sn	XOF	Franc	221	#####	^(\d{5})$	fr-SN,wo,fuc,mnk	2245662	GN,MR,GW,GM,ML	
SO	SOM	706	SO	Somalia	Mogadishu	637657	15008154	AF	.so	SOS	Shilling	252	@@  #####	^([A-Z]{2}\d{5})$	so-SO,ar-SO,it,en-SO	51537	ET,KE,DJ	
SR	SUR	740	NS	Suriname	Paramaribo	163270	575991	SA	.sr	SRD	Dollar	597			nl-SR,en,srn,hns,jv	3382998	GY,BR,GF	
ST	STP	678	TP	Sao Tome and Principe	Sao Tome	1001	197700	AF	.st	STN	Dobra	239			pt-ST	2410758		
SV	SLV	222	ES	El Salvador	San Salvador	21040	6420744	NA	.sv	USD	Dollar	503	CP ####	^(?:CP)*(\d{4})$	es-SV	3585968	GT,HN	
SX	SXM	534	NN	Sint Maarten	Philipsburg	21	40654	NA	.sx	ANG	Guilder	599			nl,en	7609695	MF	
SY	SYR	760	SY	Syria	Damascus	185180	16906283	AS	.sy	SYP	Pound	963			ar-SY,ku,hy,arc,fr,en	163843	IQ,JO,IL,TR,LB	
SZ	SWZ	748	WZ	Eswatini	Mbabane	17363	1136191	AF	.sz	SZL	Lilangeni	268	@###	^([A-Z]\d{3})$	en-SZ,ss-SZ	934841	ZA,MZ	
TC	TCA	796	TK	Turks and Caicos Islands	Cockburn Town	430	37665	NA	.tc	USD	Dollar	+1-649	TKCA 1ZZ	^(TKCA 1ZZ)$	en-TC	3576916		
TD	TCD	148	CD	Chad	N'Djamena	1284000	15477751	AF	.td	XAF	Franc	235			fr-TD,ar-TD,sre	2434508	NE,LY,CF,SD,CM,NG	
TF	ATF	260	FS	French Southern Territories	Port-aux-Francais	7829	140	AN	.tf	EUR	Euro				fr	1546748		
TG	TGO	768	TO	Togo	Lome	56785	7889094	AF	.tg	XOF	Franc	228			fr-TG,ee,hna,kbp,dag,ha	2363686	BJ,GH,BF	
TH	THA	764	TH	Thailand	Bangkok	514000	69428524	AS	.th	THB	Baht	66	#####	^(\d{5})$	th,en	1605651	LA,MM,KH,MY	
TJ	TJK	762	TI	Tajikistan	Dushanbe	143100	9100837	AS	.tj	TJS	Somoni	992	######	^(\d{6})$	tg,ru	1220409	CN,AF,KG,UZ	
TK	TKL	772	TL	Tokelau		10	1466	OC	.tk	NZD	Dollar	690			tkl,en-TK	4031074		
TL	TLS	626	TT	Timor Leste	Dili	15007	1267972	OC	.tl	USD	Dollar	670			tet,pt-TL,id,en	1966436	ID	
TM	TKM	795	TX	Turkmenistan	Ashgabat	488100	5850908	AS	.tm	TMT	Manat	993	######	^(\d{6})$	tk,ru,uz	1218197	AF,IR,UZ,KZ	
TN	TUN	788	TS	Tunisia	Tunis	163610	11565204	AF	.tn	TND	Dinar	216	####	^(\d{4})$	ar-TN,fr	2464461	DZ,LY	
TO	TON	776	TN	Tonga	Nuku'alofa	748	103197	OC	.to	TOP	Pa'anga	676			to,en-TO	4032283		
TR	TUR	792	TU	Turkey	Ankara	780580	82319724	AS	.tr	TRY	Lira	90	#####	^(\d{5})$	tr-TR,ku,diq,az,av	298795	SY,GE,IQ,IR,GR,AM,AZ,BG	
TT	TTO	780	TD	Trinidad and Tobago	Port of Spain	5128	1389858	NA	.tt	TTD	Dollar	+1-868			en-TT,hns,fr,es,zh	3573591		
TV	TUV	798	TV	Tuvalu	Funafuti	26	11508	OC	.tv	AUD	Dollar	688			tvl,en,sm,gil	2110297		
TW	TWN	158	TW	Taiwan	Taipei	35980	23451837	AS	.tw	TWD	Dollar	886	#####	^(\d{5})$	zh-TW,zh,nan,hak	1668284		
TZ	TZA	834	TZ	Tanzania	Dodoma	945087	56318348	AF	.tz	TZS	Shilling	255			sw-TZ,en,ar	149590	MZ,KE,CD,RW,ZM,BI,UG,MW	
UA	UKR	804	UP	Ukraine	Kyiv	603700	44622516	EU	.ua	UAH	Hryvnia	380	#####	^(\d{5})$	uk,ru-UA,rom,pl,hu	690791	PL,MD,HU,SK,BY,RO,RU	
UG	UGA	800	UG	Uganda	Kampala	236040	42723139	AF	.ug	UGX	Shilling	256			en-UG,lg,sw,ar	226074	TZ,KE,SS,CD,RW	
UM	UMI	581		United States Minor Outlying Islands		0	0	OC	.um	USD	Dollar	1			en-UM	5854968		
US	USA	840	US	United States	Washington	9629091	327167434	NA	.us	USD	Dollar	1	#####-####	^\d{5}(-\d{4})?$	en-US,es-US,haw,fr	6252001	CA,MX,CU	
UY	URY	858	UY	Uruguay	Montevideo	176220	3449299	SA	.uy	UYU	Peso	598	#####	^(\d{5})$	es-UY	3439705	BR,AR	
UZ	UZB	860	UZ	Uzbekistan	Tashkent	447400	32955400	AS	.uz	UZS	Som	998	######	^(\d{6})$	uz,ru,tg	1512440	TM,AF,KG,TJ,KZ	
VA	VAT	336	VT	Vatican	Vatican City	0.44	921	EU	.va	EUR	Euro	379	#####	^(\d{5})$	la,it,fr	3164670	IT	
VC	VCT	670	VC	Saint Vincent and the Grenadines	Kingstown	389	110211	NA	.vc	XCD	Dollar	+1-784			en-VC,fr	3577815		
VE	VEN	862	VE	Venezuela	Caracas	912050	28870195	SA	.ve	VES	Bolivar Soberano	58	####	^(\d{4})$	es-VE	3625428	GY,BR,CO	
VG	VGB	092	VI	British Virgin Islands	Road Town	153	29802	NA	.vg	USD	Dollar	+1-284			en-VG	3577718		
VI	VIR	850	VQ	U.S. Virgin Islands	Charlotte Amalie	352	106977	NA	.vi	USD	Dollar	+1-340	#####-####	^008\d{2}(?:-\d{4})?$	en-VI	4796775		
VN	VNM	704	VM	Vietnam	Hanoi	329560	95540395	AS	.vn	VND	Dong	84	######	^(\d{6})$	vi,en,fr,zh,km	1562822	CN,LA,KH	
VU	VUT	548	NH	Vanuatu	Port Vila	12200	292680	OC	.vu	VUV	Vatu	678			bi,en-VU,fr-VU	2134431		
WF	WLF	876	WF	Wallis and Futuna	Mata Utu	274	16025	OC	.wf	XPF	Franc	681	#####	^(986\d{2})$	wls,fud,fr-WF	4034749		
WS	WSM	882	WS	Samoa	Apia	2944	196130	OC	.ws	WST	Tala	685			sm,en-WS	4034894		
YE	YEM	887	YM	Yemen	Sanaa	527970	28498687	AS	.ye	YER	Rial	967			ar-YE	69543	SA,OM	
YT	MYT	175	MF	Mayotte	Mamoudzou	374	279471	AF	.yt	EUR	Euro	262	#####	^(\d{5})$	fr-YT	1024031		
ZA	ZAF	710	SF	South Africa	Pretoria	1219912	57779622	AF	.za	ZAR	Rand	27	####	^(\d{4})$	zu,xh,af,nso,en-ZA,tn,st,ts,ss,ve,nr	953987	ZW,SZ,MZ,BW,NA,LS	
ZM	ZMB	894	ZA	Zambia	Lusaka	752614	17351822	AF	.zm	ZMW	Kwacha	260	#####	^(\d{5})$	en-ZM,bem,loz,lun,lue,ny,toi	895949	ZW,TZ,MZ,CD,NA,MW,AO	
ZW	ZWE	716	ZI	Zimbabwe	Harare	390580	14439018	AF	.zw	ZWL	Dollar	263			en-ZW,sn,nr,nd	878675	ZA,MZ,BW,ZM	
CS	SCG	891	YI	Serbia and Montenegro	Belgrade	102350	10829175	EU	.cs	RSD	Dinar	381	#####	^(\d{5})$	cu,hu,sq,sr	8505033	AL,HU,MK,RO,HR,BA,BG	
AN	ANT	530	NT	Netherlands Antilles	Willemstad	960	300000	NA	.an	ANG	Guilder	599			nl-AN,en,es	8505032	GP	
```

## File: `geosuggest-core/tests/misc/names.txt`
```
289156	472045		Woronesh						
1615889	472045	de	Woronesch						
1615890	472045	en	Voronezh						
1615891	472045	bg	Воронеж						
1615892	472045	cs	Voroněž						
1615893	472045	eo	Voroneĵ						
1615894	472045	et	Voronež						
1615895	472045	fr	Voronej						
1615896	472045	ko	보로네시						
1615897	472045	lt	Voronežas						
1615898	472045	lv	Voroņeža						
1615899	472045	nl	Voronezj						
1615900	472045	pl	Woroneż						
1615901	472045	ru	Воронеж	1					
1615902	472045	sl	Voronež						
1638431	472045	fi	Voronež						
1902813	472045	it	Voronezh						
1902814	472045	ja	ヴォロネジ						
1902815	472045	pt	Voronezh						
1991477	472045	it	Voronež						
2181371	472045	ru	Воронежская область						
2923673	472045	link	https://en.wikipedia.org/wiki/Voronezh						
3047887	472045	link	https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6						
3724193	472045		Voronezh						
7481699	472045	iata	VOZ						
13797596	472045	unlc	RUVOZ						
1565727	2643743	la	Londinium						
1565728	2643743	es	Londres						
1565729	2643743	it	Londra						
1565730	2643743	eo	Londono						
1565731	2643743	eu	Londres						
1591343	2643743	de	London						
1591344	2643743	en	London	1					
1591345	2643743	af	Londen						
1591346	2643743	als	London						
1591347	2643743	an	Londres						
1591348	2643743	ang	Lunden						
1591349	2643743	ar	لندن						
1591350	2643743	ast	Londres						
1591351	2643743	be	Лёндан						
1591352	2643743	bg	Лондон						
1591353	2643743	br	Londrez						
1591354	2643743	bs	London						
1591355	2643743	ca	Londres						
1591356	2643743	cs	Londýn						
1591357	2643743	cy	Llundain						
1591358	2643743	da	London						
1591359	2643743	el	Λονδίνο						
1591360	2643743	et	London						
1591361	2643743	eu	London						
1591362	2643743	fi	Lontoo						
1591363	2643743	fr	Londres	1	1				
1591364	2643743	fy	Londen						
1591365	2643743	ga	Londain						
1591366	2643743	gd	Lunnainn						
1591367	2643743	gl	Londres						
1591368	2643743	gu	લંડન						
1591369	2643743	he	לונדון						
1591370	2643743	hi	लंदन						
1591371	2643743	hr	London						
1591372	2643743	hu	London						
1591373	2643743	ia	London						
1591374	2643743	id	London						
1591375	2643743	io	London						
1591376	2643743	is	London						
1591377	2643743	ja	ロンドン						
1591378	2643743	ka	ლონდონი						
1591379	2643743	ko	런던						
1591380	2643743	ku	London						
1591381	2643743	kw	Loundres						
1591382	2643743	lb	London						
1591383	2643743	li	Londe						
1591384	2643743	ln	Londoni						
1591385	2643743	lt	Londonas						
1591386	2643743	lv	Londona						
1591387	2643743	mk	Лондон						
1591388	2643743	ms	London						
1591389	2643743	nds	London						
1591390	2643743	nl	Londen						
1591391	2643743	nn	London						
1591392	2643743	no	London						
1591393	2643743	nrm	Londres						
1591394	2643743	pl	Londyn						
1591395	2643743	pt	Londres						
1591396	2643743	ro	Londra						
1591397	2643743	ru	Лондон						
1591398	2643743	scn	Londra						
1591399	2643743	sco	Lunnon						
1591400	2643743	hbs	London						
1591401	2643743	sk	Londýn						
1591402	2643743	sl	London						
1591403	2643743	sr	Лондон						
1591404	2643743	sv	London						
1591405	2643743	ta	இலண்டன்						
1591406	2643743	th	ลอนดอน						
1591407	2643743	tr	Londra						
1591408	2643743	tt	Лондон						
1591409	2643743	uk	Лондон						
1591410	2643743	vi	Luân Đôn						
1591411	2643743	yi	לאנדאן						
1591412	2643743	zh-CN	伦敦						
1618326	2643743	sq	Londra						
1618327	2643743	vo	London						
1632580	2643743	fa	لندن						
1632581	2643743	frp	Londro						
1632582	2643743	ug	لوندون						
1893910	2643743	am	ለንደን						
1893911	2643743	az	London						
1893912	2643743	bn	লন্ডন						
1893913	2643743	hy	Լոնդոն						
1893914	2643743	mr	लंडन						
1893915	2643743	oc	Londres						
1893916	2643743	os	Лондон						
1893917	2643743	rm	Londra						
1893918	2643743	tg	Лондон						
1893919	2643743	ur	لندن						
1974840	2643743	arc	ܠܘܢܕܘܢ						
1974841	2643743	be	Лондан						
1974842	2643743	co	Londra						
1974843	2643743	pms	Londra						
1974844	2643743	qu	London						
2080510	2643743	iata	LON						
2080708	2643743	is	Lundúnir						
2919903	2643743	link	https://en.wikipedia.org/wiki/London						
3051650	2643743	link	https://uk.wikipedia.org/wiki/%D0%9B%D0%BE%D0%BD%D0%B4%D0%BE%D0%BD						
3173887	2643743		London						
7581111	2643743	ext	Londri						
7581112	2643743	new	लन्दन						
7581113	2643743	mzn	لندن						
7581114	2643743	ilo	Londres						
7581115	2643743	tpi	Landen						
7581116	2643743	mwl	Londres						
7581117	2643743	cv	Лондон						
7581118	2643743	lad	Londra						
7581119	2643743	cu	Лондонъ						
7581120	2643743	wuu	伦敦						
7581121	2643743	ckb	لەندەن						
7581122	2643743	bcl	Londres						
7581123	2643743	mhr	Лондон						
7581124	2643743	bo	ལོན་ཊོན།						
7581125	2643743	pnt	Λονδίνο						
7581126	2643743	jbo	london						
7581127	2643743	ml	ലണ്ടൻ						
7581128	2643743	xmf	ლონდონი						
7581129	2643743	ba	Лондон						
7581130	2643743	pnb	لندن						
7581131	2643743	lbe	Лондон						
7581132	2643743	nap	Londra						
7581133	2643743	ne	लण्डन						
7581134	2643743	my	လန်ဒန်မြို့						
7581135	2643743	ab	Лондан						
7581136	2643743	mn	Лондон						
7581137	2643743	mt	Londra						
7581138	2643743	nah	Londres						
7581139	2643743	haw	Lākana						
7581140	2643743	vls	Londn						
7581141	2643743	mi	Rānana						
7581142	2643743	lmo	Lundra						
7581143	2643743	yo	Lọndọnu						
7581144	2643743	mrj	Лондон						
7581145	2643743	vec	Łondra						
7581146	2643743	gv	Lunnin						
7581147	2643743	te	లండన్						
7581148	2643743	tl	Londres						
7581149	2643743	kv	Лондон						
7581150	2643743	tet	Londres						
7581151	2643743	zea	Londen						
7581152	2643743	sa	लन्डन्						
7581153	2643743	sc	Londra						
7581154	2643743	gan	倫敦						
7581155	2643743	ky	Лондон						
7581156	2643743	arz	لندن						
7581157	2643743	kk	Лондон						
7581158	2643743	krc	Лондон						
7581159	2643743	kn	ಲಂಡನ್						
7581160	2643743	udm	Лондон						
7581161	2643743	wo	Londar						
7581162	2643743	ht	Lonn						
7581163	2643743	sah	Лондон						
7581164	2643743	rue	Лондон						
7581165	2643743	lij	Londra						
7581166	2643743	koi	Лондон						
7581167	2643743	szl	Lůndůn						
7581168	2643743	diq	Londra						
8185503	2643743	cdo	Lùng-dŭng						
8185504	2643743	chr	ᎫᎴ ᏗᏍᎪᏂᎯᏱ						
8185505	2643743	lez	Лондон						
8185506	2643743	lo	ລອນດອນ						
8185507	2643743	or	ଲଣ୍ଡନ						
8185508	2643743	gn	Londye						
8185509	2643743	ps	لندن						
8185510	2643743	pcd	Londe						
8185511	2643743	si	ලන්ඩන්						
8185512	2643743	zu	ILondon						
8185513	2643743	zh	伦敦						
10782258	2643743	link	http://id.loc.gov/authorities/names/n79005665						
11319222	2643743	azb	لندن						
11319223	2643743	sgs	Londons						
11319224	2643743	bh	लंदन						
11319225	2643743	bxr	Лондон						
11319226	2643743	ce	Лондон						
11319227	2643743	csb	Londin						
11319228	2643743	fj	Lodoni						
11319229	2643743	hak	Lùn-tûn						
11319230	2643743	kbd	Лондон						
11319231	2643743	lrc	لأندأن						
11319232	2643743	mai	लण्डन						
11319233	2643743	myv	Лондон ош						
11319234	2643743	om	Landan						
11319235	2643743	pa	ਲੰਡਨ						
11319236	2643743	lzh	倫敦						
11319237	2643743	nan	Lûn-tun						
11319238	2643743	yue	倫敦						
13771511	2643743	unlc	GBLON						
15886483	2643743	wkdt	Q84						
16432734	2643743	zh-TW	倫敦						
16432735	2643743	zh	倫敦						
16126773	12017370		Şāḩib az Zamān						
16126774	12017370	ar	صاحب الزمان						
2017370	2522720	eu	Villaurbana						
12017370	11291212	lt	Molykai						
993186	2017370	en	Russian Soviet Federated Socialist Republic				1		
993187	2017370		Rossiyskaya Sovetskaya Federativnaya Sotsialisticheskaya Respublika				1		
993188	2017370	en	Russian Soviet Federative Socialist Republic				1		
993191	2017370	en	Russian Socialist Federative Soviet Republic				1		
1556474	2017370	aa	Russia	1					
1556475	2017370	af	Rusland	1					
1556476	2017370	am	ሩስያ	1					
1556477	2017370	ar	روسيا	1					
1556478	2017370	be	Расія	1					
1556479	2017370	bg	Руска Федерация						
1556480	2017370	bn	রাশিয়া						
1556481	2017370	ca	Rússia	1					
1556482	2017370	cs	Rusko	1					
1556483	2017370	cy	Rwsia	1					
1556484	2017370	da	Rusland	1					
1556485	2017370	de	Russische Föderation						
1556486	2017370	el	Ρωσία	1					
1556487	2017370	en	Russia	1					
1556488	2017370	eo	Rusujo	1					
1556489	2017370	es	Rusia	1					
1556490	2017370	et	Venemaa	1					
1556491	2017370	eu	Errusia	1					
1556492	2017370	fa	روسیه	1					
1556493	2017370	fi	Venäjä	1					
1556494	2017370	fo	Russland	1					
1556495	2017370	fr	Russie	1					
1556496	2017370	ga	an Rúis	1					
1556497	2017370	he	רוסיה, הפדרציה של						
1556498	2017370	hi	रूस	1					
1556499	2017370	hr	Ruska Federacija						
1556500	2017370	hu	Oroszország	1					
1556501	2017370	hy	Ռուսաստան	1					
1556502	2017370	id	Rusia	1					
1556503	2017370	is	Rússland	1					
1556504	2017370	it	Federazione Russa						
1556505	2017370	ja	ロシア	1					
1556506	2017370	ka	რუსეთი	1					
1556507	2017370	km	រុស្ស៊ី	1					
1556508	2017370	ko	러시아	1					
1556509	2017370	lo	ຣັດເຊຍ	1					
1556510	2017370	lt	Rusija	1					
1556511	2017370	lv	Krievija	1					
1556512	2017370	mk	Русија	1					
1556513	2017370	ms	Rusia	1					
1556514	2017370	mt	ir-Russja	1					
1556515	2017370	nb	Den russiske føderasjon						
1556516	2017370	nl	Russische Federatie						
1556517	2017370	nn	Den russiske føderasjon						
1556518	2017370	om	Russia	1					
1556519	2017370	pl	Rosja	1					
1556520	2017370	ps	روسیه	1					
1556521	2017370	pt	Rússia	1					
1556522	2017370	ro	Rusia	1					
1556523	2017370	ru	Россия	1					
1556524	2017370	sk	Ruská federácia						
1556525	2017370	sl	Ruska federacija						
1556526	2017370	so	Ruush	1					
1556527	2017370	sq	Rusi	1					
1556528	2017370	sr	Русија	1					
1556529	2017370	sv	Ryssland	1					
1556530	2017370	sw	Urusi	1					
1556531	2017370	ta	ரஷ்யா	1					
1556532	2017370	te	రష్యా	1					
1556533	2017370	th	รัสเซีย	1					
1556534	2017370	tr	Rusya Federasyonu						
1556535	2017370	tt	Россия	1					
1556536	2017370	uk	Росія	1					
1556537	2017370	uz	Rossiya	1					
1556538	2017370	vi	Nga	1					
1556539	2017370	zh-TW	俄罗斯	1					
2197904	2017370	ru	Российская Федерация						
2419054	2017370	az	Rusiya	1					
2419055	2017370	be	Расійская Федэрацыя	1					
2419056	2017370	bg	Русия	1					
2419057	2017370	bn	রাশিয়া	1					
2419058	2017370	bo	ཨུ་རུ་སུ་	1					
2419059	2017370	de	Russland	1					
2419060	2017370	gl	Rusia	1					
2419061	2017370	he	חבר המדינות הרוסיות	1					
2419062	2017370	hr	Rusija	1					
2419063	2017370	ii	ꊉꇆꌦ	1					
2419064	2017370	it	Russia	1					
2419065	2017370	ml	റഷ്യ	1					
2419066	2017370	mn	Орос	1					
2419067	2017370	nl	Rusland	1					
2419068	2017370	ro	Federația Rusă	1					
2419069	2017370	se	Ruošša	1					
2419070	2017370	sk	Rusko	1					
2419071	2017370	sl	Rusija	1					
2419072	2017370	to	Lūsia	1					
2419073	2017370	tr	Rusya	1					
2419074	2017370	uk	Російська Федерація	1					
2419075	2017370	ur	روس	1					
2728832	2017370	en	Russian Federation						
2728833	2017370	no	Russland	1					
2728834	2017370	nb	Russland	1					
2728835	2017370	nn	Russland	1					
3075880	2017370	link	https://en.wikipedia.org/wiki/Russia						
3763735	2017370		Rossiyskaya Federatsiya						
5976391	2017370		Russian Soviet Federative Socialist Republic				1		
5976392	2017370		Russian Soviet Federated Socialist Republic				1		
5976393	2017370		Russian Socialist Federative Soviet Republic				1		
7090367	2017370	ak	Rɔhyea	1					
7090368	2017370	as	ৰাছিয়া	1					
7090369	2017370	bm	Irisi	1					
7090370	2017370	br	Rusia	1					
7090371	2017370	bs	Rusija	1					
7090372	2017370	ee	Russia nutome	1					
7090373	2017370	ff	Riisii	1					
7090374	2017370	gu	રશિયા	1					
7090375	2017370	ha	Rasha	1					
7090376	2017370	ki	Urusi	1					
7090377	2017370	kk	Ресей	1					
7090378	2017370	kl	Ruslandi	1					
7090379	2017370	kn	ರಷ್ಯಾ	1					
7090380	2017370	ckb	ڕووسیا						
7090381	2017370	kw	Russi	1					
7090382	2017370	lg	Lasa	1					
7090383	2017370	ln	Risí	1					
7090384	2017370	lu	Risi	1					
7090385	2017370	mg	Rosia	1					
7090386	2017370	mr	रशिया	1					
7090387	2017370	my	ရုရှား	1					
7090388	2017370	nd	Rashiya	1					
7090389	2017370	ne	रूस	1					
7090390	2017370	oc	Russia	1					
7090391	2017370	or	ରୁଷିଆ	1					
7090392	2017370	rm	Russia	1					
7090393	2017370	rn	Uburusiya	1					
7090394	2017370	sg	Rusïi	1					
7090395	2017370	si	රුසියාව	1					
7090396	2017370	sn	Russia	1					
7090397	2017370	ti	ራሺያ	1					
7090398	2017370	yo	Rọṣia	1					
7090399	2017370	zu	i-Russia	1					
8043265	2017370		Rossiya						
10386978	2017370	fy	Ruslân	1					
10795053	2017370	link	http://id.loc.gov/authorities/names/n80001203						
11015585	2017370	olo	Ven'a		1				
11015586	2017370	krl	Venäjä		1				
16076669	2017370	ku	Rûsya	1					
16490081	2017370	zh-CN	俄罗斯联邦						
16925843	2017370	zh-Hant	俄羅斯	1					
16930751	2017370	ce	Росси	1					
16930752	2017370	dz	ཨུ་རུ་སུ	1					
16930753	2017370	gd	An Ruis	1					
16930754	2017370	ia	Russia	1					
16930755	2017370	ig	Rụssịa	1					
16930756	2017370	jv	Rusia	1					
16930757	2017370	ks	روٗس	1					
16930758	2017370	ky	Россия	1					
16930759	2017370	lb	Russland	1					
16930760	2017370	mi	Rūhia	1					
16930761	2017370	os	Уӕрӕсе	1					
16930762	2017370	pa	ਰੂਸ	1					
16930763	2017370	qu	Rusia	1					
16930764	2017370	sa	रष्यदेश:	1					
16930765	2017370	sd	روس	1					
16930766	2017370	su	Rusia	1					
16930767	2017370	tg	Русия	1					
16930768	2017370	tk	Russiýa	1					
16930769	2017370	ug	رۇسىيە	1					
16930770	2017370	wo	Risi	1					
16930771	2017370	yi	רוסלאַנד	1					
16930772	2017370	zh	俄罗斯	1					
289152	472039		Voronezh Oblast						
2185009	472039		Voronezj		1				
2187586	472039	nb	Voronezj						
2187587	472039	nn	Voronezj						
2298618	472039	ru	Воронежская область	1					
2417609	472039	sv	Voronezj						
2486429	472039	no	Voronezjskaja oblast						
2923672	472039	link	https://en.wikipedia.org/wiki/Voronezh_Oblast						
3047886	472039	link	https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C						
5649326	472039		Voronezhskaya Oblast’						
8656351	472039	ru	Воронежская Область						
11761722	472039	fr	Oblast de Voronej						
12132450	472039	fi	Voronežin alue						
13287630	472039	de	Woronesch		1				
8184285	2650345	ru	Ист-Райдинг-оф-Йоркшир						
1978096	6290252	ru	Сербия	1					
1978103	6290252	sr	Србија	1					
1596790	792680	ru	Белград						
1596795	792680	sr	Београд						
```

## File: `geosuggest-core/tests/misc/population-weight.txt`
```
524901	Moscow	Moscow	MOW,Maeskuy,Maskav,Maskava,Maskva,Mat-xco-va,Matxcova,Matxcơva,Mosca,Moscfa,Moscha,Mosco,Moscou,Moscova,Moscovo,Moscow,Moscoƿ,Moscu,Moscua,Moscòu,Moscó,Moscù,Moscú,Moskva,Moska,Moskau,Mosko,Moskokh,Moskou,Moskov,Moskova,Moskovu,Moskow,Moskowa,Mosku,Moskuas,Moskva,Moskvo,Moskwa,Moszkva,Muskav,Musko,Mát-xcơ-va,Mòskwa,Məskeu,Məskəү,masko,maskw,mo si ke,moseukeuba,mosko,mosukuwa,mskw,mwskva,mwskw,mwsqbh,mx s ko,Μόσχα,Мæскуы,Маскав,Масква,Москва,Москова,Москох,Москъва,Мускав,Муско,Мәскеу,Мәскәү,Մոսկվա,מאָסקװע,מאסקווע,מוסקבה,ماسکو,مسکو,موسكو,موسكۋا,ܡܘܣܩܒܐ,मास्को,मॉस्को,মস্কো,மாஸ்கோ,มอสโก,མོ་སི་ཁོ།,მოსკოვი,ሞስኮ,モスクワ,莫斯科,모스크바	55.75222	37.61556	P	PPLC	RU		48				10381222		144	Europe/Moscow	2020-03-31
484912	Taganskiy	Taganskiy	Taganka,Taganskij,Taganskiy,Таганский	55.73333	37.66667	P	PPLX	RU		48				116000		135	Europe/Moscow	2014-01-31
517121	Novyye Kuz’minki	Novyye Kuz'minki	Novye Kuz'minki,Novyye Kuz'minki,Novyye Kuz’minki,Новые Кузьминки	55.7	37.75	P	PPLX	RU		48				143000		141	Europe/Moscow	2013-04-02
532535	Lyublino	Lyublino	Ljublino,Lublino,Lyublino,Lyublino-Dachnoye,Люблино	55.67738	37.76005	P	PPL	RU		48				172000		141	Europe/Moscow	2020-10-29
532615	Lyubertsy	Lyubertsy	Lioubertsy,Liubercai,Liuberti,Liubertsi,Liubertsy,Liuberțî,Liúbertsy,Ljoebertsy,Ljuberci,Ljubercy,Ljubertso,Ljubertsy,Ljubertsõ,Ljuberzy,Luberci,Lubertsi,Lubiercy,Lyubertsi,Lyubertsy,Lyubertsı,liu bie er qi,liubertsi,lyubeleuchi,lywbartsy,lywbrtsy,lywbyrtsy,ryuberutsu~i,Ļuberci,Љуберци,Люберци,Люберцы,Люберці,ليوبارتسي,لیوبرتسی,لیوبیرتسی,ლიუბერცი,リュベルツィ,柳別爾齊,류베르치	55.67719	37.89322	P	PPL	RU		47				154650		139	Europe/Moscow	2019-09-05
```

## File: `geosuggest-demo/Cargo.toml`
```
[package]
name = "geosuggest-demo"
version = "0.4.2"
edition = "2021"

[dependencies]
serde.workspace = true
serde_json.workspace = true

web-sys = "0.3.69"
wasm-bindgen = "0.2.92"
sycamore = { version = "0.8.2", features = ["suspense"]}

reqwasm = "0.5.0" 
serde_qs = "0.8"

console_error_panic_hook = "0.1.7"
console_log = "0.2.2"
log = "0.4.21"
```

## File: `geosuggest-demo/Dockerfile`
```
FROM rust:1.90-slim-bullseye

ARG GEOSUGGEST_BASE_API_URL=$GEOSUGGEST_BASE_API_URL
ARG GEOSUGGEST_RELEASE=$GEOSUGGEST_RELEASE
ARG GEOSUGGEST_INDEX=geosuggest-index.rkyv
ARG CITIES=cities5000

RUN apt-get update \
    && apt-get -y install curl build-essential unzip pkg-config libssl-dev

# geosuggest
RUN cd /root \
    && curl -sL https://github.com/estin/geosuggest/archive/$GEOSUGGEST_RELEASE.zip --output geosuggest-release.zip \
    && unzip geosuggest-release.zip \
    && mv geosuggest-$GEOSUGGEST_RELEASE geosuggest-release \
    && cd geosuggest-release \
    && cargo build --release --features=tokio,cli

# index
RUN cd /tmp \
    && curl -sL http://download.geonames.org/export/dump/$CITIES.zip --output $CITIES.zip \
    && curl -sL http://download.geonames.org/export/dump/alternateNamesV2.zip --output alternateNamesV2.zip \
    && curl -sL http://download.geonames.org/export/dump/admin1CodesASCII.txt --output /tmp/admin1CodesASCII.txt \
    && curl -sL http://download.geonames.org/export/dump/admin2Codes.txt --output /tmp/admin2Codes.txt \
    && curl -sl http://download.geonames.org/export/dump/countryInfo.txt --output /tmp/countryInfo.txt \
    && unzip $CITIES.zip \
    && unzip alternateNamesV2.zip

# fix new Russian regions
RUN sed -ie "s/UA\t\t11/RU\t\t192/p" /tmp/$CITIES.txt
RUN sed -ie "s/UA\t\t20/RU\t\t193/p" /tmp/$CITIES.txt
RUN sed -ie "s/UA\t\t05/RU\t\t194/p" /tmp/$CITIES.txt
RUN sed -ie "s/UA\t\t14/RU\t\t195/p" /tmp/$CITIES.txt
RUN sed -ie "s/UA\t\t08/RU\t\t196/p" /tmp/$CITIES.txt
RUN sed -ie "s/UA\t\t26/RU\t\t197/p" /tmp/$CITIES.txt

RUN ls /tmp
RUN /root/geosuggest-release/target/release/geosuggest-build-index from-files \
    --cities=/tmp/$CITIES.txt \
    --names=/tmp/alternateNamesV2.txt \
    --admin-codes=/tmp/admin1CodesASCII.txt \
    --admin2-codes=/tmp/admin2Codes.txt \
    --countries=/tmp/countryInfo.txt \
    --languages=ru,uk,be,zh,ja \
    --output=/opt/$GEOSUGGEST_INDEX

# demo ui
RUN cargo install wasm-bindgen-cli
RUN cargo install trunk
RUN rustup target add wasm32-unknown-unknown
RUN cd /root/geosuggest-release/geosuggest-demo \
    && trunk build --release -d /root/geosuggest-demo-release

# final stage
FROM debian:bookworm-slim

ARG PORT=$PORT
ARG GEOSUGGEST_INDEX=geosuggest-index.rkyv

COPY --from=0 /root/geosuggest-release/target/release/geosuggest /usr/bin
COPY --from=0 /root/geosuggest-demo-release /opt/geosuggest-static
COPY --from=0 /opt/$GEOSUGGEST_INDEX /opt/$GEOSUGGEST_INDEX

# default configuration
EXPOSE $PORT
ENV GEOSUGGEST_CONFIG_FILE="/opt/geosuggest-settings.toml"
ENV RUST_LOG=geosuggest=trace

RUN echo "host = '0.0.0.0'" >> /opt/geosuggest-settings.toml \
    && echo "port = 8000 # see GEOSUGGEST_PORT" >> /opt/geosuggest-settings.toml \
    && echo "index_file = '/opt/$GEOSUGGEST_INDEX'" >> /opt/geosuggest-settings.toml \
    && echo "static_dir = '/opt/geosuggest-static'" >> /opt/geosuggest-settings.toml \
    && echo "url_path_prefix = '/'" >> /opt/geosuggest-settings.toml

# pass $PORT to $GEOSUGGEST_PORT
ENTRYPOINT []
CMD GEOSUGGEST__PORT=$PORT geosuggest
```

## File: `geosuggest-demo/README.md`
```markdown
## geosuggest demo

This is a demonstrating how to use [geosuggest](https://github.com/estin/geosuggest).

[Live demo](https://geosuggest.etatarkin.ru/)

In Dockerfile:
 - download and compile [geosuggest](https://github.com/estin/geosuggest) backend
 - build index on [geonames free data](http://download.geonames.org/export/dump/)
 - build [sycamore](https://github.com/sycamore-rs/sycamore) based frontend

For local build&start
```bash
$ docker build \
    --build-arg PORT="8000" \
    --build-arg GEOSUGGEST_BASE_API_URL="http://127.0.0.1:8000" \
    --build-arg GEOSUGGEST_RELEASE="master" \
    -t geosuggest-demo .
$ docker run --rm -e PORT=8000 -e RUST_LOG=geosuggest=info -p 8000:8000 -it geosuggest-demo
```
```

## File: `geosuggest-demo/index.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>GEOSUGGEST</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" crossorigin=""/>
    <link data-trunk rel="sass" href="index.scss" />
   <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" crossorigin=""></script>
  </head>
  <body>
  </body>
</html>
```

## File: `geosuggest-demo/index.scss`
```scss
 .rotate-45 {
    --transform-rotate: 45deg;
    transform: rotate(45deg);
}

.group:hover .group-hover\:flex {
    display: flex;
}
```

## File: `geosuggest-demo/src/bindings.rs`
```rust
use wasm_bindgen::prelude::*;

// wasm-bindgen will automatically take care of including this script
#[wasm_bindgen(module = "/src/map.js")]
extern "C" {
    #[wasm_bindgen(js_name = "mapInit")]
    pub fn map_init(callback: &Closure<dyn FnMut(f64, f64)>);

    #[wasm_bindgen(js_name = "mapMove")]
    pub fn map_move(lat: f64, lng: f64);
}
```

## File: `geosuggest-demo/src/main.rs`
```rust
use serde::{Deserialize, Serialize};

use reqwasm::http::Request;
use sycamore::futures::{create_resource, spawn_local_scoped};
use sycamore::prelude::*;
use wasm_bindgen::prelude::*;

mod bindings;

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct CountryItem {
    id: u32,
    code: String,
    name: String,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct AdminDivisionItem {
    id: u32,
    code: String,
    name: String,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct CityResultItem {
    id: u32,
    name: String,
    country: Option<CountryItem>,
    admin_division: Option<AdminDivisionItem>,
    admin2_division: Option<AdminDivisionItem>,
    timezone: String,
    latitude: f64,
    longitude: f64,
    population: f64,
}

impl CityResultItem {
    pub fn get_country(&self) -> &str {
        if let Some(ref country) = self.country {
            &country.code
        } else {
            ""
        }
    }
}

#[derive(Serialize, Deserialize)]
pub struct ReverseItem {
    pub city: CityResultItem,
    pub distance: f64,
    pub score: f64,
}

#[derive(Debug)]
pub struct SelectedCity {
    pub city: Option<CityResultItem>,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct SuggestQuery<'a> {
    pattern: &'a str,
    limit: Option<usize>,
    /// isolanguage code
    lang: Option<&'a str>,
    min_score: Option<f64>,
}

#[derive(Deserialize, Serialize, Debug, Clone)]
pub struct SuggestResult {
    items: Vec<CityResultItem>,
    /// elapsed time in ms
    time: usize,
}

impl SuggestResult {
    fn new() -> Self {
        SuggestResult {
            items: Vec::new(),
            time: 0,
        }
    }
}

#[derive(Debug, Deserialize, Serialize)]
pub struct ReverseQuery<'a> {
    lat: f64,
    lng: f64,
    /// isolanguage code
    lang: Option<&'a str>,
    /// population weight
    k: Option<f64>,
}

#[derive(Deserialize, Serialize)]
pub struct ReverseResult {
    items: Vec<ReverseItem>,
    /// elapsed time in ms
    time: usize,
}

enum RequestError {
    #[allow(dead_code)]
    SerializeRequestError(serde_qs::Error),
    #[allow(dead_code)]
    FetchError(reqwasm::Error),
}

impl From<serde_qs::Error> for RequestError {
    fn from(e: serde_qs::Error) -> Self {
        RequestError::SerializeRequestError(e)
    }
}

impl From<reqwasm::Error> for RequestError {
    fn from(e: reqwasm::Error) -> Self {
        RequestError::FetchError(e)
    }
}

fn get_api_url(method: &str) -> String {
    format!(
        "{}{}",
        option_env!("GEOSUGGEST_BASE_API_URL").unwrap_or("http://127.0.0.1:8090"),
        method
    )
}

async fn fetch_suggest(query: SuggestQuery<'_>) -> Result<SuggestResult, RequestError> {
    if query.pattern.is_empty() {
        return Ok(SuggestResult::new());
    }
    let url = get_api_url(&format!(
        "/api/city/suggest?{}",
        serde_qs::to_string(&query)?,
    ));
    let resp = Request::get(&url).send().await?;

    let body = resp.json::<SuggestResult>().await?;
    Ok(body)
}

async fn fetch_reverse(query: ReverseQuery<'_>) -> Result<ReverseResult, RequestError> {
    let url = get_api_url(&format!(
        "/api/city/reverse?{}",
        serde_qs::to_string(&query).unwrap(),
    ));
    let resp = Request::get(&url).send().await?;

    let body = resp.json::<ReverseResult>().await?;
    Ok(body)
}

#[derive(Prop)]
struct SuggestProps<'a> {
    text: &'a ReadSignal<String>,
    lang: &'a ReadSignal<String>,
    min_score: &'a ReadSignal<String>,
}

#[component]
async fn SuggestItems<'a, G: Html>(cx: Scope<'a>, props: SuggestProps<'a>) -> View<G> {
    let selected_item = use_context::<RcSignal<SelectedCity>>(cx);

    let show_suggest = create_selector(cx, move || {
        let text = props.text.get();
        if let Some(city) = &selected_item.get_untracked().city {
            if city.name == text.as_str() {
                return (false, text);
            }
        }
        (true, text)
    });

    let handle_select = move |item: CityResultItem| {
        bindings::map_move(item.latitude, item.longitude);
        selected_item.set(SelectedCity { city: Some(item) });
    };

    let view = create_memo(cx, move || {
        let (show, text) = &*show_suggest.get();

        if !show {
            return view! {cx, };
        }

        if text.is_empty() {
            return view! {cx, };
        }

        let lang = (*props.lang.get()).clone();
        let min_score = (*props.min_score.get()).clone();

        let pattern = create_ref(cx, text.clone());
        let lang = create_ref(cx, lang);
        let min_score = create_ref(cx, min_score);
        let query = SuggestQuery {
            pattern,
            limit: Some(10),
            lang: Some(lang),
            min_score: min_score.parse::<f64>().ok(),
        };
        let items = create_resource(cx, fetch_suggest(query));

        view! {cx,
            div {
                (
                    {
                        if let Some(data) = items.get().as_ref() {
                            if let Ok(d) = data {
                                let views = View::new_fragment(
                                    d.items.iter().map(|item| {
                                        let country = item.get_country().to_owned();
                                        let name = item.name.to_owned();
                                        let item = item.clone();
                                        view! { cx,
                                            li(on:click=move |_| handle_select(item.clone()),class="px-2 py-3 space-x-2 hover:bg-blue-600 hover:text-white focus:bg-blue-600 focus:text-white focus:outline-none"){
                                                (name) " " (country)
                                            }
                                        }
                                    }).collect()
                                );
                                view! {cx,
                                    aside(role="menu",class="absolute z-10 flex flex-col items-start w-64 bg-white border rounded-md shadow-md mt-1") {
                                        ul(class="flex flex-col w-full") {
                                            (views)
                                        }
                                    }
                                }
                            } else {
                                view! {cx, "Error on fetch"}
                            }
                        } else {
                            view! {cx, "loading..."}
                        }
                    }
                )
            }
        }
    });

    view! {cx, div { ((*view.get()).clone()) }}
}

#[component]
async fn ResultView<G: Html>(cx: Scope<'_>) -> View<G> {
    let selected_item = use_context::<RcSignal<SelectedCity>>(cx);
    view! {cx,
        (match selected_item.get().city {
            Some(ref city) => {
                let pretty = serde_json::to_string_pretty(&city).unwrap_or_else(|e| format!("Error: {}", e));

                view! {cx,
                    div(class="w-full px-2 py-1 pb-4") {
                        p(class="font-semibold"){ "City:" }
                        code {
                            pre { (pretty) }
                        }
                    }
                }
            }
            _ => view! {cx, }
        })
    }
}

#[component]
fn App<G: Html>(cx: Scope) -> View<G> {
    // common settings
    let min_score = create_signal(cx, "0.8".to_string());
    let distance_coefficient = create_signal(cx, "0.000000005".to_string());
    let language = create_signal(cx, String::new());

    let suggest_input = create_signal(cx, String::new());
    let reverse_lat = create_signal(cx, String::new());
    let reverse_lng = create_signal(cx, String::new());

    // result city
    let selected_item = create_rc_signal(SelectedCity { city: None });
    let selected_item_clone = selected_item.clone();
    let selected_item_clone2 = selected_item.clone();
    provide_context(cx, selected_item);

    // sync input and selected item
    create_effect(cx, move || {
        let selected = selected_item_clone2.get();
        if let Some(city) = &selected.city {
            suggest_input.set(city.name.clone());
        }
    });

    let do_reverse = Box::new(move || {
        let lat = (*reverse_lat.get_untracked()).clone();
        let lng = (*reverse_lng.get_untracked()).clone();

        if lat.is_empty() || lng.is_empty() {
            return;
        }

        let lang = (*language.get_untracked()).clone();

        let lat = lat.parse::<f64>();
        let lng = lng.parse::<f64>();

        let selected_item_clone = selected_item_clone.clone();
        spawn_local_scoped(cx, async move {
            match (lat, lng) {
                (Ok(lat), Ok(lng)) => {
                    let query = ReverseQuery {
                        lat,
                        lng,
                        lang: Some(&lang),
                        k: None,
                    };
                    if let Ok(result) = fetch_reverse(query).await {
                        if let Some(item) = result.items.first() {
                            selected_item_clone.set(SelectedCity {
                                city: Some(item.city.clone()),
                            });
                        } else {
                            selected_item_clone.set(SelectedCity { city: None });
                        }
                    }
                }
                _ => {
                    log::error!("Invalid lat/lng values");
                }
            };
        });
    });

    // signal to accept coordinates from map events
    let map_click_signal = create_rc_signal((String::new(), String::new()));

    // on map double click set new coordinates
    let map_click_signal_clone = map_click_signal.clone();
    let map_dblclick_closure = Closure::wrap(Box::new(move |lat: f64, lng: f64| {
        log::info!("Map double-click on lat: {} lng: {}", lat, lng);
        map_click_signal_clone.set((lat.to_string(), lng.to_string()));
    }) as Box<dyn FnMut(f64, f64)>);

    // and pass coordinates to manual inputs
    let do_reverse_clone = do_reverse.clone();
    create_effect(cx, move || {
        let c = map_click_signal.get();
        reverse_lat.set(c.0.to_owned());
        reverse_lng.set(c.1.to_owned());
        do_reverse_clone();
    });

    // initialize map
    spawn_local_scoped(cx, async move {
        bindings::map_init(&map_dblclick_closure);
        map_dblclick_closure.forget();
    });

    let handle_reverse = move |_| {
        do_reverse();
    };

    view! { cx,
        div(id="app") {
            div(class="flex h-screen font-sans text-gray-900 bg-gray-300 border-box") {
                div(class="flex flex-row w-full max-w lg:w-1/2 xl:w-1/4 justify-center align-top mb-auto mx-4") {
                    div(class="flex flex-col items-start justify-between h-auto my-4 overflow-hidden bg-white rounded-lg shadow-xl") {
                        div(class="flex flex-row items-baseline justify-around w-full p-1 pt-4 pb-0 mb-0") {
                            h2(class="mr-auto text-lg font-semibold tracking-wide") { "Settings" }
                        }
                        div(class="w-full p-1 pt-0 text-gray-800 bg-gray-100 divide-y divide-gray-400") {
                            div(class="flex flex-col items-center justify-between py-1") {
                                div(class="w-full mt-1") {
                                    label(class="block text-gray-700 text-sm font-bold mb-2",for="min_score") {
                                        "Suggest: Jaro Winkler min score"
                                    }
                                    div(class="mt-1 rounded-md shadow-sm") {
                                        input(bind:value=min_score, id="min_score",type="number",min="0", max="1", class="w-full px-3 py-2 border border-gray-400 rounded-lg outline-none focus:shadow-outline")
                                    }
                                }
                                div(class="w-full mt-1") {
                                    label(class="block text-gray-700 text-sm font-bold mb-2",for="distance_coefficient") {
                                        "Reverse: Distance correction coefficient by population"
                                    }
                                    div(class="mt-1 rounded-md shadow-sm") {
                                        input(bind:value=distance_coefficient, id="distance_coefficient", type="number", class="w-full px-3 py-2 border border-gray-400 rounded-lg outline-none focus:shadow-outline")
                                    }
                                }
                            }
                        }
                        div(class="flex flex-row items-baseline justify-around w-full p-1 pt-4 pb-0 mb-0") {
                            h2(class="mr-auto text-lg font-semibold tracking-wide"){ "1. Suggest" }
                        }
                        div(class="w-full p-1 pt-0 text-gray-800 bg-gray-100 divide-y divide-gray-400") {
                            div(class="flex flex-row items-center justify-between py-1") {
                                div(class="w-full") {
                                    div(class="flex") {
                                        div(class="w-5/6") {
                                            div(class="mt-1 flex rounded-md shadow-sm") {
                                                input(bind:value=suggest_input,type="text",placeholder="Please write a city name",class="w-full px-3 py-2 border border-gray-400 rounded-lg outline-none focus:shadow-outline")
                                            }
                                        }
                                        div(class="ml-1 mt-1 w-1/6 flex rounded-md shadow-sm") {
                                            select(bind:value=language, class="bg-white w-full px-3 py-2 border border-gray-400 rounded-lg outline-none focus:shadow-outline") {
                                                option(value="en"){"en"}
                                                option(value="ru"){"ru"}
                                                option(value="uk"){"uk"}
                                                option(value="be"){"be"}
                                                option(value="zh"){"zh"}
                                                option(value="ja"){"ja"}
                                          }
                                        }
                                    }
                                    SuggestItems(
                                        text=suggest_input,
                                        lang=language,
                                        min_score=min_score,
                                    )
                                }
                            }
                        }
                        div(class="flex flex-row items-baseline justify-around w-full p-1 pb-0 mb-0") {
                            h2(class="mr-auto text-lg font-semibold tracking-wide"){"2. Reverse (dbl-click on map)"}
                        }
                        div(class="w-full p-1 pt-0 text-gray-800 bg-gray-100 divide-y divide-gray-400") {
                            div(class="flex flex-row items-center justify-between py-1") {
                                div(class="mt-1 w-1/2 pr-1 flex rounded-md shadow-sm") {
                                    // input(on:input=move |event: Event| handle_input("lat", event), value=reverse_lat, placeholder="Latitude", class="w-full px-3 py-1 border border-gray-400 rounded-lg outline-none focus:shadow-outline", type="text")
                                    input(bind:value=reverse_lat, placeholder="Latitude", class="w-full px-3 py-1 border border-gray-400 rounded-lg outline-none focus:shadow-outline", type="text")
                                }
                                div(class="mt-1 w-1/2 flex rounded-md shadow-sm") {
                                    input(bind:value=reverse_lng, placeholder="Longitude", class="w-full px-3 py-1 border border-gray-400 rounded-lg outline-none focus:shadow-outline", type="text")
                                }
                                div(class="mt-1 w-1/3 flex rounded-md shadow-sm") {
                                    button(on:click=handle_reverse, class="w-full ml-1 px-3 py-1 border border-gray-400 rounded-lg outline-none"){"Find"}
                                }
                            }
                        }

                        ResultView { }

                        div(class="flex w-full p-1 mb-1") {
                            h4(class="font-semibold"){"API: "}
                            a(class="mx-1 text-blue-500",href="./swagger"){"Swagger"}
                            " / "
                            a(class="mx-1 text-blue-500",href="./redoc"){"ReDoc"}
                        }
                        div(class="flex w-full p-1 mb-1") {
                            h4(class="font-semibold"){"Github: "}
                            a(class="mx-1 text-blue-500",href="https://github.com/estin/geosuggest"){"geosuggest"}
                        }
                    }
                }
                div(id="map",class="flex-row hidden lg:block lg:w-1/2 xl:w-3/4") {}
            }
        }
    }
}

fn main() {
    console_error_panic_hook::set_once();
    console_log::init_with_level(log::Level::Debug).unwrap();

    sycamore::render(|cx| {
        view! {cx,
           App {}
        }
    });
}
```

## File: `geosuggest-demo/src/map.js`
```javascript
export function mapInit(callback) {
    window.map = L.map('map').setView([51.67204, 39.1843], 13);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiZXRhdGFya2luIiwiYSI6ImNrNXh3aTN2ZTA1OXgza3AzM3J3dW52bDgifQ.LyoBwR8ixePf-5erIXhKRg'
    }).addTo(window.map);
    window.map.doubleClickZoom.disable();
    
    window.setMarker = function (lat, lng) {
      if (window.marker) {
          window.map.removeLayer(window.marker);
      }
      window.marker = new L.CircleMarker([lat, lng], 10).addTo(window.map);
    };

    // event handler
    window.map.on('dblclick', function(event) {
        window.setMarker(event.latlng.lat, event.latlng.lng);
        callback(event.latlng.lat, event.latlng.lng);
    });
};

export function mapMove(lat, lng) {
    if (window.map) {
        window.setMarker(lat, lng);
        window.map.setView([lat, lng], 11, { animation: true });
    }
};
```

## File: `geosuggest-examples/Cargo.toml`
```
[package]
name = "geosuggest-examples"
version = "0.1.0"
edition = "2021"
publish = false

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
[[bin]]
name = "simple"
path = "src/simple.rs"

[dependencies]
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter", "fmt"] }
tokio = { version = "1", features = ["macros", "net", "rt-multi-thread"] }

geosuggest-core = { path = "../geosuggest-core", version = "0.8", features=[ "tracing" ] }
geosuggest-utils = { path = "../geosuggest-utils", version = "0.8", features=[ "tracing" ] }
```

## File: `geosuggest-examples/src/simple.rs`
```rust
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

use geosuggest_core::{storage, EngineData};
use geosuggest_utils::{IndexUpdater, IndexUpdaterSettings};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // logging
    let subscriber = tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::new(
            std::env::var("RUST_LOG").unwrap_or_else(|_| "info".into()),
        ))
        .with(tracing_subscriber::fmt::layer());
    subscriber.init();

    // build/load/update index
    let engine_data = load_engine_data().await?;
    tracing::info!("Index metadata: {:#?}", engine_data.metadata);

    // use
    let engine = engine_data.as_engine()?;
    tracing::info!(
        "Suggest result: {:#?}",
        engine.suggest::<&str>("Beverley", 1, None, Some(&["US"]))
    );
    tracing::info!(
        "Reverse result: {:#?}",
        engine.reverse::<&str>((11.138298, 57.510973), 1, None, None)
    );
    tracing::info!("Country info: {:#?}", engine.country_info("RS"));
    tracing::info!("Capital info: {:#?}", engine.capital("GB"));

    Ok(())
}

async fn load_engine_data() -> Result<EngineData, Box<dyn std::error::Error>> {
    let index_file = std::path::Path::new("/tmp/geosuggest-index.rkyv");

    let storage = storage::Storage::new();

    let updater = IndexUpdater::new(IndexUpdaterSettings {
        filter_languages: vec!["ru", "ar"],
        ..Default::default()
    })?;

    Ok(if index_file.exists() {
        // load existed index
        let metadata = storage
            .read_metadata(index_file)
            .map_err(|e| format!("On load index metadata from {index_file:?}: {e}"))?;

        // check updates
        let mut engine = match &metadata {
            Some(m) if updater.has_updates(m).await? => {
                let engine_data = updater.build().await?;
                storage
                    .dump_to(index_file, &engine_data)
                    .map_err(|e| format!("Failed dump to {index_file:?}: {e}"))?;
                engine_data
            }
            _ => storage
                .load_from(index_file)
                .map_err(|e| format!("On load index from {index_file:?}: {e}"))?,
        };

        // attach metadata
        engine.metadata = metadata;
        engine
    } else {
        // initial
        let engine_data = updater.build().await?;
        storage
            .dump_to(index_file, &engine_data)
            .map_err(|e| format!("Failed dump to {index_file:?}: {e}"))?;
        engine_data
    })
}
```

## File: `geosuggest-utils/Cargo.toml`
```
[package]
name = "geosuggest-utils"
version.workspace = true
authors.workspace = true
description = "Geosuggest index update utilities"
readme = "README.md"
keywords = ["geocoding", "service"]
repository = "https://github.com/estin/geosuggest.git"
documentation = "https://docs.rs/geosuggest-utils/"
categories = ["web-programming::http-server",
              "development-tools"]
license = "MIT"
edition = "2021"

[features]
default = []
cli = ["clap"]
tracing = ["dep:tracing", "dep:tracing-subscriber", "geosuggest-core/tracing"]

[lib]
path = "src/lib.rs"

[[bin]]
name = "geosuggest-build-index"
path = "src/build-index.rs"
required-features = ["clap"]

[dependencies]
tracing = { workspace = true, optional = true }
tracing-subscriber = { workspace = true, optional = true } 
anyhow.workspace = true
zip.workspace = true
reqwest.workspace = true
serde.workspace = true
tokio.workspace = true
futures.workspace = true
clap = { workspace = true, optional = true }
rkyv.workspace = true

geosuggest-core = { path = "../geosuggest-core", version = "0.8" }
```

## File: `geosuggest-utils/README.md`
```markdown
<div align="center">
  <p><h1>geosuggest-utils</h1></p>
  <p><strong></strong></p>
  <p></p>
</div>

[HTTP service](https://github.com/estin/geosuggest)

[Examples](https://github.com/estin/geosuggest/tree/master/examples/src)

Usage example
```rust
use tokio;
use geosuggest_utils::{IndexUpdater, IndexUpdaterSettings};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Build index...");
    let updater = IndexUpdater::new(IndexUpdaterSettings {
        names: None, // no multilang support
        ..Default::default()
    })?;

    let engine_data = updater.build().await?;

    let engine = engine_data.as_engine()?;

    println!(
        "Suggest result: {:#?}",
        engine.suggest::<&str>("Beverley", 1, None, Some(&["US"]))
    );
    println!(
        "Reverse result: {:#?}",
        engine.reverse::<&str>((11.138298, 57.510973), 1, None, None)
    );

    Ok(())
}
```
```

## File: `geosuggest-utils/src/build-index.rs`
```rust
use anyhow::Result;
#[cfg(feature = "tracing")]
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

use geosuggest_core::{
    index::{IndexData, SourceFileOptions},
    storage, EngineData,
};
use geosuggest_utils::{IndexUpdater, IndexUpdaterSettings, SourceItem};

use clap::Parser;

/// Build index from files or urls
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
enum Args {
    FromUrls(Urls),
    FromFiles(Files),
}

/// Build index from files
#[derive(clap::Args, Debug)]
#[command(version, about)]
struct Files {
    /// Cities file
    #[arg(long)]
    cities: String,

    /// Countries file
    #[arg(long)]
    countries: Option<String>,

    /// Names file
    #[arg(long)]
    names: Option<String>,

    /// Admin codes file
    #[arg(long)]
    admin_codes: Option<String>,

    /// Admin2 codes file
    #[arg(long)]
    admin2_codes: Option<String>,

    /// Languages
    #[arg(long)]
    languages: Option<String>,

    /// Dump index to file
    #[arg(long)]
    output: String,
}

/// Build index from urls
#[derive(clap::Args, Debug)]
#[command(version, about)]
struct Urls {
    /// Cities url
    #[arg(long)]
    cities_url: Option<String>,

    /// Citeis filename in archive
    #[arg(long)]
    cities_filename: Option<String>,

    /// Names url
    #[arg(long)]
    names_url: Option<String>,

    /// Names filename in archive
    #[arg(long)]
    names_filename: Option<String>,

    /// Countries url
    #[arg(long)]
    countries_url: Option<String>,

    /// Admin codes url
    #[arg(long)]
    admin_codes_url: Option<String>,

    /// Admin2 codes url
    #[arg(long)]
    admin2_codes_url: Option<String>,

    /// Languages
    #[arg(long)]
    languages: Option<String>,

    /// Dump index to file
    #[arg(long)]
    output: String,
}

#[tokio::main]
async fn main() -> Result<()> {
    // logging
    #[cfg(feature = "tracing")]
    {
        let subscriber = tracing_subscriber::registry()
            .with(tracing_subscriber::EnvFilter::new(
                std::env::var("RUST_LOG").unwrap_or_else(|_| "info".into()),
            ))
            .with(tracing_subscriber::fmt::layer());
        subscriber.init();
    }

    match Args::parse() {
        Args::FromUrls(args) => {
            let mut settings = IndexUpdaterSettings::default();

            if let Some(url) = &args.cities_url {
                settings.cities = SourceItem {
                    url,
                    filename: args.cities_filename.as_ref().ok_or_else(|| {
                        anyhow::anyhow!("Cities filename required to extract from archive")
                    })?,
                };
            }

            if let Some(url) = &args.names_url {
                settings.names = Some(SourceItem {
                    url,
                    filename: args.names_filename.as_ref().ok_or_else(|| {
                        anyhow::anyhow!("Names filename required to extract from archive")
                    })?,
                });
            }

            if args.countries_url.is_some() {
                settings.countries_url = args.countries_url.as_deref();
            }

            if args.admin_codes_url.is_some() {
                settings.admin1_codes_url = args.admin_codes_url.as_deref();
            }

            if let Some(languages) = &args.languages {
                settings.filter_languages = languages.split(',').map(AsRef::as_ref).collect();
            }

            let engine = IndexUpdater::new(settings)?
                .build()
                .await
                .expect("On build index");

            storage::Storage::new()
                .dump_to(&args.output, &engine)
                .map_err(|e| anyhow::anyhow!("Failed to dump index: {e}"))?;
        }

        Args::FromFiles(args) => {
            let index_data = IndexData::new_from_files(SourceFileOptions {
                cities: args.cities,
                names: args.names,
                countries: args.countries,
                admin1_codes: args.admin_codes,
                admin2_codes: args.admin2_codes,
                filter_languages: if let Some(languages) = &args.languages {
                    languages.split(',').map(AsRef::as_ref).collect()
                } else {
                    Vec::new()
                },
            })
            .map_err(|e| anyhow::anyhow!("Failed to build index: {e}"))?;

            let engine_data = EngineData::try_from(index_data)?;

            storage::Storage::new()
                .dump_to(&args.output, &engine_data)
                .map_err(|e| anyhow::anyhow!("Failed to dump index: {e}"))?;
        }
    };

    Ok(())
}
```

## File: `geosuggest-utils/src/lib.rs`
```rust
#![doc = include_str!("../README.md")]
use anyhow::Result;
use geosuggest_core::EngineData;
use std::collections::HashMap;
use std::io::{Cursor, Read};

#[cfg(feature = "tracing")]
use std::time::Instant;

use geosuggest_core::{
    index::{IndexData, SourceFileContentOptions},
    EngineMetadata, EngineSourceMetadata,
};
use serde::Serialize;

#[derive(Serialize, Clone)]
pub struct SourceItem<'a> {
    pub url: &'a str,
    pub filename: &'a str,
}

#[derive(Serialize, Clone)]
pub struct IndexUpdaterSettings<'a> {
    pub http_timeout_ms: u64,
    pub cities: SourceItem<'a>,
    pub names: Option<SourceItem<'a>>,
    pub countries_url: Option<&'a str>,
    pub admin1_codes_url: Option<&'a str>,
    pub admin2_codes_url: Option<&'a str>,
    pub filter_languages: Vec<&'a str>,
}

impl Default for IndexUpdaterSettings<'_> {
    fn default() -> Self {
        IndexUpdaterSettings {
            http_timeout_ms: 300_000,
            cities: SourceItem {
                url: "https://download.geonames.org/export/dump/cities5000.zip",
                filename: "cities5000.txt",
            },
            names: Some(SourceItem {
                url: "https://download.geonames.org/export/dump/alternateNamesV2.zip",
                filename: "alternateNamesV2.txt",
            }),
            countries_url: Some("https://download.geonames.org/export/dump/countryInfo.txt"),
            admin1_codes_url: Some(
                "https://download.geonames.org/export/dump/admin1CodesASCII.txt",
            ),
            admin2_codes_url: Some("https://download.geonames.org/export/dump/admin2Codes.txt"),
            filter_languages: Vec::new(),
            // max_payload_size: 200 * 1024 * 1024,
        }
    }
}

pub struct IndexUpdater<'a> {
    http_client: reqwest::Client,
    settings: IndexUpdaterSettings<'a>,
}

impl<'a> IndexUpdater<'a> {
    pub fn new(settings: IndexUpdaterSettings<'a>) -> Result<Self> {
        Ok(IndexUpdater {
            http_client: reqwest::ClientBuilder::new()
                .timeout(std::time::Duration::from_millis(settings.http_timeout_ms))
                .build()?,
            settings,
        })
    }

    pub async fn has_updates(&self, metadata: &EngineMetadata) -> Result<bool> {
        #[cfg(feature = "tracing")]
        tracing::info!("Check updates");
        if metadata.source.etag.is_empty() {
            #[cfg(feature = "tracing")]
            tracing::info!("Engine hasn't source ETAGs");
            return Ok(true);
        }

        let mut requests = vec![self.get_etag(self.settings.cities.url)];
        let mut results = vec!["cities"];
        if let Some(item) = &self.settings.names {
            requests.push(self.get_etag(item.url));
            results.push("names");
        }
        if let Some(url) = self.settings.countries_url {
            requests.push(self.get_etag(url));
            results.push("countries");
        }
        if let Some(url) = self.settings.admin1_codes_url {
            requests.push(self.get_etag(url));
            results.push("admin1_codes");
        }
        let responses = futures::future::join_all(requests).await;
        let results: HashMap<_, _> = results.into_iter().zip(responses.into_iter()).collect();

        for (entry, etag) in results {
            let current_etag = metadata
                .source
                .etag
                .get(entry)
                .map(AsRef::as_ref)
                .unwrap_or("");
            let new_etag = etag?;
            if current_etag != new_etag {
                #[cfg(feature = "tracing")]
                tracing::info!("New version of {entry}");
                return Ok(true);
            }
        }

        Ok(false)
    }

    pub async fn get_etag(&self, url: &str) -> Result<String> {
        let response = self.http_client.head(url).send().await?;
        #[cfg(feature = "tracing")]
        tracing::info!("Try HEAD {url}");

        Ok(response
            .headers()
            .get(reqwest::header::ETAG)
            .and_then(|v| v.to_str().ok())
            .map(String::from)
            .unwrap_or_default())
    }

    pub async fn fetch(&self, url: &str, filename: Option<&str>) -> Result<(String, Vec<u8>)> {
        let response = self.http_client.get(url).send().await?;
        #[cfg(feature = "tracing")]
        tracing::info!("Try GET {url}");

        if !response.status().is_success() {
            anyhow::bail!("GET {url} return status {}", response.status())
        }

        let etag = response
            .headers()
            .get(reqwest::header::ETAG)
            .and_then(|v| v.to_str().ok())
            .map(String::from)
            .unwrap_or_default();

        let content = response.bytes().await?.to_vec();
        #[cfg(feature = "tracing")]
        tracing::info!("Downloaded {url} size: {}", content.len());

        let content = if let Some(filename) = filename {
            #[cfg(feature = "tracing")]
            tracing::info!("Unzip {filename}");
            let cursor = Cursor::new(content);
            let mut archive = zip::read::ZipArchive::new(cursor)?;
            let mut file = archive
                .by_name(filename)
                .map_err(|e| anyhow::anyhow!("On get file {filename} from archive: {e}"))?;
            let mut buf = Vec::new();
            file.read_to_end(&mut buf)?;
            buf
        } else {
            content
        };

        Ok((etag, content))
    }

    pub async fn build(self) -> Result<EngineData> {
        let mut requests = vec![self.fetch(
            self.settings.cities.url,
            Some(self.settings.cities.filename),
        )];
        let mut results = vec!["cities"];
        if let Some(item) = &self.settings.names {
            requests.push(self.fetch(item.url, Some(item.filename)));
            results.push("names");
        }
        if let Some(url) = self.settings.countries_url {
            requests.push(self.fetch(url, None));
            results.push("countries");
        }
        if let Some(url) = self.settings.admin1_codes_url {
            requests.push(self.fetch(url, None));
            results.push("admin1_codes");
        }
        if let Some(url) = self.settings.admin2_codes_url {
            requests.push(self.fetch(url, None));
            results.push("admin2_codes");
        }
        let responses = futures::future::join_all(requests).await;
        let mut results: HashMap<_, _> = results.into_iter().zip(responses.into_iter()).collect();

        let etag = results
            .iter()
            .filter_map(|(k, v)| {
                let Ok((etag, _)) = v else { return None };
                Some(((*k).to_string(), etag.to_string()))
            })
            .collect();

        #[cfg(feature = "tracing")]
        tracing::info!("Try to build index...");

        #[cfg(feature = "tracing")]
        let now = Instant::now();

        let data = IndexData::new_from_files_content(SourceFileContentOptions {
            cities: String::from_utf8(
                results
                    .remove(&"cities")
                    .ok_or_else(|| anyhow::anyhow!("Cities file required"))?
                    .map_err(|e| anyhow::anyhow!("On fetch cities file: {e}"))?
                    .1, // .ok_or_else(|| anyhow::anyhow!("Cities file required"))?,
            )?,
            names: if let Some(c) = results.remove(&"names") {
                Some(String::from_utf8(c?.1)?)
            } else {
                None
            },
            countries: if let Some(c) = results.remove(&"countries") {
                Some(String::from_utf8(c?.1)?)
            } else {
                None
            },
            admin1_codes: if let Some(c) = results.remove(&"admin1_codes") {
                Some(String::from_utf8(c?.1)?)
            } else {
                None
            },
            admin2_codes: if let Some(c) = results.remove(&"admin2_codes") {
                Some(String::from_utf8(c?.1)?)
            } else {
                None
            },
            filter_languages: self.settings.filter_languages.clone(),
        })
        .map_err(|e| anyhow::anyhow!("Failed to build index: {e}"))?;

        let mut engine_data = EngineData::try_from(data)?;

        engine_data.metadata = Some(EngineMetadata {
            source: EngineSourceMetadata {
                cities: self.settings.cities.url.to_owned(),
                names: self.settings.names.as_ref().map(|v| v.url.to_owned()),
                countries: self.settings.countries_url.map(String::from),
                admin1_codes: self.settings.admin1_codes_url.map(String::from),
                admin2_codes: self.settings.admin2_codes_url.map(String::from),
                filter_languages: self
                    .settings
                    .filter_languages
                    .into_iter()
                    .map(String::from)
                    .collect::<Vec<_>>(),
                etag,
            },
            ..Default::default()
        });

        #[cfg(feature = "tracing")]
        tracing::info!("Engine data ready. took {}ms", now.elapsed().as_millis());

        Ok(engine_data)
    }
}
```

