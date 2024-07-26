from django.shortcuts import render


# Create your views here.

def main_page(request):
    name = 'test'
    return render(request, 'pages/main_page.html', {'name': name})