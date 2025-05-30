from django.db import models
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from io import BytesIO
import os


class About(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    image = models.ImageField(upload_to='about/', verbose_name='Imagem', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = About.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)

    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'sobre'
        verbose_name_plural = 'sobre'


# Modelo que representa um 'Registro de usuários'
class Register_Users(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    birth_date = models.DateField(verbose_name='Data de nascimento')
    city = models.CharField(max_length=150, verbose_name='Cidade')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    is_patient = models.BooleanField(default=False, verbose_name='É paciente renal?')
    '''Is_patience usa campo 'BooleanField' e indica se o usuário é ou não paciente renal usando
    'default' 'True' ou 'False'.'''
    is_archived = models.BooleanField(default=False, verbose_name='Arquivar registro')
    '''Is_archived é um campo booleano que só aceita 'True' ou 'False'. Serve para indicar se
    um registro está ou não arquivado. Se for 'is_archived = False' (valor padrão), o registro
    está ativo; se for 'is_archived = True', o registro está arquivado.'''
    password = models.CharField(max_length=200, verbose_name='Senha')
    '''Estamos armazenando a senha como um campo de texto, o que não é adequado; no formulário,
    usaremos o 'make_password' do Django para criptografar a senha antes de salvá-la.'''
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Avatar')
   

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'registro de usuário'
        verbose_name_plural = 'registros de usuários'

# Modelo que representa o campo 'Notícias Recentes'
class Recent_News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    image = models.ImageField(upload_to='news/', verbose_name='Imagem')
    text = models.TextField(verbose_name='Texto')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Recent_News.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)

    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'notícia recente'
        verbose_name_plural = 'notícias recentes'


# Modelo que representa o campo 'Depoimentos'
class Testimonials(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    age = models.IntegerField(verbose_name='Idade')
    city = models.CharField(max_length=150, verbose_name='Cidade')
    image = models.ImageField(
        upload_to='testimonial/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )
    testimonial = models.TextField(verbose_name='Seu depoimento')
    created_at = models.DateTimeField(auto_now_add=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Testimonials.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)

    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
            super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.age} anos, {self.city}'
    
    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        ordering = ['-created_at']


# Modelo que representa o sublink 'História(da Associação)'
class History(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    image = models.ImageField(upload_to='history/', verbose_name='Imagem', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = History.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)

    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'história'
        verbose_name_plural = 'histórias'

# Modelo que representa o sublink 'Documentos' na seção 'Transparência'(link APREPI)
class Documents(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    file = models.FileField(upload_to='files/', verbose_name='Arquivo')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.file and not self.thumbnail:
            # Caminho do PDF salvo
            pdf_path = self.file.path

            # Converte a primeira página do PDF em imagem
            images = convert_from_path(pdf_path, first_page=1, last_page=1)
            if images:
                img_io = BytesIO()
                images[0].save(img_io, format='PNG')

                # Salva como ImageField
                img_name = os.path.splitext(os.path.basename(self.file.name))[0] + '.png'
                self.thumbnail.save(img_name, ContentFile(img_io.getvalue()), save=False)
                super().save(update_fields=['thumbnail'])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'

# Modelo que representa o link 'Diretoria'
class Directors(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    image = models.ImageField(upload_to='directors/', verbose_name='Imagem', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Directors.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)

    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'diretoria'
        verbose_name_plural = 'diretorias'



