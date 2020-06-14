from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        activities=[]
        if request.POST['places'] == 'farm':
            gold = random.randint(10, 21)
            activities.append('Earned ' + str(gold) + ' golds from the ' + request.POST['places'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['places'] == 'cave':
            gold = random.randint(5, 11)
            activities.append('Earned ' + str(gold) + ' golds from the ' + request.POST['places'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['places'] == 'house':
            gold = random.randint(2,6)
            activities.append('Earned ' + str(gold) + ' golds from the ' + request.POST['places'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['places'] == 'casino':
            gold = random.randint(-50, 51)
            if gold >= 0:
                activities.append('Entered a casino and earned ' + str(gold) +' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                activities.append('Entered a casino and lost ' + str(gold) + ' gold... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['total_gold'] += gold
        
        if 'activities' not in request.session:
            request.session['activities'] = []
        else:
            request.session['activities'] += activities

    return redirect('/')

