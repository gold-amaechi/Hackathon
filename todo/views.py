from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description', 'priority', 'date']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'date']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # def form_valid(self, form):
    #     return super().form_valid(form)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        return super(TaskDelete, self).delete(request, *args, **kwargs)
