from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=100,verbose_name='titre')
    sumary = models.CharField(max_length=200,verbose_name='Resume')
    date_pub = models.DateTimeField(null=True,default=timezone.now,verbose_name='Date de publication')
    content = models.TextField(default="Contenu par défaut",verbose_name='Contenu')
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
    CATEGORIE_CHOICES = [
        (1, 'Politique'),
        (2, 'Technologie'),
        (3, 'Sport'),
        (4, 'Voiture'),
        (5, 'Decouverte'),
        (6, 'Education')
    ]
    categorie= models.IntegerField(choices=CATEGORIE_CHOICES,null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='contenu')
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return f"{self.created_at}"