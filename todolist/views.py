from django.urls import reverse
from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.
@login_required(login_url='/todolist/login')
def show_tasks(request):
    tasks = Task.objects.filter(user=request.user).all()
    context = {'tasks':tasks, 'user':request.user}
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
    print("keluar")
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

def create_task(request: HttpRequest):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                user=request.user,
            )
            task.save()
            messages.success(request, "Task Berhasil dibuat!")
            return redirect("todolist:show_tasks")
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, "create_task.html", context)

def update(request, id):
    task = Task.objects.get(pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponseRedirect(reverse("todolist:show_tasks"))

def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_tasks"))

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="Description", required=False)