from django.contrib import admin
from .models import TimeTable, Entry, EntryItem

# Register your models here.
admin.site.register(TimeTable)
admin.site.register(Entry)
admin.site.register(EntryItem)