---
id: killkimno-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.848340
---

# KNOWLEDGE EXTRACT: killkimno
> **Extracted on:** 2026-03-30 17:38:16
> **Source:** killkimno

---

## File: `MORT.md`
```markdown
# 📦 killkimno/MORT [🔖 PENDING/APPROVE]
🔗 https://github.com/killkimno/MORT
🌐 https://blog.naver.com/killkimno/70179867557

## Meta
- **Stars:** ⭐ 1457 | **Forks:** 🍴 80
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
MORT 번역기 프로젝트 - Real-time game translator with OCR

## README (trích đầu)
```
🌏[한국어](README.kr.md) | [English](../../../core/security/QUARANTINE/vetted/repos/tookie_osint/docs/readmelang/README.en.md)


[![GitHub downloads](https://img.shields.io/github/downloads/killkimno/MORT/total.svg?logo=github)](https://github.com/killkimno/MORT/releases)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y6DIUR2)

<img src="https://github.com/killkimno/MORT/blob/main/MORT_LOGO.png" width="90%"></img>


[![Video Label](https://img.youtube.com/vi/LHTErVnsaws/0.jpg)](https://youtu.be/LHTErVnsaws)

https://youtu.be/LHTErVnsaws

Sample video

# MORT #

MORT is a program that extracts dialogs from the screen in real time using OCR and outputs a translations using DB or machine translation.

Currently, English and Japanese translation/extraction can be extracted by default, and it can also be translated by linking with a hooking program using the save to clipboard function.

[Latest version download and release notes - https://blog.naver.com/killkimno/70179867557]

## Features ##
* Realtime translate
* OCR - TesseractOCR , Windows OCR, Google Cloud Vision OCR, Snipping Tool OCR, Easy OCR
* Machine translation - Naver Papago, Google Web, Google Sheet, ezTrans, DeepL
* Language Patch with using DB
* Multiple OCR areas
* Img adjust

## System Requirement ##
* Windows 10 or higer
* 64bit os
* .NET 9 or higer
  - https://dotnet.microsoft.com/ko-kr/download/dotnet/thank-you/runtime-desktop-9.0.4-windows-x64-installer
* Visual Studio 2022 Visual C++ (x64) - vcredist_x64.exe
  - https://aka.ms/vs/17/release/vc_redist.x64.exe


## How to use ##
#### Basic usage ####

1. After setting in the quick settings, press Trnaselate on the remote control to start translation
2. Or Preferences tab -> Set the OCR language according to the language of the game to be translated
3. Remote control -> Click Search and select the area where the lines appear
4. Click Apply on MORT main form
5. Remote control -> Real-time translation by pressing Translate

#### User Manual ####
* https://blog.naver.com/killkimno/221904784013

## Custom usage ##
#### Add translation result language code ####
You can add Google Translator language code in the UserData/UserTransCode.txt file​

```
code, name
(ex : it, Italian)
```

​A list of language codes can be found here: https://cloud.google.com/translate/docs/languages?hl=en

#### Custom API usage ####
1. You can use a custom API based on HTTP
2. Translation Type -> Custom API
3. Advanced Settings -> Custom API URL Settings
```
POST Rule
name - string
text - string - ocr string
target - string - translation result language code
source - string - ocr language code

ex
{
"name" : "test",
"text" : "tank divsion" ,
"target" : "ko",
"source" : "en"
...
}


Reponse Rule
result - string - translation result text
errorCode - string - error code
errorMessage - string - error message

ex
{
"result" : "탱크 사단",
"errorMessage" : "",
"errorCode" : "0"
}
```

4. Example1 - Using LibreTranslate
* Translator address to use as an example
  - https://github.com/LibreTranslate/LibreTranslate
* sample c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

