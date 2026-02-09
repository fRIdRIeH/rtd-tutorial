# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'fRIdRIeH Test'
copyright = '2026, Vladislav Valiullin'
author = 'Vladislav'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.numfig',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

numfig = True
numfig_secnum_depth = 2
numfig_format = {
    'figure': 'Рисунок %s',
    'table': 'Таблица %s', 
    'code-block': 'Листинг %s',
    'section': 'Раздел %s',
}

# Дополнительные настройки
numfig_prefix = {
    'figure': 'рис.',
    'table': 'табл.',
}
numfig_start_from = 1
