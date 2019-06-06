from django.contrib import admin
from .models import *

# Register your models here.
class AdminProducto(admin.ModelAdmin):
    list_display = ["codigo", "descripcion"]
    list_filter = ["codigo", "id_categoria_id"]
    search_fields = ["codigo", "id_categoria_id"]

    class Meta:
        model = Producto


class AdminCategoria(admin.ModelAdmin):
    list_display = ["nombre"]
    list_filter = ["nombre"]
    search_fields = ["nombre"]

    class Meta:
        model = Categoria




admin.site.register(Producto, AdminProducto)
admin.site.register(Categoria, AdminCategoria)