from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Todos
from django.contrib import messages


# Create your views here.


class TodoListView(ListView):
    model = Todos
    template_name = 'todoMVC/listTaskPage.html'
    context_object_name = 'todos'



from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TodoCreateView(CreateView):
    model = Todos
    template_name = 'todoMVC/formPage.html'
    fields = ["title","task"]

    success_url = reverse_lazy('todo_list_view')




class TodoUpdateView(UpdateView):
    model = Todos
    template_name = 'todoMVC/formPage.html'
    fields = ["title","task"]
    success_url = reverse_lazy('todo_list_view')

    def form_valid(self, form):
        messages.success(self.request, "Task Updated Successfully")
        return super().form_valid(form)



class TodoDeleteView(DeleteView):
    model = Todos
    success_url = reverse_lazy('todo_list_view')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Task Deleted Successfully")
        return super().delete(request, *args, **kwargs)



def TodoDeleteAllView(request):
    if request.method == "POST":
        Todos.objects.all().delete()
        messages.success(request, "All Tasks have been deleted")


