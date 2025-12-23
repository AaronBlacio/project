#!/bin/bash
# ============================================
# 🚀 Manual Deploy Script for PythonAnywhere
# ============================================
# Run this script from the PythonAnywhere console
# Usage: bash deploy.sh

echo "============================================"
echo "🚀 Deploying Cooporoverde to PythonAnywhere"
echo "============================================"

# Navigate to project directory
cd ~/project/Boceto || { echo "❌ Project directory not found"; exit 1; }

echo ""
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

echo ""
echo "📦 Installing/updating dependencies..."
pip install -r requirements.txt --user

echo ""
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

echo ""
echo "============================================"
echo "✅ Deployment completed!"
echo "============================================"
echo ""
echo "📌 Next steps:"
echo "   1. Go to the Web tab in PythonAnywhere"
echo "   2. Click the 'Reload' button for your web app"
echo "   3. Visit your site to verify the deployment"
echo ""
