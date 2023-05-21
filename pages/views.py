from django.shortcuts import redirect, render
from pages.forms import CreateContactForm
from .models import Contact, Category, SocialMedia, Personalİnfo, Certificate
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
# Create your views here.



def index(request):
    return render(request, 'pages/index.html')

def about(request):
    social_media = SocialMedia.objects.all()
    personal_info = Personalİnfo.objects.all()
    certificate = Certificate.objects.all()
    context = {
        'social_media':social_media,
        'personal_info':personal_info,
        'certificate':certificate,
    }
    return render(request, 'pages/about.html',context)

class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = CreateContactForm
    success_url = '/contact'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        email = form.cleaned_data['mail']
        message = form.cleaned_data['message']

        mail = EmailMessage(
            f"{name} Tarafından mesaj gönderildi",
            f'Konu: {subject}\n\nEmail: {email}\n\nMesaj:{message}',
            f"Yeni Mesaj <{email}>",
            [settings.EMAIL_ADMIN],
            reply_to=[f"{email}"]
        )
        mail.send()
        form.save()
        messages.success(self.request, 'Mesajınız başarıyla gönderilmiştir.')
        return super().form_valid(form)