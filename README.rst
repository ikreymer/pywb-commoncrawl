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

There are a few quick run scripts:

- ``./run.sh`` -- run with wsgi ref
- ``./run-uwsgi.sh`` -- run with uwsgi (must have uwsgi installed, eg: ``pip install uwsgi``)
- ``./run-gunicorn.sh`` -- run with gunicorn (must have gunicorn install, eg: ``pip install gunicorn``)


Tests
"""""

To run tests against live index (must have py.test installed, eg: ``pip install pytest``)

- ``./run-tests.sh``


Browsing
--------

This browser follow standard wayback machine url conventions:
For example, to see a list of captures for *ask.metafilter.com*
you can point your browser to:

`http://localhost:8080/commoncrawl/*/http://ask.metafilter.com <http://localhost:8080/commoncrawl/*/http://ask.metafilter.com>`_

You can also view captures for all urls starting with a given prefix by using
the wildcard query:

`http://localhost:8080/commoncrawl/*/http://ask.metafilter.com* <http://localhost:8080/commoncrawl/*/http://ask.metafilter.com*>`_

There is also a lower-level api for fetching the index in plain-text format:

`http://localhost:8080/commoncrawl-index?url=http://ask.metafilter.com&matchType=host <http://localhost:8080/commoncrawl-index?url=http://ask.metafilter.com&matchType=host>`_

(This query converts the Common-Crawl Index into a text CDX-like index. Additional
options to be added at a later time.)

Additional Info
"""""""""""""""
See the `cci-config.yaml <https://github.com/ikreymer/pywb-commoncrawl/blob/master/cci-config.yaml>`_ file for configuration info specific to this deployment.

See the `pywb github page <https://github.com/ikreymer/pywb>`_ project for more details and documentation of pywb wayback implementation.

