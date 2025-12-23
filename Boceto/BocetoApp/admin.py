from django.contrib import admin
from .models import Post, Cotizacion, Testimonial


# ============================================
# 📰 ADMIN PARA POSTS
# ============================================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'created', 'updated')
    list_filter = ('autor', 'created')
    search_fields = ('titulo', 'contenido')
    exclude = ('created', 'updated')
    date_hierarchy = 'created'


# ============================================
# 📋 ADMIN PARA COTIZACIONES
# ============================================
@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'pais', 'email', 'cantidad', 'created', 'atendida')
    list_filter = ('pais', 'atendida', 'created')
    search_fields = ('nombre', 'empresa', 'email')
    list_editable = ('atendida',)
    readonly_fields = ('created',)
    date_hierarchy = 'created'
    
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('nombre', 'empresa', 'email', 'telefono', 'pais')
        }),
        ('Detalles de la Cotización', {
            'fields': ('cantidad', 'mensaje')
        }),
        ('Estado', {
            'fields': ('atendida', 'created')
        }),
    )


# ============================================
# ⭐ ADMIN PARA TESTIMONIALES
# ============================================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'pais', 'rating', 'activo', 'created')
    list_filter = ('pais', 'rating', 'activo')
    search_fields = ('nombre', 'empresa', 'testimonio')
    list_editable = ('activo', 'rating')
    readonly_fields = ('created',)