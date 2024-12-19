from django.urls import path
from .views import BookListCreateView, BookDetailUpdateDeleteView, MemberListCreateView, MemberDetailUpdateDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),
    path('members/', MemberListCreateView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MemberDetailUpdateDeleteView.as_view(), name='member-detail-update-delete'),
]
