from main_app.models import Task


from django.shortcuts import render
def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True)
    print(completed_task)
    context = {
        "tasks": tasks,
        "completed_task": completed_task,
        

    }
    return render(request, 'home.html', context)