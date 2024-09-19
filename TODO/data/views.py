from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user

            var.save()
            messages.info(request, 'Plan Added')
            return redirect('home')
        
        else:
            messages.warning(request, 'Sorry, something went wrong')
            return redirect('create')
        
    else:
        form = CreateTaskForm()

        context = {'form':form}
        return render(request, 'data/create.html', context)

@login_required
def update_task(request, pk):
    task = Task.objects.get(user=request.user, pk=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST or None, instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'data/update.html', context) mfn
    else:
        form = UpdateTaskForm()

    context = {'form':form}
    return render(request, 'data/update.html', context)
    
@login_required
def home(request):
    query = Task.objects.filter(user=request.user).order_by('created')
    context = {'tasks':query}
    return render(request, 'data/home.html', context)


@login_required
def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    messages.success(request, 'Task Completed')
    return redirect('home')

@login_required
def delete_task(request, pk):
    task = Task.objects.get(user=request.user, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted')
    return redirect('home')


