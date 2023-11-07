from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'priority', 'date', 'completed']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'date', 'completed']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task-list')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task-list')
