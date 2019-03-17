from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
class Livro(models.Model):
    # ---------------'primeira e ultima letra do genero -> Historia = 'ha' e etc
    genero_historia = 'ha'
    genero_matematica = 'ma'
    genero_portugues = 'ps'
    genero_geografia = 'ga'
    genero_fisica = 'fa'
    genero_biologia = 'ba'
    genero_quimica = 'qa'
    genero_informatica = 'ia'
    genero_ciencias = 'cs'
    genero_filosofia = 'fi' #primeira e penultima letra pra n bater com fisica
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

    nome = models.CharField(verbose_name = 'Nome do Livro', max_length=120)
    autor = models.CharField(verbose_name = 'Nome do autor', max_length =120, default = 'SOBRENOME, Nome (Apenas o 1º)') 
    genero = models.CharField(verbose_name = 'Gênero', max_length=2, choices = genero_opcoes)
    descricao = models.TextField(verbose_name = 'Descrição', default = 'Insira uma breve descrição do livro.')
    lancamento = models.DateField(verbose_name = 'Lançamento', null = True)
    arquivo = models.FileField(upload_to = '', default = 'VAZIO')
#New CustomUserManager 
class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Usuers must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            # date_joined=now,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self.__db)
        return user
    
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    # Creates and saves a superuser with the given email, date of
    # birth and password.
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
#New UserCustom model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True,blank=True)
    # data_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return '/app_principal/%i' %(self.pk)


class Teacher(User):
    creation = models.DateTimeField(auto_now=True)
    teacher_register = models.IntegerField()

    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    name = models.CharField(max_length=20)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Student(User):
    student_register = models.IntegerField()
    creation = models.DateTimeField(auto_now=True)
    student_teachers = models.ManyToManyField(Teacher,blank=True,related_name='teachers')
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HomeWork(models.Model):   
    title = models.CharField(max_length=200)
    creation = models.DateTimeField(auto_now=True)
    file = models.FileField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.title