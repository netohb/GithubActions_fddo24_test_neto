import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Ruta al código fuente

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

# Configuración general
project = 'Documentación'
author = 'Alberto'
release = '1.0'
language = 'es'

# Tema de la documentación
html_theme = 'alabaster'
