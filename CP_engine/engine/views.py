from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
from engine.models import problem

# Create your views here.

def search(request):
	if request.method == 'POST':
		input = request.POST.get('search')
		result = problem.objects.filter(search__icontains=input).all()
		context = { 'result' : result }
		return render(request, 'engine/results.html', context)
	return render(request, 'engine/search.html')

def results(request):
	if request.method == 'POST':
		input = request.POST.get('search')
		result = problem.objects.filter(search__icontains=input).all()
		context = { 'result' : result }
		return render(request, 'engine/results.html', context)
	return render(request, 'engine/results.html')