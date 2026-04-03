---
id: codelucas-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:08.069786
---

# KNOWLEDGE EXTRACT: codelucas
> **Extracted on:** 2026-03-30 17:34:53
> **Source:** codelucas

---

## File: `newspaper.md`
```markdown
# 📦 codelucas/newspaper [🔖 PENDING/APPROVE]
🔗 https://github.com/codelucas/newspaper
🌐 https://goo.gl/VX41yK

## Meta
- **Stars:** ⭐ 15017 | **Forks:** 🍴 2129
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
newspaper3k is a news, full-text, and article metadata extraction in Python 3. Advanced docs:

## README (trích đầu)
```
Newspaper3k: Article scraping & curation
========================================

.. image:: https://badge.fury.io/py/newspaper3k.svg
    :target: http://badge.fury.io/py/newspaper3k.svg
        :alt: Latest version

.. image:: https://travis-ci.org/codelucas/newspaper.svg
        :target: http://travis-ci.org/codelucas/newspaper/
        :alt: Build status

.. image:: https://coveralls.io/repos/github/codelucas/newspaper/badge.svg?branch=master
        :target: https://coveralls.io/github/codelucas/newspaper
        :alt: Coverage status


Inspired by `requests`_ for its simplicity and powered by `lxml`_ for its speed:

    "Newspaper is an amazing python library for extracting & curating articles."
    -- `tweeted by`_ Kenneth Reitz, Author of `requests`_

    "Newspaper delivers Instapaper style article extraction." -- `The Changelog`_

.. _`tweeted by`: https://twitter.com/kennethreitz/status/419520678862548992
.. _`The Changelog`: http://thechangelog.com/newspaper-delivers-instapaper-style-article-extraction/

**Newspaper is a Python3 library**! Or, view our **deprecated and buggy** `Python2 branch`_

.. _`Python2 branch`: https://github.com/codelucas/newspaper/tree/python-2-head

A Glance:
---------

.. code-block:: pycon

    >>> from newspaper import Article

    >>> url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    >>> article = Article(url)

.. code-block:: pycon

    >>> article.download()

    >>> article.html
    '<!DOCTYPE HTML><html itemscope itemtype="http://...'

.. code-block:: pycon

    >>> article.parse()

    >>> article.authors
    ['Leigh Ann Caldwell', 'John Honway']

    >>> article.publish_date
    datetime.datetime(2013, 12, 30, 0, 0)

    >>> article.text
    'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'

    >>> article.top_image
    'http://someCDN.com/blah/blah/blah/file.png'

    >>> article.movies
    ['http://youtube.com/path/to/link.com', ...]

.. code-block:: pycon

    >>> article.nlp()

    >>> article.keywords
    ['New Years', 'resolution', ...]

    >>> article.summary
    'The study shows that 93% of people ...'

.. code-block:: pycon

    >>> import newspaper

    >>> cnn_paper = newspaper.build('http://cnn.com')

    >>> for article in cnn_paper.articles:
    >>>     print(article.url)
    http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/
    http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html
    ...

    >>> for category in cnn_paper.category_urls():
    >>>     print(category)

    http://lifestyle.cnn.com
    http://cnn.com/world
    http://tech.cnn.com
    ...

    >>> cnn_article = cnn_paper.articles[0]
    >>> cnn_article.download()
    >>> cnn_article.parse()
    >>> cnn_article.nlp()
    ...

.. code-block:: pycon

    >>> from newspaper import fulltext

    >>> html = requests.get(...).text
    >>> text = fulltext(html)


Newspaper can extract and detect languages *seamlessly*.
If no langua
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

