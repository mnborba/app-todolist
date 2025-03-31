from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Todo
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

# FPV - Função de View
# def todo_list(request):
#     todo = Todo.objects.all()
#     return render(request, "todo/todo_list.html", {"todo": todo})


# CBV - Class Based View
class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "descricao", "data_entrega"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["titulo", "descricao", "data_entrega"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_as_completed()
        return redirect("todo_list")
