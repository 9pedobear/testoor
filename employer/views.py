from django.views.generic import ListView
from .models import *



class HomeEmployers(ListView):
    model = Employer
    template_name = 'index.html'
    context_object_name = 'employer'

    def get_queryset(self):
        return Employer.objects.filter(is_published=True)