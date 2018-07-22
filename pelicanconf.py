#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jeff S.'
SITENAME = 'Introducing Pelican Using Pelican'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican Docs', 'http://docs.getpelican.com/en/stable/'),
         ('Pelican Github Repo', 'https://github.com/getpelican/pelican'),
        ('Pelican Theme Repo', 'https://github.com/getpelican/pelican-themes'),
('Pelican Plugin Repo','https://github.com/getpelican/pelican-plugins'),
         ('Full Stack Python', 'https://www.fullstackpython.com/pelican.html'),
         )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#         ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
