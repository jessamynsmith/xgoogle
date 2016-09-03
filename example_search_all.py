#!/usr/bin/python
#
# This program does a Google search for "quick" and returns
# all results.
#

from xgoogle.search import GoogleSearch, SearchError

try:
    gs = GoogleSearch("quick=", tld="ca")
    gs.results_per_page = 50
    total_results = 0
    while not gs.eor:
        results = gs.get_results()
        total_results += len(results)
        for res in results:
            print(res.url.encode('utf8'))
    print('Got %s results total' % total_results)
except SearchError, e:
    print "Search failed: %s" % e
