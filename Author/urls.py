from django.urls import path
from Books.views import AuthorList, AuthorDetail, BookList, BookDetail, BookList1

urlpatterns = [
    path('author/', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('book/', BookList1.as_view(), name='book_list'),
    path('author/<int:author_id>/book/', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
