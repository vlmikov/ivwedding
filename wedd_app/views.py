from django.shortcuts import render
from .models import Guest, Invitation



def home(request, slug):
    user = Invitation.objects.get(slug_name=slug)

    context = {
        'user': user
        }
    return render(request, 'wedd_app/home.html', context)
    

def dashboard(request):
    invitations = Invitation.objects.all()
    invitations_without_url = Invitation.objects.filter(url="")
    for inv in invitations_without_url:
        inv.create_url()
        inv.save() 
    context = {'invitations':invitations}
    return render(request, 'wedd_app/dashboard.html', context)


# def invitation(request):
#     return render(request, 'wedd_app/invitation.html')

