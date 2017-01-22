from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {}
    return render(request, "cooking_app/home_page.html", context)