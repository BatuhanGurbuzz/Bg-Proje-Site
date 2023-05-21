from django.contrib import admin
from .models import Contact, Category, SocialMedia, Certificate, Personalİnfo
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'mail')

    search_fields = ('name', 'mail')
    readonly_fields = ('name', 'subject', 'mail', 'message')
    
    
    fields = ('name', 'subject', 'mail', 'message')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name','url')
    search_fields = ('name',)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name','url')
    search_fields = ('name',)

class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name','mail')
    search_fields = ('name','mail')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Personalİnfo, PersonalInfoAdmin)

