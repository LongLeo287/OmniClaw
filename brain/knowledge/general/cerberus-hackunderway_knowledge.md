---
id: cerberus-hackunderway-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.542758
---

# KNOWLEDGE EXTRACT: cerberus-hackunderway
> **Extracted on:** 2026-03-30 17:31:16
> **Source:** cerberus-hackunderway

---

## File: `.gitignore`
```
.env
*.jpg
__pycache__/
venv/
```

## File: `cerberus.py`
```python
import requests
import os
from colorama import Fore, Style, init

os.system("printf '\033]2;Cerberus v1.0 🕵🏽‍♂️\a'")

# Inicializar colorama
init(autoreset=True)

# Logo
print(Style.BRIGHT + Fore.YELLOW + r'''
                            /\_/\____,
                  ,___/\_/\ \  ~     /
                  \     ~  \ )   XXX
                    XXX     /    /\_/\___,
                       \o-o/-o-o/   ~    /
                        ) /     \    XXX
                       _|    / \ \_/
                    ,-/   _  \_/   \
                   / (   /____,__|  )
                  (  |_ (    )  \) _|
                 _/ _)   \   \__/   (_
                (,-(,(,(,/      \,),),)
''')
print(f"{' ' * 17}{Fore.WHITE}{Style.BRIGHT}Created by Hack Underway{Style.RESET_ALL}")

BASE_URL = "https://cvedb.shodan.io"

def fetch_cves(query):
    """Consulta la API de cvedb.shodan.io por producto o CVE puntual."""
    results = []
    query = query.strip()

    # Si es CVE-ID, buscar directamente
    if query.upper().startswith("CVE-"):
        url = f"{BASE_URL}/cve/{query.upper()}"
        response = requests.get(url)
        if response.status_code == 200:
            try:
                results.append(response.json())
            except ValueError:
                print(f"{Fore.RED}La respuesta del servidor no es JSON válido.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No se encontró información para {query}.{Style.RESET_ALL}")
    else:
        # Búsqueda por producto
        url = f"{BASE_URL}/cves?product={query}"
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, dict) and "cves" in data:
                    cve_list = data["cves"]
                    print(f"{Fore.LIGHTCYAN_EX}Se encontraron {len(cve_list)} CVEs para '{query}'. Mostrando los primeros 10...{Style.RESET_ALL}")
                    results.extend(cve_list[:10])  # Limita a los primeros 10
                else:
                    print(f"{Fore.RED}Formato de respuesta inesperado para '{query}'.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}No se pudo analizar la respuesta JSON para '{query}'.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Error al buscar vulnerabilidades para '{query}'. Código: {response.status_code}{Style.RESET_ALL}")

    return results

def display_cves(cves):
    """Muestra los CVEs obtenidos de forma formateada."""
    results_output = []

    if not cves:
        print(f"{Fore.YELLOW}No se encontraron vulnerabilidades.{Style.RESET_ALL}")
        return results_output

    for idx, cve in enumerate(cves, 1):
        print(f"{Fore.GREEN}--- CVE {idx} ---{Style.RESET_ALL}")
        cve_id = cve.get("id") or cve.get("cve_id", "N/A")
        description = cve.get("summary", "Sin descripción.")
        cvss = cve.get("cvss", "N/A")
        severity = cve.get("severity", "N/A")
        exploited = cve.get("exploit") == True
        references = cve.get("references", [])

        output = f"--- CVE {idx} ---\n"
        output += f"ID: {cve_id}\n"
        output += f"Descripción: {description}\n"
        output += f"CVSS: {cvss} | Severidad: {severity}\n"
        output += f"¿Explotado?: {'Sí' if exploited else 'No'}\n"
        output += "Referencias:\n"
        for ref in references:
            output += f" - {ref}\n"

        print(f"{Fore.CYAN}ID:{Style.RESET_ALL} {cve_id}")
        print(f"{Fore.CYAN}Descripción:{Style.RESET_ALL} {description}")
        print(f"{Fore.CYAN}CVSS:{Style.RESET_ALL} {cvss} | Severidad: {severity}")
        print(f"{Fore.CYAN}¿Explotado?:{Style.RESET_ALL} {'Sí' if exploited else 'No'}")
        print(f"{Fore.CYAN}Referencias:{Style.RESET_ALL}")
        for ref in references:
            print(f"{Fore.BLUE} - {ref}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}{'-'*60}{Style.RESET_ALL}")

        results_output.append(output + '-'*60 + '\n\n')

    return results_output

def save_results(results, query):
    """Guarda resultados en archivo TXT."""
    if not results:
        print(f"{Fore.YELLOW}No hay resultados para guardar.{Style.RESET_ALL}")
        return

    filename = f"cvedb_results_{query.replace(' ', '_')}_{os.urandom(3).hex()}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(results)

    print(f"{Fore.GREEN}Resultados guardados en {filename}{Style.RESET_ALL}")

def main():
    while True:
        query = input(f"\n{Fore.LIGHTBLUE_EX}Introduce un CVE o nombre de producto (ej. CVE-2024-12345, nginx): {Style.RESET_ALL}").strip()
        cves = fetch_cves(query)
        results = display_cves(cves)

        if results:
            choice = input(f"{Fore.YELLOW}¿Guardar resultados en archivo? (s/n): {Style.RESET_ALL}").lower()
            if choice == 's':
                save_results(results, query)

        again = input(f"{Fore.LIGHTBLUE_EX}¿Deseas hacer otra búsqueda? (s/n): {Style.RESET_ALL}").lower()
        if again != 's':
            print(f"{Fore.GREEN}¡Hasta luego!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
```

## File: `LICENSE`
```
MIT License

Copyright (c) [2025] [HackUnderway]

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

## File: `README.md`
```markdown
<h1 align="center">CERBERUS 👁</h1>

<p align="center">
  Herramienta de extracción de exploits desde <strong>Shodan Exploits</strong> para facilitar la búsqueda de vulnerabilidades conocidas.
</p>

<p align="center">
  <img src="assets/Demo_1.png" title="CERBERUS" alt="CERBERUS" width="600"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white" alt="Python version">
  <img src="https://img.shields.io/badge/Shodan-CVEDB-1e90ff" alt="Shodan CVEDB">
  <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative&logoColor=white" alt="License">
</p>

---

## 🚀 Características

- Búsqueda de exploits por palabra clave (ej. CVE-2024-XXXX, Laravel, WordPress, etc.).
- Extracción de resultados desde <strong>Shodan Exploits</strong>.
- Visualización clara con título, enlace, autor, etiquetas y contenido.
- Compatible con Python 3.

## 📌 Requisitos

- Python 3.8+

- Librerías: `requests`, `colorama`

## ⚠️ Advertencia de uso

- Esta herramienta ha sido creada únicamente con fines educativos y de investigación en seguridad.
- El uso indebido para actividades maliciosas es responsabilidad del usuario.

🔴 **No utilices esta herramienta para actividades ilegales.**

🟢 **El autor no se hace responsable del mal uso que otros puedan darle.**

---
## ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/HackUnderway/cerberus.git
```
```bash
cd cerberus
```
```bash
pip install -r requirements.txt
```

## 🐍 Uso básico 
##### Ejecuta el script:

python3 cerberus.py

- Se te pedirá un término de búsqueda. Ejemplo:

- CVE-2024-24919

- Laravel

<p align="center">
  <img src="assets/Demo_2.png" title="CERBERUS" alt="CERBERUS" width="600"/>
</p>

> **El proyecto está abierto a colaboradores.**


# DISTRIBUCIONES SOPORTADAS
|Distribución | Versión verificada | 	¿Soportado? | 	Estado |
|--------------|--------------------|------|-------|
|Kali Linux| 2025.2| si| funcionando   |
|Parrot Security OS| 6.3| si | funcionando   |
|Windows| 11 | si | funcionando   |
|BackBox| 9 | si | funcionando   |
|Arch Linux| 2024.12.01 | si | funcionando   |

# SOPORTE
Preguntas, errores o sugerencias: info@hackunderway.com

# LICENSE
- [x] Cerberus tiene licencia.
- [x] Consulta el archivo [LICENSE](https://github.com/HackUnderway/cerberus#MIT-1-ov-file) para más información.

# CYBERSECURITY RESEARCHER

* [Victor Bancayan](https://www.offsec.com/bug-bounty-program/) - (**CEO at [Hack Underway](https://hackunderway.com/)**) 

## 🔗 ENLACES
[![Patreon](https://img.shields.io/badge/patreon-000000?style=for-the-badge&logo=Patreon&logoColor=white)](https://www.patreon.com/c/HackUnderway)
[![Web site](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://hackunderway.com)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/HackUnderway)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@JeyZetaOficial)
[![Twitter/X](https://img.shields.io/badge/Twitter/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/JeyZetaOficial)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/hackunderway)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/JeyZeta)

## ☕️ Apoya el proyecto

Si te gusta esta herramienta, considera invitarme un café:

[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/hackunderway)

## Manual Shodan para Pentesters:
https://hackunderway.com/producto/shodan-para-pentesters/

## 🌞 Suscripciones

###### Suscríbete a: [Jey Zeta](https://www.facebook.com/JeyZetaOficial/subscribe/)

[![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)

from <img src="https://i.imgur.com/ngJCbSI.png" title="Perú"> made in <img src="https://i.imgur.com/NNfy2o6.png" title="Python"> with <img src="https://i.imgur.com/S86RzPA.png" title="Love"> by: <font color="red">Victor Bancayan</font>

© 2025
```

## File: `requirements.txt`
```
requests
colorama
```

## File: `_VET_REPORT.md`
```markdown
﻿# Strix Vet Report: cerberus-hackunderway
**Date:** 2026-03-17 10:09:30
**Status:** PASS
**Critical Findings:** 0
**Warnings:** 1

## Verdict

PASS - Repo passed all security checks. Safe to extract specific files into AI OS.

## Findings

| Level | Category | Detail | File |
|-------|----------|--------|------|
| PASS | GIT_HOOK | No active hooks found | `` |
| WARN | OBFUSCATION | os.system shell execution | `D:\Project\QUARANTINE\cerberus-hackunderway\cerberus.py` |


## Next Step

Proceed to content extraction. Copy only needed files into D:\APP\AI OS\knowledge\ or relevant skill folder.
```

