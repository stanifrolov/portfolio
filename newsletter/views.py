from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("name")
        form_subject = form.cleaned_data.get("subject")
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        send_mail(form_subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
    else:
        print("error")

    context = {
            "form": form,
        }

    return render(request, "home.html", context)


def contact(request):
     form = ContactForm(request.POST or None)
     if form.is_valid():
        # for key,value in form.cleaned_data.items(): #iteritems() in 2.7
        #     print(key, value)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print (email, message, full_name)
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'stani_frolov@web.de']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False
                  )

     context = {
        "form": form,
      }

     return render(request, "contact.html", context)
