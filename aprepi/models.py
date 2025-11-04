from django.db import models
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from io import BytesIO
from tinymce.models import HTMLField
import os

# Modelo que representa um 'Carrossel'
class Carousel(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    image1 = models.ImageField(upload_to='carroussel/', verbose_name='Imagem 1')
    image2 = models.ImageField(upload_to='carroussel/', verbose_name='Imagem 2')
    image3 = models.ImageField(upload_to='carroussel/', verbose_name='Imagem 3')

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        """Remove as imagens antigas se forem substituídas."""
        if self.pk:
            old = Carousel.objects.get(pk=self.pk)
            for field in ['image1', 'image2', 'image3']:
                old_image = getattr(old, field)
                new_image = getattr(self, field)
                if old_image and old_image != new_image:
                    if os.path.isfile(old_image.path):
                        os.remove(old_image.path)
        super().save(*args, **kwargs)

    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        """Remove as imagens do sistema de arquivos ao deletar o objeto."""
        for field in ['image1', 'image2', 'image3']:
            image = getattr(self, field)
            if image and os.path.isfile(image.path):
                os.remove(image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'carrossel'
        verbose_name_plural = 'carrosseis'


# Modelo que representa 'Sobre'
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


# Modelo que representa um 'Contato'
class Contact(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    image = models.ImageField(upload_to='contact/', verbose_name='Imagem', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Contact.objects.get(pk=self.pk).image
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
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


# Modelo que representa um 'Registro de usuários'
class Register_Users(models.Model):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

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

    # Novo campo de gênero
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        verbose_name='Gênero'
    )
   
    def __str__(self):
        return self.name
    
    @property
    def first_name(self):
    #Retorna o primeiro nome para usar na saudação.
        return self.name.split()[0] if self.name else ''
    
    @property
    # """Saudação pronta para usar no template: Bem-vindo / Bem-vinda / Bem-vindo(a).
    def greeting(self):
        if self.gender == 'M':
            return f'Bem-vindo, {self.first_name}!'
        if self.gender == 'F':
            return f'Bem-vinda, {self.first_name}!'
        return f'Bem-vindo(a), {self.first_name}!'

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


# Modelo que representa o comentário de uma notícia
class Comment_News(models.Model):
    news = models.ForeignKey(Recent_News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150, verbose_name='Nome')
    comment = models.TextField(max_length=250, verbose_name='Deixe seu comentário')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'


# Modelo que representa uma resposta ao comentário de uma notícia
class Reply_Comment(models.Model):
    comment = models.ForeignKey(Comment_News, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=150, verbose_name='Nome')
    reply = models.TextField(max_length=250, verbose_name='Responder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'resposta'
        verbose_name_plural = 'respostas'


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

#------------------------ LINK APREPI ------------------------#

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
        verbose_name_plural = 'história'

#------------------------ SUBLINK TRANSPARÊNCIA ------------------------#

# Modelo que representa o submenu 'Documentos'
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


# Modelo que representa o submenu 'Atas'
class Ata(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    file = models.FileField(upload_to='atas/', verbose_name='Arquivo da ata')
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
        verbose_name = 'ata'
        verbose_name_plural = 'atas'

#------------------------ SUBLINK EVENTOS ------------------------#

'''Modelo que representa o campo de EVENTOS'''
class EventImage(models.Model):
    image = models.ImageField(upload_to='event_image/', verbose_name='Imagem')
    description = models.TextField(max_length=250, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return f"Imagem:{self.description[:30]}"
    
    # Sobrescrevendo o 'método delete' para o campo 'image'
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
            super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'imagem de evento'
        verbose_name_plural = 'imagens de eventos'

'''Modelo que representa o campo de VÍDEOS'''
class EventVideo(models.Model):
    thumbnail = models.ImageField(upload_to='event_thumbs/', verbose_name='Escolha uma miniatura')
    video = models.FileField(upload_to='event_video', verbose_name='Escolha um vídeio')
    description = models.TextField(max_length=250, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return f"Vídeo:{self.description[:30]}"
    
    # Sobrescrevendo o 'método delete' para o campo 'vídeo'
    # Remove o thumbnail do disco
    def delete(self, *args, **kwargs):
        if self.thumbnail and os.path.isfile(self.thumbnail.path):
            os.remove(self.thumbnail.path)
        # Remove o vídeo do disco
        if self.video and os.path.isfile(self.video.path):
            os.remove(self.video.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'vídeo de evento'
        verbose_name_plural = 'vídeos de eventos'

#------------------------ LINK DIRETORIA ------------------------#

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
        verbose_name_plural = 'diretoria'

#------------------------ LINK CONTRIBUA ------------------------#

class Contribute(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    image = models.ImageField(upload_to='contribute/', verbose_name='Imagem', blank=True, null=True)
    description = HTMLField(verbose_name='Descrição', blank=True, null=True)

    # Sobrescrevendo o 'método save' para o campo 'image'
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Contribute.objects.get(pk=self.pk).image
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
        verbose_name = 'contribua'
        verbose_name_plural = 'contribua'
