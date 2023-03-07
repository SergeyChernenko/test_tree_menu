from django.contrib import admin
from .models import Tree
from mptt.admin import MPTTModelAdmin

admin.site.register(Tree, MPTTModelAdmin)