from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index),
    path('dashbord', views.Index),
    path('add_Student/', views.add_student),
    path('add_Book/', views.add_book),
    path('Book_issue/', views.Book_issue),
    path('search/<int:id>', views.search),
]