from django.shortcuts import render
from django.http import HttpResponse

def all_habits(request):
    return render(request, "main/all_habits.html")
    
def create_habit(request):
    return render(request, "main/create_habit.html")
def update_habit(request):
    return render(request, "main/update_habit.html")