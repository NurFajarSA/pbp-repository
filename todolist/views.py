from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
@login_required(login_url='/todolist/login')
def show_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            return redirect('todolist:show_tasks')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Akun ' + user + ' berhasil dibuat!')
            return redirect('todolist:login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

# def create_task(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         date = str(request.POST.get('date'))
#         user = request.user
#         Task.objects.create(user=user, title=title, description=description, date=date)
#     return redirect('todolist:show_tasks')