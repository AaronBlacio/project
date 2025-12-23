# ============================================
# 🚀 WSGI Configuration for PythonAnywhere
# ============================================
# This file contains the WSGI configuration required to serve your Django webapp.
# It works by setting the variable 'application' to a WSGI handler of some description.
#
# For PythonAnywhere, update the path to your project in the Web tab.

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# ============================================
# 📂 PROJECT PATHS
# ============================================
# Add your project directory to the sys.path
# IMPORTANT: Change 'yourusername' to your PythonAnywhere username

# For local development (Windows paths will be different)
project_home = Path(__file__).resolve().parent

# For PythonAnywhere, use:
# project_home = '/home/yourusername/project/Boceto'

if str(project_home) not in sys.path:
    sys.path.insert(0, str(project_home))

# ============================================
# 🔐 ENVIRONMENT VARIABLES
# ============================================
# Load environment variables from .env file
env_path = project_home / '.env'
if env_path.exists():
    load_dotenv(env_path)

# ============================================
# 🎯 DJANGO CONFIGURATION
# ============================================
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Boceto.settings')

# ============================================
# 🌐 WSGI APPLICATION
# ============================================
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
