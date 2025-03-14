from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Author, Genre, Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    genre_id = request.GET.get('genre_id')
    if genre_id:
        posts = Post.objects.filter(genre__id=genre_id)
    else:
        posts = Post.objects.all()
    
    paginator = Paginator(posts, 6)  # Показывать 5 постов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    genres = Genre.objects.all()
    context = {
        'page_obj': page_obj,
        'genres': genres
    }
    return render(request, 'djangoPosts/post_list.html', context)

# Остальные представления остаются без изменений


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


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request, 'djangoPosts/create_post.html', context)