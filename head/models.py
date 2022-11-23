from django.db import models

# Create your models here.
class TipoDeImposto(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Estado(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Servicos(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class especificoTDP(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Produtos(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Categorias(models.Model):
    categoriaImposto = models.ForeignKey(TipoDeImposto, on_delete=models.CASCADE)
    categoriaEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    categoriaServicos = models.ForeignKey(Servicos,on_delete=models.CASCADE)
    categoriaespecificoTPD = models.ForeignKey(especificoTDP,on_delete=models.CASCADE)
    categoriaProdutos = models.ForeignKey(Produtos,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    ncm = models.FloatField(null=False, blank=False)
    situacaoTributaria = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

