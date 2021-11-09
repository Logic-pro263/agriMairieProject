from django.shortcuts import render, redirect
from mairie.models import Cooeperatives, Members, Partenaire
from mairie.forms import cooeperativeForm, membersForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def dashbord(request):
    liste_cooeperative = Cooeperatives.objects.all()
    liste_femme = Members.objects.all()
    total_cooep = liste_cooeperative.count()
    total_fem = liste_femme.count()
    context={
        'total_cooep': total_cooep,
        'total_fem' :total_fem
    }
    return render(request, 'app_admin/db.html', context)

@login_required()
def listingCooeperative(request):
    sauvegarde = False
    list_cooeperative = Cooeperatives.objects.filter(user=request.user).order_by('-created_at')[:10]
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
        'list_cooeperative': list_cooeperative,
        'form': form,
    }
    return render(request, 'app_admin/cooeperative-list.html', context)

@login_required()
def delete_cooeperative(request, pk):
    dCooeperative = Cooeperatives.objects.get(id=pk)
    if request.method == 'POST':
        dCooeperative.delete()
        return redirect('toutes-les-cooeperatives')
    return render(request, 'app_admin/delete_cooeperative.html')

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
    return render(request, 'app_admin/update_cooeperative.html', context={'form':form, 'uCooeperative':uCooeperative})


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
        form = membersForm(request.POST,request.FILES, instance=uWoman)
        if form.is_valid():
            form.save()
            return redirect('toutes-les-femmes')
    else:
        form = membersForm(instance=uWoman)
    return render(request, 'app_admin/update_woman.html', context={'form':form, 'uwoman':uWoman})