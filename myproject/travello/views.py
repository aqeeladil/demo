from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = 'Karachi'
    # dest1.desc = 'Capital of Sindh'
    # dest1.price = 17000
    # dest1.offer = False
    # dest1.review = 310
    # dest1.img = '1.png'

    # dest2 = Destination()
    # dest2.name = 'Islamabad'
    # dest2.desc = 'Capital of Pakistan'
    # dest2.price = 19000
    # dest2.offer = True
    # dest2.review = 480
    # dest2.img = '2.png'

    # dest3 = Destination()
    # dest3.name = 'Lahore'
    # dest3.desc = 'Capital of North Punjab'
    # dest3.price = 14000
    # dest3.offer = False
    # dest3.review = 222
    # dest3.img = '3.png'

    # dest4 = Destination()
    # dest4.name = 'Multan'
    # dest4.desc = 'Capital of South Punjab'
    # dest4.price = 11000
    # dest4.offer = False
    # dest4.review = 121
    # dest4.img = '4.png'

    # dest5 = Destination()
    # dest5.name = 'Peshawar'
    # dest5.desc = 'Capital of KPK'
    # dest5.price = 12000
    # dest5.offer = False
    # dest5.review = 541
    # dest5.img = '5.png'

    # dest6 = Destination()
    # dest6.name = 'Quetta'
    # dest6.desc = 'Capital of Balochistan'
    # dest6.price = 9000
    # dest6.offer = False
    # dest6.review = 115
    # dest6.img = '6.png'

    dests = Destination.objects.all()
    
    # dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    # return render(request, 'index.html', {'places':'09'})
    # return render(request, 'index.html', {'dests':dests})

    return render(request, 'index.html', {'dests':dests})