#! python3
import sys
import urllib2
from scrapy.selector import Selector    # tested with scrapy 0.20.2
from cookielib import CookieJar

def xpathgrep(xpath, url):
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    page_handle = opener.open(url)
    html_source = page_handle.read()
    selector = Selector(text=html_source)
    return '\t'.join(selector.xpath(xpath).extract())

if __name__=='__main__':
    xpath = sys.argv[1]
    url = sys.argv[2]
    print xpathgrep(xpath, url)