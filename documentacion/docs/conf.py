# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Calculator Documentation'
author = 'Alberto Marquez'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Genera documentación desde docstrings
    'sphinx.ext.napoleon',       # Soporta formatos Google y NumPy para docstrings
    'sphinx.ext.viewcode',       # Muestra el código fuente vinculado en la documentación
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Tema Read the Docs (popular y profesional)
html_static_path = ['_static']

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../'))  # Ruta al proyecto principal
