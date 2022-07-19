from django.shortcuts import render
from .forms import *
from .models import SendMailContacts

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from diplom_django_netology import configure


def sendOneMail(nameUser, emailUser, phoneUser, title, text, toaddr):
    msg = MIMEMultipart()
    msg["From"] = configure.SERVER_EMAIL
    msg["To"] = toaddr
    msg["Subject"] = title
    body = (
        "От: "
        + nameUser
        + "( почта: "
        + emailUser
        + "; телефон: "
        + phoneUser
        + ";)\n\n"
        + text
    )
    msg.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP(configure.EMAIL_HOST, configure.EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.login(configure.SERVER_EMAIL, configure.EMAIL_HOST_PASSWORD)
    text = msg.as_string()
    server.sendmail(configure.SERVER_EMAIL, toaddr, text)
    server.quit()


def sendMail(nameUser, emailUser, phoneUser, title, text):
    allMail = SendMailContacts.objects.all()
    for i in allMail:
        sendOneMail(nameUser, emailUser, phoneUser, title, text, i.email)
    sendOneMail(nameUser, emailUser, phoneUser, title, text, configure.SERVER_EMAIL)


def view_contacts(request):
    authUser = request.user.is_authenticated
    formOld = None
    valSend = False
    if request.method == "POST":
        if authUser:
            formOld = ContactFormUser(request.POST)
            if formOld.is_valid():
                valSend = True
                formPost = formOld.cleaned_data
                name = request.user.first_name + " " + request.user.last_name
                email = request.user.email
                phone = request.user.phone
                sendMail(name, email, phone, formPost["title"], formPost["text"])
        else:
            formOld = ContactFormAnonumus(request.POST)
            if formOld.is_valid():
                valSend = True
                fp = formOld.cleaned_data
                sendMail(fp["name"], fp["email"], fp["phone"], fp["title"], fp["text"])
    if authUser:
        form = ContactFormUser()
    else:
        form = ContactFormAnonumus()
    context = {"form": form, "formOld": formOld, "valSend": valSend}
    return render(request, "contacts.html", context)
