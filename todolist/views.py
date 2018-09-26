from django.shortcuts import render , redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			temp =form.save(commit=False)
			temp.user=request.user
			temp.save()
			all_items = List.objects.filter(user=request.user)
			messages.success(request,('Task Has Been Added To List yayy!'))
			return render(request, 'home.html',{'all_items':all_items})
	else:
		all_items = List.objects.filter(user=request.user)		
		print(all_items)
		return render(request,'home.html',{'all_items':all_items})
def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,("Task Deleted"))
	return redirect('home')
def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed= True
	item.save()
	return redirect('home')
def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed= False
	item.save()
	return redirect('home')
def edit(request,list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		item.delete()
		form = ListForm(request.POST or None)

		if form.is_valid():
			temp =form.save(commit=False)
			temp.user=request.user
			temp.save()
			all_items = List.objects.filter(user=request.user)
			messages.success(request,('Task Has Been updated yayy!'))
			return redirect('home')
	else:
		item = List.objects.get(pk=list_id)	
		return render(request,'edit.html',{'items':item})