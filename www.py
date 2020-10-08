# -*- coding: utf-8 -*-

"""Open an url in default browser."""

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Open URL"
__version__ = "1.0.2"
__trigger__ = "www"
__author__ = "Arnaud Locquet"
__dependencies__ = []

iconPath = iconLookup('www')

def handleQuery(query):
	if not query.isTriggered:
		return
	results = []
	results.append(
		Item(
			id=__prettyname__,
	        icon=iconPath,
	        text="-> https://" + query.string.strip(),
	        subtext="Open URL in browser",
	        completion=query.rawString,
	        actions=[
	            UrlAction("Open", "https://" + query.string.strip())
	        ]
        )
    )
	return results
