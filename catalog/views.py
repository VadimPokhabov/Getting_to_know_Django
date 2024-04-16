from django.shortcuts import render
from catalog.user_cases import save_feedback


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        save_feedback(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

    return render(request, 'catalog/contacts.html')
