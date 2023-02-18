from django.shortcuts import render

# Create your views here.

from .models import Book, Genre

def index(request):
    num_books = Book.objects.all().count()


    return render(
        request,
        "index.html",
        context={
            "num_books": num_books
        }
    )