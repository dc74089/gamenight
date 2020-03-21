from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
@login_required
def admin(request):
    return render(request, "tribes/admin.html")


def admin_ajax(request):
    return render(request, "tribes/partial_admin_names.html", {"names": TribeName.objects.filter(game__active=True)})


def admin_reset(request):
    for tg in TribeGame.objects.filter(active=True):
        tg.active = False
        tg.save()

    TribeGame().save()

    return redirect('tribes_admin')


def index(request):
    if 'gameid' in request.session and request.session['gameid'] == TribeGame.objects.filter(active=True).first().id:
        return render(request, 'tribes/index.html', {'hide': True})

    if request.method == 'POST':
        if 'name' in request.POST:
            TribeName(gamename=request.POST.get("name"), game=TribeGame.objects.filter(active=True).first()).save()
            request.session['gameid'] = TribeGame.objects.filter(active=True).first().id
        return redirect('tribes')

    if not TribeGame.objects.filter(active=True).exists():
        return render(request, 'tribes/index.html', {'hide': True})

    if 'gameid' in request.session and request.session['gameid'] == TribeGame.objects.filter(active=True).first().id:
        return render(request, 'tribes/index.html', {'hide': True})

    return render(request, 'tribes/index.html')
