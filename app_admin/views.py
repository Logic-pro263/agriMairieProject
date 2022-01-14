import datetime
import xlwt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mairie.models import Cooeperatives, Members, Partenaire
from mairie.forms import cooeperativeForm, membersForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post
from .forms import blogForm


# Create your views here.
@login_required()
def dashbord(request):
    liste_cooeperative = Cooeperatives.objects.all()
    liste_femme = Members.objects.all()
    total_cooep = liste_cooeperative.count()
    total_fem = liste_femme.count()
    context = {
        'total_cooep': total_cooep,
        'total_fem': total_fem
    }
    return render(request, 'app_admin/db.html', context)



@login_required()
def listingCooeperative(request):
    sauvegarde = False
    list_cooperative = Cooeperatives.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = cooeperativeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            sauvegarde = True

            return redirect('toutes-les-cooeperatives')
    else:
        form = cooeperativeForm()

    context = {
        'list_cooperative': list_cooperative,
        'form': form,
    }
    return render(request, 'app_admin/cooeperative-list.html', context)

@login_required()
def add_cooperative(request):
    sauvegarde = False
    if request.method == 'POST':
        form = cooeperativeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            sauvegarde = True

            return redirect('toutes-les-cooeperatives')
    else:
        form = cooeperativeForm()

    context = {
        'form': form,
    }
    return render(request, 'app_admin/cooeperative-list.html', context)


@login_required()
def delete_cooeperative(request, pk):
    Cooperative = Cooeperatives.objects.get(id=pk)
    if request.method == 'POST':
        Cooperative.delete()
        return redirect('toutes-les-cooeperatives')
    return render(request, 'partials/listing-cooperative.html', context={'cooperative': Cooperative})


@login_required()
def update_cooeperative(request, pk):
    uCooeperative = Cooeperatives.objects.get(id=pk)
    if request.method == 'POST':
        form = cooeperativeForm(request.POST, request.FILES, instance=uCooeperative)
        if form.is_valid():
            form.save()
            return redirect('toutes-les-cooeperatives')
    else:
        form = cooeperativeForm(instance=uCooeperative)
    return render(request, 'app_admin/update_cooeperative.html', context={'form': form, 'uCooeperative': uCooeperative})


@login_required()
def listing_woman(request):
    sauvergarde = False
    list_woman = Members.objects.filter(user=request.user)[:10]
    if request.method == 'POST':
        form = membersForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            sauvergarde = True

            return redirect('toutes-les-femmes')
    else:
        form = membersForm()
    return render(request, 'app_admin/toute-les-femmes.html', context={'list_woman': list_woman, 'form': form})


@login_required()
def delete_woman(request, pk):
    dWoman = Members.objects.get(id=pk)
    if request.method == 'POST':
        dWoman.delete()
        return redirect('toutes-les-femmes')
    return render(request, 'app_admin/delete_woman.html', context={'femme': dWoman})


@login_required()
def update_woman(request, pk):
    uWoman = Members.objects.get(id=pk)
    if request.method == 'POST':
        form = membersForm(request.POST, request.FILES, instance=uWoman)
        if form.is_valid():
            form.save()
            return redirect('toutes-les-femmes')
    else:
        form = membersForm(instance=uWoman)
    return render(request, 'app_admin/update_woman.html', context={'form': form, 'uwoman': uWoman})


def index_post(request):
    posts = Post.objects.all().order_by('-created_on')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'app_admin/home.html', context)


def create_post(request):
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auteur = request.user
            instance.save()

            return redirect("index_post")

    else:
        form = blogForm()

    context = {
        'form': form
    }
    return render(request, 'app_admin/redac_blog.html', context)


def export_excel_c(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition'] = 'attachement; filename=Liste_des_coopératives ' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Cooperatives')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Coopératives', 'Membre', 'Présidente', 'Date de Création', 'Localisation']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Cooeperatives.objects.filter(user=request.user).values_list('name', 'members_in', 'name_president', 'creation_date', 'city')
    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response
