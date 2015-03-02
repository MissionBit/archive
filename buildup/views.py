from datetime import datetime
from random import randint
import subprocess

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from buildup.models import Fact

def hello(request):
    return HttpResponse("Hello world!")

def time(request):
    return render(request, "time.html", { "current_time": str(datetime.now()) })

def random(request):
    return render(request, "random.html", { "random_number": randint(0, 10) })

def hello_template(request, yourname):
    return render(request, "hello.html", { "yourname": yourname, "foobar": 12 })

def speak(request, sentence):
    subprocess.call(["say", sentence])
    return render(request, "speak.html")

def all_facts(request):
    return render(request, "all_facts.html", { "facts": Fact.objects.all() })

class FactForm(forms.Form):
    text = forms.CharField(label="A random fact", max_length=255)

@login_required
def new_fact(request):
    # someone wants to create a fact
    if request.method == "GET":
        form = FactForm()
        return render(request, "new_fact.html", { "form": form })
    else:
        # someone submitted the form so we need to save the data
        form = FactForm(request.POST)

        if form.is_valid():
            # save the new fact
            text = form.cleaned_data['text']
            author = request.user
            new_fact = Fact(text=text, author=author, created_date=datetime.now())
            new_fact.save()

            # and redirect to the all_facts page
            return HttpResponseRedirect(reverse('all_facts'))
        else:
            # return the form with any errors
            return render(request, "new_fact.html", { "form": form })
