from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def main_page(request):
    return render(request, 'pages/main_page.html')

@login_required
def settings(request):
    return render(request, 'pages/settings.html')