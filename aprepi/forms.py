from django import forms
from django.contrib.auth.hashers import make_password
from .models import Register_Users

class RegisterUsersForm(forms.ModelForm):
    '''Campo adicional que não será salvo no banco de dados'''
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirme a senha')

    class Meta:
        model = Register_Users
        fields = ['name', 'birth_date', 'city', 'email', 'is_patient', 'avatar', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'is_patient': 'É paciente renal?',
            'password': 'Senha',
        }
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
            
        if password and confirm_password and password != confirm_password:
                self.add_error('confirm_password', 'Sua senha é diferente da primeira.')
                
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password']) # A senha é criptografada.
        if commit:
            user.save()
        return user