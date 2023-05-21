from django.db import models
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default="defaults/default.png", upload_to='images')
    date = models.DateField(auto_now_add=True)
    isHome = models.BooleanField(default = True)
    slug = models.SlugField(default = "", blank=True, null=True, unique=True, db_index=True)
    url = models.URLField(default = "")

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return f"{self.title}"
    
