from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username = data['username'],
                                password = data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Muvafaqqiyatli login")
                else:
                    return HttpResponse("Sizning profilingiz faol holatda emas")
            else:
                return HttpResponse("Login yoki parolda xatolik bor")
    else:
        form = LoginForm()
        context = {
            'form': form
        }
    return render(request, 'registration/login.html', context)