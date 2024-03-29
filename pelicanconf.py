AUTHOR = 'Me as Authors'
SITENAME = "My Blog's Jupyter Python"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
IPYNB_USE_METACELL = True

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup

PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]

THEME='pelican-themes/Casper2Pelican'