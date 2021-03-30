from django import forms
from .models import MainGuest, SecondGuest, Invitation
from django.forms import ModelForm

class MainGuestForm(ModelForm):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['is_vegetarian'].required = True
        self.fields['accept_invitation'].required = True
        
        
    

    class Meta:
        model = MainGuest
        fields = [
            'first_name',
            'last_name',
            'email',
            'is_vegetarian',
            'accept_invitation'
        ]

        labels = {
            'first_name':'Име',
            'last_name': 'Фамилия',
            'is_vegetarian': 'Вегетарианец ли си?',
            'accept_invitation':'Какво решаваш?'
        }

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'is_vegetarian':forms.Select(attrs={'class':'form-control'}),
            'accept_invitation':forms.Select(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }

        


    def save_all_fields_from_request(self, slug):
        invitation = Invitation.objects.filter(slug_name = slug)
        print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;')
        print(self)
        guest = invitation.guest_1
        guest.first_name = self['first_name']
        print('form:')
        print(type(self))

    def clean_is_vegetarian(self):
        is_vegetarian = self.cleaned_data.get('is_vegetarian')
        if is_vegetarian != 'Не' and is_vegetarian != 'Да':
            raise forms.ValidationError('Какво ще хапваш ?')
        return is_vegetarian
        


class SecondGuestForm(ModelForm):
    

    class Meta:
        model = SecondGuest
        fields = [
            'first_name',
            'last_name',
            'is_vegetarian',
            'accept_invitation'
        ]

        labels = {
            'first_name':'Име',
            'last_name': 'Фамилия',
            'is_vegetarian': 'Вегетарианец ли си?',
            'accept_invitation':'Какво решаваш?'
        }

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'is_vegetarian':forms.Select(attrs={'class':'form-control'}),
            'accept_invitation':forms.Select(attrs={'class':'form-control'}),
            
        }

    def save_all_fields_from_request(self, request):
        self.save()
        guest = SecondGuest.objects.get(id=request.user.id)
        guest.first_name = request.POST['first_name']
        guest.last_name = request.POST['last_name']
        

        guest.is_vegetarian = request.POST['is_vegetarian']
        guest.accept_invitation = request.POST['accept_invitation']


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        fields = [
            'greeting_message_1'
        ]
        labels = {
            'greeting_message_1': 'Поздравче'
        }
        widgets = {
            'greeting_message_1':forms.Textarea(attrs={'class':'form-control'})
        }