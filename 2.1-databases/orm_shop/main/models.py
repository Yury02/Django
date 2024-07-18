from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=12)
    mileage = models.IntegerField()
    volume = models.DecimalField(max_digits=4, decimal_places=2)
    body_type = models.CharField(max_length=15, choices=BODY_TYPE_CHOICES, null=False, blank=True)
    drive_unit = models.CharField(max_length=15, choices=DRIVE_UNIT_CHOICES, null=False, blank=True)
    gearbox = models.CharField(max_length=15, choices=GEARBOX_CHOICES, null=False, blank=True)
    fuel_type = models.CharField(max_length=15, choices=FUEL_TYPE_CHOICES, null=False, blank=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255)

    # def get_cars_dict(self):
    #     return {'model': self.model, 'year': self.year}
    #
    def __str__(self):
        return f'{self.id} {self.model} {self.year} {self.color} {self.mileage} {self.volume} {self.body_type} ' \
               f'{self.drive_unit} {self.gearbox} {self.fuel_type} {self.price} {self.image}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} продал {self.car} {self.created_at}'