from django.shortcuts import render,redirect
from django.contrib.auth import login # Connecter directement
# Create your views here.
from authentication.forms import SignUpForm


def signup(request):
    """ Vue d'inscription """
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect("home")
    else:
        form=SignUpForm()
    return render(request,"auth/signup.html",context={"form":form})