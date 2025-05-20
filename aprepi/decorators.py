from django.contrib.auth.decorators import user_passes_test

def is_patient(user):
    return user.is_authenticated and hasattr(user, 'usuario') and user.usuario.tipo == 'paciente'