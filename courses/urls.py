from django.urls import path
from courses.views import show_all, book,delete,create,edit






urlpatterns = [
    path('',show_all),
    path('create', create),

    path('<id>', book),
    path('delete/<id>', delete),
    path('edit/<id>', edit),

]