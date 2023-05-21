from django import forms
from django.forms import EmailInput, TextInput, Textarea, URLInput, Widget

from pages.models import Contact, Category, SocialMedia, Certificate, Personalİnfo

# Sertifika ekleme, düzenleme, silme formu oluşturulacak. 
# İletişim formu oluşturulacak.
# Hakkımda formu oluşturmayı dene, bildiğimiz diller kısmı category temel orta ileri diye ayrılacak, kişisel bilgiler kısmında ad, soyad, mail cv bilgisi bulunacak bilgisi bulunacak, sosyal medya hesapları olacak.  

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'subject', 'mail', 'message')

        labels = {
            'name':'Adınız ve Soyadınız',
            'subject':'Konu',
            'mail': 'E-mail Adresiniz',
            'message':'Mesajınız'
        }

        widgets = {
            'name' : TextInput(attrs={"class":"form-control"}),
            'subject': TextInput(attrs={"class":"form-control"}),
            'mail': EmailInput(attrs={'class':'form-control'}),
            'message':Textarea(attrs={"class":"form-control"}),
        }

class CreateSocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ('name', 'url')

        labels = {
            'name':'Sosyal Medya Hesabı',
            'url':'Hesap Linki',
        }

        widgets = {
            'name' : TextInput(attrs={"class":"form-control"}),
            'url': URLInput(attrs={"class":"form-control"}),
        }

class CreateCertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('name', 'url')

        labels = {
            'name':'Sertifika ismi',
            'url':'Sertifika Linki',
        }

        widgets = {
            'name' : TextInput(attrs={"class":"form-control"}),
            'url': URLInput(attrs={"class":"form-control"}),
        }
