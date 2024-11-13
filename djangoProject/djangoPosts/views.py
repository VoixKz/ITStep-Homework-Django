from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Genre, Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    genre_id = request.GET.get('genre_id')
    if genre_id:
        posts = Post.objects.filter(genre__id=genre_id)
    else:
        posts = Post.objects.all()
    
    genres = Genre.objects.all()
    context = {
        'posts': posts, 
        'genres': genres
    }
    return render(request, 'djangoPosts/post_list.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', id=post.id)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'djangoPosts/post.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request, 'djangoPosts/create_post.html', context)