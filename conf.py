# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
from typing import List
from importlib import import_module
from jinja2.filters import FILTERS

from datetime import date

project = 'Lorenzo Bonicelli'
author = 'loribonna'
copyright = f'{date.today().year}, {author}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              #   'sphinx.ext.autosummary',
              'sphinx.ext.napoleon',
              #   'sphinx.ext.viewcode',
              'sphinx_tabs.tabs',
              'sphinx-prompt',
              'sphinx_toolbox',
              'sphinx.ext.autosectionlabel']

github_username = 'loribonna'
github_repository = 'loribonna'

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3', None),
#     'torch': ('https://pytorch.org/docs/master/', None),
#     'torchvision': ('https://pytorch.org/docs/master/', None),
#     'numpy': ('https://numpy.org/doc/stable/', None),
# }

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpicky
# This generates a lot of warnings because of the broken internal links, which
# makes the docs build fail because of the "fail_on_warning: true" option in
# the .readthedocs.yml config file
# nitpicky = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "insegel"
html_title = "Lorenzo Bonicelli"
html_static_path = ['_static']
html_favicon = 'images/logo.png'

# autosummary_generate = True
# numpydoc_show_class_members = False

# Disable docstring inheritance
# autodoc_inherit_docstrings = False

# Show type hints in the description
# autodoc_typehints = "description"

# Add parameter types if the parameter is documented in the docstring
# autodoc_typehints_description_target = "documented_params"
