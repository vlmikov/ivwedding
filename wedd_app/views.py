from django.shortcuts import render, redirect, HttpResponse
from .models import MainGuest, SecondGuest, Invitation
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout as auth_logout

import json

from .forms import MainGuestForm, SecondGuestForm, InvitationForm






def home(request, slug):
    if request.method == 'POST':
        form_1_data_dict = {}
        form_2_data_dict = {}
        print(request.POST)
        print(request.POST.keys())

        for key in request.POST.keys():
            print(f'key :  {key}')
            if key != 'add_guest' and key!= 'csrfmiddlewaretoken':
                v = request.POST.getlist(key)
                print(f'value  {v}')
                if key == 'email':
                    form_1_data_dict[key] = v[0]
                    
                else:
                    form_1_data_dict[key] = v[0]
                    form_2_data_dict[key] = v[1]


        form_1 = MainGuestForm(form_1_data_dict)
        form_2 = SecondGuestForm(form_2_data_dict)
        #print(form_1)
        print('form_1 :valid')
        print(form_1.is_valid())
        print('form_2 :valid')
        print(form_2.is_valid())
        print('pppppppppppppppppppppppppppppp')
        print(request.POST.get('add_guest'))
        
        invitation = Invitation.objects.filter(slug_name=slug)[0]
        print(f'onvitation_complete {invitation.complete}')
        invitation.complete = True
        invitation.save()
        guest_1 = invitation.guest_1
        guest_2 = invitation.guest_2
        form_1 = MainGuestForm(form_1_data_dict, instance=guest_1)
        form_2 = SecondGuestForm(form_2_data_dict, instance=guest_2)
        if form_1.is_valid() and form_2.is_valid():
            temp = form_1.cleaned_data.get("email")
            print(f'tempppp: {temp}')
            form_1.save()
            form_2.save()
            first_name_1 = form_1.cleaned_data['first_name']
            last_name_1 = form_1.cleaned_data['last_name']
            
            



            form_1.save()
            # form_1.save_all_fields_from_request(slug)


            first_name_2 = form_2.cleaned_data['first_name']
            last_name_2 = form_2.cleaned_data['last_name']
            print('---------------------------------')
            print(f'first_name_form_1: {first_name_1}')
            print(f'last_name_form_1: {last_name_1}')
            print('---------------------------------')
            print(f'first_name_form_2: {first_name_2}')
            print(f'last_name_form_2: {last_name_2}')

            print('=============================================')
            return redirect('after_submit', slug=invitation.slug_name )

        # if form_2.is_valid():
        #     first_name_2 = form_2.cleaned_data['first_name']
        # if form_1.is_valid():
        #     print('////////////////////////////////////////////')
        #     print('FORM _  1')
        #     print(form_1.cleaned_data['first_name'])
        #     print(form_2.cleaned_data['last_name'])
        # if form_2.is_valid():
        #     print('////////////////////////////////////////////')
        #     print('FORM _  2')
        #     print(form_2.cleaned_data['first_name'])
        #     print(form_2.cleaned_data['last_name'])
        #     print('////////////////////////////////////////////')
       
    
    user = Invitation.objects.get(slug_name=slug)
    # print('USER-------------------')
    # print(user.slug_name)

    invitation = Invitation.objects.filter(slug_name = user.slug_name)[0]
    # print('=========')
    # print(invitation.guests.values())
    # print('==========')
    print(invitation)


    # print(len(guests))
    # if len(guests) == 2:
    #     form_1 = GuestForm1(guests[0])
    #     form_2 = GuestForm2(guests[1])
    # elif len(guests) == 1:
    #     form_1 = GuestForm1(guests[0])
    #     form_2 = GuestForm2()
    # else:
    #     form_1 = GuestForm1()
    #     form_2 = GuestForm2()
    print(f'guest_1 = {type(invitation.guest_1)}')
    print('//////////////////////')
    print(f'guest_2 = {invitation.guest_2}')
    print(invitation.guest_1)

    if invitation.guest_2.first_name == "":
        guests_number = 1
    else:
        guests_number=2
    
    form_1 = MainGuestForm(instance= invitation.guest_1)
    form_2 = SecondGuestForm(instance= invitation.guest_2)
    

    

    context = {
            'form_1':form_1,
            'form_2':form_2,
            'slug_name':slug,
            'guests_number':guests_number,
            'invitation':invitation,
        }
    return render(request, 'wedd_app/home.html', context)
    
@login_required
def dashboard(request):
    invitations = Invitation.objects.all()
    invitations_without_url = Invitation.objects.filter(url="")
    for inv in invitations_without_url:
        inv.create_url()
        inv.save() 


    

    viki_rodnini = Invitation.objects.filter(cat_type_guests='Вики Роднини')
    viki_friends = Invitation.objects.filter(cat_type_guests='Вики Приятели')
    viki_all_invitations = len(viki_rodnini) + len(viki_friends)
    viki_complete_invitation_rodnini = len([inv for inv in viki_rodnini if inv.complete==True ])
    viki_complete_invitation_friends = len([inv for inv in viki_friends if inv.complete==True ])
    viki_total_complete = viki_complete_invitation_friends + viki_complete_invitation_rodnini

    viki_pending_invitations = viki_all_invitations - viki_total_complete
    try:
        viki_complete_percentage = int((viki_total_complete / viki_all_invitations)*100)
    except:
        viki_complete_percentage = 0
    print(f'VIKI percentage COMPLETE: {viki_complete_percentage}')
    viki_ucomplete = 100 - viki_complete_percentage
    print(f'Viki uncomplete : {viki_ucomplete}')

    #viki_invitation = Invitation.objects.filter(cat_type_guests__incontains= 'Вики')
    viki_invitation = Invitation.objects.filter(cat_type_guests__icontains = 'Вики')
    print(viki_invitation)
    print('===============')
 
    viki_guests = []

    number_viki_guests_accept = len([invitation.guest_1 for invitation in viki_invitation if invitation.guest_1.accept_invitation == 'Приемам']) + len([invitation.guest_2 for invitation in viki_invitation if invitation.guest_2.accept_invitation == 'Приемам'])
    number_viki_guests_not_accept = len([invitation.guest_1 for invitation in viki_invitation if invitation.guest_1.accept_invitation == 'Отказвам']) + len([invitation.guest_2 for invitation in viki_invitation if invitation.guest_2.accept_invitation == 'Отказвам'])
    
    for invitation in viki_invitation:
        viki_guests.append(invitation.guest_1)
        viki_guests.append(invitation.guest_2)
    
    
    number_viki_guests_pending = len(viki_guests) - number_viki_guests_accept - number_viki_guests_not_accept
    print(f'number_accept:  {number_viki_guests_accept}')
    print(f'number_not_accept:  {number_viki_guests_not_accept}')
    print(f'number_pending:  {number_viki_guests_pending}')
    
    try:
        percents_viki_guests_accept = int((number_viki_guests_accept/(number_viki_guests_accept + number_viki_guests_not_accept + number_viki_guests_pending))*100)
    except:
        percents_viki_guests_accept = 0
    percentage_viki_not_ = 100 - percents_viki_guests_accept
    print('sssssssssssss')
    print(percents_viki_guests_accept)
    print(percentage_viki_not_)





    ilian_rodnini = Invitation.objects.filter(cat_type_guests='Илиан Роднини')
    ilian_friends = Invitation.objects.filter(cat_type_guests='Илиан Приятели')
    ilian_all_invitations = len(ilian_rodnini) + len(ilian_friends)
    ilian_complete_invitation_rodnini = len([inv for inv in ilian_rodnini if inv.complete==True ])
    ilian_complete_invitation_friends = len([inv for inv in ilian_friends if inv.complete==True ])
    ilian_total_complete = ilian_complete_invitation_friends + ilian_complete_invitation_rodnini
    #print(f'ILIAN TOTAL COMPLETE: {ilian_total_complete}')
    ilian_pending_invitations = ilian_all_invitations - ilian_total_complete
    print(ilian_pending_invitations)
    try:
        ilian_complete_percentage = (ilian_total_complete / ilian_all_invitations)*100
    except:
        ilian_complete_percentage = 0
    print(f'Ilian percentage COMPLETE: {ilian_complete_percentage}')
    ilian_ucomplete = 100 - ilian_complete_percentage

   
    ilian_invitation = Invitation.objects.filter(cat_type_guests__icontains = 'Илиан')
    print(ilian_invitation)
    print('===============')
 
    ilian_guests = []

    number_ilian_guests_accept = len([invitation.guest_1 for invitation in ilian_invitation if invitation.guest_1.accept_invitation == 'Приемам']) + len([invitation.guest_2 for invitation in ilian_invitation if invitation.guest_2.accept_invitation == 'Приемам'])
    number_ilian_guests_not_accept = len([invitation.guest_1 for invitation in ilian_invitation if invitation.guest_1.accept_invitation == 'Отказвам']) + len([invitation.guest_2 for invitation in ilian_invitation if invitation.guest_2.accept_invitation == 'Отказвам'])
    
    for invitation in ilian_invitation:
        ilian_guests.append(invitation.guest_1)
        ilian_guests.append(invitation.guest_2)
    
    
    number_ilian_guests_pending = len(ilian_guests) - number_ilian_guests_accept - number_ilian_guests_not_accept
    print(f'number_accept:  {number_ilian_guests_accept}')
    print(f'number_not_accept:  {number_ilian_guests_not_accept}')
    print(f'number_pending:  {number_ilian_guests_pending}')
    
    try:
        percents_ilian_guests_accept = int((number_ilian_guests_accept/(number_ilian_guests_accept+number_ilian_guests_not_accept+number_ilian_guests_pending))*100)
    except:
        percents_ilian_guests_accept = 0
    percentage_ilian_not_ = 100 - percents_ilian_guests_accept
    print('sssssssssssss')
    print(percents_ilian_guests_accept)
    print(percentage_ilian_not_)
    

    
    

    print(ilian_guests)
    context = {
        'invitations':invitations,
        'viki_complete_percentage':json.dumps(viki_complete_percentage),
        'viki_uncomplete': json.dumps(viki_ucomplete),
        'ilian_complete_percentage':json.dumps(ilian_complete_percentage),
        'ilian_uncomplete': json.dumps(ilian_ucomplete),
        'ilian_guests':ilian_guests,
        'viki_guests': viki_guests,


        'guests_viki_pending': number_viki_guests_pending,
        'guests_viki_accept': number_viki_guests_accept,
        'guests_viki_not_accept': number_viki_guests_not_accept,
        'guests_percentage_accept_viki': json.dumps(percents_viki_guests_accept),
        'guests_percentage_not_viki': json.dumps(percentage_viki_not_),

        'guests_ilian_pending': number_ilian_guests_pending,
        'guests_ilian_accept': number_ilian_guests_accept,
        'guests_ilian_not_accept': number_ilian_guests_not_accept,
        'guests_percentage_accept_ilian': json.dumps(percents_ilian_guests_accept),
        'guests_percentage_not_ilian': json.dumps(percentage_ilian_not_)


        }
    return render(request, 'wedd_app/dashboard.html', context)


# def invitation(request):
#     return render(request, 'wedd_app/invitation.html')

def logout(request):
    auth_logout(request)
    return render(request, 'registration/login.html')


def invitation_page(request, slug):
    if request.method == 'POST':
        form_1_data_dict = {}
        form_2_data_dict = {}
        print(request.POST)
        print(request.POST.get('add_guest'))

        for key in request.POST.keys():
            if key != 'add_guest':
                v = request.POST.getlist(key)
                form_1_data_dict[key] = v[0]
                form_2_data_dict[key] = v[1]

        form_1 = MainGuestForm(form_1_data_dict)
        form_2 = SecondGuestForm(form_2_data_dict)
        #print(form_1)
        print('form_1 :valid')
        print(form_1.is_valid())
        print('form_2 :valid')
        print(form_2.is_valid())
        print('pppppppppppppppppppppppppppppp')
        

        if form_1.is_valid() and form_2.is_valid():
            first_name_1 = form_1.cleaned_data['first_name']
            last_name_1 = form_1.cleaned_data['last_name']
            
            first_name_2 = form_2.cleaned_data['first_name']
            last_name_2 = form_2.cleaned_data['last_name']
            print('---------------------------------')
            print(f'first_name_form_1: {first_name_1}')
            print(f'last_name_form_1: {last_name_1}')
            print('---------------------------------')
            print(f'first_name_form_2: {first_name_2}')
            print(f'last_name_form_2: {last_name_2}')

            print('=============================================')
            return HttpResponse('Done')

        # if form_2.is_valid():
        #     first_name_2 = form_2.cleaned_data['first_name']
        # if form_1.is_valid():
        #     print('////////////////////////////////////////////')
        #     print('FORM _  1')
        #     print(form_1.cleaned_data['first_name'])
        #     print(form_2.cleaned_data['last_name'])
        # if form_2.is_valid():
        #     print('////////////////////////////////////////////')
        #     print('FORM _  2')
        #     print(form_2.cleaned_data['first_name'])
        #     print(form_2.cleaned_data['last_name'])
        #     print('////////////////////////////////////////////')
       
    
    user = Invitation.objects.get(slug_name=slug)
    # print('USER-------------------')
    # print(user.slug_name)

    invitation = Invitation.objects.filter(slug_name = user.slug_name)[0]
    # print('=========')
    # print(invitation.guests.values())
    # print('==========')
    print(invitation)


    # print(len(guests))
    # if len(guests) == 2:
    #     form_1 = GuestForm1(guests[0])
    #     form_2 = GuestForm2(guests[1])
    # elif len(guests) == 1:
    #     form_1 = GuestForm1(guests[0])
    #     form_2 = GuestForm2()
    # else:
    #     form_1 = GuestForm1()
    #     form_2 = GuestForm2()
    print(f'guest_1 = {type(invitation.guest_1)}')
    print('//////////////////////')
    print(f'guest_2 = {invitation.guest_2}')
    print(invitation.guest_1)

    if invitation.guest_2.first_name == "":
        guests_number = 1
    else:
        guests_number=2
    
    form_1 = MainGuestForm(instance= invitation.guest_1)
    form_2 = SecondGuestForm(instance= invitation.guest_2)
    

    

    context = {
            'form_1':form_1,
            'form_2':form_2,
            'slug_name':slug,
            'guests_number':guests_number
        }


    return render(request, 'wedd_app/invitation.html', context)


def all_accept(request):
    invitations = Invitation.objects.all()
    guests = []
    for invitation in invitations:
        if invitation.guest_1.first_name != '':
            guests.append(invitation.guest_1)
        if invitation.guest_2.first_name != '':
            guests.append(invitation.guest_2) 
    context = {
        'guests':guests
    }
    return render(request, 'wedd_app/all_guest.html', context)


def email_test(request):
    context = {}
    return render(request, 'wedd_app/email_template.html')



def after_submit(request, slug):
    print(f'slug: {slug}')
    invitation = Invitation.objects.filter(slug_name=slug)[0]
    accept_all = True
    if invitation.guest_1.accept_invitation == 'Отказвам' and invitation.guest_2.accept_invitation == 'Отказвам':
        accept_all = False

    print(accept_all)

    form_1 = InvitationForm()

    context = {
        'accept_all': accept_all,
        'form' : form_1
    }
    return render(request, 'wedd_app/after_submit.html', context)