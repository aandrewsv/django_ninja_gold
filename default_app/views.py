from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'values' not in request.session:
        request.session['values'] = []
    return render(request, 'index.html')


def process_money(request):
    if request.POST['findgold'] == 'farm':
        temp = random.randint(10,20)
        request.session['gold'] += temp
        request.session['values'].append(f"Earned {temp} gold from the {request.POST['findgold']} ({datetime.now()})")
        return redirect("/")


    if request.POST['findgold'] == 'cave':
        temp = random.randint(5,10)
        request.session['gold'] += temp
        request.session['values'].append(f"Earned {temp} gold from the {request.POST['findgold']} ({datetime.now()})")
        return redirect("/")

    if request.POST['findgold'] == 'house':
        temp = random.randint(2,5)
        request.session['gold'] += temp
        request.session['values'].append(f"Earned {temp} gold from the {request.POST['findgold']} ({datetime.now()})")   
        return redirect("/")

    if request.POST['findgold'] == 'casino':
        luck = random.randint(1,2)
        temp = random.randint(1,50)
        if luck == 1:
            request.session['gold'] += temp
            request.session['values'].append(f"Earned {temp} gold from the {request.POST['findgold']} ({datetime.now()})")
        else:
            request.session['gold'] -= temp
            request.session['values'].append(f"Lost {temp} gold from the {request.POST['findgold']} ({datetime.now()})")   
        return redirect("/")

def reset(request):
    del request.session['gold']
    del request.session['values']
    return redirect("/")
