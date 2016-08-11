from django.shortcuts import render, get_object_or_404
from .models import Page
from shows.models import Deejay, Show, Playlist, Song

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

def shows(request):
	p, p2 = getBaseInfo()
	return render(request, 'pages/base.html', {'p':p, 'p2':p2})

def dj_detail(request, djName):
	print(djName)
	dj = get_object_or_404(Deejay, dj=djName)
	p, p2 = getBaseInfo()
	return render(request, 'pages/dj_detail.html', {'p':p, 'p2':p2, 'dj':dj})