from django.shortcuts import render, redirect
from django.views import View
from .models import Activity
import random
from datetime import datetime

class ActivityListView(View):
    def get(self, request):
        activities = Activity.objects.all()
        return render(request, 'activities/list.html', {'activities': activities})

class ActivityCreateView(View):
    def get(self, request):
        return render(request, 'activities/create.html')

    def post(self, request):
        title = request.POST.get('title')
        Activity.objects.create(title=title)
        return redirect('activity_list')

class RandomActivityView(View):
    def get(self, request):
        activity = Activity.objects.order_by('?').first()
        if activity:
            activity.last_picked = datetime.now()
            activity.save()
        return render(request, 'activities/random.html', {'activity': activity})
    
class ActivityDeleteView(View):
    def post(self, request, pk):
        activity = Activity.objects.get(pk=pk)
        activity.delete()
        return redirect('activity_list')