from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
import re

def index(request):
    context = {
        "username": request.user.get_username()
    }
    return render(request, "core/index.html", context)

def register(request):
    context = None

    if request.method == "POST":
        form = request.POST
        username = form['username']
        email = form['email']
        password_1 = form['password_1']
        password_2 = form['password_2']
        first_name = form["fname"]
        last_name = form['lname']
        error = None

        if not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required'
        elif not password_1:
            error = 'Password is required.'
        elif not password_2:
            error = 'Password is required.'
        elif password_1 != password_2:
            error = "Passwords don\'t match"
        elif re.match('^([a-z]*|[A-Z]*|[0-9]*|.{0,7})$', password_1):
            error = "Passwords must have at least 8 characters, an uppercase letter, and a number"
        elif not email:
            error = "Email is required."
        elif len(User.objects.filter(username=username)) > 0:
            error = f'User {username} is already registered.'.format(username)

        if error is None:
            User.objects.create_user(
                username=username,
                email=email,
                password=password_1,
                first_name=first_name,
                last_name=last_name
                )

            return redirect("login")

        context = {
        'error' : error
        }

        print(error)

    return render(request, "registration/register.html", context)
