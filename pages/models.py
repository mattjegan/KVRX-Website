from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

def validate_legal_url(value):
    RESTRICTED_URLS = [
        'base',
        'shows',
        'login',
        'dj',
        'show',
    ]
    for url in RESTRICTED_URLS:
        if str(value).startswith(url):
            raise ValidationError('Urls starting with {} are not allowed'.format(url))

# Create your models here.
class Page(models.Model):
	pageTitle = models.CharField(max_length=20, verbose_name='Page Title (Will be displayed on site')
	pageURL = models.CharField(max_length=50, verbose_name='Page URL (http://kvrx.org/PAGEURL)', validators=[validate_legal_url])
	pageContent = models.TextField(verbose_name='Page Content (HTML). Will be placed inside the standard KVRX template')
	showOnHomepage = models.BooleanField(verbose_name='Show on home page?')
	def __unicode__(self):
		return self.pageTitle

