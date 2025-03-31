from django.urls import path
from todo.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),  # URL para a lista de tarefas
    path("criar/", TodoCreateView.as_view(), name="todo_create"),  # URL para criar uma nova tarefa
    path("atualizar/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
    path("deletar/<int:pk>/", TodoDeleteView.as_view(), name="todo_delete"),
    path("completar/<int:pk>/", TodoCompleteView.as_view(), name="todo_complete"),
]
