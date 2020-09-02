from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
from django.http import HttpResponse
from .models import Finch, Toy, Feeding
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Define the home view


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    toys_finch_doesnt_have = Toy.objects.exclude(
        id__in=finch.toys.all().values_list('id'))

    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        # include the cat and feeding_form in the context
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })
    # return render(request, 'finches/detail.html', {'finch': finch})


def assoc_toy(request, finch_id, toy_id):
    f = Finch.objects.get(id=finch_id)
    f.toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)


def remove_toy(request, finch_id, toy_id):
    f = Finch.objects.get(id=finch_id)
    print("i am here")
    f.toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)


def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'finches/index.html', {'finches': toys})


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

# uses the same form as createview form


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
