from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ("New User Account Created, Login to Get Started!"))
            return redirect('register')
        # if register_form.errors:
        #     password1 = register_form.data['password1']
        #     password2 = register_form.data['password2']
        #     email = register_form.data['email']
        #     for msg in register_form.errors.as_data():
        #         if msg == 'email':
        #             messages.error(request, f"Declared {email} is not valid")
        #         if msg == 'password2' and password1 == password2:
        #             messages.error(
        #                 request, f"Selected password is not strong enough. Consider that: \n Your password can’t be too similar to your other personal information. \n Your password must contain at least 8 characters. \nYour password can’t be a commonly used password. \n Your password can’t be entirely numeric.")
        #         elif msg == 'password2' and password1 != password2:
        #             messages.error(
        #                 # request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
        #                 request, "The two password fields didn’t match.")
        #         elif msg == 'username':
        #             messages.error(
        #                 # request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
        #                 request, "The username already exist.")
        #         else:
        #             messages.error(
        #                 # request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
        #                 request, "Consider that: Your password can’t be too similar to your other personal information. \n Your password must contain at least 8 characters. \nYour password can’t be a commonly used password. \n Your password can’t be entirely numeric.")
        #     return redirect('register')
    else:
        form = UserAdminCreationForm()
    return render(request, 'register.html', {'form': form})
