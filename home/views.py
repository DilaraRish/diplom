from django.shortcuts import render
from .models import Service, Reviews, Team, Usluga, UslugaPrice, Order, Social
from .forms import OrderForm
from sample.sendmessage import send_telegram




def home(request):
    ser = Service.objects.all()
    re = Reviews.objects.all()
    team = Team.objects.all()
    social = Social.objects.all()

    context = {
        'home': ser,
        'reviews': re,
        'team': team,
        'social': social,

    }
    return render(request, "home/index.html", context)

def about(request):

    team = Team.objects.all()
    social = Social.objects.all()
    context = {

        'team': team,
        'social': social,
    }
    return render(request, "home/about.html", context)


def service(request):
    ser = Service.objects.all()
    usluga = Usluga.objects.all()
    social = Social.objects.all()


    context = {
        'home': ser,
        'usluga': usluga,
        'social': social,



    }
    return render(request, "home/service.html", context)


def contact(request):
    form = OrderForm()
    social = Social.objects.all()

    context = {
        'form': form,
        'social': social,
    }
    return render(request, "home/contact.html", context)


def thanks_page(request):
    social = Social.objects.all()
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'home/thanks.html', {'name': name, 'social': social})
    else:
        return render(request, 'home/thanks.html', {'social': social})