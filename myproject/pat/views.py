"""
Pat App Views
"""
from django.views import generic
from .forms import DateDisplayForm
from myproject.settings import BASE_DIR

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world.")


class Index(generic.FormView):
    """display dates"""
    template_name = "index.html"
    success_url = "/"
    form_class = DateDisplayForm
    print(BASE_DIR)
