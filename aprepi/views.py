from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.templatetags.static import static
from .models import Register_Users, Recent_News, Comment_News, Testimonials, History, Documents, Ata, Directors, About
from .forms import RegisterUsersForm, TestimonialsForm, CommentNewsForm, ReplyCommentForm
from .decorators import is_patient
from datetime import date

def home(request):
    return render(request, 'aprepi/home.html')

def about(request):
    abouts = About.objects.all()
    return render(request, 'aprepi/about.html', {'abouts': abouts})

def contact(request):
    return render(request, 'aprepi/contact.html')

def register_users(request):
    if request.method == 'POST':
        form = RegisterUsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = RegisterUsersForm()
    return render(request, 'aprepi/register_users.html', {'form':form})

def list_users(request):
    users = Register_Users.objects.all()
    return render(request, 'aprepi/list_users.html', {'users': users})

def update_user(request, id):
    user = get_object_or_404(Register_Users, id=id)

    if request.method == 'POST':
        form = RegisterUsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = RegisterUsersForm(instance=user)

    return render(request, 'aprepi/update_user.html', {'form': form})

def delete_user(request, id):
    user = get_object_or_404(Register_Users, id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    
    return render(request, 'aprepi/delete_user.html', {'user': user})

def archive_user(request, id):
    user = get_object_or_404(Register_Users, id=id)
    user.is_archived = True
    user.save()
    return redirect('list_users')

def list_patients(request):
    patients = Register_Users.objects.all()
    return render(request, 'aprepi/list_patients.html', {'patients': patients})

def update_patient(request):
    return render(request, 'aprepi/update_patient.html')

def delete_patient(request):
    return render(request, 'aprepi/delete_patient.html')

'''Função para implementar o LOGIN'''
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Register_Users.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('reception_page')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
    
    return render(request, 'aprepi/login.html')

'''Função para implementar o LOGOUT, retornando para a HOME'''
def logout(request):
    request.session.flush()
    return redirect('home')


def reception_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user= Register_Users.objects.get(id=user_id)
    first_name = user.name.split()[0]

    if user.avatar:
        avatar_url = user.avatar.url
    else:
        avatar_url = '/media/avatars/avatar.png'

    news = Recent_News.objects.all().order_by('-created_at')[:4]
    testimonials = Testimonials.objects.all().order_by('-id')[:4]

    return render(request, 'aprepi/reception_page.html', {
        'user_name': first_name,
        'user_avatar_url': avatar_url,
        'news': news,
        'testimonials': testimonials
    })


def news_list(request):
    news = Recent_News.objects.all().order_by('id')
    return render(request, 'aprepi/news_list.html', {'news': news})


def new_detail(request, id):
    new = get_object_or_404(Recent_News, id=id)
    comments = new.comments.all().order_by('created_at')

    comment_form = CommentNewsForm()
    reply_form = ReplyCommentForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentNewsForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.news = new
                
                user_id = request.session.get('user_id')
                if user_id:
                    try:
                        usuario = Register_Users.objects.get(id=user_id)
                        comment.name = usuario.name
                    except Register_Users.DoesNotExist:
                        comment.name = 'Anônimo'
                else:
                    comment.name = 'Anônimo'

                comment.save()
                return redirect('new_detail', id=new.id)
        
        elif 'reply_submit' in request.POST:
            reply_form = ReplyCommentForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                comment_id = request.POST.get('comment_id')
                reply.comment = get_object_or_404(Comment_News, id=comment_id)
                reply.save()
                return redirect('new_detail', id=new.id)

    return render(request, 'aprepi/new_detail.html', {
        'new': new,
        'comments': comments,
        'form': comment_form,
        'reply_form': reply_form
    })


def testimonials_list(request):
    testimonials = Testimonials.objects.all().order_by('-id')
    return render(request, 'aprepi/testimonials_list.html', {'testimonials': testimonials})

# Função que mostra o depoimento de cada paciente
def testimonial_detail(request, id):
    testimonial = get_object_or_404(Testimonials, id=id)
    return render(request, 'aprepi/testimonial_detail.html', {'testimonial': testimonial})


def calcular_idade(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


# Função para a 'Página de Depoimento'
def create_testimonial(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')
    
    try:
        user = Register_Users.objects.get(id=user_id)
    except Register_Users.DoesNotExist:
        return redirect('login')
    
    if not user.is_patient:
        return redirect('reception_page') # Não é paciente.
    
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.name = user.name
            testimonial.age = calcular_idade(user.birth_date)
            testimonial.city = user.city
            testimonial.avatar = user.avatar
            testimonial.save()
            return redirect('reception_page')
    else:
        form = TestimonialsForm()
    return render(request, 'aprepi/create_testimonial.html', {'form': form})


def history(request):
    historys = History.objects.all()
    return render(request, 'aprepi/history.html', {'historys': historys})


def documents(request):
    documents = Documents.objects.all()
    return render(request, 'aprepi/documents.html', {'documents': documents})


def ata(request):
    atas = Ata.objects.all()
    return render(request, 'aprepi/atas.html', {'atas': atas})


def director(request):
    directors = Directors.objects.all()
    return render(request, 'aprepi/directors.html', {'directors': directors})







