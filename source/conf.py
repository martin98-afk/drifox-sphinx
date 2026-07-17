# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'DriFox'
copyright = '2025~2026, Martin98-afk'
author = 'Martin98-afk'
release = '0.4.1'

# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

import os
import sys

base_path = os.path.abspath('.')
root_path = os.path.split(base_path)[0]
sys.path.insert(0, root_path)

sys.path.insert(0, os.path.abspath('_themes'))

from sphinxawesome_theme.postprocess import Icons

# -- Suppress warnings --------------------------------------------------

autosectionlabel_prefix_document = True   # 自动添加文档前缀，避免跨文档标签冲突

suppress_warnings = [
    'autosectionlabel.*',                # 允许跨页面相同节标题（前缀后仍可能冲突）
]

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxawesome_theme',
]

intersphinx_mapping = {
    'PyQt5': ('https://www.riverbankcomputing.com/static/Docs/PyQt5/', None),
}

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': False,
}

autosummary_generate = True
autosummary_generate_option = True

rst_prolog = '''
.. |version_str| replace:: v{0}
'''.format(release)

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'zh_CN'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_themes']
pygments_style = 'monokai'

# -- Options for HTML output -------------------------------------------------

html_favicon = '_images/drifox.ico'
html_logo = '_images/drifox.png'
html_theme = 'sphinxawesome_theme'
html_theme_path = ['_themes']
html_show_sourcelink = False
html_show_sphinx = False
html_title = 'DriFox'
html_permalinks_icon = (
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'height="1em" width="1em" viewBox="0 0 24 24"'
    '>'
    '<path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 '
    '5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 '
    '0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/>'
    '</svg>'
)

html_context = {
    'display_github': True,
    'github_user': 'martin98-afk',
    'github_repo': 'DriFox',
    'github_version': 'develop',
    'conf_py_path': '/docs/',
    'source_suffix': '.rst',
}

html_theme_options = {
    'show_scrolltop': True,
    'show_prev_next': True,
    'awesome_external_links': True,
    'extra_header_link_icons': {
        "GitHub Repository": {
            "link": "https://github.com/martin98-afk/DriFox",
            "icon": (
                '<svg height="26px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" '
                'fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                "14.853 20.608 1.087.2 1.483-.47 1.483-1.047 "
                "0-.516-.019-1.881-.03-3.693-6.04 "
                "1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 "  # noqa
                "2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 "
                "1.803.197-1.403.759-2.36 "
                "1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 "
                "0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 "
                "1.822-.584 5.972 2.226 "
                "1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 "
                "4.147-2.81 5.967-2.226 "
                "5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 "
                "2.232 5.828 0 "
                "8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 "
                "2.904-.027 5.247-.027 "
                "5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 "
                '22.647c0-11.996-9.726-21.72-21.722-21.72" '
                'fill="currentColor"/></svg>'
            ),
        }
    }
}

html_static_path = ['_static', '_images']
html_css_files = ['custom.css']

html_sidebars = {
    '**': [
        'sidebar_main_nav_links.html',
        'sidebar_toc.html'
    ]
}

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'DriFoxdoc'

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'DriFox', 'DriFox Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc,
     'DriFox', 'DriFox Documentation',
     author,
     'DriFox',
     'DriFox — 一个轻量化 AI 桌面对话助手',
     'Miscellaneous'),
]

# -- Options for autodoc ----------------------------------------------------

autodoc_member_order = 'groupwise'

# -- Options for image link -------------------------------------------------

html_scaled_image_link = False
