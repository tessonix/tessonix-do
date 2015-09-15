from django.contrib import admin

# Register your models here.
from models import Category, DoItem, User
admin.site.register(Category)
admin.site.register(DoItem)
admin.site.register(User)
