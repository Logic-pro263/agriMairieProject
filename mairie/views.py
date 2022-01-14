from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cooeperatives, Members, Partenaire, CooperativeComment, MemberComment, Galeries
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.conf import settings
from blog.views import Post
from .forms import CooperativeCommentForm, MemberCommentForm


def index(request):
    posts = Post.objects.all()[:2] #Two recent post
    liste_partenaire = Partenaire.objects.all() # list of all partners
    c_comments = CooperativeComment.objects.all().order_by('-timestamp')[:3] # three testimonials of cooperatives
    m_comments = MemberComment.objects.all().order_by('-timestamp')[:2] # three testimonials of members
    return render(request, 'mairie/index.html', context={'liste_partenaire': liste_partenaire, 'posts': posts, 'c_comments': c_comments, 'm_comments': m_comments})

@login_required()
def cooeperativeList(request):
    liste_cooeperative = Cooeperatives.objects.all().order_by('-created_at') # list of all cooperative in a database
    paginator = Paginator(liste_cooeperative, 10) # number cooperative in one page
    page_number = request.GET.get('page')  # get the number of the page
    page_objects = paginator.get_page(page_number)
    return render(request, 'mairie/list-cooep-grid.html', context={'liste_cooeperative': page_objects})

@login_required()
def womanList(request):
    liste_femmes = Members.objects.all() # list of all the woman in a database
    paginator = Paginator(liste_femmes, 10)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    return render(request, 'mairie/list-femme-grid.html', context={'liste_femmes': page_objects})

@login_required()
def detailCooperative(request, id_cooeperative):
    cooeperative = get_object_or_404(Cooeperatives, id=id_cooeperative)
    cooeperative_l = Cooeperatives.objects.all()[:4]

    # Start Comments
    comments = cooeperative.comments.filter(active=True)
    new_comment = None

    # Comments Posted
    if request.method == 'POST':
        comment_form = CooperativeCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.cooperatives = cooeperative
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CooperativeCommentForm()
    return render(request, 'mairie/detail-cooeperative.html', context={'cooeperative': cooeperative, 'cooeperative_l': cooeperative_l, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

@login_required()
def detailWoman(request, id_member):
    member = get_object_or_404(Members, id=id_member)
    member_l = Members.objects.all()[:4]

    # Start Comments
    comments = member.comments.filter(active=True)
    new_comment = None

    # Comments Posted
    if request.method == 'POST':
        comment_form = MemberCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.members = member
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = MemberCommentForm()
    return render(request, 'mairie/detail-woman.html', context={'member': member, 'member_l': member_l, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

@login_required()
def gallery(request):
    images = Galeries.objects.all().order_by('-created_on')
    return render(request, 'mairie/gallery.html', context={'image': images})

@login_required()
def about(request):
    return render(request, 'mairie/about.html', context={})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email = EmailMessage(
            subject=f"{subject} de la part de {name}",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Votre mail a été envoyé avec succès nous reprendrons contact avec vous dans un delai court ")
    return render(request, 'mairie/contact.html')

@login_required()
def search_r(request):
    search = request.GET.get('search')
    cooeperative = Cooeperatives.objects.filter(Q(name__icontains=search) |
                                                Q(name_president__icontains=search) |
                                                Q(city__icontains=search) |
                                                Q(description__icontains=search))


    member = Members.objects.filter(Q(name__icontains=search) |
                                    Q(city__icontains=search) |
                                    Q(activity__icontains=search))

    context = {
        'cooeperatives': cooeperative,
        'members': member
    }
    return render(request, 'mairie/search_result.html', context)