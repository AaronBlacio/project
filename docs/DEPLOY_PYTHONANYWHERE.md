# 🚀 Guía de Deploy en PythonAnywhere

Esta guía explica cómo desplegar **Cooporoverde** en PythonAnywhere con deploy automático desde GitHub.

## 📋 Pre-requisitos

1. Cuenta en [PythonAnywhere](https://www.pythonanywhere.com) (cuenta gratuita o de pago)
2. Repositorio en GitHub configurado
3. API Token de PythonAnywhere

---

## 🔧 Paso 1: Configuración Inicial en PythonAnywhere

### 1.1 Clonar el Repositorio

Abre una consola Bash en PythonAnywhere y ejecuta:

```bash
cd ~
git clone https://github.com/AaronBlacio/project.git
cd project/Boceto
```

### 1.2 Crear Entorno Virtual

```bash
mkvirtualenv --python=/usr/bin/python3.10 cooporoverde
workon cooporoverde
pip install -r requirements.txt
```

### 1.3 Crear Base de Datos MySQL

1. Ve a la pestaña **Databases** en PythonAnywhere
2. Crea una base de datos MySQL (ej: `yourusername$cooporoverde`)
3. Anota la contraseña y el host

### 1.4 Configurar Variables de Entorno

Crea el archivo `.env` en el directorio `~/project/Boceto/`:

```bash
nano ~/project/Boceto/.env
```

Contenido (cambia los valores):

```env
SECRET_KEY=tu-clave-secreta-muy-larga-y-compleja
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com

CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com

DB_NAME=yourusername$cooporoverde
DB_USER=yourusername
DB_PASSWORD=tu-contraseña-mysql
DB_HOST=yourusername.mysql.pythonanywhere-services.com
DB_PORT=3306

EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
```

### 1.5 Ejecutar Migraciones

```bash
cd ~/project/Boceto
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

## 🌐 Paso 2: Configurar Web App

### 2.1 Crear Web App

1. Ve a la pestaña **Web** en PythonAnywhere
2. Click en **Add a new web app**
3. Selecciona **Manual configuration** (NOT Django)
4. Selecciona **Python 3.10**

### 2.2 Configurar WSGI

Edita el archivo WSGI (click en el enlace del WSGI file):

```python
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add your project directory to the sys.path
project_home = '/home/yourusername/project/Boceto'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables
env_path = Path(project_home) / '.env'
load_dotenv(env_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Boceto.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 2.3 Configurar Archivos Estáticos

En la sección **Static files**:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/project/Boceto/staticfiles` |
| `/media/` | `/home/yourusername/project/Boceto/media` |

### 2.4 Configurar Virtualenv

En el campo **Virtualenv**, ingresa:

```
/home/yourusername/.virtualenvs/cooporoverde
```

### 2.5 Recargar la App

Click en el botón **Reload** ✅

---

## 🔄 Paso 3: Deploy Automático con GitHub Actions

### 3.1 Obtener API Token de PythonAnywhere

1. Ve a **Account** → **API Token** en PythonAnywhere
2. Copia tu token

### 3.2 Configurar Secrets en GitHub

En tu repositorio de GitHub, ve a **Settings** → **Secrets and variables** → **Actions**

Agrega estos secrets:

| Secret Name | Value |
|-------------|-------|
| `PYTHONANYWHERE_API_TOKEN` | Tu API token |
| `PYTHONANYWHERE_USERNAME` | Tu username de PythonAnywhere |
| `PYTHONANYWHERE_DOMAIN` | `yourusername.pythonanywhere.com` |

### 3.3 ¡Listo!

Ahora cada vez que hagas `git push` a la rama `main`, el workflow:

1. ✅ Hará `git pull` en PythonAnywhere
2. ✅ Instalará dependencias
3. ✅ Ejecutará `collectstatic`
4. ✅ Ejecutará migraciones
5. ✅ Recargará la web app

---

## 📝 Deploy Manual (Alternativa)

Si necesitas hacer deploy manual, ejecuta en la consola de PythonAnywhere:

```bash
cd ~/project/Boceto
bash deploy.sh
```

Luego ve a la pestaña **Web** y haz click en **Reload**.

---

## 🔍 Solución de Problemas

### Error 502 Bad Gateway
- Revisa el archivo de log de errores en la pestaña Web
- Verifica que el WSGI esté correctamente configurado

### Static files no cargan
- Asegúrate de haber ejecutado `collectstatic`
- Verifica las rutas en Static files

### Database connection error
- Verifica las credenciales en `.env`
- Asegúrate de que la base de datos esté creada

### ImportError
- Verifica que el virtualenv esté configurado
- Ejecuta `pip install -r requirements.txt`

---

## 📞 Soporte

Si tienes problemas, revisa:
- 📚 [Documentación de PythonAnywhere](https://help.pythonanywhere.com/)
- 🐛 Logs de error en la pestaña Web
- 💬 Foros de PythonAnywhere

---

¡Happy deploying! 🚀
