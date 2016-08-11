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
	return render(request, 'pages/details/page_detail.html', {'p':p, 'p2':p2, 'content': userPage})

def login(request):
	p, p2 = getBaseInfo()
	return render(request, 'pages/login.html', {'p':p, 'p2':p2})

def dj_detail(request, djName):
	djObject = get_object_or_404(Deejay.objects.filter(dj__iexact=djName))
	shows = Show.objects.filter(dj=djObject)
	p, p2 = getBaseInfo()
	return render(request, 'pages/details/dj_detail.html', {'p':p, 'p2':p2, 'dj':djObject, 'shows':shows})

def show_detail(request, namegiven):
	showObject = get_object_or_404(Show.objects.filter(showname__iexact=namegiven))
	playlists = Playlist.objects.filter(show=showObject)
	p, p2 = getBaseInfo()
	return render(request, 'pages/details/show_detail.html', {'p':p, 'p2':p2, 'show':showObject, 'playlists':playlists})

def shows(request):
	djs = Deejay.objects.all()
	shows = Show.objects.all()
	p, p2 = getBaseInfo()
	return render(request, 'pages/show_list.html', {'p':p, 'p2':p2, 'djs':djs, 'shows':shows})