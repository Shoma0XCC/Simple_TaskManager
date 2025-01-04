from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView
from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy
from .filters import TaskFilter



def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})

class Detail(DetailView):
    model = Task
    template_name = 'main/details.html'
    success_url = reverse_lazy('creat')



class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'main/task.html'
    success_url = reverse_lazy('creat')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Получаем текущий объект задачи
        if request.POST.get('delete_task') == 'on':
            self.object.delete()  # Удаляем задачу без проверки валидации формы
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Стандартное поведение, если задача не удаляется
        return super().form_valid(form)


def creat(request):
    error = ''
    # Обработка POST-запроса (создание задачи)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('creat')
        else:
            error = 'Некорректные данные'

    # Форма создания задачи
    form = TaskForm()

    # Применяем фильтрацию только для GET-запросов
    task = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=task)
    filtered_tasks = task_filter.qs

    # Передаём все данные в шаблон
    data = {
        'form': form,
        'tasks': filtered_tasks,
        'error': error,
        'filter': task_filter,
    }

    return render(request, 'main/index.html', data)
