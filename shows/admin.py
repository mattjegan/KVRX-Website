from django.contrib import admin
from .models import Deejay, Show, Playlist, Song

# Register your models here.
admin.site.register(Deejay)
admin.site.register(Show)
admin.site.register(Playlist)
admin.site.register(Song)
