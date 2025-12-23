---
description: Deploy automático a PythonAnywhere después de cada push a main
---

# 🚀 Workflow de Deploy a PythonAnywhere

Este workflow describe cómo funciona el deploy automático y cómo configurarlo.

## Requisitos Previos

1. Tener cuenta en PythonAnywhere
2. Tener el proyecto clonado en PythonAnywhere
3. Haber configurado los GitHub Secrets

## Configuración de GitHub Secrets

Ve a tu repositorio en GitHub → Settings → Secrets and variables → Actions

Agrega estos 3 secrets:

1. **PYTHONANYWHERE_API_TOKEN** - Obtén este token en: PythonAnywhere → Account → API Token
2. **PYTHONANYWHERE_USERNAME** - Tu nombre de usuario en PythonAnywhere
3. **PYTHONANYWHERE_DOMAIN** - Tu dominio (ej: `username.pythonanywhere.com`)

## Deploy Automático

El deploy se ejecuta automáticamente cuando:
- Se hace push a la rama `main`
- Se dispara manualmente desde Actions → Deploy to PythonAnywhere → Run workflow

## Deploy Manual en PythonAnywhere

Si necesitas hacer deploy manual, sigue estos pasos:

// turbo-all
1. Abre una consola Bash en PythonAnywhere
2. Ejecuta: `cd ~/project/Boceto`
3. Ejecuta: `bash deploy.sh`
4. Ve a la pestaña Web y haz clic en "Reload"

## Verificar el Deploy

1. Visita tu sitio: `https://username.pythonanywhere.com`
2. Verifica que los cambios estén aplicados
3. Revisa los logs si hay errores

## Archivos Relacionados

- `.github/workflows/deploy-pythonanywhere.yml` - Workflow de GitHub Actions
- `Boceto/deploy.sh` - Script de deploy manual
- `Boceto/.env.production.example` - Plantilla de variables de entorno
- `docs/DEPLOY_PYTHONANYWHERE.md` - Guía completa de deploy
