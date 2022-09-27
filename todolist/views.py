import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from todolist.models import TodoList

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = TodoList.objects.filter(user=request.user)
    var = request.COOKIES.get('last_login', 'UserNotFound')
    if var == "UserNotFound":
        response = HttpResponseRedirect(reverse("todolist:login"))
        return response
    context = {
        'username' : request.user.username,
        'todo_list' : data,
        'last_login': var,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title_task')
        description = request.POST.get('description_task')
        if title != "" and description != "":
            date = datetime.datetime.now()
            new_task = TodoList.objects.create(title=title, description=description, user=request.user, date=date)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
        else :
            list(messages.get_messages(request))
            messages.error(request, "Harap isi nama dan deskripsi task")
    return render(request, "add.html")

def delete(request, id):
    data = TodoList.objects.get(id=id)
    data.delete()
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return response

def set_status(request, id):
    data = TodoList.objects.get(id=id)
    data.is_finished = not (data.is_finished)
    data.save()
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return response

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
