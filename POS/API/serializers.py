from rest_framework import serializers

from .models import Categoria,Producto,Cliente


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation ['image'] = instance.image.url
        return representation
    

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


""" Serializers de tablas relacionadas """

class CategoriaProductoSerializer(serializers.ModelSerializer):
    Productos = ProductoSerializer(many=True, read_only=True)
    class Meta:
        model = Categoria
    