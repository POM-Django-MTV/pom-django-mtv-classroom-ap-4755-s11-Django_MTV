from django.shortcuts import render


def book_view(request):
    return render(request, "book/index.html")
