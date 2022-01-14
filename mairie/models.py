from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Cooeperatives(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    name_president = models.CharField(max_length=50)
    creation_date = models.DateField()
    members_in = models.PositiveIntegerField()
    city = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="photo", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Coopératives"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('toutes-les-cooeperatives', kwargs={'pk': self.pk})

class Members(models.Model):
    HOMME = 'Homme'
    FEMME = 'Femme'
    GENDER_IN_COOPERATIVE = [
        (HOMME, 'Homme'),
        (FEMME, 'Femme'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    born_date = models.DateField()
    city = models.CharField(max_length=60)
    gender = models.CharField(
        max_length=5, choices=GENDER_IN_COOPERATIVE, default= FEMME,
    )
    phone_number = PhoneNumberField()
    activity = models.TextField()
    picture = models.ImageField(upload_to='members', null=True, blank=True)
    cooeperative = models.ForeignKey(Cooeperatives, on_delete=models.CASCADE, related_name='cooeperative')

    class Meta:
        verbose_name_plural = "Membres"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toutes-les-femmes', kwargs={'pk': self.pk})

class Partenaire(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name



class CooperativeComment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nom')
    Subject = models.CharField(max_length=100, verbose_name='Sujet')
    email = models.EmailField()
    cooperatives = models.ForeignKey(Cooeperatives, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(verbose_name='Commentaire Cooperative')
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Commentaire'

    def __str__(self):
        return f"Commentaires sur {self.cooperatives.name} par {self.full_name}"



class MemberComment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nom')
    Subject = models.CharField(max_length=100, verbose_name='Sujet')
    email = models.EmailField()
    members = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(verbose_name='Commentaire Membre')
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Commentaire'

    def __str__(self):
        return f"Commentaires sur {self.members.name} par {self.full_name}"


class Galeries(models.Model):
    image = models.ImageField(upload_to='galerie_images')
    title = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title