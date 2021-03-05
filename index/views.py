from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from index.models import User


def index_page(request):
    return render(
        request=request,
        template_name='index/index.html',
    )


def contact_us(request):
    has_error = False
    if request.method == 'POST':
        title = request.POST.get('title', False)
        email = request.POST.get('email', False)
        text = request.POST.get('text', False)
        if (len(text) < 10) or (len(text) > 250) or (not email) or (not title) or (not text):
            has_error = True
        if not has_error:
            # send email
            send_mail(
                subject=title,
                from_email=settings.EMAIL_HOST_USER,
                message="{}\n{}".format(email, text),
                recipient_list=["seyyedaliayati@gmail.com",
                                "webe21lopers@gmail.com", ]
            )
            return HttpResponse('<div id="done">درخواست شما ثبت شد</div>')
    return render(request, 'index/contact_us.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_page')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Login!')
    return render(
        request=request,
        template_name='index/login.html'
    )


def register(request):
    if request.method == 'POST':
        has_error = False
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        if User.objects.filter(username=username).count() > 0:
            messages.add_message(request, messages.INFO,
                                 "نام کاربری شما در سیستم موجود است")
            has_error = True

        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.add_message(request, messages.INFO,
                                 "گذرواژه و تکرار گذرواژه یکسان نیستند")
            has_error = True

        if not has_error:
            user = User.objects.create_user(
                username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
            user.save()
            #messages.add_message(request, messages.INFO, "created , thank you")
            return HttpResponseRedirect('/')

    return render(request, 'index/register.html')
