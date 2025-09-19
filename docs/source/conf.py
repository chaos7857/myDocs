import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Achao的文档库'
copyright = '2025, achao'
author = 'achao'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'sphinx.ext.duration', # 
    # 'sphinx.ext.doctest', # 尽可能保持文档和代码同步
    'sphinx.ext.autodoc', # 描述与代码本身不同步，因为函数签名不相同。此外，最好在文档中重用 Python 文档字符串，而不是必须在两个地方编写信息。
    'sphinx.ext.autosummary',# 再进一步偷懒
    'sphinx.ext.napoleon'  # 支持Google/NumPy风格（可选）
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
