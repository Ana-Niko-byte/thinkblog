from django.contrib import admin
from .models import Creator
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Creator)
class AboutCreator(SummernoteModelAdmin):
    summernote_fields = ('content',)