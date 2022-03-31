from django.db import models


sexo_escolha =[
    ('', 'Escolha uma opção' ),
    ('F', 'Feminino'),
    ('M', 'Masculino')
]
program_escolhas = [
    ('', 'Python'),
    ('js', 'Javascript')
]

class Cadas(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    data_nascimento = models.DateField()
    celular = models.IntegerField()
    genero = models.CharField(max_length=1, choices=sexo_escolha, default='', blank=True)
    leg_prog = models.CharField(max_length=2,choices=program_escolhas, default='', blank=True)
    trabalhou = models.BooleanField()
    softskills = models.CharField(max_length=150, blank=True)

    def __str__(self):
         return self.nome