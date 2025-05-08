from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, filters
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Comment, Post
from .serializers import CommentSerializer
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

@login_required  # Теперь эту страницу нельзя открыть без авторизации
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated] 

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']  # Фильтрация по полю titlen



class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи могут редактировать и удалять

    def perform_update(self, serializer):
        # Проверяем, что текущий пользователь — автор поста
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You cannot edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        # Проверяем, что текущий пользователь — автор поста
        if instance.author != self.request.user:
            raise PermissionDenied("You cannot delete this post.")
        instance.delete()


from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Только авторизованные пользователи могут создавать комментарии

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = Post.objects.get(id=post_id)
        serializer.save(post=post, author=self.request.user)  # Привязываем комментарий к посту и автору


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_id'])
        serializer.save(post=post, author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]