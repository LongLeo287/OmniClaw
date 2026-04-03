---
id: github.com-voidcosmos-npkill-13967b39-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:40.574129
---

# KNOWLEDGE EXTRACT: github.com_voidcosmos_npkill_13967b39
> **Extracted on:** 2026-04-01 07:36:05
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519071/github.com_voidcosmos_npkill_13967b39

---

## File: `.gitignore`
```
node_modules
lib
out.txt
# stryker temp files
.stryker-tmp
stryker.log
reports
coverage
stuff
test-files
docs/private
.npkillrc
```

## File: `.node-version`
```
20.12.0
```

## File: `.npmignore`
```
src
tsconfig.json
tslint.json
.prettierrc
```

## File: `.prettierrc`
```
{
  "trailingComma": "all",
  "tabWidth": 2,
  "semi": true,
  "singleQuote": true
}
```

## File: `API.md`
```markdown
# NPKill API

This document does not include all project documentation at this stage. It brings together the basic concepts.
For more details see the project interfaces.

- [NPKill API](#npkill-api)
  - [Interface: `Npkill`](#interface-npkill)
    - [`startScan$(rootPath, options?)`](#startscanrootpath-options)
    - [`stopScan()`](#stopscan)
    - [`getSize$(path, options?)`](#getsizepath-options)
    - [`getNewestFile$(path)`](#getnewestfilepath)
    - [`delete$(path, options?)`](#deletepath-options)
    - [`getLogs$()`](#getlogs)
    - [`isValidRootFolder(path)`](#isvalidrootfolderpath)
    - [`getVersion()`](#getversion)
  - [Interfaces & Types](#interfaces-types)
    - [`ScanOptions`](#scanoptions)
    - [`ScanFoundFolder`](#scanfoundfolder)
    - [`RiskAnalysis`](#riskanalysis)
    - [`GetSizeOptions`](#getsizeoptions)
    - [`GetSizeResult`](#getsizeresult)
    - [`GetNewestFileResult`](#getnewestfileresult)
    - [`DeleteOptions`](#deleteoptions)
  - [Usage Example](#usage-example)

---

## Interface: `Npkill`

The core of the system is the `NpkillInterface`. It offers methods to:

- Scan folders recursively.
- Get metadata about folders (size, last modified).
- Perform safe deletions.
- Stream logs and validate folders.

### `startScan$(rootPath, options?)`

Starts a recursive scan from a given root folder.

- **Parameters**:
  - `rootPath`: `string` — Folder to start scanning from.
  - `options`: [`ScanOptions`](#scanoptions) — Optional scan configuration.

- **Returns**: `Observable<ScanFoundFolder>`
- **Description**: Emits each matching folder as it's found.

---

### `stopScan()`

Stops any ongoing scan and releases resources.

---

### `getSize$(path, options?)`

Returns the total size of a directory.

- **Parameters**:
  - `path`: `string` — Path to folder.
  - `options`: [`GetSizeOptions`](#getsizeoptions)

- **Returns**: `Observable<GetSizeResult>`

---

### `getNewestFile$(path)`

Gets the most recently modified file inside a directory (recursively).

- **Parameters**:
  - `path`: `string`

- **Returns**: `Observable<GetNewestFileResult | null>`

---

### `delete$(path, options?)`

Deletes a folder, optionally as a dry-run. Only allowed if the folder is within the `target` of the initial scan.

- **Parameters**:
  - `path`: `string`
  - `options`: [`DeleteOptions`](#deleteoptions)

- **Returns**: `Observable<DeleteResult>`
- **Throws**: If the path is outside the original target.

---

### `getLogs$()`

Streams internal log entries.

- **Returns**: `Observable<LogEntry[]>`

---

### `isValidRootFolder(path)`

Validates whether a folder is suitable for scanning.

- **Parameters**:
  - `path`: `string`

- **Returns**: [`IsValidRootFolderResult`](#isvalidrootfolderresult)

---

### `getVersion()`

Returns the current version of npkill from `package.json`.

- **Returns**: `string`

---

## Interfaces & Types

---

### `ScanOptions`

```ts
interface ScanOptions {
  targets: string[];
  exclude?: string[];
  sortBy?: 'path' | 'size' | 'age';
  performRiskAnalysis?: boolean; // Default: true
}
```

---

### `ScanFoundFolder`

```ts
interface ScanFoundFolder {
  path: string;
  riskAnalysis?: RiskAnalysis;
}
```

---

### `RiskAnalysis`

Determines whether a result is safe to delete. That is, if it is likely to belong to some application and deleting it could break it.

```ts
interface RiskAnalysis {
  isSensitive: boolean;
  reason?: string;
}
```

---

### `GetSizeOptions`

```ts
interface GetSizeOptions {
  unit?: 'bytes'; // Default: 'bytes'
}
```

---

### `GetSizeResult`

```ts
interface GetSizeResult {
  size: number;
  unit: 'bytes';
}
```

---

### `GetNewestFileResult`

```ts
interface GetNewestFileResult {
  path: string;
  name: string;
  timestamp: number;
}
```

---

### `DeleteOptions`

```ts
interface DeleteOptions {
  dryRun?: boolean;
}
```

---

## Usage Example

This is a minimal example where:

1. it will start a search for `.nx` folders.
2. Get the most recent file
3. Get the total size of the directory

```ts
import { Npkill } from 'npkill';
import { mergeMap, filter, map } from 'rxjs';

const npkill = new Npkill();

let files: {
  path: string;
  size: number;
  newestFile: string;
}[] = [];

npkill
  .startScan$('/home/user/projects/', { target: '.nx' })
  .pipe(
    // Step 1: For each scan result, get the newest file
    mergeMap((scanResult) =>
      npkill.getNewestFile$(scanResult.path).pipe(
        // Step 2: If no newest file, skip this result
        filter((newestFile) => newestFile !== null),
        // Step 3: Combine scanResult and newestFile
        map((newestFile) => ({
          path: scanResult.path,
          newestFile: newestFile.path,
        })),
      ),
    ),
    // Step 4: For each result, get the folder size
    mergeMap((result) =>
      npkill.getSize$(result.path).pipe(
        map(({ size }) => ({
          ...result,
          size,
        })),
      ),
    ),
  )
  .subscribe({
    next: (result) => {
      files.push(result);
    },
    complete: () => {
      console.log('✅ Scan complete. Found folders:', files.length);
      console.table(files);
      console.log(JSON.stringify(files));
    },
  });
```

Output:

```bash
✅ Scan complete. Found folders: 3
┌─────────┬───────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────┬─────────┐
│ (index) │ path                                      │ newestFile                                                               │ size    │
├─────────┼───────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────┼─────────┤
│ 0       │ '/home/user/projects/hello-world/.nx'     │ '/home/user/projects/hello-world/.nx/cache/18.3.4-nx.linux-x64-gnu.node' │ 9388032 │
│ 1       │ '/home/user/projects/another-project/.nx' │ '/home/user/projects/another-project/.nx/workspace-data/d/daemon.log'    │ 3182592 │
│ 2       │ '/home/user/projects/ARCHIVED/demo/.nx'   │ '/home/user/projects/ARCHIVED/demo/.nx/cache/d/daemon.log'               │ 2375680 │
└─────────┴───────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────┴─────────┘
[
  {
    "path": "/home/user/projects/hello-world/.nx",
    "newestFile": "/home/user/projects/hello-world/.nx/cache/18.3.4-nx.linux-x64-gnu.node",
    "size": 9388032
  },
  {
    "path": "/home/user/projects/another-project/.nx",
    "newestFile": "/home/user/projects/another-project/.nx/workspace-data/d/daemon.log",
    "size": 3182592
  },
  ........
]
```
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Estefanía García Gallardo and Juan Torres Gómez

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

## File: `README.es.md`
```markdown
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Encuentra y **destruye** directorios <font color="red">**node_modules**</font> viejos y pesados :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Esta herramienta te permite listar cualquier directorio _node_modules_ que haya en tu sistema, además del espacio que ocupa. Entonces puedes seleccionar los que quieras borrar para liberar espacio. ¡Yay!

## i18n

Nos estamos esforzando por internacionalizar la documentación de Npkill. Aquí tienes una lista de las traducciones disponibles:

- [Español](./README.es.md)
- [Português](../../../core/security/QUARANTINE/vetted/repos/goclaw/readmes/README.pt.md)

## Table of Contents

- [Características](#features)
- [Instalación](#installation)
- [Uso](#usage)
  - [Opciones](#options)
  - [Ejemplos](#examples)
- [Configuración local](#setup-locally)
- [Roadmap](#roadmap)
- [Bugs conocidos](#known-bugs)
- [Cómo contribuir](#contributing)
- [Invítanos a un café](#donations)
- [Licencia](#license)

<a name="features"></a>

# :heavy_check_mark: Características

- **Libera espacio:** Elimina tus directorios _node_modules_ viejos y polvorientos que le roban espacio a tu máquina.

- **Último uso del Workspace**: Comprueba cuándo ha sido la última vez que has modificado un fichero en el workspace (indicado en la columna **last_mod**).

- **Rapidez:** NPKILL está escrito en TypeScript, pero las búsquedas se llevan a cabo a bajo nivel, lo que supone una mejora considerable del rendimiento.

- **Fácil de utilizar:** Despídete de comandos largos y difíciles. Utilizar Npkill es tan sencillo como leer la lista de tus node_modules, y pulsar la tecla Del para eliminarlos. ¿Podría ser más fácil? ;)

- **Minificado:** Apenas tiene dependencias.

<a name="installation"></a>

# :cloud: Instalación

¡Lo mejor es que no tienes que instalar Npkill para utilizarlo!
Simplemente utiliza el siguiente comando:

```bash
$ npx npkill
```

O, si por alguna razón te apetece instalarlo:

```bash
$ npm i -g npkill
# Los usuarios de Unix quizá tengan que ejecutar el comando con sudo. Ve con cuidado
```

> NPKILL no tiene soporte para node<v14. Si esto te afecta puedes utilizar `npkill@0.8.3`

<a name="usage"></a>

# :clipboard: Uso

```bash
$ npx npkill
# o solo npkill si está instalado de forma global
```

Por defecto, Npkill comenzará la búsqueda de node_modules comenzando en la ruta donde se ejecute el comando `npkill`.

Muévete por los distintos directorios listados con <kbd>↓</kbd> <kbd>↑</kbd>, y utiliza <kbd>Space</kbd> para borrar el directorio seleccionado.

También puedes usar <kbd>j</kbd> y <kbd>k</kbd> para moverte por los resultados.

Puedes abrir el directorio donde se aloja el resultado seleccionado pulsando <kbd>o</kbd>.

Para salir de Npkill, utiliza <kbd>Q</kbd>, o si te sientes valiente, <kbd>Ctrl</kbd> + <kbd>c</kbd>.

**¡Importante!** Algunas aplicaciones que están instaladas en el sistema necesitan su directorio node_modules para funcionar, y borrarlo puede romperlas. NPKILL te mostrará un :warning: para que sepas que tienes que tener cuidado.

<a name="options"></a>

## Opciones

| ARGUMENTO                        | DESCRIPCIÓN                                                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --bg-color                   | Cambia el color de selección de la fila. _(Colores disponibles: **azul**, cyan, magenta, blanco, rojo y amarillo)_                                             |
| -d, --directory                  | Permite seleccionar el directorio desde el que comienza la búsqueda. Por defecto, se empieza en .                                                              |
| -D, --delete-all                 | Borra automáticamente todos los node_modules que se encuentren. Recomendable utilizar junto a `-x`                                                             |
| -e, --hide-errors                | Esconde los errores en el caso de que ocurra alguno                                                                                                            |
| -E, --exclude                    | Excluye directorios de la búsqueda (la lista de directorios debe estar entre comillas dobles "", cada directorio separado por ',' Ejemplo: "ignore1, ignore2") |
| -f, --full                       | Comienza la búsqueda en el home del usuario (ejemplo: "/home/user" en Linux)                                                                                   |
| -gb                              | Muestra el tamaño en Gigabytes en lugar de en Megabytes.                                                                                                       |
| -h, --help, ?                    | Muestra esta página de ayuda y finaliza                                                                                                                        |
| -nu, --no-check-update           | No comprobar si hay actualizaciones al iniciar la aplicación                                                                                                   |
| -s, --sort                       | Ordena los resultados por: `size`, `path` or `last-mod`                                                                                                        |
| -t, --target                     | Especifica el nombre del directorio que se buscará (por defecto es node_modules)                                                                               |
| -x, --exclude-hidden-directories | Excluye directorios ocultos (directorios "dot") de la búsqueda                                                                                                 |
| --dry-run                        | No borra nada (simula un tiempo de borrado aleatorio)                                                                                                          |
| -v, --version                    | Muestra la versión de Npkill                                                                                                                                   |

**Precaución:** _Algunos comandos pueden cambiar en versiones futuras_

<a name="examples"></a>

## Ejemplo

- Busca y encuentra los directorios **node_modules** en un directorio _projects_ :

```bash
npkill -d ~/projects

# otra alternativa:
cd ~/projects
npkill
```

- Lista los directorios llamados "dist" y muestra los errores que ocurran:

```bash
npkill --target dist -e
```

- Muestra el cursor de color magenta... ¡Porque me gusta el magenta!

```bash
npkill --bg-color magenta
```

- Lista los directorios **vendor** en un directorio _projects_, ordenados por tamaño y mostrando el tamaño en gb:

```bash
npkill -d '~/more projects' -gb --sort size --target vendor
```

- Lista los **node_modules** en el directorio _projects_, excluyendo los que están en los directorios _progress_ e _ignore-this_:

```bash
npkill -d 'projects' --exclude "progress, ignore-this"
```

- Borra automáticamente todos los **node_modules** que se encuentren en el directorio _backups_:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Configuración local

```bash
# -- Primero, clona el repositorio
git clone https://github.com/voidcosmos/npkill.git

# -- Navega al dir
cd npkill

# -- Instala las dependencias
npm install

# -- ¡Y ejecuta!
npm run start


# -- Si quieres ejecutar con algún parámetro, hay que añadir "--", tal y como se muestra a continuación:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Roadmap

- [x] Lanzar la versión 0.1.0 !
- [x] Mejorar el código
  - [x] Mejorar el rendimiento
  - [ ] ¡Mejorar el rendimiento aún más!
- [x] Ordenar los resultados por tamaño y ruta
- [x] Permitir la búsqueda de otro tipo de directorios (targets)
- [ ] Reducir las dependencies para ser un módulo más minimalista
- [ ] Permitir el filtrado por directorios que no se hayan utilizado en un periodo de tiempo determinado
- [ ] Crear una opción para mostrar los directorios en formato árbol
- [x] Añadir menús
- [x] Añadir un servicio de logs
- [ ] Limpieza periódica y automática (?)

<a name="known-bugs"></a>

# :bug: Bugs conocidos :bug:

- A veces, el CLI se bloquea mientras un directorio se está borrando.
- La ordenación, especialmente por rutas, puede ralentizar la terminal cuando haya muchos resultados al mismo tiempo.
- A veces, los cálculos de tamaño son mayores de lo que deberían ser.
- (RESUELTO) Problemas de rendimiento al hacer la búsqueda desde directorios de alto nivel (como / en Linux).
- (RESUELTO) A veces el texto se colapsa al actualizar el CLI.
- (RESUELTO) Analizar el tamaño de los directorios tarda más de lo que debería.

> Si encuentras algún bug, no dudes en abrir un issue :)

<a name="contributing"></a>

# :revolving_hearts: Cómo contribuir

Si quieres contribuir, échale un vistazo al [CONTRIBUTING.md](.github/CONTRIBUTING.es.md)

<a name="donations"></a>

# :coffee: Invítanos a un café

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Hemos desarrollado Npkill en nuestro tiempo libre, porque nos apasiona la programación.

El día de mañana nos gustaría dedicarnos al open source completamente, pero antes, nos queda un largo camino por recorrer.

Seguiremos contribuyendo al open source por y para siempre, pero las donaciones son una de las muchas formas de apoyarnos.

¡Invítanos a un café! (O a un té para Nya, la única programadora a la que no le gusta el café).

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Dona a este proyecto utilizando Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Botón de donar con Open Collective" /></a></span>

### ¡¡Mil gracias!!

## Muchísimas gracias a todos los que nos han apoyado :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Alternativa cripto

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Licencia

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) y [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---
```

## File: `README.id.md`
```markdown
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Mudah menemukan dan **menghapus** folder <font color="red">**node_modules**</font> yang lama dan berat :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Alat ini memungkinkan Anda untuk mencantumkan semua direktori _node_modules_ di sistem Anda, serta ruang yang mereka gunakan. Anda kemudian dapat memilih mana yang ingin Anda hapus untuk mengosongkan ruang penyimpanan. Yay!

## i18n

Kami berusaha untuk menerjemahkan dokumen Npkill ke berbagai bahasa. Berikut daftar terjemahan yang tersedia:

- [Español](./README.es.md)
- [Indonesian](./README.id.md)
- [Portugis](../../../core/security/QUARANTINE/vetted/repos/goclaw/readmes/README.pt.md)
- [Turki](./README.tr.md)

## Daftar Isi

- [Fitur](#features)
- [Instalasi](#installation)
- [Penggunaan](#usage)
  - [Opsi](#options)
  - [Contoh](#examples)
- [Pengaturan Lokal](#setup-locally)
- [Peta Jalan](#roadmap)
- [Bug yang Diketahui](#known-bugs)
- [Kontribusi](#contributing)
- [Buy us a coffee](#donations)
- [Lisensi](#license)

<a name="features"></a>

# :heavy_check_mark: Fitur

- **Bersihkan Ruang:** Hapus _node_modules_ lama yang tidak digunakan yang memenuhi mesin Anda.

- **Penggunaan Terakhir Workspace:** Cek kapan terakhir kali Anda mengubah file di workspace (ditunjukkan di kolom **last_mod**).

- **Sangat Cepat:** NPKILL ditulis dalam TypeScript, tetapi pencarian dilakukan di tingkat rendah, sehingga performanya sangat baik.

- **Mudah Digunakan:** Tidak perlu perintah panjang. Menggunakan npkill semudah membaca daftar _node_modules_ Anda, dan menekan tombol Del untuk menghapusnya. Bisa lebih mudah dari itu?

- **Ringkas:** Hampir tidak memiliki dependensi.

<a name="installation"></a>

# :cloud: Instalasi

Anda tidak perlu menginstal untuk menggunakannya! Cukup gunakan perintah berikut:

```bash
$ npx npkill
```

Atau jika Anda benar-benar ingin menginstalnya:

```bash
$ npm i -g npkill
# Pengguna Unix mungkin perlu menjalankan perintah dengan sudo. Gunakan dengan hati-hati
```

> NPKILL tidak mendukung node<v14. Jika ini memengaruhi Anda, gunakan `npkill@0.8.3`

<a name="usage"></a>

# :clipboard: Penggunaan

```bash
$ npx npkill
# atau cukup npkill jika telah diinstal secara global
```

Secara default, npkill akan memindai _node_modules_ mulai dari jalur tempat perintah `npkill` dijalankan.

Pindah di antara folder yang terdaftar menggunakan <kbd>↓</kbd> <kbd>↑</kbd>, dan gunakan <kbd>Space</kbd> atau <kbd>Del</kbd> untuk menghapus folder yang dipilih. Anda juga dapat menggunakan <kbd>j</kbd> dan <kbd>k</kbd> untuk bergerak di antara hasil.

Anda dapat membuka direktori tempat hasil yang dipilih berada dengan menekan <kbd>o</kbd>.

Untuk keluar, tekan <kbd>Q</kbd> atau <kbd>Ctrl</kbd> + <kbd>c</kbd> jika Anda pemberani.

**Penting!** Beberapa aplikasi yang diinstal di sistem membutuhkan direktori _node_modules_ untuk berfungsi, dan menghapusnya dapat menyebabkan kerusakan. NPKILL akan menandainya dengan :warning: agar berhati-hati.

<a name="options"></a>

## Opsi

| ARGUMEN                          | DESKRIPSI                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| -c, --bg-color                   | Ubah warna sorotan baris. _(Tersedia: **blue**, cyan, magenta, white, red, dan yellow)_                       |
| -d, --directory                  | Tetapkan direktori awal pencarian. Secara default, mulai dari .                                               |
| -D, --delete-all                 | Secara otomatis hapus semua folder _node_modules_ yang ditemukan. Disarankan digunakan bersama `-x`.          |
| -e, --hide-errors                | Sembunyikan kesalahan (jika ada)                                                                              |
| -E, --exclude                    | Kecualikan direktori dari pencarian. Daftar direktori harus dalam tanda kutip ganda "", dipisahkan dengan ',' |
| -f, --full                       | Mulai pencarian dari direktori home pengguna (contoh: "/home/user" di Linux)                                  |
| -gb                              | Tampilkan folder dalam Gigabyte daripada Megabyte.                                                            |
| -h, --help, ?                    | Tampilkan halaman bantuan ini dan keluar                                                                      |
| -nu, --no-check-update           | Jangan memeriksa pembaruan saat startup                                                                       |
| -s, --sort                       | Urutkan hasil berdasarkan: `size`, `path`, atau `last-mod`                                                    |
| -t, --target                     | Tentukan nama direktori yang ingin Anda cari (default: node_modules)                                          |
| -x, --exclude-hidden-directories | Kecualikan direktori tersembunyi dari pencarian.                                                              |
| --dry-run                        | Tidak menghapus apa pun (hanya simulasi dengan delay acak).                                                   |
| -v, --version                    | Tampilkan versi npkill                                                                                        |

**Peringatan:** _Di versi mendatang, beberapa perintah mungkin berubah._

<a name="examples"></a>

## Contoh

- Cari direktori **node_modules** di direktori _projects_ Anda:

```bash
npkill -d ~/projects

# alternatif lain:
cd ~/projects
npkill
```

- Daftar direktori bernama "dist" dan tampilkan kesalahan jika ada:

```bash
npkill --target dist -e
```

- Tampilkan kursor warna magenta... karena saya suka magenta!

```bash
npkill --color magenta
```

- Daftar direktori **vendor** di _projects_, urutkan berdasarkan ukuran, dan tampilkan ukuran dalam GB:

```bash
npkill -d '~/more projects' -gb --sort size --target vendor
```

- Secara otomatis hapus semua _node_modules_ di folder cadangan Anda:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Pengaturan Lokal

```bash
# -- Pertama, kloning repositori
git clone https://github.com/voidcosmos/npkill.git

# -- Masuk ke direktori
cd npkill

# -- Instal dependensi
npm install

# -- Dan jalankan!
npm run start

# -- Jika ingin menjalankannya dengan parameter, tambahkan "--" seperti contoh berikut:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Peta Jalan

- [x] Rilis versi 0.1.0!
- [x] Tingkatkan kode
  - [x] Tingkatkan performa
  - [ ] Tingkatkan performa lebih lanjut!
- [x] Urutkan hasil berdasarkan ukuran dan jalur
- [x] Izinkan pencarian untuk jenis direktori (target) lainnya
- [ ] Kurangi dependensi agar minimalis
- [ ] Filter berdasarkan waktu terakhir penggunaan
- [ ] Tampilkan direktori dalam format tree
- [x] Tambahkan beberapa menu
- [x] Tambahkan log
- [ ] Pembersihan otomatis berkala (?)

<a name="known-bugs"></a>

# :bug: Bug yang Diketahui :bug:

- CLI terkadang berhenti saat menghapus folder.
- Beberapa terminal tanpa TTY (seperti Git Bash di Windows) tidak bekerja.
- Mengurutkan berdasarkan jalur dapat memperlambat terminal dengan banyak hasil.
- Perhitungan ukuran kadang lebih besar dari seharusnya.
- (TERPECAHKAN) Masalah performa pada direktori tingkat tinggi (seperti / di Linux).
- (TERPECAHKAN) Teks terkadang kacau saat CLI diperbarui.
- (TERPECAHKAN) Analisis ukuran direktori memakan waktu lebih lama dari seharusnya.

> Jika menemukan bug, jangan ragu untuk membuka issue. :)

<a name="contributing"></a>

# :revolving_hearts: Kontribusi

Jika ingin berkontribusi, cek [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md).

<a name="donations"></a>

# :coffee: Buy us a coffee

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Kami mengembangkan npkill di waktu luang karena kami mencintai pemrograman.

Kami akan terus mengerjakan ini, tetapi donasi adalah salah satu cara mendukung apa yang kami lakukan.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Donate to this project using Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Terima Kasih!!

## Terima kasih banyak kepada pendukung kami :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Alternatif Crypto

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Lisensi

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) dan [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---
```

## File: `README.md`
```markdown
<p align="center">
  <img src="./docs/npkill-text-clean.svg" width="380" alt="npkill logo" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Easily find and **remove** old and heavy <font color="red">**node_modules**</font> folders :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

This tool allows you to list any _node_modules_ directories in your system, as well as the space they take up. You can then select which ones you want to erase to free up space. Yay!

## i18n

We're making an effort to internationalize the Npkill docs. Here's a list of the available translations:

- [Español](./README.es.md)
- [Indonesian](./README.id.md)
- [Português](../../../core/security/QUARANTINE/vetted/repos/goclaw/readmes/README.pt.md)
- [Turkish](./README.tr.md)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Multi-Select Mode](#multi-select-mode)
  - [Options](#options)
  - [Examples](#examples)
  - [JSON Output](#json-output)
- [Set Up Locally](#setup-locally)
- [API](#API)
- [Roadmap](#roadmap)
- [Known bugs](#known-bugs)
- [Contributing](#contributing)
- [Buy us a coffee](#donations)
- [License](#license)

<a name="features"></a>

# :heavy_check_mark: Features

- **Clear space:** Get rid of old and dusty _node_modules_ cluttering up your machine.

- **Last Workspace Usage**: Check when was the last time you modified a file in the workspace (indicated in the **last_mod** column).

- **Very fast:** NPKILL is written in TypeScript, but searches are performed at a low level, improving performance greatly.

- **Easy to use:** Say goodbye to lengthy commands. Using npkill is as simple as reading a list of your node_modules, and pressing Del to get rid of them. Could it be any easier? ;)

- **Minified:** It barely has any dependencies.

<a name="installation"></a>

# :cloud: Installation

You don't really need to install it to use it!
Simply use the following command:

```bash
$ npx npkill
```

Or if for some reason you really want to install it:

```bash
$ npm i -g npkill
# Unix users may need to run the command with sudo. Go carefully
```

> NPKILL does not support node<v14. If this affects you you can use `npkill@0.8.3`

<a name="usage"></a>

# :clipboard: Usage

```bash
$ npx npkill
# or just npkill if installed globally
```

By default, npkill will scan for node_modules starting at the path where `npkill` command is executed.

Move between the listed folders with <kbd>↓</kbd> <kbd>↑</kbd>, and use <kbd>Space</kbd> or <kbd>Del</kbd> to delete the selected folder.
You can also use <kbd>j</kbd> and <kbd>k</kbd> to move between the results.

You can open the directory where the selected result is placed by pressing <kbd>o</kbd>.

To exit, <kbd>Q</kbd> or <kbd>Ctrl</kbd> + <kbd>c</kbd> if you're brave.

**Important!** Some applications installed on the system need their node_modules directory to work and deleting them may break them. NPKILL will highlight them by displaying a :warning: to be careful.

## Search Mode

Search mode allows you to filter results. This can be particularly useful for limiting the view to a specific route or ensuring that only those results that meet the specified condition are “selected all.”

For example, you can use this expression to limit the results to those that are in the `work` directory and that include `data` somewhere in the path: `/work/.*/data`.

Press <kbd>/</kbd> to enter search mode. You can type a regex pattern to filter results.

Press <kbd>Enter</kbd> to confirm the search and navigate the filtered results, or <kbd>Esc</kbd> to clear and exit.

To exit from this mode, leave empty.

## Multi-Select Mode

This mode allows you to select and delete multiple folders at once, making it more efficient when cleaning up many directories.

### Entering Multi-Select Mode

Press <kbd>T</kbd> to toggle multi-select mode. When active, you'll see a selection counter and additional instructions at the top of the results.

### Controls

- **<kbd>Space</kbd>**: Toggle selection of the current folder.
- **<kbd>V</kbd>**: Start/end range selection mode.
- **<kbd>A</kbd>**: Toggle select/unselect all folders.
- **<kbd>Enter</kbd>**: Delete all selected folders.
- **<kbd>T</kbd>**: Unselect all and back to normal mode.

### Range Selection

After pressing <kbd>V</kbd> to enter range selection mode:

- Move the cursor with arrow keys, <kbd>j</kbd>/<kbd>k</kbd>, <kbd>Home</kbd>/<kbd>End</kbd>, or page up/down
- All folders between the starting position and current cursor position will be selected/deselected
- Press <kbd>V</kbd> again to exit range selection mode

<a name="options"></a>

## Options

| ARGUMENT                | DESCRIPTION                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p, --profiles          | Allows you to select the [profile](../../../core/security/QUARANTINE/vetted/repos/npkill/docs/profiles.md) (set of targets) to use. If no option is specified, the available ones will be listed _(**node** by default)_.         |
| --config                | Path to a custom .npkillrc configuration file. By default, npkill looks first for `./.npkillrc` and then for `~/.npkillrc`.                                                   |
| -d, --directory         | Set the directory from which to begin searching. By default, starting-point is .                                                                                              |
| -D, --delete-all        | Automatically delete all folders that are found. Suggested to be used together with `-x`.                                                                                     |
| -e, --hide-errors       | Hide errors if any                                                                                                                                                            |
| -E, --exclude           | Exclude directories from search (directory list must be inside double quotes "", each directory separated by ',' ) Example: "ignore1, ignore2"                                |
| -f, --full              | Start searching from the home of the user (example: "/home/user" in linux)                                                                                                    |
| --size-unit             | Set the unit for displaying folder sizes. _(Available: **auto**, mb, gb)_. With auto, sizes < 1024MB are shown in MB (rounded), larger sizes in GB (with decimals).           |
| -h, --help, ?           | Show help page                                                                                                                                                                |
| -nu, --no-check-update  | Don't check for updates on startup                                                                                                                                            |
| -s, --sort              | Sort results by: `size`, `path` or `age`                                                                                                                                      |
| -t, --targets           | Disable profiles feature and specify the name of the directories you want to search for. You can define multiple targets separating with comma. Ej. `-t node_modules,.cache`. |
| -x, --exclude-sensitive | Exclude sensitive directories.                                                                                                                                                |
| -y                      | Avoid displaying a warning when executing --delete-all.                                                                                                                       |
| --dry-run               | It does not delete anything (will simulate it with a random delay).                                                                                                           |
| --json                  | Output results in JSON format at the end of the scan. Useful for automation and scripting.                                                                                    |
| --json-stream           | Output results in streaming JSON format (one JSON object per line as results are found). Useful for real-time processing.                                                     |
| -v, --version           | Show npkill version                                                                                                                                                           |

<a name="examples"></a>

## Examples

- Search **node_modules** directories in your _projects_ directory:

```bash
npkill -d ~/projects

# other alternative:
cd ~/projects
npkill
```

- List **node_modules** in your _projects_ directory, excluding the ones in _progress_ and _ignore-this_ directories:

```bash
npkill -d 'projects' --exclude "progress, ignore-this"
```

- Automatically delete all node_modules that have sneaked into your backups:

```bash
npkill -d ~/backups/ --delete-all
```

- Get results in JSON format for automation or further processing:

```bash
npkill --json > results.json
```

- Stream results in real-time as JSON (useful for monitoring or piping to other tools):

```bash
npkill --json-stream | jq '.'
```

- Save only successful results to a file, ignoring errors:

```bash
npkill --json-stream 2>/dev/null | jq -s '.' > clean-results.json
```

<a name="json-output"></a>

## JSON Output

Npkill supports JSON output formats for automation and integration with other tools:

- **`--json`**: Output all results as a single JSON object at the end of the scan
- **`--json-stream`**: Output each result as a separate JSON object in real-time

For detailed documentation, examples, and TypeScript interfaces, see [JSON Output Documentation](./docs/json-output.md).

**Quick Examples:**

```bash
# Get all results as JSON
npkill --json > results.json

# Process results in real-time
npkill --json-stream | jq '.result.path'

# Find directories larger than 100MB
npkill --json | jq '.results[] | select(.size > 104857600)'
```

<a name="setup-locally"></a>

# :pager: Set Up Locally

```bash
# -- First, clone the repository
git clone https://github.com/voidcosmos/npkill.git

# -- Navigate to the dir
cd npkill

# -- Install dependencies
npm install

# -- And run!
npm run start


# -- If you want to run it with some parameter, you will have to add "--" as in the following example:
npm run start -- -f -e
```

<a name="API"></a>

# :bookmark_tabs: API

The api allows you to interact with npkill from node to create your own implementations in your scripts (automations, for example).

You can check the basic API [here](./API.md) or on the web (comming soon).

<a name="roadmap"></a>

# :crystal_ball: Roadmap

- [x] Release 0.1.0 !
- [x] Improve code
  - [x] Improve performance
  - [ ] Improve performance even more!
- [x] Sort results by size and path
- [x] Allow the search for other types of directories (targets)
- [ ] Reduce dependencies to be a more minimalist module
- [ ] Allow to filter by directories that have not been used in a period of time
- [ ] Create option for displaying directories in tree format
- [x] Add some menus
- [x] Add log service
- [ ] Periodic and automatic cleaning (?)

<a name="known-bugs"></a>

# :bug: Known bugs :bug:

- Sometimes, CLI is blocked while folder is deleting.
- Sorting, especially by routes, can slow down the terminal when there are many results at the same time.
- Sometimes, size calculations are higher than they should be.
- (SOLVED) Performance issues when searching from high level directories (like / in linux).
- (SOLVED) Sometimes text collapses when updating the cli.
- (SOLVED) Analyzing the size of the directories takes longer than it should.

> If you find any bugs, don't hesitate and open an issue :)

<a name="contributing"></a>

# :revolving_hearts: Contributing

If you want to contribute check the [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md)

<a name="donations"></a>

# :coffee: Buy us a coffee

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
We have developed npkill in our free time, because we are passionate about the programming sector.
Tomorrow we would like to dedicate ourselves to this, but first, we have a long way to go.

We will continue to do things anyway, but donations are one of the many ways to support what we do.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Donate to this project using Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Thanks!!

## A huge thank you to our backers :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Crypto alternative

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: License

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) and [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---
```

## File: `README.pt.md`
```markdown
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Encontre e **remova** facilemente pastas <font color="red">**node_modules**</font> antigas e pesadas :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Esta ferramenta permite que você liste as pastas _node_modules_ em seu sistema, bem como o espaço que ocupam. Então você pode selecionar quais deles deseja apagar para liberar espaço. ¡Yay!

## i18n

Estamos fazendo esforço para internacionalizar a documentação do Npkill. Aqui está uma lista das traduções disponíveis:

- [Español](./README.es.md)
- [Português](../../../core/security/QUARANTINE/vetted/repos/goclaw/readmes/README.pt.md)

## Table of Contents

- [Funcionalidades](#features)
- [Instalação](#installation)
- [Utilização](#usage)
  - [Opções](#options)
  - [Exemplos](#examples)
- [Configurar localmente](#setup-locally)
- [Roteiro](#roadmap)
- [Problemas conhecidos](#known-bugs)
- [Contribuindo](#contributing)
- [Compre-nos um café](#donations)
- [Licença](#license)

<a name="features"></a>

# :heavy_check_mark: Funcionalidades

- **Liberar espaço:** Livre-se dos antigos e empoeirados node_modules que ocupam espaço em sua máquina.

- **Último Uso do Espaço de Trabalho**: Verifique quando foi a última vez que você modificou um arquivo no espaço de trabalho (indicado na coluna **última_modificação**).

- **Muito rápido:** O NPKILL é escrito em TypeScript, mas as pesquisas são realizadas em um nível baixo, melhorando muito o desempenho.

- **Fácil de usar:** Diga adeus aos comandos longos. Usar o npkill é tão simples quanto ler uma lista de seus node_modules e pressionar Delete para se livrar deles. Pode ser mais fácil do que isso? ;)

- **Minificado:** Ele mal possui dependências.

<a name="installation"></a>

# :cloud: Instalação

Você nem precisa instalá-lo para usar!
Basta usar o seguinte comando:

```bash
$ npx npkill
```

Ou, se por algum motivo você realmente deseja instalá-lo:

```bash
$ npm i -g npkill
# Usuários do Unix podem precisar executar o comando com sudo. Tome cuidado.
```

> O NPKILL não suporta versões node<v14. Se isso afeta você, use npkill@0.8.3.

<a name="usage"></a>

# :clipboard: Utilização

```bash
$ npx npkill
# ou apenas npkill se você instalou globalmente
```

Por padrão, o npkill fará a varredura em busca de node_modules a partir do local onde o comando npkill é executado.

Para mover entre as pastas listadas, utilize as teclas <kbd>↓</kbd> e <kbd>↑</kbd>, e use <kbd>Space</kbd> ou <kbd>Del</kbd> para excluir a pasta selecionada.
Você também pode usar <kbd>j</kbd> e <kbd>k</kbd> para se mover entre os resultados.

Para abrir o diretório onde o resultado selecionado está localizado, pressione <kbd>o</kbd>.

Para sair, use <kbd>Q</kbd> ou <kbd>Ctrl</kbd> + <kbd>c</kbd> se você estiver se sentindo corajoso.

**Importante!** Algumas aplicações instaladas no sistema precisam do diretório node_modules delas para funcionar, e excluí-los pode quebrá-las. O NPKILL irá destacá-los exibindo um :warning: para que você tenha cuidado.

<a name="options"></a>

## Opções

| Comando                          | Descrição                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -c, --bg-color                   | Troca a cor de destaque da linha. _(Disponível: **blue**, cyan, magenta, white, red e yellow)_                                                                      |
| -d, --directory                  | Defina o diretório a partir do qual iniciar a pesquisa. Por padrão, o ponto de partida é a raiz is .                                                                |
| -D, --delete-all                 | Exclui automaticamente todos os node_modules encontrados. Recomendado para usar junto com `-x`                                                                      |
| -e, --hide-errors                | Oculta erros                                                                                                                                                        |
| -E, --exclude                    | Excluir diretórios da pesquisa (a lista de diretórios deve estar entre aspas duplas "", com cada diretório separado por vírgula ','). Exemplo: "ignorar1, ignorar2" |
| -f, --full                       | Iniciar a pesquisa a partir do diretório pessoal do usuário (exemplo: "/home/user" no Linux)                                                                        |
| -gb                              | Mostra as pastas em Gigabytes ao invés de Megabytes.                                                                                                                |
| -h, --help, ?                    | Mostrar a página de ajuda e sair                                                                                                                                    |
| -nu, --no-check-update           | Não verificar atualizações na inicialização                                                                                                                         |
| -s, --sort                       | Ordenar resultados por: `size` (tamanho), `path`(localização) ou `last-mod`(última modificação)                                                                     |
| -t, --target                     | Especifique o nome dos diretórios que deseja pesquisar (por padrão, é node_modules)                                                                                 |
| -x, --exclude-hidden-directories | Excluir diretórios ocultos ("diretórios com ponto") da pesquisa.                                                                                                    |
| --dry-run                        | Não exclui nada (irá simular com um atraso aleatório).                                                                                                              |
| -v, --version                    | Mostrar versão do npkill                                                                                                                                            |

**Aviso:** _No futuro alguns comandos podem mudar_

<a name="examples"></a>

## Examples

- Busque pastas **node_modules** no seu diretório de projetos:

```bash
npkill -d ~/projetos

# alternativa:
cd ~/projetos
npkill
```

- Listar diretórios com o nome "dist" e mostrar erros, se houver algum:

```bash
npkill --target dist -e
```

- Exibe o cursor na cor magenta... porque eu gosto de magenta!

```bash
npkill --bg-color magenta
```

- Listar pastas **vendor** no seu diretório de _projetos_, ordenar por tamanho e mostrar o tamanho em GB:

```bash
npkill -d '~/more projetos' -gb --sort size --target vendor
```

- Listar **node_modules** no seu diretório de _projetos_, exceto nas pastas _progresso_ e _ignorar_:

```bash
npkill -d 'projetos' --exclude "progresso, ignorar"
```

- Exclua automaticamente todos os node_modules que tenham entrado em seus backups:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Configurar localmente

```bash
# -- Primeiramente, clone o repositório
git clone https://github.com/voidcosmos/npkill.git

# -- Acesse a pasta
cd npkill

# -- Instale as dependências
npm install

# -- E rode!
npm run start


# -- Se você deseja executá-lo com algum parâmetro, você terá que adicionar "--" como no seguinte exemplo:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Roteiro

- [x] Lançamento 0.1.0 !
- [x] Melhorias de código
  - [x] Melhorias de performance
  - [ ] Ainda mais melhorias de performance!
- [x] Ordenação de resultados por tamanho e localização
- [x] Permitir a pesquisa por outros tipos de diretórios (alvo)
- [ ] Reduzir as dependências para tornar o módulo mais minimalista
- [ ] Permitir filtrar por diretórios que não foram usados em um período de tempo
- [ ] Criar opção para mostrar as pastas em formato de árvore
- [x] Adicionar menus
- [x] Adicionar logs
- [ ] Limpeza automatizada periódica (?)

<a name="known-bugs"></a>

# :bug: Problemas conhecidos :bug:

- Às vezes, a CLI fica bloqueada enquanto a pasta está sendo excluída.
- Alguns terminais que não utilizam TTY (como o git bash no Windows) não funcionam.
- A ordenação, especialmente por rotas, pode deixar o terminal mais lento quando há muitos resultados ao mesmo tempo.
- Às vezes, os cálculos de tamanho são maiores do que deveriam ser.
- (RESOLVIDO) Problemas de desempenho ao pesquisar em diretórios de alto nível (como / no Linux).
- (RESOLVIDO) Às vezes, o texto se desfaz ao atualizar a interface de linha de comando (CLI).
- (RESOLVIDO) A análise do tamanho dos diretórios leva mais tempo do que deveria.

> Se você encontrar algum erro, não hesite em abrir uma solicitação (via issue) :)

<a name="contributing"></a>

# :revolving_hearts: Contribuindo

Se você quer contribuir confira o [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md)

<a name="donations"></a>

# :coffee: Compre-nos um café

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Desenvolvemos o npkill em nosso tempo livre, porque somos apaixonados pelo setor de programação. Amanhã, gostaríamos de nos dedicar mais a isso, mas antes, temos um longo caminho a percorrer.

Continuaremos a fazer as coisas de qualquer maneira, mas as doações são uma das muitas formas de apoiar o que fazemos.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Faça uma doação para este projeto usando o Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Obrigado!!

## Um enorme agradecimento aos nossos apoiadores :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### via Crypto

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Licença

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) e [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---
```

## File: `README.tr.md`
```markdown
<p align="center">
  <img src="https://npkill.js.org/img/npkill-text-outlined.svg" width="320" alt="npkill logo" />
  <img src="https://npkill.js.org/img/npkill-scope-mono.svg" width="50" alt="npkill logo scope" />
</p>
<p align="center">
<img alt="npm" src="https://img.shields.io/npm/dy/npkill.svg">
<a href="#donations"><img src="https://img.shields.io/badge/donate-<3-red" alt="Donations Badge"/></a>
<img alt="npm version" src="https://img.shields.io/npm/v/npkill.svg">
<img alt="NPM" src="https://img.shields.io/npm/l/npkill.svg">
</p>

### Eski ve büyük <font color="red">**node_modules**</font> klasörlerini kolayca bulun ve **silin** :sparkles:

<p align="center">
  <img src="/docs/npkill-demo-0.10.0.gif" alt="npkill demo GIF" />
</p>

Bu araç, sisteminizdeki tüm _node_modules_ dizinlerini ve kapladıkları alanı listelemenizi sağlar. Daha sonra, hangilerini silmek istediğinizi seçerek yer açabilirsiniz. Yaşasın!

## i18n

Npkill dokümantasyonunu uluslararası hale getirmek için çaba gösteriyoruz. İşte mevcut çevirilerin listesi:

- [Endonezce](./README.id.md)
- [İspanyolca](./README.es.md)
- [Portekizce](../../../core/security/QUARANTINE/vetted/repos/goclaw/readmes/README.pt.md)
- [Türkçe](./README.tr.md)

## İçindekiler

- [Özellikler](#features)
- [Kurulum](#installation)
- [Kullanım](#usage)
  - [Seçenekler](#options)
  - [Örnekler](#examples)
- [Yerel Kurulum](#setup-locally)
- [Yol Haritası](#roadmap)
- [Bilinen Hatalar](#known-bugs)
- [Katkıda Bulunma](#contributing)
- [Kahve Ismarlayın](#donations)
- [Lisans](#license)

<a name="features"></a>

# :heavy_check_mark: Özellikler

- **Alan Açın:** Makinenizde birikmiş, eski ve tozlu _node_modules_ klasörlerinden kurtulun.

- **Son Çalışma Alanı Kullanımı**: Çalışma alanındaki bir dosyayı en son ne zaman değiştirdiğinizi kontrol edin (bu, **last_mod** sütununda gösterilir).

- **Çok Hızlı:** NPKILL TypeScript ile yazılmıştır, ancak aramalar düşük seviyede gerçekleştirilerek performans büyük ölçüde artırılır.

- **Kullanımı Kolay:** Uzun komutlara elveda deyin. NPKILL kullanmak, node_modules listenizi okumak ve silmek için Del tuşuna basmak kadar basittir. Daha kolay olabilir mi? ;)

- **Düşük Bağımlılık:** Hiçbir bağımlılığı yok denecek kadar az.

<a name="installation"></a>

# :cloud: Kurulum

Kullanmak için gerçekten yüklemenize gerek yok!
Basitçe aşağıdaki komutu kullanabilirsiniz:

```bash
$ npx npkill
```

Ya da herhangi bir nedenle gerçekten yüklemek isterseniz:

```bash
$ npm i -g npkill
# Unix kullanıcılarının komutu sudo ile çalıştırması gerekebilir. Dikkatli olun.
```

> NPKILL, Node 14’ten düşük sürümleri desteklemiyor. Eğer bu durum sizi etkiliyorsa, `npkill@0.8.3` sürümünü kullanabilirsiniz.

<a name="usage"></a>

# :clipboard: Kullanım

```bash
$ npx npkill
# Ya da global olarak yüklüyse sadece npkill kullanabilirsiniz.
```

Varsayılan olarak, npkill `npkill` komutunun çalıştırıldığı dizinden başlayarak node_modules klasörlerini tarar.

Listelenen klasörler arasında <kbd>↓</kbd> ve <kbd>↑</kbd> tuşlarıyla gezinebilir, seçili klasörü silmek için <kbd>Space</kbd> veya <kbd>Del</kbd> tuşlarını kullanabilirsiniz.
Ayrıca sonuçlar arasında gezinmek için <kbd>j</kbd> ve <kbd>k</kbd> tuşlarını da kullanabilirsiniz.

Seçili sonucun bulunduğu klasörü açmak için <kbd>o</kbd> tuşuna basabilirsiniz.

Çıkmak için, <kbd>Q</kbd> ya da <kbd>Ctrl</kbd> + <kbd>C</kbd>.

**Önemli!** Sisteme kurulu bazı uygulamaların çalışması için node_modules klasörüne ihtiyacı vardır ve bu klasörlerin silinmesi uygulamaların bozulmasına yol açabilir. NPKILL, dikkatli olmanız için bu klasörleri :warning: simgesiyle vurgulayacaktır.

<a name="options"></a>

## Seçenekler

| ARGÜMAN                          | AÇIKLAMA                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| -c, --bg-color                   | Satır vurgulama rengini değiştirin. _(Mevcut seçenekler: **mavi**, cam göbeği, eflatun, beyaz, kırmızı ve sarı)_                                 |
| -d, --directory                  | Aramaya başlanacak dizini ayarlayın. Varsayılan başlangıç noktası . olarak belirlenmiştir.                                                       |
| -D, --delete-all                 | Bulunan tüm node_modules klasörlerini otomatik olarak siler. `-x` ile birlikte kullanılması önerilir.                                            |
| -e, --hide-errors                | Varsa hataları gizler                                                                                                                            |
| -E, --exclude                    | Aramadan hariç tutulacak dizinleri belirtin (dizin listesi çift tırnak içinde "", dizinler virgülle ',' ayrılmalıdır). Örnek: "ignore1, ignore2" |
| -f, --full                       | Aramaya kullanıcının ev dizininden başlayın (örneğin Linux'ta "/home/user").                                                                     |
| -gb                              | Klasörleri Megabytes yerine Gigabytes olarak göster.                                                                                             |
| -h, --help, ?                    | Bu yardım sayfasını göster ve çık.                                                                                                               |
| -nu, --no-check-update           | Başlangıçta güncellemeleri kontrol etme.                                                                                                         |
| -s, --sort                       | Sonuçları şu kriterlere göre sırala: `size`, `path` veya `last-mod`                                                                              |
| -t, --target                     | Aramak istediğiniz dizinlerin adını belirtin (varsayılan olarak node_modules).                                                                   |
| -x, --exclude-hidden-directories | Gizli dizinleri ("nokta" dizinleri) arama kapsamı dışında bırak.                                                                                 |
| --dry-run                        | Hiçbir şeyi silmez (rastgele bir gecikme ile simüle eder).                                                                                       |
| -v, --version                    | npkill sürümünü gösterir.                                                                                                                        |

**Uyarı:** _Gelecek sürümlerde bazı komutlar değişebilir_

<a name="examples"></a>

## Örnekler

- _projects_ dizininizdeki **node_modules** klasörlerini arayın:

```bash
npkill -d ~/projects

# diğer alternatif:
cd ~/projects
npkill
```

- "dist" adlı dizinleri listeleyin ve hata oluşursa gösterin.

```bash
npkill --target dist -e
```

- Mor renkli imleç gösterilir... çünkü moru seviyorum!

```bash
npkill --color magenta
```

- _projects_ dizininizdeki **vendor** klasörlerini listeleyin, boyuta göre sırala ve boyutları GB cinsinden göster:

```bash
npkill -d '~/more projects' -gb --sort size --target vendor
```

- _projects_ dizininizdeki **node_modules** klasörlerini listeleyin, ancak _progress_ ve _ignore-this_ dizinlerindeki klasörleri hariç tutun:

```bash
npkill -d 'projects' --exclude "progress, ignore-this"
```

- Yedeklerinize gizlice karışmış tüm node_modules klasörlerini otomatik olarak silin:

```bash
npkill -d ~/backups/ --delete-all
```

<a name="setup-locally"></a>

# :pager: Yerel Kurulum

```bash
# -- Öncelikle, repoyu klonlayın.
git clone https://github.com/voidcosmos/npkill.git

# -- Dizin içine gidin
cd npkill

# -- Bağımlılıkları yükleyin
npm install

# -- Ve çalıştırın!
npm run start


# -- Eğer bazı parametrelerle çalıştırmak istiyorsanız, aşağıdaki örnekte olduğu gibi "--" eklemeniz gerekir:
npm run start -- -f -e
```

<a name="roadmap"></a>

# :crystal_ball: Yol Haritası

- [x] 0.1.0 yayınla!
- [x] Kodu geliştir
  - [x] Performansı iyileştir
  - [ ] Performansı daha da iyileştir!
- [x] Sonuçları boyuta ve yola göre sırala
- [x] Diğer türde dizinlerin (hedeflerin) aranmasına izin ver
- [ ] Daha minimalist bir modül olması için bağımlılıkları azalt
- [ ] Belirli bir süredir kullanılmayan dizinlere göre filtreleme yapmaya izin ver
- [ ] Dizinleri ağaç biçiminde göstermek için bir seçenek oluştur
- [x] Bazı menüler ekle
- [x] Log servisi ekle
- [ ] Periyodik ve otomatik temizlik (?)

<a name="known-bugs"></a>

# :bug: Bilinen Hatalar :bug:

- Bazen klasör silinirken CLI kilitlenebilir.
- TTY kullanmayan bazı terminaller (örneğin Windows’taki Git Bash) çalışmaz.
- Özellikle yol (path) bazında sıralama, çok sayıda olduğunda terminali yavaşlatabilir.
- Bazen, boyut hesaplamaları olması gerekenden daha yüksek çıkabilir.
- (ÇÖZÜLDÜ) Yüksek seviyeli dizinlerden (örneğin Linux'taki / dizini) arama yaparken performans sorunları yaşanabilir.
- (ÇÖZÜLDÜ) Bazen CLI güncellenirken metinler bozuluyor.
- (ÇÖZÜLDÜ) Dizinlerin boyutunu analiz etmek olması gerekenden daha uzun sürüyor.

> Eğer herhangi bir hata bulursanız, çekinmeden bir issue açın :)

<a name="contributing"></a>

# :revolving_hearts: Katkıda Bulunma

Katkıda bulunmak isterseniz [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md) dosyasını inceleyin.

<a name="donations"></a>

# :coffee: Bize bir kahve ısmarlayın

<img align="right" width="300" src="https://npkill.js.org/img/cat-donation-cup.png">
Boş zamanlarımızda, programlama sektörüne olan tutkumuz nedeniyle npkill'i geliştirdik.
Gelecekte, tamamen buna odaklanmak istiyoruz ama önümüzde uzun bir yol var.

Yine de işlerimizi yapmaya devam edeceğiz, ancak bağışlar yaptığımız işi desteklemenin birçok yolundan sadece biridir.

<span class="badge-opencollective"><a href="https://opencollective.com/npkill/contribute" title="Donate to this project using Open Collective"><img src="https://img.shields.io/badge/open%20collective-donate-green.svg" alt="Open Collective donate button" /></a></span>

### Teşekkürler!!

## Destekçilerimize kocaman teşekkürler :heart:

<a href="https://opencollective.com/npkill#backers" target="_blank"><img width="535" src="https://opencollective.com/npkill/tiers/backer.svg?width=535"></a>

---

### Kripto alternatifi

- btc: 1ML2DihUoFTqhoQnrWy4WLxKbVYkUXpMAX
- bch: 1HVpaicQL5jWKkbChgPf6cvkH8nyktVnVk
- eth: 0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259

<a name="license"></a>

# :scroll: Lisans

MIT © [Nya García Gallardo](https://github.com/NyaGarcia) and [Juan Torres Gómez](https://github.com/zaldih)

:cat::baby_chick:

---
```

## File: `eslint.config.mjs`
```
// @ts-check

import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import nodePlugin from 'eslint-plugin-n';
import pluginPromise from 'eslint-plugin-promise';
import eslintConfigPrettier from 'eslint-config-prettier/flat';

export default tseslint.config(
  eslint.configs.recommended,
  tseslint.configs.recommended,
  nodePlugin.configs['flat/recommended'],
  pluginPromise.configs['flat/recommended'],
  eslintConfigPrettier,
  {
    ignores: [
      'node_modules',
      'lib',
      'dist',
      'build',
      '**/*.min.js',
      '/src/index.ts',
    ],
    rules: {
      quotes: ['error', 'single'],
    },
  },
);
```

## File: `jest.config.ts`
```typescript
import type { JestConfigWithTsJest } from 'ts-jest';

const config: JestConfigWithTsJest = {
  preset: 'ts-jest/presets/default-esm',
  testEnvironment: 'node',
  extensionsToTreatAsEsm: ['.ts'],
  testRegex: '(/tests/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?)$',
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
  moduleNameMapper: {
    '^(\\.{1,2}/.*)\\.js$': '$1',
  },
  // moduleNameMapper: {
  //   '^@core/(.*)$': '<rootDir>/src/$1',
  //   '^@services/(.*)$': '<rootDir>/src/services/$1',
  //   '^@interfaces/(.*)$': '<rootDir>/src/interfaces/$1',
  //   '^@constants/(.*)$': '<rootDir>/src/constants/$1',
  // },
  // transform: {
  //   '^.+\\.(t|j)sx?$': ['ts-jest', { useESM: true }],
  // },
  transform: {
    '^.+\\.(t|j)sx?$': ['ts-jest', { useESM: true }],
  },
  testPathIgnorePatterns: ['<rootDir>/.stryker*'],
};

export default config;
```

## File: `package.json`
```json
{
  "name": "npkill",
  "version": "0.12.2",
  "description": "List any node_modules directories in your system, as well as the space they take up. You can then select which ones you want to erase to free up space.",
  "exports": "./lib/index.js",
  "type": "module",
  "engines": {
    "node": ">=18.18.0"
  },
  "publishConfig": {
    "access": "public"
  },
  "bin": {
    "npkill": "lib/index.js"
  },
  "author": "Nya Garcia & Juan Torres",
  "repository": {
    "type": "git",
    "url": "https://github.com/zaldih/npkill"
  },
  "license": "MIT",
  "keywords": [
    "cli",
    "free up space",
    "npm",
    "node",
    "modules",
    "clean",
    "tool",
    "delete",
    "find",
    "interactive"
  ],
  "files": [
    "lib/**/*"
  ],
  "scripts": {
    "build": "tsc",
    "start": "node -r tsconfig-paths/register --loader ts-node/esm --no-warnings ./src/index.ts",
    "test": "node --experimental-vm-modules --experimental-modules node_modules/jest/bin/jest.js",
    "test:watch": "npm run test -- --watch",
    "test:mutant": "stryker run",
    "release": "npm run build && np",
    "debug": "TS_NODE_FILES=true node --inspect -r ts-node/register ./src/index.ts",
    "prepare": "husky install",
    "format": "prettier --write .",
    "lint": "eslint"
  },
  "dependencies": {
    "ansi-escapes": "7.1.1",
    "open-file-explorer": "1.0.2",
    "picocolors": "1.1.1"
  },
  "devDependencies": {
    "@commitlint/config-conventional": "20.0.0",
    "@eslint/js": "9.38.0",
    "@jest/globals": "30.2.0",
    "@stryker-mutator/core": "9.2.0",
    "@stryker-mutator/jest-runner": "9.2.0",
    "@types/jest": "30.0.0",
    "@types/node": "18.18.0",
    "commitlint": "20.1.0",
    "del": "8.0.1",
    "eslint": "9.38.0",
    "eslint-config-prettier": "10.1.8",
    "eslint-plugin-n": "17.23.1",
    "eslint-plugin-promise": "7.2.1",
    "husky": "9.1.7",
    "jest": "30.2.0",
    "lint-staged": "15.5.2",
    "np": "10.2.0",
    "prettier": "3.6.2",
    "rimraf": "5.0.10",
    "ts-jest": "29.4.5",
    "ts-node": "10.9.2",
    "tslint": "6.1.3",
    "typescript": "5.8.3",
    "typescript-eslint": "8.46.2"
  },
  "peerDependencies": {
    "rxjs": "^7.8.2"
  },
  "husky": {
    "hooks": {
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS",
      "pre-commit": "lint-staged"
    }
  },
  "commitlint": {
    "extends": [
      "@commitlint/config-conventional"
    ]
  },
  "lint-staged": {
    "*.{js,ts,css,json,md}": [
      "prettier --write"
    ]
  },
  "ethereum": "0x7668e86c8bdb52034606db5aa0d2d4d73a0d4259"
}
```

## File: `stryker.conf.js`
```javascript
/**
 * @type {import('@stryker-mutator/api/core').StrykerOptions}
 */
const config = {
  packageManager: 'npm',
  reporters: ['html', 'clear-text', 'progress'],
  testRunner: 'command',
  coverageAnalysis: 'off',
  concurrency: 4,
  commandRunner: {
    command:
      'node --experimental-vm-modules --experimental-modules node_modules/jest/bin/jest.js --verbose',
  },
};
export default config;
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "esModuleInterop": true,
    "sourceMap": true,
    "module": "ESNext",
    "target": "ESNext",
    "moduleResolution": "node",
    "declaration": true,
    "rootDir": "./src/",
    "outDir": "./lib/",
    "strict": true,
    "strictFunctionTypes": true,
    "noImplicitAny": false,
    "noImplicitOverride": true,
    "strictNullChecks": true,
    "strictPropertyInitialization": false,
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "baseUrl": ".",
    "skipLibCheck": true,
    "paths": {
      "@core/*": ["src/core/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules", "__tests__"]
}
```

## File: `tslint.json`
```json
{
  "defaultSeverity": "error",
  "extends": ["tslint:recommended"],
  "jsRules": {},
  "rules": {
    "quotemark": [true, "single"],
    "member-access": [true, "no-public"],
    "arrow-parens": false,
    "no-shadowed-variable": false,
    "no-string-literal": false,
    "curly": false,
    "ordered-imports": false
  },
  "rulesDirectory": []
}
```

## File: `docs/RELEASE.md`
```markdown
# How to release a new version

### 1. Ensure the latest changes are available

```bash
git checkout develop
git pull
git checkout main
git pull
```

### 2. Merge develop into main

```bash
git merge develop --no-ff
```

### 3. Run the release script...

```bash
# Ensure that the dependencies match those in package.json
rm -rf node_modules; npm i
npm run release
```

The release script takes care of 2 things:

- Execute the compilation tasks (`npm run build`).

- Start the interactive release process itself.

### 4. Pick version type (major, minor, path)

### 5. Test the new release.
```

## File: `docs/create-demo.sh`
```bash
#!/bin/bash
#
# This script create a example node_modules files
# only for demo purpose.
#

BASE_PATH="$HOME/allStartHere"

function create(){
  projectName=$1
  fileSize=$2
  fakeModificationDate=$(expr $(date +"%s") - $(shuf -i 0-5259486 -n 1)) # 2 month of margin
  mkdir -p "$BASE_PATH/$projectName/node_modules"
  head -c ${fileSize}MB /dev/zero > "$BASE_PATH/$projectName/node_modules/a"
  touch -a -m -d @$fakeModificationDate "$BASE_PATH/$projectName/sample_npkill_file"
}


create 'secret-project' '58'
create 'Angular Tuto' '812'
create 'testest' '43'
create 'archived/Half Dead 3' '632'
create 'cats' '384'
create 'navigations/001' '89'
create 'navigations/002' '88'
create 'navigations/003' '23'
create 'more-cats' '371'
create 'projects/hero-sample' '847'
create 'projects/awesome-project' '131'
create 'projects/calculator/frontend' '883'
create 'projects/caluclator/backend' '244'
create 'games/buscaminas' '349'
create 'games/archived/cards' '185'
create 'archived/weather-api' '151'
create 'kiwis-are-awesome' '89'
create 'projects/projects-of-projects/trucs' '237'
create 'projects/projects-of-projects/conversor-divisas' '44'
create 'projects/vue/hello-world' '160'
create 'projects/vue/Quantic stuff' '44'
```

## File: `docs/json-output.md`
```markdown
# JSON Output

Npkill supports two JSON output modes that allow you to integrate it into automation scripts, monitoring systems, or other tools.

## Table of Contents

- [Output Modes](#output-modes)
- [JSON Structure](#json-structure)
- [Examples](#examples)
- [TypeScript Interfaces](#typescript-interfaces)
- [Use Cases](#use-cases)

## Output Modes

### Simple JSON (`--json`)

The `--json` option collects all results and outputs them as a single JSON object at the end of the scan. This is useful when you need all results at once for batch processing.

```bash
npkill --json
```

### Streaming JSON (`--json-stream`)

The `--json-stream` option outputs each result as a separate JSON object on its own line as soon as it's found. This is useful for real-time processing or when dealing with large scans where you want to start processing results immediately.

```bash
npkill --json-stream
```

## JSON Structure

### Simple JSON Output

The simple JSON format includes all results in a single object with metadata:

```json
{
  "version": 1,
  "results": [
    {
      "path": "/home/user/project1/node_modules",
      "size": 157286400,
      "modificationTime": 1640995200000,
      "riskAnalysis": {
        "isSensitive": false
      }
    },
    {
      "path": "/home/user/project2/node_modules",
      "size": 89478400,
      "modificationTime": 1640995300000
    }
  ],
  "meta": {
    "resultsCount": 2,
    "runDuration": 1523
  }
}
```

### Streaming JSON Output

Each line in streaming mode contains a single result:

```json
{"version":1,"result":{"path":"/home/user/project1/node_modules","size":157286400,"modificationTime":1640995200000,"riskAnalysis":{"isSensitive":false}}}
{"version":1,"result":{"path":"/home/user/project2/node_modules","size":89478400,"modificationTime":1640995300000}}
```

### Error Output

Errors are output to stderr in JSON format:

```json
{
  "version": 1,
  "error": true,
  "message": "Permission denied accessing /restricted/path",
  "timestamp": "1640995300000"
}
```

### Field Descriptions

- **`version`**: Schema version.
- **`path`**: Absolute path to the found directory.
- **`size`**: Directory size in bytes.
- **`modificationTime`**: Unix timestamp (milliseconds) of the most recently modified file.
- **`riskAnalysis`**: Optional risk assessment for deletion
  - **`isSensitive`**: Whether the directory might be important for system functionality.
  - **`reason`**: Human-readable explanation of the risk assessment.
- **`resultsCount`**: Total number of results found.
- **`runDuration`**: Total scan time in milliseconds.

## Examples

### Basic Usage

```bash
# Get all results as JSON
npkill --json > results.json

# Stream results in real-time
npkill --json-stream | while read line; do
  echo "Found: $(echo $line | jq -r '.result.path')"
done
```

### Using with jq for Processing

```bash
# Extract only paths larger than 100MB
npkill --json | jq '.results[] | select(.size > 104857600) | .path'

# Count total size of all node_modules
npkill --json | jq '.results | map(.size) | add'

# Get the 5 largest directories
npkill --json | jq '.results | sort_by(.size) | reverse | .[0:5] | .[] | "\(.size | tostring) bytes: \(.path)"'

# Convert streaming output to a valid JSON array
npkill --json-stream | jq -s 'map(.result)'
```

### Error Handling

```bash
# Save results to file, ignore errors
npkill --json 2>/dev/null > results.json

# Save both results and errors to separate files
npkill --json-stream > results.jsonl 2> errors.jsonl

# Process only successful results in streaming mode
npkill --json-stream 2>/dev/null | jq -r '.result.path'
```

### Automation Examples

```bash
# Find and delete directories older than 30 days
npkill --json | jq -r '.results[] | select(.modificationTime < (now - 2592000) * 1000) | .path' | while read dir; do
  echo "Deleting old directory: $dir"
  rm -rf "$dir"
done

# Generate a report of space usage
npkill --json | jq -r '.results[] | "\(.path): \(.size / 1048576 | floor)MB"' > space-report.txt

# Monitor in real-time and alert on large directories
npkill --json-stream | jq -r 'select(.result.size > 524288000) | "LARGE DIR: \(.result.path) (\(.result.size / 1048576 | floor)MB)"'
```

### Integration with Other Tools

```bash
# Send results to a monitoring system
npkill --json-stream | while read line; do
  curl -X POST -H "Content-Type: application/json" -d "$line" http://monitoring-system/api/npkill
done

# Create a CSV report
echo "Path,Size(MB),LastModified,Status" > report.csv
npkill --json | jq -r '.results[] | "\(.path),\(.size/1048576|floor),\(.modificationTime),\(.status)"' >> report.csv

# Filter and format for human reading
npkill --json | jq -r '.results[] | select(.size > 52428800) | "📁 \(.path)\n   💾 Size: \(.size/1048576|floor)MB\n   📅 Modified: \(.modificationTime | strftime("%Y-%m-%d %H:%M:%S"))\n"'
```

## Interfaces

```typescript
interface JsonOutputBase {
  version: number;
}

interface JsonStreamOutput extends JsonOutputBase {
  result: CliScanFoundFolder;
}

interface JsonSimpleOutput extends JsonOutputBase {
  results: CliScanFoundFolder[];
  meta: {
    resultsCount: number;
    runDuration: number; // milliseconds
  };
}

interface JsonErrorOutput extends JsonOutputBase {
  error: true;
  message: string;
  timestamp: string;
}

interface CliScanFoundFolder {
  path: string;
  size: number; // bytes
  modificationTime: number; // Unix timestamp
  riskAnalysis?: {
    isSensitive: boolean;
    reason?: string;
  };
}
```
```

## File: `docs/npkillrc.md`
```markdown
# Config File - npkillrc

You can customize the behavior of npkill through the config file (`.npkillrc` by default).

## Table of Contents

- [Location](#location)
- [Example](#example)
- [Options](#options)
  - [rootDir](#rootDir)
  - [exclude](#exclude)
  - [sortBy](#sortby)
  - [sizeUnit](#sizeunit)
  - [excludeSensitiveResults](#excludeSensitiveResults)
  - [dryRun](#dryrun)
  - [checkUpdates](#checkupdates)
  - [defaultProfiles](#defaultProfiles)
  - [profiles](#profiles)
- [Error Handling](#error-handling)
  - [Testing Your Configuration](#testing-your-configuration)

## Location

Npkill searches for the configuration file in the following order of priority:

1. **Custom path** specified via `--config` flag
2. **Current working directory**: `./.npkillrc`
3. **User's home directory**: `~/.npkillrc`

The first configuration file found will be used.

You can use `--config` in this way:

```bash
npkill --config /path/to/your/config.json
```

## Example

```json
{
  "rootDir": "/home/user/projects",
  "exclude": ["important-project", "production-app"],
  "sortBy": "size",
  "sizeUnit": "auto",
  "excludeSensitiveResults": true,
  "dryRun": false,
  "checkUpdates": true,
  "defaultProfiles": ["node", "database"],
  "profiles": {
    "webdev": {
      "description": "Frontend web development artifacts and build outputs",
      "targets": ["dist", ".next", ".nuxt", ".output", "build", ".svelte-kit"]
    },
    "mobile": {
      "description": "Mobile platform build folders and caches",
      "targets": ["Pods", "build", "DerivedData", ".gradle", "android/build"]
    },
    "database": {
      "description": "Database data folders (use with caution)",
      "targets": ["data", "db", "mongodb", "postgres"]
    }
  }
}
```

## Options

### rootDir

**Type:** `string`  
**Default:** ``

Absolute path from which the search will begin.

```json
"rootdir": "/home/user/my-projects/"
```

### exclude

**Type:** `string[]`  
**Default:** `[]`

Array of directory names to exclude from search. Npkill will skip these directories and their subdirectories.

```json
"exclude": ["production-project", "node_modules/.cache"]
```

### sortBy

**Type:** `"none" | "size" | "path" | "age"`  
**Default:** `"none"`

Default sort order for results.

- `"none"`: Results appear in the order they're found
- `"size"`: Largest folders first
- `"path"`: Alphabetical by path
- `"age"`: Oldest modified projects first

```json
"sortBy": "size"
```

### sizeUnit

**Type:** `"auto" | "mb" | "gb"`  
**Default:** `"auto"`

Unit for displaying folder sizes.

- `"auto"`: Sizes < 1024MB shown in MB, larger sizes in GB
- `"mb"`: Always show in megabytes
- `"gb"`: Always show in gigabytes

```json
"sizeUnit": "auto"
```

### excludeSensitiveResults

**Type:** `boolean`  
**Default:** `false`

Hide results that may be sensitive.

```json
"excludeSensitiveResults": true
```

### dryRun

**Type:** `boolean`  
**Default:** `false`

When true, deletions are simulated (nothing is actually deleted).

```json
"dryRun": false
```

### checkUpdates

**Type:** `boolean`  
**Default:** `true`

Check for updates on startup.

```json
"checkUpdates": true
```

### defaultProfiles

**Type:** `string[]`  
**Default:** `["node"]`

Define the profile names to be used by default. These can be either built-in or user-defined names.

```json
"checkUpdates": true
```

### profiles

**Type:** `{ [name: string]: { targets: string[] } }`  
**Default:** `{}`

Define custom profiles with specific target directories. These can be used with the `-p` or `--profiles` flag.

These will overwrite the base profiles.

You can check the existing ones with `--profiles` and even copy the output of those you are interested in to combine them into one.

```json
"profiles": {
  "webdev": {
    "description": "Frontend web development artifacts and build outputs",
    "targets": ["dist", ".next", ".nuxt", ".output"]
  },
  "mystack": {
    "description": "Full-stack project artifacts (JS/Python/Java)",
    "targets": ["venv", ".venv", "target", "__pycache__", ".gradle"]
  },
  "mobile": {
    "description": "Mobile platform build folders and caches",
    "targets": ["Pods", "build", "DerivedData", "gradle"]
  }
}
```

## Error Handling

Npkill will check that the configuration file is correct at each startup. This includes:

- **Unknown properties**.
- **Type checking**.
- **Value validation**.

### Testing Your Configuration

To test if your `.npkillrc` is valid, simply run npkill:

To check that a file is valid, simply run npkill as usual. If there is an error, you will be informed exactly what the problem is.
```

## File: `docs/profiles.md`
```markdown
# Profiles

This document defines built-in profiles for npkill. A profile is a named preset of "safe-to-delete" directories for a given ecosystem.

While these directories are **generally safe to delete**, it all depends on their context. Therefore, it is important to verify the result shown before deleting it. However, we have tried to maintain a conservative list.

- Profiles are opt-in via `--profiles` (comma-separated). Example: `--profiles node,python`.
- Only directory base names are matched (the last path segment) (more advanced heuristics will be implemented in the future).
- All targets below are rebuildable caches, dependencies, or compiled outputs. So doesnt should have any problem deleting it. But before delete, peek if is secure to remove for your case.

Default behavior

- By default (no `--profiles`), npkill use the `node` profile.

Special profile: all

- `all` includes every target listed in all profiles below. Use with care if you want a full clean sweep.

## node (default)

- `node_modules`: Node.js project dependencies. Deleting forces a full reinstallation. Regenerated by running `npm install`, `yarn`, or `pnpm install`.
- `.npm`: npm's package cache. Deleting may slow down the next install. Regenerated automatically by npm on subsequent installs.
- `.pnpm-store`: pnpm's global content-addressable store. Deleting removes all shared packages. Regenerated by pnpm on subsequent installs.
- `.yarn/cache`: Yarn v2+ local project cache. Deleting requires re-downloading packages. Regenerated by `yarn install`.
- `.next`: Next.js build and cache directory. Deleting clears build artifacts and cache. Regenerated on the next `next dev` or `next build`.
- `.nuxt`: Nuxt.js build output directory. Deleting removes the generated application. Regenerated by running `nuxt build`.
- `.angular`: Angular CLI cache and metadata. Deleting is safe and may resolve caching issues. Regenerated by the Angular CLI during the next build or serve command.
- `.svelte-kit`: SvelteKit build and cache directory. Deleting removes the generated application and cache. Regenerated on the next build or dev server run.
- `.vite`: Vite's pre-bundled dependency cache. Deleting forces Vite to re-bundle dependencies on next startup. Regenerated automatically by Vite.
- `.nx`: Nx workspace computation cache. Deleting results in a slower, non-cached build next time. Regenerated by Nx on subsequent task executions.
- `.turbo`: Turborepo's local cache. Deleting forces a full execution of all tasks on the next run. Regenerated by Turborepo on subsequent `turbo run` commands.
- `.parcel-cache`: Parcel bundler's cache. Deleting may slow down the next build. Regenerated automatically by Parcel.
- `.rpt2_cache`: Cache for `rollup-plugin-typescript2`. Deleting forces a full TypeScript re-compilation. Regenerated on the next Rollup build.
- `.eslintcache`: ESLint's cache for changed files. Deleting forces a full linting process. Regenerated by ESLint when run with the `--cache` flag.
- `.esbuild`: esbuild's build cache. Deleting may slow down builds that use esbuild. Regenerated automatically by esbuild.
- `.cache`: Generic cache directory for various tools. Deleting is generally safe but may slow down the tools that use it. Regenerated automatically by the respective tools.
- `.rollup.cache`: Rollup's build cache. Deleting may slow down the next build. Regenerated on the next Rollup build if caching is enabled.
- `storybook-static`: Static build output for a Storybook. Deleting removes the deployed Storybook. Regenerated by running `build-storybook`.
- `coverage`: Code coverage reports. Deleting removes historical coverage data. Regenerated by running tests with coverage enabled.
- `.nyc_output`: Raw coverage output from `nyc`. Deleting removes raw coverage data. Regenerated on the next run of `nyc`.
- `.jest`: Jest's test cache and artifacts. Deleting may slow down the next test run. Regenerated automatically by Jest.
- `gatsby_cache`: Gatsby's internal cache. Deleting may slow down the next build. Regenerated automatically by Gatsby.
- `.docusaurus`: Docusaurus build cache and data. Deleting removes generated site files. Regenerated by Docusaurus on the next build.
- `.swc`: SWC (Speedy Web Compiler) cache. Deleting may slow down the next compilation. Regenerated automatically by SWC.
- `.stylelintcache`: Stylelint's cache for linted files. Deleting forces a full re-lint. Regenerated by Stylelint when run with the `--cache` flag.
- `deno_cache`: Deno's cache for modules. Deleting is safe. Regenerated when Deno modules are next fetched.

## python

- `__pycache__`: Python bytecode files. Deleting is safe as they are regenerated by Python automatically.
- `.pytest_cache`: pytest's cache for test results and metadata. Deleting may slow down the next test run. Regenerated automatically by pytest.
- `.mypy_cache`: mypy's cache for type-checking results. Deleting forces a full re-check. Regenerated automatically by mypy.
- `.ruff_cache`: Ruff linter's cache. Deleting forces a full re-lint. Regenerated automatically by Ruff.
- `.tox`: tox's virtual environments and test artifacts. Deleting removes isolated testing environments. Regenerated by running `tox`.
- `.nox`: nox's virtual environments and session data. Deleting removes isolated session environments. Regenerated by running `nox`.
- `.pytype`: pytype's cache for static analysis. Deleting forces a full re-analysis. Regenerated automatically by pytype.
- `.pyre`: Pyre type checker's cache. Deleting forces a full re-check. Regenerated automatically by Pyre.
- `htmlcov`: HTML code coverage reports. Deleting removes historical coverage data. Regenerated by running coverage tools (e.g., `coverage html`).
- `.venv`: Python virtual environment. Deleting removes all installed packages and the isolated environment. Regenerated by creating a new virtual environment (e.g., `python -m venv .venv`).
- `venv`: Same as `.venv`. Deleting removes the virtual environment. Regenerated similarly.

## data-science

- `.ipynb_checkpoints`: Jupyter Notebook's auto-save checkpoints. Deleting removes recovery points for notebooks. Regenerated automatically by Jupyter.
- `__pycache__`: Python bytecode files. Deleting is safe. Regenerated automatically by Python.
- `.venv` / `venv`: Python virtual environment. Deleting removes the isolated environment and its packages. Regenerated by creating a new virtual environment.
- `outputs/`: A common directory for auto-generated files, such as models or plots. Verify contents before deleting. Regeneration depends on the specific script or tool that created it.
- `.dvc`: Data Version Control (DVC) cache and metadata. Deleting can lead to data loss if not properly managed. Regenerated by DVC commands like `dvc repro`.
- `.mlruns`: MLflow experiment tracking logs. Deleting removes experiment history. Regenerated when you run new MLflow experiments.

## java

- `target`: Maven's build output directory. Deleting removes all compiled code, packages, and artifacts. Regenerated by running `mvn package` or other Maven build commands.
- `.gradle`: Gradle's cache and wrapper files within a project. Deleting may slow down the next build. Regenerated automatically by Gradle.
- `out`: Default output directory for some IDEs like IntelliJ IDEA. Deleting removes compiled classes. Regenerated on the next build.
  - Warning: `out` is a generic folder name in various ecosystems.

## android

- `.cxx`: Android NDK build cache. Deleting may slow down native builds. Regenerated by the Android Gradle plugin during the next build.
- `externalNativeBuild`: External NDK build artifacts. Deleting removes intermediate native build files. Regenerated on the next native build.

## swift

- `DerivedData`: Xcode's build artifacts, indexes, and cache. Deleting is a common troubleshooting step and clears the build cache. Regenerated by Xcode on the next build.
- `.swiftpm`: Swift Package Manager's cache and build data. Deleting removes local package caches and build artifacts. Regenerated on the next `swift build` or resolve.

## dotnet

- `obj`: Intermediate object files from the build process. Deleting forces a full recompile. Regenerated by the .NET compiler (e.g., `dotnet build`).
- `TestResults`: Test output and reports. Deleting removes historical test data. Regenerated by running tests (e.g., `dotnet test`).
- `.vs`: Visual Studio's local workspace data, including user-specific settings and cache. Deleting is generally safe. Regenerated when you open the solution in Visual Studio.

## rust

- `target`: Cargo's build output directory. Deleting removes all compiled artifacts. Regenerated by running `cargo build`.

## ruby

- `.bundle`: Bundler's settings and cache for the project. Deleting is safe. Regenerated by `bundle install`.

## elixir

- `_build`: Mix's build output directory. Deleting removes compiled artifacts. Regenerated by `mix compile`.
- `deps`: Project dependencies. Deleting requires re-fetching all dependencies. Regenerated by `mix deps.get`.
  - Warning: `deps/` is a generic name that may appear in non-Elixir projects too.
- `cover`: Test coverage reports. Deleting removes historical coverage data. Regenerated by running tests with coverage enabled.

## haskell

- `dist-newstyle`: Cabal's build output and cache. Deleting removes compiled files. Regenerated by `cabal build`.
- `.stack-work`: Stack's build cache and artifacts. Deleting removes compiled files and intermediate data. Regenerated by `stack build`.

## scala

- `.bloop`: Bloop build server's metadata and configuration. Deleting may require re-importing the project in your IDE. Regenerated by Bloop.
- `.metals`: Metals IDE's cache and build data. Deleting forces a re-index of the project. Regenerated when you open the project in a Metals-enabled editor.
- `target`: sbt's build output directory. Deleting removes compiled code and artifacts. Regenerated by sbt build commands.

## cpp

- `CMakeFiles`: CMake's intermediate build files. Deleting forces CMake to regenerate the build environment. Regenerated by running `cmake`.
- `cmake-build-debug`: CLion or CMake's debug build output. Deleting removes debug binaries. Regenerated on the next debug build.
- `cmake-build-release`: CLion or CMake's release build output. Deleting removes release binaries. Regenerated on the next release build.

## unity

- `Library`: Unity's cache of imported assets and metadata. Deleting is safe but forces a full re-import of all project assets, which can be time-consuming. Regenerated when Unity opens the project.
  - Warning: On macOS, this can match the critical `~/Library` system folder.
- `Temp`: Temporary build files. Deleting is safe when the Unity editor is closed. Regenerated during the next build process.
- `Obj`: Intermediate object files from the build process. Deleting forces a full recompile. Regenerated on the next build.
  - Warning: Generic name; may appear in unrelated toolchains.

## unreal

- `Intermediate`: Intermediate build files. Deleting is safe and forces a regeneration of these files. Regenerated by the Unreal Engine build system.
  - Warning: Generic name; ensure it’s an Unreal project context.
- `DerivedDataCache`: Cache for derived asset data. Deleting forces assets to be re-cooked. Regenerated on demand by the engine.
- `Binaries`: Compiled binaries and libraries. Deleting removes executable files. Regenerated by the build system.

## godot

- `.import`: Godot's cache of imported assets. Deleting forces a re-import of all assets. Regenerated when the Godot editor is opened.
- `.godot`: Godot's project cache and metadata. Deleting is generally safe. Regenerated by the Godot editor.

## infra

- `.serverless`: Serverless Framework's deployment artifacts. Deleting removes the packaged service. Regenerated on the next `serverless package` or `deploy`.
- `.vercel`: Vercel's local project data and deployment cache. Deleting is safe for local development. Regenerated by the Vercel CLI.
- `.netlify`: Netlify's local cache and configuration data. Deleting is safe for local development. Regenerated by the Netlify CLI.
- `.terraform`: Terraform's working directory for providers and modules. Deleting requires re-initialization. Regenerated by running `terraform init`.
- `.sass-cache`: Legacy cache for the Sass compiler. Deleting is safe. Regenerated by the Sass compiler if still in use.
- `.cpcache`: Clojure CLI's compilation cache. Deleting forces a re-compilation of Clojure sources. Regenerated on the next execution.
- `elm_stuff`: Elm's dependency cache and build artifacts. Deleting requires re-downloading dependencies. Regenerated by `elm make` or `elm reactor`.
- `nimcache`: Nim compiler's cache. Deleting may slow down the next compilation. Regenerated automatically by the Nim compiler.
- `deno_cache`: Deno's cache for modules. Deleting is safe. Regenerated when Deno modules are next fetched.
```

## File: `src/dirname.ts`
```typescript
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const _filename = fileURLToPath(import.meta.url);
const _dirname = dirname(_filename);

export default _dirname;
```

## File: `src/index.ts`
```typescript
#!/usr/bin/env node

import { fileURLToPath } from 'url';
import main from './main.js';

// Check if npkill is called directly from the command line. If so, start the
// cli. If not, the module is being imported by another module, so don't start.
const shouldStartCli = process.argv[1] === fileURLToPath(import.meta.url);
if (shouldStartCli) {
  main();
}

export * from './core/index.js';
```

## File: `src/main.ts`
```typescript
import {
  ConsoleService,
  HttpsService,
  JsonOutputService,
  ResultsService,
  SpinnerService,
  UpdateService,
} from './cli/services/index.js';

import { CliController } from './cli/cli.controller.js';
import { UiService } from './cli/services/ui.service.js';
import { LoggerService, ConfigService, ProfilesService } from './core/index.js';
import { ScanStatus } from './core/interfaces/search-status.model.js';
import { Npkill } from './core/index.js';
import { ScanService } from './cli/services/scan.service.js';

export default (): void => {
  const logger = new LoggerService();
  const searchStatus = new ScanStatus();
  const resultsService = new ResultsService();
  const configService = new ConfigService();

  const npkill = new Npkill({ logger, searchStatus, resultsService });

  const stdOut = process.stdout;
  const jsonOutputService = new JsonOutputService(stdOut, process.stderr);

  const cli = new CliController(
    stdOut,
    npkill,
    logger,
    searchStatus,
    resultsService,
    new SpinnerService(),
    new ConsoleService(),
    new UpdateService(new HttpsService()),
    new UiService(),
    new ScanService(npkill),
    jsonOutputService,
    new ProfilesService(),
    configService,
  );

  cli.init();
};
```

## File: `src/cli/cli.controller.ts`
```typescript
import {
  ConsoleService,
  ResultsService,
  SpinnerService,
  UpdateService,
} from './services/index.js';
import {
  DEFAULT_CONFIG,
  MIN_CLI_COLUMNS_SIZE,
  UI_POSITIONS,
} from '../constants/index.js';
import { DEFAULT_PROFILE } from '../core/constants/profiles.constants.js';
import { ERROR_MSG, INFO_MSGS } from '../constants/messages.constants.js';
import { IConfig, CliScanFoundFolder, IKeyPress } from './interfaces/index.js';
import { firstValueFrom, Subject } from 'rxjs';
import { mergeMap, tap } from 'rxjs/operators';

import { COLORS } from '../constants/cli.constants.js';
import { FOLDER_SORT } from '../constants/sort.result.js';
import {
  StatusUi,
  StatsUi,
  ResultsUi,
  LogsUi,
  InteractiveUi,
  HelpCommandUi,
  HeaderUi,
  GeneralUi,
  WarningUi,
  OptionsUi,
  HelpUi,
} from './ui/index.js';
import { MENU_BAR_OPTIONS } from './ui/components/header/header-ui.constants.js';

import { UiService } from './services/ui.service.js';
import _dirname from '../dirname.js';
import pc from 'picocolors';
import { homedir } from 'os';
import path from 'path';
import openExplorer from 'open-file-explorer';
import { Npkill, ConfigService, ProfilesService } from '../core/index.js';
import { LoggerService } from '../core/services/logger.service.js';
import { ScanStatus } from '../core/interfaces/search-status.model.js';
import { isSafeToDelete } from '../utils/is-safe-to-delete.js';
import { getFileContent } from '../utils/get-file-content.js';
import { ResultDetailsUi } from './ui/components/result-details.ui.js';
import { ScanService } from './services/scan.service.js';
import { JsonOutputService } from './services/json-output.service.js';

export class CliController {
  private readonly config: IConfig = DEFAULT_CONFIG;

  private searchStart: number;
  private searchDuration: number;

  private uiHeader: HeaderUi;
  private uiGeneral: GeneralUi;
  private uiStats: StatsUi;
  private uiStatus: StatusUi;
  private uiResults: ResultsUi;
  private uiLogs: LogsUi;
  private uiWarning: WarningUi;
  private activeComponent: InteractiveUi | null = null;

  constructor(
    private readonly stdout: NodeJS.WriteStream,
    private readonly npkill: Npkill,
    private readonly logger: LoggerService,
    private readonly searchStatus: ScanStatus,
    private readonly resultsService: ResultsService,
    private readonly spinnerService: SpinnerService,
    private readonly consoleService: ConsoleService,
    private readonly updateService: UpdateService,
    private readonly uiService: UiService,
    private readonly scanService: ScanService,
    private readonly jsonOutputService: JsonOutputService,
    private readonly profilesService: ProfilesService,
    private readonly configService: ConfigService,
  ) {}

  init(): void {
    this.logger.info(`Npkill CLI started! v${this.getVersion()}`);

    this.loadConfigFile();
    this.parseArguments();

    if (this.config.jsonStream) {
      this.logger.info('JSON stream mode enabled.');
      this.setupJsonModeSignalHandlers();
      this.scan();
      return;
    }

    if (this.config.jsonSimple) {
      this.logger.info('JSON simple mode enabled.');
      this.setupJsonModeSignalHandlers();
      this.scan();
      return;
    }

    this.initUi();
    if (this.consoleService.isRunningBuild()) {
      this.uiHeader.programVersion = this.getVersion();
    }

    this.consoleService.startListenKeyEvents();
    this.checkRequirements();
    this.prepareScreen();
    this.setupEventsListener();
    if (this.config.checkUpdates) {
      this.checkVersion();
    }

    if (this.config.deleteAll && !this.config.yes) {
      this.showDeleteAllWarning();
      this.uiWarning.confirm$
        .pipe(
          tap(() => {
            this.activeComponent = this.uiResults;
            this.uiWarning.setDeleteAllWarningVisibility(false);
            this.uiService.renderAll();
            this.scan();
          }),
        )
        .subscribe();
      return;
    }

    this.scan();
  }

  private showDeleteAllWarning(): void {
    this.uiWarning.setDeleteAllWarningVisibility(true);
    this.activeComponent = this.uiWarning;
  }

  private initUi(): void {
    this.uiHeader = new HeaderUi(this.config);
    this.uiService.add(this.uiHeader);
    this.uiResults = new ResultsUi(this.resultsService, this.consoleService);
    this.uiService.add(this.uiResults);
    this.uiStats = new StatsUi(this.config, this.resultsService, this.logger);
    this.uiService.add(this.uiStats);
    this.uiStatus = new StatusUi(this.spinnerService, this.searchStatus);
    this.uiService.add(this.uiStatus);
    this.uiGeneral = new GeneralUi();
    this.uiService.add(this.uiGeneral);
    this.uiLogs = new LogsUi(this.logger);
    this.uiService.add(this.uiLogs);
    this.uiWarning = new WarningUi();
    this.uiService.add(this.uiWarning);

    // Set Events
    this.uiResults.delete$.subscribe((folder) => this.deleteFolder(folder));
    this.uiResults.showErrors$.subscribe(() => this.showErrorPopup(true));
    this.uiLogs.close$.subscribe(() => this.showErrorPopup(false));
    this.uiResults.openFolder$.subscribe((path) => openExplorer(path));
    this.uiResults.showDetails$.subscribe((folder) =>
      this.openResultsDetails(folder),
    );
    this.uiResults.endNpkill$.subscribe(() => this.quit());
    this.uiResults.goOptions$.subscribe(() => this.openOptions());
    this.uiResults.search$.subscribe((state) => {
      if (state === null) {
        this.uiHeader.setSearch(null);
      } else {
        this.uiHeader.setSearch(state.text, state.isInputActive);
      }
    });

    // Activate the main interactive component
    this.activeComponent = this.uiResults;
  }

  private openOptions(): void {
    const changeConfig$ = new Subject<Partial<IConfig>>();
    const optionsUi = new OptionsUi(changeConfig$, this.config);
    this.uiResults.clear();
    this.uiResults.setVisible(false);
    this.uiService.add(optionsUi);
    this.activeComponent = optionsUi;
    this.uiHeader.menuIndex$.next(MENU_BAR_OPTIONS.OPTIONS);
    this.uiStats.reset();
    this.uiService.renderAll();

    changeConfig$.subscribe((configChanges) => {
      Object.assign(this.config, configChanges);
      if (
        configChanges.targets ||
        configChanges.folderRoot ||
        Object.keys(configChanges).includes('excludeSensitiveResults') ||
        configChanges.exclude
      ) {
        this.scan();
      }
      if (configChanges.sortBy) {
        this.resultsService.sortResults(configChanges.sortBy);
      }
      if (configChanges.sizeUnit) {
        this.resultsService.setSizeUnit(configChanges.sizeUnit);
      }
      this.logger.info(`Config updated: ${JSON.stringify(configChanges)}`);
      this.uiService.renderAll();
    });

    optionsUi.goToHelp$.subscribe(() => {
      const helpUi = new HelpUi();
      this.uiService.add(helpUi);
      this.activeComponent = helpUi;
      optionsUi.clear();
      optionsUi.setVisible(false);
      this.uiHeader.menuIndex$.next(MENU_BAR_OPTIONS.HELP);
      this.uiStats.reset();
      this.uiService.renderAll();
      helpUi.render();
      helpUi.goToOptions$.subscribe(() => {
        helpUi.clear();
        this.activeComponent = optionsUi;
        this.uiService.remove(helpUi.id);
        optionsUi.clear();
        optionsUi.setVisible(true);
        this.uiHeader.menuIndex$.next(MENU_BAR_OPTIONS.OPTIONS);
        this.uiStats.reset();
        this.uiService.renderAll();
      });
    });

    optionsUi.goBack$.subscribe(() => {
      optionsUi.clear();
      this.activeComponent = this.uiResults;
      this.uiService.remove(optionsUi.id);
      this.uiResults.clear();
      this.uiResults.setVisible(true);
      this.uiHeader.menuIndex$.next(MENU_BAR_OPTIONS.DELETE);
      this.uiStats.reset();
      this.uiService.renderAll();
    });
  }

  private openResultsDetails(folder: CliScanFoundFolder): void {
    const detailsUi = new ResultDetailsUi(folder, this.config);
    this.uiResults.clear();
    this.uiResults.setVisible(false);

    this.uiService.add(detailsUi);
    this.activeComponent = detailsUi;
    // detailsUi.render();
    this.uiHeader.menuIndex$.next(MENU_BAR_OPTIONS.INFO);
    this.uiStats.reset();
    this.uiService.renderAll();

    detailsUi.openFolder$.subscribe((path) => openExplorer(path));
    detailsUi.goBack$.subscribe(() => {
      detailsUi.clear();
      this.activeComponent = this.uiResults;
      this.uiService.remove(detailsUi.id);
      this.uiResults.clear();
      this.uiResults.setVisible(true);
      this.uiHeader.menuIndex$.next(MENU_BAR_OPTIONS.DELETE);
      this.uiStats.reset();
      this.uiService.renderAll();
    });
  }

  private loadConfigFile(): void {
    const configPathArg = process.argv.indexOf('--config');
    const customConfigPath =
      configPathArg !== -1 ? process.argv[configPathArg + 1] : undefined;

    const result = this.configService.loadConfig(customConfigPath);

    if (result.error) {
      const isDefaultLocationNotFound =
        !customConfigPath && result.error === undefined;

      if (isDefaultLocationNotFound) {
        this.logger.info(`No config file found at ${result.configPath}`);
      } else {
        this.logger.error(`Configuration error: ${result.error}`);
        console.log(
          `${pc.red(pc.bold('Configuration Error'))} (${pc.yellow(result.configPath)})`,
        );
        console.log(pc.red(`${result.error}\n`));
        console.log(
          pc.gray(
            'Please fix the configuration file and try again.\n' +
              'For configuration reference, see: https://npkill.js.org/docs/npkillrc',
          ),
        );
        this.exitWithError();
      }
    }

    if (!result.config) {
      return;
    }

    this.logger.info(`Loaded config from ${result.configPath}`);

    if (result.config.rootDir !== undefined) {
      this.config.folderRoot = result.config.rootDir;
    }

    if (result.config.exclude !== undefined) {
      this.config.exclude = [
        ...new Set([...this.config.exclude, ...result.config.exclude]),
      ];
    }
    if (result.config.sortBy !== undefined) {
      this.config.sortBy = result.config.sortBy;
    }

    if (result.config.sizeUnit !== undefined) {
      this.config.sizeUnit = result.config.sizeUnit;
    }
    if (result.config.excludeSensitiveResults !== undefined) {
      this.config.excludeSensitiveResults =
        result.config.excludeSensitiveResults;
    }
    if (result.config.dryRun !== undefined) {
      this.config.dryRun = result.config.dryRun;
    }
    if (result.config.checkUpdates !== undefined) {
      this.config.checkUpdates = result.config.checkUpdates;
    }

    const userProfiles = this.configService.getUserDefinedProfiles(
      result.config,
    );

    const profileCount = Object.keys(userProfiles).length;

    if (profileCount > 0) {
      this.profilesService.setUserDefinedProfiles(userProfiles);
      this.logger.info(`Loaded ${profileCount} custom profile(s) from config`);
    }

    if (result.config.defaultProfiles !== undefined) {
      // Store default profiles from config to be used later if no CLI profiles are specified
      this.config.profiles = result.config.defaultProfiles;
      this.logger.info(
        `Default profiles set from config: ${result.config.defaultProfiles.join(', ')}`,
      );
    }
  }

  private parseArguments(): void {
    const options = this.consoleService.getParameters(process.argv);
    if (options.isTrue('help')) {
      this.showHelp();
      this.exitGracefully();
    }
    if (options.isTrue('version')) {
      this.showProgramVersion();
      this.exitGracefully();
    }

    if (options.isTrue('profiles') && options.isTrue('target-folders')) {
      console.log('Cannot use both --profiles and --targets options together.');
      this.exitGracefully();
    }

    if (
      options.isTrue('profiles') &&
      options.getStrings('profiles').length === 0
    ) {
      console.log(pc.bold(pc.bgYellow(pc.black(' Available profiles '))));
      console.log(
        `Remember: ${pc.bold(pc.yellow('context matters'))}. What's safe to remove in one project or ecosystem could be important in another.\n`,
      );

      const defaultProfiles =
        this.config.profiles.length > 0
          ? this.config.profiles
          : [DEFAULT_PROFILE];

      const userProfiles = this.profilesService.getProfiles('user');
      const baseProfiles = this.profilesService.getProfiles('base');

      let profilesToPrint = '';

      if (Object.keys(userProfiles).length > 0) {
        profilesToPrint += Object.entries(userProfiles).reduce(
          (acc, [name, profile]) => {
            const isDefault = defaultProfiles.includes(name);
            const entry =
              ` ${pc.green(name)}${isDefault ? pc.italic(pc.magenta(' (default)')) : ''} ${pc.cyan('(user-defined)')} - ${profile.description}\n` +
              pc.gray(` ${profile.targets.join(pc.italic(','))}\n\n`);
            return acc + entry;
          },
          '',
        );
      }

      profilesToPrint += Object.entries(baseProfiles).reduce(
        (acc, [name, profile]) => {
          const isDefault = defaultProfiles.includes(name);
          const entry =
            ` ${pc.green(name)}${isDefault ? pc.italic(pc.magenta(' (default)')) : ''} - ${profile.description}\n` +
            pc.gray(` ${profile.targets.join(pc.italic(','))}\n\n`);
          return acc + entry;
        },
        '',
      );

      console.log(profilesToPrint);
      this.exitGracefully();
    }

    if (options.isTrue('delete-all')) {
      if (!options.isTrue('target-folders') || options.isTrue('profiles')) {
        // TODO mejorar mensaje e incluir tip buscar lista targets de un profile.
        console.log('--delete-all only can be used with --targets.');
        console.log(
          'You can copy all targets from a profile with `npkill --profiles`.',
        );
        this.exitWithError();
      }
      this.config.deleteAll = true;
    }

    if (options.isTrue('sort-by')) {
      if (!this.isValidSortParam(options.getString('sort-by'))) {
        this.invalidSortParam();
      }
      this.config.sortBy = options.getString('sort-by');
    }

    const exclude = options.getString('exclude');

    if (exclude !== undefined && exclude !== '') {
      console.log('EXCLUDE', exclude);
      const userExcludeList = this.consoleService
        .splitData(this.consoleService.replaceString(exclude, '"', ''), ',')
        .map((path) => path.trim())
        .filter(Boolean)
        .map(path.normalize);

      // Add custom filters to the default exclude list.
      this.config.exclude = [...this.config.exclude, ...userExcludeList];
    }

    // Set folder root: CLI --directory takes precedence, then config rootDir, then process.cwd()
    if (options.isTrue('directory')) {
      this.config.folderRoot = options.getString('directory');
    } else if (!this.config.folderRoot) {
      // Only use process.cwd() if folderRoot wasn't set by config
      this.config.folderRoot = process.cwd();
    }

    if (options.isTrue('full-scan')) {
      this.config.folderRoot = homedir();
    }
    if (options.isTrue('hide-errors')) {
      this.config.showErrors = false;
    }
    if (options.isTrue('size-unit')) {
      const sizeUnit = options.getString('size-unit');
      if (this.isValidSizeUnit(sizeUnit)) {
        this.config.sizeUnit = sizeUnit as 'auto' | 'mb' | 'gb';
      } else {
        this.invalidSizeUnitParam();
        return;
      }
    }
    if (options.isTrue('no-check-updates')) {
      this.config.checkUpdates = false;
    }

    if (!options.isTrue('target-folders')) {
      if (!options.isTrue('profiles')) {
        // Use defaultProfiles from config if available, otherwise use DEFAULT_PROFILE
        const profilesToUse =
          this.config.profiles.length > 0
            ? this.config.profiles
            : [DEFAULT_PROFILE];

        this.logger.info(
          `Using default profile targets (${profilesToUse.join(', ')})`,
        );
        this.config.targets =
          this.profilesService.getTargetsFromProfiles(profilesToUse);
      } else {
        const selectedProfiles = options.getStrings('profiles');
        const badProfiles =
          this.profilesService.getInvalidProfileNames(selectedProfiles);

        if (badProfiles.length > 0) {
          this.logger.warn(
            `The following profiles are invalid: ${badProfiles.join(', ')}`,
          );
          const profileText = badProfiles.length > 1 ? 'profiles' : 'profile';
          console.log(pc.bold(pc.bgRed(pc.white(` Invalid ${profileText} `))));
          console.log(
            `The following ${profileText} are invalid: ${pc.red(badProfiles.join(', '))}.`,
          );
          console.log(
            `You can list the available profiles with ${pc.bold(pc.green('--profiles'))} command ${pc.gray('(without arguments)')}.`,
          );
          this.exitWithError();
        }

        const targets =
          this.profilesService.getTargetsFromProfiles(selectedProfiles);
        this.logger.info(
          `Using profiles ${selectedProfiles.join(', ')} | With targets ${targets.join(', ')}`,
        );
        this.config.profiles = selectedProfiles;
        this.config.targets = targets;
      }
    }

    if (options.isTrue('target-folders')) {
      this.config.targets = options.getString('target-folders').split(',');
      this.config.profiles = [];
    }
    if (options.isTrue('exclude-sensitive')) {
      this.config.excludeSensitiveResults = true;
    }

    if (options.isTrue('dry-run')) {
      this.config.dryRun = true;
    }

    if (options.isTrue('yes')) {
      this.config.yes = true;
    }

    if (options.isTrue('jsonStream')) {
      this.config.jsonStream = true;
    }

    if (options.isTrue('jsonSimple')) {
      this.config.jsonSimple = true;
    }

    if (this.config.jsonStream && this.config.jsonSimple) {
      this.logger.error(ERROR_MSG.CANT_USE_BOTH_JSON_OPTIONS);
      this.exitWithError();
    }

    // Remove trailing slash from folderRoot for consistency
    this.config.folderRoot = this.config.folderRoot.replace(/[/\\]$/, '');
  }

  private showErrorPopup(visible: boolean): void {
    this.uiLogs.setVisible(visible);
    // Need convert to pattern and have a stack for recover latest
    // component.
    this.uiResults.freezed = visible;
    this.uiStats.freezed = visible;
    this.uiStatus.freezed = visible;
    if (visible) {
      this.activeComponent = this.uiLogs;
      this.uiLogs.render();
    } else {
      this.activeComponent = this.uiResults;
      this.uiService.renderAll();
    }
  }

  private invalidSortParam(): void {
    this.uiService.print(INFO_MSGS.NO_VALID_SORT_NAME);
    this.logger.error(INFO_MSGS.NO_VALID_SORT_NAME);
    this.exitWithError();
  }

  private showHelp(): void {
    new HelpCommandUi(this.consoleService).show();
  }

  private showProgramVersion(): void {
    this.uiService.print('v' + this.getVersion());
  }

  private isValidColor(color: string): boolean {
    return Object.keys(COLORS).some((validColor) => validColor === color);
  }

  private isValidSortParam(sortName: string): boolean {
    return Object.keys(FOLDER_SORT).includes(sortName);
  }

  private isValidSizeUnit(sizeUnit: string): boolean {
    return ['auto', 'mb', 'gb'].includes(sizeUnit);
  }

  private invalidSizeUnitParam(): void {
    this.uiService.print(INFO_MSGS.NO_VALID_SIZE_UNIT);
    this.logger.error(INFO_MSGS.NO_VALID_SIZE_UNIT);
    this.exitWithError();
  }

  private getVersion(): string {
    const packageJson = _dirname + '/../package.json';

    const packageData = JSON.parse(getFileContent(packageJson));
    return packageData.version;
  }

  private prepareScreen(): void {
    this.uiService.setRawMode();
    // this.uiService.prepareUi();
    this.uiService.setCursorVisible(false);
    this.uiService.clear();
    this.uiService.renderAll();
  }

  private checkRequirements(): void {
    this.checkScreenRequirements();
    this.checkFileRequirements();
  }

  private checkScreenRequirements(): void {
    if (this.isTerminalTooSmall()) {
      this.uiService.print(INFO_MSGS.MIN_CLI_CLOMUNS);
      this.logger.error(INFO_MSGS.MIN_CLI_CLOMUNS);
      this.exitWithError();
    }
  }

  private checkFileRequirements(): void {
    const result = this.npkill.isValidRootFolder(this.config.folderRoot);
    if (!result.isValid) {
      const errorMessage =
        result.invalidReason || 'Root folder is not valid. Unknown reason';
      this.uiService.print(errorMessage);
      this.logger.error(errorMessage);
      this.exitWithError();
    }
  }

  private checkVersion(): void {
    this.logger.info('Checking updates...');
    this.updateService
      .isUpdated(this.getVersion())
      .then((isUpdated: boolean) => {
        if (!isUpdated) {
          this.showUpdateMessage();
          this.logger.info('New version found!');
        } else {
          this.logger.info('Npkill is update');
        }
        return isUpdated;
      })
      .catch((err: Error) => {
        const errorMessage =
          ERROR_MSG.CANT_GET_REMOTE_VERSION + ': ' + err.message;
        this.newError(errorMessage);
      });
  }

  private showUpdateMessage(): void {
    const message = pc.magenta(INFO_MSGS.NEW_UPDATE_FOUND);
    this.uiService.printAt(message, UI_POSITIONS.NEW_UPDATE_FOUND);
  }

  private isTerminalTooSmall(): boolean {
    return this.stdout.columns <= MIN_CLI_COLUMNS_SIZE;
  }

  private printFoldersSection(): void {
    this.uiResults.render();
  }

  private setupEventsListener(): void {
    this.uiService.stdin.on('keypress', (_, key: IKeyPress) => {
      if (key['name'] !== '') {
        this.keyPress(key);
      } else {
        throw new Error('Invalid key: ' + JSON.stringify(key));
      }
    });

    this.stdout.on('resize', () => {
      this.uiService.clear();
      this.uiService.renderAll();
    });

    process.on('uncaughtException', (error: Error) => {
      this.newError(error.message);
    });

    process.on('unhandledRejection', (error: Error) => {
      this.newError(error.stack ?? error.message);
    });
  }

  private keyPress(key: IKeyPress): void {
    const { name, ctrl } = key;

    if (this.isQuitKey(ctrl, name)) {
      this.quit();
    }

    if (this.activeComponent === null) {
      this.logger.error('activeComponent is NULL in Controller.');
      return;
    }

    this.activeComponent.onKeyInput(key);
  }

  private scan(): void {
    this.initializeScan();

    const shouldOutputInJson = this.config.jsonSimple || this.config.jsonStream;

    if (shouldOutputInJson) {
      this.scanInJson();
    } else {
      this.scanInUiMode();
    }
  }

  private initializeScan(): void {
    this.searchStatus.reset();
    this.resultsService.reset();
    this.resultsService.setSizeUnit(this.config.sizeUnit);
  }

  private scanInJson(): void {
    const isStreamMode = this.config.jsonStream;
    this.jsonOutputService.initializeSession(isStreamMode);

    this.scanService
      .scan(this.config)
      .pipe(
        mergeMap(
          (nodeFolder) =>
            this.scanService.calculateFolderStats(nodeFolder, {
              getModificationTimeForSensitiveResults: true,
            }),
          10, // Limit to 10 concurrent stat calculations at a time
        ),
        tap((folder) => this.jsonOutputService.processResult(folder)),
      )
      .subscribe({
        error: (error) => this.jsonOutputService.writeError(error),
        complete: () => {
          this.jsonOutputService.completeScan();
          this.exitGracefully();
        },
      });
  }

  private scanSubscription: any = null;

  private scanInUiMode(): void {
    if (this.scanSubscription) {
      this.scanSubscription.unsubscribe();
    }

    this.uiStatus.reset();
    this.uiStatus.start();
    this.searchStart = Date.now();

    this.scanSubscription = this.scanService
      .scan(this.config)
      .pipe(
        tap((nodeFolder) => this.processNodeFolderForUi(nodeFolder)),
        mergeMap(
          (nodeFolder) => this.scanService.calculateFolderStats(nodeFolder),
          10, // Limit to 10 concurrent stat calculations at a time
        ),
        tap((folder) => this.processFolderStatsForUi(folder)),
      )
      .subscribe({
        next: () => this.printFoldersSection(),
        error: (error) => this.newError(error),
        complete: () => this.completeSearch(),
      });
  }

  private setupJsonModeSignalHandlers(): void {
    const gracefulShutdown = () => {
      this.jsonOutputService.handleShutdown();
      this.exitGracefully();
    };

    process.on('SIGINT', gracefulShutdown);
    process.on('SIGTERM', gracefulShutdown);
  }

  private processNodeFolderForUi(nodeFolder: CliScanFoundFolder): void {
    this.searchStatus.newResult();
    this.resultsService.addResult(nodeFolder);

    if (this.config.sortBy === 'path') {
      this.resultsService.sortResults(this.config.sortBy);
      this.uiResults.clear();
    }

    this.uiResults.render();
  }

  private processFolderStatsForUi(folder: CliScanFoundFolder): void {
    this.searchStatus.completeStatCalculation();
    this.finishFolderStats();

    if (this.config.deleteAll) {
      this.deleteFolder(folder);
    }
  }

  private finishFolderStats(): void {
    const needSort =
      this.config.sortBy === 'size' || this.config.sortBy === 'age';
    if (needSort) {
      this.resultsService.sortResults(this.config.sortBy);
      this.uiResults.clear();
    }
    this.uiStats.render();
    this.printFoldersSection();
  }

  private completeSearch(): void {
    this.setSearchDuration();
    this.uiResults.completeSearch();
    this.uiStatus.completeSearch(this.searchDuration);
  }

  private setSearchDuration(): void {
    this.searchDuration = +((Date.now() - this.searchStart) / 1000).toFixed(2);
  }

  private isQuitKey(ctrl: boolean, name: string): boolean {
    return ctrl && name === 'c';
  }

  private exitWithError(): void {
    this.resetConsoleState();
    const logPath = this.logger.getSuggestLogFilePath();
    this.logger.saveToFile(logPath);
    // eslint-disable-next-line n/no-process-exit
    process.exit(1);
  }

  private exitGracefully(): void {
    this.resetConsoleState();
    const logPath = this.logger.getSuggestLogFilePath();
    this.logger.saveToFile(logPath);
    // eslint-disable-next-line n/no-process-exit
    process.exit(0);
  }

  private quit(): void {
    this.uiService.setRawMode(false);
    this.uiService.clear();
    this.uiService.setCursorVisible(true);
    this.printExitMessage();
    this.logger.info('Thank for using npkill. Bye!');
    const logPath = this.logger.getSuggestLogFilePath();
    this.logger.saveToFile(logPath);
    // eslint-disable-next-line n/no-process-exit
    process.exit(0);
  }

  private resetConsoleState(): void {
    this.uiService.print('\n');
    this.uiService.setRawMode(false);
    this.uiService.setCursorVisible(true);
  }

  private printExitMessage(): void {
    const { spaceReleased } = this.resultsService.getStats();
    new GeneralUi().printExitMessage({ spaceReleased });
  }

  private deleteFolder(folder: CliScanFoundFolder): void {
    if (folder.status === 'deleted' || folder.status === 'deleting') {
      return;
    }

    if (!isSafeToDelete(folder.path, this.config.targets)) {
      this.newError(`Folder not safe to delete: ${String(folder.path)}`);
      return;
    }

    folder.status = 'deleting';
    this.searchStatus.pendingDeletions++;
    this.uiStatus.render();
    this.printFoldersSection();

    firstValueFrom(
      this.npkill.delete$(String(folder.path), { dryRun: this.config.dryRun }),
    )
      .then(() => {
        folder.status = 'deleted';
        this.searchStatus.pendingDeletions--;
        this.uiStats.render();
        this.uiStatus.render();
        this.printFoldersSection();
        return folder;
      })
      .catch((e) => {
        folder.status = 'error-deleting';
        this.searchStatus.pendingDeletions--;
        this.uiStatus.render();
        this.printFoldersSection();
        this.newError(e.message);
      });
  }

  private newError(error: string): void {
    this.logger.error(error);
    this.uiStats.render();
  }
}
```

## File: `src/cli/interfaces/cli-options.interface.ts`
```typescript
export interface ICliOptions {
  arg: string[];
  name: string;
  description: string;
}
```

## File: `src/cli/interfaces/command-keys.interface.ts`
```typescript
export interface IKeysCommand {
  up: () => void;
  down: () => void;
  space: () => void;
  j: () => void;
  k: () => void;
  h: () => void;
  l: () => void;
  d: () => void;
  u: () => void;
  pageup: () => void;
  pagedown: () => void;
  home: () => void;
  end: () => void;
  e: () => void;
  execute: (command: string, params?: string[]) => number;
}
```

## File: `src/cli/interfaces/config.interface.ts`
```typescript
export interface IConfig {
  profiles: string[];
  folderRoot: string;
  checkUpdates: boolean;
  deleteAll: boolean;
  sizeUnit: 'auto' | 'mb' | 'gb';
  maxSimultaneousSearch: number;
  showErrors: boolean;
  sortBy: string;
  targets: string[];
  exclude: string[];
  excludeSensitiveResults: boolean;
  dryRun: boolean;
  yes: boolean;
  jsonStream: boolean;
  jsonSimple: boolean;
}
```

## File: `src/cli/interfaces/index.ts`
```typescript
export * from './cli-options.interface.js';
export * from './command-keys.interface.js';
export * from './config.interface.js';
export * from '@core/interfaces/file-service.interface.js';
export * from '@core/interfaces/folder.interface.js';
export * from './key-press.interface.js';
export * from './stats.interface.js';
export * from './ui-positions.interface.js';
export * from './version.interface.js';
export * from './node-version.interface.js';
export * from './json-output.interface.js';
```

## File: `src/cli/interfaces/json-output.interface.ts`
```typescript
import { CliScanFoundFolder } from './stats.interface.js';

export interface JsonOutputBase {
  version: number;
}

export interface JsonCliScanFoundFolder
  extends Omit<CliScanFoundFolder, 'status'> {}

/**
 * JSON output format for streaming mode (--json-stream).
 * Each result is output as a separate JSON object on its own line.
 */
export interface JsonStreamOutput extends JsonOutputBase {
  result: JsonCliScanFoundFolder;
}

/**
 * JSON output format for simple mode (--json).
 * All results are collected and output as a single JSON object at the end.
 */
export interface JsonSimpleOutput extends JsonOutputBase {
  results: JsonCliScanFoundFolder[];
  meta: {
    resultsCount: number;
    /** Scan duration in milliseconds */
    runDuration: number;
  };
}

export interface JsonErrorOutput extends JsonOutputBase {
  error: true;
  message: string;
  timestamp: number; // Unix timestamp in milliseconds
}
```

## File: `src/cli/interfaces/key-press.interface.ts`
```typescript
export interface IKeyPress {
  name: string;
  meta: boolean;
  ctrl: boolean;
  shift: boolean;
  sequence: string;
}
```

## File: `src/cli/interfaces/node-version.interface.ts`
```typescript
export interface INodeVersion {
  major: number;
  minor: number;
  patch: number;
}
```

## File: `src/cli/interfaces/stats.interface.ts`
```typescript
import { ScanFoundFolder } from '../../core/interfaces/index.js';

export interface CliScanFoundFolder extends ScanFoundFolder {
  size: number;
  modificationTime: number;
  status: 'live' | 'deleting' | 'error-deleting' | 'deleted';
}

export interface IResultTypeCount {
  type: string;
  count: number;
}

export interface IStats {
  spaceReleased: string;
  totalSpace: string;
  resultsTypesCount: IResultTypeCount[];
}
```

## File: `src/cli/interfaces/ui-positions.interface.ts`
```typescript
export interface IPosition {
  x: number;
  y: number;
}

export type IUiPosition = Record<string, IPosition>;
```

## File: `src/cli/interfaces/version.interface.ts`
```typescript
export interface IVersion {
  major: number;
  minor: number;
  patch: number;
}
```

## File: `src/cli/models/start-parameters.model.ts`
```typescript
export class StartParameters {
  private values: Record<string, string | boolean> = {};

  add(key: string, value: string | boolean): void {
    this.values[key] = value;
  }

  isTrue(key: string): boolean {
    const value = this.values[key];
    return value !== undefined && (value === true || value !== 'false');
  }

  getString(key: string): string {
    const value = this.values[key];
    if (typeof value === 'boolean') {
      return value.toString();
    }

    return value;
  }

  getStrings(key: string): string[] {
    const value = this.values[key];
    if (!value || typeof value === 'boolean') {
      return [];
    }

    return value.split(',').map((item) => item.trim());
  }
}
```

## File: `src/cli/services/console.service.ts`
```typescript
import { OPTIONS, WIDTH_OVERFLOW } from '../../constants/index.js';

import { ICliOptions } from '../interfaces/cli-options.interface.js';
import { extname } from 'path';
import * as readline from 'node:readline';
import { StartParameters } from '../models/start-parameters.model.js';

export class ConsoleService {
  getParameters(rawArgv: string[]): StartParameters {
    // This needs a refactor, but fck, is a urgent update
    const rawProgramArgvs = this.removeSystemArgvs(rawArgv);
    const argvs = this.normalizeParams(rawProgramArgvs);
    const options: StartParameters = new StartParameters();

    argvs.forEach((argv, index) => {
      if (!this.isArgOption(argv) || !this.isValidOption(argv)) {
        return;
      }
      const nextArgv = argvs[index + 1];
      const option = this.getOption(argv);

      if (option === undefined) {
        throw new Error('Invalid option name.');
      }

      const optionName = option.name;
      options.add(
        optionName,
        this.isArgHavingParams(nextArgv) ? nextArgv : true,
      );
    });

    return options;
  }

  splitWordsByWidth(text: string, width: number): string[] {
    const splitRegex = new RegExp(
      `(?![^\\n]{1,${width}}$)([^\\n]{1,${width}})\\s`,
      'g',
    );
    const splitText = this.replaceString(text, splitRegex, '$1\n');
    return this.splitData(splitText);
  }

  splitData(data: string, separator = '\n'): string[] {
    if (data === '') {
      return [];
    }
    return data.split(separator);
  }

  replaceString(
    text: string,
    textToReplace: string | RegExp,
    replaceValue: string,
  ): string {
    return text.replace(textToReplace, replaceValue);
  }

  shortenText(text: string, width: number, startCut = 0): string {
    if (!this.isValidShortenParams(text, width, startCut)) {
      return text;
    }

    const startPartB = text.length - (width - startCut - WIDTH_OVERFLOW.length);
    const partA = text.substring(startCut, -1);
    const partB = text.substring(startPartB, text.length);

    return partA + WIDTH_OVERFLOW + partB;
  }

  isRunningBuild(): boolean {
    return extname(import.meta.url) === '.js';
  }

  startListenKeyEvents(): void {
    readline.emitKeypressEvents(process.stdin);
  }

  /** Argvs can be specified for example by
   *  "--sort size" and "--sort=size". The main function
   *  expect the parameters as the first form so this
   *  method convert the second to first.
   */
  private normalizeParams(argvs: string[]): string[] {
    return argvs.join('=').split('=');
  }

  private isValidShortenParams(
    text: string,
    width: number,
    startCut: number,
  ): boolean {
    return (
      startCut <= width &&
      text.length >= width &&
      !this.isNegative(width) &&
      !this.isNegative(startCut)
    );
  }

  private removeSystemArgvs(allArgv: string[]): string[] {
    return allArgv.slice(2);
  }

  private isArgOption(argv: string): boolean {
    return argv.charAt(0) === '-';
  }

  private isArgHavingParams(nextArgv: string): boolean {
    return (
      nextArgv !== undefined && nextArgv !== '' && !this.isArgOption(nextArgv)
    );
  }

  private isValidOption(arg: string): boolean {
    return OPTIONS.some((option) => option.arg.includes(arg));
  }

  private getOption(arg: string): ICliOptions | undefined {
    return OPTIONS.find((option) => option.arg.includes(arg));
  }

  private isNegative(numb: number): boolean {
    return numb < 0;
  }
}
```

## File: `src/cli/services/https.service.ts`
```typescript
import * as https from 'node:https';

export class HttpsService {
  async getJson(url: string): Promise<Record<string, string>> {
    return new Promise((resolve, reject) => {
      const fail = (err: Error): void => {
        reject(err);
      };

      const request = https.get(url, (res) => {
        if (!this.isCorrectResponse(res.statusCode ?? -1)) {
          const error = new Error(res.statusMessage ?? 'Unknown error');
          fail(error);
          return;
        }

        res.setEncoding('utf8');
        let body = '';
        res.on('data', (data: string) => {
          body += data;
        });
        res.on('end', () => {
          resolve(JSON.parse(body));
        });
      });

      request.on('error', (error) => fail(error));
    });
  }

  private isCorrectResponse(statusCode: number): boolean {
    const correctRangeStart = 200;
    const correctRangeEnd = 299;
    return statusCode >= correctRangeStart && statusCode <= correctRangeEnd;
  }
}
```

## File: `src/cli/services/index.ts`
```typescript
export * from './console.service.js';
export * from './https.service.js';
export * from './results.service.js';
export * from './spinner.service.js';
export * from './update.service.js';
export * from './json-output.service.js';
export * from '../../core/services/stream.service.js';
```

## File: `src/cli/services/json-output.service.ts`
```typescript
import { CliScanFoundFolder } from '../interfaces/stats.interface.js';
import {
  JsonStreamOutput,
  JsonSimpleOutput,
  JsonErrorOutput,
  JsonCliScanFoundFolder,
} from '../interfaces/json-output.interface.js';
import { convertGbToBytes } from '../../utils/unit-conversions.js';

export class JsonOutputService {
  private readonly OUTPUT_VERSION = 1;
  private results: JsonCliScanFoundFolder[] = [];
  private scanStartTime: number = 0;
  private isStreamMode: boolean = false;

  constructor(
    private readonly stdout: NodeJS.WriteStream = process.stdout,
    private readonly stderr: NodeJS.WriteStream = process.stderr,
  ) {}

  initializeSession(streamMode: boolean = false): void {
    this.results = [];
    this.scanStartTime = Date.now();
    this.isStreamMode = streamMode;
  }

  processResult(folder: CliScanFoundFolder): void {
    if (this.isStreamMode) {
      this.writeStreamResult(folder);
    } else {
      this.addResult(folder);
    }
  }

  completeScan(): void {
    if (!this.isStreamMode && this.results.length > 0) {
      this.writeSimpleResults();
    }
  }

  private writeStreamResult(folder: CliScanFoundFolder): void {
    const output: JsonStreamOutput = {
      version: this.OUTPUT_VERSION,
      result: this.sanitizeFolderForOutput(folder),
    };

    try {
      this.stdout.write(JSON.stringify(output) + '\n');
    } catch (error) {
      const errorMessage =
        error instanceof Error
          ? error.message
          : 'Unknown JSON serialization error';
      this.writeError(`Failed to serialize result to JSON: ${errorMessage}`);
    }
  }

  private addResult(folder: CliScanFoundFolder): void {
    this.results.push(this.sanitizeFolderForOutput(folder));
  }

  private writeSimpleResults(): void {
    const runDuration = Date.now() - this.scanStartTime;
    const output: JsonSimpleOutput = {
      version: this.OUTPUT_VERSION,
      results: this.results,
      meta: {
        resultsCount: this.results.length,
        runDuration,
      },
    };

    try {
      this.stdout.write(JSON.stringify(output, null, 2) + '\n');
    } catch (error) {
      const errorMessage =
        error instanceof Error
          ? error.message
          : 'Unknown JSON serialization error';
      this.writeError(`Failed to serialize results to JSON: ${errorMessage}`);
    }
  }

  writeError(error: Error | string): void {
    const errorMessage = error instanceof Error ? error.message : error;
    const errorOutput: JsonErrorOutput = {
      version: this.OUTPUT_VERSION,
      error: true,
      message: errorMessage,
      timestamp: new Date().getDate(),
    };

    this.stderr.write(JSON.stringify(errorOutput) + '\n');
  }

  getResultsCount(): number {
    return this.results.length;
  }

  handleShutdown(): void {
    if (!this.isStreamMode && this.results.length > 0) {
      this.writeSimpleResults();
    }
  }

  private sanitizeFolderForOutput(
    folder: CliScanFoundFolder,
  ): JsonCliScanFoundFolder {
    return {
      path: folder.path,
      size: convertGbToBytes(folder.size),
      modificationTime: folder.modificationTime,
      riskAnalysis: folder.riskAnalysis
        ? {
            isSensitive: folder.riskAnalysis.isSensitive,
            reason: folder.riskAnalysis.reason,
          }
        : undefined,
    };
  }
}
```

## File: `src/cli/services/results.service.ts`
```typescript
import {
  CliScanFoundFolder,
  IStats,
  IResultTypeCount,
} from '../interfaces/index.js';
import { FOLDER_SORT } from '../../constants/sort.result.js';
import { formatSize } from '../../utils/unit-conversions.js';
import path from 'path';

export class ResultsService {
  results: CliScanFoundFolder[] = [];
  private sizeUnit: 'auto' | 'mb' | 'gb' = 'auto';

  addResult(result: CliScanFoundFolder): void {
    this.results = [...this.results, result];
  }

  sortResults(method: string): void {
    this.results = this.results.sort(FOLDER_SORT[method]);
  }

  reset(): void {
    this.results = [];
  }

  setSizeUnit(sizeUnit: 'auto' | 'mb' | 'gb'): void {
    this.sizeUnit = sizeUnit;
  }

  getStats(): IStats {
    let spaceReleased = 0;
    const typeCounts = new Map<string, number>();

    const totalSpace = this.results.reduce((total, folder) => {
      if (folder.status === 'deleted') {
        spaceReleased += folder.size;
      }

      const folderType = path.basename(folder.path);
      typeCounts.set(folderType, (typeCounts.get(folderType) || 0) + 1);

      return total + folder.size;
    }, 0);

    const formattedTotal = formatSize(totalSpace, this.sizeUnit);
    const formattedReleased = formatSize(spaceReleased, this.sizeUnit);

    const resultsTypesCount: IResultTypeCount[] = Array.from(
      typeCounts.entries(),
    )
      .map(([type, count]) => ({ type, count }))
      .sort((a, b) => {
        if (b.count !== a.count) {
          return b.count - a.count;
        }
        return a.type.localeCompare(b.type);
      });

    return {
      spaceReleased: formattedReleased.text,
      totalSpace: formattedTotal.text,
      resultsTypesCount,
    };
  }
}
```

## File: `src/cli/services/scan.service.ts`
```typescript
import { Npkill } from '@core/npkill';
import {
  CliScanFoundFolder,
  IConfig,
  ScanFoundFolder,
  ScanOptions,
  SortBy,
} from '../interfaces';
import {
  Observable,
  filter,
  firstValueFrom,
  map,
  switchMap,
  tap,
  catchError,
  of,
  timeout,
} from 'rxjs';
import { convertBytesToGb } from '../../utils/unit-conversions.js';
import { join } from 'path';
import os from 'os';

export interface CalculateFolderStatsOptions {
  getModificationTimeForSensitiveResults: boolean;
}

export class ScanService {
  constructor(private readonly npkill: Npkill) {}

  scan(config: IConfig): Observable<CliScanFoundFolder> {
    const { targets, exclude, sortBy } = config;

    const params: ScanOptions = {
      targets,
      exclude,
      performRiskAnalysis: true,
      sortBy: sortBy as SortBy,
    };

    const results$ = this.npkill.startScan$(config.folderRoot, params);
    const nonExcludedResults$ = results$.pipe(
      filter(
        (path) =>
          !this.isExcludedDangerousDirectory(
            path,
            config.excludeSensitiveResults,
          ),
      ),
    );

    return nonExcludedResults$.pipe(
      map<ScanFoundFolder, CliScanFoundFolder>(({ path, riskAnalysis }) => ({
        path,
        size: 0,
        modificationTime: -1,
        riskAnalysis,
        status: 'live',
      })),
    );
  }

  calculateFolderStats(
    nodeFolder: CliScanFoundFolder,
    options: CalculateFolderStatsOptions = {
      /** Saves resources by not scanning a result that is probably not of interest. */
      getModificationTimeForSensitiveResults: false,
    },
  ): Observable<CliScanFoundFolder> {
    return this.npkill.getSize$(nodeFolder.path).pipe(
      timeout(30000), // 30 seconds timeout
      catchError(() => {
        // If size calculation fails or times out, keep size as 0 but mark as calculated
        nodeFolder.size = 0;
        nodeFolder.modificationTime = 1; // 1 = calculated, -1 = not calculated
        return of({ size: 0, unit: 'bytes' as const });
      }),
      tap(({ size }) => {
        nodeFolder.size = convertBytesToGb(size);
      }),
      switchMap(async () => {
        if (
          nodeFolder.riskAnalysis?.isSensitive &&
          !options.getModificationTimeForSensitiveResults
        ) {
          nodeFolder.modificationTime = -1;
          return nodeFolder;
        }

        const parentFolder = join(nodeFolder.path, '../');
        const normalizedParent = parentFolder.replace(/\\/g, '/').toLowerCase();
        const normalizedHome = os.homedir().replace(/\\/g, '/').toLowerCase();

        const isDirectChildOfHome =
          normalizedHome && normalizedParent === normalizedHome;

        // If it's directly under HOME, skip modification time calculation
        if (isDirectChildOfHome) {
          nodeFolder.modificationTime = -1;
          return nodeFolder;
        }

        // For other folders, scan the parent folder for modification time
        try {
          const result = await firstValueFrom(
            this.npkill.getNewestFile$(parentFolder).pipe(
              timeout(10000), // 10 seconds timeout for modification time
              catchError(() => of(null)),
            ),
          );

          nodeFolder.modificationTime = result ? result.timestamp : 1;
          return nodeFolder;
        } catch {
          nodeFolder.modificationTime = 1;
          return nodeFolder;
        }
      }),
      catchError(() => {
        // Final fallback: mark as calculated with default values
        nodeFolder.modificationTime = 1;
        if (nodeFolder.size === undefined || nodeFolder.size === null) {
          nodeFolder.size = 0;
        }
        return of(nodeFolder);
      }),
    );
  }

  private isExcludedDangerousDirectory(
    scanResult: ScanFoundFolder,
    excludeSensitiveResults: boolean,
  ): boolean {
    return Boolean(
      excludeSensitiveResults && scanResult.riskAnalysis?.isSensitive,
    );
  }
}
```

## File: `src/cli/services/spinner.service.ts`
```typescript
export class SpinnerService {
  private spinner: string[] = [];
  private count = -1;

  setSpinner(spinner: string[]): void {
    this.spinner = spinner;
    this.reset();
  }

  nextFrame(): string {
    this.updateCount();
    return this.spinner[this.count];
  }

  reset(): void {
    this.count = -1;
  }

  private updateCount(): void {
    if (this.isLastFrame()) {
      this.count = 0;
    } else {
      ++this.count;
    }
  }

  private isLastFrame(): boolean {
    return this.count === this.spinner.length - 1;
  }
}
```

## File: `src/cli/services/ui.service.ts`
```typescript
import ansiEscapes from 'ansi-escapes';
import { Position, BaseUi } from '../ui/index.js';

export class UiService {
  stdin: NodeJS.ReadStream = process.stdin;
  // public stdout: NodeJS.WriteStream = process.stdout;
  uiComponents: BaseUi[] = [];

  setRawMode(set = true): void {
    if (this.stdin.isTTY) {
      this.stdin.setRawMode(set);
    }
    process.stdin.resume();
  }

  setCursorVisible(visible: boolean): void {
    const instruction = visible
      ? ansiEscapes.cursorShow
      : ansiEscapes.cursorHide;
    this.print(instruction);
  }

  add(component: BaseUi): void {
    this.uiComponents.push(component);
  }

  remove(baseUiId: string): void {
    this.uiComponents = this.uiComponents.filter((c) => c.id !== baseUiId);
  }

  renderAll(): void {
    this.clear();
    this.uiComponents.forEach((component) => {
      if (component.visible) {
        component.render();
      }
    });
  }

  setFreezeAll(freeze: boolean): void {
    this.uiComponents.forEach((component) => {
      component.freezed = freeze;
    });
  }

  setVisibleAll(visible: boolean): void {
    this.uiComponents.forEach((component) => {
      component.setVisible(visible);
    });
  }

  clear(): void {
    this.print(ansiEscapes.clearTerminal);
  }

  print(text: string): void {
    process.stdout.write.bind(process.stdout)(text);
  }

  printAt(message: string, position: Position): void {
    this.setCursorAt(position);
    this.print(message);
  }

  setCursorAt({ x, y }: Position): void {
    this.print(ansiEscapes.cursorTo(x, y));
  }

  clearLine(row: number): void {
    this.printAt(ansiEscapes.eraseLine, { x: 0, y: row });
  }
}
```

## File: `src/cli/services/update.service.ts`
```typescript
import {
  VERSION_CHECK_DIRECTION,
  VERSION_KEY,
} from '../../constants/update.constants.js';

import { HttpsService } from './https.service.js';

export class UpdateService {
  constructor(private readonly httpsService: HttpsService) {}

  /**
   * Check if localVersion is greater or equal to remote version
   * ignoring the pre-release tag. ex: 1.3.12 = 1.3.12-21
   */
  async isUpdated(localVersion: string): Promise<boolean> {
    const removePreReaseTag = (value: string): string => value.split('-')[0];

    const localVersionPrepared = removePreReaseTag(localVersion);
    const remoteVersion = await this.getRemoteVersion();
    const remoteVersionPrepared = removePreReaseTag(remoteVersion);
    return this.compareVersions(localVersionPrepared, remoteVersionPrepared);
  }

  private compareVersions(local: string, remote: string): boolean {
    return (
      this.isSameVersion(local, remote) ||
      this.isLocalVersionGreater(local, remote)
    );
  }

  private async getRemoteVersion(): Promise<string> {
    const response = await this.httpsService.getJson(VERSION_CHECK_DIRECTION);
    return response[VERSION_KEY];
  }

  private isSameVersion(version1: string, version2: string): boolean {
    return version1 === version2;
  }

  /** Valid to compare versions up to 99999.99999.99999 */
  private isLocalVersionGreater(local: string, remote: string): boolean {
    const leadingZeros = (value: string): string =>
      ('00000' + value).substring(-5);

    const localLeaded = +local.split('.').map(leadingZeros).join('');
    const remoteLeaded = +remote.split('.').map(leadingZeros).join('');

    return localLeaded >= remoteLeaded;
  }
}
```

## File: `src/cli/ui/base.ui.ts`
```typescript
import { IKeyPress } from '../interfaces/index.js';
import ansiEscapes from 'ansi-escapes';

export interface Position {
  x: number;
  y: number;
}

export interface InteractiveUi {
  onKeyInput: (key: IKeyPress) => void;
}

export abstract class BaseUi {
  public readonly id = Math.random().toString(36).substring(2, 10);
  public freezed = false;
  protected _position: Position;
  protected _visible = true;
  private readonly stdout: NodeJS.WriteStream = process.stdout;

  protected printAt(message: string, position: Position): void {
    this.setCursorAt(position);
    this.print(message);
  }

  protected setCursorAt({ x, y }: Position): void {
    this.print(ansiEscapes.cursorTo(x, y));
  }

  protected print(text: string): void {
    if (this.freezed) {
      return;
    }
    process.stdout.write.bind(process.stdout)(text);
  }

  protected clearLine(row: number): void {
    this.printAt(ansiEscapes.eraseLine, { x: 0, y: row });
  }

  setPosition(position: Position, renderOnSet = true): void {
    this._position = position;

    if (renderOnSet) {
      this.render();
    }
  }

  setVisible(visible: boolean, renderOnSet = true): void {
    this._visible = visible;

    if (renderOnSet) {
      this.render();
    }
  }

  get position(): Position {
    return this._position;
  }

  get visible(): boolean {
    return this._visible;
  }

  get terminal(): { columns: number; rows: number } {
    return {
      columns: this.stdout.columns,
      rows: this.stdout.rows,
    };
  }

  abstract render(): void;
}
```

## File: `src/cli/ui/heavy.ui.ts`
```typescript
import { BaseUi } from './base.ui.js';

/**
 * A UI that buffers the output and prints it all at once when calling the
 * flush() function.
 */
export abstract class HeavyUi extends BaseUi {
  private buffer = '';
  private previousBuffer = '';

  resetBufferState(): void {
    this.buffer = '';
    this.previousBuffer = '';
  }

  /**
   * Stores the text in a buffer. No will print it to stdout until flush()
   * is called.
   */
  protected override print(text: string): void {
    this.buffer += text;
  }

  /** Prints the buffer (if have any change) to stdout and clears it. */
  protected flush(): void {
    if (this.freezed) {
      return;
    }

    if (this.buffer === this.previousBuffer) {
      this.clearBuffer();
      return;
    }

    process.stdout.write.bind(process.stdout)(this.buffer);
    this.clearBuffer();
  }

  private clearBuffer(): void {
    this.previousBuffer = this.buffer;
    this.buffer = '';
  }
}
```

## File: `src/cli/ui/index.ts`
```typescript
export * from './base.ui.js';
export * from './heavy.ui.js';
export * from './components/general.ui.js';
export * from './components/help/help.ui.js';
export * from './components/help/help-command.ui.js';
export * from './components/logs.ui.js';
export * from './components/warning.ui.js';
export * from './components/results.ui.js';
export * from './components/header/header.ui.js';
export * from './components/header/stats.ui.js';
export * from './components/header/status.ui.js';
export * from './components/header/status.ui.js';
export * from './components/options.ui.js';
```

## File: `src/cli/ui/components/general.ui.ts`
```typescript
// This class in only a intermediate for the refactor.

import { BaseUi } from '../base.ui.js';
import pc from 'picocolors';

export class GeneralUi extends BaseUi {
  render(): void {}

  printExitMessage(stats: { spaceReleased: string }): void {
    const { spaceReleased } = stats;
    let exitMessage = `Space saved: ${spaceReleased}\n`;
    exitMessage += pc.dim(
      'Thanks for using npkill!\nLike it? Give us a star http://github.com/voidcosmos/npkill\n',
    );
    this.print(exitMessage);
  }
}
```

## File: `src/cli/ui/components/logs.ui.ts`
```typescript
import { LoggerService } from '@core/services/logger.service.js';
import { InteractiveUi, BaseUi } from '../base.ui.js';
import pc from 'picocolors';
import { IPosition } from '../../interfaces/ui-positions.interface.js';
import { Subject } from 'rxjs';
import { IKeyPress } from '../../interfaces/key-press.interface.js';

export class LogsUi extends BaseUi implements InteractiveUi {
  readonly close$ = new Subject<null>();
  private size: IPosition;
  private errors = 0;
  private pages: string[][] = [];
  private actualPage = 0;

  private readonly KEYS = {
    e: () => this.cyclePages(),
    escape: () => this.close(),
  };

  constructor(private readonly logger: LoggerService) {
    super();
    this.setVisible(false, false);
  }

  onKeyInput({ name }: IKeyPress): void {
    const action = this.KEYS[name];
    if (action === undefined) {
      return;
    }
    action();
  }

  render(): void {
    this.renderPopup();
  }

  private cyclePages(): void {
    this.actualPage++;
    if (this.actualPage >= this.pages.length) {
      this.actualPage = 0;
      this.close();
      return;
    }

    this.render();
  }

  private close(): void {
    this.close$.next(null);
  }

  private renderPopup(): void {
    this.calculatePosition();
    for (let x = this.position.x; x < this.size.x; x++) {
      for (let y = this.position.y; y < this.size.y; y++) {
        let char = ' ';
        if (x === this.position.x || x === this.size.x - 1) {
          char = '│';
        }
        if (y === this.position.y) {
          char = '═';
        }
        if (y === this.size.y - 1) {
          char = '─';
        }
        if (x === this.position.x && y === this.position.y) {
          char = '╒';
        }
        if (x === this.size.x - 1 && y === this.position.y) {
          char = '╕';
        }
        if (x === this.position.x && y === this.size.y - 1) {
          char = '╰';
        }
        if (x === this.size.x - 1 && y === this.size.y - 1) {
          char = '╯';
        }

        this.printAt(pc.bgBlack(char), { x, y });
      }
    }

    const width = this.size.x - this.position.x - 2;
    const maxEntries = this.size.y - this.position.y - 2;

    const messagesByLine: string[] = this.logger
      .get('error')
      .map((entry, index) => `${index}. ${entry.message}`)
      .reduce((acc: string[], line) => {
        acc = [...acc, ...this.chunkString(line, width)];
        return acc;
      }, []);

    this.pages = this.chunkArray(messagesByLine, maxEntries);
    this.errors = this.logger.get('error').length;

    if (messagesByLine.length === 0) {
      this.printAt(this.stylizeText('No errors!'), {
        x: this.position.x + 1,
        y: this.position.y + 1,
      });
    }

    this.pages[this.actualPage].forEach((entry, index) => {
      this.printAt(this.stylizeText(entry, 'error'), {
        x: this.position.x + 1,
        y: this.position.y + 1 + index,
      });
    });

    this.printHeader();
  }

  private printHeader(): void {
    const titleText = ' Errors ';
    this.printAt(this.stylizeText(titleText), {
      x: Math.floor((this.size.x + titleText.length / 2) / 2) - this.position.x,
      y: this.position.y,
    });

    const rightText = ` ${this.errors} errors | Page ${this.actualPage + 1}/${
      this.pages.length
    } `;

    this.printAt(this.stylizeText(rightText), {
      x: Math.floor(this.size.x + this.position.x - 4 - (rightText.length + 2)),
      y: this.position.y,
    });
  }

  private stylizeText(
    text: string,
    style: 'normal' | 'error' = 'normal',
  ): string {
    const styles = { normal: 'white', error: 'red' };
    const color = styles[style];
    return pc[color](pc.bgBlack(text));
  }

  private chunkString(str: string, length: number): string[] {
    const matches = str.match(new RegExp(`.{1,${length}}`, 'g'));
    return matches !== null ? [...matches] : [];
  }

  private chunkArray(arr: string[], size: number): string[][] {
    return arr.length > size
      ? [arr.slice(0, size), ...this.chunkArray(arr.slice(size), size)]
      : [arr];
  }

  private calculatePosition(): void {
    const posX = 5;
    const posY = 4;
    this.setPosition({ x: posX, y: posY }, false);
    this.size = {
      x: this.terminal.columns - posX,
      y: this.terminal.rows - 3,
    };
  }
}
```

## File: `src/cli/ui/components/options.ui.ts`
```typescript
import { MARGINS } from '../../../constants/main.constants.js';
import { BaseUi, InteractiveUi } from '../base.ui.js';
import { IKeyPress } from '../../interfaces/key-press.interface.js';
import { Subject } from 'rxjs';
import pc from 'picocolors';
import path from 'path';
import { existsSync } from 'fs';
import { IConfig } from '../../../cli/interfaces/config.interface.js';
import { OPTIONS_HINTS_BY_TYPE } from '../../../constants/options.constants.js';

type OptionType = 'checkbox' | 'dropdown' | 'input';

interface OptionItem<K extends keyof IConfig = keyof IConfig> {
  label: string;
  type: OptionType;
  key: K;
  value: IConfig[K];
  options?: string[]; // dropdown options
}

export class OptionsUi extends BaseUi implements InteractiveUi {
  resultIndex = 0;
  readonly goBack$ = new Subject<null>();
  readonly goToHelp$ = new Subject<null>();
  private readonly config: IConfig;

  private selectedIndex = 0;
  private isEditing = false;
  private editBuffer = '';

  private options: OptionItem[];

  private readonly KEYS: Record<string, () => void> = {
    up: () => this.move(-1),
    down: () => this.move(1),
    k: () => this.move(-1),
    j: () => this.move(1),
    return: () => this.activateSelected(),
    space: () => this.activateSelected(),
    left: () => this.goToHelp(),
    right: () => this.goBack(),
    h: () => this.goToHelp(),
    l: () => this.goBack(),
    escape: () => (this.isEditing ? this.cancelEdit() : this.goBack()),
    q: () => this.goBack(),
  };

  constructor(
    private readonly changeConfig$: Subject<Partial<IConfig>>,
    config: IConfig,
  ) {
    super();
    this.config = { ...config };
    this.initializeOptions();
  }

  private initializeOptions(): void {
    this.options = [
      {
        label: 'Sensitive results',
        type: 'checkbox',
        key: 'excludeSensitiveResults',
        value: !this.config.excludeSensitiveResults,
      },
      {
        label: 'Sort by',
        type: 'dropdown',
        key: 'sortBy',
        value: this.config.sortBy,
        options: ['path', 'size', 'age'],
      },
      {
        label: 'Dry-run',
        type: 'checkbox',
        key: 'dryRun',
        value: this.config.dryRun,
      },
      {
        label: 'Exclude',
        type: 'input',
        key: 'exclude',
        value: Array.isArray(this.config.exclude)
          ? this.config.exclude.join(',')
          : '',
      },
      {
        label: 'Size unit',
        type: 'dropdown',
        key: 'sizeUnit',
        value: this.config.sizeUnit,
        options: ['auto', 'MB', 'GB'],
      },
      {
        label: 'Cwd',
        type: 'input',
        key: 'folderRoot',
        value: path.resolve(this.config.folderRoot),
      },
      {
        label: 'Target folder',
        type: 'input',
        key: 'targets',
        value: Array.isArray(this.config.targets)
          ? this.config.targets.join(',')
          : '',
      },
    ];
  }

  private move(dir: -1 | 1): void {
    if (this.isEditing) return;
    this.selectedIndex =
      (this.selectedIndex + dir + this.options.length) % this.options.length;
    this.render();
  }

  private activateSelected(): void {
    const opt = this.options[this.selectedIndex];

    if (opt.type === 'checkbox') {
      // Direct assignment for boolean types
      opt.value = !opt.value as IConfig[typeof opt.key];
      const key = opt.key as keyof Pick<
        IConfig,
        {
          [K in keyof IConfig]: IConfig[K] extends boolean ? K : never;
        }[keyof IConfig]
      >;

      const valueToSave =
        key === 'excludeSensitiveResults' ? !opt.value : opt.value;

      this.config[key] = !!valueToSave;
      this.emitConfigChange(opt.key, valueToSave);
      this.render();
    } else if (opt.type === 'dropdown') {
      const key = opt.key as keyof Pick<
        IConfig,
        {
          [K in keyof IConfig]: IConfig[K] extends string ? K : never;
        }[keyof IConfig]
      >;
      const idx = opt.options!.indexOf(opt.value as string);
      const next = (idx + 1) % opt.options!.length;
      opt.value = opt.options![next] as IConfig[typeof key];

      if (opt.key === 'sizeUnit') {
        this.config[key] = opt.value as IConfig['sizeUnit'];
      } else {
        this.config[opt.key as any] = opt.value as IConfig[typeof opt.key];
      }

      this.emitConfigChange(opt.key, opt.value);
      this.render();
    } else if (opt.type === 'input') {
      this.isEditing = true;
      // Convertir el valor existente a string para el buffer de edición
      this.editBuffer = String(opt.value);
      this.render();
    }
  }

  private handleEditKey(name: string, sequence: string): void {
    const opt = this.options[this.selectedIndex];

    if (opt.type !== 'input') {
      this.isEditing = false;
      this.render();
      return;
    }

    if (name === 'return') {
      if (opt.key === 'targets' || opt.key === 'exclude') {
        const arrValue = this.editBuffer
          .split(',')
          .map((s) => s.trim())
          .filter(Boolean);
        this.config[opt.key] = arrValue;
        this.emitConfigChange(opt.key, arrValue);
        opt.value = this.editBuffer;
      } else {
        const key = opt.key as keyof Pick<
          IConfig,
          {
            [K in keyof IConfig]: IConfig[K] extends string ? K : never;
          }[keyof IConfig]
        >;
        const newValue: IConfig[typeof opt.key] = this
          .editBuffer as IConfig[typeof opt.key];

        if (key === 'folderRoot') {
          const newPath = path.resolve(newValue as string);
          if (existsSync(newPath)) {
            this.config[key] = newPath;
            opt.value = newPath;
            this.emitConfigChange(opt.key, newPath);
          }
          // if not valid, revert visually to old value on render
        } else {
          this.config[key as any] = newValue as unknown as string;
          opt.value = newValue;
          this.emitConfigChange(opt.key, newValue);
        }
      }
      this.isEditing = false;
      this.render();
    } else if (name === 'escape') {
      this.cancelEdit();
    } else if (name === 'backspace') {
      this.editBuffer = this.editBuffer.slice(0, -1);
      this.render();
    } else if (sequence && sequence.length === 1) {
      this.editBuffer += sequence;
      this.render();
    }
  }

  private emitConfigChange<K extends keyof IConfig>(
    key: K,
    value: IConfig[K],
  ): void {
    const configChange: Partial<IConfig> = { [key]: value } as Partial<IConfig>;
    this.changeConfig$.next(configChange);
  }

  private cancelEdit(): void {
    this.isEditing = false;
    this.editBuffer = '';
    this.render();
  }

  onKeyInput(key: IKeyPress): void {
    if (this.isEditing) {
      this.handleEditKey(key.name, key.sequence);
      return;
    }

    const action = this.KEYS[key.name];
    if (action) action();
  }

  private goBack(): void {
    this.clear();
    this.goBack$.next(null);
  }

  private goToHelp(): void {
    this.clear();
    this.goToHelp$.next(null);
  }

  render(): void {
    this.clear();
    this.printHintMessage();
    let currentRow = MARGINS.ROW_RESULTS_START;

    this.printAt(pc.bold(pc.bgYellow(pc.black('  OPTIONS  '))), {
      x: 1,
      y: currentRow++,
    });
    currentRow++;

    let activeDropdown: {
      options: string[];
      yBase: number;
    } | null = null;

    for (let i = 0; i < this.options.length; i++) {
      const opt = this.options[i];
      const isSelected = i === this.selectedIndex;
      const label = `${opt.label.padEnd(18)}`;

      let valueText = '';
      if (opt.type === 'checkbox') {
        valueText = opt.value ? '[x]' : '[ ]';
      } else if (opt.type === 'dropdown') {
        valueText = `${opt.value}`;
      } else if (opt.type === 'input') {
        valueText =
          this.isEditing && isSelected
            ? this.editBuffer + '_'
            : String(opt.value) === ''
              ? 'none'
              : String(opt.value);
      }

      // Move the options down to prevent the values from overlapping.
      const LEFT_MARGIN = 2;
      const terminalWidth = this.terminal.columns;
      const PREFIX_LENGTH = 20; // Marker (1) + Space (1) + Label (18)
      const valueStartX = LEFT_MARGIN + PREFIX_LENGTH;
      const maxContentWidth = Math.max(10, terminalWidth - valueStartX);

      const chunks: string[] = [];
      if (valueText.length === 0) {
        chunks.push('');
      } else {
        for (let k = 0; k < valueText.length; k += maxContentWidth) {
          chunks.push(valueText.substring(k, k + maxContentWidth));
        }
      }

      chunks.forEach((chunk, index) => {
        let line = '';
        let chunkText = chunk;
        if (
          opt.type === 'input' &&
          String(opt.value) === '' &&
          chunk === 'none'
        ) {
          chunkText = pc.gray(chunk);
        }

        if (index === 0) {
          line = `${isSelected ? pc.bgCyan(' ') : ' '} ${label}${chunkText}`;
        } else {
          const padding = ' '.repeat(PREFIX_LENGTH);
          line = `${padding}${chunkText}`;
        }

        this.printAt(isSelected ? pc.cyan(line) : line, {
          x: LEFT_MARGIN,
          y: currentRow++,
        });
      });

      // If selected and dropdown, queue for rendering
      if (opt.type === 'dropdown' && isSelected) {
        activeDropdown = {
          options: opt.options || [],
          yBase: currentRow,
        };
      }
    }

    if (activeDropdown) {
      const dropdownOptions = activeDropdown.options;
      const optionsNumber = dropdownOptions.length;
      const maxLength =
        dropdownOptions.length > 0
          ? Math.max(...dropdownOptions.map((o) => o.length))
          : 0;
      const activeOpt = this.options[this.selectedIndex];

      for (let i = 0; i < optionsNumber; i++) {
        const option = dropdownOptions[i];
        const paddedOption = option.padEnd(maxLength, ' ');
        const optionEntryText =
          option === activeOpt.value
            ? pc.bgCyan(pc.black(` ${paddedOption} `))
            : pc.bgBlack(pc.white(` ${paddedOption} `));
        this.printAt(optionEntryText, {
          x: 28,
          y: activeDropdown.yBase - Math.round(optionsNumber / 2) + i,
        });
      }
    }
  }

  private printHintMessage() {
    const optionSelected = this.options[this.selectedIndex];

    const hintText =
      optionSelected.type === 'input' && this.isEditing
        ? OPTIONS_HINTS_BY_TYPE['input-exit']
        : OPTIONS_HINTS_BY_TYPE[optionSelected.type];

    if (!hintText) {
      return;
    }

    this.printAt(hintText, {
      x: 15,
      y: MARGINS.ROW_RESULTS_START,
    });
  }

  clear(): void {
    for (let row = MARGINS.ROW_RESULTS_START; row < this.terminal.rows; row++) {
      this.clearLine(row);
    }
  }
}
```

## File: `src/cli/ui/components/result-details.ui.ts`
```typescript
import { MARGINS } from '../../../constants/main.constants.js';
import { BaseUi, InteractiveUi } from '../base.ui.js';
import { IKeyPress } from '../../interfaces/key-press.interface.js';
import { Subject } from 'rxjs';
import pc from 'picocolors';
import { resolve } from 'node:path';
import { CliScanFoundFolder } from '../../../cli/interfaces/stats.interface.js';
import { formatSize } from '../../../utils/unit-conversions.js';
import { RESULT_TYPE_INFO } from '../../../constants/index.js';
import { IConfig } from '../../interfaces/config.interface.js';

export class ResultDetailsUi extends BaseUi implements InteractiveUi {
  resultIndex = 0;

  readonly goBack$ = new Subject<null>();
  readonly openFolder$ = new Subject<string>();

  private readonly KEYS = {
    left: () => this.goBack(),
    h: () => this.goBack(),
    o: () => this.openFolder(),
    q: () => this.goBack(),
    escape: () => this.goBack(),
  };

  constructor(
    private readonly result: CliScanFoundFolder,
    private readonly config: IConfig,
  ) {
    super();
  }

  private openFolder(): void {
    const folderPath = this.result.path;
    const parentPath = resolve(folderPath, '..');
    this.openFolder$.next(parentPath);
  }

  private goBack(): void {
    this.clear();
    this.goBack$.next(null);
  }

  onKeyInput({ name }: IKeyPress): void {
    const action: (() => void) | undefined = this.KEYS[name];
    if (action === undefined) {
      return;
    }
    action();
  }

  render(): void {
    const { path, size, modificationTime, status, riskAnalysis } = this.result;

    const maxWidth = Math.min(this.terminal.columns, 80);
    const startRow = MARGINS.ROW_RESULTS_START;
    let currentRow = startRow;

    this.clear();

    const wrapText = (
      text: string,
      width: number,
      splitter: RegExp | string = ' ',
    ): string[] => {
      const words =
        typeof splitter === 'string'
          ? text.split(splitter)
          : text.split(splitter);
      const lines: string[] = [];
      let currentLine = '';
      for (const word of words) {
        if ((currentLine + word).length >= width) {
          lines.push(currentLine.trim());
          currentLine = '';
        }
        currentLine += word + (typeof splitter === 'string' ? splitter : '');
      }
      if (currentLine.trim()) lines.push(currentLine.trim());
      return lines;
    };

    const wrapPath = (text: string, width: number): string[] => {
      return wrapText(text, width, /([/\\])/g);
    };

    const drawLabel = (
      label: string,
      value: string,
      colorFn = (v: string) => v,
    ) => {
      const text = `${label.padEnd(16)}${colorFn(value)}`;
      this.printAt(text, { x: 2, y: currentRow++ });
    };

    // Header
    this.printAt(pc.bold(pc.bgYellow(pc.black('  Result Details  '))), {
      x: 1,
      y: currentRow++,
    });
    this.printAt('-'.repeat(maxWidth - 4), { x: 2, y: currentRow++ });

    // Path
    const folderName = path.split(/[/\\]/).filter(Boolean).pop() || '';
    const wrappedPath = wrapPath(path, maxWidth - 4);
    this.printAt(pc.cyan('Path:'), { x: 2, y: currentRow++ });
    for (let i = 0; i < wrappedPath.length; i++) {
      const line = wrappedPath[i];
      const isLastLine = i === wrappedPath.length - 1;

      if (isLastLine && line.includes(folderName)) {
        const idx = line.lastIndexOf(folderName);
        const before = line.slice(0, idx);
        const name = line.slice(idx);
        this.printAt('  ' + before + pc.yellow(pc.underline(name)), {
          x: 2,
          y: currentRow++,
        });
      } else {
        this.printAt('  ' + line, { x: 2, y: currentRow++ });
      }
    }

    // Size, Modified
    const formattedSize = formatSize(size, this.config.sizeUnit);
    drawLabel(
      'Size:',
      size ? formattedSize.text : '...',
      size ? pc.yellow : pc.gray,
    );
    drawLabel(
      'Modified:',
      modificationTime > 0
        ? new Date(modificationTime * 1000).toLocaleString()
        : '...',
      pc.gray,
    );

    // Status
    const statusColors = {
      live: pc.green,
      deleting: pc.yellow,
      'error-deleting': pc.red,
      deleted: pc.gray,
    };
    drawLabel('Status:', status, statusColors[status]);

    // Delicate
    drawLabel(
      'Delicate:',
      riskAnalysis?.isSensitive ? 'YES ⚠️' : 'No',
      riskAnalysis?.isSensitive ? (v) => pc.red(pc.bold(v)) : pc.green,
    );

    if (riskAnalysis?.isSensitive && riskAnalysis.reason) {
      const reasonLines = wrapPath(riskAnalysis?.reason + '.', maxWidth - 16);
      for (const line of reasonLines) {
        this.printAt('  ' + pc.red(pc.italic(line)), {
          x: 16,
          y: currentRow++,
        });
      }
    }

    // Footer
    currentRow++;
    this.printAt(pc.gray('← Back    ') + pc.gray('o: Open parent folder'), {
      x: 2,
      y: currentRow++,
    });

    // Target folder details
    const folderKey = folderName.toLowerCase();
    const targetInfo: string = RESULT_TYPE_INFO[folderKey];

    if (targetInfo) {
      currentRow += 2;
      this.printAt(pc.bold(pc.bgBlack(pc.gray(` ${folderName} info `))), {
        x: 2,
        y: currentRow++,
      });

      const warningMatch = targetInfo.match(/^(.*?)\s*WARNING:\s*(.*)$/s);

      if (warningMatch) {
        const mainInfo = warningMatch[1].trim();
        const warningText = warningMatch[2].trim();

        const infoLines = wrapText(mainInfo, maxWidth - 2);
        for (const line of infoLines) {
          this.printAt(pc.gray(line), {
            x: 2,
            y: currentRow++,
          });
        }

        const warningLines = wrapText(`⚠️ ${warningText}`, maxWidth - 2);
        for (const line of warningLines) {
          this.printAt(pc.yellow(line), {
            x: 2,
            y: currentRow++,
          });
        }
      } else {
        const infoLines = wrapText(targetInfo, maxWidth - 2);
        for (const line of infoLines) {
          this.printAt(pc.gray(line), {
            x: 2,
            y: currentRow++,
          });
        }
      }
    }
  }

  clear(): void {
    for (let row = MARGINS.ROW_RESULTS_START; row < this.terminal.rows; row++) {
      this.clearLine(row);
    }
  }

  /** Returns the number of results that can be displayed. */
  private getRowsAvailable(): number {
    return this.terminal.rows - MARGINS.ROW_RESULTS_START;
  }

  /** Returns the row to which the index corresponds. */
  private getRow(index: number): number {
    return index + MARGINS.ROW_RESULTS_START;
  }
}
```

## File: `src/cli/ui/components/results.ui.ts`
```typescript
import {
  DECIMALS_SIZE,
  DEFAULT_CONFIG,
  MARGINS,
  OVERFLOW_CUT_FROM,
} from '../../../constants/main.constants.js';

import { InteractiveUi } from '../base.ui.js';
import { HeavyUi } from '../heavy.ui.js';

import { ConsoleService } from '../../services/console.service.js';
import { IConfig } from '../../interfaces/config.interface.js';
import { IKeyPress } from '../../interfaces/key-press.interface.js';
import { INFO_MSGS } from '../../../constants/messages.constants.js';
import { ResultsService } from '../../services/results.service.js';
import { Subject } from 'rxjs';
import pc from 'picocolors';
import { resolve } from 'node:path';
import { CliScanFoundFolder } from '../../../cli/interfaces/stats.interface.js';
import { formatSize } from '../../../utils/unit-conversions.js';

const CURSOR_ROW_COLOR = 'bgBlue';

export class ResultsUi extends HeavyUi implements InteractiveUi {
  resultIndex = 0;
  previousIndex = 0;
  scroll: number = 0;
  private haveResultsAfterCompleted = true;
  private selectMode = false;
  private selectedFolders: Map<string, CliScanFoundFolder> = new Map();
  private rangeSelectionStart: number | null = null;
  private isRangeSelectionMode: boolean = false;

  readonly delete$ = new Subject<CliScanFoundFolder>();
  readonly deleteMultiple$ = new Subject<CliScanFoundFolder[]>();
  readonly showErrors$ = new Subject<null>();
  readonly openFolder$ = new Subject<string>();
  readonly showDetails$ = new Subject<CliScanFoundFolder>();
  readonly goOptions$ = new Subject<null>();
  readonly endNpkill$ = new Subject<null>();
  readonly search$ = new Subject<{
    text: string;
    isInputActive: boolean;
  } | null>();

  private isSearchInputMode = false;
  private searchText = '';
  private filteredResults: CliScanFoundFolder[] = [];

  private readonly config: IConfig = DEFAULT_CONFIG;
  private readonly KEYS = {
    up: () => this.cursorUp(),
    down: () => this.cursorDown(),
    space: () => this.handleSpacePress(),
    delete: () => this.handleSpacePress(),
    j: () => this.cursorDown(),
    k: () => this.cursorUp(),
    h: () => this.goOptions(),
    l: () => this.showDetails(),
    d: () => this.cursorPageDown(),
    u: () => this.cursorPageUp(),
    pageup: () => this.cursorPageUp(),
    pagedown: () => this.cursorPageDown(),
    home: () => this.cursorFirstResult(),
    end: () => this.cursorLastResult(),
    e: () => this.showErrorsPopup(),
    o: () => this.openFolder(),
    right: () => this.showDetails(),
    left: () => this.goOptions(),
    q: () => this.endNpkill(),
    t: () => this.toggleSelectMode(),
    return: () => this.deleteSelected(),
    enter: () => this.deleteSelected(),
    v: () => this.startRangeSelection(),
    a: () => this.toggleSelectAll(),
  };

  constructor(
    private readonly resultsService: ResultsService,
    private readonly consoleService: ConsoleService,
  ) {
    super();
  }

  private openFolder(): void {
    const folder = this.results[this.resultIndex];
    const parentPath = resolve(folder.path, '..');
    this.openFolder$.next(parentPath);
  }

  private showDetails(): void {
    const result = this.results[this.resultIndex];
    if (!result) {
      return;
    }
    this.showDetails$.next(result);
  }

  private goOptions(): void {
    if (this.searchText) {
      return;
    }
    this.goOptions$.next(null);
  }

  private endNpkill(): void {
    this.endNpkill$.next(null);
  }

  private toggleSelectMode(): void {
    this.selectMode = !this.selectMode;
    if (!this.selectMode) {
      this.selectedFolders.clear();
      this.rangeSelectionStart = null;
      this.isRangeSelectionMode = false;
    }
  }

  private startRangeSelection(): void {
    if (!this.selectMode) {
      return;
    }

    if (this.isRangeSelectionMode) {
      // Selection mode was started, so end the range.
      this.isRangeSelectionMode = false;
      this.rangeSelectionStart = null;
      return;
    }

    this.isRangeSelectionMode = true;
    this.rangeSelectionStart = this.resultIndex;

    const folder = this.results[this.resultIndex];
    if (folder) {
      if (this.selectedFolders.has(folder.path)) {
        this.selectedFolders.delete(folder.path);
      } else {
        this.selectedFolders.set(folder.path, folder);
      }
    }
  }

  private toggleSelectAll(): void {
    if (!this.selectMode) {
      return;
    }

    const allFolders = this.results;
    const totalFolders = allFolders.length;
    const selectedCount = this.selectedFolders.size;

    // If all folders are selected, deselect all
    // If some or none are selected, select all
    if (selectedCount === totalFolders) {
      this.selectedFolders.clear();
    } else {
      allFolders.forEach((folder) => {
        this.selectedFolders.set(folder.path, folder);
      });
    }
  }

  private handleSpacePress(): void {
    if (!this.selectMode) {
      this.delete();
      return;
    }

    this.toggleFolderSelection();
  }

  private toggleFolderSelection(): void {
    const folder = this.results[this.resultIndex];
    if (!folder) {
      return;
    }

    if (this.selectedFolders.has(folder.path)) {
      this.selectedFolders.delete(folder.path);
    } else {
      this.selectedFolders.set(folder.path, folder);
    }
  }

  private applyRangeSelection(): void {
    if (
      !this.selectMode ||
      !this.isRangeSelectionMode ||
      this.rangeSelectionStart === null
    ) {
      return;
    }

    const start = Math.min(this.rangeSelectionStart, this.resultIndex);
    const end = Math.max(this.rangeSelectionStart, this.resultIndex);

    const firstFolder = this.results[this.rangeSelectionStart];
    if (!firstFolder) {
      return;
    }

    const shouldSelect = this.selectedFolders.has(firstFolder.path);

    for (let i = start; i <= end; i++) {
      const folder = this.results[i];
      if (!folder) {
        continue;
      }

      if (shouldSelect) {
        this.selectedFolders.set(folder.path, folder);
      } else {
        this.selectedFolders.delete(folder.path);
      }
    }
  }

  private deleteSelected(): void {
    if (!this.selectMode || this.selectedFolders.size === 0) {
      return;
    }

    const selectedFolders = this.selectedFolders.entries();
    for (const [, folder] of selectedFolders) {
      this.delete$.next(folder);
    }
    this.selectedFolders.clear();
  }

  private activateSearchInputMode(): void {
    this.isSearchInputMode = true;
    this.search$.next({ text: this.searchText, isInputActive: true });
    this.render();
  }

  private handleSearchInput(key: IKeyPress): void {
    if (key.name === 'return' || key.name === 'enter') {
      this.isSearchInputMode = false;
      if (this.searchText.trim() === '') {
        this.searchText = '';
        this.search$.next(null);
      } else {
        this.search$.next({ text: this.searchText, isInputActive: false });
      }
      this.render();
      return;
    }

    if (key.name === 'backspace') {
      this.searchText = this.searchText.slice(0, -1);
    } else if (key.name === 'escape') {
      this.isSearchInputMode = false;
      this.searchText = '';
      this.search$.next(null);
      this.render();
      return;
    } else if (
      key.sequence &&
      key.sequence.length === 1 &&
      !key.ctrl &&
      !key.meta
    ) {
      this.searchText += key.sequence;
    } else {
      return;
    }

    this.filterResults();
    this.search$.next({ text: this.searchText, isInputActive: true });
    this.resultIndex = 0;
    this.scroll = 0;
    this.render();
  }

  private filterResults(): void {
    try {
      const regex = new RegExp(this.searchText, 'i');
      this.filteredResults = this.resultsService.results.filter((r) =>
        regex.test(r.path),
      );
    } catch {
      this.filteredResults = [];
    }
  }

  onKeyInput(key: IKeyPress): void {
    if (this.isSearchInputMode) {
      this.handleSearchInput(key);
      return;
    }

    if (key.sequence === '/') {
      this.activateSearchInputMode();
      return;
    }

    const action: (() => void) | undefined = this.KEYS[key.name];
    if (action === undefined) {
      return;
    }
    action();

    if (this.visible) {
      this.render();
    }
  }

  render(): void {
    if (!this.visible) {
      return;
    }

    this.clear();

    if (!this.haveResultsAfterCompleted) {
      this.noResults();
      return;
    }

    this.printResults();

    const tagStartXPosition = 16;
    // 14 for the selection counter, 56 for the instruction message
    const maxClearLength = 14 + 56;
    const availableWidthForClear = this.terminal.columns - tagStartXPosition;
    const clearLength = Math.min(maxClearLength, availableWidthForClear);
    const clearSelectionCounterText = ' '.repeat(Math.max(0, clearLength));

    this.printAt(clearSelectionCounterText, {
      x: tagStartXPosition,
      y: MARGINS.ROW_RESULTS_START - 2,
    });
    if (this.selectMode) {
      const selectedMessage = ` ${this.selectedFolders.size} selected `;
      this.printAt(pc.bgYellow(pc.black(selectedMessage)), {
        x: tagStartXPosition,
        y: MARGINS.ROW_RESULTS_START - 2,
      });

      const instructionMessage = pc.gray(
        pc.bold('SPACE') +
          ': toggle | ' +
          pc.bold('v') +
          ': range | ' +
          pc.bold('a') +
          ': select all | ' +
          pc.bold('ENTER') +
          ': delete',
      );

      const startX = tagStartXPosition + selectedMessage.length + 1;
      const availableWidth = this.terminal.columns - startX;
      const truncatedInstructionMessage = this.truncateText(
        instructionMessage,
        availableWidth,
      );

      this.printAt(truncatedInstructionMessage, {
        x: startX,
        y: MARGINS.ROW_RESULTS_START - 2,
      });
    }

    this.printScrollBar();
    this.flush();
  }

  clear(): void {
    this.resetBufferState();
    for (let row = MARGINS.ROW_RESULTS_START; row < this.terminal.rows; row++) {
      this.clearLine(row);
    }
  }

  completeSearch(): void {
    if (this.resultsService.results.length === 0) {
      this.haveResultsAfterCompleted = false;
      this.render();
    }
  }

  private printResults(): void {
    const visibleFolders = this.getVisibleScrollFolders();

    visibleFolders.forEach((folder: CliScanFoundFolder, index: number) => {
      const row = MARGINS.ROW_RESULTS_START + index;
      this.printFolderRow(folder, row);
    });
  }

  private noResults(): void {
    const targetFolderColored: string = pc.yellowBright(
      this.config.targets.join(', '),
    );
    const message = `No ${targetFolderColored} found!`;
    this.printAt(message, {
      x: Math.floor(this.terminal.columns / 2 - message.length / 2),
      y: MARGINS.ROW_RESULTS_START + 2,
    });
  }

  private printFolderRow(folder: CliScanFoundFolder, row: number): void {
    this.clearLine(row);
    let { path, lastModification, size } = this.getFolderTexts(folder);
    const isRowSelected =
      row === this.getRealCursorPosY() && !this.isSearchInputMode;

    lastModification = isRowSelected
      ? pc.white(lastModification)
      : pc.gray(lastModification);

    // Adjust column start based on select mode
    const pathColumnStart = this.selectMode
      ? MARGINS.FOLDER_COLUMN_START + 1
      : MARGINS.FOLDER_COLUMN_START;

    if (isRowSelected) {
      path = pc[CURSOR_ROW_COLOR](path);
      size = pc[CURSOR_ROW_COLOR](size);
      lastModification = pc[CURSOR_ROW_COLOR](lastModification);

      this.paintBgRow(row);
    }

    if (folder.riskAnalysis?.isSensitive) {
      path += '⚠️';
    }

    const isFolderSelected = this.selectedFolders.has(folder.path);
    if (folder.riskAnalysis?.isSensitive) {
      path = pc[isFolderSelected ? 'blue' : 'yellowBright'](path);
    } else if (!isRowSelected && isFolderSelected) {
      path = pc.blue(path);
    }

    if (this.selectMode && this.selectedFolders.has(folder.path)) {
      this.rangeSelectedCursor(row);
    }

    if (this.selectMode && this.isRangeSelectionMode && isRowSelected) {
      this.selectionCursor(row);
    }

    this.printAt(path, {
      x: pathColumnStart,
      y: row,
    });
    this.printAt(lastModification, {
      x: this.terminal.columns - MARGINS.FOLDER_SIZE_COLUMN - 4,
      y: row,
    });
    this.printAt(size, {
      x: this.terminal.columns - MARGINS.FOLDER_SIZE_COLUMN,
      y: row,
    });
  }

  private rangeSelectedCursor(row: number): void {
    this.printAt('●', {
      x: MARGINS.FOLDER_COLUMN_START,
      y: row,
    });
  }

  private selectionCursor(row: number): void {
    const indicator = this.isRangeSelectionMode ? '●' : ' ';
    this.printAt(pc.yellow(indicator), {
      x: MARGINS.FOLDER_COLUMN_START - 1,
      y: row,
    });
  }

  private getFolderTexts(folder: CliScanFoundFolder): {
    path: string;
    size: string;
    lastModification: string;
  } {
    const folderText = this.getFolderPathText(folder);
    const formattedSize = formatSize(
      folder.size,
      this.config.sizeUnit,
      DECIMALS_SIZE,
    );
    let daysSinceLastModification: string;

    if (folder.modificationTime !== null && folder.modificationTime > 0) {
      daysSinceLastModification = `${Math.floor(
        (new Date().getTime() / 1000 - folder.modificationTime) / 86400,
      )}d`;
    } else {
      daysSinceLastModification = pc.gray('  ...');
    }

    if (folder.riskAnalysis?.isSensitive) {
      daysSinceLastModification = '';
    }

    // Align to right
    const alignMargin = 4 - daysSinceLastModification.length;
    daysSinceLastModification =
      ' '.repeat(alignMargin > 0 ? alignMargin : 0) + daysSinceLastModification;

    const OFFSET_COLUMN = 9;
    let folderSize = formattedSize.text;

    // Right-align size text
    const sizeLength = folderSize.length;
    const spacePadding = ' '.repeat(Math.max(0, OFFSET_COLUMN - sizeLength));
    folderSize = `${spacePadding}${folderSize}`;

    // Only show "..." if size is exactly 0 AND modificationTime is -1 (not yet calculated)
    // If size is 0 but modificationTime is set, then it's a truly empty folder
    const isCalculating = folder.size === 0 && folder.modificationTime === -1;
    const folderSizeText = isCalculating ? pc.gray('   .....') : folderSize;

    return {
      path: folderText,
      size: folderSizeText,
      lastModification: daysSinceLastModification,
    };
  }

  cursorUp(): void {
    this.moveCursor(-1);
  }

  cursorDown(): void {
    this.moveCursor(1);
  }

  cursorPageUp(): void {
    const resultsInPage = this.getRowsAvailable();
    this.moveCursor(-(resultsInPage - 2));
  }

  cursorPageDown(): void {
    const resultsInPage = this.getRowsAvailable();
    this.moveCursor(resultsInPage - 2);
  }

  cursorFirstResult(): void {
    this.moveCursor(-this.resultIndex);
  }

  cursorLastResult(): void {
    this.moveCursor(this.results.length - 1);
  }

  fitScroll(): void {
    const shouldScrollUp =
      this.getRow(this.resultIndex) <
      MARGINS.ROW_RESULTS_START + this.scroll + 1;

    const shouldScrollDown =
      this.getRow(this.resultIndex) > this.terminal.rows + this.scroll - 2;

    const isOnBotton = this.resultIndex === this.results.length - 1;

    let scrollRequired = 0;

    if (shouldScrollUp) {
      scrollRequired =
        this.getRow(this.resultIndex) -
        MARGINS.ROW_RESULTS_START -
        this.scroll -
        1;
    } else if (shouldScrollDown) {
      scrollRequired =
        this.getRow(this.resultIndex) - this.terminal.rows - this.scroll + 2;

      if (isOnBotton) {
        scrollRequired -= 1;
      }
    }

    if (scrollRequired !== 0) {
      this.scrollFolderResults(scrollRequired);
    }
  }

  scrollFolderResults(scrollAmount: number): void {
    const virtualFinalScroll = this.scroll + scrollAmount;
    this.scroll = this.clamp(virtualFinalScroll, 0, this.results.length);
    this.clear();
  }

  private moveCursor(index: number): void {
    this.previousIndex = this.resultIndex;
    this.resultIndex += index;

    // Upper limit
    if (this.isCursorInLowerLimit()) {
      this.resultIndex = 0;
    }

    // Lower limit
    if (this.isCursorInUpperLimit()) {
      this.resultIndex = this.results.length - 1;
    }

    this.fitScroll();

    if (this.isRangeSelectionMode) {
      this.applyRangeSelection();
    }
  }

  private getFolderPathText(folder: CliScanFoundFolder): string {
    let cutFrom = OVERFLOW_CUT_FROM;
    let text = folder.path;
    const ACTIONS = {
      deleted: () => {
        cutFrom += INFO_MSGS.DELETED_FOLDER.length;
        text = INFO_MSGS.DELETED_FOLDER + text;
      },
      deleting: () => {
        cutFrom += INFO_MSGS.DELETING_FOLDER.length;
        text = INFO_MSGS.DELETING_FOLDER + text;
      },
      'error-deleting': () => {
        cutFrom += INFO_MSGS.ERROR_DELETING_FOLDER.length;
        text = INFO_MSGS.ERROR_DELETING_FOLDER + text;
      },
    };

    if (ACTIONS[folder.status] !== undefined) {
      ACTIONS[folder.status]();
    }

    // Adjust text width based if select mode is enabled
    const columnEnd = this.selectMode
      ? MARGINS.FOLDER_COLUMN_END + 1
      : MARGINS.FOLDER_COLUMN_END;

    text = this.consoleService.shortenText(
      text,
      this.terminal.columns - columnEnd,
      cutFrom,
    );

    // This is necessary for the coloring of the text, since
    // the shortener takes into ansi-scape codes invisible
    // characters and can cause an error in the cli.
    text = this.paintStatusFolderPath(text, folder.status);

    return text;
  }

  private paintStatusFolderPath(folderString: string, action: string): string {
    const TRANSFORMATIONS = {
      deleted: (text) =>
        text.replace(
          INFO_MSGS.DELETED_FOLDER,
          pc.green(INFO_MSGS.DELETED_FOLDER),
        ),
      deleting: (text) =>
        text.replace(
          INFO_MSGS.DELETING_FOLDER,
          pc.yellow(INFO_MSGS.DELETING_FOLDER),
        ),
      'error-deleting': (text) =>
        text.replace(
          INFO_MSGS.ERROR_DELETING_FOLDER,
          pc.red(INFO_MSGS.ERROR_DELETING_FOLDER),
        ),
    };

    return TRANSFORMATIONS[action] !== undefined
      ? TRANSFORMATIONS[action](folderString)
      : folderString;
  }

  private printScrollBar(): void {
    const SCROLLBAR_ACTIVE = pc.gray('█');
    const SCROLLBAR_BG = pc.gray('░');

    const totalResults = this.results.length;
    const visibleRows = this.getRowsAvailable();

    if (totalResults <= visibleRows) {
      return;
    }

    const scrollPercentage = this.scroll / (totalResults - visibleRows);
    const start = MARGINS.ROW_RESULTS_START;
    const end = this.terminal.rows - 1;
    const scrollBarPosition = Math.round(
      scrollPercentage * (end - start) + start,
    );

    for (let i = start; i <= end; i++) {
      this.printAt(SCROLLBAR_BG, {
        x: this.terminal.columns - 1,
        y: i,
      });
    }

    this.printAt(SCROLLBAR_ACTIVE, {
      x: this.terminal.columns - 1,
      y: scrollBarPosition,
    });
  }

  private isCursorInLowerLimit(): boolean {
    return this.resultIndex < 0;
  }

  private isCursorInUpperLimit(): boolean {
    return this.resultIndex >= this.results.length;
  }

  private getRealCursorPosY(): number {
    return this.getRow(this.resultIndex) - this.scroll;
  }

  private getVisibleScrollFolders(): CliScanFoundFolder[] {
    return this.results.slice(
      this.scroll,
      this.getRowsAvailable() + this.scroll,
    );
  }

  private paintBgRow(row: number): void {
    const startPaint = MARGINS.FOLDER_COLUMN_START;
    const endPaint = this.terminal.columns - MARGINS.FOLDER_SIZE_COLUMN;
    let paintSpaces = '';

    for (let i = startPaint; i < endPaint; ++i) {
      paintSpaces += ' ';
    }

    this.printAt(pc[CURSOR_ROW_COLOR](paintSpaces), {
      x: startPaint,
      y: row,
    });
  }

  private delete(): void {
    const folder = this.results[this.resultIndex];
    this.delete$.next(folder);
  }

  /** Returns the number of results that can be displayed. */
  private getRowsAvailable(): number {
    return this.terminal.rows - MARGINS.ROW_RESULTS_START;
  }

  /** Returns the row to which the index corresponds. */
  private getRow(index: number): number {
    return index + MARGINS.ROW_RESULTS_START;
  }

  private showErrorsPopup(): void {
    this.showErrors$.next(null);
  }

  private truncateText(text: string, maxLength: number): string {
    const stripAnsi = (str: string) => str.replace(/\x1b\[[0-9;]*m/g, '');
    const plainText = stripAnsi(text);

    if (plainText.length <= maxLength) {
      return text;
    }

    const targetLength = maxLength - 3;
    if (targetLength <= 0) {
      return '...';
    }

    let visibleLength = 0;
    let output = '';
    let i = 0;
    const ansiRegex = /\x1b\[[0-9;]*m/;

    while (i < text.length && visibleLength < targetLength) {
      const remaining = text.substring(i);
      const match = remaining.match(ansiRegex);

      if (match && match.index === 0) {
        output += match[0];
        i += match[0].length;
      } else {
        output += text[i];
        visibleLength++;
        i++;
      }
    }

    return output + '...' + '\x1b[0m';
  }

  private clamp(num: number, min: number, max: number): number {
    return Math.min(Math.max(num, min), max);
  }

  private get results(): CliScanFoundFolder[] {
    return this.searchText ? this.filteredResults : this.resultsService.results;
  }
}
```

## File: `src/cli/ui/components/warning.ui.ts`
```typescript
import { InteractiveUi, BaseUi } from '../base.ui.js';
import { Subject } from 'rxjs';
import { IKeyPress } from '../../interfaces/key-press.interface.js';
import { INFO_MSGS, UI_POSITIONS } from '../../../constants/index.js';

export class WarningUi extends BaseUi implements InteractiveUi {
  private showDeleteAllWarning = false;
  readonly confirm$ = new Subject<null>();

  private readonly KEYS = {
    y: () => this.confirm$.next(null),
  };

  onKeyInput({ name }: IKeyPress): void {
    const action = this.KEYS[name];
    if (action === undefined) {
      return;
    }
    action();
  }

  setDeleteAllWarningVisibility(visible: boolean): void {
    this.showDeleteAllWarning = visible;
    this.render();
  }

  render(): void {
    if (this.showDeleteAllWarning) {
      this.printDeleteAllWarning();
    }
  }

  private printDeleteAllWarning(): void {
    this.printAt(INFO_MSGS.DELETE_ALL_WARNING, UI_POSITIONS.WARNINGS);
  }
}
```

## File: `src/cli/ui/components/header/header-ui.constants.ts`
```typescript
export enum MENU_BAR_OPTIONS {
  HELP = 0,
  OPTIONS = 1,
  DELETE = 2,
  INFO = 3,
}
```

## File: `src/cli/ui/components/header/header.ui.ts`
```typescript
import { BehaviorSubject } from 'rxjs';
import {
  BANNER,
  UI_POSITIONS,
  MENU_BAR,
  INFO_MSGS,
} from '../../../../constants/index.js';
import { BaseUi } from '../../base.ui.js';
import pc from 'picocolors';
import { IConfig } from '../../../../cli/interfaces/config.interface.js';
import { MENU_BAR_OPTIONS } from './header-ui.constants.js';

export class HeaderUi extends BaseUi {
  programVersion: string;
  private activeMenuIndex = MENU_BAR_OPTIONS.DELETE;
  private searchMode = false;
  private searchText = '';
  private isSearchInputActive = false;

  readonly menuIndex$ = new BehaviorSubject<MENU_BAR_OPTIONS>(
    MENU_BAR_OPTIONS.DELETE,
  );

  constructor(private readonly config: IConfig) {
    super();
    this.menuIndex$.subscribe((menuIndex) => {
      this.activeMenuIndex = menuIndex;
      this.render();
    });
  }

  setSearch(text: string | null, isInputActive = false) {
    if (text === null) {
      this.searchMode = false;
      this.searchText = '';
      this.isSearchInputActive = false;
    } else {
      this.searchMode = true;
      this.searchText = text;
      this.isSearchInputActive = isInputActive;
    }
    this.render();
  }

  render(): void {
    // banner and tutorial
    this.printAt(BANNER, UI_POSITIONS.INITIAL);
    this.renderHeader();
    this.renderMenuBar();

    if (this.programVersion !== undefined) {
      this.printAt(pc.gray(this.programVersion), UI_POSITIONS.VERSION);
    }

    if (this.config.dryRun) {
      this.printAt(
        pc.black(pc.bgMagenta(` ${INFO_MSGS.DRY_RUN} `)),
        UI_POSITIONS.DRY_RUN_NOTICE,
      );
    }

    // Columns headers
    if (this.activeMenuIndex === MENU_BAR_OPTIONS.DELETE) {
      this.printAt(pc.bgYellow(pc.black(INFO_MSGS.HEADER_COLUMNS)), {
        x: this.terminal.columns - INFO_MSGS.HEADER_COLUMNS.length - 2,
        y: UI_POSITIONS.FOLDER_SIZE_HEADER.y,
      });
    }

    // npkill stats
    this.printAt(pc.gray(INFO_MSGS.TOTAL_SPACE), UI_POSITIONS.TOTAL_SPACE);
    this.printAt(
      pc.gray(INFO_MSGS.SPACE_RELEASED),
      UI_POSITIONS.SPACE_RELEASED,
    );
  }

  private renderHeader(): void {
    const { columns } = this.terminal;
    const spaceToFill = Math.max(0, columns - 2);
    this.printAt(
      pc.bgYellow(' '.repeat(spaceToFill)),
      UI_POSITIONS.TUTORIAL_TIP,
    );
  }

  private renderMenuBar(): void {
    if (this.searchMode) {
      let searchText = ` Search: ${this.searchText} `;
      if (this.isSearchInputActive) {
        searchText = ` Search: ${this.searchText}_ `;
        this.printAt(pc.bgBlue(pc.white(searchText)), {
          x: 2,
          y: UI_POSITIONS.TUTORIAL_TIP.y,
        });
      } else {
        this.printAt(pc.bgWhite(pc.black(searchText)), {
          x: 2,
          y: UI_POSITIONS.TUTORIAL_TIP.y,
        });
      }
      return;
    }

    const options = Object.values(MENU_BAR);
    let xStart = 2;
    for (const option of options) {
      const isActive = option === options[this.activeMenuIndex];
      const colorFn = isActive
        ? (v: string) => pc.bgYellow(pc.black(pc.bold(pc.underline(v))))
        : (v: string) => pc.bgYellow(pc.gray(v));

      this.printAt(colorFn(option), {
        x: xStart,
        y: UI_POSITIONS.TUTORIAL_TIP.y,
      });

      const MARGIN = 1;
      xStart += option.length + MARGIN;
    }
  }
}
```

## File: `src/cli/ui/components/header/stats.ui.ts`
```typescript
import { UI_POSITIONS, INFO_MSGS } from '../../../../constants/index.js';
import { BaseUi } from '../../base.ui.js';
import { ResultsService } from '../../../services/results.service.js';
import { LoggerService } from '@core/services/logger.service.js';
import pc from 'picocolors';
import { IConfig } from '../../../interfaces/config.interface.js';
import { IPosition } from '../../../interfaces/ui-positions.interface.js';

interface ShowStatProps {
  description: string;
  value: string;
  lastValueKey: 'totalSpace' | 'spaceReleased';
  position: IPosition;
  updateColor: 'green' | 'yellow';
}

type ResultTypeRowKey = 'row1' | 'row2' | 'row3' | 'row4' | 'row5';

export class StatsUi extends BaseUi {
  private lastValues = {
    totalSpace: '',
    spaceReleased: '',
  };

  private timeouts = {
    totalSpace: setTimeout(() => {}),
    spaceReleased: setTimeout(() => {}),
  };

  private lastResultTypesValues: Map<ResultTypeRowKey, string> = new Map();
  private resultTypesTimeouts: Map<ResultTypeRowKey, NodeJS.Timeout> =
    new Map();

  constructor(
    private readonly config: IConfig,
    private readonly resultsService: ResultsService,
    private readonly logger: LoggerService,
  ) {
    super();
  }

  // Prevent bug where the "Releasable space" and "Saved Space" got o 0.
  reset(): void {
    this.lastValues = {
      totalSpace: '',
      spaceReleased: '',
    };
    this.lastResultTypesValues.clear();
  }

  render(): void {
    const { totalSpace, spaceReleased, resultsTypesCount } =
      this.resultsService.getStats();

    this.showStat({
      description: INFO_MSGS.TOTAL_SPACE,
      value: totalSpace,
      lastValueKey: 'totalSpace',
      position: UI_POSITIONS.TOTAL_SPACE,
      updateColor: 'yellow',
    });

    this.showStat({
      description: INFO_MSGS.SPACE_RELEASED,
      value: spaceReleased,
      lastValueKey: 'spaceReleased',
      position: UI_POSITIONS.SPACE_RELEASED,
      updateColor: 'green',
    });

    if (this.config.showErrors) {
      this.showErrorsCount();
    }

    this.showResultsTypesCount(resultsTypesCount);
    this.showActivePreset();
  }

  /** Print the value of the stat and if it is a different value from the
   * previous run, highlight it for a while.
   */
  private showStat({
    description,
    value,
    lastValueKey,
    position,
    updateColor,
  }: ShowStatProps): void {
    const statPosition = { ...position };
    statPosition.x += description.length;

    if (value !== this.lastValues[lastValueKey]) {
      // If is first render, initialize.
      if (!this.lastValues[lastValueKey]) {
        this.printAt(value, statPosition);
        this.lastValues[lastValueKey] = value;
        return;
      }

      this.printAt(pc[updateColor](`${value} ▲`), statPosition);

      if (this.timeouts[lastValueKey]) {
        clearTimeout(this.timeouts[lastValueKey]);
      }

      this.timeouts[lastValueKey] = setTimeout(() => {
        this.printAt(value + '  ', statPosition);
      }, 700);

      this.lastValues[lastValueKey] = value;
    } else {
      this.printAt(value, statPosition);
    }
  }

  private showErrorsCount(): void {
    const errors = this.logger.get('error').length;

    if (errors === 0) {
      return;
    }

    const text = `${errors} error${errors > 1 ? 's' : ''}. 'e' to see`;
    this.printAt(pc.yellow(text), { ...UI_POSITIONS.ERRORS_COUNT });
  }

  private showActivePreset(): void {
    const MIN_TERMINAL_WIDTH = 94;
    if (this.terminal.columns < MIN_TERMINAL_WIDTH) {
      return;
    }

    const RIGHT_MARGIN = 2;
    const CLEAR_LENGTH = 50;
    const xStartClear = this.terminal.columns - CLEAR_LENGTH - RIGHT_MARGIN;
    const clearText = ' '.repeat(CLEAR_LENGTH);
    this.printAt(clearText, { x: xStartClear, y: 0 });

    if (!this.config.profiles || this.config.profiles.length === 0) {
      return;
    }

    const text = `[${this.config.profiles.join(', ')}]`;
    const xPosition = this.terminal.columns - text.length - RIGHT_MARGIN;
    this.printAt(pc.gray(pc.bold(text)), { x: xPosition, y: 0 });
  }

  private showResultsTypesCount(
    resultsTypesCount: Array<{ type: string; count: number }>,
  ): void {
    const MAX_CONTENT_LENGTH = 20;
    const RIGHT_MARGIN = 2;
    const MIN_TERMINAL_WIDTH = 94;
    const START_Y = 1;
    const NUM_ROWS = 5;

    if (this.terminal.columns < MIN_TERMINAL_WIDTH) {
      return;
    }

    const clearText = ' '.repeat(MAX_CONTENT_LENGTH);
    const xStart = this.terminal.columns - MAX_CONTENT_LENGTH - RIGHT_MARGIN;

    for (let i = 0; i < NUM_ROWS; i++) {
      const yPos = START_Y + i;
      this.printAt(clearText, { x: xStart, y: yPos });
    }

    const positions: { key: ResultTypeRowKey; yPosition: number }[] = [
      { key: 'row1', yPosition: 1 },
      { key: 'row2', yPosition: 2 },
      { key: 'row3', yPosition: 3 },
      { key: 'row4', yPosition: 4 },
      { key: 'row5', yPosition: 5 },
    ];

    const maxRows = 5;

    if (resultsTypesCount.length <= maxRows) {
      resultsTypesCount.forEach((item, index) => {
        const { key, yPosition } = positions[index];
        const text = this.formatResultTypeText(
          item.count,
          item.type,
          MAX_CONTENT_LENGTH,
        );
        const xPosition = this.terminal.columns - text.length - RIGHT_MARGIN;
        this.showResultTypeRow(key, text, { x: xPosition, y: yPosition });
      });
    } else {
      const topTypes = resultsTypesCount.slice(0, 4);
      const remainingTypes = resultsTypesCount.slice(4);

      topTypes.forEach((item, index) => {
        const { key, yPosition } = positions[index];
        const text = this.formatResultTypeText(
          item.count,
          item.type,
          MAX_CONTENT_LENGTH,
        );
        const xPosition = this.terminal.columns - text.length - RIGHT_MARGIN;
        this.showResultTypeRow(key, text, { x: xPosition, y: yPosition });
      });

      // Show summary in 5th row
      const totalRemaining = remainingTypes.reduce(
        (sum, item) => sum + item.count,
        0,
      );
      const { key, yPosition } = positions[4];
      const summaryText = `[+${remainingTypes.length}·total ${totalRemaining}]`;
      const trimmedSummary =
        summaryText.length > MAX_CONTENT_LENGTH
          ? summaryText.substring(0, MAX_CONTENT_LENGTH - 3) + '...'
          : summaryText;
      const xPosition =
        this.terminal.columns - trimmedSummary.length - RIGHT_MARGIN;
      this.showResultTypeRow(key, trimmedSummary, {
        x: xPosition,
        y: yPosition,
      });
    }
  }

  private formatResultTypeText(
    count: number,
    type: string,
    maxLength: number,
  ): string {
    const countStr = count.toString();
    const baseLength = countStr.length + 3; // ' (' and ')'

    const fullText = `${type} (${countStr})`;
    if (fullText.length <= maxLength) {
      return fullText;
    }

    const maxTypeLength = maxLength - baseLength;
    const trimmedType =
      type.length > maxTypeLength
        ? type.substring(0, maxTypeLength - 3) + '...'
        : type;

    return `${trimmedType} (${countStr})`;
  }

  private showResultTypeRow(
    rowKey: ResultTypeRowKey,
    text: string,
    position: IPosition,
  ): void {
    const lastValue = this.lastResultTypesValues.get(rowKey);
    const valueChanged = text !== lastValue;
    const hasActiveHighlight = this.resultTypesTimeouts.has(rowKey);
    const shouldHighlight = valueChanged && lastValue !== undefined;

    if (shouldHighlight) {
      this.printAt(pc.white(text), { ...position });

      const previousTimeout = this.resultTypesTimeouts.get(rowKey);
      if (previousTimeout) {
        clearTimeout(previousTimeout);
      }

      const timeout = setTimeout(() => {
        this.printAt(pc.gray(text), { ...position });
        this.resultTypesTimeouts.delete(rowKey);
      }, 300);

      this.resultTypesTimeouts.set(rowKey, timeout);
    } else if (hasActiveHighlight) {
      this.printAt(pc.white(text), { ...position });
    } else {
      this.printAt(pc.gray(text), { ...position });
    }

    this.lastResultTypesValues.set(rowKey, text);
  }
}
```

## File: `src/cli/ui/components/header/status.ui.ts`
```typescript
import { BaseUi } from '../../base.ui.js';
import pc from 'picocolors';
import { SpinnerService } from '../../../services/spinner.service.js';
import { interval, Subject, takeUntil } from 'rxjs';
import { INFO_MSGS } from '../../../../constants/messages.constants.js';
import {
  SPINNERS,
  SPINNER_INTERVAL,
} from '../../../../constants/spinner.constants.js';
import { UI_POSITIONS } from '../../../../constants/main.constants.js';
import { ScanStatus } from '@core/interfaces/search-status.model.js';
import {
  BAR_PARTS,
  BAR_WIDTH,
} from '../../../../constants/status.constants.js';

export class StatusUi extends BaseUi {
  private text = '';
  private barNormalizedWidth = 0;
  private barClosing = false;
  private showProgressBar = true;
  private pendingTasksPosition = { ...UI_POSITIONS.PENDING_TASKS };
  private searchEnd$ = new Subject();
  private readonly SEARCH_STATES = {
    stopped: () => this.startingSearch(),
    scanning: () => this.continueSearching(),
    dead: () => this.fatalError(),
    finished: () => this.continueFinishing(),
  };

  constructor(
    private readonly spinnerService: SpinnerService,
    private readonly searchStatus: ScanStatus,
  ) {
    super();
  }

  start(): void {
    this.barClosing = false;
    this.showProgressBar = true;
    this.spinnerService.setSpinner(SPINNERS.W10);
    interval(SPINNER_INTERVAL)
      .pipe(takeUntil(this.searchEnd$))
      .subscribe(() => {
        this.SEARCH_STATES[this.searchStatus.workerStatus]();
      });

    this.animateProgressBar();
  }

  reset(): void {
    this.barClosing = false;
    this.showProgressBar = true;
    this.barNormalizedWidth = 0;
    this.text = '';
    this.pendingTasksPosition = { ...UI_POSITIONS.PENDING_TASKS };
    this.searchEnd$.next(true);
    this.searchEnd$.complete();
    this.searchEnd$ = new Subject();

    if (this.activeAnimation) {
      clearTimeout(this.activeAnimation);
    }
    this.clearPendingTasks();
    this.render();
  }

  completeSearch(duration: number): void {
    this.searchEnd$.next(true);
    this.searchEnd$.complete();

    this.text = pc.green(INFO_MSGS.SEARCH_COMPLETED) + pc.gray(`${duration}s`);
    this.render();
    if (this.activeAnimation) {
      clearTimeout(this.activeAnimation);
    }
    this.activeAnimation = setTimeout(() => this.animateClose(), 2000);
  }

  render(): void {
    this.printAt(this.text + '      ', UI_POSITIONS.STATUS);

    if (this.showProgressBar) {
      this.renderProgressBar();
    }

    this.renderPendingTasks();
  }

  private renderPendingTasks(): void {
    this.clearPendingTasks();
    if (this.searchStatus.pendingDeletions === 0) {
      return;
    }

    const { pendingDeletions } = this.searchStatus;
    const text = pendingDeletions > 1 ? 'pending tasks' : 'pending task ';
    this.printAt(
      pc.yellow(`${pendingDeletions} ${text}`),
      this.pendingTasksPosition,
    );
  }

  private clearPendingTasks(): void {
    const PENDING_TASK_LENGHT = 17;
    this.printAt(' '.repeat(PENDING_TASK_LENGHT), this.pendingTasksPosition);
  }

  private renderProgressBar(): void {
    const {
      pendingSearchTasks,
      completedSearchTasks,
      completedStatsCalculation,
      pendingStatsCalculation,
    } = this.searchStatus;

    const proportional = (a: number, b: number, c: number): number => {
      if (c === 0) {
        return 0;
      }
      return (a * b) / c;
    };

    const modifier =
      this.barNormalizedWidth === 1
        ? 1
        : // easeInOut formula
          -(Math.cos(Math.PI * this.barNormalizedWidth) - 1) / 2;

    const barSearchMax = pendingSearchTasks + completedSearchTasks;
    const barStatsMax = pendingStatsCalculation + completedStatsCalculation;

    let barLenght = Math.ceil(BAR_WIDTH * modifier);

    let searchBarLenght = proportional(
      completedSearchTasks,
      BAR_WIDTH,
      barSearchMax,
    );
    searchBarLenght = Math.ceil(searchBarLenght * modifier);

    let doneBarLenght = proportional(
      completedStatsCalculation,
      searchBarLenght,
      barStatsMax,
    );
    doneBarLenght = Math.floor(doneBarLenght * modifier);

    barLenght -= searchBarLenght;
    searchBarLenght -= doneBarLenght;

    barLenght = Math.max(0, barLenght);
    searchBarLenght = Math.max(0, searchBarLenght);
    doneBarLenght = Math.max(0, doneBarLenght);

    // Debug
    // this.printAt(
    //   `V: ${barSearchMax},T: ${barLenght},C: ${searchBarLenght},D:${doneBarLenght}   `,
    //   { x: 60, y: 5 },
    // );

    const progressBar =
      BAR_PARTS.completed.repeat(doneBarLenght) +
      BAR_PARTS.searchTask.repeat(searchBarLenght) +
      BAR_PARTS.bg.repeat(barLenght);

    this.printProgressBar(progressBar);
  }

  private activeAnimation: NodeJS.Timeout | null = null;

  private animateProgressBar(): void {
    if (this.barNormalizedWidth > 1) {
      this.barNormalizedWidth = 1;
      return;
    }
    this.barNormalizedWidth += 0.05;

    this.renderProgressBar();
    if (this.activeAnimation) {
      clearTimeout(this.activeAnimation);
    }
    this.activeAnimation = setTimeout(
      () => this.animateProgressBar(),
      SPINNER_INTERVAL,
    );
  }

  private animateClose(): void {
    this.barClosing = true;
    if (this.barNormalizedWidth < 0) {
      this.barNormalizedWidth = 0;
      this.showProgressBar = false;

      this.movePendingTaskToTop();
      return;
    }
    this.barNormalizedWidth -= 0.05;

    this.renderProgressBar();
    if (this.activeAnimation) {
      clearTimeout(this.activeAnimation);
    }
    this.activeAnimation = setTimeout(
      () => this.animateClose(),
      SPINNER_INTERVAL,
    );
  }

  /** When the progress bar disappears, "pending tasks" will move up one
      position. */
  private movePendingTaskToTop(): void {
    this.clearPendingTasks();
    this.pendingTasksPosition = { ...UI_POSITIONS.STATUS_BAR };
    this.renderPendingTasks();
  }

  private printProgressBar(progressBar: string): void {
    if (this.barClosing) {
      const postX =
        UI_POSITIONS.STATUS_BAR.x -
        1 +
        Math.round((BAR_WIDTH / 2) * (1 - this.barNormalizedWidth));
      // Clear previus bar
      this.printAt(' '.repeat(BAR_WIDTH), UI_POSITIONS.STATUS_BAR);

      this.printAt(progressBar, {
        x: postX,
        y: UI_POSITIONS.STATUS_BAR.y,
      });
    } else {
      this.printAt(progressBar, UI_POSITIONS.STATUS_BAR);
    }
  }

  private startingSearch(): void {
    this.text = INFO_MSGS.STARTING;
    this.render();
  }

  private continueSearching(): void {
    this.text = INFO_MSGS.SEARCHING + this.spinnerService.nextFrame();
    this.render();
  }

  private fatalError(): void {
    this.text = pc.red(INFO_MSGS.FATAL_ERROR);
    this.searchEnd$.next(true);
    this.searchEnd$.complete();
    this.render();
  }

  private continueFinishing(): void {
    this.text = INFO_MSGS.CALCULATING_STATS + this.spinnerService.nextFrame();
    this.render();
  }
}
```

## File: `src/cli/ui/components/help/help-command.ui.ts`
```typescript
import {
  HELP_HEADER,
  OPTIONS,
  HELP_FOOTER,
  HELP_PROGRESSBAR,
} from '../../../../constants/cli.constants.js';
import { MARGINS, UI_HELP } from '../../../../constants/main.constants.js';
import { INFO_MSGS } from '../../../../constants/messages.constants.js';
import { ConsoleService } from '../../../services/console.service.js';
import { BaseUi } from '../../base.ui.js';
import pc from 'picocolors';

export class HelpCommandUi extends BaseUi {
  constructor(private readonly consoleService: ConsoleService) {
    super();
  }

  render(): void {
    throw new Error('Method not implemented.');
  }

  show(): void {
    const maxWidth = Math.min(UI_HELP.MAX_WIDTH, this.terminal.columns);

    this.clear();
    this.print(pc.inverse(pc.bold(INFO_MSGS.HELP_TITLE + '\n')));

    const headerLines = this.consoleService.splitWordsByWidth(
      HELP_HEADER,
      maxWidth,
    );
    headerLines.forEach((line) => this.print(line + '\n'));
    this.print('\n');

    const progressBarLines = this.consoleService.splitWordsByWidth(
      HELP_PROGRESSBAR,
      maxWidth,
    );
    progressBarLines.forEach((line) => this.print(line + '\n'));
    this.print('\n');

    const maxDescriptionWidth = Math.min(
      maxWidth - UI_HELP.X_DESCRIPTION_OFFSET,
      this.terminal.columns - UI_HELP.X_DESCRIPTION_OFFSET,
    );

    this.print(pc.black(pc.bgYellow(pc.bold(' Options '))) + '\n');
    OPTIONS.forEach((option) => {
      const args = option.arg.reduce((text, arg) => text + ', ' + arg);
      const padding = ' '.repeat(UI_HELP.X_COMMAND_OFFSET);
      const commandLength = UI_HELP.X_COMMAND_OFFSET + args.length;

      const commandTooLong = commandLength >= UI_HELP.X_DESCRIPTION_OFFSET;

      if (commandTooLong) {
        this.print(padding + args + '\n');
      } else {
        this.print(padding + args);
      }

      const description = this.consoleService.splitWordsByWidth(
        option.description,
        maxDescriptionWidth,
      );

      description.forEach((line, index) => {
        if (index === 0 && !commandTooLong) {
          const spaceBetween = ' '.repeat(
            UI_HELP.X_DESCRIPTION_OFFSET - commandLength,
          );
          this.print(spaceBetween + line + '\n');
        } else {
          const descriptionPadding = ' '.repeat(UI_HELP.X_DESCRIPTION_OFFSET);
          this.print(descriptionPadding + line + '\n');
        }
      });

      this.print('\n');
    });

    this.print('\n');
    const footerLines = this.consoleService.splitWordsByWidth(
      HELP_FOOTER,
      maxWidth,
    );
    footerLines.forEach((line) => this.print(line + '\n'));
  }

  clear(): void {
    for (let row = MARGINS.ROW_RESULTS_START; row < this.terminal.rows; row++) {
      this.clearLine(row);
    }
  }
}
```

## File: `src/cli/ui/components/help/help.constants.ts`
```typescript
/* eslint-disable quotes */
import pc from 'picocolors';

interface HelpSection {
  id: string;
  title: string;
  icon: string;
  content: string[];
}

export const HELP_SECTIONS: HelpSection[] = [
  {
    id: 'welcome',
    title: 'Welcome',
    icon: '👋',
    content: [
      pc.bold('Welcome to npkill!'),
      '',
      'Npkill helps you find and manage "junk" directories',
      'left behind by development tools.',
      '',
      'These folders are essential while working on projects,',
      'but over time they pile up, eating tons of space long',
      "after you've moved on.",
      '',
      'Npkill scans your directories, lists these folders with',
      'their sizes, and shows when you last touched each project,',
      'so you can quickly decide what to keep and what to clean.',
      '',
      pc.green(pc.bold('Easy and powerful!')),
    ],
  },
  {
    id: 'shortcuts',
    title: 'Quick Reference',
    icon: '⌨️',
    content: [
      pc.cyan(pc.bold('Navigation')),
      `  ${pc.green('↑/↓ or j/k')}       Move cursor.`,
      `  ${pc.green('←/→ or h/l')}       Switch panels.`,
      `  ${pc.green('PgUp/PgDown')}      Fast scroll.`,
      `  ${pc.green('Home/End')}         Jump to first/last.`,
      '',
      pc.cyan(pc.bold('Actions (normal mode)')),
      `  ${pc.green('SPACE / DEL')}      Delete folder.`,
      `  ${pc.green('o')}                Open parent folder.`,
      `  ${pc.green('/')}                Search (Regex supported).`,
      `  ${pc.green('t')}                Enter ${pc.green('multi-select mode')}.`,
      '',
      pc.cyan(pc.bold('Actions (multi-select mode)')),
      `  ${pc.green('t')}                Back to ${pc.green('normal mode')} without delete.`,
      `  ${pc.green('v')}                Range selection.`,
      `  ${pc.green('a')}                Select/deselect all.`,
      `  ${pc.green('SPACE')}            Select/deselect current.`,
      `  ${pc.green('ENTER')}            Delete selected folders.`,
      '',
      pc.cyan(pc.bold('Others')),
      `  ${pc.green('e')}                Show errors.`,
      `  ${pc.green('q / ESC')}          Quit npkill.`,
    ],
  },
  {
    id: 'header',
    title: 'Header Info',
    icon: '📊',
    content: [
      pc.bold('Understanding the header'),
      '',
      pc.bold(pc.green('Potential Space')),
      'The total size of all detected directories.',
      'This represents the maximum possible space you could',
      'free if you deleted everything.',
      '',
      pc.bold(pc.green('Freed Space')),
      'The space actually recovered in this session.',
      '',
      pc.bold(pc.green('Last Modified (age)')),
      'Shows when the last file in the parent workspace was',
      'modified. This helps identify abandoned projects.',
      '',
      pc.dim('Note: This checks the entire parent directory,'),
      pc.dim('not just the target folder itself.'),
      '',
      pc.bold(pc.green('Progress Bar')),
      'The progress bar has 3 color-coded parts:',
      '',
      ` ${pc.green('▀▀▀▀')} Green  → Results ready (stats calculated)`,
      ` ${pc.white('▀▀▀▀')} White  → Directories examined`,
      ` ${pc.gray('▀▀▀▀')} Gray   → Pending to be analyzed`,
      '',
      'Full bar example:',
      ` ${pc.green('▀▀▀▀▀▀▀')}${pc.white('▀▀▀▀')}${pc.gray('▀▀▀▀▀▀▀▀▀▀▀')}`,
    ],
  },
  {
    id: 'warnings',
    title: 'Warnings',
    icon: '⚠️',
    content: [
      pc.bold(pc.yellow('Important: Not all results are safe to delete!')),
      '',
      'Some applications (VSCode, Discord, Slack, etc.) need',
      'their dependencies to work. If their directory is deleted,',
      'the application will probably break until dependencies',
      'are reinstalled.',
      '',
      'Npkill will try to detect this folders and show "⚠️"',
      'alongside the result and mark it as "sensitive".',
      '',
      '',
      pc.bold(pc.green('Pro tip')),
      'Use the Info panel (→) to see more information',
      'about why a folder is flagged.',
    ],
  },
  {
    id: 'panels',
    title: 'Panels',
    icon: '📋',
    content: [
      pc.bold('Understanding the interface'),
      '',
      pc.bold(pc.cyan('Delete Panel (Main)')),
      'Lists all found directories with their sizes.',
      'Navigate with arrow keys or j/k.',
      'Press SPACE to delete a folder.',
      'Press → to see details.',
      '',
      pc.bold(pc.cyan('Info Panel')),
      'Shows details of the selected result. Plus notes',
      'that might be useful to you.',
      '',
      pc.bold(pc.cyan('Options Panel')),
      'Configure npkill settings on the fly.',
      '',
      pc.bold(pc.cyan('Help Panel (You are here!)')),
      'Navigate through help sections.',
      'Use ↑/↓ to change sections.',
      'Scroll content with j/k or arrow keys.',
    ],
  },
  //   { // TODO pending to add .npkillrc support
  //     id: 'config',
  //     title: 'Configuration',
  //     icon: '⚙️',
  //     content: [
  //       colors.bold('Customizing npkill with .npkillrc'),
  //       '',
  //       colors.bold.cyan('What is .npkillrc?'),
  //       'A configuration file where you can set your default',
  //       'preferences, custom profiles, and target folders.',
  //       '',
  //       colors.bold.cyan('Location'),
  //       '',
  //       'Place it in your home directory:',
  //       colors.dim('  ~/.npkillrc'),
  //       '',
  //       'Or load from a custom location:',
  //       colors.green('  npkill --config /path/to/config'),
  //       '',
  //       colors.bold.cyan('Example Configuration'),
  //       '',
  //       colors.dim('{'),
  //       colors.dim('  "targets": ["node_modules", ".venv", "target"],'),
  //       colors.dim('  "exclude": [".git", "important-project"],'),
  //       colors.dim('  "sortBy": "size",'),
  //       colors.dim('  "excludeSensitiveResults": true,'),
  //       colors.dim('  "profiles": {'),
  //       colors.dim('    "mystack": {'),
  //       colors.dim('      "targets": ["node_modules", "venv", "target"]'),
  //       colors.dim('    }'),
  //       colors.dim('  }'),
  //       colors.dim('}'),
  //       '',
  //       colors.bold.cyan('Available Options'),
  //       `${colors.green('targets')}              Target folder names to search`,
  //       `${colors.green('exclude')}              Directories to skip`,
  //       `${colors.green('sortBy')}               Default sort (size/path/age)`,
  //       `${colors.green('sizeUnit')}             Display unit (auto/mb/gb)`,
  //       `${colors.green('profiles')}             Custom profile definitions`,
  //     ],
  //   },
  {
    id: 'profiles',
    title: 'Profiles',
    icon: '📦',
    content: [
      pc.bold('Working with profiles'),
      '',
      pc.bold(pc.cyan('What are profiles?')),
      'Profiles are presets of target folders for different',
      'programming languages and tools.',
      '',
      pc.bold(pc.cyan('Usage')),
      'List available profiles:',
      pc.green('  npkill -p'),
      '',
      'Single profile:',
      pc.green('  npkill -p node'),
      '',
      'Multiple profiles:',
      pc.green('  npkill -p node,python,java'),
      '',
      // colors.bold.cyan('Custom Profiles'),
      //   'Define your own in .npkillrc:',
      //   '',
      //   colors.dim('"profiles": {'),
      //   colors.dim('  "webdev": {'),
      //   colors.dim('    "targets": ["node_modules", "dist", ".next"]'),
      //   colors.dim('  }'),
      //   colors.dim('}'),
      //   '',
      //   'Then use:',
      // colors.green('  npkill -p webdev'),
    ],
  },
  {
    id: 'tips',
    title: 'Tips & Tricks',
    icon: '💡',
    content: [
      pc.bold('Get the most out of npkill'),
      '',
      pc.bold(pc.cyan('1. Use profiles')),
      '   Start with profiles for common tools:',
      `   ${pc.green('npkill -p node,python,java')}.`,
      '',
      pc.bold(pc.cyan('2. Sort intelligently')),
      '   Sort by size to find the biggest space hogs:',
      `   ${pc.green('npkill --sort size')}`,
      '   Or by age to find abandoned projects.',
      '',
      pc.bold(pc.cyan('3. Exclude what you need')),
      '   Protect important directories:',
      `   ${pc.green('npkill -E ".git,important_project"')}`,
      '',
      pc.bold(pc.cyan('4. Try dry-run mode')),
      '   Test without risk using --dry-run.',
      '   Nothing is deleted! (simulated with delay).',
      '',
      pc.bold(pc.cyan('5. Multi-select workflow')),
      '   Press "t" to enter selection mode.',
      '   Mark folders with SPACE.',
      '   Press ENTER to delete all at once.',
      '',
      '   Press "v" on first item.',
      '   Move to last item and press "v" again.',
      '   All items in between are selected!',
      '',
      pc.bold(pc.cyan('6. Check details first')),
      '   Unsure about a result? Press → to see',
      '   more details.',
    ],
  },
  {
    id: 'about',
    title: 'About',
    icon: 'ℹ️',
    content: [
      pc.bold('About npkill'),
      '',
      'Npkill, a tool designed to help developers',
      'reclaim disk space by finding and removing',
      'unnecessary dependency folders.',
      '',
      pc.bold(pc.cyan('Get Involved')),
      'GitHub: github.com/voidcosmos/npkill',
      'Report bugs, request features, contribute!',
      '',
      pc.bold(pc.cyan('License')),
      'MIT License - Free and open source.',
      '',
      '',
      pc.dim('Made with ❤️'),
    ],
  },
];
```

## File: `src/cli/ui/components/help/help.ui.ts`
```typescript
import { MARGINS } from '../../../../constants/main.constants.js';
import { BaseUi, InteractiveUi } from '../../base.ui.js';
import { IKeyPress } from '../../../interfaces/key-press.interface.js';
import { Subject } from 'rxjs';
import pc from 'picocolors';
import { HELP_SECTIONS } from './help.constants.js';

export class HelpUi extends BaseUi implements InteractiveUi {
  resultIndex = 0;

  readonly goToOptions$ = new Subject<null>();

  private selectedSection = 0;
  private scrollOffset = 0;
  private readonly INDEX_WIDTH = 23;
  private readonly SCROLL_STEP = 2;

  private readonly KEYS = {
    up: () => this.previousSection(),
    down: () => this.nextSection(),
    k: () => this.scrollUp(),
    j: () => this.scrollDown(),
    u: () => this.scrollPageUp(),
    d: () => this.scrollPageDown(),
    pageup: () => this.scrollPageUp(),
    pagedown: () => this.scrollPageDown(),
    home: () => this.scrollToTop(),
    end: () => this.scrollToBottom(),
    right: () => this.goToOptions(),
    l: () => this.goToOptions(),
    q: () => this.goToOptions(),
    escape: () => this.goToOptions(),
    return: () => this.selectSection(),
  };

  constructor() {
    super();
  }

  private previousSection(): void {
    if (this.selectedSection > 0) {
      this.selectedSection--;
      this.scrollOffset = 0;
      this.render();
    }
  }

  private nextSection(): void {
    if (this.selectedSection < HELP_SECTIONS.length - 1) {
      this.selectedSection++;
      this.scrollOffset = 0;
      this.render();
    }
  }

  private selectSection(): void {
    this.scrollOffset = 0;
    this.render();
  }

  private scrollUp(): void {
    if (this.scrollOffset > 0) {
      this.scrollOffset = Math.max(0, this.scrollOffset - this.SCROLL_STEP);
      this.render();
    }
  }

  private scrollDown(): void {
    const currentSection = HELP_SECTIONS[this.selectedSection];
    const contentHeight = this.getContentAreaHeight();
    const maxScroll = Math.max(
      0,
      currentSection.content.length - contentHeight,
    );

    if (this.scrollOffset < maxScroll) {
      this.scrollOffset = Math.min(
        maxScroll,
        this.scrollOffset + this.SCROLL_STEP,
      );
      this.render();
    }
  }

  private scrollPageUp(): void {
    const pageSize = this.getContentAreaHeight() - 2;
    this.scrollOffset = Math.max(0, this.scrollOffset - pageSize);
    this.render();
  }

  private scrollPageDown(): void {
    const currentSection = HELP_SECTIONS[this.selectedSection];
    const contentHeight = this.getContentAreaHeight();
    const pageSize = contentHeight - 2;
    const maxScroll = Math.max(
      0,
      currentSection.content.length - contentHeight,
    );

    this.scrollOffset = Math.min(maxScroll, this.scrollOffset + pageSize);
    this.render();
  }

  private scrollToTop(): void {
    this.scrollOffset = 0;
    this.render();
  }

  private scrollToBottom(): void {
    const currentSection = HELP_SECTIONS[this.selectedSection];
    const contentHeight = this.getContentAreaHeight();
    this.scrollOffset = Math.max(
      0,
      currentSection.content.length - contentHeight,
    );
    this.render();
  }

  private goToOptions(): void {
    this.clear();
    this.goToOptions$.next(null);
  }

  private getContentAreaHeight(): number {
    return this.terminal.rows - MARGINS.ROW_RESULTS_START - 4;
  }

  onKeyInput({ name }: IKeyPress): void {
    const action: (() => void) | undefined = this.KEYS[name];
    if (action === undefined) {
      return;
    }
    action();
  }

  render(): void {
    this.clear();
    const startRow = MARGINS.ROW_RESULTS_START;
    const contentAreaHeight = this.getContentAreaHeight();

    // Header hint
    this.printAt(
      pc.dim('Use ') +
        pc.green('↑/↓') +
        pc.dim(' to change section, ') +
        pc.green('j/k') +
        pc.dim(' to scroll.'),
      { x: 2, y: startRow },
    );

    this.drawIndex(startRow + 2);
    this.drawContent(startRow + 2, contentAreaHeight);
  }

  private drawIndex(startRow: number): void {
    const indexHeight = this.terminal.rows - startRow - 1;

    this.printAt(pc.gray('╭' + '─'.repeat(this.INDEX_WIDTH - 2) + '╮'), {
      x: 2,
      y: startRow - 1,
    });

    for (let i = 0; i < Math.min(HELP_SECTIONS.length, indexHeight); i++) {
      const section = HELP_SECTIONS[i];
      const isSelected = i === this.selectedSection;

      const padding = ' '.repeat(
        Math.max(0, this.INDEX_WIDTH - section.title.length - 6),
      );
      const line = ` ${section.icon} ${section.title}${padding}`;

      if (isSelected) {
        this.printAt(pc.gray('│') + pc.bgCyan(pc.black(line)) + pc.gray('│'), {
          x: 2,
          y: startRow + i,
        });
      } else {
        this.printAt(pc.gray('│') + pc.white(line) + pc.gray('│'), {
          x: 2,
          y: startRow + i,
        });
      }
    }

    const bottomRow = startRow + Math.min(HELP_SECTIONS.length, indexHeight);
    this.printAt(pc.gray('╰' + '─'.repeat(this.INDEX_WIDTH - 2) + '╯'), {
      x: 2,
      y: bottomRow,
    });
  }

  private drawContent(startRow: number, contentHeight: number): void {
    const currentSection = HELP_SECTIONS[this.selectedSection];
    const contentStartX = this.INDEX_WIDTH + 2;
    const contentWidth = Math.max(
      20,
      this.terminal.columns - contentStartX - 4,
    );

    this.printAt(pc.gray('╭' + '─'.repeat(contentWidth) + '╮'), {
      x: contentStartX,
      y: startRow - 1,
    });

    const visibleContent = currentSection.content.slice(
      this.scrollOffset,
      this.scrollOffset + contentHeight,
    );

    for (let i = 0; i < contentHeight; i++) {
      const line = visibleContent[i] || '';

      const padding = ' '.repeat(
        Math.max(0, contentWidth - this.getStringWidth(line) - 1),
      );
      this.printAt(pc.gray('│ ') + line + padding + pc.gray('│'), {
        x: contentStartX,
        y: startRow + i,
      });
    }

    this.printAt(pc.gray('╰' + '─'.repeat(contentWidth) + '╯'), {
      x: contentStartX,
      y: startRow + contentHeight,
    });
  }

  /** Get real width, removing ANSI color codes. */
  private getStringWidth(str: string): number {
    // eslint-disable-next-line no-control-regex
    return str.replace(/\u001b\[[0-9;]*m/g, '').length;
  }

  clear(): void {
    for (let row = MARGINS.ROW_RESULTS_START; row < this.terminal.rows; row++) {
      this.clearLine(row);
    }
  }
}
```

## File: `src/constants/cli.constants.ts`
```typescript
import { ICliOptions } from '../cli/interfaces/index.js';
import pc from 'picocolors';

export const OPTIONS: ICliOptions[] = [
  {
    arg: ['-p', '--profiles'],
    description:
      'Specifies profiles (presets) of folders to search, separated by commas (e.g., `-p python,java`, `-p all`). If used without a value, lists the available profiles. Default: `node`.',
    name: 'profiles',
  },
  {
    arg: ['--config'],
    description:
      'Path to a custom .npkillrc configuration file. By default, npkill looks for ~/.npkillrc.',
    name: 'config',
  },
  {
    arg: ['-d', '--directory'],
    description:
      'Set directory from which to start searching. By default, starting-point is .',
    name: 'directory',
  },
  {
    arg: ['-D', '--delete-all'],
    description: 'Auto-delete all target folders that are found.',
    name: 'delete-all',
  },
  {
    arg: ['-y'],
    description: 'Avoid displaying a warning when executing --delete-all.',
    name: 'yes',
  },
  {
    arg: ['-e', '--hide-errors'],
    description: 'Hide errors if any.',
    name: 'hide-errors',
  },
  {
    arg: ['-E', '--exclude'],
    description:
      'Exclude directories from search (directory list must be inside double quotes "", each directory separated by "," ) Example: "ignore1,ignore2"',
    name: 'exclude',
  },
  {
    arg: ['-f', '--full'],
    description:
      'Start searching from the home of the user (example: "/home/user" in linux).',
    name: 'full-scan',
  },
  {
    arg: ['--size-unit'],
    description:
      'Set the unit for displaying folder sizes. Options: auto (default), mb, gb. With auto, sizes < 1024MB are shown in MB, larger sizes in GB.',
    name: 'size-unit',
  },
  {
    arg: ['-h', '--help', '?'],
    description: 'Show this help page, with all options.',
    name: 'help',
  },
  {
    arg: ['-nu', '--no-check-update'],
    description: 'Dont check for updates on startup.',
    name: 'no-check-updates',
  },
  {
    arg: ['-s', '--sort'],
    description:
      'Sort results by: size, path or age (last time the most recent file was modified in the workspace)',
    name: 'sort-by',
  },
  {
    arg: ['-t', '--targets'],
    description:
      'Disable profiles feature and specify the name of the directories you want to search for. You can define multiple targets separating with comma. Ej. `-t node_modules,.cache`.',
    name: 'target-folders',
  },
  {
    arg: ['-x', '--exclude-sensitive'],
    description: 'Exclude sensitive directories.',
    name: 'exclude-sensitive',
  },
  {
    arg: ['--dry-run'],
    description:
      'It does not delete anything (will simulate it with a random delay).',
    name: 'dry-run',
  },
  {
    arg: ['--json-stream'],
    description: 'Output results in a stream JSON format.',
    name: 'jsonStream',
  },
  {
    arg: ['--json'],
    description: 'Output results in a JSON format.',
    name: 'jsonSimple',
  },
  {
    arg: ['-v', '--version'],
    description: 'Show version.',
    name: 'version',
  },
];

const getHeader = (title: string) => {
  return pc.black(pc.bgYellow(pc.bold(` ${title} `)));
};

export const HELP_HEADER = `Npkill helps you find and manage “junk” directories left behind by development tools.
These folders are essential while you’re actively working on a project, but over time they pile up, eating tons of space long after you’ve moved on.
Npkill scans your directories, lists these directories with their sizes, and shows when you last touched each project, so you can quickly decide what to keep and what to clean. Easy!

${getHeader('How to interact')}
 ${pc.green('SPACE / DEL')}             Delete selected result.
 ${pc.green('↑ / k')}                   Move up.
 ${pc.green('↓ / j')}                   Move down.
 ${pc.green('→ / ←')}                   Switch between panels.
 ${pc.green('t')}                       Multi-selection mode.
 ${pc.green('PgUp / Ctrl+u / u / h')}   Move one page up.
 ${pc.green('PgDown / Ctrl+d / d / l')} Move one page down.
 ${pc.green('Home, End')}               Jump to first / last result.
 ${pc.green('o')}                       Open the parent directory.
 ${pc.green('/')}                       Search (Regex supported).
 ${pc.green('e')}                       Show errors.
 ${pc.green('q')}                       Quit.`;

export const HELP_PROGRESSBAR = `${getHeader('Header information')}
${pc.green('Potential space')}: The total size of all detected directories. Not everything needs to be deleted. This represents the maximum possible space you could free.
${pc.green('Freed space')}: The space actually recovered in this session.

The progress bar provides information on the search process. It has 3 parts differentiated by colors.

 (green) Results ready (stats calculated).
    🭲  (white) Directories examined.
    🭲     🭲     ┌ (gray) Directories pending to be analyzed.
 ${pc.green('▀▀▀▀▀▀▀')}${pc.white('▀▀▀▀')}${pc.gray('▀▀▀▀▀▀▀▀▀▀▀')}

The header will also display other relevant contextual information, such as when selection mode is activated or npkill is started in "dry-run mode".
`;

export const HELP_FOOTER = `${getHeader('Important note')}
${pc.bold('Not all results listed are bad!')} Some applications (like vscode, Discord, etc) need those dependencies to work. If their directory is deleted, the application will probably break (until the dependencies are reinstalled). NPKILL will try to show you these results by highlighting them ⚠️.`;

export const COLORS = {
  red: 'bgRed',
  green: 'bgGreen',
  yellow: 'bgYellow',
  blue: 'bgBlue',
  magenta: 'bgMagenta',
  cyan: 'bgCyan',
  white: 'bgWhite',
};
```

## File: `src/constants/index.ts`
```typescript
export * from './cli.constants.js';
export * from './main.constants.js';
export * from './messages.constants.js';
export * from './sort.result.js';
export * from './spinner.constants.js';
export * from './update.constants.js';
export * from './options.constants.js';
export * from './result-descriptions.constants.js';
```

## File: `src/constants/main.constants.ts`
```typescript
import { DEFAULT_PROFILE } from '../core/constants/index.js';
import { IConfig } from '../cli/interfaces/index.js';

export const MIN_CLI_COLUMNS_SIZE = 60;
export const CURSOR_SIMBOL = '~>';
export const WIDTH_OVERFLOW = '...';
export const DEFAULT_SIZE = '0 MB';
export const DECIMALS_SIZE = 2;
export const OVERFLOW_CUT_FROM = 11;

export const DEFAULT_CONFIG: IConfig = {
  profiles: [DEFAULT_PROFILE],
  folderRoot: '',
  checkUpdates: true,
  deleteAll: false,
  dryRun: false,
  exclude: [],
  excludeSensitiveResults: false,
  sizeUnit: 'auto',
  maxSimultaneousSearch: 6,
  showErrors: true,
  sortBy: 'none',
  targets: ['node_modules'],
  yes: false,
  jsonStream: false,
  jsonSimple: false,
};

export const MARGINS = {
  FOLDER_COLUMN_END: 16,
  FOLDER_COLUMN_START: 1,
  FOLDER_SIZE_COLUMN: 10,
  ROW_RESULTS_START: 8,
};

export const UI_HELP = {
  X_COMMAND_OFFSET: 3,
  X_DESCRIPTION_OFFSET: 27,
  Y_OFFSET: 2,
  MAX_WIDTH: 80,
};

export const UI_POSITIONS = {
  FOLDER_SIZE_HEADER: { x: -1, y: 7 }, // x is calculated in controller
  INITIAL: { x: 0, y: 0 },
  VERSION: { x: 30, y: 5 },
  DRY_RUN_NOTICE: { x: 1, y: 6 },
  NEW_UPDATE_FOUND: { x: 42, y: 0 },
  SPACE_RELEASED: { x: 43, y: 3 },
  STATUS: { x: 43, y: 4 },
  STATUS_BAR: { x: 43, y: 5 },
  PENDING_TASKS: { x: 43, y: 6 }, //Starting position. It will then be replaced.
  TOTAL_SPACE: { x: 43, y: 2 },
  ERRORS_COUNT: { x: 43, y: 1 },
  TUTORIAL_TIP: { x: 1, y: 7 },
  WARNINGS: { x: 0, y: 9 },
  RESULTS_TYPES_COUNT_ROW_1: { x: 73, y: 1 },
  RESULTS_TYPES_COUNT_ROW_2: { x: 73, y: 2 },
  RESULTS_TYPES_COUNT_ROW_3: { x: 73, y: 3 },
  RESULTS_TYPES_COUNT_ROW_4: { x: 73, y: 4 },
  RESULTS_TYPES_COUNT_ROW_5: { x: 73, y: 5 },
};

// export const VALID_KEYS: string[] = [
//   'up', // Move up
//   'down', // Move down
//   'space', // Delete
//   'j', // Move down
//   'k', // Move up
//   'h', // Move page down
//   'l', // Move page up
//   'u', // Move page up
//   'd', // Move page down
//   'pageup',
//   'pagedown',
//   'home', // Move to the first result
//   'end', // Move to the last result
//   'e', // Show errors
// ];

export const BANNER = `                  __   .__.__  .__
     ____ ______ |  | _|__|  | |  |
    /    \\\\____ \\|  |/ /  |  | |  |
   |   |  \\  |_> >    <|  |  |_|  |__
   |___|  /   __/|__|_ \\__|____/____/
        \\/|__|        \\/`;

export const STREAM_ENCODING = 'utf8';
```

## File: `src/constants/messages.constants.ts`
```typescript
export const MENU_BAR = {
  HELP: 'Help',
  OPTIONS: 'Options',
  DELETE: 'Delete',
  INFO: 'Info',
};

export const INFO_MSGS = {
  DELETED_FOLDER: '[DELETED] ',
  DELETING_FOLDER: '[..deleting..] ',
  ERROR_DELETING_FOLDER: '[ ERROR ] ',
  HEADER_COLUMNS: 'Age    Size', // Δ (delta) for last_mod/age?
  HELP_TITLE: ' NPKILL HELP ',
  MIN_CLI_CLOMUNS:
    'Oh no! The terminal is too narrow. Please, ' +
    'enlarge it (This will be fixed in future versions. Disclose the inconveniences)',
  NEW_UPDATE_FOUND: 'New version found! npm i -g npkill for update.',
  NO_VALID_SORT_NAME: 'Invalid sort option. Available: path | size | age',
  NO_VALID_SIZE_UNIT: 'Invalid size-unit option. Available: auto | mb | gb',
  STARTING: 'Initializing ',
  SEARCHING: 'Searching ',
  CALCULATING_STATS: 'Calculating stats ',
  FATAL_ERROR: 'Fatal error ',
  SEARCH_COMPLETED: 'Search completed ',
  SPACE_RELEASED: 'Space saved: ',
  TOTAL_SPACE: 'Releasable space: ',
  DRY_RUN: 'Dry run mode',
  DELETE_ALL_WARNING:
    '    --delete-all may have undesirable effects and\n' +
    '    delete dependencies needed by some applications.\n' +
    '    Recommended to use -x and preview with --dry-run.\n\n' +
    '                 Press y to continue.\n\n' +
    '           pass -y to not show this next time',
};

export const ERROR_MSG = {
  CANT_DELETE_FOLDER:
    'The directory cannot be deleted. Do you have permission?',
  CANT_GET_REMOTE_VERSION: 'Couldnt check for updates',
  CANT_USE_BOTH_JSON_OPTIONS:
    'Cannot use both --json and --json-stream options simultaneously.',
};
```

## File: `src/constants/options.constants.ts`
```typescript
import pc from 'picocolors';

export const OPTIONS_HINTS_BY_TYPE = {
  input: pc.gray(
    `${pc.bold(pc.underline('SPACE'))} or ${pc.bold(pc.underline('ENTER'))} to edit.`,
  ),
  'input-exit': pc.gray(
    `${pc.bold(pc.underline('ENTER'))} to confirm. ${pc.bold(pc.underline('ESC'))} To cancel.`,
  ),
  dropdown: pc.gray(
    `${pc.bold(pc.underline('SPACE'))}/${pc.bold(pc.underline('SHIFT'))}+${pc.bold(pc.underline('SPACE'))} to navigate.`,
  ),
  checkbox: pc.gray(
    `${pc.bold(pc.underline('SPACE'))} or ${pc.bold(pc.underline('ENTER'))} to toggle.`,
  ),
};
```

## File: `src/constants/os-service-map.constants.ts`
```typescript
import {
  UnixFilesService,
  WindowsFilesService,
} from '../core/services/files/index.js';

/**
 * A mapping of operating system names to their corresponding file service classes.
 * This map is used to dynamically instantiate the appropriate file service based on the OS.
 */
export const OSServiceMap = {
  linux: UnixFilesService,
  darwin: UnixFilesService,
  win32: WindowsFilesService,
};
```

## File: `src/constants/result-descriptions.constants.ts`
```typescript
/* eslint-disable quotes */
///////////
// IMPORTANT: Keys must be lowercase to match lookup logic
///////////

export const RESULT_TYPE_INFO = {
  // =====================
  // Node.js / JavaScript
  // =====================
  node_modules:
    "Holds all the Node packages your project depends on. Can get huge. Deleting it won't hurt. Just run `npm install` to restore it.",
  dist: 'Distribution/build output: compiled, minified, and ready to ship. Delete and rebuild when needed. Commonly used by Node.js, Python, and many other build tools.',
  build:
    'Generic build output. Like a photocopy of your source: disposable and regenerable. WARNING: Generic name; verify contents before deleting.',
  bower_components:
    'Old-school Bower package folder. If you still have this, congrats on archaeological findings.',
  jspm_packages: 'JSPM packages cache. Safe to delete. Reinstall will fix it.',
  '.npm':
    "npm's local cache folder. Free up space if you don't mind re-downloading packages.",
  '.pnpm-store':
    "pnpm's global store. Deleting it frees space but pnpm will re-populate it on next install.",
  '.yarn':
    "Yarn v2+ folder (cache, plugins, etc.). Not strictly 'junk' but can be regenerated.",
  '.cache':
    'Generic cache folder used by many tools (babel, webpack, rollup, etc.). Delete to force fresh work.',
  //   '.cache/webpack':
  //     "Webpack's cache area. Deleting it will make the next build slower but deterministic.",
  //   '.cache/babel-loader':
  //     'Babel/Webpack loader cache. Safe to remove  transforms will re-run.',
  '.parcel-cache':
    "Parcel's cache. Big and regenerable: delete it and Parcel will rebuild from scratch.",
  '.rpt2_cache':
    'Rollup/TypeScript cache (sometimes created by rollup-plugin-typescript2). Safe to delete.',
  '.vite':
    "Vite's prebundle cache (often node_modules/.vite). Delete to force fresh dependency prebundling.",

  // =====================
  // Frontend Frameworks
  // =====================
  '.next':
    'Next.js build/cache folder. Contains server bundles, static files, and caches. Delete to rebuild: Next will regenerate.',
  '.nuxt':
    'Nuxt build folder (compiled server + client pieces). Safe to delete; run your build step to recreate.',
  '.svelte-kit':
    'SvelteKit build artifacts and caches. Delete to force a fresh build.',
  '.astro':
    "Astro's build/cache directory. Safe to remove; Astro will recompile.",
  '.angular':
    'Angular CLI cache and build metadata. Can grow large: delete to force a full rebuild (`ng build` will recreate it).',
  out: "Next.js/Static export output (often named `out`). Safe to delete: it's generated by `next export` or similar. WARNING: Generic name; some IDEs also use `out` for build output.",
  '.expo':
    'Expo project cache and metadata. Safe to trash; `expo start` will rebuild.',
  '.expo-shared':
    'Expo shared assets metadata. Deletable: Expo will recreate it.',
  '.nx': 'Nx workspace cache. Blow it away to force cold builds.',
  '.turbo':
    'Turborepo incremental cache. Nuke to re-run everything from scratch.',
  'storybook-static':
    'Storybook static build output. Delete and rebuild when needed.',
  gatsby_cache:
    'Gatsby build cache (.cache folder) and public output. `.cache` (internal build cache) and `public` (static output). `public` is safe to delete; `.cache` will be rebuilt. WARNING: This description refers to the cache specifically, not the public folder.',
  public:
    'Generic static site output (Hugo, Gatsby, others). Toss it: your build will regenerate. WARNING: Some projects use `public` for source assets, not build output. Verify before deleting!',
  _site:
    'Eleventy/Hugo/Jekyll static output (`_site` for Jekyll/Eleventy). Safe to clear and rebuild.',
  '.vercel':
    'Vercel project/deploy metadata. Usually safe to delete locally but may contain deploy hints.',
  '.now': 'Legacy Zeit/Now deploy data. Safe to remove.',
  '.netlify':
    "Netlify config/cache data. Safe to remove locally if you don't need historical deploy data.",

  // =====================
  // Web bundlers / tool caches
  // =====================
  '.cache-loader':
    'Loader cache used by some bundlers to speed builds. Delete to force cold builds.',
  '.swc': 'SWC cache (if present). Regenerable by your build tools.',
  '.esbuild':
    'esbuild cache area. Safe to delete: esbuild will re-run transforms.',
  '.rollup.cache':
    'Rollup cache dir (if configured). Zap it to rebuild bundles.',
  '.toiletd':
    "Okay this one is a joke: you won't see it. But seriously, caches are safe to delete.",

  // =====================
  // Test / Coverage / CI
  // =====================
  coverage:
    'Test coverage reports (nyc/istanbul). Useful for CI, but fully regenerable.',
  '.nyc_output':
    "nyc's raw coverage output. Safe to delete: coverage will be recomputed.",
  '.jest':
    'Possible Jest cache or artifacts. Deleting may slow the next test run.',
  //   '.cache/jest':
  //     'Jest cache area. Safe to remove if you want tests to start fresh.',
  '.tap-snapshots':
    'Snapshot/test cache. Deleting removes recorded snapshots: be cautious if you rely on them.',
  'playwright-report':
    'Playwright HTML report output. Delete after peeking at the pretty charts.',
  'test-results': 'Generic test results folder (often Playwright). Disposable.',
  cypress:
    'Cypress artifacts (screenshots/videos/logs). Delete if you don’t need recordings from past runs.',

  // =====================
  // Lint / Formatter caches
  // =====================
  '.eslintcache':
    "ESLint cache file. Deleting will make linting slower the first run but won't break anything.",
  '.prettiercache': 'Prettier cache (rare). Safe to remove.',
  '.stylelintcache': 'Stylelint cache. Safe to nuke; it will be recreated.',

  // =====================
  // Editors / IDEs / Local configs
  // =====================
  '.idea':
    'JetBrains IDE project files (workspace settings, caches, etc.). Not build artifacts but can be large: treat with care. WARNING: Contains run configurations, code style settings, and custom tool windows. Usually committed to Git in team projects.',
  '.vscode':
    "VS Code workspace settings and local state. Contains editor preferences, debug configs, etc. Generally safe to remove if you don't share workspace settings. WARNING: Deleting removes custom debug configurations and tasks.",
  '.history':
    'Local editor history (varies by plugin). Can be deleted to shrink repo clones.',
  '.sublime-workspace':
    "Sublime Text workspace state. Safe to remove if you don't need session restore.",
  '.bloop':
    'Scala build server metadata. Deleting will make the next import slower.',
  '.metals': 'Scala Metals IDE cache. Safe to delete; Metals will re-index.',
  '.gradle':
    "Gradle's cache and wrapper downloads. Deleting forces Gradle to re-download dependencies: slows builds but ok.",

  // =====================
  // OS / miscellaneous files (often found in repos)
  // =====================
  '.ds_store':
    'macOS Finder metadata file. This is a file, not folder. Safe to delete.',
  'thumbs.db':
    'Windows image thumbnail cache. This is a file, not folder. Safe to delete.',
  '.vagrant':
    "Vagrant VM state: deleting frees space but you'll lose VM state; recreate with `vagrant up`.",
  '.terraform':
    'Terraform working dir (providers/modules cache). Safe to delete; `terraform init` will re-download.',

  // =====================
  // Package managers / lockstores
  // =====================
  vendor:
    "Composer's PHP dependency folder (or Go vendor folder). Delete and run `composer install` (PHP) or rebuild (Go) to restore. WARNING: Different meaning in PHP vs Go contexts.",
  '.composer': 'Composer global cache/dir. Regenerable by Composer.',
  '.m2':
    'Maven local repository (usually in user home ~/.m2/repository). Contains all downloaded Maven dependencies. Huge sometimes: can be cleaned but re-downloading takes time.',
  '.bundle':
    'Ruby Bundler settings/cache. Safe to remove; `bundle install` will recreate bits.',
  packages:
    'Old .NET/NuGet packages folder (pre-PackageReference style). You can restore with your package manager. WARNING: Verify this is build output, not a source directory containing actual project packages.',

  // =====================
  // Java / JVM
  // =====================
  target:
    'Maven `target` folder (Java) or Cargo `target` folder (Rust). Contains compiled classes and packaged artifacts. Safe to delete and rebuild. WARNING: Generic name used by multiple build systems.',
  out_java: 'IDE/build `out` folder containing compiled classes. Rebuildable.',
  build_classes: 'Generated class files. Safe to delete.',
  '.settings':
    'Eclipse project settings. Not build output, but safe to regenerate.',
  '.classpath':
    'Eclipse metadata. File/dir you can regenerate by re-importing the project.',
  '.project': 'Eclipse project definition. Can be re-created by the IDE.',

  // =====================
  // .NET / C#
  // =====================
  bin: "Compiled binaries folder (used by many ecosystems: .NET, Go, etc.). Delete to rebuild cleanly. WARNING: Very generic name; verify it's build output, not source binaries.",
  obj: 'Intermediate object files (.NET, C++, Unity). Deleting forces a full recompile next time. Safe to delete.',
  '.vs':
    'Visual Studio local workspace data. Safe to delete; VS will rehydrate it.',
  TestResults: 'Visual Studio/.NET test result output. Toss it after runs.',
  artifacts:
    'Generic build artifacts folder used by many .NET repos. Generated: safe to purge and rebuild.',

  // =====================
  // Python
  // =====================
  venv: 'A self-contained Python environment with its own packages. Delete to start fresh, then recreate with `python -m venv venv`.',
  env: 'Another virtual environment name. Same deal as `venv`.',
  __pycache__:
    'Python bytecode caches (.pyc). Safe to delete: Python will recreate them.',
  '.pytest_cache':
    'Pytest cache. Delete to forget previous runs; tests will run fresh.',
  pipenv:
    "Pipenv's virtualenv location (usually in user home directory, not project). Regenerable by Pipenv. WARNING: Typically stored globally, not in project directory.",
  '.venv':
    'Virtual environment, but dot-prefixed. Remove and recreate if you need a clean slate.',
  '.ipynb_checkpoints':
    'Jupyter notebook autosaves. Safe to nuke; notebooks stay.',
  '.mypy_cache': 'mypy type-checker cache. Delete to force a full re-check.',
  '.ruff_cache': 'Ruff linter cache. Safe to delete; Ruff will refill it.',
  '.tox': 'tox environments. Delete and tox will recreate them on next run.',
  '.nox': 'nox virtualenvs. Safe to remove; tasks will recreate.',
  '.pytype': 'pytype analysis cache. Disposable.',
  '.pyre': 'Pyre type checker cache. Disposable.',
  htmlcov: 'HTML coverage output (pytest-cov). Just reports: delete anytime.',

  // =====================
  // Go / Rust / C / C++
  // =====================
  pkg: 'Go compiled package cache (or generic `pkg` dir). Safe to delete: `go build` will restore it.',
  bin_go: 'Compiled Go binaries folder. Deletable and rebuildable.',
  target_rust:
    "Cargo's `target` folder with compiled Rust artifacts. Large but regenerable with `cargo build`.",
  cmake_build: 'CMake output directory. Delete and re-run CMake to rebuild.',
  'cmake-build-debug':
    'CLion/CMake debug build output. Delete and reconfigure builds.',
  'cmake-build-release': 'CLion/CMake release build output. Disposable.',
  CMakeFiles: 'CMake intermediate files. You can remove them safely.',
  Debug:
    'Generic debug build folder (C/C++, Visual Studio). Contains debug binaries. Safe to remove and rebuild.',
  Release:
    'Generic release build folder (C/C++, Visual Studio). Contains optimized binaries. Safe to remove and rebuild.',
  x64: 'Architecture-specific build output. Generated: delete and rebuild.',
  x86: 'Architecture-specific build output. Generated: delete and rebuild.',
  '.cxx': 'Android NDK build cache. Safe to delete; Gradle will regenerate.',
  externalNativeBuild: 'Android external NDK build output. Disposable.',

  // =====================
  // Game engines (from previous list, kept for completeness)
  // =====================
  library:
    "Unity's internal imported-asset cache. Huge but re-creatable: Unity will reimport everything.",
  Library:
    "Unity's actual 'Library' folder (case-sensitive systems). Same deal: giant cache: safe to delete. WARNING: On macOS, DO NOT delete ~/Library (user's system Library). Only delete if it's in a Unity project!",
  Temp: "Unity temp build files. Close the Unity editor first, then delete. WARNING: Generic name; ensure it's in a Unity project context.",
  Obj: "Unity intermediate object cache. Disposable. WARNING: Generic name; verify it's in a Unity project before deleting.",
  intermediate:
    "Unreal temp build files. Safe to delete but expect long rebuilds. WARNING: Generic name; verify it's in an Unreal project.",
  Intermediate:
    "Unreal intermediate files (proper case). Delete to force a clean rebuild. WARNING: Generic name; verify it's in an Unreal project.",
  DerivedDataCache:
    'Unreal Engine derived data cache. Stores cooked/processed assets to speed up builds. Deleting forces re-cooking of assets. WARNING: Can be many GB. Safe to delete but rebuild will be slow.',
  Saved:
    'Unreal Engine saved files (logs, autosaves, cooked content, screenshots). Safe to delete but you may lose local editor settings, autosaves, and cooked assets. WARNING: May contain unsaved work!',
  Binaries:
    'Unreal Engine compiled binaries. Contains game/editor executables and DLLs. Regenerated by the build system. Safe to delete but requires full recompilation.',
  '.import': 'Godot imported assets cache. Re-imports on next run.',
  '.godot':
    'Godot 4 project cache and metadata. Safe to delete; Godot will rebuild it.',

  // =====================
  // Docker / Containers / Cloud
  // =====================
  docker:
    'Local Docker build artifacts (if present in project). WARNING: This is unusual; Docker data is typically in system directories. Verify before deleting as it may contain important container volumes or configs.',
  '.serverless':
    'Serverless Framework output (deploy packages, cloud artifacts). Rebuildable, but check before deleting.',
  '.firebase':
    'Firebase local state/cache. Contains local emulator data and deployment cache. Safe locally but contains deploy helpers. WARNING: May contain local emulator data.',
  '.docusaurus':
    'Docusaurus build cache (v2). You can wipe it; `npm run build` restores output.',

  // =====================
  // Misc / catch-all
  // =====================
  tmp: "Generic temporary files. Safe to clear if the program isn't running. WARNING: Very generic name; ensure programs using it are closed.",
  temp: 'Same as tmp. Temporary files directory. Cleans up disk but might slow first run after deletion. WARNING: Ensure no programs are actively using it.',
  logs: "Log files directory. Useful for debugging, but safe to archive or delete when old. WARNING: Verify logs aren't critical for auditing/compliance before deleting.",
  coverage_reports:
    'Saved coverage outputs: can grow. Delete if you can regenerate.',
  '.cache-ci':
    'Generic CI cache folder. Deleting will make CI re-download dependencies next run.',
  out_static: 'Generic static export output: disposable and rebuildable.',
  '.sass-cache': 'Legacy Sass cache. Totally safe to delete.',
  '.cpcache': 'Clojure CLI compilation cache. Delete to recompile on next run.',
  'dist-newstyle': 'Haskell Cabal build output. Delete and rebuild.',
  '.stack-work':
    'Haskell Stack build cache. Disposable; `stack build` will recreate.',
  _build:
    'Generic build output for many tools (Sphinx, Dune, Elixir Mix, etc.). Safe to delete and rebuild. Commonly used by Elixir, Erlang, OCaml, and Python documentation tools.',
  deps: "Elixir/Erlang dependencies (or generic deps folder). Delete and `mix deps.get` to restore. WARNING: Generic name; verify it's an Elixir/Erlang project.",
  cover: 'Elixir test coverage output. Disposable coverage reports and data.',
  nimcache: 'Nim compiler cache. Safe to nuke; it will recompile.',
  elm_stuff: 'Elm dependency cache. Delete and `elm make` will restore.',
  '.pants.d': 'Pants build system cache. Remove to force clean builds.',
  'buck-out': 'Buck build output. Delete to rebuild.',
  'bazel-bin': 'Bazel binary outputs. Regenerated by Bazel.',
  'bazel-out': 'Bazel build outputs. Disposable.',
  'bazel-testlogs': 'Bazel test logs. Delete freely.',
  deno_dir:
    'Deno cache dir (if set locally). Safe to clear: Deno will fetch again.',
  deno_cache: 'Another name for a local Deno cache dir. Disposable.',
  lightning_logs:
    "PyTorch Lightning logs and checkpoints. Contains training metrics and model checkpoints. WARNING: Delete only if you don't need experiment history or saved model weights!",
  wandb:
    "Weights & Biases run logs. Contains experiment tracking data and artifacts. Big sometimes: delete if you're done with the experiments. WARNING: May contain model checkpoints and metrics!",
  mlruns:
    'MLflow tracking data. Contains experiment runs, parameters, and artifacts. WARNING: Remove only if you accept losing past runs and model artifacts!',
  runs: "TensorBoard logs (often named runs/). Purely for visualization: safe to prune. WARNING: Generic name; verify it's actually TensorBoard logs before deleting.",
  npkill: `You’re aiming at *me*!
  I clean junk... I *am* not junk!
  /(ಥ﹏ಥ)\\`,
  //   npkill: `Ah, recursion.
  //   A beautiful concept... until it deletes itself.
  // `,
};
```

## File: `src/constants/sort.result.ts`
```typescript
import { CliScanFoundFolder } from '../cli/interfaces/index.js';

export const FOLDER_SORT = {
  path: (a: CliScanFoundFolder, b: CliScanFoundFolder) =>
    a.path > b.path ? 1 : -1,
  size: (a: CliScanFoundFolder, b: CliScanFoundFolder) => {
    if (a.size !== b.size) {
      return a.size < b.size ? 1 : -1;
    }
    return FOLDER_SORT.path(a, b);
  },
  age: (a: CliScanFoundFolder, b: CliScanFoundFolder) => {
    if (a.modificationTime === b.modificationTime) {
      return FOLDER_SORT.path(a, b);
    }

    if (a.modificationTime === null && b.modificationTime !== null) {
      return 1;
    }

    if (b.modificationTime === null && a.modificationTime !== null) {
      return -1;
    }

    return a.modificationTime - b.modificationTime;
  },
};
```

## File: `src/constants/spinner.constants.ts`
```typescript
export const SPINNER_INTERVAL = 70;
export const SPINNERS = {
  SPRING: [
    '⠈',
    '⠉',
    '⠋',
    '⠓',
    '⠒',
    '⠐',
    '⠐',
    '⠒',
    '⠖',
    '⠦',
    '⠤',
    '⠠',
    '⠠',
    '⠤',
    '⠦',
    '⠖',
    '⠒',
    '⠐',
    '⠐',
    '⠒',
    '⠓',
    '⠋',
    '⠉',
    '⠈',
  ],
  W10: [
    '⢀⠀',
    '⡀⠀',
    '⠄⠀',
    '⢂⠀',
    '⡂⠀',
    '⠅⠀',
    '⢃⠀',
    '⡃⠀',
    '⠍⠀',
    '⢋⠀',
    '⡋⠀',
    '⠍⠁',
    '⢋⠁',
    '⡋⠁',
    '⠍⠉',
    '⠋⠉',
    '⠋⠉',
    '⠉⠙',
    '⠉⠙',
    '⠉⠩',
    '⠈⢙',
    '⠈⡙',
    '⢈⠩',
    '⡀⢙',
    '⠄⡙',
    '⢂⠩',
    '⡂⢘',
    '⠅⡘',
    '⢃⠨',
    '⡃⢐',
    '⠍⡐',
    '⢋⠠',
    '⡋⢀',
    '⠍⡁',
    '⢋⠁',
    '⡋⠁',
    '⠍⠉',
    '⠋⠉',
    '⠋⠉',
    '⠉⠙',
    '⠉⠙',
    '⠉⠩',
    '⠈⢙',
    '⠈⡙',
    '⠈⠩',
    '⠀⢙',
    '⠀⡙',
    '⠀⠩',
    '⠀⢘',
    '⠀⡘',
    '⠀⠨',
    '⠀⢐',
    '⠀⡐',
    '⠀⠠',
    '⠀⢀',
    '⠀⡀',
  ],
};
```

## File: `src/constants/status.constants.ts`
```typescript
import pc from 'picocolors';

export const BAR_PARTS = {
  bg: pc.gray('▀'),
  searchTask: pc.white('▀'),
  calculatingTask: pc.blue('▀'),
  completed: pc.green('▀'),
};

export const BAR_WIDTH = 25;
```

## File: `src/constants/update.constants.ts`
```typescript
export const VERSION_CHECK_DIRECTION = 'https://npkill.js.org/version.json';
export const VERSION_KEY = 'last-recomended-version';
```

## File: `src/constants/workers.constants.ts`
```typescript
export const MAX_WORKERS = 8;
// More PROCS improve the speed of the search in the worker,
// but it will greatly increase the maximum ram usage.
export const MAX_PROCS = 100;
export enum EVENTS {
  startup = 'startup',
  alive = 'alive',
  exploreConfig = 'exploreConfig',
  explore = 'explore',
  scanResult = 'scanResult',
  getFolderSize = 'getFolderSize',
  GetSizeResult = 'GetSizeResult',
  stop = 'stop',
  error = 'error',
}
```

## File: `src/core/index.ts`
```typescript
export * from './npkill.js';
export * from './interfaces/index.js';
export * from './services/index.js';
export * from './constants/index.js';
```

## File: `src/core/npkill.ts`
```typescript
import { FileWorkerService } from './services/files/index.js';
import { from, Observable } from 'rxjs';
import { catchError, filter, map, mergeMap, take, tap } from 'rxjs/operators';
import { ScanStatus } from './interfaces/search-status.model.js';
import _dirname from '../dirname.js';
import { LoggerService } from './services/logger.service.js';
import { StreamService } from './services/stream.service.js';
import { ProfilesService } from './services/profiles.service.js';
import { Services } from './interfaces/services.interface.js';
import {
  ScanFoundFolder,
  GetNewestFileResult,
  GetSizeResult,
  ScanOptions,
  DeleteOptions,
  DeleteResult,
  SizeUnit,
} from './interfaces/folder.interface.js';
import { OSServiceMap } from '../constants/os-service-map.constants.js';
import {
  IsValidRootFolderResult,
  NpkillInterface,
} from './interfaces/npkill.interface.js';

import { LogEntry } from './interfaces/logger-service.interface.js';
import { getFileContent } from '../utils/get-file-content.js';
import { ResultsService } from '../cli/services/results.service.js';

/**
 * Main npkill class that implements the core directory scanning and cleanup functionality.
 * Provides methods for recursive directory scanning, size calculation, file analysis,
 * and safe deletion operations.
 */
export class Npkill implements NpkillInterface {
  private readonly services: Services;

  constructor(customServices?: Partial<Services>) {
    const defaultServices = createDefaultServices(
      customServices?.searchStatus,
      customServices?.logger,
    );
    this.services = { ...defaultServices, ...customServices };
    this.logger.info(process.argv.join(' '));
    this.logger.info(`Npkill started! v${this.getVersion()}`);
  }

  private searchDuration = 0;

  startScan$(
    rootPath: string,
    options: ScanOptions,
  ): Observable<ScanFoundFolder> {
    const { fileService } = this.services;
    this.logger.info(`Scan started in ${rootPath}`);
    const startTime = Date.now();

    return fileService.listDir(rootPath, options).pipe(
      catchError(() => {
        throw new Error('Error while listing directories');
      }),
      mergeMap((dataFolder) => from(splitData(dataFolder))),
      filter((path) => path !== ''),
      map((path) => {
        if (
          options.performRiskAnalysis !== undefined &&
          !options.performRiskAnalysis
        ) {
          return { path };
        }
        const riskAnalysis = fileService.isDangerous(path);
        return {
          path,
          riskAnalysis,
        };
      }),
      tap((nodeFolder) =>
        this.logger.info(`Folder found: ${String(nodeFolder.path)}`),
      ),
      tap({
        complete: () => {
          this.searchDuration = (Date.now() - startTime) / 1000;
          this.logger.info(`Search completed after ${this.searchDuration}s`);
        },
      }),
    );
  }

  getSize$(path: string): Observable<GetSizeResult> {
    const { fileService } = this.services;
    this.logger.info(`Calculating folder size for ${String(path)}`);
    return fileService.getFolderSize(path).pipe(
      take(1),
      map((size) => ({ size, unit: 'bytes' as SizeUnit })),
      tap(({ size }) => this.logger.info(`Size of ${path}: ${size} bytes`)),
    );
  }

  getNewestFile$(
    path: string,
    // options?: GetNewestFileOptions,
  ): Observable<GetNewestFileResult | null> {
    const { fileService } = this.services;
    this.logger.info(`Calculating last mod. of ${path}`);
    return from(fileService.getRecentModificationInDir(path)).pipe(
      tap((result) => {
        if (!result) {
          return;
        }
        this.logger.info(`Last mod. of ${path}: ${result.timestamp}`);
      }),
    );
  }

  delete$(path: string, options?: DeleteOptions): Observable<DeleteResult> {
    const { fileService } = this.services;
    this.logger.info(
      `Deleting ${String(path)} ${options?.dryRun ? '(dry run)' : ''}...`,
    );
    const deleteOperation = options?.dryRun
      ? from(fileService.fakeDeleteDir())
      : from(fileService.deleteDir(path));

    return deleteOperation.pipe(
      map((result) => {
        if (!result) {
          this.logger.error(`Failed to delete ${String(path)}`);
          return { path, success: false };
        }
        this.logger.info(`Deleted ${String(path)}: ${result}`);
        return {
          path,
          success: result,
        };
      }),
    );
  }

  getLogs$(): Observable<LogEntry[]> {
    return this.services.logger.getLog$();
  }

  stopScan(): void {
    this.logger.info('Stopping scan...');
    this.services.fileService.stopScan();
  }

  isValidRootFolder(path: string): IsValidRootFolderResult {
    return this.services.fileService.isValidRootFolder(path);
  }

  getVersion(): string {
    const packageJson = _dirname + '/../package.json';

    const packageData = JSON.parse(getFileContent(packageJson));
    return packageData.version;
  }

  get logger(): LoggerService {
    return this.services.logger;
  }
}

function createDefaultServices(
  searchStatus?: ScanStatus,
  logger?: LoggerService,
): Services {
  const actualLogger = logger || new LoggerService();
  const actualSearchStatus = searchStatus || new ScanStatus();
  const fileWorkerService = new FileWorkerService(
    actualLogger,
    actualSearchStatus,
  );
  const streamService = new StreamService();
  const resultsService = new ResultsService();
  const profilesService = new ProfilesService();

  const OSService = OSServiceMap[process.platform];
  if (typeof OSService === 'undefined') {
    throw new Error(
      `Unsupported platform: ${process.platform}. Cannot load OS service.`,
    );
  }
  const fileService = new OSService(streamService, fileWorkerService);

  return {
    logger: actualLogger,
    searchStatus: actualSearchStatus,
    fileService,
    fileWorkerService,
    streamService,
    resultsService,
    profilesService,
  };
}

function splitData(data: string, separator = '\n'): string[] {
  if (data === '') {
    return [];
  }
  return data.split(separator);
}
```

## File: `src/core/constants/global-ignored.constants.ts`
```typescript
/*
These directories will always be excluded during the search.
However, if the name matches a target, it will be displayed as a result.
This way, we avoid entering directories where we know we won't find what we need.
*/

export const GLOBAL_IGNORE = new Set([
  // Version controls
  '.git',
  '.svn',
  '.hg',
  '.fossil',

  // System folders
  '.Trash',
  '.Trashes',
  'System Volume Information',
  '.Spotlight-V100',
  '.fseventsd',

  // Tools and environment
  '.nvm',
  '.rvm',
  '.rustup',
  '.pyenv',
  '.rbenv',
  '.asdf',
  '.deno',

  // IDEs
  '.vscode',
  '.idea',
  '.vs',
  '.settings',

  // Other
  'snap',
  '.flatpak-info',

  //Heavy
  'node_modules',
  '__pycache__',
  'target',
  'build',
  'dist',
  '.cache',
  '.venv',
  'venv',
]);
```

## File: `src/core/constants/index.ts`
```typescript
export * from './profiles.constants.js';
```

## File: `src/core/constants/profiles.constants.ts`
```typescript
/* eslint-disable quotes */
import { PROFILE } from '../interfaces/profile.interface.js';

export const DEFAULT_PROFILE = 'node';

export const BASE_PROFILES: { [profileName: string]: PROFILE } = {
  node: {
    description:
      'All the usual suspects related with the node/web/javascript dev toolchain: node_modules, caches, build artifacts, and assorted JavaScript junk. Safe to clean and your disk will thank you.',
    targets: [
      'node_modules',
      '.npm',
      '.pnpm-store',
      '.next',
      '.nuxt',
      '.angular',
      '.svelte-kit',
      '.vite',
      '.nx',
      '.turbo',
      '.parcel-cache',
      '.rpt2_cache',
      '.eslintcache',
      '.esbuild',
      '.cache',
      '.rollup.cache',
      'storybook-static',
      'coverage',
      '.nyc_output',
      '.jest',
      'gatsby_cache',
      '.docusaurus',
      '.swc',
      '.stylelintcache',
      'deno_cache',
    ],
  },
  python: {
    description:
      "The usual Python leftovers — caches, virtual environments, and test artifacts. Safe to clear once you've closed your IDE and virtualenvs.",
    targets: [
      '__pycache__',
      '.pytest_cache',
      '.mypy_cache',
      '.ruff_cache',
      '.tox',
      '.nox',
      '.pytype',
      '.pyre',
      'htmlcov',
      '.venv',
      'venv',
    ],
  },
  'data-science': {
    description:
      'Jupyter checkpoints, virtualenvs, MLflow runs, and experiment outputs. Great for learning, terrible for disk space.',
    targets: [
      '.ipynb_checkpoints',
      '__pycache__',
      '.venv',
      'venv',
      'outputs',
      '.dvc',
      '.mlruns',
    ],
  },
  java: {
    description: 'Build outputs and Gradle junk.',
    targets: ['target', '.gradle', 'out'],
  },
  android: {
    description:
      "Native build caches and intermediate files from Android Studio. Deleting won't hurt, but expect a rebuild marathon next time.",
    targets: ['.cxx', 'externalNativeBuild'],
  },
  swift: {
    description:
      "Xcode's playground leftovers and Swift package builds. Heavy, harmless, and happy to go.",
    targets: ['DerivedData', '.swiftpm'],
  },
  dotnet: {
    description:
      "Compilation artifacts and Visual Studio cache folders. Disposable once you're done building or testing.",
    targets: ['obj', 'TestResults', '.vs'],
  },
  rust: {
    description:
      'Cargo build targets. Huge, regenerable, and surprisingly clingy, your disk will appreciate the reset.',
    targets: ['target'],
  },
  ruby: {
    description: 'Bundler caches and dependency leftovers.',
    targets: ['.bundle'],
  },
  elixir: {
    description:
      'Mix build folders, dependencies, and coverage reports. Easy to regenerate, safe to purge.',
    targets: ['_build', 'deps', 'cover'],
  },
  haskell: {
    description:
      "GHC and Stack build outputs. A collection of intermediate binaries you definitely don't need anymore.",
    targets: ['dist-newstyle', '.stack-work'],
  },
  scala: {
    description: 'Bloop, Metals, and build outputs from Scala projects.',
    targets: ['.bloop', '.metals', 'target'],
  },
  cpp: {
    description:
      'CMake build directories and temporary artifacts. Rebuilds take time, but space is priceless.',
    targets: ['CMakeFiles', 'cmake-build-debug', 'cmake-build-release'],
  },
  unity: {
    description:
      "Unity's cache and build artifacts. Expect longer load times next launch but it can save tons of space on unused projects.",
    targets: ['Library', 'Temp', 'Obj'],
  },
  unreal: {
    description:
      'Intermediate and binary build caches. Safe to clean. Unreal will (happily?) recompile.',
    targets: ['Intermediate', 'DerivedDataCache', 'Binaries'],
  },
  godot: {
    description:
      'Editor caches and import data. Godot can recreate these in a blink.',
    targets: ['.import', '.godot'],
  },
  infra: {
    description:
      'Leftovers from deployment tools like Serverless, Vercel, Netlify, and Terraform.',
    targets: [
      '.serverless',
      '.vercel',
      '.netlify',
      '.terraform',
      '.sass-cache',
      '.cpcache',
      'elm_stuff',
      'nimcache',
      'deno_cache',
    ],
  },
};

const ALL_TARGETS = [
  ...new Set(
    Object.values(BASE_PROFILES).flatMap((profile) => profile.targets),
  ),
];

export const DEFAULT_PROFILES: { [profileName: string]: PROFILE } = {
  ...BASE_PROFILES,
  all: {
    targets: ALL_TARGETS,
    description:
      'Includes all targets listed above. Not recommended, as it mixes unrelated ecosystems and may remove context-specific data (a good recipe for chaos if used recklessly).',
  },
};
```

## File: `src/core/interfaces/file-service.interface.ts`
```typescript
import { FileWorkerService } from '../services/files/files.worker.service.js';
import { GetNewestFileResult, RiskAnalysis } from '../interfaces/index.js';
import { ScanOptions } from './folder.interface.js';
import { Observable } from 'rxjs';
import { IsValidRootFolderResult } from './npkill.interface.js';

/**
 * Core file system operations service for npkill.
 * Provides methods for directory scanning, size calculation, deletion, and validation.
 */
export interface IFileService {
  /** Worker service for handling file operations in background threads. */
  fileWorkerService: FileWorkerService;

  /**
   * Calculates the total size of a directory.
   * @param path Path to the directory to measure.
   * @returns Observable emitting the size in bytes.
   */
  getFolderSize: (path: string) => Observable<number>;

  /**
   * Lists directories matching scan criteria.
   * @param path Root path to start listing from.
   * @param params Scan options for filtering and configuration.
   * @returns Observable emitting found directory paths.
   */
  listDir: (path: string, params: ScanOptions) => Observable<string>;

  /**
   * Permanently deletes a directory and its contents.
   * @param path Path to the directory to delete.
   * @returns Promise resolving to true if deletion was successful.
   */
  deleteDir: (path: string) => Promise<boolean>;

  /**
   * Simulates directory deletion without actually removing files.
   * @param _path Path to the directory that would be deleted.
   * @returns Promise resolving to true (always succeeds for dry run).
   */
  fakeDeleteDir: (_path: string) => Promise<boolean>;

  /**
   * Validates whether a path is suitable as a scan root directory.
   * @param path Path to validate.
   * @returns Validation result with success status and error reason if invalid.
   */
  isValidRootFolder(path: string): IsValidRootFolderResult;

  /**
   * Analyzes a directory path for potential deletion risks.
   * @param path Path to analyze for safety.
   * @returns Risk analysis indicating if the path is dangerous to delete.
   */
  isDangerous: (path: string) => RiskAnalysis;

  /**
   * Finds the most recently modified file in a directory tree.
   * @param path Root directory to search within.
   * @returns Promise resolving to newest file info, or null if no files found.
   */
  getRecentModificationInDir: (
    path: string,
  ) => Promise<GetNewestFileResult | null>;

  /**
   * Retrieves file statistics for all files in a directory.
   * @param dirname Directory to analyze.
   * @returns Promise resolving to array of file statistics.
   */
  getFileStatsInDir: (dirname: string) => Promise<IFileStat[]>;

  /**
   * Stops any ongoing scan operations.
   * Cancels workers and cleans up resources.
   */
  stopScan: () => void;
}

/**
 * Statistical information about a file.
 */
export interface IFileStat {
  /** Full path to the file. */
  path: string;
  /** Unix timestamp of the file's last modification. */
  modificationTime: number;
}
```

## File: `src/core/interfaces/folder.interface.ts`
```typescript
/** Unit for representing file/directory sizes. */
export type SizeUnit = 'bytes'; // | 'kb' | 'mb' | 'gb'; // TODO implement

/** Options soported for the sortBy scan option. */
export type SortBy = 'path' | 'size' | 'age';
/**
 * Analysis of potential risks associated with deleting a directory.
 */
export interface RiskAnalysis {
  /** Whether the directory is considered sensitive or risky to delete. */
  isSensitive: boolean;
  /** Human-readable reason for the risk assessment. */
  reason?: string;
}

/**
 * Represents a folder found during the scan process.
 */
export interface ScanFoundFolder {
  /** Full path to the found folder. */
  path: string;
  /** Optional risk analysis for the folder. */
  riskAnalysis?: RiskAnalysis;
}

/**
 * Configuration options for scanning directories.
 */
export interface ScanOptions {
  /** Target directories to scan for matching folders. */
  targets: string[];
  /** Array of directory paths to exclude from the scan. */
  exclude?: string[];
  /** Criteria for sorting scan results. */
  sortBy?: SortBy;
  /** Whether to perform risk analysis on found directories. Default: true. */
  performRiskAnalysis?: boolean; // Default: true
  // maxConcurrentScans?: number; // Need to implement this.
}

/**
 * Options for calculating directory size.
 */
export interface GetSizeOptions {
  /** Unit to return the size in. Default: bytes. */
  unit?: SizeUnit; // Default: bytes
}

/**
 * Result of a directory size calculation.
 */
export interface GetSizeResult {
  /** Size value in the specified unit. Default: bytes. */
  size: number; // Default: bytes
  /** Unit of the size measurement. */
  unit: SizeUnit;
}

/**
 * Options for finding the newest file in a directory.
 */
// eslint-disable-next-line @typescript-eslint/no-empty-object-type
export interface GetNewestFileOptions {}

/**
 * Information about the most recently modified file in a directory.
 */
export interface GetNewestFileResult {
  /** Full path to the newest file. */
  path: string;
  /** Name of the newest file. */
  name: string;
  /** Unix timestamp of the file's last modification. */
  timestamp: number; // epoch timestamp
}

/**
 * Options for directory deletion operations.
 */
export interface DeleteOptions {
  /** If true, simulate deletion without actually removing files. */
  dryRun?: boolean;
}

/**
 * Result of a directory deletion operation.
 */
export interface DeleteResult {
  /** Path that was attempted to be deleted. */
  path: string;
  /** Whether the deletion was successful. */
  success: boolean;
  /** Error information if deletion failed. */
  error?: {
    /** Human-readable error message. */
    message: string;
    /** Error code if available. */
    code?: string;
  };
}
```

## File: `src/core/interfaces/index.ts`
```typescript
export * from './file-service.interface.js';
export * from './folder.interface.js';
export * from './services.interface.js';
export * from './search-status.model.js';
export * from './npkillrc-config.interface.js';
export * from './profile.interface.js';
```

## File: `src/core/interfaces/logger-service.interface.ts`
```typescript
import { Observable } from 'rxjs';

/**
 * Represents an individual entry in the log.
 */
export interface LogEntry {
  type: 'info' | 'warn' | 'error';
  timestamp: number;
  message: string;
}

/**
 * Interface for a logging service that allows logging messages
 * of different types, retrieving them, and saving them to a file.
 */
export interface ILoggerService {
  /**
   * Logs an info message.
   * @param message The message to log.
   */
  info(message: string): void;

  /**
   * Logs a warning message.
   * @param message The message to log.
   */
  warn(message: string): void;

  /**
   * Logs an error message.
   * @param message The message to log.
   */
  error(message: string): void;

  /**
   * Gets log entries filtered by type.
   * @param type The type of entries to retrieve ('all', 'info', 'warn', 'error'). Default is 'all'.
   * @returns An array of log entries.
   */
  get(type?: 'all' | 'info' | 'warn' | 'error'): LogEntry[];

  /**
   * Gets an Observable that emits the full array of log entries whenever it changes.
   * @returns An Observable of an array of log entries.
   */
  getLog$(): Observable<LogEntry[]>;

  /**
   * Gets an Observable that emits log entries filtered by type whenever they change.
   * @param type The type of entries to retrieve ('all', 'info', 'warn', 'error'). Default is 'all'.
   * @returns An Observable of an array of log entries.
   */
  getLogByType$(
    type?: 'all' | 'info' | 'warn' | 'error',
  ): Observable<LogEntry[]>;

  /**
   * Saves the current log content to a specified file.
   * Rotates the log file if one with the same name already exists.
   * @param path The full path of the file where the log will be saved.
   */
  saveToFile(path: string): void;

  /**
   * Suggests a default file path to save the log,
   * usually in the system's temporary directory.
   * @returns The suggested file path.
   */
  getSuggestLogFilePath(): string;
}
```

## File: `src/core/interfaces/npkill.interface.ts`
```typescript
import { Observable } from 'rxjs';
import {
  ScanFoundFolder,
  GetNewestFileResult,
  GetSizeOptions,
  GetSizeResult,
  ScanOptions,
  DeleteResult,
  DeleteOptions,
} from './folder.interface.js';
import { LogEntry } from '@core/interfaces/logger-service.interface.js';

export type ProfileFilterType = 'base' | 'user' | 'all';

/**
 * Result of validating a root folder path.
 */
export interface IsValidRootFolderResult {
  /** Whether the folder is valid as a root. */
  isValid: boolean;
  /** Reason for invalidity, if not valid. */
  invalidReason?: string;
}

/**
 * Npkill is a powerful search engine that allows you to scan the file system
 * for specified directories. It also allows you to perform operations on them
 * in order to clean them up.
 */
export interface NpkillInterface {
  /**
   * Starts the recursive search from the specified directory.
   * @param rootPath Root directory to scan from.
   * @param options Optional scan options.
   * @returns Observable that emits the results that are found in real time.
   */
  startScan$(
    rootPath: string,
    options?: ScanOptions,
  ): Observable<ScanFoundFolder>;

  /**
   * Stops the current scan if any.
   *
   * Frees resources and terminates the observable returned by `startScan$`.
   */
  stopScan(): void;

  /**
   * Returns the total size of the contents of a directory.
   * @param path Path to the directory.
   * @param options Optional size options.
   * @returns Observable that outputs a value with the result of the operation.
   */
  getSize$(path: string, options?: GetSizeOptions): Observable<GetSizeResult>;

  /**
   * Retrieves the most recently modified file (the one with the latest
   * modification timestamp) within a given directory and its subdirectories,
   * recursively.
   * @param path Path to the directory.
   * @returns Observable that outputs a value with the result of the
   * operation. May return null if no files exist or the most recent file
   * cannot be determined.
   */
  getNewestFile$(path: string): Observable<GetNewestFileResult | null>;

  /**
   * Deletes the specified directory. For security purposes, this directory
   * must be contained within the `target` path defined when initiating the scan
   * with `startScan$` or throw an exception.
   * @param path Path to delete.
   * @param options Optional delete options.
   * @returns Observable emitting the delete result.
   * @throws Error if the path is not within the target directory.
   */
  delete$(path: string, options?: DeleteOptions): Observable<DeleteResult>;

  /**
   * Gets the log stream generated by npkill.
   * @returns Observable emitting an array of log entries.
   */
  getLogs$(): Observable<LogEntry[]>;

  /**
   * Checks if a given route has problems initiating a scan. Validates that the
   * path belongs to a directory, that the directory exists and that there are
   * no permissions issues.
   * @param path Path to validate.
   * @returns Result of validation.
   */
  isValidRootFolder(path: string): IsValidRootFolderResult;

  /**
   * Get the current version of npkill.
   * @returns Version string defined in npkill's package.json.
   */
  getVersion(): string;
}
```

## File: `src/core/interfaces/npkillrc-config.interface.ts`
```typescript
import { PROFILE } from './profile.interface.js';

/**
 * Represents the structure of .npkillrc configuration file.
 * All properties are optional as users may only override specific settings.
 */
export interface INpkillrcConfig {
  /**
   * Absolute path from which the search will begin.
   * @example "/home/user/my-projects/"
   */
  rootDir?: string;

  /**
   * Array of directory names to exclude from search.
   * These directories and their subdirectories will be skipped.
   * @example [".git", "important-project"]
   */
  exclude?: string[];

  /**
   * Default sort order for results.
   * @default "none"
   */
  sortBy?: 'none' | 'size' | 'path' | 'age';

  /**
   * Unit for displaying folder sizes.
   * - "auto": Sizes < 1024MB shown in MB, larger sizes in GB
   * - "mb": Always show in megabytes
   * - "gb": Always show in gigabytes
   * @default "auto"
   */
  sizeUnit?: 'auto' | 'mb' | 'gb';

  /**
   * Exclude sensitive results.
   * @default false
   */
  excludeSensitiveResults?: boolean;

  /**
   * Enable dry-run mode by default.
   * When true, deletions are simulated (nothing is actually deleted).
   * @default false
   */
  dryRun?: boolean;

  /**
   * Check for npkill updates on startup.
   * @default true
   */
  checkUpdates?: boolean;

  /**
   * Profiles to use.
   * @example ["node", "python"]
   * @default ["node"]
   */
  defaultProfiles?: string[];

  /**
   * Custom profiles with specific target directories.
   * Profile names can be used with the -p/--profiles flag.
   * @example
   * {
   *   "webdev": {
   *     "targets": ["node_modules", "dist", ".next"],
   *     "description": "Web development artifacts"
   *   },
   *   "python": {
   *     "targets": [".venv", "__pycache__"],
   *     "description": "Python virtual environments and caches"
   *   }
   * }
   */
  profiles?: Record<string, PROFILE>;
}

/**
 * Result of loading and parsing a .npkillrc configuration file.
 */
export interface IConfigLoadResult {
  /**
   * The parsed configuration, or null if loading failed.
   */
  config: INpkillrcConfig | null;

  /**
   * Path to the configuration file that was loaded or attempted to load.
   */
  configPath: string;

  /**
   * Error message if loading or parsing failed.
   */
  error?: string;
}

export const VALID_NPKILLRC_PROPERTIES = [
  'rootDir',
  'exclude',
  'sortBy',
  'sizeUnit',
  'excludeSensitiveResults',
  'dryRun',
  'checkUpdates',
  'defaultProfiles',
  'profiles',
] as const satisfies readonly (keyof INpkillrcConfig)[];
```

## File: `src/core/interfaces/profile.interface.ts`
```typescript
/**
 * Represents a profile with target directories and description.
 */
export interface PROFILE {
  /** Array of directory names to search for */
  targets: string[];
  /** Description of what this profile is for */
  description: string;
}
```

## File: `src/core/interfaces/search-status.model.ts`
```typescript
import { WorkerStatus } from '../services/files/files.worker.service.js';

/**
 * Tracks the progress and status of directory scanning operations.
 * Maintains counters for various stages of the scan process including
 * search tasks, statistics calculation, and deletion operations.
 */
export class ScanStatus {
  /** Number of search tasks currently pending execution. */
  public pendingSearchTasks = 0;
  /** Number of search tasks that have been completed. */
  public completedSearchTasks = 0;
  /** Number of pending statistics calculations for found directories. */
  public pendingStatsCalculation = 0;
  /** Number of completed statistics calculations. */
  public completedStatsCalculation = 0;
  /** Total number of matching directories found during the scan. */
  public resultsFound = 0;
  /** Number of deletion operations currently pending. */
  public pendingDeletions = 0;
  /** Current status of the worker threads handling the scan. */
  public workerStatus: WorkerStatus = 'stopped';
  /** Information about active worker jobs. */
  public workersJobs;

  /**
   * Records the discovery of a new matching directory.
   * Increments result count and pending statistics calculation.
   */
  newResult(): void {
    this.resultsFound++;
    this.pendingStatsCalculation++;
  }

  /**
   * Records the completion of a statistics calculation.
   * Decrements pending count and increments completed count.
   */
  completeStatCalculation(): void {
    this.pendingStatsCalculation--;
    this.completedStatsCalculation++;
  }

  reset() {
    this.pendingSearchTasks = 0;
    this.completedSearchTasks = 0;
    this.pendingStatsCalculation = 0;
    this.completedStatsCalculation = 0;
    this.resultsFound = 0;
    this.pendingDeletions = 0;
  }
}
```

## File: `src/core/interfaces/services.interface.ts`
```typescript
import { FileService, FileWorkerService } from '@core/services/files/index.js';
import { LoggerService } from '@core/services/logger.service.js';
import { StreamService } from '@core/services/stream.service.js';
import { ProfilesService } from '@core/services/profiles.service.js';
import { ResultsService } from '../../cli/services/index.js';
import { ScanStatus } from './search-status.model.js';

/**
 * Collection of all core services used by npkill.
 * Provides centralized access to logging, file operations, streaming, and result management.
 */
export interface Services {
  /** Service for logging messages and managing log output. */
  logger: LoggerService;
  /** Status tracker for ongoing scan operations. */
  searchStatus: ScanStatus;
  /** Service for file system operations and directory management. */
  fileService: FileService;
  /** Worker service for background file processing tasks. */
  fileWorkerService: FileWorkerService;
  /** Service for managing reactive streams and data flow. */
  streamService: StreamService;
  /** Service for managing and formatting scan results. */
  resultsService: ResultsService;
  /** Service for managing profiles. */
  profilesService: ProfilesService;
}
```

## File: `src/core/services/config.service.ts`
```typescript
import { existsSync, readFileSync } from 'fs';
import { homedir } from 'os';
import { join } from 'path';
import {
  IConfigLoadResult,
  INpkillrcConfig,
} from '../interfaces/npkillrc-config.interface.js';
import { PROFILE } from '../interfaces/profile.interface.js';
import { validateConfig, applyFileConfigProperties } from './config/index.js';

const DEFAULT_CONFIG_FILENAME = '.npkillrc';

/**
 * Service responsible for loading and parsing .npkillrc configuration files.
 */
export class ConfigService {
  /**
   * Loads configuration with priority order:
   * 1. Custom path specified via --config parameter
   * 2. Current working directory ./.npkillrc
   * 3. User's home directory ~/.npkillrc
   * @param customPath Optional custom path to a configuration file
   * @returns Configuration load result containing the parsed config or error information
   */
  loadConfig(customPath?: string): IConfigLoadResult {
    const configPath = this.resolveConfigPath(customPath);

    if (!existsSync(configPath)) {
      return {
        config: null,
        configPath,
        error: customPath
          ? `Custom config file not found: ${configPath}`
          : undefined,
      };
    }

    try {
      const fileContent = readFileSync(configPath, 'utf-8');
      const parsedConfig = JSON.parse(fileContent) as INpkillrcConfig;

      const validationResult = validateConfig(parsedConfig);
      if (!validationResult.isValid) {
        return {
          configPath,
          config: null,
          error: validationResult.error,
        };
      }

      return {
        config: parsedConfig,
        configPath,
      };
    } catch (error) {
      const errorMessage =
        error instanceof Error ? error.message : 'Unknown error';
      return {
        config: null,
        configPath,
        error: `Failed to parse config file: ${errorMessage}.`,
      };
    }
  }

  /**
   * Resolves the configuration file path based on priority order.
   * Priority: custom path > cwd > home directory
   * @param customPath Optional custom path specified by user
   * @returns Resolved configuration file path
   */
  private resolveConfigPath(customPath?: string): string {
    // Priority 1: Custom path from --config flag
    if (customPath) {
      return customPath;
    }

    // Priority 2: Current working directory
    const cwdPath = join(process.cwd(), DEFAULT_CONFIG_FILENAME);
    if (existsSync(cwdPath)) {
      return cwdPath;
    }

    // Priority 3: User's home directory
    return join(homedir(), DEFAULT_CONFIG_FILENAME);
  }

  /**
   * Merges configuration from .npkillrc with a base configuration.
   * Config file values take precedence over base values.
   * @param baseConfig Base configuration object
   * @param fileConfig Configuration loaded from .npkillrc
   * @returns Merged configuration
   */
  mergeConfigs<T extends Record<string, unknown>>(
    baseConfig: T,
    fileConfig: INpkillrcConfig | null,
  ): T {
    if (!fileConfig) {
      return baseConfig;
    }

    const merged = { ...baseConfig };
    applyFileConfigProperties(
      merged as Record<string, unknown>,
      baseConfig as Record<string, unknown>,
      fileConfig,
    );

    return merged;
  }

  /**
   * Gets custom profiles from the configuration file.
   * @param config Configuration loaded from .npkillrc
   * @returns Record of user-defined profiles
   */
  getUserDefinedProfiles(
    config: INpkillrcConfig | null,
  ): Record<string, PROFILE> {
    if (!config || !config.profiles) {
      return {};
    }

    return config.profiles;
  }
}
```

## File: `src/core/services/index.ts`
```typescript
export * from './logger.service.js';
export * from './stream.service.js';
export * from './config.service.js';
export * from './profiles.service.js';
export * from './files/index.js';
```

## File: `src/core/services/logger.service.ts`
```typescript
import { tmpdir } from 'os';
import { existsSync, renameSync, writeFileSync } from 'fs';
import { basename, dirname, join } from 'path';

import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import {
  ILoggerService,
  LogEntry,
} from '@core/interfaces/logger-service.interface.js';

const LATEST_TAG = 'latest';
const OLD_TAG = 'old';

/**
 * Implementation of the logging service for npkill.
 * Manages application logs with different severity levels and provides
 * reactive streams for log observation and file output capabilities.
 */
export class LoggerService implements ILoggerService {
  private log: LogEntry[] = [];
  private logSubject = new BehaviorSubject<LogEntry[]>([]);

  info(message: string): void {
    this.addToLog({
      type: 'info',
      timestamp: this.getTimestamp(),
      message,
    });
  }

  warn(message: string): void {
    this.addToLog({
      type: 'warn',
      timestamp: this.getTimestamp(),
      message,
    });
  }

  error(message: string): void {
    this.addToLog({
      type: 'error',
      timestamp: this.getTimestamp(),
      message,
    });
  }

  get(type: 'all' | 'info' | 'warn' | 'error' = 'all'): LogEntry[] {
    if (type === 'all') {
      return this.log;
    }

    return this.log.filter((entry) => entry.type === type);
  }

  getLog$(): Observable<LogEntry[]> {
    return this.logSubject.asObservable();
  }

  getLogByType$(
    type: 'all' | 'info' | 'warn' | 'error' = 'all',
  ): Observable<LogEntry[]> {
    return this.logSubject
      .asObservable()
      .pipe(
        map((entries) =>
          type === 'all'
            ? entries
            : entries.filter((entry) => entry.type === type),
        ),
      );
  }

  saveToFile(path: string): void {
    const convertTime = (timestamp: number): number => timestamp;

    const content: string = this.log.reduce((log, actual) => {
      const line = `[${convertTime(actual.timestamp)}](${actual.type}) ${
        actual.message
      }\n`;
      return log + line;
    }, '');

    this.rotateLogFile(path);
    writeFileSync(path, content);
  }

  getSuggestLogFilePath(): string {
    const filename = `npkill-${LATEST_TAG}.log`;
    return join(tmpdir(), filename);
  }

  private rotateLogFile(newLogPath: string): void {
    if (!existsSync(newLogPath)) {
      return; // Rotation is not necessary
    }
    const basePath = dirname(newLogPath);
    const logName = basename(newLogPath);
    const oldLogName = logName.replace(LATEST_TAG, OLD_TAG);
    const oldLogPath = join(basePath, oldLogName);
    renameSync(newLogPath, oldLogPath);
  }

  private addToLog(entry: LogEntry): void {
    this.log = [...this.log, entry];
    this.logSubject.next(this.log);
  }

  private getTimestamp(): number {
    return new Date().getTime();
  }
}
```

## File: `src/core/services/profiles.service.ts`
```typescript
import { DEFAULT_PROFILES } from '../constants/profiles.constants.js';
import { PROFILE } from '../interfaces/profile.interface.js';

export type ProfileFilterType = 'base' | 'user' | 'all';

/**
 * Service responsible for managing profiles.
 * Handles profile registration, retrieval, and target resolution.
 */
export class ProfilesService {
  private userDefinedProfiles: Record<string, PROFILE> = {};

  /**
   * Sets user-defined profiles loaded from .npkillrc configuration.
   * @param profiles Record of user-defined profile configurations
   */
  setUserDefinedProfiles(profiles: Record<string, PROFILE>): void {
    this.userDefinedProfiles = profiles;
  }

  /**
   * Gets profiles based on the specified filter type.
   * @param filterType Type of profiles to retrieve:
   *   - 'base': Only built-in profiles
   *   - 'user': Only user-defined profiles from .npkillrc
   *   - 'all': Both base and user-defined (user profiles override base)
   * @returns Record of profiles matching the filter
   */
  getProfiles(filterType: ProfileFilterType = 'all'): Record<string, PROFILE> {
    switch (filterType) {
      case 'base':
        return DEFAULT_PROFILES;
      case 'user':
        return this.userDefinedProfiles;
      case 'all':
        return { ...DEFAULT_PROFILES, ...this.userDefinedProfiles };
      default:
        return DEFAULT_PROFILES;
    }
  }

  /**
   * Gets a specific profile by name.
   * Searches user-defined profiles first, then base profiles.
   * @param name Name of the profile to retrieve
   * @returns The profile if found, undefined otherwise
   */
  getProfileByName(name: string): PROFILE | undefined {
    return this.userDefinedProfiles[name] || DEFAULT_PROFILES[name];
  }

  /**
   * Checks if a profile with the given name exists.
   * @param name Name of the profile to check
   * @returns true if the profile exists, false otherwise
   */
  hasProfile(name: string): boolean {
    return this.getProfileByName(name) !== undefined;
  }

  /**
   * Gets the targets from multiple profiles by their names.
   * Combines targets from all specified profiles, removing duplicates.
   * @param profileNames Array of profile names to get targets from
   * @returns Array of unique target directory names
   */
  getTargetsFromProfiles(profileNames: string[]): string[] {
    const targets = new Set<string>();

    for (const name of profileNames) {
      const profile = this.getProfileByName(name);
      if (profile) {
        for (const target of profile.targets) {
          targets.add(target);
        }
      }
    }

    return Array.from(targets);
  }

  /**
   * Validates an array of profile names.
   * @param profileNames Array of profile names to validate
   * @returns Array of invalid profile names (profiles that don't exist)
   */
  getInvalidProfileNames(profileNames: string[]): string[] {
    return profileNames.filter((name) => !this.hasProfile(name));
  }

  /**
   * Gets the default profile name.
   * @returns Name of the default profile
   */
  getDefaultProfileName(): string {
    return 'node';
  }
}
```

## File: `src/core/services/stream.service.ts`
```typescript
import { ChildProcessWithoutNullStreams } from 'child_process';
import { Observable } from 'rxjs';
import { STREAM_ENCODING } from '../../constants/index.js';

/**
 * Service for converting child process streams into RxJS observables.
 * Handles the conversion of stdout/stderr streams to reactive streams
 * for better integration with the application's reactive architecture.
 */
export class StreamService {
  streamToObservable<T>(stream: ChildProcessWithoutNullStreams): Observable<T> {
    const { stdout, stderr } = stream;

    return new Observable<T>((observer) => {
      const dataHandler = (data): void => observer.next(data);
      const bashErrorHandler = (error): void =>
        observer.error({ ...error, bash: true });
      const errorHandler = (error): void => observer.error(error);
      const endHandler = (): void => observer.complete();

      stdout.addListener('data', dataHandler);
      stdout.addListener('error', errorHandler);
      stdout.addListener('end', endHandler);

      stderr.addListener('data', bashErrorHandler);
      stderr.addListener('error', errorHandler);

      return () => {
        stdout.removeListener('data', dataHandler);
        stdout.removeListener('error', errorHandler);
        stdout.removeListener('end', endHandler);

        stderr.removeListener('data', bashErrorHandler);
        stderr.removeListener('error', errorHandler);
      };
    });
  }

  getStream<T>(child: ChildProcessWithoutNullStreams): Observable<T> {
    this.setEncoding(child, STREAM_ENCODING);
    return this.streamToObservable<T>(child);
  }

  private setEncoding(
    child: ChildProcessWithoutNullStreams,
    encoding: BufferEncoding,
  ): void {
    child.stdout.setEncoding(encoding);
    child.stderr.setEncoding(encoding);
  }
}
```

## File: `src/core/services/config/config-merger.ts`
```typescript
import { INpkillrcConfig } from '../../interfaces/npkillrc-config.interface.js';

/**
 * Merges exclude arrays from base and file config, avoiding duplicates
 */
export function mergeExcludeArrays(
  baseExclude: unknown,
  fileExclude: string[],
): string[] {
  const base = Array.isArray(baseExclude) ? (baseExclude as string[]) : [];
  return [...new Set([...base, ...fileExclude])];
}

/**
 * Merges a simple property (direct override)
 */
export function mergeProperty<T>(
  merged: Record<string, unknown>,
  key: string,
  value: T,
): void {
  merged[key] = value;
}

/**
 * Type guard to check if a property exists and is not undefined
 */
export function isDefined<T>(value: T | undefined): value is T {
  return value !== undefined;
}

/**
 * Applies all file config properties to the merged config
 */
export function applyFileConfigProperties(
  merged: Record<string, unknown>,
  baseConfig: Record<string, unknown>,
  fileConfig: INpkillrcConfig,
): void {
  // rootDir
  if (isDefined(fileConfig.rootDir)) {
    mergeProperty(merged, 'rootDir', fileConfig.rootDir);
  }

  // exclude (special merge logic)
  if (isDefined(fileConfig.exclude)) {
    merged.exclude = mergeExcludeArrays(baseConfig.exclude, fileConfig.exclude);
  }

  // sortBy
  if (isDefined(fileConfig.sortBy)) {
    mergeProperty(merged, 'sortBy', fileConfig.sortBy);
  }

  // sizeUnit
  if (isDefined(fileConfig.sizeUnit)) {
    mergeProperty(merged, 'sizeUnit', fileConfig.sizeUnit);
  }

  // excludeSensitiveResults
  if (isDefined(fileConfig.excludeSensitiveResults)) {
    mergeProperty(
      merged,
      'excludeSensitiveResults',
      fileConfig.excludeSensitiveResults,
    );
  }

  // dryRun
  if (isDefined(fileConfig.dryRun)) {
    mergeProperty(merged, 'dryRun', fileConfig.dryRun);
  }

  // checkUpdates
  if (isDefined(fileConfig.checkUpdates)) {
    mergeProperty(merged, 'checkUpdates', fileConfig.checkUpdates);
  }

  // defaultProfiles
  if (isDefined(fileConfig.defaultProfiles)) {
    mergeProperty(merged, 'defaultProfiles', fileConfig.defaultProfiles);
  }
}
```

## File: `src/core/services/config/config-validator.ts`
```typescript
import {
  INpkillrcConfig,
  VALID_NPKILLRC_PROPERTIES,
} from '../../interfaces/npkillrc-config.interface.js';
import {
  validateRootDir,
  validateExclude,
  validateSortBy,
  validateSizeUnit,
  validateBoolean,
  validateDefaultProfiles,
  validateUnknownProperties,
  ValidationResult,
} from './property-validators.js';
import { validateProfiles } from './profile-validator.js';

export function validateConfig(config: INpkillrcConfig): ValidationResult {
  // Validate that config is an object
  if (typeof config !== 'object' || config === null) {
    return { isValid: false, error: 'Configuration must be an object.' };
  }

  // Validate unknown properties first
  const unknownPropsResult = validateUnknownProperties(
    config,
    VALID_NPKILLRC_PROPERTIES,
  );
  if (!unknownPropsResult.isValid) {
    return unknownPropsResult;
  }

  // Validate each property
  const validators: Array<{ name: string; result: ValidationResult }> = [
    { name: 'rootDir', result: validateRootDir(config.rootDir) },
    { name: 'exclude', result: validateExclude(config.exclude) },
    { name: 'sortBy', result: validateSortBy(config.sortBy) },
    { name: 'sizeUnit', result: validateSizeUnit(config.sizeUnit) },
    {
      name: 'excludeSensitiveResults',
      result: validateBoolean(
        config.excludeSensitiveResults,
        'excludeSensitiveResults',
      ),
    },
    { name: 'dryRun', result: validateBoolean(config.dryRun, 'dryRun') },
    {
      name: 'checkUpdates',
      result: validateBoolean(config.checkUpdates, 'checkUpdates'),
    },
    {
      name: 'defaultProfiles',
      result: validateDefaultProfiles(config.defaultProfiles),
    },
    { name: 'profiles', result: validateProfiles(config.profiles) },
  ];

  // Return first validation error found
  for (const validator of validators) {
    if (!validator.result.isValid) {
      return validator.result;
    }
  }

  return { isValid: true };
}
```

## File: `src/core/services/config/index.ts`
```typescript
export { validateConfig } from './config-validator.js';
export {
  validateRootDir,
  validateExclude,
  validateSortBy,
  validateSizeUnit,
  validateBoolean,
  validateDefaultProfiles,
  validateUnknownProperties,
  type ValidationResult,
} from './property-validators.js';
export { validateProfile, validateProfiles } from './profile-validator.js';
export {
  mergeExcludeArrays,
  mergeProperty,
  isDefined,
  applyFileConfigProperties,
} from './config-merger.js';
```

## File: `src/core/services/config/profile-validator.ts`
```typescript
import { ValidationResult } from './property-validators.js';

export function validateProfile(
  profileName: string,
  profile: unknown,
): ValidationResult {
  if (typeof profile !== 'object' || profile === null) {
    return {
      isValid: false,
      error: `Profile "${profileName}" must be an object.`,
    };
  }

  const profileObj = profile as Record<string, unknown>;

  // Validate description
  if (!profileObj.description || typeof profileObj.description !== 'string') {
    return {
      isValid: false,
      error: `Profile "${profileName}" must have a description property (string).`,
    };
  }

  // Validate targets property exists
  if (!profileObj.targets) {
    return {
      isValid: false,
      error: `Profile "${profileName}" must have a targets property.`,
    };
  }

  // Validate targets is an array
  if (!Array.isArray(profileObj.targets)) {
    return {
      isValid: false,
      error: `Profile "${profileName}" targets must be an array of strings.`,
    };
  }

  // Validate all targets are strings
  if (!profileObj.targets.every((t) => typeof t === 'string')) {
    return {
      isValid: false,
      error: `All targets in profile "${profileName}" must be strings.`,
    };
  }

  // Validate targets array is not empty
  if (profileObj.targets.length === 0) {
    return {
      isValid: false,
      error: `Profile "${profileName}" targets array cannot be empty.`,
    };
  }

  return { isValid: true };
}

/**
 * Validates the profiles property (all profiles)
 */
export function validateProfiles(value: unknown): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (typeof value !== 'object' || value === null || Array.isArray(value)) {
    return {
      isValid: false,
      error: 'profiles must be an object.',
    };
  }

  // Validate each profile
  for (const [profileName, profile] of Object.entries(value)) {
    const result = validateProfile(profileName, profile);
    if (!result.isValid) {
      return result;
    }
  }

  return { isValid: true };
}
```

## File: `src/core/services/config/property-validators.ts`
```typescript
import { INpkillrcConfig } from '../../interfaces/npkillrc-config.interface.js';

const VALID_SORT_OPTIONS = ['none', 'size', 'path', 'age'] as const;
const VALID_SIZE_UNITS = ['auto', 'mb', 'gb'] as const;

export interface ValidationResult {
  isValid: boolean;
  error?: string;
}

/**
 * Validates the rootDir property
 */
export function validateRootDir(value: unknown): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (typeof value !== 'string') {
    return {
      isValid: false,
      error: 'rootDir must be a string.',
    };
  }

  if (value.trim() === '') {
    return {
      isValid: false,
      error: 'rootDir cannot be an empty string.',
    };
  }

  return { isValid: true };
}

/**
 * Validates the exclude property
 */
export function validateExclude(value: unknown): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (!Array.isArray(value)) {
    return {
      isValid: false,
      error: 'exclude must be an array of strings.',
    };
  }

  if (!value.every((item) => typeof item === 'string')) {
    return {
      isValid: false,
      error: 'All exclude items must be strings.',
    };
  }

  return { isValid: true };
}

/**
 * Validates the sortBy property
 */
export function validateSortBy(value: unknown): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (!(VALID_SORT_OPTIONS as readonly string[]).includes(value as string)) {
    return {
      isValid: false,
      error: `sortBy must be one of: ${VALID_SORT_OPTIONS.join(', ')}.`,
    };
  }

  return { isValid: true };
}

/**
 * Validates the sizeUnit property
 */
export function validateSizeUnit(value: unknown): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (!(VALID_SIZE_UNITS as readonly string[]).includes(value as string)) {
    return {
      isValid: false,
      error: `sizeUnit must be one of: ${VALID_SIZE_UNITS.join(', ')}.`,
    };
  }

  return { isValid: true };
}

/**
 * Validates a boolean property
 */
export function validateBoolean(
  value: unknown,
  propertyName: string,
): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (typeof value !== 'boolean') {
    return {
      isValid: false,
      error: `${propertyName} must be a boolean.`,
    };
  }

  return { isValid: true };
}

/**
 * Validates the defaultProfiles property
 */
export function validateDefaultProfiles(value: unknown): ValidationResult {
  if (value === undefined) {
    return { isValid: true };
  }

  if (!Array.isArray(value)) {
    return {
      isValid: false,
      error: 'defaultProfiles must be an array of strings.',
    };
  }

  if (!value.every((item) => typeof item === 'string')) {
    return {
      isValid: false,
      error: 'All defaultProfiles items must be strings.',
    };
  }

  return { isValid: true };
}

/**
 * Validates unknown properties
 */
export function validateUnknownProperties(
  config: INpkillrcConfig,
  validProperties: readonly string[],
): ValidationResult {
  const unknownProps = Object.keys(config).filter(
    (key) => !validProperties.includes(key),
  );

  if (unknownProps.length > 0) {
    return {
      isValid: false,
      error:
        `Unknown configuration ${unknownProps.length === 1 ? 'property' : 'properties'}:` +
        ` ${unknownProps.join(', ')}. Valid properties are: ${validProperties.join(', ')}.`,
    };
  }

  return { isValid: true };
}
```

## File: `src/core/services/files/files.service.ts`
```typescript
import path from 'path';
import os from 'os';
import {
  ScanOptions,
  IFileService,
  IFileStat,
  GetNewestFileResult,
  RiskAnalysis,
} from '@core/index.js';
import fs, { accessSync, Stats, statSync } from 'fs';
import { readdir, stat } from 'fs/promises';
import { map, Observable, Subject } from 'rxjs';
import { FileWorkerService } from './files.worker.service.js';
import { IsValidRootFolderResult } from '@core/interfaces/npkill.interface.js';

export abstract class FileService implements IFileService {
  public fileWorkerService: FileWorkerService;

  constructor(fileWorkerService: FileWorkerService) {
    this.fileWorkerService = fileWorkerService;
  }

  abstract deleteDir(path: string): Promise<boolean>;

  listDir(path: string, params: ScanOptions): Observable<string> {
    const stream$ = new Subject<string>();
    this.fileWorkerService.startScan(stream$, { ...params, rootPath: path });
    return stream$;
  }

  getFolderSize(path: string): Observable<number> {
    const stream$ = new Subject<number>();
    this.fileWorkerService.getFolderSize(stream$, path);
    return stream$.pipe(map((data) => data));
  }

  stopScan(): void {
    this.fileWorkerService.stopScan();
  }

  /** Used for dry-run or testing. */
  async fakeDeleteDir(): Promise<boolean> {
    const randomDelay = Math.floor(Math.random() * 4000 + 200);
    await new Promise((resolve) => setTimeout(resolve, randomDelay));
    return true;
  }

  isValidRootFolder(path: string): IsValidRootFolderResult {
    let stat: Stats;
    try {
      stat = statSync(path);
    } catch {
      return { isValid: false, invalidReason: 'The path does not exist.' };
    }

    if (!stat.isDirectory()) {
      return {
        isValid: false,
        invalidReason: 'The path must point to a directory.',
      };
    }

    try {
      accessSync(path, fs.constants.R_OK);
    } catch {
      return {
        isValid: false,
        invalidReason: 'Cannot read the specified path.',
      };
    }

    return { isValid: true };
  }

  /**
   * > Why dangerous?
   * It is probable that if the node_module is included in some hidden directory, it is
   * required by some application like "spotify", "vscode" or "Discord" and deleting it
   * would imply breaking the application (until the dependencies are reinstalled).
   *
   * In the case of macOS applications and Windows AppData directory, these locations often contain
   * application-specific data or configurations that should not be tampered with. Deleting directories
   * from these locations could potentially disrupt the normal operation of these applications.
   */
  isDangerous(originalPath: string): RiskAnalysis {
    const isUnc =
      originalPath.startsWith('\\\\') || originalPath.startsWith('//');
    const absolutePath = isUnc
      ? originalPath
      : path.isAbsolute(originalPath)
        ? originalPath
        : path.resolve(process.cwd(), originalPath);

    const normalizePath = (p: string): string => {
      let normalized = p.replace(/\\/g, '/').toLowerCase();
      if (/^[a-z]:\//.test(normalized)) {
        normalized = normalized.substring(2);
      }
      return normalized;
    };

    const normalizedPath = normalizePath(absolutePath);
    const normalizedOriginal = normalizePath(originalPath);

    const home =
      process.env.HOME ?? process.env.USERPROFILE ?? os.homedir() ?? '';
    let isInHome = false;
    let normalizedHome = '';

    if (home !== '') {
      // Normalize the home path. If it's already absolute, just normalize separators.
      // Only use path.resolve() if it's a relative path to avoid cross-platform issues.
      const homeAbsolute = path.isAbsolute(home) ? home : path.resolve(home);
      normalizedHome = normalizePath(homeAbsolute);
      isInHome =
        normalizedPath === normalizedHome ||
        normalizedPath.startsWith(normalizedHome + '/');
    }

    if (isInHome) {
      // Relative path inside HOME (without the HOME prefix)
      let rel = normalizedPath.slice(normalizedHome.length);
      if (rel.startsWith('/')) rel = rel.slice(1);

      // Special sensitive locations inside HOME
      if (rel === '.config' || rel.startsWith('.config/')) {
        return {
          isSensitive: true,
          reason: 'Contains user configuration data (~/.config)',
        };
      }
      if (rel === '.local/share' || rel.startsWith('.local/share/')) {
        return {
          isSensitive: true,
          reason: 'User data folder (~/.local/share)',
        };
      }

      // ~/.cache is safe to delete but system-wide, mark as sensitive
      if (rel === '.cache' || rel.startsWith('.cache/')) {
        return {
          isSensitive: true,
          reason: 'System-wide cache directory (~/.cache)',
        };
      }

      // Whitelisted hidden top-level folders inside HOME
      if (/^\.(npm|pnpm)(\/|$)/.test(rel)) {
        return { isSensitive: false };
      }

      // Only consider TOP-LEVEL hidden entries inside HOME as sensitive
      const topLevel = rel.split('/')[0] ?? '';
      if (
        topLevel.startsWith('.') &&
        topLevel !== '.' &&
        topLevel !== '..' &&
        !['.npm', '.pnpm'].includes(topLevel)
      ) {
        return { isSensitive: true, reason: 'Contains unsafe hidden folder' };
      }
    }

    // macOs
    if (/\/applications\/[^/]+\.app\//.test(normalizedPath)) {
      return { isSensitive: true, reason: 'Inside macOS .app package' };
    }

    // Windows UNC network paths (e.g., \\server\\share -> //server/share)
    if (normalizedOriginal.startsWith('//')) {
      if (/\/\.[^/]+(\/|$)/.test(normalizedOriginal)) {
        return { isSensitive: true, reason: 'Hidden path in network share' };
      }
    }

    // Windows
    if (normalizedPath.includes('/appdata/roaming')) {
      return {
        isSensitive: true,
        reason: 'Inside Windows AppData Roaming folder',
      };
    }
    if (normalizedPath.includes('/appdata/local')) {
      if (/\/\.(cache|npm|pnpm)(\/|$)/.test(normalizedPath)) {
        return { isSensitive: false };
      }
      return {
        isSensitive: true,
        reason: 'Inside Windows AppData Local folder',
      };
    }
    if (/program files( \(x86\))?\//.test(normalizedPath)) {
      return { isSensitive: true, reason: 'Inside Program Files folder' };
    }

    return { isSensitive: false };
  }

  async getRecentModificationInDir(
    path: string,
  ): Promise<GetNewestFileResult | null> {
    const files = await this.getFileStatsInDir(path);
    const sorted = files.sort(
      (a, b) => b.modificationTime - a.modificationTime,
    );
    const newestFile = sorted.length > 0 ? sorted[0] : null;
    if (!newestFile) {
      return null;
    }

    return {
      timestamp: newestFile.modificationTime,
      name: newestFile.path.split('/').pop() || '',
      path: newestFile.path,
    };
  }

  async getFileStatsInDir(dirname: string): Promise<IFileStat[]> {
    const ignoredFolders = ['node_modules', '.git', 'coverage', 'dist'];

    let files: IFileStat[] = [];

    try {
      const items = await readdir(dirname, { withFileTypes: true });

      for (const item of items) {
        if (item.isDirectory()) {
          const itemNameLowerCase = item.name.toLowerCase();
          if (ignoredFolders.includes(itemNameLowerCase)) {
            continue;
          }
          files = [
            ...files,
            ...(await this.getFileStatsInDir(`${dirname}/${item.name}`).catch(
              () => [],
            )),
          ];
        } else {
          try {
            const path = `${dirname}/${item.name}`;
            const fileStat = await stat(path);

            files.push({ path, modificationTime: fileStat.mtimeMs / 1000 });
          } catch {
            // Skip files that can't be accessed (e.g., permission denied, broken symlinks)
            continue;
          }
        }
      }
    } catch {
      // If we can't read the directory (e.j., permission denied), return empty array.
      return [];
    }

    return files;
  }
}
```

## File: `src/core/services/files/files.worker.service.ts`
```typescript
import os from 'os';
import { dirname, extname } from 'path';

import { Worker, MessageChannel, MessagePort } from 'worker_threads';
import { Subject } from 'rxjs';
import { LoggerService } from '../logger.service.js';
import { ScanStatus } from '../../interfaces/search-status.model.js';
import { EVENTS, MAX_WORKERS } from '../../../constants/workers.constants.js';
import { ScanOptions } from '../../index.js';

export type WorkerStatus = 'stopped' | 'scanning' | 'dead' | 'finished';
type WorkerJob = {
  job: EVENTS.explore | EVENTS.getFolderSize;
  value: { path: string };
};

export interface WorkerScanOptions extends ScanOptions {
  rootPath: string;
}

export type WorkerMessage =
  | {
      type: EVENTS.scanResult;
      value: {
        results: Array<{ path: string; isTarget: boolean }>;
        workerId: number;
        pending: number;
      };
    }
  | {
      type: EVENTS.GetSizeResult;
      value: {
        results: { path: string; size: number };
        workerId: number;
        pending: number;
      };
    }
  | { type: EVENTS.explore | EVENTS.getFolderSize; value: { path: string } }
  | { type: EVENTS.exploreConfig; value: WorkerScanOptions }
  | { type: EVENTS.startup; value: { channel: MessagePort; id: number } }
  | { type: EVENTS.alive; value?: undefined }
  | { type: EVENTS.stop; value?: undefined }
  | { type: EVENTS.error; value: { error: Error } };

export interface WorkerStats {
  pendingSearchTasks: number;
  completedSearchTasks: number;
  procs: number;
}

export class FileWorkerService {
  private index = 0;
  private workers: Worker[] = [];
  private workersPendingJobs: number[] = [];
  private getSizePendings: Array<{
    path: string;
    stream$: Subject<number>;
    timeoutId?: NodeJS.Timeout;
  }> = [];

  private pendingJobs = 0;
  private totalJobs = 0;
  private tunnels: MessagePort[] = [];
  private shouldStop = false;
  private readonly SIZE_TIMEOUT_MS = 60000; // 1 minute timeout per folder

  constructor(
    private readonly logger: LoggerService,
    private readonly searchStatus: ScanStatus,
  ) {}

  async startScan(
    stream$: Subject<string>,
    params: WorkerScanOptions,
  ): Promise<void> {
    await this.killWorkers();

    this.totalJobs = 0;
    this.pendingJobs = 0;
    this.index = 0;
    this.workersPendingJobs = [];

    this.shouldStop = false;
    this.instantiateWorkers(this.getOptimalNumberOfWorkers());
    this.listenEvents(stream$);
    this.setWorkerConfig(params);

    // Manually add the first job.
    this.addJob({ job: EVENTS.explore, value: { path: params.rootPath } });
  }

  getFolderSize(stream$: Subject<number>, path: string): void {
    if (this.workers.length === 0) {
      this.instantiateWorkers(this.getOptimalNumberOfWorkers());
      this.listenEvents(new Subject<string>());
      this.setWorkerConfig({ rootPath: path } as WorkerScanOptions);
    }

    const timeoutId = setTimeout(() => {
      const index = this.getSizePendings.findIndex((p) => p.path === path);
      if (index !== -1) {
        this.logger.error(
          `Timeout calculating size for: ${path} (${this.SIZE_TIMEOUT_MS}ms)`,
        );
        const pending = this.getSizePendings[index];
        pending.stream$.error(
          new Error(`Timeout calculating size for ${path}`),
        );
        this.getSizePendings.splice(index, 1);
      }
    }, this.SIZE_TIMEOUT_MS);

    this.getSizePendings = [
      ...this.getSizePendings,
      { path, stream$, timeoutId },
    ];
    this.addJob({ job: EVENTS.getFolderSize, value: { path } });
  }

  stopScan(): void {
    this.logger.info('Stopping scan...');
    this.shouldStop = true;
    this.searchStatus.workerStatus = 'stopped';

    this.tunnels.forEach((tunnel) => {
      tunnel.postMessage({
        type: EVENTS.stop,
        value: undefined,
      });
    });

    void this.killWorkers();
  }

  private listenEvents(stream$: Subject<string>): void {
    this.tunnels.forEach((tunnel) => {
      tunnel.on('message', (data: WorkerMessage) => {
        this.newWorkerMessage(data, stream$);
      });

      this.workers.forEach((worker, index) => {
        worker.on('exit', () => {
          this.logger.info(`Worker ${index} exited.`);
        });

        worker.on('error', (error) => {
          // Respawn worker.
          throw error;
        });
      });
    });
  }

  private newWorkerMessage(
    message: WorkerMessage,
    stream$: Subject<string>,
  ): void {
    const { type, value } = message;

    if (type === EVENTS.scanResult) {
      const results: Array<{ path: string; isTarget: boolean }> = value.results;
      const workerId: number = value.workerId;
      this.workersPendingJobs[workerId] = value.pending;

      results.forEach((result) => {
        const { path, isTarget } = result;
        if (isTarget) {
          stream$.next(path);
        } else if (!this.shouldStop) {
          this.addJob({
            job: EVENTS.explore,
            value: { path },
          });
        }
      });

      this.pendingJobs = this.getPendingJobs();
      this.checkJobComplete(stream$);
    }

    if (type === EVENTS.GetSizeResult) {
      const result: { path: string; size: number } = value.results;
      const workerId: number = value.workerId;
      this.workersPendingJobs[workerId] = value.pending;

      const index = this.getSizePendings.findIndex(
        (pending) => pending.path === result.path,
      );

      if (index !== -1) {
        const pending = this.getSizePendings[index];

        if (pending.timeoutId) {
          clearTimeout(pending.timeoutId);
        }

        pending.stream$.next(result.size);
        pending.stream$.complete();
        this.getSizePendings.splice(index, 1);
      }

      this.pendingJobs = this.getPendingJobs();
      this.checkJobComplete(stream$);
    }

    if (type === EVENTS.alive) {
      this.searchStatus.workerStatus = 'scanning';
    }

    if (type === EVENTS.error) {
      this.logger.error(`Worker error: ${value.error.message}`);
    }
  }

  /** Jobs are distributed following the round-robin algorithm. */
  private addJob(job: WorkerJob): void {
    if (this.shouldStop) {
      return;
    }

    const tunnel = this.tunnels[this.index];
    const message: WorkerMessage = { type: job.job, value: job.value };
    tunnel.postMessage(message);
    this.workersPendingJobs[this.index]++;
    this.totalJobs++;
    this.pendingJobs++;
    this.index = this.index >= this.workers.length - 1 ? 0 : this.index + 1;
  }

  private checkJobComplete(stream$: Subject<string>): void {
    this.updateStats();
    const isCompleted = this.getPendingJobs() === 0;
    if (isCompleted) {
      this.searchStatus.workerStatus = 'finished';
      stream$.complete();
      void this.killWorkers();
    }
  }

  private instantiateWorkers(amount: number): void {
    this.logger.info(`Instantiating ${amount} workers..`);
    for (let i = 0; i < amount; i++) {
      const { port1, port2 } = new MessageChannel();
      const worker = new Worker(this.getWorkerPath());
      this.tunnels.push(port1);
      worker.postMessage(
        { type: EVENTS.startup, value: { channel: port2, id: i } },
        [port2], // Prevent clone the object and pass the original.
      );
      this.workers.push(worker);
      this.logger.info(`Worker ${i} instantiated.`);
    }
  }

  private setWorkerConfig(params: WorkerScanOptions): void {
    this.tunnels.forEach((tunnel) =>
      tunnel.postMessage({
        type: EVENTS.exploreConfig,
        value: params,
      }),
    );
  }

  private async killWorkers(): Promise<void> {
    this.getSizePendings.forEach((pending) => {
      if (pending.timeoutId) {
        clearTimeout(pending.timeoutId);
      }
      if (!pending.stream$.closed) {
        pending.stream$.error(
          new Error('Workers terminated before completion'),
        );
      }
    });
    this.getSizePendings = [];

    for (let i = 0; i < this.workers.length; i++) {
      this.workers[i].removeAllListeners();
      this.tunnels[i].removeAllListeners();
      await this.workers[i]
        .terminate()
        .catch((error) => this.logger.error(error));
    }
    this.workers = [];
    this.tunnels = [];
  }

  private getPendingJobs(): number {
    return this.workersPendingJobs.reduce((acc, x) => x + acc, 0);
  }

  private updateStats(): void {
    this.searchStatus.pendingSearchTasks = this.pendingJobs;
    this.searchStatus.completedSearchTasks = this.totalJobs;
    this.searchStatus.workersJobs = this.workersPendingJobs;
  }

  private getWorkerPath(): URL {
    const actualFilePath = import.meta.url;
    const dirPath = dirname(actualFilePath);
    // Extension = .ts if is not transpiled.
    // Extension = .js if is a build
    const extension = extname(actualFilePath);
    const workerName = 'files.worker';

    return new URL(`${dirPath}/${workerName}${extension}`);
  }

  private getOptimalNumberOfWorkers(): number {
    const cores = os.cpus().length;
    // TODO calculate amount of RAM available and take it
    // as part on the ecuation.
    const numWorkers = cores > MAX_WORKERS ? MAX_WORKERS : cores - 1;
    return numWorkers < 1 ? 1 : numWorkers;
  }
}
```

## File: `src/core/services/files/files.worker.ts`
```typescript
import { Dir, Dirent } from 'fs';
import { lstat, opendir, readdir } from 'fs/promises';
import EventEmitter from 'events';
import { WorkerMessage, WorkerScanOptions } from './files.worker.service.js';
import { join } from 'path';
import { MessagePort, parentPort } from 'node:worker_threads';
import { EVENTS, MAX_PROCS } from '../../../constants/workers.constants.js';
import { GLOBAL_IGNORE } from '../../constants/global-ignored.constants.js';

enum ETaskOperation {
  'explore',
  'getFolderSize',
  'getFolderSizeChild',
}

interface Task {
  operation: ETaskOperation;
  path: string;
  sizeCollector?: {
    total: number;
    pending: number;
    onComplete: (total: number) => void;
  };
}

(() => {
  let id = 0;
  let fileWalker: FileWalker;
  let tunnel: MessagePort;

  if (parentPort === null) {
    throw new Error('Worker must be spawned from a parent thread.');
  }

  parentPort.on('message', (message: WorkerMessage) => {
    if (message?.type === EVENTS.startup) {
      id = message.value.id;
      tunnel = message.value.channel;
      fileWalker = new FileWalker();
      initTunnelListeners();
      initFileWalkerListeners();
      notifyWorkerReady();
    }
  });

  function notifyWorkerReady(): void {
    tunnel.postMessage({
      type: EVENTS.alive,
      value: null,
    });
  }

  function initTunnelListeners(): void {
    tunnel.on('message', (message: WorkerMessage) => {
      if (message?.type === EVENTS.exploreConfig) {
        fileWalker.setSearchConfig(message.value);
      }

      if (message?.type === EVENTS.explore) {
        fileWalker.enqueueTask(message.value.path, ETaskOperation.explore);
      }

      if (message?.type === EVENTS.getFolderSize) {
        fileWalker.enqueueTask(
          message.value.path,
          ETaskOperation.getFolderSize,
          true,
        );
      }

      if (message?.type === EVENTS.stop) {
        fileWalker.stop();
      }
    });
  }

  function initFileWalkerListeners(): void {
    fileWalker.events.on('newResult', ({ results }) => {
      tunnel.postMessage({
        type: EVENTS.scanResult,
        value: { results, workerId: id, pending: fileWalker.pendingJobs },
      });
    });

    fileWalker.events.on(
      'folderSizeResult',
      (result: { path: string; size: number }) => {
        tunnel.postMessage({
          type: EVENTS.GetSizeResult,
          value: {
            results: result,
            workerId: id,
            pending: fileWalker.pendingJobs,
          },
        });
      },
    );
  }
})();

class FileWalker {
  readonly events = new EventEmitter();
  private searchConfig: WorkerScanOptions = {
    rootPath: '',
    targets: [''],
    exclude: [],
  };

  private readonly taskQueue: Task[] = [];
  private completedTasks = 0;
  private procs = 0;
  private shouldStop = false;

  setSearchConfig(params: WorkerScanOptions): void {
    this.searchConfig = params;
  }

  stop(): void {
    this.shouldStop = true;
  }

  enqueueTask(
    path: string,
    operation: ETaskOperation,
    priorize: boolean = false,
    sizeCollector?: Task['sizeCollector'],
  ): void {
    if (this.shouldStop) {
      return;
    }

    const task: Task = { path, operation };
    if (sizeCollector) {
      task.sizeCollector = sizeCollector;
    }

    if (priorize) {
      this.taskQueue.unshift(task);
    } else {
      this.taskQueue.push(task);
    }

    this.processQueue();
  }

  private async run(path: string): Promise<void> {
    this.updateProcs(1);

    try {
      const dir = await opendir(path);
      await this.analizeDir(path, dir);
    } catch {
      this.completeTask();
    }
  }

  private async analizeDir(path: string, dir: Dir): Promise<void> {
    const results = [];
    let entry: Dirent | null = null;

    while ((entry = await dir.read().catch(() => null)) != null) {
      this.newDirEntry(path, entry, results);
    }

    this.events.emit('newResult', { results });
    await dir.close();
    this.completeTask();

    if (this.taskQueue.length === 0 && this.procs === 0) {
      this.completeAll();
    }
  }

  private async runGetFolderSize(path: string): Promise<void> {
    this.updateProcs(1);

    try {
      const collector = {
        total: 0,
        pending: 1,
        onComplete: (finalSize: number) => {
          this.events.emit('folderSizeResult', { path, size: finalSize });
        },
      };

      this.enqueueTask(
        path,
        ETaskOperation.getFolderSizeChild,
        false,
        collector,
      );
      this.completeTask();
    } catch {
      // If anything fails during setup, emit size 0 and complete
      this.events.emit('folderSizeResult', { path, size: 0 });
      this.completeTask();
    }
  }

  private async runGetFolderSizeChild(
    path: string,
    collector: Task['sizeCollector'],
  ): Promise<void> {
    if (!collector) {
      // Should not happen with proper initiation, but safe.
      this.completeTask();
      return;
    }

    this.updateProcs(1);

    try {
      const entries = await readdir(path, { withFileTypes: true });
      let currentLevelSize = 0;
      const directoriesToProcess: string[] = [];

      for (let i = 0; i < entries.length; i += 100) {
        const chunk = entries.slice(i, i + 100);
        await Promise.all(
          chunk.map(async (entry) => {
            const fullPath = join(path, entry.name);
            try {
              if (entry.isSymbolicLink()) {
                return;
              }

              if (entry.isDirectory()) {
                currentLevelSize += 4096; // General directory size
                directoriesToProcess.push(fullPath);
              } else {
                const stats = await lstat(fullPath);
                const size =
                  typeof stats.blocks === 'number'
                    ? stats.blocks * 512
                    : stats.size;

                currentLevelSize += size;
              }
            } catch {
              // Ignore permissions errors.
            }
          }),
        );
      }

      collector.total += currentLevelSize;
      collector.pending += directoriesToProcess.length;

      for (const dirPath of directoriesToProcess) {
        this.enqueueTask(
          dirPath,
          ETaskOperation.getFolderSizeChild,
          false,
          collector,
        );
      }
    } catch {
      // Ignore permissions errors.
    } finally {
      collector.pending -= 1;

      if (collector.pending === 0) {
        collector.onComplete(collector.total);
      }

      this.completeTask();
    }
  }

  private newDirEntry(
    path: string,
    entry: Dirent,
    results: { path: string; isTarget: boolean }[],
  ): void {
    if (entry.isSymbolicLink() || !entry.isDirectory()) {
      return;
    }

    const isTarget = this.isTargetFolder(entry.name);

    if (GLOBAL_IGNORE.has(entry.name) && !isTarget) {
      return;
    }

    const subpath = join(path, entry.name);

    if (this.isExcluded(subpath)) {
      return;
    }

    results.push({
      path: subpath,
      isTarget,
    });
  }

  private isExcluded(path: string): boolean {
    if (this.searchConfig.exclude == null) {
      return false;
    }
    return this.searchConfig.exclude.some((ex) => path.includes(ex));
  }

  private isTargetFolder(path: string): boolean {
    return this.searchConfig.targets.includes(path);
  }

  private completeTask(): void {
    this.updateProcs(-1);
    this.processQueue();
    this.completedTasks++;
  }

  private updateProcs(value: number): void {
    this.procs += value;
  }

  private processQueue(): void {
    while (
      this.procs < MAX_PROCS &&
      this.taskQueue.length > 0 &&
      !this.shouldStop
    ) {
      const task = this.taskQueue.shift();
      if (!task?.path) {
        continue;
      }

      switch (task.operation) {
        case ETaskOperation.explore:
          this.run(task.path).catch(() => {
            this.completeTask();
          });
          break;
        case ETaskOperation.getFolderSize:
          this.runGetFolderSize(task.path).catch(() => {
            // If runGetFolderSize fails, we need to emit a size of 0
            // Otherwise the stream will hang forever
            this.events.emit('folderSizeResult', { path: task.path, size: 0 });
          });
          break;
        case ETaskOperation.getFolderSizeChild:
          this.runGetFolderSizeChild(task.path, task.sizeCollector).catch(
            () => {
              // Ensure we always decrement the collector even on errors
              if (task.sizeCollector == null) {
                // This shouldn't happen, but if it does, we can't recover properly
                // The best we can do is not crash
                return;
              }

              task.sizeCollector.pending -= 1;
              if (task.sizeCollector.pending === 0) {
                task.sizeCollector.onComplete(task.sizeCollector.total);
              }

              this.completeTask();
            },
          );
          break;
      }
    }
  }

  private completeAll(): void {
    // Any future action.
  }

  /*  get stats(): WorkerStats {
    return {
      pendingSearchTasks: this.taskQueue.length,
      completedSearchTasks: this.completedTasks,
      procs: this.procs,
    };
  } */

  get pendingJobs(): number {
    return this.taskQueue.length;
  }
}
```

## File: `src/core/services/files/index.ts`
```typescript
export * from './files.service.js';
export * from './files.worker.service.js';
export * from './unix-files.service.js';
export * from './windows-files.service.js';
```

## File: `src/core/services/files/unix-files.service.ts`
```typescript
import { exec } from 'child_process';

import { FileService } from './files.service.js';
import { Observable, Subject } from 'rxjs';
import { StreamService } from '../stream.service.js';
import { FileWorkerService } from './files.worker.service.js';
import { ScanOptions } from '@core/index.js';

export class UnixFilesService extends FileService {
  constructor(
    protected streamService: StreamService,
    public override fileWorkerService: FileWorkerService,
  ) {
    super(fileWorkerService);
  }

  async deleteDir(path: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
      const command = `rm -rf "${path}"`;
      exec(command, (error, stdout, stderr) => {
        if (error !== null) {
          reject(error);
          return;
        }
        if (stderr !== '') {
          reject(stderr);
          return;
        }
        resolve(true);
      });
    });
  }
}
```

## File: `src/core/services/files/windows-files.service.ts`
```typescript
import { Subject, Observable } from 'rxjs';
import { FileService } from './files.service.js';
import { FileWorkerService } from './files.worker.service.js';
import { ScanOptions } from '@core/index.js';
import { StreamService } from '../stream.service.js';
import { rm } from 'fs/promises';

export class WindowsFilesService extends FileService {
  constructor(
    private readonly streamService: StreamService,
    public override fileWorkerService: FileWorkerService,
  ) {
    super(fileWorkerService);
  }

  async deleteDir(path: string): Promise<boolean> {
    await rm(path, { recursive: true, force: true });
    return true;
  }
}
```

## File: `src/utils/get-file-content.ts`
```typescript
import { readFileSync } from 'fs';

export function getFileContent(path: string): string {
  const encoding = 'utf8';
  return readFileSync(path, encoding);
}
```

## File: `src/utils/is-safe-to-delete.ts`
```typescript
import * as path from 'path';

export function isSafeToDelete(filePath: string, targets: string[]): boolean {
  const lastPath = path.basename(filePath);
  if (!lastPath) {
    return false;
  }

  return targets.some((target) => target === lastPath);
}
```

## File: `src/utils/unit-conversions.ts`
```typescript
export function convertBytesToKB(bytes: number): number {
  const factorBytestoKB = 1024;
  return bytes / factorBytestoKB;
}

export function convertBytesToGb(bytes: number): number {
  return bytes / Math.pow(1024, 3);
}

export function convertGBToMB(gb: number): number {
  const factorGBtoMB = 1024;
  return gb * factorGBtoMB;
}

export function convertGbToKb(gb: number): number {
  const factorGBtoKB = 1024 * 1024;
  return gb * factorGBtoKB;
}

export function convertGbToBytes(gb: number): number {
  return gb * Math.pow(1024, 3);
}

export interface FormattedSize {
  value: number;
  unit: 'MB' | 'GB';
  text: string;
}

export function formatSize(
  sizeInGB: number,
  sizeUnit: 'auto' | 'mb' | 'gb',
  decimals = 2,
): FormattedSize {
  let value: number;
  let unit: 'MB' | 'GB';

  if (sizeUnit === 'gb') {
    value = sizeInGB;
    unit = 'GB';
  } else if (sizeUnit === 'mb') {
    value = convertGBToMB(sizeInGB);
    unit = 'MB';
  } else {
    // auto
    const sizeInMB = convertGBToMB(sizeInGB);
    if (sizeInMB < 1024) {
      value = sizeInMB;
      unit = 'MB';
    } else {
      value = sizeInGB;
      unit = 'GB';
    }
  }

  // For MB, round to no use decimals.
  // For GB, use specified decimals.
  let formattedValue: string;
  if (unit === 'MB') {
    formattedValue = Math.round(value).toString();
  } else {
    formattedValue = value.toFixed(decimals);
  }

  const text = `${formattedValue} ${unit}`;

  return { value, unit, text };
}
```

## File: `tests/index.test.ts`
```typescript
import { jest } from '@jest/globals';

const mainMock = jest.fn();
const fileURLToPathMock = jest.fn();

jest.unstable_mockModule('url', () => ({
  fileURLToPath: fileURLToPathMock,
}));

jest.unstable_mockModule('../src/main.js', () => ({
  default: mainMock,
}));

describe('index.ts', () => {
  beforeEach(() => {
    jest.resetModules();
    mainMock.mockClear();
    fileURLToPathMock.mockClear();
  });

  it('should call main when npkill is called directly from the command line', async () => {
    fileURLToPathMock.mockReturnValue('/path/to/index.ts');
    process.argv[1] = '/path/to/index.ts';

    await importIndex();

    expect(mainMock).toHaveBeenCalled();
  });

  it('should not call main when npkill is imported as a module', async () => {
    fileURLToPathMock.mockReturnValue('/path/to/index.ts');
    process.argv[1] = '/path/to/anotherModule.ts';

    await importIndex();

    expect(mainMock).not.toHaveBeenCalled();
  });
});

function importIndex() {
  return import('../src/index.js');
}
```

## File: `tests/main.test.ts`
```typescript
import { jest } from '@jest/globals';

const controllerConstructorMock = jest.fn();
const constructorInitMock = jest.fn();
const unixServiceConstructorMock = jest.fn();
const windowsServiceConstructorMock = jest.fn();
const fileWorkerServiceConstructorMock = jest.fn();

jest.mock('../src/cli/cli.controller', () => ({
  CliController: controllerConstructorMock.mockImplementation(() => ({
    init: constructorInitMock,
    fileService: {
      getFileContent: jest.fn().mockReturnValue('{}'),
    },
  })),
}));

//#region mock of files services
jest.unstable_mockModule(
  '../src/core/services/files/unix-files.service',
  () => ({
    UnixFilesService: unixServiceConstructorMock,
  }),
);
jest.unstable_mockModule(
  '../src/core/services/files/windows-files.service',
  () => ({
    WindowsFilesService: windowsServiceConstructorMock,
  }),
);
jest.unstable_mockModule(
  '../src/core/services/files/files.worker.service',
  () => ({
    FileWorkerService: fileWorkerServiceConstructorMock,
  }),
);
//#endregion

xdescribe('main', () => {
  let main;
  beforeEach(() => {
    jest.resetModules();
    unixServiceConstructorMock.mockClear();
    windowsServiceConstructorMock.mockClear();
  });

  describe('Should load correct File Service based on the OS', () => {
    const SERVICES_MOCKS = [
      unixServiceConstructorMock,
      windowsServiceConstructorMock,
    ];

    const mockOs = (platform: NodeJS.Platform) => {
      Object.defineProperty(process, 'platform', {
        value: platform,
      });
    };

    const testIfServiceIsIstanciated = async (serviceMock) => {
      const servicesThatShouldNotBeCalled = [...SERVICES_MOCKS].filter(
        (service) => service !== serviceMock,
      );
      expect(serviceMock).toHaveBeenCalledTimes(0);
      main = await import('../src/main.js');
      main.default();
      expect(serviceMock).toHaveBeenCalledTimes(1);
      servicesThatShouldNotBeCalled.forEach((service) =>
        expect(service).toHaveBeenCalledTimes(0),
      );
    };

    it('when OS is Linux', async () => {
      mockOs('linux');
      await testIfServiceIsIstanciated(unixServiceConstructorMock);
    });

    it('when OS is MAC', async () => {
      mockOs('darwin');
      await testIfServiceIsIstanciated(unixServiceConstructorMock);
    });

    it('when OS is Windows', async () => {
      mockOs('win32');
      await testIfServiceIsIstanciated(windowsServiceConstructorMock);
    });
  });
});
```

## File: `tests/cli/cli.controller.test.ts`
```typescript
import { jest } from '@jest/globals';
import { StartParameters } from '../../src/cli/models/start-parameters.model.js';
import { Subject } from 'rxjs';
import {
  ConfigService,
  DeleteResult,
  Npkill,
  ScanStatus,
} from '../../src/core/index.js';
import { LoggerService } from '../../src/core/services/logger.service.js';
import { ResultsService } from '../../src/cli/services/results.service.js';
import { SpinnerService } from '../../src/cli/services/spinner.service.js';
import { ConsoleService } from '../../src/cli/services/console.service.js';
import { UpdateService } from '../../src/cli/services/update.service.js';
import { UiService } from '../../src/cli/services/ui.service.js';
import { ScanService } from '../../src/cli/services/scan.service.js';
import { ERROR_MSG } from '../../src/constants/messages.constants.js';
import { JsonOutputService } from '../../src/cli/services/json-output.service.js';
import { ProfilesService } from '../../src/core/services/profiles.service.js';
import { DEFAULT_CONFIG } from '../../src/constants/main.constants.js';

const resultsUiDeleteMock$ = new Subject<DeleteResult>();
const setDeleteAllWarningVisibilityMock = jest.fn();

jest.mock('../../src/dirname.js', () => {
  return {};
});

jest.unstable_mockModule(
  '../../src/cli/ui/components/header/header.ui.js',
  () => ({
    HeaderUi: jest.fn(),
  }),
);
jest.unstable_mockModule(
  '../../src/cli/ui/components/header/stats.ui.js',
  () => ({
    StatsUi: jest.fn(() => ({ render: jest.fn() })),
  }),
);
jest.unstable_mockModule(
  '../../src/cli/ui/components/header/status.ui.js',
  () => ({
    StatusUi: jest.fn(() => ({
      start: jest.fn(),
      render: jest.fn(),
    })),
  }),
);
jest.unstable_mockModule('../../src/cli/ui/components/general.ui.js', () => ({
  GeneralUi: jest.fn(),
}));
jest.unstable_mockModule('../../src/cli/ui/components/help/help.ui.js', () => ({
  HelpUi: jest.fn(),
}));
jest.unstable_mockModule('../../src/cli/ui/components/results.ui.js', () => ({
  ResultsUi: jest.fn(() => ({
    delete$: resultsUiDeleteMock$,
    showErrors$: { subscribe: jest.fn() },
    openFolder$: { subscribe: jest.fn() },
    showDetails$: { subscribe: jest.fn() },
    endNpkill$: { subscribe: jest.fn() },
    search$: { subscribe: jest.fn() },
    goOptions$: new Subject(),
    render: jest.fn(),
  })),
}));
jest.unstable_mockModule('../../src/cli/ui/components/logs.ui.js', () => ({
  LogsUi: jest.fn(() => ({
    close$: { subscribe: jest.fn() },
  })),
}));
jest.unstable_mockModule('../../src/cli/ui/components/warning.ui.js', () => ({
  WarningUi: jest.fn(() => ({
    setDeleteAllWarningVisibility: setDeleteAllWarningVisibilityMock,
    render: jest.fn(),
    confirm$: new Subject(),
  })),
}));
jest.unstable_mockModule('../../src/cli/ui/base.ui.js', () => ({
  BaseUi: class {
    setVisible() {}
  },
}));
jest.unstable_mockModule('../../src/cli/ui/heavy.ui.js', () => ({
  HeavyUi: {},
}));

const CliControllerConstructor = (
  await import('../../src/cli/cli.controller.js')
).CliController;
class CliController extends CliControllerConstructor {}

describe('CliController test', () => {
  let cliController;

  const filesServiceDeleteMock = jest
    .fn<() => Promise<boolean>>()
    .mockResolvedValue(true);
  const filesServiceFakeDeleteMock = jest
    .fn<() => Promise<boolean>>()
    .mockResolvedValue(true);

  const linuxFilesServiceMock = {
    getFileContent: jest.fn().mockReturnValue('{}'),
    isValidRootFolder: jest.fn().mockReturnValue({ isValid: true }),
    isSafeToDelete: jest.fn().mockReturnValue(true),
    deleteDir: filesServiceDeleteMock,
    fakeDeleteDir: filesServiceFakeDeleteMock,
  };
  const spinnerServiceMock = jest.fn();
  const updateServiceMock = jest.fn();
  const resultServiceMock = jest.fn();
  const searchStatusMock = jest.fn();
  const loggerServiceMock: Partial<LoggerService> = {
    info: jest.fn(),
    error: jest.fn(),
    getSuggestLogFilePath: jest.fn(() => '/example/file'),
    saveToFile: jest.fn(),
  };
  const uiServiceMock = {
    add: jest.fn(),
    print: jest.fn(),
    setRawMode: jest.fn(),
    setCursorVisible: jest.fn(),
    clear: jest.fn(),
    renderAll: jest.fn(),
  };
  const scanServiceMock = {
    scan: jest.fn(),
    calculateFolderStats: jest.fn(),
  };
  const consoleServiceMock = {
    getParameters: () => new StartParameters(),
    isRunningBuild: () => false,
    startListenKeyEvents: jest.fn(),
  };

  const jsonOutputServiceMock = {
    initializeSession: jest.fn(),
    writeStreamResult: jest.fn(),
    getResultsCount: jest.fn(() => 0),
  };

  const npkillDeleteMock = jest.fn();
  const npkillMock: Npkill = {
    logger: loggerServiceMock,
    isValidRootFolder: linuxFilesServiceMock.isValidRootFolder,
    getSize$: jest.fn(),
    getNewestFile$: jest.fn(),
    startScan$: jest.fn(),
    delete$: npkillDeleteMock,
  } as unknown as Npkill;
  const profilesServiceMock = {
    getAvailableProfilesToPrint: jest.fn(),
    getInvalidProfileNames: jest.fn(),
    getTargetsFromProfiles: jest.fn(() => ['node_modules']),
  };
  const configServiceMock = {
    loadConfig: jest.fn().mockReturnValue(DEFAULT_CONFIG),
    validateConfig: jest.fn(),
    mergeConfigs: jest.fn(),
    getUserDefinedProfiles: jest.fn(),
  };

  ////////// mocked Controller Methods
  let showHelpSpy;
  let setupEventsListenerSpy;
  let scanSpy;
  let checkVersionSpy;
  let exitSpy;
  ///////////////////////////////////

  beforeEach(() => {
    jest.clearAllMocks();

    (profilesServiceMock.getTargetsFromProfiles as jest.Mock).mockReturnValue([
      'node_modules',
    ]);

    exitSpy = jest.spyOn(process, 'exit').mockImplementation((number) => {
      throw new Error('process.exit: ' + number);
    });
    cliController = new CliController(
      process.stdout,
      npkillMock,
      loggerServiceMock as LoggerService,
      searchStatusMock as unknown as ScanStatus,
      resultServiceMock as unknown as ResultsService,
      spinnerServiceMock as unknown as SpinnerService,
      consoleServiceMock as unknown as ConsoleService,
      updateServiceMock as unknown as UpdateService,
      uiServiceMock as unknown as UiService,
      scanServiceMock as unknown as ScanService,
      jsonOutputServiceMock as unknown as JsonOutputService,
      profilesServiceMock as unknown as ProfilesService,
      configServiceMock as unknown as ConfigService,
    );

    Object.defineProperty(process.stdout, 'columns', {
      value: 80,
      configurable: true,
    });
    Object.defineProperty(process.stdout, 'isTTY', {
      value: true,
      configurable: true,
    });

    showHelpSpy = jest
      .spyOn(cliController, 'showHelp')
      .mockImplementation(() => ({}));
    setupEventsListenerSpy = jest
      .spyOn(cliController, 'setupEventsListener')
      .mockImplementation(() => ({}));
    scanSpy = jest.spyOn(cliController, 'scan').mockImplementation(() => ({}));
    checkVersionSpy = jest
      .spyOn(cliController, 'checkVersion')
      .mockImplementation(() => ({}));
  });

  it('#init normal start should call some methods', () => {
    cliController.init();
    expect(showHelpSpy).toHaveBeenCalledTimes(0);
    expect(setupEventsListenerSpy).toHaveBeenCalledTimes(1);
    expect(scanSpy).toHaveBeenCalledTimes(1);
    expect(checkVersionSpy).toHaveBeenCalledTimes(1);
  });

  describe('#getArguments', () => {
    const mockParameters = (parameters: object) => {
      consoleServiceMock.getParameters = () => {
        const startParameters = new StartParameters();
        Object.keys(parameters).forEach((key) => {
          startParameters.add(key, parameters[key]);
        });
        return startParameters;
      };
      /*  jest
      .spyOn(consoleService, 'getParameters')
      .mockImplementation((rawArgv) => {
        return parameters;
      }); */
    };

    const spyMethod = (method, fn = () => {}) => {
      return jest.spyOn(cliController, method).mockImplementation(fn);
    };

    afterEach(() => {
      jest.spyOn(process, 'exit').mockReset();
      mockParameters({});
      // Reset DEFAULT_CONFIG to avoid test pollution
      DEFAULT_CONFIG.jsonStream = false;
      DEFAULT_CONFIG.jsonSimple = false;
      DEFAULT_CONFIG.deleteAll = false;
      DEFAULT_CONFIG.dryRun = false;
      DEFAULT_CONFIG.sortBy = 'none';
    });

    it('#showHelp should called if --help flag is present and exit', () => {
      mockParameters({ help: true });
      expect(() => cliController.init()).toThrow();
      expect(showHelpSpy).toHaveBeenCalledTimes(1);
      expect(exitSpy).toHaveBeenCalledTimes(1);
    });

    it('#showProgramVersion should called if --version flag is present and exit', () => {
      mockParameters({ version: true });
      const functionSpy = jest
        .spyOn(cliController, 'showProgramVersion')
        .mockImplementation(() => ({}));
      expect(() => cliController.init()).toThrow();
      expect(functionSpy).toHaveBeenCalledTimes(1);
      expect(exitSpy).toHaveBeenCalledTimes(1);
    });

    it('#checkVersionn should not be called if --no-check-updates is given', () => {
      mockParameters({ 'no-check-updates': true });
      const functionSpy = spyMethod('checkVersion');
      cliController.init();
      expect(functionSpy).toHaveBeenCalledTimes(0);
    });

    describe('--sort-by parameter   ', () => {
      it('Should detect if option is invalid', () => {
        mockParameters({ 'sort-by': 'novalid' });
        spyMethod('isValidSortParam', () => false);
        const functionSpy = spyMethod('invalidSortParam');
        cliController.init();
        expect(functionSpy).toHaveBeenCalledTimes(1);
      });

      // TODO test that check sortBy property is changed
    });

    describe('--delete-all', () => {
      beforeEach(() => {
        jest.clearAllMocks();
        (
          profilesServiceMock.getTargetsFromProfiles as jest.Mock
        ).mockReturnValue(['node_modules']);
      });

      it('Should show a warning before start scan with --targets defined', () => {
        mockParameters({
          'delete-all': true,
          'target-folders': 'node_modules',
        });
        expect(setDeleteAllWarningVisibilityMock).toHaveBeenCalledTimes(0);
        expect(scanSpy).toHaveBeenCalledTimes(0);

        cliController.init();
        expect(setDeleteAllWarningVisibilityMock).toHaveBeenCalledTimes(1);
        expect(scanSpy).toHaveBeenCalledTimes(0);
      });

      it('Should no show a warning if -y is given', () => {
        mockParameters({
          'delete-all': true,
          yes: true,
          'target-folders': 'node_modules',
        });
        expect(setDeleteAllWarningVisibilityMock).toHaveBeenCalledTimes(0);
        expect(scanSpy).toHaveBeenCalledTimes(0);

        cliController.init();
        expect(setDeleteAllWarningVisibilityMock).toHaveBeenCalledTimes(0);
        expect(scanSpy).toHaveBeenCalledTimes(1);
      });
    });

    describe('--dry-run', () => {
      let testFolder: DeleteResult;

      beforeEach(() => {
        testFolder = {
          path: '/my/path/node_modules',
          success: true,
        };
        jest.clearAllMocks();
      });

      it('Should call normal deleteDir function when no --dry-run is included', () => {
        mockParameters({
          'target-folders': 'node_modules',
          'dry-run': 'false',
        });
        cliController.init();

        expect(npkillDeleteMock).toHaveBeenCalledTimes(0);

        resultsUiDeleteMock$.next(testFolder);

        expect(npkillDeleteMock).toHaveBeenCalledTimes(1);
        expect(npkillDeleteMock).toHaveBeenCalledWith(testFolder.path, {
          dryRun: false,
        });
      });

      it('Should call fake deleteDir function instead of deleteDir', () => {
        mockParameters({ 'target-folders': 'node_modules', 'dry-run': true });
        cliController.init();

        expect(npkillDeleteMock).toHaveBeenCalledTimes(0);

        resultsUiDeleteMock$.next(testFolder);

        expect(npkillDeleteMock).toHaveBeenCalledTimes(1);
        expect(npkillDeleteMock).toHaveBeenCalledWith(testFolder.path, {
          dryRun: true,
        });
      });
    });

    describe('--json and --json-stream options', () => {
      it('Should enable JSON stream mode when --json-stream is provided', () => {
        mockParameters({ jsonStream: true });
        const setupJsonSignalsSpy = spyMethod('setupJsonModeSignalHandlers');

        cliController.init();

        expect(setupJsonSignalsSpy).toHaveBeenCalledTimes(1);
        expect(scanSpy).toHaveBeenCalledTimes(1);
      });

      it('Should enable JSON simple mode when --json is provided', () => {
        mockParameters({ jsonSimple: true });
        const setupJsonSignalsSpy = spyMethod('setupJsonModeSignalHandlers');

        cliController.init();

        expect(setupJsonSignalsSpy).toHaveBeenCalledTimes(1);
        expect(scanSpy).toHaveBeenCalledTimes(1);
      });

      it('Should show error and exit when both --json and --json-stream are provided', () => {
        mockParameters({ jsonSimple: true, jsonStream: true });
        const exitWithErrorSpy = spyMethod('exitWithError');

        cliController.init();

        expect(loggerServiceMock.error).toHaveBeenCalledWith(
          ERROR_MSG.CANT_USE_BOTH_JSON_OPTIONS,
        );
        expect(exitWithErrorSpy).toHaveBeenCalledTimes(1);
      });
    });

    describe('TTY Handling', () => {
      it('Should run normally even if stdout is NOT TTY', () => {
        Object.defineProperty(process.stdout, 'isTTY', {
          value: false,
          configurable: true,
        });
        cliController.init();
        expect(scanSpy).toHaveBeenCalledTimes(1);
      });

      it('Should exit if terminal is too small', () => {
        Object.defineProperty(process.stdout, 'columns', {
          value: 10,
          configurable: true,
        });
        const exitWithErrorSpy = spyMethod('exitWithError');
        cliController.init();
        expect(exitWithErrorSpy).toHaveBeenCalledTimes(1);
      });
    });
  });
});
```

## File: `tests/cli/services/console.service.test.ts`
```typescript
import { ConsoleService } from '../../../src/cli/services/console.service.js';

describe('Console Service', () => {
  let consoleService: ConsoleService;
  beforeAll(() => {
    consoleService = new ConsoleService();
  });

  describe('#getParameters', () => {
    it('should get valid parameters', () => {
      const argvs = [
        '/usr/bin/ts-node',
        '/blablabla inexistent parameters',
        '-h',
        '--directory',
        '/sample/path',
        '-D',
        'lala',
        'random text',
        '-f',
        '--exclude-sensitive',
      ];

      const result = consoleService.getParameters(argvs);

      expect(result.isTrue('help')).not.toBeFalsy();
      expect(result.getString('directory')).toBe('/sample/path');
      expect(result.isTrue('delete-all')).not.toBeFalsy();
      expect(result.isTrue('lala')).toBeFalsy();
      expect(result.isTrue('inexistent')).toBeFalsy();
      expect(result.isTrue('full-scan')).not.toBeFalsy();
      expect(result.isTrue('exclude-sensitive')).toBeTruthy();
    });
    it('should get valid parameters 2', () => {
      const argvs = [
        '/usr/bin/ts-node',
        '/blablabla inexistent parameters',
        '-f',
        'lala',
        '--sort=size',
      ];

      const result = consoleService.getParameters(argvs);
      expect(result.isTrue('help')).toBeFalsy();
      expect(result.isTrue('full-scan')).not.toBeFalsy();
      expect(result.getString('sort-by')).toBe('size');
      expect(result.isTrue('exclude-sensitive')).toBeFalsy();
    });
  });

  describe('#splitData', () => {
    it('should split data with default separator', () => {
      expect(consoleService.splitData('foo\nbar\nfoot')).toEqual([
        'foo',
        'bar',
        'foot',
      ]);
    });
    it('should split data with custom separator', () => {
      expect(consoleService.splitData('foo;bar;foot', ';')).toEqual([
        'foo',
        'bar',
        'foot',
      ]);
    });
    it('should return empty array if data is empty', () => {
      expect(consoleService.splitData('')).toEqual([]);
    });
  });

  describe('#splitWordsByWidth', () => {
    it('should get array with text according to width', () => {
      const cases = [
        {
          expect: [
            'Lorem ipsum dolor sit amet, consectetur',
            'adipiscing elit. Mauris faucibus sit amet',
            'libero non vestibulum. Morbi ac tellus',
            'dolor. Duis consectetur eget lectus sed',
            'ullamcorper.',
          ],
          text:
            // tslint:disable-next-line: max-line-length
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris faucibus sit amet libero non vestibulum. Morbi ac tellus dolor. Duis consectetur eget lectus sed ullamcorper.',
          width: 43,
        },
        /* {
          text: 'Lorem ipsum dolor sit amet.',
          width: 2,
          expect: ['Lorem', 'ipsum', 'dolor', 'sit', 'amet.'],
        }, */
      ];

      cases.forEach((cas) => {
        expect(consoleService.splitWordsByWidth(cas.text, cas.width)).toEqual(
          cas.expect,
        );
      });
    });
  });

  describe('#shortenText', () => {
    it('should short text according parameters', () => {
      const cases = [
        {
          cutFrom: 0,
          expect: '...',
          text: '/sample/text/for/test how/service/split/thisA',
          width: 0,
        },
        {
          cutFrom: 10,
          expect: '/sample/te.../service/split/this',
          text: '/sample/text/for/test how/service/split/this',
          width: 32,
        },
        {
          cutFrom: 5,
          expect: '/aaa/.../jjj/kkk',
          text: '/aaa/bbb/ccc/ddd/eee/fff/ggg/hhhh/iiii/jjj/kkk',
          width: 16,
        },
        {
          cutFrom: 3,
          expect: '/neketaro/a:desktop/folder',
          text: '/neketaro/a:desktop/folder',
          width: 50,
        },
      ];

      cases.forEach((cas) => {
        const result = consoleService.shortenText(
          cas.text,
          cas.width,
          cas.cutFrom,
        );
        expect(result).toEqual(cas.expect);
      });
    });

    it('should no modify input if "cutFrom" > text length', () => {
      const text = '/sample/text/';
      const expectResult = '/sample/text/';
      const width = 5;
      const cutFrom = 50;

      const result = consoleService.shortenText(text, width, cutFrom);
      expect(result).toEqual(expectResult);
    });

    it('should no modify input if "cutFrom" > width', () => {
      const text = '/sample/text/';
      const expectResult = '/sample/text/';
      const width = 5;
      const cutFrom = 7;

      const result = consoleService.shortenText(text, width, cutFrom);
      expect(result).toEqual(expectResult);
    });

    it('should ignore negative parameters', () => {
      const cases = [
        {
          cutFrom: -10,
          expect: '/sample/text/for/test how/service/split/thisA',
          text: '/sample/text/for/test how/service/split/thisA',
          width: 5,
        },
        {
          cutFrom: 10,
          expect: '/sample/text/for/test how/service/split/thisB',
          text: '/sample/text/for/test how/service/split/thisB',
          width: -10,
        },
        {
          cutFrom: -20,
          expect: '/sample/text/for/test how/service/split/thisC',
          text: '/sample/text/for/test how/service/split/thisC',
          width: -10,
        },
      ];

      cases.forEach((cas) => {
        const result = consoleService.shortenText(
          cas.text,
          cas.width,
          cas.cutFrom,
        );
        expect(result).toEqual(cas.expect);
      });
    });
  });
});
```

## File: `tests/cli/services/https.service.test.ts`
```typescript
/* eslint-disable promise/valid-params */
/* eslint-disable promise/catch-or-return */
/* eslint-disable promise/no-callback-in-promise */
/* eslint-disable promise/always-return */

import { jest } from '@jest/globals';
import { EventEmitter } from 'events';

let statusCodeMock = 200;
const eventEmitter = new EventEmitter();
const eventEmitter2 = new EventEmitter();
const response = () => ({
  statusCode: statusCodeMock,
  setEncoding: jest.fn(),
  on: (eventName: string, listener: (...args: unknown[]) => void) =>
    eventEmitter2.on(eventName, listener),
});

jest.unstable_mockModule('node:https', () => ({
  get: (url, cb) => {
    cb(response());
    return eventEmitter;
  },
}));

const HttpsServiceConstructor = (
  await import('../../../src/cli/services/https.service.js')
).HttpsService;
class HttpsService extends HttpsServiceConstructor {}

describe('Http Service', () => {
  let httpsService: HttpsService;
  beforeEach(() => {
    httpsService = new HttpsService();
  });

  describe('#get', () => {
    beforeEach(() => {
      statusCodeMock = 200;
    });

    it('should reject if a error ocurr', (done) => {
      const errorMsg = 'test error';
      httpsService
        .getJson('http://sampleUrl')
        .then()
        .catch((error: Error) => {
          expect(error.message).toBe(errorMsg);
          done();
        });
      eventEmitter.emit('error', new Error(errorMsg));
    });

    it('should reject if the code of the response indicate error (101)', (done) => {
      statusCodeMock = 101;
      httpsService
        .getJson('http://sampleUrl')
        .then()
        .catch(() => {
          done();
        });
    });

    it('should reject if the code of the response indicate error (404)', (done) => {
      statusCodeMock = 404;
      httpsService
        .getJson('http://sampleUrl')
        .then()
        .catch(() => {
          done();
        });
    });

    it('should resolve with all chunks of data on end', (done) => {
      const chunks = ['{"key1"', ':"test","ke', 'y2":"p', 'assed"}'];
      const expected = {
        key1: 'test',
        key2: 'passed',
      };

      httpsService.getJson('http://sampleUrl').then((data) => {
        expect(data).toEqual(expected);
        done();
      });

      chunks.forEach((chunk) => eventEmitter2.emit('data', chunk));
      eventEmitter2.emit('end');
    });
  });
});
```

## File: `tests/cli/services/json-output.service.test.ts`
```typescript
import { jest } from '@jest/globals';
import { JsonOutputService } from '../../../src/cli/services/json-output.service.js';
import { CliScanFoundFolder } from '../../../src/cli/interfaces/stats.interface.js';

describe('JsonOutputService', () => {
  let jsonOutputService: JsonOutputService;
  let mockStdout: any;
  let mockStderr: any;

  beforeEach(() => {
    mockStdout = {
      write: jest.fn(),
    };
    mockStderr = {
      write: jest.fn(),
    };
    jsonOutputService = new JsonOutputService(mockStdout, mockStderr);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe('initializeSession', () => {
    it('should initialize session correctly', () => {
      jsonOutputService.initializeSession();
      expect(jsonOutputService.getResultsCount()).toBe(0);
    });
  });

  describe('processResult in stream mode', () => {
    it('should write stream result in correct format', () => {
      const mockFolder: CliScanFoundFolder = {
        path: '/test/node_modules',
        size: 1024,
        modificationTime: 1640995200000,
        status: 'live',
        riskAnalysis: {
          isSensitive: false,
        },
      };

      jsonOutputService.initializeSession(true); // stream mode
      jsonOutputService.processResult(mockFolder);

      expect(mockStdout.write).toHaveBeenCalledTimes(1);
      const writtenData = mockStdout.write.mock.calls[0][0];
      const parsedData = JSON.parse(writtenData.trim());

      expect(parsedData).toMatchObject({
        version: 1,
        result: {
          path: '/test/node_modules',
          size: 1099511627776,
          modificationTime: 1640995200000,
          riskAnalysis: {
            isSensitive: false,
          },
        },
      });
    });
  });

  describe('processResult and completeScan in simple mode', () => {
    it('should collect results and output them in simple format', () => {
      const mockFolder1: CliScanFoundFolder = {
        path: '/test/node_modules',
        size: 1024,
        modificationTime: 1640995200000,
        status: 'live',
      };

      const mockFolder2: CliScanFoundFolder = {
        path: '/test2/node_modules',
        size: 2048,
        modificationTime: 1640995300000,
        status: 'deleted',
      };

      jsonOutputService.initializeSession(false); // simple mode
      jsonOutputService.processResult(mockFolder1);
      jsonOutputService.processResult(mockFolder2);

      expect(jsonOutputService.getResultsCount()).toBe(2);

      jsonOutputService.completeScan();

      expect(mockStdout.write).toHaveBeenCalledTimes(1);
      const writtenData = mockStdout.write.mock.calls[0][0];
      const parsedData = JSON.parse(writtenData.trim());

      expect(parsedData).toMatchObject({
        version: 1,
        results: [
          {
            path: '/test/node_modules',
            size: 1099511627776,
            modificationTime: 1640995200000,
          },
          {
            path: '/test2/node_modules',
            size: 2199023255552,
            modificationTime: 1640995300000,
          },
        ],
        meta: {
          resultsCount: 2,
          runDuration: expect.any(Number),
        },
      });
    });

    it('should not output anything on completeScan in stream mode', () => {
      const mockFolder: CliScanFoundFolder = {
        path: '/test/node_modules',
        size: 1024,
        modificationTime: 1640995200000,
        status: 'live',
      };

      jsonOutputService.initializeSession(true); // stream mode
      jsonOutputService.processResult(mockFolder);
      mockStdout.write.mockClear();

      jsonOutputService.completeScan();

      expect(mockStdout.write).not.toHaveBeenCalled();
    });
  });

  describe('writeError', () => {
    it('should write error in correct format when given Error object', () => {
      const error = new Error('Test error message');
      jsonOutputService.writeError(error);

      expect(mockStderr.write).toHaveBeenCalledTimes(1);
      const writtenData = mockStderr.write.mock.calls[0][0];
      const parsedData = JSON.parse(writtenData.trim());

      expect(parsedData).toMatchObject({
        version: 1,
        error: true,
        message: 'Test error message',
        timestamp: expect.any(Number),
      });
    });

    it('should write error in correct format when given string', () => {
      const error = 'String error message';
      jsonOutputService.writeError(error);

      expect(mockStderr.write).toHaveBeenCalledTimes(1);
      const writtenData = mockStderr.write.mock.calls[0][0];
      const parsedData = JSON.parse(writtenData.trim());

      expect(parsedData).toMatchObject({
        version: 1,
        error: true,
        message: 'String error message',
        timestamp: expect.any(Number),
      });
    });
  });

  describe('handleShutdown', () => {
    it('should output collected results when shutdown is called in simple mode', () => {
      const mockFolder: CliScanFoundFolder = {
        path: '/test/node_modules',
        size: 1024,
        modificationTime: 1640995200000,
        status: 'live',
      };

      jsonOutputService.initializeSession(false); // simple mode
      jsonOutputService.processResult(mockFolder);
      jsonOutputService.handleShutdown();

      expect(mockStdout.write).toHaveBeenCalledTimes(1);
      const writtenData = mockStdout.write.mock.calls[0][0];
      const parsedData = JSON.parse(writtenData.trim());

      expect(parsedData.results).toHaveLength(1);
      expect(parsedData.results[0].path).toBe('/test/node_modules');
    });

    it('should not output anything when no results collected', () => {
      jsonOutputService.initializeSession(false); // simple mode
      jsonOutputService.handleShutdown();

      expect(mockStdout.write).not.toHaveBeenCalled();
    });

    it('should not output anything in stream mode', () => {
      const mockFolder: CliScanFoundFolder = {
        path: '/test/node_modules',
        size: 1024,
        modificationTime: 1640995200000,
        status: 'live',
      };

      jsonOutputService.initializeSession(true); // stream mode
      jsonOutputService.processResult(mockFolder); // This writes to stdout
      mockStdout.write.mockClear(); // Clear the call from processResult

      jsonOutputService.handleShutdown();

      expect(mockStdout.write).not.toHaveBeenCalled();
    });
  });
});
```

## File: `tests/cli/services/profiles.service.test.ts`
```typescript
import { ProfilesService } from '../../../src/core/services/profiles.service.js';
import { DEFAULT_PROFILES } from '../../../src/core/constants/profiles.constants.js';
import { PROFILE } from '../../../src/core/interfaces/profile.interface.js';

describe('ProfilesService', () => {
  let profilesService: ProfilesService;

  beforeEach(() => {
    profilesService = new ProfilesService();
  });

  describe('setUserDefinedProfiles', () => {
    it('should set user-defined profiles', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile for testing',
          targets: ['custom_modules', 'custom_cache'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getProfiles('user');

      expect(result).toEqual(userProfiles);
    });

    it('should override previous user-defined profiles', () => {
      const firstProfiles: Record<string, PROFILE> = {
        first: { description: 'First', targets: ['first'] },
      };
      const secondProfiles: Record<string, PROFILE> = {
        second: { description: 'Second', targets: ['second'] },
      };

      profilesService.setUserDefinedProfiles(firstProfiles);
      profilesService.setUserDefinedProfiles(secondProfiles);
      const result = profilesService.getProfiles('user');

      expect(result).toEqual(secondProfiles);
      expect(result['first']).toBeUndefined();
      expect(result['second']).toBeDefined();
    });
  });

  describe('getProfiles', () => {
    it('should return base profiles when filterType is "base"', () => {
      const result = profilesService.getProfiles('base');

      expect(result).toEqual(DEFAULT_PROFILES);
      expect(result['node']).toBeDefined();
      expect(result['python']).toBeDefined();
    });

    it('should return user profiles when filterType is "user"', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile',
          targets: ['custom_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getProfiles('user');

      expect(result).toEqual(userProfiles);
      expect(result['custom']).toBeDefined();
    });

    it('should return all profiles when filterType is "all"', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile',
          targets: ['custom_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getProfiles('all');

      expect(result['node']).toBeDefined();
      expect(result['python']).toBeDefined();
      expect(result['custom']).toBeDefined();
    });

    it('should default to "all" when no filterType is provided', () => {
      const result = profilesService.getProfiles();

      expect(result).toEqual(DEFAULT_PROFILES);
    });

    it('should allow user profiles to override base profiles', () => {
      const userProfiles: Record<string, PROFILE> = {
        node: {
          description: 'Custom Node profile',
          targets: ['custom_node_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getProfiles('all');

      expect(result['node'].description).toBe('Custom Node profile');
      expect(result['node'].targets).toEqual(['custom_node_modules']);
    });
  });

  describe('getProfileByName', () => {
    it('should return a base profile by name', () => {
      const result = profilesService.getProfileByName('node');

      expect(result).toBeDefined();
      expect(result?.targets).toContain('node_modules');
    });

    it('should return a user-defined profile by name', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile',
          targets: ['custom_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getProfileByName('custom');

      expect(result).toBeDefined();
      expect(result?.targets).toEqual(['custom_modules']);
    });

    it('should prioritize user-defined profiles over base profiles', () => {
      const userProfiles: Record<string, PROFILE> = {
        node: {
          description: 'Custom Node profile',
          targets: ['custom_node_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getProfileByName('node');

      expect(result?.description).toBe('Custom Node profile');
      expect(result?.targets).toEqual(['custom_node_modules']);
    });

    it('should return undefined for non-existent profiles', () => {
      const result = profilesService.getProfileByName('nonexistent');

      expect(result).toBeUndefined();
    });
  });

  describe('hasProfile', () => {
    it('should return true for existing base profiles', () => {
      expect(profilesService.hasProfile('node')).toBe(true);
      expect(profilesService.hasProfile('python')).toBe(true);
    });

    it('should return true for existing user-defined profiles', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile',
          targets: ['custom_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);

      expect(profilesService.hasProfile('custom')).toBe(true);
    });

    it('should return false for non-existent profiles', () => {
      expect(profilesService.hasProfile('nonexistent')).toBe(false);
    });
  });

  describe('getInvalidProfileNames', () => {
    it('should return empty array when all profiles are valid', () => {
      const validProfiles = ['node', 'python', 'java'];
      const result = profilesService.getInvalidProfileNames(validProfiles);

      expect(result).toEqual([]);
    });

    it('should return array with invalid profile names', () => {
      const profiles = ['node', 'invalid-profile', 'python', 'nonexistent'];
      const result = profilesService.getInvalidProfileNames(profiles);

      expect(result).toEqual(['invalid-profile', 'nonexistent']);
    });

    it('should return all profiles when none are valid', () => {
      const invalidProfiles = ['fake1', 'fake2', 'fake3'];
      const result = profilesService.getInvalidProfileNames(invalidProfiles);

      expect(result).toEqual(invalidProfiles);
    });

    it('should return empty array for empty input', () => {
      const result = profilesService.getInvalidProfileNames([]);

      expect(result).toEqual([]);
    });

    it('should be case-sensitive', () => {
      const profiles = ['Node', 'PYTHON', 'node'];
      const result = profilesService.getInvalidProfileNames(profiles);

      expect(result).toEqual(['Node', 'PYTHON']);
    });

    it('should handle profiles with special characters', () => {
      const profiles = ['node', 'python!', 'java@'];
      const result = profilesService.getInvalidProfileNames(profiles);

      expect(result).toEqual(['python!', 'java@']);
    });

    it('should recognize user-defined profiles as valid', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile',
          targets: ['custom_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const result = profilesService.getInvalidProfileNames(['node', 'custom']);

      expect(result).toEqual([]);
    });
  });

  describe('getTargetsFromProfiles', () => {
    it('should return targets for a single profile', () => {
      const result = profilesService.getTargetsFromProfiles(['node']);

      expect(result).toBeInstanceOf(Array);
      expect(result.length).toBeGreaterThan(0);
      expect(result).toContain('node_modules');
      expect(result).toContain('.npm');
    });

    it('should return targets for multiple profiles', () => {
      const result = profilesService.getTargetsFromProfiles(['node', 'python']);

      expect(result).toBeInstanceOf(Array);
      expect(result.length).toBeGreaterThan(0);

      expect(result).toContain('node_modules');

      expect(result).toContain('__pycache__');
      expect(result).toContain('.pytest_cache');
    });

    it('should remove duplicate targets from multiple profiles', () => {
      const result = profilesService.getTargetsFromProfiles(['node', 'python']);

      const uniqueTargets = [...new Set(result)];
      expect(result.length).toBe(uniqueTargets.length);
    });

    it('should return empty array for invalid profile names', () => {
      const result = profilesService.getTargetsFromProfiles([
        'invalid-profile',
      ]);

      expect(result).toEqual([]);
    });

    it('should return empty array for empty input', () => {
      const result = profilesService.getTargetsFromProfiles([]);

      expect(result).toEqual([]);
    });

    it('should skip invalid profiles and return targets from valid ones', () => {
      const result = profilesService.getTargetsFromProfiles([
        'node',
        'invalid-profile',
        'python',
      ]);

      expect(result.length).toBeGreaterThan(0);
      expect(result).toContain('node_modules');
      expect(result).toContain('__pycache__');
    });

    it('should handle the "all" profile correctly', () => {
      const allProfileResult = profilesService.getTargetsFromProfiles(['all']);
      const nodeResult = profilesService.getTargetsFromProfiles(['node']);
      const pythonResult = profilesService.getTargetsFromProfiles(['python']);

      expect(allProfileResult.length).toBeGreaterThan(nodeResult.length);
      expect(allProfileResult.length).toBeGreaterThan(pythonResult.length);

      expect(allProfileResult).toContain('node_modules');
      expect(allProfileResult).toContain('__pycache__');
    });

    it('should maintain target uniqueness when using "all" profile with other profiles', () => {
      const result = profilesService.getTargetsFromProfiles([
        'all',
        'node',
        'python',
      ]);

      const uniqueTargets = [...new Set(result)];
      expect(result.length).toBe(uniqueTargets.length);
    });

    it('should return targets in a consistent order for the same input', () => {
      const result1 = profilesService.getTargetsFromProfiles([
        'node',
        'python',
      ]);
      const result2 = profilesService.getTargetsFromProfiles([
        'node',
        'python',
      ]);

      expect(result1).toEqual(result2);
    });

    it('should handle profile names with different order', () => {
      const result1 = profilesService.getTargetsFromProfiles([
        'node',
        'python',
      ]);
      const result2 = profilesService.getTargetsFromProfiles([
        'python',
        'node',
      ]);

      expect(result1.sort()).toEqual(result2.sort());
    });

    it('should handle all available profiles', () => {
      const allProfileNames = Object.keys(DEFAULT_PROFILES).filter(
        (name) => name !== 'all',
      );
      const result = profilesService.getTargetsFromProfiles(allProfileNames);

      expect(result.length).toBeGreaterThan(0);

      expect(result).toContain('node_modules');
      expect(result).toContain('__pycache__');
    });
  });

  describe('getDefaultProfileName', () => {
    it('should return "node" as the default profile name', () => {
      const result = profilesService.getDefaultProfileName();

      expect(result).toBe('node');
    });
  });

  describe('Integration tests', () => {
    it('should only return valid targets when mixing valid and invalid profiles', () => {
      const badProfiles = profilesService.getInvalidProfileNames([
        'node',
        'fake-profile',
        'python',
      ]);
      const validProfiles = ['node', 'fake-profile', 'python'].filter(
        (p) => !badProfiles.includes(p),
      );
      const targets = profilesService.getTargetsFromProfiles(validProfiles);

      expect(badProfiles).toEqual(['fake-profile']);
      expect(targets.length).toBeGreaterThan(0);
      expect(targets).toContain('node_modules');
      expect(targets).toContain('__pycache__');
    });

    it('should handle workflow of managing profiles and getting targets', () => {
      const userProfiles: Record<string, PROFILE> = {
        custom: {
          description: 'Custom profile',
          targets: ['custom_modules', 'custom_cache'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);

      const badProfiles = profilesService.getInvalidProfileNames([
        'node',
        'invalid',
        'custom',
      ]);
      expect(badProfiles).toEqual(['invalid']);

      const targets = profilesService.getTargetsFromProfiles([
        'node',
        'custom',
      ]);
      expect(targets.length).toBeGreaterThan(0);
      expect(targets).toContain('node_modules');
      expect(targets).toContain('custom_modules');
    });

    it('should allow user profiles to override base profiles in target resolution', () => {
      const userProfiles: Record<string, PROFILE> = {
        node: {
          description: 'Custom Node',
          targets: ['my_custom_modules'],
        },
      };

      profilesService.setUserDefinedProfiles(userProfiles);
      const targets = profilesService.getTargetsFromProfiles(['node']);

      expect(targets).toEqual(['my_custom_modules']);
      expect(targets).not.toContain('node_modules');
    });
  });

  describe('Edge cases', () => {
    it('should handle duplicate profile names in input', () => {
      const result = profilesService.getTargetsFromProfiles([
        'node',
        'node',
        'python',
        'python',
      ]);

      const uniqueTargets = [...new Set(result)];
      expect(result.length).toBe(uniqueTargets.length);
    });

    it('should return consistent results for multiple calls', () => {
      const profiles = ['node', 'python', 'java'];

      const result1 = profilesService.getTargetsFromProfiles(profiles);
      const result2 = profilesService.getTargetsFromProfiles(profiles);
      const result3 = profilesService.getTargetsFromProfiles(profiles);
      const result4 = profilesService.getTargetsFromProfiles(profiles);

      expect(result1).toEqual(result2);
      expect(result2).toEqual(result3);
      expect(result3).toEqual(result4);
    });
  });
});
```

## File: `tests/cli/services/result.service.test.ts`
```typescript
import { CliScanFoundFolder } from '../../../src/cli/interfaces/stats.interface.js';
import { ResultsService } from '../../../src/cli/services/results.service.js';

describe('Result Service', () => {
  let resultService;
  beforeEach(() => {
    resultService = new ResultsService();
  });

  describe('#addResult', () => {
    it('should add folder if that is the first', () => {
      const newResult: CliScanFoundFolder = {
        path: 'path',
        size: 5,
        status: 'live',
        modificationTime: 0,
        riskAnalysis: { isSensitive: false },
      };
      const resultExpected = [newResult];
      resultService.addResult(newResult);
      expect(resultService.results).toMatchObject(resultExpected);
    });
    it('should add folders', () => {
      const newResults: CliScanFoundFolder[] = [
        {
          path: 'path',
          size: 1,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'path2',
          size: 2,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'path3',
          size: 3,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
      ];

      const resultExpected = newResults;

      newResults.forEach((result) => resultService.addResult(result));
      expect(resultService.results).toMatchObject(resultExpected);
    });
  });

  describe('#sortResults', () => {
    let mockResults: CliScanFoundFolder[];
    beforeEach(() => {
      mockResults = [
        {
          path: 'pathd',
          size: 5,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'patha',
          size: 6,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathc',
          size: 16,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathcc',
          size: 0,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathb',
          size: 3,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathz',
          size: 8,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
      ];

      resultService.results = [...mockResults];
    });

    it('should sort by path', () => {
      const expectResult = [
        {
          path: 'patha',
          size: 6,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathb',
          size: 3,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathc',
          size: 16,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathcc',
          size: 0,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathd',
          size: 5,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathz',
          size: 8,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
      ];

      resultService.sortResults('path');
      expect(resultService.results).toMatchObject(expectResult);
    });
    it('should sort by size', () => {
      const expectResult = [
        {
          path: 'pathc',
          size: 16,
          status: 'live',
        },
        {
          path: 'pathz',
          size: 8,
          status: 'live',
        },
        {
          path: 'patha',
          size: 6,
          status: 'live',
        },
        {
          path: 'pathd',
          size: 5,
          status: 'live',
        },
        {
          path: 'pathb',
          size: 3,
          status: 'deleted',
        },
        {
          path: 'pathcc',
          size: 0,
          status: 'deleted',
        },
      ];

      resultService.sortResults('size');
      expect(resultService.results).toMatchObject(expectResult);
    });
    it('should not sort if method dont exist', () => {
      const expectResult = mockResults;

      resultService.sortResults('color');
      expect(resultService.results).toMatchObject(expectResult);
    });
  });

  describe('#getStats', () => {
    let mockResults: CliScanFoundFolder[];
    beforeEach(() => {
      mockResults = [
        {
          path: 'pathd',
          size: 5,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'patha',
          size: 6,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathc',
          size: 16,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathcc',
          size: 0,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathb',
          size: 3,
          status: 'deleted',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
        {
          path: 'pathz',
          size: 8,
          status: 'live',
          modificationTime: 0,
          riskAnalysis: { isSensitive: false },
        },
      ];

      resultService.results = [...mockResults];
    });

    it('should get stats of results', () => {
      const expectResult = {
        spaceReleased: '9.00 GB',
        totalSpace: '38.00 GB',
      };

      const stats = resultService.getStats();
      expect(stats).toMatchObject(expectResult);
    });
  });
});
```

## File: `tests/cli/services/scan.service.test.ts`
```typescript
import { jest } from '@jest/globals';
import { ScanService } from '../../../src/cli/services/scan.service.js';
import { Npkill, ScanFoundFolder, SortBy } from '../../../src/core/index.js';
import {
  CliScanFoundFolder,
  IConfig,
} from '../../../src/cli/interfaces/index.js';
import { of, firstValueFrom, throwError } from 'rxjs';
import { convertBytesToGb } from '../../../src/utils/unit-conversions.js';
import path from 'node:path';
import { DEFAULT_PROFILE } from '../../../src/core/constants/profiles.constants.js';

describe('ScanService', () => {
  let scanService: ScanService;
  let mockNpkill: {
    startScan$: jest.Mock;
    getSize$: jest.Mock;
    getNewestFile$: jest.Mock;
  };

  // Sample data for testing
  const mockConfig: IConfig = {
    profiles: [DEFAULT_PROFILE],
    folderRoot: '/test/root',
    targets: ['node_modules'],
    exclude: ['/test/root/excluded'],
    sortBy: 'size',
    excludeSensitiveResults: false,
    checkUpdates: false,
    deleteAll: false,
    sizeUnit: 'auto',
    maxSimultaneousSearch: 0,
    showErrors: false,
    dryRun: false,
    yes: false,
    jsonStream: false,
    jsonSimple: false,
  };

  const mockScanFoundFolder: ScanFoundFolder = {
    path: '/test/root/project/node_modules',
    riskAnalysis: {
      isSensitive: false,
    },
  };

  const mockSensitiveScanFoundFolder: ScanFoundFolder = {
    path: '/test/root/.hidden/node_modules',
    riskAnalysis: {
      isSensitive: true,
    },
  };

  const mockCliScanFoundFolder: CliScanFoundFolder = {
    path: '/test/root/project/node_modules',
    size: 0,
    modificationTime: -1,
    riskAnalysis: mockScanFoundFolder.riskAnalysis,
    status: 'live',
  };

  beforeEach(() => {
    mockNpkill = {
      startScan$: jest.fn(),
      getSize$: jest.fn(),
      getNewestFile$: jest.fn(),
    };

    scanService = new ScanService(mockNpkill as unknown as Npkill);
  });

  it('should be created', () => {
    expect(scanService).toBeTruthy();
  });

  describe('scan', () => {
    it('should call npkill.startScan$ with the correct parameters', () => {
      mockNpkill.startScan$.mockReturnValue(of(mockScanFoundFolder));

      scanService.scan(mockConfig);

      expect(mockNpkill.startScan$).toHaveBeenCalledWith(
        mockConfig.folderRoot,
        {
          targets: mockConfig.targets,
          exclude: mockConfig.exclude,
          performRiskAnalysis: true,
          sortBy: mockConfig.sortBy as SortBy,
        },
      );
    });

    it('should emit a CliScanFoundFolder for each non-sensitive result', async () => {
      mockNpkill.startScan$.mockReturnValue(of(mockScanFoundFolder));

      const result$ = scanService.scan(mockConfig);
      const emittedValue = await firstValueFrom(result$);

      expect(emittedValue).toEqual({
        path: mockScanFoundFolder.path,
        size: 0,
        modificationTime: -1,
        riskAnalysis: mockScanFoundFolder.riskAnalysis,
        status: 'live',
      });
    });

    it('should filter out sensitive directories if excludeSensitiveResults is true', (done) => {
      const configWithExclusion: IConfig = {
        ...mockConfig,
        excludeSensitiveResults: true,
      };
      mockNpkill.startScan$.mockReturnValue(
        of(mockScanFoundFolder, mockSensitiveScanFoundFolder),
      );

      const results: CliScanFoundFolder[] = [];
      scanService.scan(configWithExclusion).subscribe({
        next: (value) => results.push(value),
        complete: () => {
          expect(results.length).toBe(1);
          expect(results[0].path).toBe(mockScanFoundFolder.path);
          done();
        },
      });
    });

    it('should NOT filter out sensitive directories if excludeSensitiveResults is false', (done) => {
      mockNpkill.startScan$.mockReturnValue(
        of(mockScanFoundFolder, mockSensitiveScanFoundFolder),
      );

      const results: CliScanFoundFolder[] = [];
      scanService.scan(mockConfig).subscribe({
        next: (value) => results.push(value),
        complete: () => {
          expect(results.length).toBe(2);
          expect(results[0].path).toBe(mockScanFoundFolder.path);
          expect(results[1].path).toBe(mockSensitiveScanFoundFolder.path);
          done();
        },
      });
    });
  });

  describe('calculateFolderStats', () => {
    it('should calculate size and get modification time for a non-sensitive folder', async () => {
      const folderSize = 1024 * 1024 * 500; // 500 MB
      const newestFile = { path: 'index.js', timestamp: 1672531200000 }; // Jan 1, 2023

      mockNpkill.getSize$.mockReturnValue(of({ size: folderSize }));
      mockNpkill.getNewestFile$.mockReturnValue(of(newestFile));

      const result$ = scanService.calculateFolderStats(mockCliScanFoundFolder);
      const result = await firstValueFrom(result$);

      expect(mockNpkill.getSize$).toHaveBeenCalledWith(
        mockCliScanFoundFolder.path,
      );
      expect(mockNpkill.getNewestFile$).toHaveBeenCalledWith(
        path.normalize('/test/root/project/'), // parent folder
      );
      expect(result.size).toBe(convertBytesToGb(folderSize));
      expect(result.modificationTime).toBe(newestFile.timestamp);
    });

    it('should NOT get modification time for a sensitive folder', async () => {
      const sensitiveCliFolder: CliScanFoundFolder = {
        ...mockCliScanFoundFolder,
        riskAnalysis: {
          isSensitive: true,
        },
      };
      const folderSize = 1024 * 1024 * 200; // 200 MB

      mockNpkill.getSize$.mockReturnValue(of({ size: folderSize }));

      const result$ = scanService.calculateFolderStats(sensitiveCliFolder);
      const result = await firstValueFrom(result$);

      expect(mockNpkill.getSize$).toHaveBeenCalledWith(sensitiveCliFolder.path);
      // Should not attempt to get the newest file for sensitive folders
      expect(mockNpkill.getNewestFile$).not.toHaveBeenCalled();
      expect(result.size).toBe(convertBytesToGb(folderSize));
      expect(result.modificationTime).toBe(-1);
    });

    it('should handle the case where getNewestFile$ emits null', async () => {
      const folderSize = 1024 * 1024 * 100; // 100 MB

      mockNpkill.getSize$.mockReturnValue(of({ size: folderSize }));
      mockNpkill.getNewestFile$.mockReturnValue(of(null)); // Simulate no file found

      const result$ = scanService.calculateFolderStats(mockCliScanFoundFolder);
      const result = await firstValueFrom(result$);

      expect(result.size).toBe(convertBytesToGb(folderSize));
      expect(result.modificationTime).toBe(1);
    });

    it('should handle errors in getSize$ and set size to 0', async () => {
      mockNpkill.getSize$.mockReturnValue(
        throwError(() => new Error('Permission denied')),
      );
      mockNpkill.getNewestFile$.mockReturnValue(of(null));

      const result$ = scanService.calculateFolderStats(mockCliScanFoundFolder);
      const result = await firstValueFrom(result$);

      expect(result.size).toBe(0);
      expect(result.modificationTime).toBe(1);
    });

    it('should handle errors in getNewestFile$ and set modificationTime to 1', async () => {
      const folderSize = 1024 * 1024 * 100; // 100 MB

      mockNpkill.getSize$.mockReturnValue(of({ size: folderSize }));
      mockNpkill.getNewestFile$.mockReturnValue(
        throwError(() => new Error('Permission denied')),
      );

      const result$ = scanService.calculateFolderStats(mockCliScanFoundFolder);
      const result = await firstValueFrom(result$);

      expect(result.size).toBe(convertBytesToGb(folderSize));
      expect(result.modificationTime).toBe(1);
    });
  });
});
```

## File: `tests/cli/services/spinner.service.test.ts`
```typescript
import { jest } from '@jest/globals';
import { SpinnerService } from '../../../src/cli/services/spinner.service.js';

describe('Spinner Service', () => {
  let spinnerService: SpinnerService;

  beforeEach(() => {
    spinnerService = new SpinnerService();
  });

  describe('#setSpinner', () => {
    // it('should set spinner passed by argument', () => {});

    it('should reset count', () => {
      const resetFn = (spinnerService.reset = jest.fn());
      spinnerService.setSpinner([]);
      expect(resetFn).toHaveBeenCalled();
    });
  });

  describe('#nextFrame', () => {
    it('should get next frame in orden every call', () => {
      spinnerService.setSpinner(['a  ', ' b ', '  c']);
      expect(spinnerService.nextFrame()).toBe('a  ');
      expect(spinnerService.nextFrame()).toBe(' b ');
      expect(spinnerService.nextFrame()).toBe('  c');
      expect(spinnerService.nextFrame()).toBe('a  ');
    });
  });

  describe('#reset', () => {
    it('should set to first frame', () => {
      spinnerService.setSpinner(['1', '2', '3']);
      expect(spinnerService.nextFrame()).toBe('1');
      expect(spinnerService.nextFrame()).toBe('2');
      spinnerService.reset();
      expect(spinnerService.nextFrame()).toBe('1');
    });
  });
});
```

## File: `tests/cli/services/ui.service.test.ts`
```typescript
import { jest } from '@jest/globals';
import { UiService } from '../../../src/cli/services/ui.service.js';

jest.mock('../../../src/dirname.js', () => {
  return {};
});

describe('UiService', () => {
  let uiService: UiService;
  let stdinMock: any;
  let stdoutMock: any;

  beforeEach(() => {
    stdinMock = {
      isTTY: true,
      setRawMode: jest.fn(),
      resume: jest.fn(),
      on: jest.fn(),
    };
    stdoutMock = {
      write: jest.fn(),
    };

    // Mock process.stdout and process.stdin
    Object.defineProperty(process, 'stdin', {
      value: stdinMock,
      configurable: true,
    });
    Object.defineProperty(process, 'stdout', {
      value: stdoutMock,
      configurable: true,
    });

    uiService = new UiService();
    // Inject the mocked stdin into the service instance as it's assigned in the property declaration
    uiService.stdin = stdinMock;
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe('setRawMode', () => {
    it('should call setRawMode when stdin is TTY', () => {
      uiService.setRawMode(true);
      expect(stdinMock.setRawMode).toHaveBeenCalledWith(true);
      expect(stdinMock.resume).toHaveBeenCalled();
    });

    it('should NOT call setRawMode when stdin is NOT TTY', () => {
      // update mock to simulate non-TTY
      stdinMock.isTTY = false;

      uiService.setRawMode(true);
      expect(stdinMock.setRawMode).not.toHaveBeenCalled();
      expect(stdinMock.resume).toHaveBeenCalled(); // Resume should still be called
    });
  });
});
```

## File: `tests/cli/services/update.service.test.ts`
```typescript
/* eslint-disable promise/no-callback-in-promise */
/* eslint-disable promise/always-return */
import { jest } from '@jest/globals';

import { HttpsService } from '../../../src/cli/services/https.service.js';
import { UpdateService } from '../../../src/cli/services/update.service.js';

describe('update Service', () => {
  let updateService: UpdateService;
  let httpsService: HttpsService;

  beforeEach(() => {
    httpsService = new HttpsService();
    updateService = new UpdateService(httpsService);
  });

  describe('#isUpdated', () => {
    const cases = [
      {
        isUpdated: false,
        localVersion: '2.3.6',
        remoteVersion: '2.4.0',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '2.3.6',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '2.3.6-0',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '2.3.6-2',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6-1',
        remoteVersion: '2.3.6-2',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '0.3.6',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '0.2.1',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '2.2.1',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '2.3.5',
      },
      {
        isUpdated: true,
        localVersion: '2.3.6',
        remoteVersion: '0.2.53',
      },
      {
        isUpdated: false,
        localVersion: '2.3.6',
        remoteVersion: '2.3.61',
      },
      {
        isUpdated: false,
        localVersion: '2.3.6',
        remoteVersion: '2.3.59',
      },
      {
        isUpdated: false,
        localVersion: '2.3.6',
        remoteVersion: '2.3.7',
      },
      {
        isUpdated: false,
        localVersion: '2.3.6-0',
        remoteVersion: '4.74.452',
      },
      {
        isUpdated: true,
        localVersion: '0.10.0',
        remoteVersion: '0.9.0',
      },
      {
        isUpdated: true,
        localVersion: '0.11.0',
        remoteVersion: '0.9.0',
      },
    ];

    cases.forEach((cas) => {
      it(`should check the local version ${cas.localVersion} is up to date with the remote ${cas.remoteVersion}`, (done) => {
        const mockResponse = `{"last-recomended-version": "${cas.remoteVersion}"}`;
        jest
          .spyOn(httpsService, 'getJson')
          .mockImplementation(() => Promise.resolve(JSON.parse(mockResponse)));

        updateService
          .isUpdated(cas.localVersion)
          .then((isUpdated) => {
            expect(isUpdated).toBe(cas.isUpdated);
            done();
          })
          .catch(done);
      });
    });
  });
});
```

## File: `tests/cli/ui/results.ui.test.ts`
```typescript
import { ConsoleService } from '../../../src/cli/services/index.js';
import { ResultsService } from '../../../src/cli/services/results.service.js';
import { jest } from '@jest/globals';
import { CliScanFoundFolder } from '../../../src/cli/interfaces/stats.interface.js';

const stdoutWriteMock = jest.fn() as unknown;

const originalProcess = process;
const mockProcess = () => {
  global.process = {
    ...originalProcess,
    stdout: {
      write: stdoutWriteMock,
      rows: 30,
      columns: 80,
    } as NodeJS.WriteStream & {
      fd: 1;
    },
  };
};

const ResultsUiConstructor = (
  await import('../../../src/cli/ui/components/results.ui.js')
).ResultsUi;
class ResultsUi extends ResultsUiConstructor {}

describe('ResultsUi', () => {
  let resultsUi: ResultsUi;

  const resultsServiceMock: ResultsService = {
    results: [],
  } as unknown as ResultsService;

  const consoleServiceMock: ConsoleService = {
    shortenText: (text) => text,
  } as unknown as ConsoleService;

  beforeEach(() => {
    mockProcess();
    resultsServiceMock.results = [];
    resultsUi = new ResultsUi(resultsServiceMock, consoleServiceMock);
  });

  afterEach(() => {
    jest.resetAllMocks();
  });

  describe('render', () => {
    it('should render results', () => {
      resultsServiceMock.results = [
        {
          path: 'path/folder/1',
          size: 1,
          status: 'live',
        },
        {
          path: 'path/folder/2',
          size: 1,
          status: 'live',
        },
      ] as CliScanFoundFolder[];

      resultsUi.render();

      // With stringContaining we can ignore the terminal color codes.
      expect(stdoutWriteMock).toHaveBeenCalledWith(
        expect.stringContaining('path/folder/1'),
      );
      expect(stdoutWriteMock).toHaveBeenCalledWith(
        expect.stringContaining('path/folder/2'),
      );
    });

    // eslint-disable-next-line quotes
    it("should't render results if it is not visible", () => {
      const populateResults = () => {
        for (let i = 0; i < 100; i++) {
          resultsServiceMock.results.push({
            path: `path/folder/${i}`,
            size: 1,
            status: 'live',
            isDangerous: false,
            modificationTime: -1,
          } as CliScanFoundFolder);
        }
      };

      populateResults();
      resultsUi.render();

      // With stringContaining we can ignore the terminal color codes.
      expect(stdoutWriteMock).toHaveBeenCalledWith(
        expect.stringContaining('path/folder/1'),
      );
      expect(stdoutWriteMock).not.toHaveBeenCalledWith(
        expect.stringContaining('path/folder/64'),
      );
    });
  });

  describe('selection mode', () => {
    let folders: CliScanFoundFolder[];

    beforeEach(() => {
      folders = [
        { path: 'folder/1', size: 1, status: 'live' } as CliScanFoundFolder,
        { path: 'folder/2', size: 1, status: 'live' } as CliScanFoundFolder,
        { path: 'folder/3', size: 1, status: 'live' } as CliScanFoundFolder,
      ];

      resultsServiceMock.results = folders;
      resultsUi = new ResultsUi(resultsServiceMock, consoleServiceMock);
    });

    it('should toggle select mode on and off with "t"', () => {
      expect(resultsUi['selectMode']).toBe(false);

      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      });
      expect(resultsUi['selectMode']).toBe(true);

      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      });
      expect(resultsUi['selectMode']).toBe(false);
      expect(resultsUi['selectedFolders'].size).toBe(0);
    });

    it('should select and unselect folder with space', () => {
      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      }); // enable select mode

      resultsUi.onKeyInput({
        name: 'space',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: ' ',
      });
      expect(resultsUi['selectedFolders'].has('folder/1')).toBe(true);

      resultsUi.onKeyInput({
        name: 'space',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: ' ',
      });
      expect(resultsUi['selectedFolders'].has('folder/1')).toBe(false);
    });

    it('should start and end range selection with "v"', () => {
      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      }); // select mode on

      resultsUi.onKeyInput({
        name: 'v',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 'v',
      }); // start range
      expect(resultsUi['isRangeSelectionMode']).toBe(true);
      expect(resultsUi['rangeSelectionStart']).toBe(0);

      resultsUi.onKeyInput({
        name: 'down',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: '\u001b[B',
      }); // move to folder/2
      expect(resultsUi['selectedFolders'].has('folder/1')).toBe(true);
      expect(resultsUi['selectedFolders'].has('folder/2')).toBe(true);

      resultsUi.onKeyInput({
        name: 'v',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 'v',
      }); // end range
      expect(resultsUi['isRangeSelectionMode']).toBe(false);
      expect(resultsUi['rangeSelectionStart']).toBe(null);
    });

    it('should delete all selected folders on enter', () => {
      const spy = jest.spyOn(resultsUi['delete$'], 'next');

      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      }); // selection mode
      resultsUi.onKeyInput({
        name: 'space',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: ' ',
      }); // select folder/1
      resultsUi.onKeyInput({
        name: 'down',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: '\u001b[B',
      });
      resultsUi.onKeyInput({
        name: 'space',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: ' ',
      }); // select folder/2

      resultsUi.onKeyInput({
        name: 'enter',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: '\r',
      });

      expect(spy).toHaveBeenCalledTimes(2);
      expect(spy).toHaveBeenCalledWith(folders[0]);
      expect(spy).toHaveBeenCalledWith(folders[1]);

      expect(resultsUi['selectedFolders'].size).toBe(0);
    });

    it('should clear range selection when toggling mode off', () => {
      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      }); // selection mode on
      resultsUi.onKeyInput({
        name: 'v',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 'v',
      }); // start range
      resultsUi.onKeyInput({
        name: 'down',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: '\u001b[B',
      }); // move and apply range

      expect(resultsUi['selectedFolders'].size).toBe(2);
      expect(resultsUi['isRangeSelectionMode']).toBe(true);

      resultsUi.onKeyInput({
        name: 't',
        meta: false,
        ctrl: false,
        shift: false,
        sequence: 't',
      }); // toggle mode off
      expect(resultsUi['selectMode']).toBe(false);
      expect(resultsUi['selectedFolders'].size).toBe(0);
      expect(resultsUi['rangeSelectionStart']).toBe(null);
    });
  });
});
```

## File: `tests/core/npkill.test.ts`
```typescript
import { jest } from '@jest/globals';
import { of, throwError, BehaviorSubject } from 'rxjs';
import { take } from 'rxjs/operators';
import { Npkill } from '../../src/core/npkill.js';
import { IFileService } from '../../src/core/interfaces/file-service.interface.js';
import { LoggerService } from '../../src/core/services/logger.service.js';
import { ScanStatus } from '../../src/core/interfaces/search-status.model.js';
import {
  ScanOptions,
  ScanFoundFolder,
  GetSizeResult,
  GetNewestFileResult,
  DeleteResult,
  DeleteOptions,
  RiskAnalysis,
} from '../../src/core/interfaces/folder.interface.js';
import { LogEntry } from '../../src/core/interfaces/logger-service.interface.js';
import { IsValidRootFolderResult } from '../../src/core/interfaces/npkill.interface.js';
import { FileService } from '../../src/core/services/files/index.js';

describe('Npkill', () => {
  let npkill: Npkill;
  let fileServiceMock: jest.Mocked<IFileService>;
  let loggerMock: jest.Mocked<LoggerService>;
  let searchStatusMock: jest.Mocked<ScanStatus>;
  let logSubject: BehaviorSubject<LogEntry[]>;

  beforeEach(() => {
    // Reset all mocks
    jest.clearAllMocks();

    // Create mock services
    fileServiceMock = {
      listDir: jest.fn(),
      getFolderSize: jest.fn(),
      getRecentModificationInDir: jest.fn(),
      deleteDir: jest.fn(),
      fakeDeleteDir: jest.fn(() => Promise.resolve(true)),
      isValidRootFolder: jest.fn(),
      isDangerous: jest.fn(),
      getFileStatsInDir: jest.fn(),
      stopScan: jest.fn(),
      fileWorkerService: {
        startScan: jest.fn(),
        getFolderSize: jest.fn(),
        stopScan: jest.fn(),
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
      } as unknown as any,
    };

    logSubject = new BehaviorSubject<LogEntry[]>([]);
    loggerMock = {
      info: jest.fn(),
      warn: jest.fn(),
      error: jest.fn(),
      get: jest.fn(),
      getLog$: jest.fn(() => logSubject.asObservable()),
      getLogByType$: jest.fn(),
      saveToFile: jest.fn(),
      getSuggestLogFilePath: jest.fn(),
      // Private properties (for mocking purposes)
      log: [],
      logSubject: logSubject,
      rotateLogFile: jest.fn(),
      addToLog: jest.fn(),
      getTimestamp: jest.fn(() => Date.now()),
    } as unknown as jest.Mocked<LoggerService>;

    searchStatusMock = {} as jest.Mocked<ScanStatus>;

    // Mock getVersion dependencies
    jest.mock('../../src/utils/get-file-content.js', () => ({
      getFileContent: jest.fn(() => JSON.stringify({ version: '1.0.0' })),
    }));

    npkill = new Npkill({
      fileService: fileServiceMock as unknown as FileService,
      logger: loggerMock,
      searchStatus: searchStatusMock,
    });
  });

  describe('constructor', () => {
    it('should initialize with custom services', () => {
      expect(npkill).toBeInstanceOf(Npkill);
      expect(loggerMock.info).toHaveBeenCalledWith(
        expect.stringContaining('Npkill started!'),
      );
    });

    it('should initialize with default services when none provided', () => {
      const defaultNpkill = new Npkill();
      expect(defaultNpkill).toBeInstanceOf(Npkill);
    });
  });

  describe('startScan$', () => {
    const mockRootPath = '/test/root';
    const mockOptions: ScanOptions = {
      targets: ['node_modules'],
      exclude: ['node_modules/.cache'],
      sortBy: 'size',
      performRiskAnalysis: true,
    };

    it('should emit scan results with risk analysis enabled', (done) => {
      const mockFolderData = 'folder1\nfolder2\nfolder3';
      const mockRiskAnalysis: RiskAnalysis = {
        isSensitive: false,
      };

      fileServiceMock.listDir.mockReturnValue(of(mockFolderData));
      fileServiceMock.isDangerous.mockReturnValue(mockRiskAnalysis);

      const results: ScanFoundFolder[] = [];
      npkill.startScan$(mockRootPath, mockOptions).subscribe({
        next: (result) => {
          results.push(result);
        },
        complete: () => {
          expect(results).toHaveLength(3);
          expect(results[0]).toEqual({
            path: 'folder1',
            riskAnalysis: mockRiskAnalysis,
          });
          expect(fileServiceMock.isDangerous).toHaveBeenCalledTimes(3);
          expect(loggerMock.info).toHaveBeenCalledWith(
            `Scan started in ${mockRootPath}`,
          );
          done();
        },
      });
    });

    it('should emit scan results without risk analysis when disabled', (done) => {
      const mockFolderData = 'folder1\nfolder2';
      const optionsWithoutRisk = { ...mockOptions, performRiskAnalysis: false };

      fileServiceMock.listDir.mockReturnValue(of(mockFolderData));

      const results: ScanFoundFolder[] = [];
      npkill.startScan$(mockRootPath, optionsWithoutRisk).subscribe({
        next: (result) => {
          results.push(result);
        },
        complete: () => {
          expect(results).toHaveLength(2);
          expect(results[0]).toEqual({ path: 'folder1' });
          expect(fileServiceMock.isDangerous).not.toHaveBeenCalled();
          done();
        },
      });
    });

    it('should filter out empty paths', (done) => {
      const mockFolderData = 'folder1\n\nfolder3\n';
      fileServiceMock.listDir.mockReturnValue(of(mockFolderData));

      const results: ScanFoundFolder[] = [];
      npkill.startScan$(mockRootPath, mockOptions).subscribe({
        next: (result) => {
          results.push(result);
        },
        complete: () => {
          expect(results).toHaveLength(2);
          expect(results.map((r) => r.path)).toEqual(['folder1', 'folder3']);
          done();
        },
      });
    });

    it('should handle errors in listDir', (done) => {
      fileServiceMock.listDir.mockReturnValue(
        throwError(() => new Error('Permission denied')),
      );

      npkill.startScan$(mockRootPath, mockOptions).subscribe({
        next: () => {},
        error: (error) => {
          expect(error).toBeInstanceOf(Error);
          expect(error.message).toBe('Error while listing directories');
          done();
        },
      });
    });

    it('should log completion time', (done) => {
      fileServiceMock.listDir.mockReturnValue(of('folder1'));

      npkill.startScan$(mockRootPath, mockOptions).subscribe({
        complete: () => {
          expect(loggerMock.info).toHaveBeenCalledWith(
            expect.stringMatching(/^Search completed after \d+(\.\d+)?s$/),
          );
          done();
        },
      });
    });
  });

  describe('getSize$', () => {
    const mockPath = '/test/folder';

    it('should return folder size in bytes', (done) => {
      const mockSize = 1024;
      fileServiceMock.getFolderSize.mockReturnValue(of(mockSize));

      npkill.getSize$(mockPath).subscribe((result: GetSizeResult) => {
        expect(result).toEqual({
          size: mockSize,
          unit: 'bytes',
        });
        expect(loggerMock.info).toHaveBeenCalledWith(
          `Calculating folder size for ${mockPath}`,
        );
        expect(loggerMock.info).toHaveBeenCalledWith(
          `Size of ${mockPath}: ${mockSize} bytes`,
        );
        done();
      });
    });

    it('should take only one value from the stream', () => {
      fileServiceMock.getFolderSize.mockReturnValue(of(100, 200, 300));

      npkill
        .getSize$(mockPath)
        .pipe(take(1))
        .subscribe((result) => {
          expect(result.size).toBe(100);
        });
    });
  });

  describe('getNewestFile$', () => {
    const mockPath = '/test/folder';

    it('should return newest file information', (done) => {
      const mockResult: GetNewestFileResult = {
        path: '/test/folder/newest.txt',
        name: 'newest.txt',
        timestamp: 1640995200000,
      };

      fileServiceMock.getRecentModificationInDir.mockResolvedValue(mockResult);

      npkill.getNewestFile$(mockPath).subscribe((result) => {
        expect(result).toEqual(mockResult);
        expect(loggerMock.info).toHaveBeenCalledWith(
          `Calculating last mod. of ${mockPath}`,
        );
        expect(loggerMock.info).toHaveBeenCalledWith(
          `Last mod. of ${mockPath}: ${mockResult.timestamp}`,
        );
        done();
      });
    });

    it('should handle null result when no files found', (done) => {
      fileServiceMock.getRecentModificationInDir.mockResolvedValue(null);

      npkill.getNewestFile$(mockPath).subscribe((result) => {
        expect(result).toBeNull();
        expect(loggerMock.info).toHaveBeenCalledWith(
          `Calculating last mod. of ${mockPath}`,
        );
        // Should not log the timestamp when result is null
        expect(loggerMock.info).not.toHaveBeenCalledWith(
          expect.stringContaining('Last mod. of'),
        );
        done();
      });
    });
  });

  describe('delete$', () => {
    const mockPath = '/test/folder/node_modules';

    it('should successfully delete folder', (done) => {
      fileServiceMock.deleteDir.mockResolvedValue(true);

      npkill.delete$(mockPath).subscribe({
        next: (result: DeleteResult) => {
          expect(result).toEqual({
            path: mockPath,
            success: true,
          });
          expect(fileServiceMock.deleteDir).toHaveBeenCalledWith(mockPath);
          expect(loggerMock.info).toHaveBeenCalledWith(
            `Deleting ${mockPath} ...`,
          );
          expect(loggerMock.info).toHaveBeenCalledWith(
            `Deleted ${mockPath}: true`,
          );
          done();
        },
        error: (err) => {
          done(err);
        },
      });
    });

    it('should handle deletion failure', (done) => {
      fileServiceMock.deleteDir.mockResolvedValue(false);

      npkill.delete$(mockPath).subscribe((result: DeleteResult) => {
        expect(result).toEqual({
          path: mockPath,
          success: false,
        });
        expect(loggerMock.error).toHaveBeenCalledWith(
          `Failed to delete ${mockPath}`,
        );
        done();
      });
    });

    it('should perform dry run when specified', (done) => {
      const options: DeleteOptions = { dryRun: true };
      fileServiceMock.fakeDeleteDir.mockResolvedValue(true);

      npkill.delete$(mockPath, options).subscribe((result: DeleteResult) => {
        expect(result).toEqual({
          path: mockPath,
          success: true,
        });
        expect(fileServiceMock.fakeDeleteDir).toHaveBeenCalled();
        expect(fileServiceMock.deleteDir).not.toHaveBeenCalled();
        expect(loggerMock.info).toHaveBeenCalledWith(
          `Deleting ${mockPath} (dry run)...`,
        );
        done();
      });
    });
  });

  describe('getLogs$', () => {
    it('should return log stream from logger service', (done) => {
      const mockLogs: LogEntry[] = [
        { type: 'info', timestamp: Date.now(), message: 'Test log' },
      ];
      logSubject.next(mockLogs);

      npkill.getLogs$().subscribe((logs) => {
        expect(logs).toEqual(mockLogs);
        done();
      });
    });
  });

  describe('stopScan', () => {
    it('should stop scan and log action', () => {
      npkill.stopScan();

      expect(loggerMock.info).toHaveBeenCalledWith('Stopping scan...');
      expect(fileServiceMock.stopScan).toHaveBeenCalled();
    });
  });

  describe('isValidRootFolder', () => {
    const mockPath = '/test/root';

    it('should return valid result for valid folder', () => {
      const mockResult: IsValidRootFolderResult = {
        isValid: true,
      };
      fileServiceMock.isValidRootFolder.mockReturnValue(mockResult);

      const result = npkill.isValidRootFolder(mockPath);

      expect(result).toEqual(mockResult);
      expect(fileServiceMock.isValidRootFolder).toHaveBeenCalledWith(mockPath);
    });

    it('should return invalid result with reason', () => {
      const mockResult: IsValidRootFolderResult = {
        isValid: false,
        invalidReason: 'Directory does not exist',
      };
      fileServiceMock.isValidRootFolder.mockReturnValue(mockResult);

      const result = npkill.isValidRootFolder(mockPath);

      expect(result).toEqual(mockResult);
    });
  });

  describe('getVersion', () => {
    it('should return version from package.json', () => {
      // This is mocked in beforeEach, so it should return '1.0.0'
      const version = npkill.getVersion();
      expect(typeof version).toBe('string');
      expect(version.length).toBeGreaterThan(0);
    });
  });

  describe('logger getter', () => {
    it('should return the logger service', () => {
      expect(npkill.logger).toBe(loggerMock);
    });
  });

  describe('error handling and edge cases', () => {
    it('should handle empty scan results', (done) => {
      fileServiceMock.listDir.mockReturnValue(of(''));

      const results: ScanFoundFolder[] = [];
      npkill.startScan$('/test', { targets: ['node_modules'] }).subscribe({
        next: (result) => results.push(result),
        complete: () => {
          expect(results).toHaveLength(0);
          done();
        },
      });
    });

    it('should handle scan with minimal options', (done) => {
      fileServiceMock.listDir.mockReturnValue(of('folder1'));

      npkill.startScan$('/test', { targets: ['node_modules'] }).subscribe({
        next: (result) => {
          expect(result.path).toBe('folder1');
          done();
        },
      });
    });

    it('should handle size calculation errors gracefully', (done) => {
      fileServiceMock.getFolderSize.mockReturnValue(
        throwError(() => new Error('Access denied')),
      );

      npkill.getSize$('/test').subscribe({
        error: (error) => {
          expect(error).toBeInstanceOf(Error);
          done();
        },
      });
    });

    it('should handle newest file calculation errors', (done) => {
      fileServiceMock.getRecentModificationInDir.mockRejectedValue(
        new Error('Access denied'),
      );

      npkill.getNewestFile$('/test').subscribe({
        error: (error) => {
          expect(error).toBeInstanceOf(Error);
          done();
        },
      });
    });

    it('should handle deletion errors', (done) => {
      fileServiceMock.deleteDir.mockRejectedValue(
        new Error('Permission denied'),
      );

      npkill.delete$('/test').subscribe({
        error: (error) => {
          expect(error).toBeInstanceOf(Error);
          done();
        },
      });
    });
  });

  describe('API contract validation', () => {
    it('should maintain consistent return types for startScan$', () => {
      fileServiceMock.listDir.mockReturnValue(of('test'));

      const observable = npkill.startScan$('/test', {
        targets: ['node_modules'],
      });
      expect(observable).toBeDefined();

      observable.subscribe((result) => {
        expect(result).toHaveProperty('path');
        expect(typeof result.path).toBe('string');
        // riskAnalysis is optional
        if (result.riskAnalysis) {
          expect(result.riskAnalysis).toHaveProperty('isSensitive');
          expect(typeof result.riskAnalysis.isSensitive).toBe('boolean');
        }
      });
    });

    it('should maintain consistent return types for getSize$', () => {
      fileServiceMock.getFolderSize.mockReturnValue(of(1024));

      const observable = npkill.getSize$('/test');
      expect(observable).toBeDefined();

      observable.subscribe((result) => {
        expect(result).toHaveProperty('size');
        expect(result).toHaveProperty('unit');
        expect(typeof result.size).toBe('number');
        expect(result.unit).toBe('bytes');
      });
    });

    it('should maintain consistent return types for delete$', () => {
      fileServiceMock.deleteDir.mockResolvedValue(true);

      const observable = npkill.delete$('/test');
      expect(observable).toBeDefined();

      observable.subscribe((result) => {
        expect(result).toHaveProperty('path');
        expect(result).toHaveProperty('success');
        expect(typeof result.path).toBe('string');
        expect(typeof result.success).toBe('boolean');
      });
    });
  });
});
```

## File: `tests/core/services/config.service.test.ts`
```typescript
import { ConfigService } from '../../../src/core/services/config.service.js';
import { INpkillrcConfig } from '../../../src/core/interfaces/npkillrc-config.interface.js';
import { existsSync, mkdirSync, writeFileSync, rmSync, realpathSync } from 'fs';
import { join } from 'path';
import { tmpdir } from 'os';

describe('ConfigService', () => {
  let configService: ConfigService;
  let tempDir: string;
  let originalCwd: string;

  beforeEach(() => {
    configService = new ConfigService();
    tempDir = join(tmpdir(), `npkill-test-${Date.now()}`);
    originalCwd = process.cwd();

    // Create test directory
    if (!existsSync(tempDir)) {
      mkdirSync(tempDir, { recursive: true });
    }
  });

  afterEach(() => {
    // Restore original working directory
    process.chdir(originalCwd);

    // Clean up temp directory
    if (existsSync(tempDir)) {
      rmSync(tempDir, { recursive: true, force: true });
    }
  });

  describe('loadConfig', () => {
    it('should return null config when file does not exist', () => {
      const result = configService.loadConfig('/non/existent/path/.npkillrc');

      expect(result.config).toBeNull();
      expect(result.error).toBeDefined();
      expect(result.error).toContain('Custom config file not found');
    });

    it('should load valid configuration file', () => {
      const configPath = join(tempDir, '.npkillrc');
      const validConfig: INpkillrcConfig = {
        exclude: ['.git', 'important'],
        sortBy: 'size',
      };

      writeFileSync(configPath, JSON.stringify(validConfig, null, 2));

      const result = configService.loadConfig(configPath);

      expect(result.config).not.toBeNull();
      expect(result.error).toBeUndefined();
      expect(result.config?.exclude).toEqual(['.git', 'important']);
      expect(result.config?.sortBy).toBe('size');
    });

    it('should return error for invalid JSON', () => {
      const configPath = join(tempDir, '.npkillrc');
      writeFileSync(configPath, '{ invalid json }');

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toBeDefined();
      expect(result.error).toContain('Failed to parse');
    });

    it('should validate sortBy values', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        sortBy: 'invalid-sort',
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('sortBy must be one of');
    });

    it('should reject unknown properties', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        unknownProp: 'value',
        anotherBadProp: 123,
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('Unknown configuration');
      expect(result.error).toContain('unknownProp');
      expect(result.error).toContain('anotherBadProp');
    });

    it('should validate boolean fields', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        dryRun: 'not-a-boolean',
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('dryRun must be a boolean');
    });

    it('should load and validate custom profiles', () => {
      const configPath = join(tempDir, '.npkillrc');
      const validConfig: INpkillrcConfig = {
        profiles: {
          webdev: {
            description: 'Web development',
            targets: ['node_modules', 'dist', '.next'],
          },
          python: {
            description: 'Python development',
            targets: ['.venv', '__pycache__'],
          },
        },
      };

      writeFileSync(configPath, JSON.stringify(validConfig, null, 2));

      const result = configService.loadConfig(configPath);

      expect(result.config).not.toBeNull();
      expect(result.config?.profiles).toBeDefined();
      expect(Object.keys(result.config?.profiles || {}).length).toBe(2);
      expect(result.config?.profiles?.webdev).toBeDefined();
      expect(result.config?.profiles?.webdev?.targets).toEqual([
        'node_modules',
        'dist',
        '.next',
      ]);
    });

    it('should reject profiles without targets', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        profiles: {
          webdev: {
            description: 'Test',
          },
        },
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('must have a targets property');
    });

    it('should reject profiles with empty targets array', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        profiles: {
          webdev: {
            description: 'Test',
            targets: [],
          },
        },
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('targets array cannot be empty');
    });

    it('should validate rootDir as string', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        rootDir: 123,
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('rootDir must be a string');
    });

    it('should reject empty rootDir string', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        rootDir: '   ',
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('rootDir cannot be an empty string');
    });

    it('should load valid rootDir', () => {
      const configPath = join(tempDir, '.npkillrc');
      const validConfig: INpkillrcConfig = {
        rootDir: '/home/user/projects',
      };

      writeFileSync(configPath, JSON.stringify(validConfig, null, 2));

      const result = configService.loadConfig(configPath);

      expect(result.config).not.toBeNull();
      expect(result.error).toBeUndefined();
      expect(result.config?.rootDir).toBe('/home/user/projects');
    });

    it('should validate defaultProfiles as array', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        defaultProfiles: 'not-an-array',
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain('defaultProfiles must be an array');
    });

    it('should validate defaultProfiles array contains only strings', () => {
      const configPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        defaultProfiles: ['node', 123, 'python'],
      };

      writeFileSync(configPath, JSON.stringify(invalidConfig));

      const result = configService.loadConfig(configPath);

      expect(result.config).toBeNull();
      expect(result.error).toContain(
        'All defaultProfiles items must be strings',
      );
    });

    it('should load valid defaultProfiles', () => {
      const configPath = join(tempDir, '.npkillrc');
      const validConfig: INpkillrcConfig = {
        defaultProfiles: ['node', 'python', 'webdev'],
      };

      writeFileSync(configPath, JSON.stringify(validConfig, null, 2));

      const result = configService.loadConfig(configPath);

      expect(result.config).not.toBeNull();
      expect(result.error).toBeUndefined();
      expect(result.config?.defaultProfiles).toEqual([
        'node',
        'python',
        'webdev',
      ]);
    });
  });

  describe('getUserDefinedProfiles', () => {
    it('should return empty object when config is null', () => {
      const profiles = configService.getUserDefinedProfiles(null);

      expect(profiles).toEqual({});
    });

    it('should return empty object when profiles is undefined', () => {
      const config: INpkillrcConfig = {
        exclude: ['.git'],
      };

      const profiles = configService.getUserDefinedProfiles(config);

      expect(profiles).toEqual({});
    });

    it('should extract user profiles correctly', () => {
      const config: INpkillrcConfig = {
        profiles: {
          webdev: {
            description: 'Web development',
            targets: ['node_modules', 'dist'],
          },
          python: {
            description: 'Python development',
            targets: ['.venv', '__pycache__'],
          },
        },
      };

      const profiles = configService.getUserDefinedProfiles(config);

      expect(Object.keys(profiles).length).toBe(2);
      expect(profiles.webdev).toEqual({
        description: 'Web development',
        targets: ['node_modules', 'dist'],
      });
      expect(profiles.python).toEqual({
        description: 'Python development',
        targets: ['.venv', '__pycache__'],
      });
    });
  });

  describe('mergeConfigs', () => {
    it('should return base config when file config is null', () => {
      const baseConfig = {
        exclude: ['.git'],
        sortBy: 'none',
      };

      const merged = configService.mergeConfigs(baseConfig, null);

      expect(merged).toEqual(baseConfig);
    });

    it('should merge sortBy from file config', () => {
      const baseConfig = {
        sortBy: 'none' as const,
      };
      const fileConfig: INpkillrcConfig = {
        sortBy: 'size',
      };

      const merged = configService.mergeConfigs(baseConfig, fileConfig);

      expect(merged.sortBy).toBe('size');
    });

    it('should merge exclude arrays without duplicates', () => {
      const baseConfig = {
        exclude: ['.git'],
      };
      const fileConfig: INpkillrcConfig = {
        exclude: ['node_modules', '.git'],
      };

      const merged = configService.mergeConfigs(baseConfig, fileConfig);

      expect(merged.exclude).toContain('.git');
      expect(merged.exclude).toContain('node_modules');
      expect(merged.exclude?.length).toBe(2);
    });

    it('should override simple properties', () => {
      const baseConfig = {
        sortBy: 'none',
        sizeUnit: 'auto',
        dryRun: false,
      };
      const fileConfig: INpkillrcConfig = {
        sortBy: 'size',
        sizeUnit: 'mb',
        dryRun: true,
      };

      const merged = configService.mergeConfigs(baseConfig, fileConfig);

      expect(merged.sortBy).toBe('size');
      expect(merged.sizeUnit).toBe('mb');
      expect(merged.dryRun).toBe(true);
    });

    it('should preserve base config properties not in file config', () => {
      const baseConfig = {
        sortBy: 'none',
        dryRun: false,
      };
      const fileConfig: INpkillrcConfig = {
        sortBy: 'size',
      };

      const merged = configService.mergeConfigs(baseConfig, fileConfig);

      expect(merged.sortBy).toBe('size');
      expect(merged.dryRun).toBe(false);
    });

    it('should merge rootDir from file config', () => {
      const baseConfig = {
        folderRoot: '/default/path',
        rootDir: undefined as string | undefined,
      };
      const fileConfig: INpkillrcConfig = {
        rootDir: '/custom/projects',
      };

      const merged = configService.mergeConfigs(baseConfig, fileConfig);

      expect(merged.rootDir).toBe('/custom/projects');
    });

    it('should merge defaultProfiles from file config', () => {
      const baseConfig = {
        defaultProfiles: ['node'],
      };
      const fileConfig: INpkillrcConfig = {
        defaultProfiles: ['node', 'python', 'webdev'],
      };

      const merged = configService.mergeConfigs(baseConfig, fileConfig);

      expect(merged.defaultProfiles).toEqual(['node', 'python', 'webdev']);
    });
  });

  describe('integration tests', () => {
    it('should load a complete realistic config file', () => {
      const configPath = join(tempDir, '.npkillrc');
      const realisticConfig: INpkillrcConfig = {
        rootDir: '/home/user/my-projects',
        exclude: ['.git', 'important-project'],
        sortBy: 'age',
        sizeUnit: 'auto',
        excludeSensitiveResults: false,
        dryRun: false,
        checkUpdates: true,
        defaultProfiles: ['node', 'python'],
        profiles: {
          frontend: {
            description: 'Frontend projects',
            targets: ['node_modules', 'dist', 'build'],
          },
          backend: {
            description: 'Backend projects',
            targets: ['node_modules', 'venv', 'target'],
          },
        },
      };

      writeFileSync(configPath, JSON.stringify(realisticConfig, null, 2));

      const result = configService.loadConfig(configPath);

      expect(result.config).not.toBeNull();
      expect(result.error).toBeUndefined();
      expect(result.config?.rootDir).toBe('/home/user/my-projects');
      expect(result.config?.defaultProfiles).toEqual(['node', 'python']);
      expect(result.config?.sortBy).toBe('age');
      expect(result.config?.profiles).toBeDefined();

      const userProfiles = configService.getUserDefinedProfiles(result.config);
      expect(Object.keys(userProfiles).length).toBe(2);
      expect(userProfiles.frontend).toBeDefined();
      expect(userProfiles.backend).toBeDefined();
    });
  });

  describe('config file resolution priority', () => {
    it('should prioritize custom path over cwd and home', () => {
      // Create configs in all locations
      const customPath = join(tempDir, 'custom.json');
      const cwdPath = join(tempDir, '.npkillrc');

      writeFileSync(customPath, JSON.stringify({ sortBy: 'size' }));
      writeFileSync(cwdPath, JSON.stringify({ sortBy: 'path' }));

      process.chdir(tempDir);

      const result = configService.loadConfig(customPath);

      expect(result.config).not.toBeNull();
      expect(result.config?.sortBy).toBe('size');
    });

    it('should use cwd config when no custom path provided and cwd config exists', () => {
      const cwdPath = join(tempDir, '.npkillrc');
      const cwdConfig: INpkillrcConfig = {
        sortBy: 'size',
        exclude: ['from-cwd'],
      };

      writeFileSync(cwdPath, JSON.stringify(cwdConfig, null, 2));
      process.chdir(tempDir);

      const result = configService.loadConfig();

      expect(result.config).not.toBeNull();
      expect(result.config?.sortBy).toBe('size');
      expect(result.config?.exclude).toContain('from-cwd');
      // Use realpathSync to resolve symlinks (e.g., /var -> /private/var on macOS)
      expect(realpathSync(result.configPath)).toBe(realpathSync(cwdPath));
    });

    it('should use home config when no custom path and no cwd config exists', () => {
      // NOTE: This test verifies the fallback to home directory by testing
      // that when cwd has no config, it falls back to the next priority.
      // We can't easily mock os.homedir() in ES modules, so we verify the
      // priority logic by ensuring cwd is checked first.

      const homeConfigPath = join(tempDir, 'simulated-home', '.npkillrc');
      const homeConfig: INpkillrcConfig = {
        sortBy: 'age',
        exclude: ['from-home'],
      };

      // Create the simulated home directory
      mkdirSync(join(tempDir, 'simulated-home'), { recursive: true });

      // Change to a directory without .npkillrc
      process.chdir(tempDir);

      // Create a config file and load it explicitly to verify it works
      writeFileSync(homeConfigPath, JSON.stringify(homeConfig, null, 2));
      const result = configService.loadConfig(homeConfigPath);

      expect(result.config).not.toBeNull();
      expect(result.config?.sortBy).toBe('age');
      expect(result.config?.exclude).toContain('from-home');
      expect(result.configPath).toBe(homeConfigPath);
    });

    it('should prioritize cwd over home when both exist', () => {
      const cwdPath = join(tempDir, '.npkillrc');
      const cwdConfig: INpkillrcConfig = {
        sortBy: 'size',
        exclude: ['from-cwd'],
      };

      writeFileSync(cwdPath, JSON.stringify(cwdConfig, null, 2));
      process.chdir(tempDir);

      const result = configService.loadConfig();

      expect(result.config).not.toBeNull();
      expect(result.config?.sortBy).toBe('size');
      expect(result.config?.exclude).toContain('from-cwd');
      // Use realpathSync to resolve symlinks (e.g., /var -> /private/var on macOS)
      expect(realpathSync(result.configPath)).toBe(realpathSync(cwdPath));
    });

    it('should return null config when no config file exists anywhere', () => {
      // Change to temp directory with no config and provide non-existent custom path
      process.chdir(tempDir);

      // Use a non-existent custom path to avoid loading real home config
      const nonExistentPath = join(tempDir, 'non-existent', '.npkillrc');
      const result = configService.loadConfig(nonExistentPath);

      expect(result.config).toBeNull();
      expect(result.error).toBeDefined();
      expect(result.error).toContain('Custom config file not found');
    });

    it('should validate config regardless of which location it comes from', () => {
      const cwdPath = join(tempDir, '.npkillrc');
      const invalidConfig = {
        sortBy: 'invalid-value',
      };

      writeFileSync(cwdPath, JSON.stringify(invalidConfig));
      process.chdir(tempDir);

      const result = configService.loadConfig();

      expect(result.config).toBeNull();
      expect(result.error).toContain('sortBy must be one of');
    });

    it('should handle different profiles from different locations', () => {
      const cwdPath = join(tempDir, '.npkillrc');
      const cwdConfig: INpkillrcConfig = {
        defaultProfiles: ['node', 'webdev'],
        profiles: {
          webdev: {
            description: 'Web development from cwd',
            targets: ['dist', '.next'],
          },
        },
      };

      writeFileSync(cwdPath, JSON.stringify(cwdConfig, null, 2));
      process.chdir(tempDir);

      const result = configService.loadConfig();

      expect(result.config).not.toBeNull();
      expect(result.config?.defaultProfiles).toEqual(['node', 'webdev']);
      expect(result.config?.profiles?.webdev?.description).toBe(
        'Web development from cwd',
      );
    });
  });
});
```

## File: `tests/core/services/logger.service.test.ts`
```typescript
import { jest } from '@jest/globals';
import { normalize } from 'path';

const writeFileSyncMock = jest.fn();
const renameFileSyncMock = jest.fn();
const existsSyncMock = jest.fn();
jest.unstable_mockModule('fs', () => {
  return {
    writeFileSync: writeFileSyncMock,
    existsSync: existsSyncMock,
    renameSync: renameFileSyncMock,
    default: jest.fn(),
  };
});

const osTmpPath = '/tmpDir';
jest.unstable_mockModule('os', () => {
  return {
    tmpdir: () => osTmpPath,
  };
});

const LoggerServiceConstructor = (
  await import('../../../src/core/services/logger.service.js')
).LoggerService;
class LoggerService extends LoggerServiceConstructor {}

describe('LoggerService', () => {
  let logger: LoggerService;
  const fakeTime = new Date('2026-01-01');
  const fakeTimeEpox = fakeTime.getTime();

  beforeEach(() => {
    logger = new LoggerService();
    jest.useFakeTimers().setSystemTime(fakeTime);
  });

  describe('add to log (info, error)', () => {
    it('should add the message to the log with the correct type and timestamp', () => {
      expect(logger.get()).toEqual([]);
      logger.info('Sample message1');
      logger.error('Sample message2');
      logger.error('Sample message3');
      logger.info('Sample message4');
      expect(logger.get()).toEqual([
        {
          type: 'info',
          timestamp: fakeTimeEpox,
          message: 'Sample message1',
        },
        {
          type: 'error',
          timestamp: fakeTimeEpox,
          message: 'Sample message2',
        },
        {
          type: 'error',
          timestamp: fakeTimeEpox,
          message: 'Sample message3',
        },
        {
          type: 'info',
          timestamp: fakeTimeEpox,
          message: 'Sample message4',
        },
      ]);
    });
  });

  describe('get', () => {
    it('should get "all" logs (by default or explicit)', () => {
      expect(logger.get()).toEqual([]);
      logger.info('');
      logger.error('');
      logger.info('');

      const expected = ['info', 'error', 'info'];

      expect(logger.get().map((entry) => entry.type)).toEqual(expected);
      expect(logger.get('all').map((entry) => entry.type)).toEqual(expected);
    });

    it('should get "info" logs', () => {
      logger.info('');
      logger.error('');
      logger.info('');

      const expected = ['info', 'info'];

      expect(logger.get('info').map((entry) => entry.type)).toEqual(expected);
    });

    it('should get "error" logs', () => {
      logger.info('');
      logger.error('');
      logger.info('');

      const expected = ['error'];

      expect(logger.get('error').map((entry) => entry.type)).toEqual(expected);
    });
  });

  describe('getSuggestLogfilePath', () => {
    it('the path should includes the os tmp dir', () => {
      const path = logger.getSuggestLogFilePath();
      expect(path.includes(normalize('/tmpDir'))).toBeTruthy();
    });
  });

  describe('LogFile rotation', () => {
    it('should not rotate file if not exist', () => {
      existsSyncMock.mockReturnValue(false);
      const path = logger.getSuggestLogFilePath();
      logger.saveToFile(path);
      expect(renameFileSyncMock).not.toHaveBeenCalled();
    });

    it('should rotate file if exist', () => {
      existsSyncMock.mockReturnValue(true);
      const path = logger.getSuggestLogFilePath();
      logger.saveToFile(path);
      const expectedOldPath = path.replace('latest', 'old');
      expect(renameFileSyncMock).toHaveBeenCalledWith(path, expectedOldPath);
    });
  });

  describe('saveToFile', () => {
    it('shoul write the content of the log to a given file', () => {
      const path = '/tmp/npkill-log.log';
      logger.info('hello');
      logger.error('bye');
      logger.info('world');
      const expected =
        '[1767225600000](info) hello\n' +
        '[1767225600000](error) bye\n' +
        '[1767225600000](info) world\n';

      logger.saveToFile(path);
      expect(writeFileSyncMock).toHaveBeenCalledWith(path, expected);
    });
  });
});
```

## File: `tests/core/services/files/files.service.test.ts`
```typescript
import { jest } from '@jest/globals';

import { IFileService } from '../../../../src/core/interfaces/file-service.interface.js';
import * as rimraf from 'rimraf';

let statSyncReturnMock = (): { isDirectory: () => boolean } | null => null;
let accessSyncReturnMock = (): boolean | null => null;
const readFileSyncSpy = jest.fn();
jest.unstable_mockModule('fs', () => {
  return {
    statSync: () => statSyncReturnMock(),
    accessSync: () => accessSyncReturnMock(),
    readFileSync: readFileSyncSpy,
    lstat: jest.fn(),
    readdir: jest.fn(),
    rmdir: jest.fn(),
    unlink: jest.fn(),
    rm: jest.fn(),
    default: { constants: { R_OK: 4 } },
  };
});

jest.useFakeTimers();

const FileServiceConstructor = (
  await import('../../../../src/core/services/files/files.service.js')
).FileService;
abstract class FileService extends FileServiceConstructor {}

const UnixFilesServiceConstructor = (
  await import('../../../../src/core/services/files/unix-files.service.js')
).UnixFilesService;
class UnixFilesService extends UnixFilesServiceConstructor {}

const WindowsFilesServiceConstructor = (
  await import('../../../../src/core/services/files/windows-files.service.js')
).WindowsFilesService;
class WindowsFilesService extends WindowsFilesServiceConstructor {}

import { existsSync, mkdirSync, readdirSync, writeFileSync } from 'fs';
import { StreamService } from '../../../../src/core/services/stream.service.js';
import { FileWorkerService } from '../../../../src/core/services/files/index.js';
import os from 'os';

jest.mock('../../../../src/dirname.js', () => {
  return { __esModule: true };
});

const fileWorkerService = jest.fn();

describe('File Service', () => {
  let fileService: FileService;

  beforeEach(() => {
    fileService = new UnixFilesService(
      new StreamService(),
      fileWorkerService as unknown as FileWorkerService,
    );
  });

  describe('isValidRootFolder', () => {
    const path = '/sample/path';

    afterEach(() => {
      jest.restoreAllMocks();
      statSyncReturnMock = () => null;
      statSyncReturnMock = () => null;
    });

    it('should throw error if statSync fail', () => {
      statSyncReturnMock = () => {
        throw new Error('ENOENT');
      };
      expect(fileService.isValidRootFolder(path)).toEqual({
        isValid: false,
        invalidReason: 'The path does not exist.',
      });
    });

    it('should throw error if is not directory', () => {
      statSyncReturnMock = () => ({
        isDirectory: () => false,
      });

      expect(fileService.isValidRootFolder(path)).toEqual({
        isValid: false,
        invalidReason: 'The path must point to a directory.',
      });
    });

    it('should throw error if cant read dir', () => {
      statSyncReturnMock = () => ({
        isDirectory: () => true,
      });
      accessSyncReturnMock = () => {
        throw new Error();
      };

      expect(fileService.isValidRootFolder(path)).toEqual({
        isValid: false,
        invalidReason: 'Cannot read the specified path.',
      });
    });

    it('should return true if is valid rootfolder', () => {
      statSyncReturnMock = () => ({
        isDirectory: () => true,
      });
      accessSyncReturnMock = () => true;

      expect(fileService.isValidRootFolder(path)).toBeTruthy();
    });
  });

  describe('isDangerous', () => {
    const originalEnv = { ...process.env };

    const mockCwd = (cwd: string) => {
      jest.spyOn(process, 'cwd').mockReturnValue(cwd);
    };

    const mockHomedir = (homedir: string) => {
      jest.spyOn(os, 'homedir').mockReturnValue(homedir);
    };

    afterAll(() => {
      process.env = originalEnv;
      jest.restoreAllMocks();
    });

    describe('POSIX paths', () => {
      beforeAll(() => {
        process.env.HOME = '/home/user';
        delete process.env.USERPROFILE;
        mockHomedir('/home/user');
      });

      test('safe relative path', () => {
        mockCwd('/safe/path');
        expect(
          fileService.isDangerous('../project/node_modules').isSensitive,
        ).toBe(false);
      });

      test('hidden relative path', () => {
        mockCwd('/home/user/projects');
        expect(fileService.isDangerous('../.config/secret').isSensitive).toBe(
          true,
        );
      });

      test('node_modules in ~/.cache', () => {
        expect(
          fileService.isDangerous('/home/user/.cache/project/node_modules')
            .isSensitive,
        ).toBe(true);
      });

      test('~/.cache itself', () => {
        expect(fileService.isDangerous('/home/user/.cache').isSensitive).toBe(
          true,
        );
      });

      test('~/.npm itself', () => {
        expect(fileService.isDangerous('/home/user/.npm').isSensitive).toBe(
          false,
        );
      });

      test('parent relative path (..)', () => {
        mockCwd('/home/user');
        expect(fileService.isDangerous('..').isSensitive).toBe(false);
      });

      test('current relative path (.)', () => {
        mockCwd('/home/user');
        expect(fileService.isDangerous('.').isSensitive).toBe(false);
      });

      test('hidden file in home path', () => {
        mockCwd('/home/user');
        expect(fileService.isDangerous('.hidden').isSensitive).toBe(true);
      });

      test('hidden file in not home path', () => {
        mockCwd('/home/user/project/projecta');
        expect(fileService.isDangerous('.hello').isSensitive).toBe(false);
      });
    });

    describe('Windows paths', () => {
      beforeAll(() => {
        process.env.USERPROFILE = 'C:\\Users\\user';
        process.env.HOME = '';
        mockHomedir('C:\\Users\\user');
      });

      test('safe relative path', () => {
        mockCwd('D:\\safe\\path');
        expect(
          fileService.isDangerous('..\\project\\node_modules').isSensitive,
        ).toBe(false);
      });

      test('AppData relative path', () => {
        mockCwd('C:\\Users\\user\\Documents');
        expect(
          fileService.isDangerous('..\\AppData\\Roaming\\app').isSensitive,
        ).toBe(true);
      });

      test('Program Files (x86)', () => {
        expect(
          fileService.isDangerous('C:\\Program Files (x86)\\app\\node_modules')
            .isSensitive,
        ).toBe(true);
      });

      test('network paths', () => {
        expect(
          fileService.isDangerous('\\\\network\\share\\.hidden\\node_modules')
            .isSensitive,
        ).toBe(true);
      });
    });

    describe('Edge cases', () => {
      test('no home directory', () => {
        delete process.env.HOME;
        delete process.env.USERPROFILE;
        mockHomedir('');
        expect(fileService.isDangerous('/some/path').isSensitive).toBe(false);
      });

      test('whitelisted hidden segments', () => {
        expect(
          fileService.isDangerous('/tmp/.cache/project/node_modules')
            .isSensitive,
        ).toBe(false);
        expect(
          fileService.isDangerous('/tmp/.npm/project/node_modules').isSensitive,
        ).toBe(false);
      });

      test('macOS application bundle', () => {
        expect(
          fileService.isDangerous(
            '/Applications/MyApp.app/Contents/node_modules',
          ).isSensitive,
        ).toBe(true);
      });

      test('Windows-style path on POSIX', () => {
        process.env.HOME = '/home/user';
        expect(
          fileService.isDangerous('/home/user/AppData/Local/.cache')
            .isSensitive,
        ).toBe(false);
      });
    });
  });

  xdescribe('Functional test for #deleteDir', () => {
    let fileService: IFileService;
    const testFolder = 'test-files';
    const directories = [
      'testProject',
      'awesome-fake-project',
      'a',
      'ewez',
      'potato and bananas',
    ];

    const createDir = (dir) => mkdirSync(dir);
    const isDirEmpty = (dir) => readdirSync(dir).length === 0;
    const createFileWithSize = (filename, mb) =>
      writeFileSync(filename, new Uint8Array(1024 * 1024 * mb));

    beforeAll(() => {
      const getOS = () => process.platform;
      const OSService = {
        linux: UnixFilesService,
        darwin: UnixFilesService,
        win32: WindowsFilesService,
      };
      const streamService: StreamService = new StreamService();
      fileService = new OSService[getOS()](streamService);

      if (existsSync(testFolder)) {
        rimraf.sync(testFolder);
      }
      createDir(testFolder);

      directories.forEach((dirName) => {
        const basePath = `${testFolder}/${dirName}`;
        const targetFolder = `${basePath}/node_modules`;
        const subfolder = `${targetFolder}/sample subfolder`;
        createDir(basePath);
        createDir(targetFolder);
        createDir(subfolder);
        createFileWithSize(targetFolder + '/a', 30);
        createFileWithSize(subfolder + '/sample file', 12);
        // Create this structure:
        //   test-files
        //    |testProject
        //      |a (file)
        //      |sample subfolder
        //       |sample file (file)
        //    |etc...
      });
    });

    afterAll(() => {
      rimraf.sync(testFolder);
    });

    it('Test folder should not be empty', () => {
      expect(isDirEmpty(testFolder)).toBeFalsy();
    });

    it('Should delete all folders created in test folder', async () => {
      for (const dirName of directories) {
        const path = `${testFolder}/${dirName}`;
        expect(existsSync(path)).toBeTruthy();
        await fileService.deleteDir(path);
        expect(existsSync(path)).toBeFalsy();
      }
      expect(isDirEmpty(testFolder)).toBeTruthy();
    });
  });

  describe('fakeDeleteDir', () => {
    it('Should return a Promise', () => {
      const result = fileService.fakeDeleteDir();
      expect(result).toBeInstanceOf(Promise);
    });
  });
});
```

## File: `tests/core/services/files/files.worker.service.test.ts`
```typescript
import { jest } from '@jest/globals';
import EventEmitter from 'node:events';
import { Subject } from 'rxjs';
import { EVENTS } from '../../../../src/constants/workers.constants.js';
import {
  WorkerMessage,
  WorkerScanOptions,
} from '../../../../src/core/services/files/index.js';
import { LoggerService } from '../../../../src/core/services/logger.service.js';
import { ScanStatus } from '../../../../src/core/index.js';

const workerEmitter: EventEmitter = new EventEmitter();
const port1Emitter: EventEmitter = new EventEmitter();
const port2Emitter: EventEmitter = new EventEmitter();
const workerPostMessageMock = jest.fn();
const workerTerminateMock = jest
  .fn()
  .mockImplementation(() => new Promise(() => {}));
const messageChannelPort1Mock = jest.fn();
const messageChannelPort2Mock = jest.fn();

jest.unstable_mockModule('os', () => ({
  default: { cpus: jest.fn().mockReturnValue([0, 0]) },
}));

jest.unstable_mockModule('node:worker_threads', () => ({
  Worker: jest.fn(() => ({
    postMessage: workerPostMessageMock,
    on: (eventName: string, listener: (...args: unknown[]) => void) =>
      workerEmitter.on(eventName, listener),
    terminate: workerTerminateMock,
    removeAllListeners: jest.fn(),
  })),

  MessageChannel: jest.fn(() => ({
    port1: {
      postMessage: messageChannelPort1Mock,
      on: (eventName: string, listener: (...args: unknown[]) => void) =>
        port1Emitter.on(eventName, listener),
      removeAllListeners: jest.fn(),
    },
    port2: {
      postMessage: messageChannelPort2Mock,
      on: (eventName: string, listener: (...args: unknown[]) => void) =>
        port2Emitter.on(eventName, listener),
      removeAllListeners: jest.fn(),
    },
  })),
}));

const logger = {
  info: jest.fn(),
} as unknown as jest.Mocked<LoggerService>;

const FileWorkerServiceConstructor = (
  await import('../../../../src/core/services/files/files.worker.service.js')
).FileWorkerService;
class FileWorkerService extends FileWorkerServiceConstructor {}

xdescribe('FileWorkerService', () => {
  let fileWorkerService: FileWorkerService;
  let searchStatus: ScanStatus;
  let params: WorkerScanOptions;

  beforeEach(async () => {
    const aa = new URL('file:///dev/null'); // Any valid URL. Is not used
    jest.spyOn(global, 'URL').mockReturnValue(aa);

    searchStatus = new ScanStatus();
    fileWorkerService = new FileWorkerService(logger, searchStatus);
    params = {
      rootPath: '/sample/path',
      targets: ['node_modules'],
    };
  });

  afterEach(() => {
    jest.restoreAllMocks();
    workerEmitter.removeAllListeners();
    port1Emitter.removeAllListeners();
    port2Emitter.removeAllListeners();
  });

  describe('startScan', () => {
    let stream$: Subject<string>;

    beforeEach(() => {
      stream$ = new Subject<string>();
    });

    afterEach(() => {
      jest.restoreAllMocks();
    });

    it('should emit "explore" and parameters to the worker', () => {
      fileWorkerService.startScan(stream$, params);
      expect(messageChannelPort1Mock).toHaveBeenCalledWith({
        type: EVENTS.explore,
        value: { rootPath: params.rootPath },
      });
    });

    it('should emit result to the streams on "scanResult"', (done) => {
      fileWorkerService.startScan(stream$, params);
      const val1 = ['/sample/path1/node_modules'];
      const val2 = ['/sample/path2/node_modules', '/sample/path3/otherDir'];

      const result: string[] = [];
      stream$.subscribe((data) => {
        result.push(data);
        if (result.length === 3) {
          expect(result[0]).toBe(val1[0]);
          expect(result[1]).toBe(val2[0]);
          expect(result[2]).toBe(val2[1]);
          done();
        }
      });

      port1Emitter.emit('message', {
        type: EVENTS.scanResult,
        value: {
          workerId: 1,
          results: [{ path: val1[0], isTarget: true }],
          pending: 0,
        },
      } as WorkerMessage);
      port1Emitter.emit('message', {
        type: EVENTS.scanResult,
        value: {
          workerId: 2,
          results: [
            { path: val2[0], isTarget: true },
            { path: val2[1], isTarget: true },
          ],
          pending: 342,
        },
      });
    });

    it('should add a job on "scanResult" when folder is not a target', () => {
      fileWorkerService.startScan(stream$, params);
      const val = [
        '/path/1/valid',
        '/path/im/target',
        '/path/other/target',
        '/path/2/valid',
      ];

      port1Emitter.emit('message', {
        type: EVENTS.scanResult,
        value: {
          workerId: 1,
          results: [
            { path: val[0], isTarget: false },
            { path: val[1], isTarget: true },
            { path: val[2], isTarget: true },
            { path: val[3], isTarget: false },
          ],
          pending: 0,
        },
      } as WorkerMessage);

      expect(messageChannelPort1Mock).toHaveBeenCalledWith({
        type: EVENTS.explore,
        value: { path: val[0] },
      });

      expect(messageChannelPort1Mock).toHaveBeenCalledWith({
        type: EVENTS.explore,
        value: { path: val[3] },
      });

      expect(messageChannelPort1Mock).not.toHaveBeenCalledWith({
        type: EVENTS.explore,
        value: { path: val[2] },
      });
    });

    it('should update searchStatus workerStatus on "alive"', () => {
      fileWorkerService.startScan(stream$, params);
      port1Emitter.emit('message', {
        type: 'alive',
        value: null,
      });

      expect(searchStatus.workerStatus).toBe('scanning');
    });

    it('should complete the stream and change worker status when all works have 0 pending tasks', (done) => {
      fileWorkerService.startScan(stream$, params);
      stream$.subscribe({
        complete: () => {
          done();
        },
      });

      port1Emitter.emit('message', {
        type: EVENTS.scanResult,
        value: {
          workerId: 0,
          results: [],
          pending: 0,
        },
      });

      expect(searchStatus.workerStatus).toBe('finished');
    });

    it('should throw error on "error"', () => {
      expect(() => {
        fileWorkerService.startScan(stream$, params);
        workerEmitter.emit('error');
        expect(searchStatus.workerStatus).toBe('dead');
      }).toThrow();
    });

    it('should register worker exit on "exit"', () => {
      fileWorkerService.startScan(stream$, params);

      logger.info.mockReset();
      workerEmitter.emit('exit');
      expect(logger.info).toHaveBeenCalledTimes(1);
    });
  });
});

// describe('getSize', () => {
//   let stream$: Subject<string>;
//   const path = '/sample/file/path';

//   const mockRandom = (value: number) =>
//     jest.spyOn(global.Math, 'random').mockReturnValue(value);

//   beforeEach(() => {
//     stream$ = new Subject<string>();
//     workerPostMessageMock.mockClear();
//   });

//   it('should emit "start-explore" and parameters to the worker', () => {
//     const randomNumber = 0.12341234;
//     mockRandom(randomNumber);

//     fileWorkerService.getSize(stream$, path);
//     expect(workerPostMessageMock).toHaveBeenCalledWith({
//       type: 'start-getSize',
//       value: { path: path, id: randomNumber },
//     });
//   });

//   it('should received "job completed" with same id, emit to the stream and complete it', (done) => {
//     const randomNumber = 0.8832342;
//     const response = 42342;
//     mockRandom(randomNumber);

//     fileWorkerService.getSize(stream$, path);

//     let streamValues = [];
//     stream$.subscribe({
//       next: (data) => {
//         streamValues.push(data);
//       },
//       complete: () => {
//         expect(streamValues.length).toBe(1);
//         expect(streamValues[0]).toBe(response);
//         done();
//       },
//     });

//     eventEmitter.emit('message', {
//       type: `getsize-job-completed-${randomNumber}`,
//       value: response,
//     });
//   });
// });
```

## File: `tests/core/services/files/files.worker.test.ts`
```typescript
import { jest } from '@jest/globals';
import EventEmitter from 'node:events';
import { Dir } from 'node:fs';
import { join, normalize } from 'node:path';
import { MessageChannel, MessagePort } from 'node:worker_threads';

import { GLOBAL_IGNORE } from '../../../../src/core/constants/global-ignored.constants.js';
import { EVENTS } from '../../../../src/constants/workers.constants.js';
import { ScanOptions } from '../../../../src/core/index.js';

const parentEmitter: EventEmitter = new EventEmitter();
let tunnelEmitter: MessagePort;
const tunnelPostMock = jest.fn();

let dirEntriesMock: {
  name: string;
  isDirectory: () => void;
  isSymbolicLink: () => void;
}[] = [];
const basePath = '/home/user/';
const target = 'node_modules';

// const opendirPathMock = jest.fn();
// const opendirDirMock = jest.fn();
// class MockDir extends EventEmitter {
//   private entries: Dirent[];

//   constructor(entries: Dirent[]) {
//     super();
//     this.entries = entries;
//   }

//   read(): Promise<Dirent> {
//     return new Promise((resolve, reject) => {
//       if (this.entries.length === 0) {
//         this.emit('close');
//         resolve(null);
//       } else {
//         resolve(this.entries.shift());
//       }
//     });
//   }
// }

const mockDir = {
  read: () => {
    if (dirEntriesMock.length > 0) {
      return Promise.resolve(dirEntriesMock.shift());
    } else {
      return Promise.resolve(null);
    }
  },
  close: () => {},
} as unknown as Dir;

jest.unstable_mockModule('fs/promises', () => ({
  opendir: () => new Promise((resolve) => resolve(mockDir)),
  lstat: () =>
    Promise.resolve({
      blocks: 1,
      size: 100,
      isDirectory: () => false,
      isSymbolicLink: () => false,
    }),
  readdir: () => Promise.resolve([]),
}));

jest.unstable_mockModule('node:worker_threads', () => ({
  parentPort: {
    postMessage: tunnelPostMock,
    on: (eventName: string, listener: (...args: unknown[]) => void) =>
      parentEmitter.on(eventName, listener),
  },
}));

describe('FileWorker', () => {
  const setExploreConfig = (params: ScanOptions) => {
    tunnelEmitter.postMessage({
      type: EVENTS.exploreConfig,
      value: params,
    });
  };

  beforeEach(async () => {
    await import('../../../../src/core/services/files/files.worker.js');

    const { port1, port2 } = new MessageChannel();
    tunnelEmitter = port1;

    parentEmitter.emit('message', {
      type: EVENTS.startup,
      value: { channel: port2 },
    });
  });

  afterEach(() => {
    jest.resetModules();
    jest.restoreAllMocks();
    parentEmitter.removeAllListeners();
    if (tunnelEmitter && typeof tunnelEmitter.close === 'function') {
      tunnelEmitter.close();
    }
  });

  // it('should plant a listener over the passed MessagePort',()=>{})

  it('should return only sub-directories from given parent', (done) => {
    setExploreConfig({ targets: [target] });
    const subDirectories = [
      {
        name: 'file1.txt',
        isDirectory: () => false,
        isSymbolicLink: () => false,
      },
      {
        name: 'file2.txt',
        isDirectory: () => false,
        isSymbolicLink: () => false,
      },
      { name: 'dir1', isDirectory: () => true, isSymbolicLink: () => false },
      {
        name: 'file3.txt',
        isDirectory: () => false,
        isSymbolicLink: () => false,
      },
      { name: 'dir2', isDirectory: () => true, isSymbolicLink: () => false },
    ];

    const expectedResult = subDirectories
      .filter((subdir) => subdir.isDirectory())
      .map((subdir) => ({
        path: join(basePath, subdir.name),
        isTarget: false,
      }));

    dirEntriesMock = [...subDirectories];

    let results: unknown[];

    tunnelEmitter.on('message', (message) => {
      if (message.type === EVENTS.scanResult) {
        results = message.value.results;

        done();
        expect(results).toEqual(expectedResult);
      }
    });

    tunnelEmitter.postMessage({
      type: EVENTS.explore,
      value: { path: '/home/user/' },
    });
  });

  describe('should mark "isTarget" correctly', () => {
    const sampleTargets = ['node_modules', 'dist'];

    sampleTargets.forEach((target) => {
      it('when target is ' + target, (done) => {
        setExploreConfig({ targets: [target] });
        const subDirectories = [
          {
            name: 'file1.cs',
            isDirectory: () => false,
            isSymbolicLink: () => false,
          },
          {
            name: '.gitignore',
            isDirectory: () => false,
            isSymbolicLink: () => false,
          },
          {
            name: 'dir1',
            isDirectory: () => true,
            isSymbolicLink: () => false,
          },
          {
            name: 'node_modules',
            isDirectory: () => true,
            isSymbolicLink: () => false,
          },
          {
            name: 'file3.txt',
            isDirectory: () => false,
            isSymbolicLink: () => false,
          },
          {
            name: 'dir2',
            isDirectory: () => true,
            isSymbolicLink: () => false,
          },
        ];
        dirEntriesMock = [...subDirectories];

        const expectedResult = subDirectories
          .filter((subdir) => {
            if (!subdir.isDirectory()) {
              return false;
            }

            const isTarget = subdir.name === target;
            if (GLOBAL_IGNORE.has(subdir.name) && !isTarget) {
              return false;
            }

            return true;
          })
          .map((subdir) => ({
            path: join(basePath, subdir.name),
            isTarget: subdir.name === target,
          }));

        let results: unknown[];

        tunnelEmitter.on('message', (message) => {
          if (message.type === EVENTS.scanResult) {
            results = message.value.results;

            expect(results).toEqual(expectedResult);
            done();
          }
        });

        tunnelEmitter.postMessage({
          type: EVENTS.explore,
          value: { path: '/home/user/' },
        });
      });
    });
  });

  describe('should exclude dir', () => {
    it('when a simple patterns is gived', (done) => {
      const excluded = ['ignorethis', 'andignorethis'];
      setExploreConfig({
        targets: ['node_modules'],
        exclude: excluded,
      });
      const subDirectories = [
        {
          name: 'file1.cs',
          isDirectory: () => false,
          isSymbolicLink: () => false,
        },
        {
          name: '.gitignore',
          isDirectory: () => false,
          isSymbolicLink: () => false,
        },
        { name: 'dir1', isDirectory: () => true, isSymbolicLink: () => false },
        {
          name: 'node_modules',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: 'ignorethis',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: 'andignorethis',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        { name: 'dir2', isDirectory: () => true, isSymbolicLink: () => false },
      ];
      dirEntriesMock = [...subDirectories];

      const expectedResult = subDirectories
        .filter(
          (subdir) => subdir.isDirectory() && !excluded.includes(subdir.name),
        )
        .map((subdir) => ({
          path: join(basePath, subdir.name),
          isTarget: subdir.name === 'node_modules',
        }));

      let results: unknown[];
      tunnelEmitter.on('message', (message) => {
        if (message.type === EVENTS.scanResult) {
          results = message.value.results;

          done();
          expect(results).toEqual(expectedResult);
        }
      });

      tunnelEmitter.postMessage({
        type: EVENTS.explore,
        value: { path: '/home/user/' },
      });
    });

    it('when a part of path is gived', (done) => {
      const excluded = ['user/ignorethis'];
      setExploreConfig({
        targets: ['node_modules'],
        exclude: excluded.map(normalize),
      });
      const subDirectories = [
        {
          name: 'file1.cs',
          isDirectory: () => false,
          isSymbolicLink: () => false,
        },
        {
          name: '.gitignore',
          isDirectory: () => false,
          isSymbolicLink: () => false,
        },
        { name: 'dir1', isDirectory: () => true, isSymbolicLink: () => false },
        {
          name: 'node_modules',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: 'ignorethis',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: 'andNOTignorethis',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        { name: 'dir2', isDirectory: () => true, isSymbolicLink: () => false },
      ];
      dirEntriesMock = [...subDirectories];

      const expectedResult = subDirectories
        .filter(
          (subdir) => subdir.isDirectory() && subdir.name !== 'ignorethis',
        )
        .map((subdir) => ({
          path: join(basePath, subdir.name),
          isTarget: subdir.name === 'node_modules',
        }));

      let results: unknown[];
      tunnelEmitter.on('message', (message) => {
        if (message.type === EVENTS.scanResult) {
          results = message.value.results;

          done();
          expect(results).toEqual(expectedResult);
        }
      });

      tunnelEmitter.postMessage({
        type: EVENTS.explore,
        value: { path: '/home/user/' },
      });
    });
  });

  describe('should skip symbolic links', () => {
    it('should not return symlinked directories', (done) => {
      setExploreConfig({ targets: ['node_modules'] });
      const subDirectories = [
        {
          name: 'regular-dir',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: 'symlinked-dir',
          isDirectory: () => true,
          isSymbolicLink: () => true, // This should be skipped
        },
        {
          name: 'node_modules',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: 'another-symlink',
          isDirectory: () => true,
          isSymbolicLink: () => true, // This should be skipped
        },
        {
          name: 'another-regular-dir',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
      ];

      // Only non-symlinked directories should be in results
      const expectedResult = subDirectories
        .filter((subdir) => subdir.isDirectory() && !subdir.isSymbolicLink())
        .map((subdir) => ({
          path: join(basePath, subdir.name),
          isTarget: subdir.name === 'node_modules',
        }));

      dirEntriesMock = [...subDirectories];

      let results: unknown[];

      tunnelEmitter.on('message', (message) => {
        if (message.type === EVENTS.scanResult) {
          results = message.value.results;

          expect(results).toEqual(expectedResult);
          // Verify symlinks were filtered out
          expect(results).toHaveLength(3);
          const paths = (results as Array<{ path: string }>).map((r) => r.path);
          expect(paths.some((p) => p.includes('symlink'))).toBe(false);
          done();
        }
      });

      tunnelEmitter.postMessage({
        type: EVENTS.explore,
        value: { path: '/home/user/' },
      });
    });

    it('should skip symlinked files', (done) => {
      setExploreConfig({ targets: ['node_modules'] });
      const subDirectories = [
        {
          name: 'regular-file.txt',
          isDirectory: () => false,
          isSymbolicLink: () => false,
        },
        {
          name: 'symlinked-file.txt',
          isDirectory: () => false,
          isSymbolicLink: () => true, // This should be skipped
        },
        {
          name: 'regular-dir',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
      ];

      // Only regular directories should be in results (files are not included anyway)
      const expectedResult = [
        {
          path: join(basePath, 'regular-dir'),
          isTarget: false,
        },
      ];

      dirEntriesMock = [...subDirectories];

      let results: unknown[];

      tunnelEmitter.on('message', (message) => {
        if (message.type === EVENTS.scanResult) {
          results = message.value.results;

          expect(results).toEqual(expectedResult);
          expect(results).toHaveLength(1);
          done();
        }
      });

      tunnelEmitter.postMessage({
        type: EVENTS.explore,
        value: { path: '/home/user/' },
      });
    });

    it('should handle yarn/pnpm workspace symlinks', (done) => {
      setExploreConfig({ targets: ['node_modules'] });
      const subDirectories = [
        {
          name: 'node_modules',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
        {
          name: '@workspace-package', // Yarn workspace symlink
          isDirectory: () => true,
          isSymbolicLink: () => true,
        },
        {
          name: 'package-a', // pnpm symlink
          isDirectory: () => true,
          isSymbolicLink: () => true,
        },
        {
          name: 'src',
          isDirectory: () => true,
          isSymbolicLink: () => false,
        },
      ];

      // Only non-symlinked directories
      const expectedResult = [
        {
          path: join(basePath, 'node_modules'),
          isTarget: true,
        },
        {
          path: join(basePath, 'src'),
          isTarget: false,
        },
      ];

      dirEntriesMock = [...subDirectories];

      let results: unknown[];

      tunnelEmitter.on('message', (message) => {
        if (message.type === EVENTS.scanResult) {
          results = message.value.results;

          expect(results).toEqual(expectedResult);
          // Verify workspace symlinks were excluded
          expect(results).toHaveLength(2);
          const paths = (results as Array<{ path: string }>).map((r) => r.path);
          expect(paths.some((p) => p.includes('@workspace'))).toBe(false);
          expect(paths.some((p) => p.includes('package-a'))).toBe(false);
          done();
        }
      });

      tunnelEmitter.postMessage({
        type: EVENTS.explore,
        value: { path: '/home/user/' },
      });
    });
  });
});
```

## File: `tests/utils/utils.test.ts`
```typescript
import {
  convertBytesToKB,
  convertBytesToGb,
  convertGBToMB,
  formatSize,
} from '../../src/utils/unit-conversions.js';
import { isSafeToDelete } from '../../src/utils/is-safe-to-delete.js';

describe('unit-conversions', () => {
  it('#convertBytesToKB', () => {
    expect(convertBytesToKB(1)).toBe(0.0009765625);
    expect(convertBytesToKB(100)).toBe(0.09765625);
    expect(convertBytesToKB(96)).toBe(0.09375);
  });

  it('#convertGBToMB', () => {
    expect(convertGBToMB(1)).toBe(1024);
    expect(convertGBToMB(100)).toBe(102400);
    expect(convertGBToMB(96)).toBe(98304);
  });

  it('#convertBytesToGb', () => {
    expect(convertBytesToGb(1)).toBeCloseTo(1.0 / Math.pow(1024, 3), 10);
    expect(convertBytesToGb(100)).toBeCloseTo(100 / Math.pow(1024, 3), 10);
    expect(convertBytesToGb(96)).toBeCloseTo(96 / Math.pow(1024, 3), 10);
  });

  describe('#formatSize', () => {
    it('should format sizes in auto mode - small sizes in MB without decimals', () => {
      const result = formatSize(0.5, 'auto'); // 512 MB
      expect(result.unit).toBe('MB');
      expect(result.value).toBe(512);
      expect(result.text).toBe('512 MB');
    });

    it('should format sizes in auto mode - large sizes in GB with decimals', () => {
      const result = formatSize(1.5, 'auto');
      expect(result.unit).toBe('GB');
      expect(result.value).toBe(1.5);
      expect(result.text).toBe('1.50 GB');
    });

    it('should format sizes in MB mode without decimals', () => {
      const result = formatSize(1.5, 'mb'); // 1536 MB
      expect(result.unit).toBe('MB');
      expect(result.value).toBe(1536);
      expect(result.text).toBe('1536 MB');
    });

    it('should format sizes in GB mode with decimals', () => {
      const result = formatSize(0.5, 'gb');
      expect(result.unit).toBe('GB');
      expect(result.value).toBe(0.5);
      expect(result.text).toBe('0.50 GB');
    });

    it('should round MB values to nearest integer', () => {
      const result = formatSize(0.123, 'mb'); // ~126.29 MB
      expect(result.unit).toBe('MB');
      expect(result.text).toBe('126 MB');
    });

    it('should use custom decimals for GB', () => {
      const result = formatSize(1.2345, 'gb', 3);
      expect(result.text).toBe('1.234 GB');
    });

    it('should switch to GB in auto mode when size >= 1024 MB', () => {
      const result = formatSize(1, 'auto'); // exactly 1024 MB = 1 GB
      expect(result.unit).toBe('GB');
      expect(result.text).toBe('1.00 GB');
    });
  });
});

describe('is-safe-to-delete', () => {
  const target = ['node_modules'];

  it('should get false if not is safe to delete ', () => {
    expect(isSafeToDelete('/one/route', target)).toBeFalsy();
    expect(isSafeToDelete('/one/node_/ro/modules', target)).toBeFalsy();
    expect(isSafeToDelete('nodemodules', target)).toBeFalsy();
    expect(isSafeToDelete('/', target)).toBeFalsy();
    expect(isSafeToDelete('/home', target)).toBeFalsy();
    expect(isSafeToDelete('/home/user', target)).toBeFalsy();
    expect(isSafeToDelete('/home/user/.angular', target)).toBeFalsy();
    expect(
      isSafeToDelete('/home/user/.angular', [...target, 'angular']),
    ).toBeFalsy();
    expect(isSafeToDelete('/home/user/dIst', [...target, 'dist'])).toBeFalsy();
  });

  it('should get true if is safe to delete ', () => {
    expect(isSafeToDelete('/one/route/node_modules', target)).toBeTruthy();
    expect(isSafeToDelete('/one/route/node_modules/', target)).toBeTruthy();
    expect(
      isSafeToDelete('/home/user/.angular', [...target, '.angular']),
    ).toBeTruthy();
    expect(isSafeToDelete('/home/user/dIst', [...target, 'dIst'])).toBeTruthy();
  });
});
```

