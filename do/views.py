from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, User, DoItem

import os
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')


def db(request):
    """ Print out the state of the database as it currently stands. """
    users = User.objects.all()
    todos = DoItem.objects.all()
    categories = Category.objects.all()

    return render(request, 'db.html', {'users': users, 'todos': todos, 'categories': categories})
