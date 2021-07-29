
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages#procesar mensajes
from .form import PostForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def feed(request):
    
    posts = Post.objects.all()#aca se hace el llamado a todos los campos de  la tabla
    
    context = {'posts':posts}#se crea el contexto
    
    return render(request,'social/feed.html',context)# renderiza la pagina con los datos respectivos


#creacion y validacion del formulario de usuario
def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            
            messages.success(request,f'Usuario {username} creado')
            return redirect('feed')
            
    else:
        
        form = UserRegisterForm()
    
    context = {'form':form}
    
    return render(request,'social/register.html',context)

@login_required
def post(request):
    current_user= get_object_or_404(User,pk=request.user.pk)
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request,'post enviado')
            return redirect('feed')
    else:
        form = PostForm()
        
    
    return render(request,'social/post.html',{'form':form})


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user=User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    
    return render(request,'social/profile.html',{'user':user,'posts':posts})

def follow(request,username):
    
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id =  to_user
    rel = RelationsShip(from_user=current_user,to_user=to_user_id)
    rel.save()
    messages.success(request,f'sigues a {username}')
    
    return redirect('feed')


def unfollow(request,username):
    
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id =  to_user.id
    rel = RelationsShip.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    
    
    messages.success(request,f'Ya no sigues a {username}')
    
    return redirect('feed')
