"""
Read the Common-Crawl-Index (cci) and convert to a cdx-like format
to be read by pywb
"""

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from commoncrawlindex.index import open_index_reader
from urlparse import urlsplit, urlunsplit

from pywb.utils.timeutils import sec_to_timestamp, timestamp_to_sec
from pywb.utils.wbexception import NotFoundException

from pywb.cdx.cdxserver import BaseCDXServer
from pywb.cdx.cdxops import cdx_filter

import bisect
import itertools
import logging


#=================================================================
class CCIServer(BaseCDXServer):
    def __init__(self, paths, **kwargs):
        super(CCIServer, self).__init__(**kwargs)
        self.index_url = paths

        logging.debug('Adding Common Crawl Index: ' + self.index_url)

    def _calc_search_keys(self, query):
        # only using start key and prefix, so return none
        return compute_cci_surt(url=query.url,
                                match_type=query.match_type), None

    def _load_cdx_query(self, query):
        index_reader = open_index_reader(self.index_url)

        cci_iter = index_reader.itemsiter(query.key)

        cci_iter = self.create_cci_obj(cci_iter)

        if query.is_exact:
            cci_iter = self.sort_cci_timestamp(cci_iter, query)

        if query.output == 'text':
            cci_iter = (str(cci) + '\n' for cci in cci_iter)

        return cci_iter

    def create_cci_obj(self, cci_iter):
        for key, data in cci_iter:
            yield CCIObject(key, data)

    def sort_cci_timestamp(self, cci_iter, query):
        sorted_cci = []

        limit = query.limit

        if query.closest:
            closest_sec = timestamp_to_sec(query.closest) * 1000
            key_func = lambda x: abs(closest_sec - x)
        elif query.reverse:
            key_func = lambda x: -x
        else:
            key_func = lambda x: x

        for cci in cci_iter:
            key = key_func(cci.data['arcFileDate'])

            # create tuple to sort by key
            bisect.insort(sorted_cci, (key, cci))

            if len(sorted_cci) > limit:
               sorted_cci.pop()

        for cci in itertools.imap(lambda x: x[1], sorted_cci):
            yield cci


#=================================================================
class CCIObject(OrderedDict):
    FORMAT = '{arcSourceSegmentId}/{arcFileDate}_{arcFilePartition}.arc.gz'

    def __init__(self, key, data):
        OrderedDict.__init__(self)

        self.data = data

        self['urlkey'] = key

        self['timestamp'] = sec_to_timestamp(data['arcFileDate'] / 1000)

        self['original'] = cci_surt_to_url(key)

        self['length'] = data['compressedSize']

        self['offset'] = data['arcFileOffset']

        self['filename'] = self.FORMAT.format(**data)

    def is_revisit(self):
        return False

    def __str__(self):
        return ' '.join(str(val) for n, val in self.iteritems())


#=================================================================
DEFAULT_SCHEME = 'http://'


#=================================================================
def compute_cci_surt(url, match_type='exact'):
    """
    >>> compute_cci_surt('http://example.com:80')
    'com.example/:http'

    >>> compute_cci_surt('example.com/path')
    'com.example/path:http'

    >>> compute_cci_surt('https://example.com/path?a=b')
    'com.example/path?a=b:https'

    >>> compute_cci_surt('https://example.com/path/', match_type='prefix')
    'com.example/path/'

    >>> compute_cci_surt('https://example.com/path?a=b', match_type='host')
    'com.example/'

    >>> compute_cci_surt('https://example.com/path?a=b', match_type='domain')
    'com.example'
    """

    if not '//' in url:
        url = DEFAULT_SCHEME + url

    splits = urlsplit(url)

    host = splits.netloc
    port_inx = host.find(':')
    if port_inx > 0:
        host = host[:port_inx]

    host_parts = host.split('.')
    host_parts.reverse()
    host = '.'.join(host_parts)

    # just return host name
    if match_type == 'domain':
        return host

    if match_type == 'host':
        return host + '/'

    path = splits.path
    if not path:
        path = '/'

    surt = host + path
    if splits.query:
        surt += '?' + splits.query

    if match_type == 'prefix':
        return surt

    surt += ':' + splits.scheme

    return surt


def cci_surt_to_url(cci_surt):
    """
    >>> cci_surt_to_url('com.example/')
    'http://example.com/'

    >>> cci_surt_to_url('com.example/:http')
    'http://example.com/'

    >>> cci_surt_to_url('com.example/path:http')
    'http://example.com/path'

    >>> cci_surt_to_url('com.example/path?a=b:https')
    'https://example.com/path?a=b'
    """

    scheme_inx = cci_surt.rfind(':')
    if scheme_inx > 0:
        scheme = cci_surt[scheme_inx + 1:] + '://'
        cci_surt = cci_surt[:scheme_inx]
    else:
        scheme = DEFAULT_SCHEME

    parts = cci_surt.split('/', 1)

    host = parts[0]
    host_parts = host.split('.')
    host_parts.reverse()
    host = '.'.join(host_parts)

    url = scheme + host + '/'

    if len(parts) == 2:
        url += parts[1]

    return url


if __name__ == "__main__":
    import doctest
    doctest.testmod()
