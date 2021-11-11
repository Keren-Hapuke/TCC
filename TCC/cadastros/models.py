from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)

class Orientador(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)

class Curso(models.Model):
    nome = models.CharField(max_length=150)

class Relatorio(models.Model):
    autor = models.ManyToManyField(Autor)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=150)
    resumo = models.TextField()
    palavras_chave = models.CharField(max_length=250)
    ano_documento = models.IntegerField()
    local_estagio = models.CharField(max_length=150)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    arquivo = models.FileField()