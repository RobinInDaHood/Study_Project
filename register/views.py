from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/shop")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})

def profile(response):
    if request.user.is_authenticated:
        return render(request, 'register/profile.html')
    return render(request, 'frontpage/dick.html')


# Create your views here.
