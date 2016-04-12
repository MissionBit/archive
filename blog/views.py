from django.shortcuts import render, render_to_response
from datetime import datetime
from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from blog.models import Review, Great_Britian
import csv

def hello(request):
    return render(request, "hello.html", { })


def hello_name(request, yourname):
    return render(request, "hello_name.html", { "yourname": yourname })

def favs(request):
    return render(request, "favorite.html", {})

def time(request):
    return render(request, "time.html", {"timeNow": datetime.now()    })




def all_reviews(request):
    return render(request, "all_reviews.html", { "revs": Review.objects.all() })





def by_title(request, game):
    if Review.objects.filter(title = game).exists():

        return render(request, "by_title.html", {"titles": Review.objects.filter(title="Pacman"), "game":game})
    else:
        return render(request, "no_game.html", {})

def random(request):
    return render(request, "random.html", {"random": Review.objects.order_by('?')[0]})


def list(request):



    with open('/data_files/Great_Britian.csv', 'rb') as csvfile:
        dataReader = csv.reader(csvfile, delimiter = ',')
        next(dataReader, None)
        for row in dataReader:
            a=Great_Britian(unit_name=row[0], class_name=row[1], description=row[2], men_count=row[3], guns=row[4], firepower=row[5], range=row[6], accuracy=row[7], reloading_skill=row[8], ammo=row[9], strength=row[10], speed=row[11], value=row[12], defense=row[13])
            a.save()
    return render(request, "list.html", {"objects": Great_Britian.objects.order_by('unit_name')})





class ReviewForm(forms.Form):
   title = forms.CharField(label="What game?", max_length=100)
   review = forms.CharField(label="What's your review?", max_length=500,widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
   name = forms.CharField(label="Your name", max_length=255)


def new_review(request):
   # someone wants to create a new review
   if request.method == "GET":
       form = ReviewForm()
       return render(request, "new_review.html", { "form": form })
   else:
       # someone submitted the form so we need to save the data
       form = ReviewForm(request.POST)

       if form.is_valid():
            title = form.cleaned_data['title']
            review = form.cleaned_data['review']
            name=form.cleaned_data['name']
            new = Review(title=title, review=review, name=name, created_date=datetime.now())
            new.save()

            return HttpResponseRedirect(reverse('all_reviews'))

       else:
            return render(request, "new_review.html", { "form": form })

