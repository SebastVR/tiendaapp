from django.contrib import admin

# Register your models here.
from .models import Marca, Producto


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "referencia"]
    list_display_links = ["nombre", "referencia"]
    search_fields = ["nombre", "referencia"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "talla",
        "marca",
        "cantidad_inventario",
        "fecha_embarque",
    ]
    list_display_links = [
        "nombre",
        "talla",
        "marca",
        "cantidad_inventario",
        "fecha_embarque",
    ]

    list_filter = ["marca", "talla"]
    search_fields = ["nombre", "marca__nombre"]
    # date_hierarchy = "fecha_embarque"
