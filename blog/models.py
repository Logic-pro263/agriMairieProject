from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image

# Create your models here
User = get_user_model()


class Authors(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nom')
    about = models.TextField(max_length=1000, verbose_name='Description')
    image = models.ImageField(default="auser.jpg", upload_to='auh_image', null=True, blank=True)

    class Meta:
        verbose_name = "Author"

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.SET_NULL, null=True, related_name='auteur')
    image = models.ImageField(upload_to="images")
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return f"{self.title} posté par {self.author}"


class Comment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nom')
    subject = models.CharField(max_length=100, verbose_name='Sujet')
    email = models.EmailField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(verbose_name='Commentaire')
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Commentaire'

    def __str__(self):
        return f"Commentaires sur {self.post.title} par {self.full_name}"
