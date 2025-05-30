from django.contrib import admin
from .models import Register_Users, Recent_News, Testimonials, History, Documents, Directors, About
from django.utils.html import format_html

@admin.register(Register_Users)
class RegisterUsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'city', 'email']


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


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'thumbnail_preview']
    readonly_fields = ['thumbnail']  # Impede edição manual

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="60"/>', obj.thumbnail.url)
        return "Nenhuma miniatura"

    thumbnail_preview.short_description = "Miniatura"


@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']