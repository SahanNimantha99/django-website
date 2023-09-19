from django.shortcuts import render
from .models import Destination#we have to import the model
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750

    dest4 = Destination()
    dest4.name = 'Chennai'
    dest4.desc = 'Colors Everywhere'
    dest4.img = 'destination_4.jpg'
    dest4.price = 670

    dest5 = Destination()
    dest5.name = 'Karachchi'
    dest5.desc = 'Folowers'
    dest5.img = 'destination_5.jpg'
    dest5.price = 600

    dest6 = Destination()
    dest6.name = 'Rajastan'
    dest6.desc = 'Crowd City'
    dest6.img = 'destination_6.jpg'
    dest6.price = 550

    dest7 = Destination()
    dest7.name = 'Decan'
    dest7.desc = 'Wonderful City'
    dest7.img = 'destination_7.jpg'
    dest7.price = 670

    dest8 = Destination()
    dest8.name = 'Kathmandu'
    dest8.desc = 'Tasty Noodles'
    dest8.img = 'destination_8.jpg'
    dest8.price = 650

    dest9 = Destination()
    dest9.name = 'Himalaya'
    dest9.desc = 'Rural City'
    dest9.img = 'destination_9.jpg'
    dest9.price = 750


    dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8, dest9]

    return render(request, "index.html", {'dests': dests})
