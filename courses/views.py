from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
# books = [{"name": "Php", "Author": "Ahmed", "details": "about php languages", "image": "one.jpeg", "id": "1"},
#          {"name": "Python", "Author": "Mohamed", "details": "about Python languages", "image": "two.jpg", "id": "2"},
#          {"name": "Networking", "Author": "Ibhrahim", "details": "about how to build a network with people",
#           "image": "one.jpg", "id": "3"},
#          {"name": "ITI", "Author": "Noura", "details": "life_in_iti", "image": "two.jpeg", "id": "4"}
#          ]
#
#
# def show_all(req):
#     # for book in books:
#     context = {"books": books}
#     return render(req, 'index.html', context)
#
#
# def book (req, id):
#     for book in books:
#         if book["id"] == id:
#             context={"book":book}
#     return render (req, "book.html", context)