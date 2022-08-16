from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from io import BytesIO
from PIL import Image
from django.core.files import File


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=300,  blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    is_admin_assoc = models.BooleanField(default=False)
    is_member_assoc = models.BooleanField(default=False)
    is_admin_orga = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    cin = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class   Association(models.Model):
    user = models.ForeignKey(User, related_name="admin_association", on_delete=models.CASCADE)
    nameassociation = models.CharField(max_length=30,  blank=True)
    emailassociation = models.EmailField(max_length=250 , blank=True)
    phoneassociation = models.CharField(max_length=20, null=True, blank=True)
    type=models.CharField(max_length=100, null=True, blank=True)
    addressassociation = models.CharField(max_length=300,  blank=True, null=True)
    cityassociation = models.CharField(max_length=30, blank=True, null=True)
    Objectivesassociation = models.TextField(null=True, blank=True)
    informationsassociation = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/',null=True, blank=True)
    logoassociation = models.ImageField(upload_to='uploads/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nameassociation',)
    def __str__(self):
        return self.nameassociation
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    def get_logoassociation(self):
        if self.logoassociation:
            return 'http://127.0.0.1:8000' + self.logoassociation.url
        else:
            if self.image:
                self.logoassociation = self.make_logoassociation(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.logoassociation.url
            else:
                return ''

    def make_logoassociation(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        logoassociation = File(thumb_io, name=image.name)

        return logoassociation


class   Memberassociation(models.Model):
    member_association = models.ForeignKey(User, related_name="member_association", on_delete=models.CASCADE)
    association = models.ManyToManyField(Association, related_name="name_association")
    type_member_association = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.type_member_association

class   Organization(models.Model):
    president_of_organisation = models.ForeignKey(User, related_name="president_organisation", on_delete=models.CASCADE)
    nameorganisation = models.CharField(max_length=30, unique=True, blank=True)
    emailorganisation = models.EmailField(max_length=250, unique=True)
    phoneorganisation = models.CharField(max_length=20, null=True, blank=True)
    type=models.CharField(max_length=100, null=True, blank=True)
    addressorganisation = models.CharField(max_length=300,  blank=True, null=True)
    cityorganisation = models.CharField(max_length=30, blank=True, null=True)
    Objectivesorganisation = models.TextField(null=True, blank=True)
    informationsorganisation = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/',null=True, blank=True)
    logoorganisation = models.ImageField(upload_to='uploads/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameorganisation
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    def get_logoorganisation(self):
        if self.logoorganisation:
            return 'http://127.0.0.1:8000' + self.logoorganisation.url
        else:
            if self.image:
                self.logoorganisation = self.make_logoorganisation(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.logoorganisation.url
            else:
                return ''

    def make_logoorganisation(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        logoorganisation = File(thumb_io, name=image.name)

        return logoorganisation