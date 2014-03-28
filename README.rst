Common Crawl Web Archive Browser (Wayback)
==========================================

This project provides for querying and direct browsing of portions of the Common Crawl.
It uses the `Common Crawl Url-Index <http://commoncrawl.org/common-crawl-url-index/>`_, specifically the `commoncrawlindex <https://github.com/wiseman/common_crawl_index>`_ python library and extends the `pywb <https://github.com/ikreymer/pywb>`_ (python wayback) project to provide web archive browsing capabilities for the Common Crawl.

This extension allows direct browsing of Common Crawl Web Data **that has been indexed.**
At this time, it appears that the url-index is only partial and a lot of non-text content may be missing.


Installation
------------

Install with pip:

``pip install -r requirements.txt``

This will install pywb and other dependencies.

To run with wsgi ref:

- ``./run.sh``


To run with uwsgi (if not already installed, ``pip install uwsgi`` may be needed)

- ``./run-uwsgi.sh``


Browsing
--------

This browser follow standard wayback machine url conventions:
For example, to see a list of captures for ``http://ask.metafilter.com``
you can point your browser to:

``http://localhost:8080/commoncrawl/*/http://ask.metafilter.com``

You can also view captures for all urls starting with a given prefix by using
the wildcard query:

``http://localhost:8080/commoncrawl/*/http://ask.metafilter.com*``

There is also a lower-level api for fetching the index in plain-text format:

``http://localhost:8080/commoncrawl-index?url=http://ask.metafilter.com&matchType=host``

(This query converts the Common-Crawl Index into a text CDX-like index. Additional
options to be added at a later time.)

Additional Info
"""""""""""""""
See the `cci-config.yaml <https://github.com/ikreymer/pywb-commoncrawl/blob/master/cci-config.yaml>` file for configuration info specific to this deployment.

See the `pywb github page <https://github.com/ikreymer/pywb>`_ project for more details and documentation of pywb wayback implementation.

