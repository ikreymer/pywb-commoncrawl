"""
Test CCI index against latest existing index

>>> load_cci(url='http://ask.metafilter.com/')
com.metafilter.ask/:http 20120905183911 http://ask.metafilter.com/ 14478 81870361 1346823846039/1346870351851_319.arc.gz
com.metafilter.ask/:http 20120906051632 http://ask.metafilter.com/ 15070 72535037 1346876860782/1346908592443_2165.arc.gz
com.metafilter.ask/:http 20120906052248 http://ask.metafilter.com/ 15169 18143837 1346876860782/1346908968496_2151.arc.gz


>>> load_cci(url='http://ask.metafilter.com/', reverse=True)
com.metafilter.ask/:http 20120906052248 http://ask.metafilter.com/ 15169 18143837 1346876860782/1346908968496_2151.arc.gz
com.metafilter.ask/:http 20120906051632 http://ask.metafilter.com/ 15070 72535037 1346876860782/1346908592443_2165.arc.gz
com.metafilter.ask/:http 20120905183911 http://ask.metafilter.com/ 14478 81870361 1346823846039/1346870351851_319.arc.gz


>>> load_cci(url='http://ask.metafilter.com/', closest='20120906051632')
com.metafilter.ask/:http 20120906051632 http://ask.metafilter.com/ 15070 72535037 1346876860782/1346908592443_2165.arc.gz
com.metafilter.ask/:http 20120906052248 http://ask.metafilter.com/ 15169 18143837 1346876860782/1346908968496_2151.arc.gz
com.metafilter.ask/:http 20120905183911 http://ask.metafilter.com/ 14478 81870361 1346823846039/1346870351851_319.arc.gz


>>> load_cci(url='http://ask.metafilter.com/', closest='20120906051632', limit=1)
com.metafilter.ask/:http 20120906051632 http://ask.metafilter.com/ 15070 72535037 1346876860782/1346908592443_2165.arc.gz


>>> load_cci(url='http://ask.metafilter.com/51007/', matchType='prefix')
com.metafilter.ask/51007/:http 20120905111717 http://ask.metafilter.com/51007/ 6374 66434006 1346823846176/1346843837912_1614.arc.gz
com.metafilter.ask/51007/Whats-the-best-eBay-auction-software:http 20120905111717 http://ask.metafilter.com/51007/Whats-the-best-eBay-auction-software 6373 62065012 1346823846176/1346843837912_1614.arc.gz


>>> load_cci(url='http://ask.metafilter.com/', matchType='prefix', limit=5)
com.metafilter.ask/100000/Ideas-for-pureed-food-for-a-30something-who-is-really-picky:http 20120906053937 http://ask.metafilter.com/100000/Ideas-for-pureed-food-for-a-30something-who-is-really-picky 15037 60370054 1346876860782/1346909977844_2165.arc.gz
com.metafilter.ask/100014/How-to-care-for-my-geek-husband:http 20120906053937 http://ask.metafilter.com/100014/How-to-care-for-my-geek-husband 38425 32253251 1346876860782/1346909977844_2165.arc.gz
com.metafilter.ask/100020/How-can-I-investigateremedy-possibly-misleading-loan-agreements-from-several-years-ago:http 20120906051341 http://ask.metafilter.com/100020/How-can-I-investigateremedy-possibly-misleading-loan-agreements-from-several-years-ago 10037 67368591 1346876860782/1346908421435_2166.arc.gz
com.metafilter.ask/100033/Whats-the-best-way-to-react-to-a-socially-awkward-situation:http 20120906053041 http://ask.metafilter.com/100033/Whats-the-best-way-to-react-to-a-socially-awkward-situation 8511 72305412 1346876860782/1346909441825_2166.arc.gz
com.metafilter.ask/100037/If-I-want-to-drop-into-college-courses-should-I-ask-the-professor-for-permission-or-should-I-just-sit-in:http 20120906052210 http://ask.metafilter.com/100037/If-I-want-to-drop-into-college-courses-should-I-ask-the-professor-for-permission-or-should-I-just-sit-in 28226 76836109 1346876860782/1346908930836_2167.arc.gz

"""

from cciserver import CCIServer

CCI_PATH = 's3://aws-publicdatasets/common-crawl/projects/url-index/url-index.1356128792'
cci_server = CCIServer(CCI_PATH)

import sys

def load_cci(**params):
    result = cci_server.load_cdx(**params)
    for line in result:
        sys.stdout.write(line)


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod()
