from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    message = models.TextField()
    subject = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'İletişim formu Ayarları'
        verbose_name_plural = 'İletişim Formları'

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.name}"

class Certificate(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    class Meta:
        verbose_name = 'Sertifika formu Ayarları'
        verbose_name_plural = 'Sertifika Formu'

    def __str__(self):
        return f"{self.name}"

class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    class Meta:
        verbose_name = 'Sosyal medya formu Ayarları'
        verbose_name_plural = 'Sosyal medya formu Formu'

    def __str__(self):
        return f"{self.name}"

class Personalİnfo(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()
    school = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    lang_categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Kişisel Bilgiler formu Ayarları'
        verbose_name_plural = 'Kişisel Bilgiler Formu'

    def __str__(self):
        return f"{self.name}"
