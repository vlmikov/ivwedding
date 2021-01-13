from django.shortcuts import render
from .models import Guest



def home(request, pk):
    user = Guest.objects.get(pk=pk)

    context = {
        'user': user
        }
    return render(request, 'wedd_app/home.html', context)
    



