from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Potrait
# Create your views here.


class IndexView(View):

    def get(self, request):
        potraits = Potrait.objects.all()
        data = {
            'potraits': potraits,
        }
        return render(request, 'web/potrait-index.html', context=data)