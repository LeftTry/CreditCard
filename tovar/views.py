from django.shortcuts import render
from django.http import HttpResponse
import random
def index(request):
    if request.method == 'GET':
        persons = ['Лупа', 'Пупа']
        user = random.choice(persons)

        return render(request, 'interactivecard_html/card.html', {'user': user})
    if request.method == 'POST':
        f=open('type.txt','w')
        f.write(request.POST['1c'])
        f.write(request.POST['2c'])
        f.write(request.POST['3c'] + '\n')
        f.write(request.POST['1y'])
        f.write(request.POST['2y'] + '\n')
        f.write(request.POST['name'] + '\n')
        f.write(request.POST['cvc'] + '\n')
        f.close()

        return HttpResponse('')