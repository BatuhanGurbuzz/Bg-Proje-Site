from django.contrib import admin
from .models import Project
# Register your models here.

admin.site.site_title = "BG Portfolyo"
admin.site.site_header = "BG Portfolyo Admin Paneli"
admin.site.index_title="BG Portfolyo Admin Paneline Hoşgeldiniz"

class ProjeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'isHome','slug')
    search_fields = ('title', 'date')
    prepopulated_fields = {'slug':('title',)}
    actions = ('is_home',)
    date_hierarchy = 'date'
    
    fields = (('title', 'slug'), 'description','image','isHome')
       

    def is_home(self, request,queryset):
        queryset.update(isHome = True)

    is_home.short_description = 'İşaretlenen projeleri anasayfaya taşı'


admin.site.register(Project, ProjeAdmin)