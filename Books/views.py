from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django.utils.dateparse import parse_date


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList1(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookList(generics.ListCreateAPIView):
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         author_id = self.kwargs['author_id']
#         return Book.objects.filter(author_id=author_id)


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        queryset = Book.objects.filter(author_id=author_id)
        publication_date = self.request.query_params.get('publication_date', None)
        if publication_date is not None:
            queryset = queryset.filter(publication_date=parse_date(publication_date))
        return queryset


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


