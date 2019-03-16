from django.db import models

# Create your models here.
class Livro(models.Model):
    # ---------------'primeira e ultima letra do genero'
    genero_historia = 'ha'
    genero_matematica = 'ma'
    genero_portugues = 'ps'
    genero_geografia = 'ga'
    genero_fisica = 'fa'
    genero_biologia = 'ba'
    genero_quimica = 'qa'
    genero_informatica = 'ia'
    genero_ciencias = 'cs'
    genero_filosofia = 'fa'
    genero_sociologia = 'sa'
    genero_artes = 'as'
    genero_ingles = 'is'
    genero_espanhol = 'el'

    genero_opcoes = [
        (genero_artes, 'Artes'),
        (genero_biologia, 'Biologia'),
        (genero_ciencias, 'Ciências'),
        (genero_espanhol, 'Espanhol'),
        (genero_filosofia, 'Filosofia'),
        (genero_fisica, 'Física'),
        (genero_geografia, 'Geografia'),
        (genero_historia, 'História'),
        (genero_informatica, 'Informática'),
        (genero_ingles, 'Inglês'),
        (genero_matematica, 'Matemática'),
        (genero_portugues, 'Português'),
        (genero_quimica, 'Química'),
        (genero_sociologia, 'Sociologia'),
    ]

    nome = models.CharField(max_length=120)
    autor = models.CharField(max_length =120, default = 'Apenas o primeiro autor listado no livro: SOBRENOME, Nome')
    genero = models.CharField(max_length=2, choices = genero_opcoes)
    descricao = models.TextField(default = 'Insira aqui uma breve descrição do livro')
    lancamento = models.DateField()
    arquivo = models.FileField(upload_to='', default = 'VAZIO')
    
    def __str__(self):
        return self.nome