from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Client

def home(request):
	clients = Client.objects.all()

	# whether there is an account and the correctness of filling
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You've logged!")
			return redirect('home')
		else:
			messages.success(request, "Filling error! Please try again!")
			return redirect('home')
	else:
		return render(request, 'home.html', {'clients':clients})


def logout_user(request):
    logout(request)
    messages.success(request, "You've logged out")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST) # all that user filled, send in form and do nice caces
	    
		#validation of input
		# if posting form	
		if form.is_valid:
			try:
				form.save()
				#after saving form, user need authenticate and login ->
				username =  form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username=username, password=password)
				login(request,user)
				messages.success(request, f"Succes! {username} registered!")
				return redirect('home')
			except Exception as e:
				messages.success(request, f"Filling error:{e}")
				return redirect('register')
		
	else:
		form = SignUpForm()
		
	return render(request, 'register.html', {'form':form})

def manager_record(request, pk):
	if request.user.is_authenticated:
		# search a record
		manager_record = Client.objects.get(client_id=pk)
		return render(request, 'record.html', {'managers_record':manager_record})
	else:
		messages.success(request, "you must be logged!")
		return redirect('home')

def manager_delete_record(request, pk):
	if request.user.is_authenticated:
		# search a record
		manager_record = Client.objects.get(client_id=pk)
		manager_record.delete()
		messages.success(request, f"Client deleted!")
		return redirect('home')
		#return render(request, 'record.html', {'managers_record':manager_record})
	else:
		messages.success(request, "you must be logged!")
		return redirect('home')
	
def manager_add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				add_rec = form.save()
				messages.success(request, "Client added!")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "you must be logged!")
		return redirect('home')

