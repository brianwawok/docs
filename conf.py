# -*- coding: utf-8 -*-
#
# MongoDB documentation build configuration file, created by
# sphinx-quickstart on Mon Oct  3 09:58:40 2011.
#
# This file is execfile()d with the current directory set to its containing dir.

import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "bin")))

import mongodb_docs_meta

meta = {
    'branch': mongodb_docs_meta.get_branch(),
    'commit': mongodb_docs_meta.get_commit(),
    'manual_path': mongodb_docs_meta.get_manual_path(),
    'date': str(datetime.date.today().year),
}

# -- General configuration ----------------------------------------------------

needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'mongodb_domain',
    'additional_directives',
    'aggregation_domain',
]

templates_path = ['.templates']
exclude_patterns = []

source_suffix = '.txt'

master_doc = 'contents'
project = u'MongoDB Manual'
copyright = u'2011-' + meta['date'] + ', 10gen, Inc.'
version = '2.2.2'
release = version

BREAK = '\n'
rst_epilog = ('.. |branch| replace:: ``' + meta['branch'] + '``' + BREAK +
              '.. |copy| unicode:: U+000A9' + BREAK +
              '.. |year| replace:: ' + meta['date'] + BREAK +
              '.. |hardlink| replace:: http://docs.mongodb.org/' + meta['branch'])

pygments_style = 'sphinx'

extlinks = {
    'issue': ('https://jira.mongodb.org/browse/%s', '' ),
    'wiki': ('http://www.mongodb.org/display/DOCS/%s', ''),
    'api': ('http://api.mongodb.org/%s', ''),
    'source': ('https://github.com/mongodb/mongo/blob/master/%s', ''),
    'docsgithub' : ( 'http://github.com/mongodb/docs/blob/' + meta['branch'] + '/%s', ''),
    'hardlink' : ( 'http://docs.mongodb.org/' + meta['branch'] + '/%s', '')
}

intersphinx_mapping = {
        'pymongo': ('http://api.mongodb.org/python/current/', None),
        'python' : ('http://docs.python.org/', None),
        'django': ('https://django.readthedocs.org/en/latest/', None),
        'djangomongodbengine': ('http://django-mongodb.org/', None),
        'djangotoolbox' : ('http://djangotoolbox.readthedocs.org/en/latest/', None),
}

# -- Options for HTML output ---------------------------------------------------

html_theme = 'mongodb'
html_theme_path = ['themes']
html_title = project
htmlhelp_basename = 'MongoDBdoc'

html_logo = ".static/logo-mongodb.png"
html_static_path = ['source/.static']

html_copy_source = False
html_use_smartypants = True
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

manual_edition_path = 'http://docs.mongodb.org/' + meta['branch'] + '/MongoDB-Manual-' + meta['branch']

html_theme_options = {
    'branch': meta['branch'],
    'pdfpath': manual_edition_path + '.pdf',
    'epubpath': manual_edition_path + '.epub',
    'manual_path': meta['manual_path'],
    'repo_name': 'docs',
    'jira_project': 'DOCS',
    'google_analytics': 'UA-7301842-8',
    'is_manual': True,
    'project': 'manual',
}

html_sidebars = {
    '**': ['pagenav.html', 'wikisidebar.html'],
}

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
#   (source start file, target name, title, author, documentclass [howto/manual]).
    ('contents', 'MongoDB.tex', u'MongoDB Documentation', u'MongoDB Documentation Project', 'manual'),
    ('meta/use-cases', 'MongoDB-use-cases.tex', u'MongoDB Use Cases', u'MongoDB Documentation Project', 'howto'),
    ('meta/reference', 'MongoDB-reference.tex', u'MongoDB Reference Manual', u'MongoDB Documentation Project', 'manual'),
    ('crud', 'MongoDB-crud.tex', u'MongoDB CRUD Operations Introduction', u'MongoDB Documentation Project', 'manual'),
]

latex_elements = {
    'preamble': '\DeclareUnicodeCharacter{FF04}{\$} \DeclareUnicodeCharacter{FF0E}{.}',
    'pointsize': '10pt',
    'papersize': 'letterpaper'
}

latex_use_parts = True
latex_show_pagerefs = True
latex_show_urls = False
latex_domain_indices = True
latex_logo = None
latex_appendices = []

# -- Options for manual page output --------------------------------------------

man_pages = [
  # (source start file, name, description, authors, manual section).
    ('reference/bsondump', 'bsondump', u'MongoDB BSON utility', [u'MongoDB Documentation Project'], 1),
    ('reference/mongo', 'mongo', u'MongoDB Shell', [u'MongoDB Documentation Project'], 1),
    ('reference/mongod', 'mongod', u'MongoDB Server', [u'MongoDB Documentation Project'], 1),
    ('reference/mongos', 'mongos', u'MongoDB Shard Utility', [u'MongoDB Documentation Project'], 1),
    ('reference/mongodump', 'mongodump', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongoexport', 'mongoexport', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongofiles', 'mongofiles', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongoimport', 'mongoimport', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongooplog', 'mongooplog', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongorestore', 'mongorestore', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongostat', 'mongostat', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongosniff', 'mongosniff', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongotop', 'mongotop', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/configuration-options', 'mongodb-config', u'MongoDB', [u'MongoDB Documentation Project'], 1),
]

texinfo_documents = [
    ('contents', 'mongodb-manual', 'MongoDB Manual', '10gen, Inc.', 'mongodb', 'MongoDB Manual', 'Database', True),
    ('meta/reference', 'mongodb-reference', 'MongoDB Reference Manual', '10gen, Inc.', 'mongodb', 'Reference Material for MongoDB', 'Database', False),
    ('crud', 'mongodb-crud', 'MongoDB Crud Guide', '10gen, Inc.', 'mongodb', 'CRUD Operation Guide for MongoDB', 'Database', False),
]

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'MongoDB'
epub_author = u'MongoDB Documentation Project'
epub_publisher = u'MongoDB Documentation Project'
epub_copyright = u'2011-' + meta['date'] + ', 10gen Inc.'
epub_theme = 'epub_mongodb'
epub_tocdup = True
epub_tocdepth = 3
epub_language = 'en'
epub_scheme = 'url'
epub_identifier = 'http://docs.mongodb.org/' + meta['branch']
epub_exclude_files = []

epub_pre_files = []
epub_post_files = []
