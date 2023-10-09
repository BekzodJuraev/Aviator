from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from .forms import LoginForm,RegistrationForm
from .models import Profile
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
def login_page(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    #logout(request)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if next:
                return redirect(next)
            return redirect('logging')
        else:
            return redirect('/')






    context = {
        'form': form,
    }


    return render(request, "login.html", context)




class AviatorView(LoginRequiredMixin,TemplateView):
    template_name = 'aviator.html'
    login_url = reverse_lazy('login')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            profile = Profile()
            profile.username = form.cleaned_data['username']
            profile.currency = form.cleaned_data['currency']
            profile.email=form.cleaned_data['email']
            profile.save()
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)
