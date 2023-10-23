from django.db import models

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=10)

class Productos(models.Model):
    T1 = models.FloatField(null=True)
    TIPO = models.CharField(max_length=20)
    T2 = models.FloatField(null = True)
    T3 = models.CharField(max_length=10)
    CANT = models.IntegerField(null=True)
    T4 = models.FloatField(null=True)
    KG_UN = models.CharField(max_length=10)
    WRIN= models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=60)
    CJ = models.FloatField(null=True)
    BOLSA = models.FloatField(null=True)
    KG_PZ = models.FloatField(null=True)
    TOTAL = models.FloatField(null=True)
    ENVIAR = models.IntegerField(null=True)
    LIMIT = models.IntegerField(null=True)
    ACCESIBLE_CHOICES = (
        (1, 'Sí'),
        (0, 'No'),
    )
    ACCESIBLE = models.IntegerField(choices=ACCESIBLE_CHOICES, default=1)
    PEDIDO_ANTERIOR = models.IntegerField(null=True)
    PROM_MENSUAL = models.FloatField(null=True)

class Pedidos(models.Model):
    WRIN= models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=60)
    ENVIAR = models.IntegerField()
    NO_PEDIDO = models.IntegerField(default=1)


class Productos_4C(models.Model):
    T1 = models.FloatField(null=True)
    TIPO = models.CharField(max_length=20)
    T2 = models.FloatField(null=True)
    T3 = models.CharField(max_length=10)
    CANT = models.IntegerField(null=True)
    T4 = models.FloatField(null=True)
    KG_UN = models.CharField(max_length=10)
    WRIN = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=60)
    CJ = models.FloatField(null=True)
    BOLSA = models.FloatField(null=True)
    KG_PZ = models.FloatField(null=True)
    TOTAL = models.FloatField(null=True)
    ENVIAR = models.IntegerField(null=True)
    LIMIT = models.IntegerField(null=True)
    ACCESIBLE_CHOICES = (
        (1, 'Sí'),
        (0, 'No'),
    )
    ACCESIBLE = models.IntegerField(choices=ACCESIBLE_CHOICES, default=1)
    PEDIDO_ANTERIOR = models.IntegerField(null=True)
    PROM_MENSUAL = models.FloatField(null=True)

class Pedidos_4C(models.Model):
    WRIN = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=60)
    ENVIAR = models.IntegerField()
    NO_PEDIDO = models.IntegerField(default=1)

class Auditorias_HEB(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.FloatField()
    DIA_ACTUAL = models.FloatField()
    CAJAS = models.IntegerField(null=True)
    COMPRAS = models.FloatField(null=True)
    ENTRADA = models.FloatField(null=True)
    SALIDA = models.FloatField(null=True)
    MERMAS = models.FloatField(null=True)
    CONSUMO_DIARIO = models.FloatField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Registro_Auditorias_HEB(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.FloatField()
    DIA_ACTUAL = models.FloatField()
    CAJAS = models.IntegerField(null=True)
    COMPRAS = models.FloatField(null=True)
    ENTRADA = models.FloatField(null=True)
    SALIDA = models.FloatField(null=True)
    MERMAS = models.FloatField(null=True)
    CONSUMO_DIARIO = models.FloatField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Auditorias_HEB_Bebidas(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.IntegerField()
    DIA_ACTUAL = models.IntegerField()
    COMPRAS = models.IntegerField(null=True)
    ENTRADA = models.IntegerField(null=True)
    SALIDA = models.IntegerField(null=True)
    CONSUMO_DIARIO = models.IntegerField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Registro_Auditorias_HEB_Bebidas(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.IntegerField()
    DIA_ACTUAL = models.IntegerField()
    COMPRAS = models.IntegerField(null=True)
    ENTRADA = models.IntegerField(null=True)
    SALIDA = models.IntegerField(null=True)
    CONSUMO_DIARIO = models.IntegerField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Auditorias_4C(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.FloatField()
    DIA_ACTUAL = models.FloatField()
    CAJAS = models.IntegerField(null=True)
    COMPRAS = models.FloatField(null=True)
    ENTRADA = models.FloatField(null=True)
    SALIDA = models.FloatField(null=True)
    MERMAS = models.FloatField(null=True)
    CONSUMO_DIARIO = models.FloatField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Registro_Auditorias_4C(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.FloatField()
    DIA_ACTUAL = models.FloatField()
    CAJAS = models.IntegerField(null=True)
    COMPRAS = models.FloatField(null=True)
    ENTRADA = models.FloatField(null=True)
    SALIDA = models.FloatField(null=True)
    MERMAS = models.FloatField(null=True)
    CONSUMO_DIARIO = models.FloatField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Auditorias_4C_Bebidas(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.IntegerField()
    DIA_ACTUAL = models.IntegerField()
    COMPRAS = models.IntegerField(null=True)
    ENTRADA = models.IntegerField(null=True)
    SALIDA = models.IntegerField(null=True)
    CONSUMO_DIARIO = models.IntegerField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()

class Registro_Auditorias_4C_Bebidas(models.Model):
    DESCRIPCION =models.CharField(max_length= 60)
    MEDIDA = models.CharField(max_length=20)
    DIA_ANTERIOR = models.IntegerField()
    DIA_ACTUAL = models.IntegerField()
    COMPRAS = models.IntegerField(null=True)
    ENTRADA = models.IntegerField(null=True)
    SALIDA = models.IntegerField(null=True)
    CONSUMO_DIARIO = models.IntegerField()
    DIA_SEMANAL = models.CharField(max_length=10)
    DIA = models.IntegerField()
    MES = models.CharField(max_length=15)
    AÑO = models.IntegerField()



    
    



