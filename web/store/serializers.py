from rest_framework import serializers
from .models import Marca, Producto


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = [
            "id",
            "nombre",
            "referencia",
        ]


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "talla",
            "observaciones",
            "marca",
            "cantidad_inventario",
            "fecha_embarque",
        ]
