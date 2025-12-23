"""
Script para poblar la base de datos con noticias de ejemplo.
Ejecutar con: python manage.py shell < BocetoApp/fixtures/create_news.py
"""
from django.contrib.auth.models import User
from BocetoApp.models import Post

# Obtener o crear usuario admin
try:
    admin_user = User.objects.get(username='admin')
except User.DoesNotExist:
    admin_user = User.objects.create_superuser('admin', 'admin@cooporoverde.com', 'admin123')
    print("Usuario admin creado")

# Lista de noticias de ejemplo
noticias = [
    {
        'titulo': '🎉 Cooporoverde Renueva Certificación Fair Trade para 2024-2025',
        'contenido': """
Nos complace anunciar que la Cooperativa Agrícola Oro Verde ha renovado exitosamente su certificación Fair Trade (Comercio Justo) para el período 2024-2025.

Esta renovación representa nuestro compromiso continuo con los principios del comercio justo:

**Prácticas Verificadas:**
- ✅ Salarios justos para todos nuestros trabajadores
- ✅ Condiciones laborales seguras y dignas
- ✅ Protección del medio ambiente
- ✅ Transparencia en todas nuestras operaciones
- ✅ Inversión en proyectos comunitarios

La auditoría fue realizada por organismos internacionales independientes que verificaron el cumplimiento de todos los estándares requeridos.

Agradecemos a todos nuestros socios, trabajadores y clientes europeos que confían en nuestro banano orgánico certificado.

¡Seguimos trabajando para llevar lo mejor de Ecuador al mundo!
        """.strip()
    },
    {
        'titulo': '🌱 Nueva Cosecha de Banano Orgánico Premium Lista para Exportación',
        'contenido': """
La temporada 2024 nos trae una cosecha excepcional de banano orgánico Cavendish, lista para ser exportada a nuestros mercados en Europa.

**Características de esta cosecha:**
- 🍌 Bananos de calibre premium (19-23cm)
- 🌿 100% orgánicos, sin químicos sintéticos
- ☀️ Madurados naturalmente bajo el sol ecuatoriano
- 📦 Empaque sostenible y trazabilidad completa

**Destinos confirmados:**
- 🇩🇪 Alemania - BioFrisch GmbH
- 🇮🇹 Italia - Frutti Biologici S.r.l.
- 🇫🇷 Francia - FruitsBio France

Nuestros 14 productores orgánicos certificados han trabajado arduamente para garantizar la calidad que nos caracteriza.

Si estás interesado en importar nuestro banano premium, contáctanos para una cotización personalizada.
        """.strip()
    },
    {
        'titulo': '🏫 Programa de Becas Educativas 2024: Beneficiando a 15 Estudiantes',
        'contenido': """
Como parte de nuestro compromiso con el desarrollo comunitario, el programa de becas educativas 2024 de Cooporoverde beneficia a 15 estudiantes este año.

**Detalles del Programa:**
Los fondos provienen de la prima Fair Trade y están destinados a hijos de trabajadores y socios de nuestra cooperativa.

**Beneficios incluidos:**
- 📚 Materiales escolares completos
- 🎒 Uniformes y útiles
- 💻 Apoyo con tecnología para estudios
- 🚌 Subsidio de transporte escolar

**Testimonios:**
> "Gracias a la beca de Cooporoverde, mi hija puede continuar sus estudios universitarios" - María García, trabajadora de empaque

Este programa demuestra que el comercio justo va más allá del comercio: es una inversión en el futuro de nuestras comunidades.

¡Felicitamos a todos los becarios de este año!
        """.strip()
    },
    {
        'titulo': '🥇 Oro Verde Recibe Reconocimiento por Buenas Prácticas Agrícolas',
        'contenido': """
La Cooperativa Agrícola Oro Verde ha recibido un reconocimiento especial del Ministerio de Agricultura de Ecuador por la implementación de Buenas Prácticas Agrícolas (BPA).

**Criterios evaluados:**
- 🌍 Sostenibilidad ambiental
- 👷 Seguridad laboral
- 📊 Trazabilidad del producto
- 💧 Uso responsable del agua
- 🐝 Protección de la biodiversidad

**Logros destacados:**
- Reducción del 40% en uso de agua mediante sistemas de riego eficientes
- Implementación de corredores biológicos para fauna local
- Capacitación continua a todos los trabajadores
- Sistema de trazabilidad digital desde la finca hasta el puerto

Este reconocimiento valida nuestro compromiso con la producción responsable y sostenible.

¡Gracias a todo el equipo que hace esto posible!
        """.strip()
    },
    {
        'titulo': '🤝 Alianza Estratégica con Nuevo Importador en Países Bajos',
        'contenido': """
Nos complace anunciar una nueva alianza comercial con NatureFruits BV, uno de los principales distribuidores de productos orgánicos en los Países Bajos.

**Detalles de la alianza:**
Esta asociación estratégica nos permite expandir nuestra presencia en el mercado europeo, llegando ahora a 4 países con nuestro banano orgánico premium.

**Mercados actuales:**
- 🇩🇪 Alemania (desde 2019)
- 🇮🇹 Italia (desde 2020)
- 🇫🇷 Francia (desde 2021)
- 🇳🇱 Países Bajos (2024 - ¡NUEVO!)

**Impacto esperado:**
- Incremento del 25% en volumen de exportación
- Nuevas oportunidades para nuestros productores
- Mayor reconocimiento de la marca Cooporoverde en Europa

Agradecemos a NatureFruits BV por confiar en la calidad de nuestro banano ecuatoriano.

¡Continuamos creciendo juntos!
        """.strip()
    },
]

# Crear las noticias
for noticia_data in noticias:
    post, created = Post.objects.get_or_create(
        titulo=noticia_data['titulo'],
        defaults={
            'contenido': noticia_data['contenido'],
            'autor': admin_user
        }
    )
    if created:
        print(f"✅ Creada: {noticia_data['titulo'][:50]}...")
    else:
        print(f"⏭️ Ya existe: {noticia_data['titulo'][:50]}...")

print(f"\n📰 Total de noticias en base de datos: {Post.objects.count()}")
