#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alex Ravenel'
SITENAME = u'Alex Ravenel'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
          #('Python.org', 'http://python.org/'),
          #('Jinja2', 'http://jinja.pocoo.org/'),
          #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter: @aravenel', 'http://www.twitter.com/aravenel'),)

MENUITEMS = (
    ('Home', SITEURL),
)

DEFAULT_PAGINATION = 5

THEME = 'themes/tuxlite_zf'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
