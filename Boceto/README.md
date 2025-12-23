# 🍌 Cooperativa Agrícola Oro Verde - Cooporoverde

Sistema web para la **Cooperativa de Producción Agrícola Oro Verde**, una organización de pequeños productores de banano orgánico ubicada en la zona sur de Ecuador.

![Django](https://img.shields.io/badge/Django-4.2.3-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Certificaciones](#-certificaciones)
- [Contribución](#-contribución)

---

## 🌟 Descripción

Este sistema web presenta la Cooperativa Agrícola Oro Verde, destacando:

- **Historia y misión** de la cooperativa
- **Certificaciones** de comercio justo y producción orgánica
- **Noticias y actualizaciones** para socios y público
- **Emprendimientos** como Bana Pan y Cooporoverdesa
- **Formulario de contacto** para comunicación directa

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| 🏠 **Página Principal** | Banner interactivo con información de la cooperativa |
| 📰 **Sistema de Noticias** | CRUD completo para publicar noticias con imágenes |
| 📧 **Formulario de Contacto** | Envío de correos con validación |
| 🔐 **Panel de Administración** | Interfaz Jazzmin personalizada |
| 📱 **Diseño Responsivo** | Adaptable a todos los dispositivos |

---

## 🛠 Tecnologías

- **Backend**: Django 4.2.3
- **Base de Datos**: MySQL 8.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Librerías**:
  - Pillow (manejo de imágenes)
  - django-jazzmin (panel admin personalizado)
  - python-decouple (variables de entorno)

---

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/cooporoverde.git
   cd cooporoverde/Boceto
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Copiar plantilla
   cp .env.example .env
   
   # Editar .env con tus credenciales
   ```

5. **Configurar base de datos**
   ```sql
   CREATE DATABASE Vinculacion CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

6. **Aplicar migraciones**
   ```bash
   python manage.py migrate
   ```

7. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

8. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

9. **Acceder al sitio**
   - Sitio web: http://localhost:8000
   - Panel admin: http://localhost:8000/admin

---

## ⚙️ Configuración

### Variables de Entorno (.env)

```env
# Django Settings
SECRET_KEY=tu-clave-secreta-muy-segura
DEBUG=True                              # False en producción
ALLOWED_HOSTS=localhost,127.0.0.1       # Agregar tu dominio en producción

# Database Settings
DB_NAME=Vinculacion
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_segura
DB_HOST=localhost
DB_PORT=3306

# Email Settings (Gmail)
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_app_password     # Usar App Password de Google
```

### Configurar Email con Gmail

1. Ir a [Configuración de Google](https://myaccount.google.com/security)
2. Activar verificación en 2 pasos
3. Generar una "Contraseña de aplicación"
4. Usar esa contraseña en `EMAIL_HOST_PASSWORD`

---

## 📁 Estructura del Proyecto

```
Boceto/
├── Boceto/                     # Configuración del proyecto Django
│   ├── settings.py             # Configuración principal
│   ├── urls.py                 # URLs raíz
│   ├── wsgi.py                 # Punto de entrada WSGI
│   └── asgi.py                 # Punto de entrada ASGI
│
├── BocetoApp/                  # Aplicación principal
│   ├── models.py               # Modelos (Post)
│   ├── views.py                # Vistas
│   ├── urls.py                 # URLs de la app
│   ├── admin.py                # Configuración del admin
│   ├── templates/boceto/       # Templates HTML
│   └── static/boceto/          # Archivos estáticos (CSS, JS, imágenes)
│
├── media/                      # Archivos subidos por usuarios
├── .env                        # Variables de entorno (no subir a Git)
├── .env.example                # Plantilla de variables
├── .gitignore                  # Archivos ignorados por Git
├── requirements.txt            # Dependencias de Python
├── manage.py                   # CLI de Django
└── README.md                   # Este archivo
```

---

## 🏆 Certificaciones

La Cooperativa Oro Verde cuenta con las siguientes certificaciones:

| Certificación | Descripción |
|---------------|-------------|
| 🌍 **Fair Trade** | Comercio justo y precios equitativos |
| 🌱 **Orgánica** | Producción sin químicos sintéticos |
| 🌿 **Global Gap** | Buenas prácticas agrícolas |
| 🏭 **BPM** | Buenas Prácticas de Manufactura |
| ✅ **Control Union** | Certificación de sostenibilidad |

---

## 👥 Contribución

1. Fork del repositorio
2. Crear rama de feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit de cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Contacto

- **Sitio Web**: [cooporoverde.com](https://cooporoverde.com)
- **Facebook**: [@cooporoverde](https://www.facebook.com/profile.php?id=100088843867191)
- **Instagram**: [@cooporoverde](https://www.instagram.com/cooporoverde/)

---

Desarrollado con ❤️ para la Cooperativa Agrícola Oro Verde 🍌
