import datetime


from django.shortcuts import render
from myfolder.models import Portfolio, Services, Team, Contact,Subscribe


# Create your views here.
def index(requst):
    if 'subscribe' in requst.POST:
        email=requst.POST.get('subscribe')
        Subscribe(gmail=email).save()
    elif requst.method == "POST":
        name = requst.POST.get('name')
        email = requst.POST.get('email')
        subject = requst.POST.get('subject')
        text = requst.POST.get('message')
        date = datetime.datetime.now()
        Contact(name=name, email=email, subject=subject, text=text, created_at=date).save()
    our_works = Portfolio.objects.all()
    our_teams = Team.objects.all()
    our_services = Services.objects.all()
    context = {'works': our_works,
               'teams': our_teams,
               'services': our_services

               }
    return render(requst, 'index.html', context)


def porfolio(requst):
    return render(requst, 'portfolio-details.html')
