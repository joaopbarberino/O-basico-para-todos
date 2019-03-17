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

    nome_c = 'Nome do Autor'
    nome = models.CharField(nome_c, max_length=120)
    autor = models.CharField(max_length =120, default = 'SOBRENOME, Nome (Apenas o 1º)')
    genero_c = 'Gênero'
    genero = models.CharField(genero_c, max_length=2, choices = genero_opcoes)
    descricao_c = 'Descrição'
    descricao = models.TextField(descricao_c, default = 'Insira uma breve descrição do livro.')
    lancamento_c = 'Lançamento'
    lancamento = models.DateField(lancamento_c, null = True)
    arquivo = models.FileField(upload_to='', default = 'VAZIO')
    
    
    def __str__(self):
        return self.nome