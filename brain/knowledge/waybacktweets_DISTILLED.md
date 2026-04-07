---
id: waybacktweets
type: knowledge
owner: OA_Triage
---
# waybacktweets
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Wayback Tweets

[![PyPI](https://img.shields.io/pypi/v/waybacktweets)](https://pypi.org/project/waybacktweets) [![PyPI Downloads](https://static.pepy.tech/badge/waybacktweets)](https://pepy.tech/projects/waybacktweets)

Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing (see [Field Options](https://waybacktweets.claromes.com/field_options)), and saves the data in HTML, for easy viewing of the tweets using the iframe tags, CSV, and JSON formats.

## Installation

It is compatible with Python versions 3.10 and above. [See installation options](https://waybacktweets.claromes.com/installation).

```shell
pipx install waybacktweets
```

## CLI

```shell
Usage:
  waybacktweets [OPTIONS] USERNAME
  USERNAME: The Twitter username without @

Options:
  -c, --collapse [urlkey|digest|timestamp:xx]
                                  Collapse results based on a field, or a
                                  substring of a field. XX in the timestamp
                                  value ranges from 1 to 14, comparing the
                                  first XX digits of the timestamp field. It
                                  is recommended to use from 4 onwards, to
                                  compare at least by years.
  -f, --from DATE                 Filtering by date range from this date.
                                  Format: YYYYmmdd
  -t, --to DATE                   Filtering by date range up to this date.
                                  Format: YYYYmmdd
  -l, --limit INTEGER             Query result limits.
  -rk, --resumption_key TEXT      Allows for a simple way to scroll through
                                  the results. Key to continue the query from
                                  the end of the previous query.
  -mt, --matchtype [exact|prefix|host|domain]
                                  Results matching a certain prefix, a certain
                                  host or all subdomains.
  -v, --verbose                   Shows the log.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.

Examples:
  waybacktweets jack
  waybacktweets --from 20200305 --to 20231231 --limit 300 --verbose jack

Repository:
  https://github.com/claromes/waybacktweets

Documentation:
  https://waybacktweets.claromes.com
```

## Module

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tnaM3rMWpoSHBZ4P_6iHFPjraWRQ3OGe?usp=sharing)

```python
from waybacktweets import WaybackTweets, TweetsParser, TweetsExporter

USERNAME = "jack"

api = WaybackTweets(USERNAME)
archived_tweets = api.get()

if archived_tweets:
    field_options = [
        "archived_urlkey",
        "archived_timestamp",
        "parsed_archived_timestamp",
        "archived_tweet_url",
        "parsed_archived_tweet_url",
        "original_tweet_url",
        "parsed_tweet_url",
        "available_tweet_text",
        "available_tweet_is_RT",
        "available_tweet_info",
        "archived_mimetype",
        "archived_statuscode",
        "archived_digest",
        "archived_length",
        "resumption_key",
    ]

    parser = TweetsParser(archived_tweets, USERNAME, field_options)
    parsed_tweets = parser.parse()

    exporter = TweetsExporter(parsed_tweets, USERNAME, field_options)
    exporter.save_to_csv()
    exporter.save_to_json()
    exporter.save_to_html()
```

## Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://waybacktweets.streamlit.app)

A prototype written in Python with the Streamlit framework and hosted on Streamlit Cloud.

Important: Starting from version 1.0, the web app will no longer receive all updates from the official package. To access all features, prefer using the package from PyPI.

## Documentation

- [Wayback Tweets documentation](https://waybacktweets.claromes.com/).
- [Wayback CDX Server API (Beta) documentation](https://archive.org/developers/wayback-cdx-server.html).

## Acknowledgements

- Tristan Lee (Bellingcat's Data Scientist) for the idea.
- Jessica Smith (Snowflake's Community Growth Specialist) and Streamlit team for the additional server resources on Streamlit Cloud.
- OSINT Community for recommending the package and the application.

## License

[GPL-3.0](LICENSE.md)

```

### File: app\requirements.txt
```txt
streamlit==1.45.0
waybacktweets

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        additional_dependencies: ["Flake8-pyproject"]
  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args:
          - --profile=black

```

### File: .pre_commit_config.yaml
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        additional_dependencies: ["Flake8-pyproject"]
  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args:
          - --profile=black

```

### File: LICENSE.md
```md
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

                            Preamble

The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works. By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users. We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors. You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price. Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights. Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received. You must make sure that they, too, receive
or can get the source code. And you must show them these terms so they
know their rights.

Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software. For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so. This is fundamentally incompatible with the aim of
protecting users' freedom to change the software. The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable. Therefore, we
have designed this version of the GPL to prohibit the practice for those
products. If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary. To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

0. Definitions.

"This License" refers to version 3 of the GNU General Public License.

"Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

"The Program" refers to any copyrightable work licensed under this
License. Each licensee is addressed as "you". "Licensees" and
"recipients" may be individuals or organizations.

To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy. The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

A "covered work" means either the unmodified Program or a work based
on the Program.

To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy. Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

To "convey" a work means any kind of propagation that enables other
parties to make or receive copies. Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License. If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

1. Source Code.

The "source code" for a work means the preferred form of the work
for making modifications to it. "Object code" means any non-source
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
implementation is available to the public in source code form. A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities. However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work. For example, Corresponding Source
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
conditions are met. This License explicitly affirms your unlimited
permission to run the unmodified Program. The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work. This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force. You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright. Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

Conveying under any other circumstances is permitted solely under
the conditions stated below. Sublicensing is not allowed; section 10
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
beyond what the individual works permit. Inclusion of a covered work
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

A "User Product" is either (1) a "con
... [TRUNCATED]
```

### File: app\app.py
```py
from datetime import datetime, timedelta

import streamlit as st
import streamlit.components.v1 as components

from waybacktweets.api.export import TweetsExporter
from waybacktweets.api.parse import TweetsParser
from waybacktweets.api.request import WaybackTweets
from waybacktweets.api.visualize import HTMLTweetsVisualizer
from waybacktweets.config import config

# ------ Initial Settings ------ #

PAGE_ICON = "assets/parthenon.png"
TITLE = "assets/waybacktweets.png"
FIELD_OPTIONS = [
    "archived_urlkey",
    "archived_timestamp",
    "parsed_archived_timestamp",
    "archived_tweet_url",
    "parsed_archived_tweet_url",
    "original_tweet_url",
    "parsed_tweet_url",
    "available_tweet_text",
    "available_tweet_is_RT",
    "available_tweet_info",
    "archived_mimetype",
    "archived_statuscode",
    "archived_digest",
    "archived_length",
]

collapse = None
matchtype = None
start_date = datetime.now() - timedelta(days=30 * 6)
end_date = datetime.now()
min_date = datetime(2006, 1, 1)

# ------ Verbose Mode Configuration ------ #

config.verbose = False

# ------ Page Configuration ------ #

st.set_page_config(
    page_title="Wayback Tweets",
    page_icon=PAGE_ICON,
    layout="centered",
    menu_items={
        "About": f"""
© 2023-{end_date.year} [Claromes](https://claromes.com). Licensed under the [GPL-3.0](https://raw.githubusercontent.com/claromes/waybacktweets/refs/heads/main/LICENSE.md). Icon by The Doodle Library. Title font by Google, licensed under the Open Font License (OFL).

---
""",  # noqa: E501
        "Report a bug": "https://github.com/claromes/waybacktweets/issues",
    },
)

# ------ Set States and Params ------ #

if "current_username" not in st.session_state:
    st.session_state.current_username = ""

if "count" not in st.session_state:
    st.session_state.count = False

if "archived_timestamp_filter" not in st.session_state:
    st.session_state.archived_timestamp_filter = (start_date, end_date)

if "username_value" not in st.session_state:
    st.session_state.username_value = ""

if "expanded_value" not in st.session_state:
    st.session_state.expanded_value = False

if "query" not in st.session_state:
    st.session_state.query = False

if "update_component" not in st.session_state:
    st.session_state.update_component = 0

if "username" not in st.query_params:
    st.query_params["username"] = ""

# ------ Add Custom CSS Style ------ #

st.html(
    """
    <style>
        header[data-testid="stHeader"] {
            opacity: 0.5;
        }
        iframe {
            border: 1px solid #dddddd;
            border-radius: 0.5rem;
        }
        div[data-testid="InputInstructions"] {
            visibility: hidden;
        }
        button[data-testid="StyledFullScreenButton"] {
            display: none;
        }
        div[class="st-emotion-cache-1v0mbdj e115fcil1"] {
            max-width: 100%;
        }
        div[data-testid="stElementToolbarButtonContainer"] {
            display: none;
        }
    </style>
    """
)

# ------ Functions ------ #


@st.cache_data(ttl=600, show_spinner=False)
def wayback_tweets(
    username,
    collapse,
    timestamp_from,
    timestamp_to,
    limit,
    matchtype,
):
    response = WaybackTweets(
        username,
        collapse,
        timestamp_from,
        timestamp_to,
        limit,
        matchtype,
    )
    archived_tweets = response.get()

    return archived_tweets


@st.cache_data(ttl=600, show_spinner=False)
def tweets_parser(archived_tweets, username, field_options):
    parser = TweetsParser(archived_tweets, username, field_options)
    parsed_tweets = parser.parse()

    return parsed_tweets


@st.cache_data(ttl=600, show_spinner=False)
def tweets_exporter(parsed_tweets, username, field_options):
    exporter = TweetsExporter(parsed_tweets, username, field_options)

    df = exporter.dataframe
    file_name = exporter.filename

    return df, file_name


# ------ Custom JavaScript ------ #


def scroll_page():
    js = f"""
    <script>
        window.parent.document.querySelector('section.main').scrollTo(700, 700);
        let update_component = {st.session_state.update_component} // Force component update to generate scroll
    </script>
    """  # noqa: E501

    components.html(js, width=0, height=0)


# ------ Query Param ------ #

if st.query_params.username != "":
    st.session_state.username_value = st.query_params.username
    st.session_state.expanded_value = True
    st.session_state.query = True

    st.session_state.update_component += 1
    scroll_page()

# ------ UI Settings ------ #

st.image(TITLE, width=None)
st.write(
    "Retrieves archived tweets CDX data in HTML, CSV, and JSON formats."  # noqa: E501
)

st.write(
    "This application is a prototype based on the Python package and does not include all available features. To explore the package, including CLI and Module usage, visit the [GitHub repository](https://github.com/claromes/waybacktweets)."  # noqa: E501
)

st.divider()

# -- Filters -- #

username = st.text_input(
    "Username",
    value=st.session_state.username_value,
    key="username",
    placeholder="Without @",
)

st.session_state.archived_timestamp_filter = st.date_input(
    "Tweets saved between",
    (start_date, end_date),
    min_date,
    end_date,
    format="YYYY/MM/DD",
    help="Using the `from` and `to` filters. Format: YYYY/MM/DD",
)
st.caption(
    ":gray[Note: Large date ranges may take longer to process and exceed the app's resource limits. Use smaller ranges for faster results.]"  # noqa: E501
)

limit = st.text_input(
    "Limit",
    key="limit",
    help="Query result limits (int)",
)

unique = st.checkbox(
    "Only unique Wayback Machine URLs",
    key="unique",
    help="Filtering by the collapse option using the `urlkey` field and the URL Match Scope `prefix`",  # noqa: E501
)
st.caption(
    ":gray[Note: As noted in the official Wayback CDX Server API documentation, retrieving unique URLs may experience slow performance at this time.]"  # noqa: E501
)


query = st.button("Go", type="primary", use_container_width=True)

if st.query_params.username == "":
    st.query_params.clear()
    st.session_state.query = query

# ------ Results ------ #

if username != st.session_state.current_username:
    st.session_state.current_username = username

if (st.session_state.query and username) or st.session_state.count:
    if unique:
        collapse = "urlkey"
        matchtype = "prefix"

    try:
        with st.spinner(f"Retrieving @{st.session_state.current_username}..."):
            wayback_tweets = wayback_tweets(
                st.session_state.current_username,
                collapse,
                st.session_state.archived_timestamp_filter[0],
                st.session_state.archived_timestamp_filter[1],
                limit,
                matchtype,
            )

        if not wayback_tweets:
            st.error("No data was saved due to an empty response.")
            st.stop()

        with st.spinner(f"Parsing @{st.session_state.current_username}..."):
            parsed_tweets = tweets_parser(
                wayback_tweets, st.session_state.current_username, FIELD_OPTIONS
            )

            df, file_name = tweets_exporter(
                parsed_tweets, st.session_state.current_username, FIELD_OPTIONS
            )

        csv_data = df.to_csv(index=False)
        json_data = df.to_json(orient="records", lines=False)
        html = HTMLTweetsVisualizer(username, json_data)
        html_content = html.generate()

        # -- Rendering -- #

        st.session_state.count = len(df)
        st.caption(f"{st.session_state.count} URLs have been captured.")

        tab1, tab2, tab3 = st.tabs(["HTML", "CSV", "JSON"])

        # -- HTML -- #
        with tab1:
            st.download_button(
                label=f"Download @{st.session_state.current_username} in HTML",
                data=html_content,
                file_name=f"{file_name}.html",
                mime="text/html",
                icon=":material/download:",
            )

            st.caption("Note: The iframes are best viewed in Firefox.")

            # -- CSV -- #
        with tab2:
            st.download_button(
                label=f"Download @{st.session_state.current_username} in CSV",
                data=csv_data,
                file_name=f"{file_name}.csv",
                mime="text/csv",
                icon=":material/download:",
            )

            st.caption("Preview:")
            st.dataframe(df, use_container_width=True)

            # -- JSON -- #
        with tab3:
            st.download_button(
                label=f"Download @{st.session_state.current_username} in JSON",
                data=json_data,
                file_name=f"{file_name}.json",
                mime="application/json",
                icon=":material/download:",
            )

            st.caption("Preview:")
            st.json(json_data, expanded=1)
    except TypeError as e:
        st.error(
            f"""
        {e}. Refresh this page and try again.

        If the problem persists [open an issue](https://github.com/claromes/waybacktweets/issues)."""  # noqa: E501
        )
        st.stop()
    except IndexError:
        st.error("Please check if you have entered a date range in the filter.")
        st.stop()
    except Exception as e:
        st.error(str(e))
        st.stop()

```

### File: docs\conf.py
```py
import datetime

from pallets_sphinx_themes import ProjectLink, get_version

project = "Wayback Tweets"
release, version = get_version("waybacktweets")
rst_epilog = f".. |release| replace:: v{release}"
copyright = f"2023 - {datetime.datetime.now().year}, Claromes · Icon by The Doodle Library · Title font by Google, licensed under the Open Font License · Release: v{release}"  # noqa: E501
author = "Claromes"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "pallets_sphinx_themes",
    "sphinxcontrib.mermaid",
    "sphinx_new_tab_link",
    "sphinx_click.ext",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autodoc_typehints = "description"

# -- Options for HTML output -------------------------------------------------

html_theme = "flask"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_context = {
    "project_links": [
        ProjectLink("PyPI", "https://pypi.org/project/waybacktweets/"),
        ProjectLink("Source Code", "https://github.com/claromes/waybacktweets/"),
        ProjectLink(
            "License",
            "https://raw.githubusercontent.com/claromes/waybacktweets/refs/heads/main/LICENSE.md",  # noqa: E501
        ),
        ProjectLink(
            "Issue Tracker", "https://github.com/claromes/waybacktweets/issues/"
        ),
        ProjectLink("Mastodon", "https://ruby.social/@claromes"),
        ProjectLink("Bluesky", "https://bsky.app/profile/claromes.com"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
html_favicon = "../assets/parthenon.png"
html_logo = "../assets/parthenon.png"
html_title = f"Wayback Tweets Documentation ({version})"
html_show_sourcelink = False

```

### File: docs\templates\page.html
```html
{% extends "!page.html" %}

{% block extrahead %}
{{ super() }}
    <meta name="description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">

    <meta property="og:title" content="{{ title|e }}" />
    <meta property="og:description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">
    <meta property="og:image" content="https://waybacktweets.claromes.com/_static/card.png" />

    <meta name="twitter:title" content="{{ title|e }}">
    <meta name="twitter:description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">
    <meta property="twitter:image" content="https://waybacktweets.claromes.com/_static/card.png" />
{% endblock %}

```

### File: docs\_templates\page.html
```html
{% extends "!page.html" %}

{% block extrahead %}
{{ super() }}
    <meta name="description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">

    <meta property="og:title" content="{{ title|e }}" />
    <meta property="og:description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">
    <meta property="og:image" content="https://waybacktweets.claromes.com/_static/card.png" />

    <meta name="twitter:title" content="{{ title|e }}">
    <meta name="twitter:description" content="Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing, and saves the data">
    <meta property="twitter:image" content="https://waybacktweets.claromes.com/_static/card.png" />
{% endblock %}

```

### File: docs\static\css\custom.css
```css
body {
    font-family: Georgia, 'Times New Roman', Times, serif;
    background-color: whitesmoke;
}

a:hover {
    background-color: whitesmoke !important;
}

#cli #usage #waybacktweets h3,
#cli .admonition-title,
.sphinxsidebarwrapper li ul li ul:has(a[href="#waybacktweets"]):last-child {
    display: none;
}

```

### File: docs\_static\css\custom.css
```css
body {
    font-family: Georgia, 'Times New Roman', Times, serif;
    background-color: whitesmoke;
}

a:hover {
    background-color: whitesmoke !important;
}

#cli #usage #waybacktweets h3,
#cli .admonition-title,
.sphinxsidebarwrapper li ul li ul:has(a[href="#waybacktweets"]):last-child {
    display: none;
}

```

