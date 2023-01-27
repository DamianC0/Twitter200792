from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
#/login
def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data = request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
        "form": form, 
        "btn_label": "Login", 
        "title": "Login"
    }
    return render(request, "accounts/auth.html", context)

#/logout
def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None, 
        "btn_label": "Logout", 
        "title": "Click to logout"
    }
    return render(request, "accounts/auth.html", context)

#/register
def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request, "accounts/auth.html", context)