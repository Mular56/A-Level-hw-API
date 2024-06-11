from django.urls import path
from .views import NoteListView, NoteCreateView, NoteDeleteView, UserListCreateAPIView, UserDetailAPIView


urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
    
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
