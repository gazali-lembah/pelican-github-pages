AUTHOR = 'Gazali'
SITENAME = "Gazali's Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Google Scholar', 'https://scholar.google.com/citations?user=cOyX2XYAAAAJ&hl=en'),
         ('SINTA id:6681756', 'https://sinta.kemdikbud.go.id/authors/profile/6681756'),
         ('Orcid id:0000-0001-7535-1057', 'https://gazali-lembah.github.io/website.github.io/#'),
         ('Universitas Tadulako', 'https://bahasaindonesia.fkip.untad.ac.id/'),)

# Social widget
SOCIAL = (('twitter', '#'),
          ('linkedin', 'http://www.linkedin.com/in/danieldebie'),
          ('github', 'http://github.com/DandyDev'),
          ('stackoverflow', '#', 'stack-overflow'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/pelican-bootstrap3"


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = False
USE_PAGER = True