from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm


def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})
# from django.shortcuts import render, redirect
# # from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages


# def register(request):
#     # return HttpResponse("users_app working!")
#     if request.method == "POST":
#         register_form = UserCreationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(
#                 request, ("New User Account Created, Loin to Get Started!"))
#             return redirect('register')
#     else:
#         register_form = UserCreationForm()
#     return render(request, 'register.html', {'register_form': register_form})
