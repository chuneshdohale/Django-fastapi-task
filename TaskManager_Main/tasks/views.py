from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Task
from .forms import TaskForm



# Class Based Views
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

# class TaskListView(ListView):
#     model = Task
#     context_object_name = 'tasks'
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'  # Specify your template name

    def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.GET.get('name')  # Get the search query for name
        status_query = self.request.GET.get('status')  # Get the search query for status

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        if status_query:
            # Ensure that status_query matches one of the valid choices ('u', 'o', 'f')
            if status_query in [choice[0] for choice in Task.Status.choices]:
                queryset = queryset.filter(status=status_query)
        return queryset


class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
