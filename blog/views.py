from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


# Create your views here.

@login_required()
def PostList(request):
    posts = Post.objects.filter(published=1).order_by('-created_on')[:9]
    return render(request, 'blog/blog-index.html', context={'posts': posts})


@login_required()
def PostDetail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    post = Post.objects.all().order_by('-created_on')[:3]

    # Start Comments
    comments = posts.comments.filter(active=True)
    new_comment = None

    # Comments Posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = posts
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blog-details.html',
                  context={'posts': posts, 'r_posts': post, 'comments': comments, 'new_comment': new_comment,
                           'comment_form': comment_form})


def Recent_post(request):
    R_posts = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'Rpost': R_posts
    }
    return render(request, 'partials/recent_article.html', context)
