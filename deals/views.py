from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    tasks = Task.objects.all()
    return render(request, 'deals/index.html', {'tasks': tasks})

@csrf_exempt
def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        status = request.POST.get('status')
        task = get_object_or_404(Task, id=task_id)
        task.status = status
        task.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})