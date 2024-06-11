from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.models import User
from .models import Note
from .serializers import UserSerializer, UserCreateSerializer
from .forms import NoteCreateForm
from rest_framework import generics


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    login_url = '/account/login/'
    extra_context = {'create_form': NoteCreateForm()}
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_visits'] = self.request.session['num_visits']
        return context

    def get(self, request, *args, **kwargs):
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return super().get(request, *args, **kwargs)


class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/account/login/'
    http_method_names = ['post',]
    form_class = NoteCreateForm
    success_url = '/notes/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form=form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/notes/'


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    