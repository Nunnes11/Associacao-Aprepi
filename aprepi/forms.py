import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Register_Users, Testimonials, Comment_News, Reply_Comment


class RegisterUsersForm(forms.ModelForm):
    '''Campo adicional que não será salvo no banco de dados'''
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirme a senha')

    class Meta:
        model = Register_Users
        fields = ['name', 'birth_date', 'city', 'email', 'is_patient', 'avatar', 'gender', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'is_patient': 'É paciente renal?',
            'password': 'Senha',
            'gender': 'Gênero',
        }

    # Validação do E-mail
    def clean_email(self):
         email = self.cleaned_data.get('email', '').strip()

         # Verifica se há letras maiúsculas
         if any(c.isupper() for c in email):
              raise ValidationError('Por favor apenas letras minúsculas no e-mail.')
         
         # Verifica se o formato do e-mail é válido
         if not re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', email):
              raise ValidationError('Por favor, forneça um e-mail válido')
         
         # Verifica se o e-mail já existe no banco
         if Register_Users.objects.filter(email__iexact=email).exists():
              raise ValidationError('E-mail já cadastro. Por favor use outro endereço.')
         
         return email
    
    # Validação da senha
    def clean_password(self):
         password = self.cleaned_data.get('password')

         if len(password) < 8:
              raise ValidationError('A senha deve ter pelo menos 8 caracteres.')
         if not re.search(r'[A-Z]', password):
              raise ValidationError('A senha deve conter pelo menos uma letra maiúscula.')
         if not re.search(r'[a-z]', password):
              raise ValidationError('A senha deve conter pelo menos uma letra minúscula')
         if not re.search(r'[0-9]', password):
              raise ValidationError('A senha deve conter pelo menos um número.')
         
         return password
    
    # Confirmação da senha
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
            
        if password and confirm_password and password != confirm_password:
                self.add_error('confirm_password', 'Sua senha é diferente da primeira.')

        return cleaned_data

    # Salvando senha criptografada
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password']) # A senha é criptografada.
        if commit:
            user.save()
        return user
    
class TestimonialsForm(forms.ModelForm):
     class Meta:
          model = Testimonials
          fields = ['testimonial']
          widgets = {
               'testimonial': forms.Textarea(attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Escreva seu depoimento'
                }),
          }

class CommentNewsForm(forms.ModelForm):
     class Meta:
          model = Comment_News
          fields = ['comment']
          widgets = {
               'comment': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
          }

class ReplyCommentForm(forms.ModelForm):
     class Meta:
          model = Reply_Comment
          fields = ['reply']
          widgets = {
               'name': forms.TextInput(attrs={'class': 'forms-control'}),
               'reply': forms.Textarea(attrs={
                    'placeholder': 'Digite sua resposta',
                    'class': 'forms-control',
                    'rows':2
                }),
          }