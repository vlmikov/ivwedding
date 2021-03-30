from django.db import models

# Create your models here.




class Table(models.Model):
    table_number = models.IntegerField(blank=True)
    capacity = models.IntegerField(blank=True)
    free_places = models.IntegerField(blank=True)

    def calculate_free_spaces(self):
        pass
    
    def __str__(self):
        return f"table number: {self.table_number}, capacity: {self.capacity}, free_places: {self.free_places}"









class MainGuest(models.Model):
    accept_data = [
        ('Приемам', 'Приемам поканата с удоволствие'),
        ('Отказвам', 'Любезно отказвам поканата')
    ]
    
    dinner_type = [
        ('Не', 'Не'),
        ('Да', 'Да')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    message = models.TextField(blank=True)
    email = models.EmailField(max_length=50, blank=True, error_messages = {'required':"Please Enter your Name"})
    is_vegetarian = models.CharField(max_length=2, choices=dinner_type, blank=True)
    
    accept_invitation = models.CharField(max_length=50, choices=accept_data, blank=True)
    table_num = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    #invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"name: {self.first_name} {self.last_name}, table: {self.table_num}, invitation: {self.accept_invitation}"



class SecondGuest(models.Model):
    accept_data = [
        ('Приемам', 'Приемам поканата с удоволствие'),
        ('Отказвам', 'Любезно отказвам поканата')
    ]
    
    dinner_type = [
        ('Не', 'Не'),
        ('Да', 'Да')
    ]
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    message = models.TextField(blank=True)
    #email = models.EmailField(max_length=50, blank=True)
    is_vegetarian = models.CharField(max_length=2, choices=dinner_type, blank=True)
    
    accept_invitation = models.CharField(max_length=50, choices=accept_data, blank=True)
    table_num = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    #invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"name: {self.first_name} {self.last_name}, table: {self.table_num}, invitation: {self.accept_invitation}"


class Invitation(models.Model):
    type_guest = [
        ('Вики Роднини', 'Вики Роднини'),
        ('Илиан Роднини', 'Илиан Роднини'),
        ('Вики Приятели', 'Вики Приятели'),
        ('Илиан Приятели', 'Илиан Приятели'),
        ('Кумове', 'Кумове'),
        ('Шаферки', 'Шаферки'),
    ]
    
    

    greeting_message_1 = models.TextField(blank=True)
    cat_type_guests = models.CharField(max_length=50, choices=type_guest)
    slug_name = models.CharField(max_length=70, unique=True)
    url = models.CharField(max_length=150, blank=True)
    complete = models.BooleanField(default=False)
    guest_1 = models.ForeignKey(MainGuest, on_delete=models.CASCADE, blank=True)
    guest_2 = models.ForeignKey(SecondGuest, on_delete=models.CASCADE, blank=True)
    
    
    def create_url(self):
        endpoint = 'http://127.0.0.1:8000/'
        self.url = endpoint+ 'guest/' + self.slug_name + '/'
        

    def __str__(self):
        return f"cat_type: {self.cat_type_guests}, slug_name: {self.slug_name}, status: {self.complete}"



