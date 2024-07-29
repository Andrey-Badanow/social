from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from .forms import UserRegistrationForm


# Create your views here.
@login_required
def main_page(request):
    return render(request, 'pages/main_page.html')

@login_required
def settings(request):
    return render(request, 'pages/settings.html')


class Registration_new_user(View):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form':form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
        return render(request, 'registration/register.html', {'form':form})
