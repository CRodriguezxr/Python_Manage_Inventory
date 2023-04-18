from django.db import models

class Producto(models.Model):
    CLASE_CHOICES = (
        ('CMP', 'Camperas'),
        ('BZS', 'Buzos'),
        ('REM', 'Remeras'),
        ('RPI', 'Ropa interior'),
        ('CLZ', 'Calzado'),
    )
    codigo = models.CharField(max_length=6, unique=True, help_text="Deben ser 3 letras mayusculas seguidas de 3 numeros")
    clase = models.CharField(max_length=3, choices=CLASE_CHOICES)
    color = models.CharField(max_length=50)
    talle = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.codigo

class Transaccion(models.Model):
    TIPO_CHOICES = (
        ('C', 'Compra'),
        ('V', 'Venta'),
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} de {self.cantidad} {self.producto.codigo} el {self.fecha}"
