#views.py in frontend basically renders the index template so that react can then take care of it.
#you will see this index function as a variable for the paths in urls.py for frontend

from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')