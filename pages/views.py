from django.shortcuts import render, get_object_or_404
from .models import Page
from shows.models import Show, Playlist, Song
#from .forms import RegisterForm

# Page rendering methods here
def getBaseInfo():
	allPages = Page.objects.all()
	primaryPages = allPages[:5]
	secondaryPages = allPages[5:]
	return primaryPages, secondaryPages

# Create your views here.

def base(request):
	p, p2 = getBaseInfo()
	return render(request, 'pages/base.html', {'p':p, 'p2':p2})

def index(request):
	p, p2 = getBaseInfo()
	return render(request, 'pages/index.html', {'p':p, 'p2':p2})

def custom_page(request, p):
	userPage = get_object_or_404(Page, pageURL=p)
	p, p2 = getBaseInfo()
	return render(request, 'pages/page_detail.html', {'p':p, 'p2':p2, 'content': userPage})

def login(request):
	p, p2 = getBaseInfo()
	return render(request, 'pages/login.html', {'p':p, 'p2':p2})

# def register(request):
# 	#Redirect if user logged in is not a superuser or a gen admin
# 	p, p2 = getBaseInfo()
# 	form = RegisterForm()
# 	return render(request, 'pages/register.html', {'p':p, 'p2':p2, 'form':form})

def shows(request):
	p, p2 = getBaseInfo()
	return render(request, 'pages/base.html', {'p':p, 'p2':p2})