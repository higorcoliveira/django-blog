from django.views.generic import DetailView, ListView

from .models import Post

# post_list é a variável montada pela view generics e usada no post_list.html

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
