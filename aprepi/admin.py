from django.contrib import admin
from .models import Carousel, Register_Users, Recent_News, Comment_News, Testimonials, History, Documents, Ata, EventImage, EventVideo, Directors, About, Contact, Contribute
from django.utils.html import format_html


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['titulo']

'''------------------------------------------'''

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

'''------------------------------------------'''

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']

    def has_add_permission(self, request):
        # Impede adicionar novo contato se já houver um
        if Contact.objects.exists():
            return False
        return True

'''------------------------------------------'''

@admin.register(Register_Users)
class RegisterUsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'city', 'email', 'gender']

'''------------------------------------------'''

@admin.register(Recent_News)
class RecentNewsAdmin(admin.ModelAdmin):
    list_display = ['short_title', 'image', 'short_text']

    # Truncamento para o tamanho do título no 'Admin do Django'
    def short_title(self, obj):
        return (obj.title[:20] + '...') if len(obj.title) > 20 else obj.title
    short_title.short_description = 'Título'

    # Truncamento para o tamanho do texto no 'Admin do Django'
    def short_text(self, obj):
        return (obj.text[:50] + '...') if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Texto'

'''------------------------------------------'''

@admin.register(Comment_News)
class CommentNewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created_at']

'''------------------------------------------'''

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city', 'image_tag']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; object-fit: cover;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Imagem'

'''------------------------------------------'''

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

'''------------------------------------------'''

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'thumbnail_preview']
    readonly_fields = ['thumbnail']  # Impede edição manual

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="60"/>', obj.thumbnail.url)
        return "Nenhuma miniatura"

    thumbnail_preview.short_description = "Miniatura"

'''------------------------------------------'''

@admin.register(Ata)
class AtaAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'thumbnail_preview']
    readonly_fields = ['thumbnail']  # Impede edição manual

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="60"/>', obj.thumbnail.url)
        return "Nenhuma miniatura"

    thumbnail_preview.short_description = "Miniatura"

'''------------------------------------------'''

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at']

'''------------------------------------------'''

@admin.register(EventVideo)
class EventVideoAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at']

'''------------------------------------------'''

@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

'''------------------------------------------'''

@admin.register(Contribute)
class ContributeAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']