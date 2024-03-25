from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from .forms import CommentForm, PostForm
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import  CommentForm
#from django.core.mail import send_mail
from django.views.decorators.http import require_POST

# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)


    return render(request,'posts/list.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.StatusChoices.published,
                            slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request,'posts/detail.html',{'post':post,
                                               'comments':comments,
                                               'form': form})

#@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,id=post_id,status=Post.StatusChoices.published)
    comment = None
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(resolve_url('core:post_detail', post_id=post_id))
    return render(request,'posts/comment.html',{'post':post,
                                                'form': form,
                                                'comment':comment
                                                })

# @require_POST
# def create_post(request):
#     form = PostForm(request.POST)
#     post = None
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()
#     return render(request,'posts/add_post.html',{'post':post,'form': form})