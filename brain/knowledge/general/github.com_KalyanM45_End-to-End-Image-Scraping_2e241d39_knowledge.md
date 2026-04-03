---
id: github.com-kalyanm45-end-to-end-image-scraping-2e2
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:17.572911
---

# KNOWLEDGE EXTRACT: github.com_KalyanM45_End-to-End-Image-Scraping_2e241d39
> **Extracted on:** 2026-04-01 13:58:08
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523571/github.com_KalyanM45_End-to-End-Image-Scraping_2e241d39

---

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
imagescraperenv
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## File: `Image Scraper.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "264983bc-65f3-4e09-b18e-2163a0037ce8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import logging\n",
    "import os\n",
    "\n",
    "from bs4 import BeautifulSoup  #to scrap data from html/xml pages - content\n",
    "from urllib.request import urlopen  #for requesting the server"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "15e0a06f-9fce-45e0-8ffc-a79615d312e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "save_dir = \"images/\"\n",
    "\n",
    "#creating the Images directory if it is doesnt exists.\n",
    "if  not os.path.exists(save_dir):\n",
    "    os.makedirs(save_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e0cd73b9-7def-4657-a28b-fca9d32061b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "query = \"ISRO\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "6f24e090-a289-40c0-97d2-46e49b5b3b22",
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(f\"https://www.google.com/search?q={query}&tbm=isch&ved=2ahUKEwizs9SKyLqAAxV2yaACHafeCUoQ2-cCegQIABAA&oq=elon+musk&gs_lcp=CgNpbWcQAzIKCAAQigUQsQMQQzIKCAAQigUQsQMQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEOgQIIxAnOgsIABCABBCxAxCDAToNCAAQigUQsQMQgwEQQzoECAAQAzoHCAAQigUQQzoHCCMQ6gIQJzoICAAQsQMQgwFQ3ARYwRlg3CFoAXAAeAKAAYMBiAHdC5IBBDAuMTOYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=-oHIZLPOMPaSg8UPp72n0AQ&bih=788&biw=767\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "197ca86f-dca5-49ab-82f2-650e0eb4327d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c07c3311-fae0-4a18-a069-bc03d9571734",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(response.content,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "9030e99a-b416-4499-bec5-f97eb65ff485",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<!DOCTYPE html PUBLIC \"-//WAPFORUM//DTD XHTML Mobile 1.0//EN\" \"http://www.wapforum.org/DTD/xhtml-mobile10.dtd\">\n",
       "<html lang=\"en-IN\" xmlns=\"http://www.w3.org/1999/xhtml\"><head><meta content=\"application/xhtml+xml; charset=utf-8\" http-equiv=\"Content-Type\"/><meta content=\"no-cache\" name=\"Cache-Control\"/><title>ISRO - Google Search</title><style>a{text-decoration:none;color:inherit}a:hover{text-decoration:underline}a img{border:0}body{font-family:arial,sans-serif;padding:8px;margin:0 auto;max-width:700px;min-width:240px;}.FbhRzb{border-left:thin solid #dadce0;border-right:thin solid #dadce0;border-top:thin solid #dadce0;height:40px;overflow:hidden}.n692Zd{margin-bottom:10px}.cvifge{height:40px;border-spacing:0}.QvGUP{height:40px;padding:0 8px 0 8px;vertical-align:top}.O4cRJf{height:40px;width:100%;padding:0;padding-right:16px}.O1ePr{height:40px;padding:0;vertical-align:top}.kgJEQe{height:36px;width:98px;vertical-align:top;margin-top:4px}.lXLRf{vertical-align:top}.MhzMZd{border:0;vertical-align:middle;font-size:14px;height:40px;padding:0;width:100%;padding-left:16px}.xB0fq{height:40px;border:none;font-size:14px;background-color:#1a73e8;color:#fff;padding:0 16px;margin:0;vertical-align:top;cursor:pointer}.xB0fq:focus{border:1px solid #1a73e8}.M7pB2{border:thin solid #dadce0;margin:0 0 3px 0;font-size:13px;font-weight:500;height:40px}.euZec{width:100%;height:40px;text-align:center;border-spacing:0}table.euZec td{padding:0;width:25%}.QIqI7{display:inline-block;padding-top:4px;font-weight:bold;color:#4285f4}.EY24We{border-bottom:2px solid #4285f4}.CsQyDc{display:inline-block;color:#70757a}.TuS8Ad{font-size:14px}.HddGcc{padding:8px;color:#70757a}.dzp8ae{font-weight:bold;color:#3c4043}.rEM8G{color:#70757a}.bookcf{table-layout:fixed;width:100%;border-spacing:0}.InWNIe{text-align:center}.uZgmoc{border:thin solid #dadce0;color:#70757a;font-size:14px;text-align:center;table-layout:fixed;width:100%}.frGj1b{display:block;padding:12px 0 12px 0;width:100%}.BnJWBc{text-align:center;padding:6px 0 13px 0;height:35px}.e3goi{vertical-align:top;padding:0;height:180px}.GpQGbf{margin:auto;border-collapse:collapse;border-spacing:0;width:100%}</style></head><body><style>.X6ZCif{color:#202124;font-size:11px;line-height:16px;display:inline-block;padding-top:2px;overflow:hidden;padding-bottom:4px;width:100%}.TwVfHd{border-radius:16px;border:thin solid #dadce0;display:inline-block;padding:8px 8px;margin-right:8px;margin-bottom:4px}.yekiAe{background-color:#dadce0}.mnTahd{width:100%}.ezO2md{border:thin solid #dadce0;padding:12px 16px 12px 16px;margin-bottom:10px;font-family:arial,sans-serif}.lIMUZd{font-family:arial,sans-serif}.IkMU6e{border-spacing:0}.SjCsie{width:100%}.EnarA{text-align:center}.NZWO1b{width:162px;height:140px;line-height:140px;overflow:'hidden';text-align:center}.yWs4tf{text-align:center;margin:auto;vertical-align:middle;max-width:162px;max-height:140px}.jB2rPd{padding-top:2px;padding-bottom:8px;}.fYyStc{word-break:break-word}.ynsChf{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.Fj3V3b{color:#1967d2;font-size:14px;line-height:20px}.FrIlee{color:#202124;font-size:11px;line-height:16px}.F9iS2e{color:#70757a;font-size:11px;line-height:16px}.WMQ2Le{color:#70757a;font-size:12px;line-height:16px}.x3G5ab{color:#202124;font-size:12px;line-height:16px}.fuLhoc{color:#1967d2;font-size:16px;line-height:20px}.epoveb{font-size:24px;line-height:28px;font-weight:400;color:#202124}.dXDvrc{color:#0d652d;font-size:14px;line-height:20px;word-wrap:break-word}.dloBPe{font-weight:bold}.YVIcad{color:#70757a}.JkVVdd{color:#ea4335}.oXZRFd{color:#ea4335}.MQHtg{color:#fbbc04}.pyMRrb{color:#1e8e3e}.EtTZid{color:#1e8e3e}.M3vVJe{color:#1967d2}.qXLe6d{display:block}.NHQNef{font-style:italic}.Cb8Z7c{white-space:pre}a.ZWRArf{text-decoration:none}a .CVA68e:hover{text-decoration:underline}</style><div class=\"n692Zd\"><div class=\"BnJWBc\"><a class=\"lXLRf\" href=\"/?bih=788&amp;biw=767&amp;output=images&amp;ie=UTF-8&amp;tbm=isch&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQPAgC\"><img alt=\"Google\" class=\"kgJEQe\" src=\"/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif\"/></a></div><div class=\"FbhRzb\"><form action=\"/search\"><input name=\"bih\" type=\"hidden\" value=\"788\"/><input name=\"biw\" type=\"hidden\" value=\"767\"/><input name=\"ie\" type=\"hidden\" value=\"ISO-8859-1\"/><input name=\"tbm\" type=\"hidden\" value=\"isch\"/><input name=\"oq\" type=\"hidden\"/><input name=\"aqs\" type=\"hidden\"/><table class=\"cvifge\"><tr><td class=\"O4cRJf\"><input class=\"MhzMZd\" name=\"q\" type=\"text\" value=\"ISRO\"/></td><td class=\"O1ePr\"><input class=\"xB0fq\" type=\"submit\" value=\"Search\"/></td></tr></table></form></div><div class=\"M7pB2\"><table class=\"euZec\"><tbody><tr><td><a class=\"CsQyDc\" href=\"/search?q=ISRO&amp;bih=788&amp;biw=767&amp;ie=UTF-8&amp;source=lnms&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ_AUIBCgA\">ALL</a></td><td><a class=\"CsQyDc\" href=\"/search?q=ISRO&amp;bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=nws&amp;source=lnms&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ_AUIBSgB\">NEWS</a></td><td class=\"EY24We\"><span class=\"QIqI7\">IMAGES</span></td><td><a class=\"CsQyDc\" href=\"/search?q=ISRO&amp;bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=vid&amp;source=lnms&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ_AUIBygD\">VIDEOS</a></td></tr></tbody></table></div></div><div class=\"X6ZCif\"><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:logo&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYICygA\">logo</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:satellite&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIDCgB\">satellite</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:rocket&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIDSgC\">rocket</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:india&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIDigD\">india</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:space&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIDygE\">space</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:scientist&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIECgF\">scientist</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:pslv&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIESgG\">pslv</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:mission&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIEigH\">mission</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:bangalore&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIEygI\">bangalore</a><a class=\"TwVfHd\" href=\"/search?bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;q=ISRO&amp;chips=q:isro,g_1:launch&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQ4lYIFCgJ\">launch</a></div><div><table class=\"GpQGbf\"><tr><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://en.wikipedia.org/wiki/ISRO&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIABAB&amp;usg=AOvVaw26pJ-dpqDP2aBDAf97qpe2\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhEO4YcjxBKR2sNpMMZWr7PQ0-iZL629ku-XPKhDAn8zRUkvIxQdc4eLjqcy4&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://en.wikipedia.org/wiki/ISRO&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIABAC&amp;usg=AOvVaw1G_1mcQY55xyvpP9TBiJD0\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO - Wikipedia</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">en.wikipedia.org</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://en.wikipedia.org/wiki/Satish_Dhawan_Space_Centre&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIExAB&amp;usg=AOvVaw1PrZU0n6967G_v_XSGWZBm\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU9gSTVkWrD3GJPOGMp-ztg1I8y6YKLkAVoDb-MbAa-lsUCQrJw_SashcJPp4&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://en.wikipedia.org/wiki/Satish_Dhawan_Space_Centre&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIExAC&amp;usg=AOvVaw3jQ9KnRPBAJ1ntCifRN4Vm\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">Satish Dhawan Space Centre...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">en.wikipedia.org</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://twitter.com/airnewsalerts/status/1676930436130557955&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIEhAB&amp;usg=AOvVaw1Dd84EhW8PUs-rDHalW7Li\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9XRJb2AQCNssAw28EIkPBUo2xjIYwr8xRQyysFirZ2-usle7EAZsuGNtPZw&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://twitter.com/airnewsalerts/status/1676930436130557955&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIEhAC&amp;usg=AOvVaw1I9HR6tiMQ1xd4xkNlwp7R\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">All India Radio News on...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">twitter.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://news.abplive.com/science/isro-plans-to-return-to-mars-explore-dark-side-of-moon-with-japan-1561836&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIERAB&amp;usg=AOvVaw14wCxtFpJyfoM7Zclr8dTI\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTG4I2dRM_m3EROpwhGw7yFLTgIPRTzFZITskFFqoG6K4jpxKhmcGl7R9yQg&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://news.abplive.com/science/isro-plans-to-return-to-mars-explore-dark-side-of-moon-with-japan-1561836&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIERAC&amp;usg=AOvVaw2FIA97mUlo0QxpQkcPFbAx\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO Plans To Return To...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">news.abplive.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td></tr><tr><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.deccanherald.com/state/top-karnataka-stories/isro-s-training-programme-open-to-more-students-1231171.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIEBAB&amp;usg=AOvVaw3Oqp5qEZmqf2yZ_bda3G1Q\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaHxxX-xAxszxVbyb8qOSMd6uldbVEEjGJ3tc-me1JnbsP5Znr_xqQVGPYcT4&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.deccanherald.com/state/top-karnataka-stories/isro-s-training-programme-open-to-more-students-1231171.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIEBAC&amp;usg=AOvVaw0IVYKTr2fTzy1RayQuqm7L\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">Isro's training programme...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.deccanherald.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://m.timesofindia.com/india/isro-successfully-places-uk-firms-36-satellites-in-orbit/articleshow/99018713.cms&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIDxAB&amp;usg=AOvVaw3MIVpBZZWe82f-KytR6Xmz\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToBjsykVkdE7Kg94AwekdKZPOef44c69uqVb4UOqxb27tY_-JpMTd8CNdnTxc&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://m.timesofindia.com/india/isro-successfully-places-uk-firms-36-satellites-in-orbit/articleshow/99018713.cms&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIDxAC&amp;usg=AOvVaw1AfNtz2Mk8kxk6JG2LWexd\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO LVM 3 Launch: Isro...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">m.timesofindia.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.isro.gov.in/GSLVmk3_CON.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIDhAB&amp;usg=AOvVaw2IUDw68eCrUQeHTypjbYhI\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeIm5oldmoLunIf_9AATed-0I24tfydDilfrbJ4HGz3rdYxuRdDcCaG3a2j18&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.isro.gov.in/GSLVmk3_CON.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIDhAC&amp;usg=AOvVaw0ID_vkyy0s3IR083YaSYgC\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">Indian Space Research...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.isro.gov.in</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.indiatoday.in/science/story/isro-moves-lvm-3-with-36-oneweb-satellites-to-pad-launch-on-oct-23-2285803-2022-10-15&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIDBAB&amp;usg=AOvVaw1Pr4Cam7IuVbmQRCcMq7OG\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIYHiLM65HIoloMSo2Iq5GyMFcw7to0JP3QGRVxpuZWzcKv1FqbLqMs-xD_w&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.indiatoday.in/science/story/isro-moves-lvm-3-with-36-oneweb-satellites-to-pad-launch-on-oct-23-2285803-2022-10-15&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIDBAC&amp;usg=AOvVaw3gqS5p5Ov4CKIEjJ5iiOdQ\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">Isro moves rocket with 36...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.indiatoday.in</span> </span> </div></a></td></tr></table></div></div> </div> </div></td></tr><tr><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.livemint.com/science/news/isro-launches-seven-singaporean-satellites-onboard-a-pslv-rocket-from-sriharikotadssar-11690677428530.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIChAB&amp;usg=AOvVaw3imv88edHzCT6xNnxEXhGO\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk4TJHTArIBeH4uCM-6fdt7BkTRPAEQukfJ0h6ThZzRISVj35s16tiUQTe2g&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.livemint.com/science/news/isro-launches-seven-singaporean-satellites-onboard-a-pslv-rocket-from-sriharikotadssar-11690677428530.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIChAC&amp;usg=AOvVaw3XPLIfOikQkdmHa0h8bdf-\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO launches seven...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.livemint.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.businesstoday.in/technology/news/story/elon-musk-congratulates-indian-space-agency-isro-for-successful-pslv-c55-launch-378546-2023-04-24&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQICxAB&amp;usg=AOvVaw1FuE1bdOzAZPR_sAYLiCj1\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMNqH4onM0kXpKJkMKZnAAshN0TB9yrkgN-A6DhlIiXC6CmYD_NjXC-1z_Dw&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.businesstoday.in/technology/news/story/elon-musk-congratulates-indian-space-agency-isro-for-successful-pslv-c55-launch-378546-2023-04-24&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQICxAC&amp;usg=AOvVaw2Yi4g0XefqDF4FgJOXM-lE\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">Elon Musk congratulates...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.businesstoday.in</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.indiatodayne.in/meghalaya/story/isro-selects-meghalayas-ustm-as-nodal-centre-for-start-programme-603519-2023-06-24&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQICRAB&amp;usg=AOvVaw1mgjLFzadf0TDI4gHQ6MeI\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ34DNmN_lxIFKnIBSKotpQTOpHIWQUD0M4SRcnmQvOZUY7ZpVn8-GAtsf3xM&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.indiatodayne.in/meghalaya/story/isro-selects-meghalayas-ustm-as-nodal-centre-for-start-programme-603519-2023-06-24&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQICRAC&amp;usg=AOvVaw2FaPfcEpC9yaNIircQPyyK\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO selects Meghalaya's...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.indiatodayne.in</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://currentaffairs.adda247.com/list-of-isro-chairman-2023-name-tenure-and-other-important-fact/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIDRAB&amp;usg=AOvVaw3APEUSGIzC-MUy2SFWdSzg\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0XmDyVkCwZGDbMzh1xRht3-MDRYQCcIp-VlWTydGGbalxa1wfWkA9BLgn4g&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://currentaffairs.adda247.com/list-of-isro-chairman-2023-name-tenure-and-other-important-fact/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIDRAC&amp;usg=AOvVaw14HxP1Q6tWA582ch1cxVQe\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">List of ISRO Chairman 2023:...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">currentaffairs.adda247.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td></tr><tr><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://telanganatoday.com/isro-helping-send-man-6000-metres-deep-into-ocean&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQICBAB&amp;usg=AOvVaw1ibBBSYlVWKGn4diM1cGe4\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrtM8jyt2dzfTXw6n50foyTR5ugUt2OUHtB6azq2kjMzeWyYWMzNsgZognlaI&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://telanganatoday.com/isro-helping-send-man-6000-metres-deep-into-ocean&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQICBAC&amp;usg=AOvVaw2Iam2y5HjNz6TLpIL2xFEi\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO helping send man 6,000...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">telanganatoday.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://theprint.in/science/isro-earned-rs-1245-cr-in-5-years-by-launching-commercial-satellites-of-26-countries/334531/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIBRAB&amp;usg=AOvVaw04MC_rkl6AeKOSC2Gudlrb\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmimNBDP9lqGhaUFyHgeISu1xDrAHMxMg-BIw_cGYN8gRE0yPOBovbBG2SqA&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://theprint.in/science/isro-earned-rs-1245-cr-in-5-years-by-launching-commercial-satellites-of-26-countries/334531/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIBRAC&amp;usg=AOvVaw28Q-vtZiYRqrZkebH_ZLcH\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO earned Rs 1,245 cr in...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">theprint.in</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.jagranjosh.com/general-knowledge/list-of-isro-chairmen-1516281232-1&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIAhAB&amp;usg=AOvVaw2ht1FkgXapi4JfIIlJ-X7d\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvpB6Fzuzw5tEk1FoVgOy_DLOOyEHjnoTobz19sp-ZT0wdz1rLab2S7ta4v3M&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.jagranjosh.com/general-knowledge/list-of-isro-chairmen-1516281232-1&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIAhAC&amp;usg=AOvVaw36_Lv9BBb-IkzJA2VpDUKa\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">List of ISRO Chairman 2023:...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.jagranjosh.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://newsonair.com/2022/07/28/isro-earns-279-million-in-forex-through-satellite-launches-for-34-countries/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIAxAB&amp;usg=AOvVaw2kn2D64D0B_xLO1i57F4Rh\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2QwOhNC0o3hTWVQUOQOkza1DCNVGwRC2J197wpK8cfs4pzqJERZc4A51ixFQ&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://newsonair.com/2022/07/28/isro-earns-279-million-in-forex-through-satellite-launches-for-34-countries/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIAxAC&amp;usg=AOvVaw3eECdP-RiGlHsWWuiHB4Rd\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO earns $279 million in...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">newsonair.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td></tr><tr><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.ndtv.com/science/2-space-technology-startups-get-access-to-isro-facilities-what-they-plan-to-test-2545213&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIBhAB&amp;usg=AOvVaw07_LzDvRhtv1_gu-dR6Kgw\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZCNHs9nOspQtHmmaiyb0aljvdz8m0KC4xcozrBHnd2oeGQnMkEopY1vHA9g&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.ndtv.com/science/2-space-technology-startups-get-access-to-isro-facilities-what-they-plan-to-test-2545213&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIBhAC&amp;usg=AOvVaw3xV_lMCtCF5iMUovJ3Q_EI\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">2 Space Technology Startups...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.ndtv.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.youtube.com/watch%3Fv%3DrZtECdBjryE&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIBxAB&amp;usg=AOvVaw3WnN-Lp1G8OA7yZZRq1qgV\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6evrA5IxNEXe477_fOjJKDhzQhaJhJhKPFKemvXq_Os1SgSl-1qdI0WRqFQ&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.youtube.com/watch%3Fv%3DrZtECdBjryE&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIBxAC&amp;usg=AOvVaw2Z9H7mIUfvzUHaXnfxi1U9\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO Launch Today LIVE |...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.youtube.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.facebook.com/ISRO/posts/isro-launched-the-space-tutor-programme-that-aims-to-collaborate-with-startups-n/383913170535750/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIARAB&amp;usg=AOvVaw1qxZgW1GEdCC6qddM8kBxw\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWigxNOXVoc6G5yWtVuAqSs_HchwVFhWQ2r1lRgDeXOOGYSIkyX8-cRd7cgQ&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.facebook.com/ISRO/posts/isro-launched-the-space-tutor-programme-that-aims-to-collaborate-with-startups-n/383913170535750/&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIARAC&amp;usg=AOvVaw1bcwONa_UgQW6_oeOXjQvD\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">ISRO Launched... - ISRO -...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.facebook.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td><td align=\"center\" class=\"e3goi\"><div class=\"mnTahd\"> <div> <div class=\"lIMUZd\"><div><table class=\"IkMU6e\"><tr><td><a href=\"/url?q=https://www.indiatimes.com/explainers/news/isro-indian-space-research-organisation-551883.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQqoUBegQIBBAB&amp;usg=AOvVaw3GwVGcXtMpkH0_DK7Sk1WW\"><div class=\"NZWO1b\"><img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOuGh-2QFQ9_-wmbbMW-s39uPD9ct8AhSSy5DmJn_gKDEH9waQIy7WAvnghNs&amp;s\"/></div></a></td></tr><tr><td><a href=\"/url?q=https://www.indiatimes.com/explainers/news/isro-indian-space-research-organisation-551883.html&amp;sa=U&amp;ved=2ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQr4kDegQIBBAC&amp;usg=AOvVaw0PzaibdGXaSR_F27KOuwQR\"><div class=\"jB2rPd\"> <span class=\"qXLe6d x3G5ab\"> <span class=\"fYyStc\">Explained: How ISRO Has...</span> </span> <span class=\"qXLe6d F9iS2e\"> <span class=\"fYyStc\">www.indiatimes.com</span> </span> </div></a></td></tr></table></div></div> </div> </div></td></tr></table></div><table class=\"uZgmoc\"><tbody><td><a class=\"frGj1b\" href=\"/search?q=ISRO&amp;bih=788&amp;biw=767&amp;ie=UTF-8&amp;tbm=isch&amp;ei=PI_IZPGNBfDgseMP95WyuAE&amp;start=20&amp;sa=N\">Next &gt;</a></td></tbody></table><br/><div class=\"TuS8Ad\" data-ved=\"0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQpyoIUg\"><style>.VYM29{font-weight:bold}</style><div align=\"center\" class=\"HddGcc\"><span class=\"VYM29\">500037, Hyderabad, Telangana</span><span> - </span><span>From your IP address</span><span> - </span><a href=\"/url?q=https://support.google.com/websearch%3Fp%3Dws_settings_location%26hl%3Den-IN&amp;sa=U&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQty4IUw&amp;usg=AOvVaw1lwgnShRtHEJO73z-YJL6h\">Learn more</a></div><div align=\"center\"><a class=\"rEM8G\" href=\"/url?q=https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps://www.google.com/search%253Fq%253DISRO%2526tbm%253Disch%2526ved%253D2ahUKEwizs9SKyLqAAxV2yaACHafeCUoQ2-cCegQIABAA%2526oq%253Delon%252Bmusk%2526gs_lcp%253DCgNpbWcQAzIKCAAQigUQsQMQQzIKCAAQigUQsQMQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEOgQIIxAnOgsIABCABBCxAxCDAToNCAAQigUQsQMQgwEQQzoECAAQAzoHCAAQigUQQzoHCCMQ6gIQJzoICAAQsQMQgwFQ3ARYwRlg3CFoAXAAeAKAAYMBiAHdC5IBBDAuMTOYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ%2526sclient%253Dimg%2526ei%253D-oHIZLPOMPaSg8UPp72n0AQ%2526bih%253D788%2526biw%253D767%26hl%3Den&amp;sa=U&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQxs8CCFQ&amp;usg=AOvVaw0gBsXiaKfaXbazf7lTNqeX\">Sign in</a></div><div><table class=\"bookcf\"><tbody class=\"InWNIe\"><tr><td><a class=\"rEM8G\" href=\"https://www.google.com/preferences?hl=en&amp;sa=X&amp;ved=0ahUKEwjxm9rc1LqAAxVwcGwGHfeKDBcQv5YECFU\">Settings</a></td><td><a class=\"rEM8G\" href=\"https://www.google.com/intl/en_in/policies/privacy/\">Privacy</a></td><td><a class=\"rEM8G\" href=\"https://www.google.com/intl/en_in/policies/terms/\">Terms</a></td></tr></tbody></table></div></div><div> </div></body></html>"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "b1cada33-5660-4e34-ab5c-3b6c4589b429",
   "metadata": {},
   "outputs": [],
   "source": [
    "allimages = soup.find_all(\"img\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "a5958204-6f0e-46b7-8ac5-25916e8eab87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<img alt=\"Google\" class=\"kgJEQe\" src=\"/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhEO4YcjxBKR2sNpMMZWr7PQ0-iZL629ku-XPKhDAn8zRUkvIxQdc4eLjqcy4&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU9gSTVkWrD3GJPOGMp-ztg1I8y6YKLkAVoDb-MbAa-lsUCQrJw_SashcJPp4&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9XRJb2AQCNssAw28EIkPBUo2xjIYwr8xRQyysFirZ2-usle7EAZsuGNtPZw&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTG4I2dRM_m3EROpwhGw7yFLTgIPRTzFZITskFFqoG6K4jpxKhmcGl7R9yQg&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaHxxX-xAxszxVbyb8qOSMd6uldbVEEjGJ3tc-me1JnbsP5Znr_xqQVGPYcT4&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToBjsykVkdE7Kg94AwekdKZPOef44c69uqVb4UOqxb27tY_-JpMTd8CNdnTxc&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeIm5oldmoLunIf_9AATed-0I24tfydDilfrbJ4HGz3rdYxuRdDcCaG3a2j18&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIYHiLM65HIoloMSo2Iq5GyMFcw7to0JP3QGRVxpuZWzcKv1FqbLqMs-xD_w&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk4TJHTArIBeH4uCM-6fdt7BkTRPAEQukfJ0h6ThZzRISVj35s16tiUQTe2g&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMNqH4onM0kXpKJkMKZnAAshN0TB9yrkgN-A6DhlIiXC6CmYD_NjXC-1z_Dw&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ34DNmN_lxIFKnIBSKotpQTOpHIWQUD0M4SRcnmQvOZUY7ZpVn8-GAtsf3xM&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0XmDyVkCwZGDbMzh1xRht3-MDRYQCcIp-VlWTydGGbalxa1wfWkA9BLgn4g&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrtM8jyt2dzfTXw6n50foyTR5ugUt2OUHtB6azq2kjMzeWyYWMzNsgZognlaI&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmimNBDP9lqGhaUFyHgeISu1xDrAHMxMg-BIw_cGYN8gRE0yPOBovbBG2SqA&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvpB6Fzuzw5tEk1FoVgOy_DLOOyEHjnoTobz19sp-ZT0wdz1rLab2S7ta4v3M&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2QwOhNC0o3hTWVQUOQOkza1DCNVGwRC2J197wpK8cfs4pzqJERZc4A51ixFQ&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZCNHs9nOspQtHmmaiyb0aljvdz8m0KC4xcozrBHnd2oeGQnMkEopY1vHA9g&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6evrA5IxNEXe477_fOjJKDhzQhaJhJhKPFKemvXq_Os1SgSl-1qdI0WRqFQ&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWigxNOXVoc6G5yWtVuAqSs_HchwVFhWQ2r1lRgDeXOOGYSIkyX8-cRd7cgQ&amp;s\"/>,\n",
       " <img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOuGh-2QFQ9_-wmbbMW-s39uPD9ct8AhSSy5DmJn_gKDEH9waQIy7WAvnghNs&amp;s\"/>]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "allimages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "ef4fbf9e-3f0b-4c94-ab94-d00cc68a2ee0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<img alt=\"Google\" class=\"kgJEQe\" src=\"/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif\"/>"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "allimages[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "def5ccfa-377a-4bb9-afb7-336ce07b6c3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "del allimages[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "4e5d3eee-e963-47d3-9573-72139beeb657",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<img alt=\"\" class=\"yWs4tf\" src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhEO4YcjxBKR2sNpMMZWr7PQ0-iZL629ku-XPKhDAn8zRUkvIxQdc4eLjqcy4&amp;s\"/>"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "allimages[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "518a2c0f-2906-4aaf-a0a0-3fe677d715aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(allimages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "403e64e5-e4f2-43b1-ae7f-7bc7c09af70d",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in allimages:\n",
    "    image_url = i['src']\n",
    "    image_data = requests.get(image_url).content\n",
    "    \n",
    "    with open(os.path.join(save_dir, f\"{query}_{allimages.index(i)}.jpg\"),\"wb\") as f:\n",
    "        f.write(image_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66d16f7a-2f9b-4198-95cd-1e5ada47dfbc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `LICENSE`
```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
```

## File: `README.md`
```markdown
# End-to-End-Image-Scraping

The "Image Scraper" is a Flask web application that allows users to search for images on Google and download them directly to their local machines. The project leverages web scraping techniques to fetch the image URLs from Google search results and then download the images to a specified directory.

![aimeos-frontend](https://github.com/KalyanMurapaka45/End-to-End-Image-Scraping/blob/main/static/css/Screenshot%202023-08-03%20214154.png)

# About

About
In the era of the internet, images play a crucial role in various applications, including web development, data analysis, machine learning, and content creation. However, obtaining a large set of images related to a specific topic or keyword can be time-consuming and challenging.

The motivation behind the "Image Scraper" project is to simplify the process of collecting images for a given search query. By creating a user-friendly web interface, users can easily search for images and retrieve them without the need to manually visit multiple websites and download images one by one.

# Dependencies & Requirements

- Flask
- Requests
- Beautiful Soup
- PyMongo

 Anyways you can install all the above-mentioned libraries at a glance by executing the following command: ```requirements.txt required```
 
  ```bash
  pip install -r requirements.txt
  ```

# Project Execution

1. Clone the repository

   ```bash
   git clone https://github.com/KalyanMurapaka45/End-to-End-Image-Scraping.git
   ```
2. Install the required libraries

   ```bash
    pip install -r requirements.txt
   ```
3. Open and run the ```app.py``` file.
   ```bash
   python app.py
   ```

# Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

 - Fork the Project
 - Create your Feature Branch
 - Commit your Changes
 - Push to the Branch
 - Open a Pull Request

# Licnese

Distributed under the GNU General Public License v3.0. See LICENSE.txt for more information.

	
 # Acknowledgements

I would like to extend my heartfelt gratitude to the entire Ineuron Team for their constant support, guidance, and expertise throughout the development of the "Image Scraper" project. Their dedication to providing high-quality education and resources has been instrumental in my growth as a developer.
```

## File: `app.py`
```python
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import pymongo
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
import os

app = Flask(__name__) # initialising the flask app with the name 'app'  

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
                try:

                    # query to search for images
                    query = request.form['content'].replace(" ","")

                            # directory to store downloaded images
                    save_directory = "images/"

                            # create the directory if it doesn't exist
                    if not os.path.exists(save_directory):
                        os.makedirs(save_directory)



                            # fake user agent to avoid getting blocked by Google
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

                            # fetch the search results page
                    response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")


                            # parse the HTML using BeautifulSoup
                    soup = BeautifulSoup(response.content, "html.parser")

                            # find all img tags
                    image_tags = soup.find_all("img")

                            # download each image and save it to the specified directory
                    del image_tags[0]
                    img_data=[]
                    for index,image_tag in enumerate(image_tags):
                                # get the image source URL
                                image_url = image_tag['src']
                                #print(image_url)
                                
                                # send a request to the image URL and save the image
                                image_data = requests.get(image_url).content
                                mydict={"Index":index,"Image":image_data}
                                img_data.append(mydict)
                                with open(os.path.join(save_directory, f"{query}_{image_tags.index(image_tag)}.jpg"), "wb") as f:
                                    f.write(image_data)   
                    client = pymongo.MongoClient("mongodb+srv://kalyanmurapaka274:<password>@ineuron.3uqntxj.mongodb.net/?retryWrites=true&w=majority")
                    db = client['image_scrap']
                    review_col = db['image_scrap_data']
                    review_col.insert_many(img_data)         

                    return "Images downloaded successfully, check your folder"
                except Exception as e:
                    logging.info(e)
                    return 'Something is wrong, please try again!'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
```

## File: `requirements.txt`
```
flask
flask_cors
requests
bs4
pymongo
```

## File: `static/css/main.css`
```css
/* Reset some default styles to ensure consistency across browsers */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
  }
  
  body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  header {
    background-color: #007bff;
    color: #fff;
    padding: 10px;
    text-align: center;
  }
  
  /* Main content */
  main {
    padding: 20px;
  }
  
  /* Form styles */
  form {
    max-width: 400px;
    margin: 0 auto;
  }
  
  input[type="text"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  input[type="submit"] {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
  }
  
  /* Image gallery styles */
  .image-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 10px;
  }
  
  .image-item {
    border: 1px solid #ccc;
    padding: 5px;
    text-align: center;
  }
  
  .image-item img {
    max-width: 100%;
    height: auto;
  }
  
  /* Footer */
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
  }
  
  /* Responsive adjustments */
  @media screen and (max-width: 768px) {
    form {
      max-width: 100%;
    }
  }
  
```

## File: `static/css/style.css`
```css
/* Reset some default styles to ensure consistency across browsers */
body, h1, h2, h3, p, ul, li {
  margin: 0;
  padding: 0;
}

body {
  background-color: #91ced4;
  font-family: Arial, sans-serif;
  color: #333;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

header {
  background-color: #327a81;
  color: white;
  font-size: 1.5em;
  padding: 1rem;
  text-align: center;
  text-transform: uppercase;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
}

.search-box {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 400px;
  margin: 20px;
}

h2 {
  color: #2b686e;
  font-size: 1.2em;
  margin-bottom: 10px;
}

.input-container {
  display: flex;
  justify-content: left;
}

input[type="text"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

input[type="submit"] {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
}

input[type="submit"]:hover {
  background-color: #0056b3;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
}
```

## File: `templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    {% block head %}{% endblock %}
</head>
<body>
    {% block body %}{% endblock %}
</body>
</html>
```

## File: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% block head %}{% endblock %}
</head>
<body>
    <div class="container">
        <header>
            <h1>SCRAP YOUR IMAGE</h1>
        </header>
        <main>
            <div class="search-box">
                <h2>Search for Images</h2>
                <div class="input-container">
                    <form action="/review" method="POST">
                        <input type="text" name="content" placeholder="Enter your search query">
                        <input type="submit" value="Search">
                    </form>
                </div>
            </div>
        </main>
        
    </div>
</body>
</html>
```

## File: `templates/result.html`
```html
<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>Review Page</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">


      <link rel="stylesheet" href="./style.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">


</head>

<body>

  <div class="table-users">
   <div class="header">Reviews</div>

   <table cellspacing="0">
      <tr>
         <th>Product</th>
         <th>Name</th>
         <th>Rating</th>
         <th>Comment Heading</th>
         <th>mycomment </th>
         <th width="230">Comments</th>
      </tr>
         {% for review in reviews %}
      <tr>
          <td>{{review['Product']}}</td>
         <td>{{review['Name']}}</td>
         <td>{{review['Rating']}}</td>
         <td>{{review['CommentHead']}}</td>
         <td>{{review['Comment']}} </td>
         <td>{{review['Comment']}} </td>
       {% endfor %}
   </table>
</div>



</body>

</html>
```

