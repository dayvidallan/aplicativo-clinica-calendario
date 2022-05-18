from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.urls import reverse



class Paciente(models.Model):
    CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    nome = models.CharField(max_length=100, unique=False)
    cpf = models.CharField(max_length=14, unique=False, null=True, blank=True, verbose_name='Nº CPF')
    rg = models.CharField(max_length=14, unique=False, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=14, null=True, blank=True, choices=CHOICES)
    email = models.EmailField('E-mail', unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=100, unique=False, verbose_name='Nº telefone celular')
    endereco = models.CharField(max_length=100, unique=False)
    data_consulta = models.DateTimeField(default=timezone.now)
    anamnesi = models.TextField(null=True, blank=True, verbose_name='Ananimese')
    upload = models.FileField(upload_to='perfil', null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('paciente_list')


    def __str__(self):
        return self.nome



class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consulta")
    data_consulta = models.DateTimeField(default=timezone.now)
    anamnesi = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Ananimese')
    upload = models.FileField(upload_to='upload', null=True, blank=True, verbose_name='Documentos')

    objects = Paciente()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.paciente.nome


    def get_absolute_url(self):
        return reverse("paciente_detail", args=(self.paciente.id,))

    @property
    def get_html_url(self):
        url = reverse("paciente_detail", args=(self.id,))
        return f'<a href="{url}"> {self.paciente} </a>'
