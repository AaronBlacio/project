# ============================================
# 🚀 WSGI Configuration for PythonAnywhere
# ============================================
# This file contains the WSGI configuration required to serve your Django webapp.

import os
import sys
from pathlib import Path

# ============================================
# 📂 PROJECT PATHS
# ============================================
# IMPORTANT: Change 'xtaxx24' to your PythonAnywhere username
project_home = '/home/xtaxx24/project/Boceto'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ============================================
# 🔐 ENVIRONMENT VARIABLES (using decouple)
# ============================================
# python-decouple will automatically load from .env file in the project directory
# No need for python-dotenv

# ============================================
# 🎯 DJANGO CONFIGURATION
# ============================================
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Boceto.settings')

# ============================================
# 🌐 WSGI APPLICATION
# ============================================
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
