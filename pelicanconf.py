#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alex Ravenel'
SITENAME = u'Alex Ravenel'
SITEURL = 'http://alexravenel.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
          #('Python.org', 'http://python.org/'),
          #('Jinja2', 'http://jinja.pocoo.org/'),
          #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/aravenel'),
          ('github', 'https://github.com/aravenel'),
          ('linkedin', 'http://www.linkedin.com/profile/view?id=23712282'))

#MENUITEMS = (
    #('Home', SITEURL),
#)

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 30
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DISQUS_SITENAME = 'alexravenel'

THEME = 'themes/svbtle/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
