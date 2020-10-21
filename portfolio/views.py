from django.http import HttpResponseRedirect
from django.shortcuts import render

from mainpage.forms import TreeSplittingForm

from subprocess import run, PIPE
import sys
from sim_scripts import simstudy


def treesplitting(request):
    throughput = 0
    output = 'digraph {a -> b}'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TreeSplittingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            settings = {'Users': cd['users'], 'Biased_Split': cd['biased_split'], 'SPLIT': cd['split'],
                        'Branch_Prob': cd['branch_prob'], 'K': cd['k'], 'Modified': cd['modified'],
                        'Unisplit': cd['unisplit'], 'SIC': cd['sic']}

            throughput, output = simstudy.simulate_tree_branching(settings)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'treesplitting/treemain.html', {'form': form, 'data': throughput, 'dot_file': output})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TreeSplittingForm()

    return render(request, 'treesplitting/treemain.html', {'form': form, 'data': throughput, 'dot_file': output})


def desktopdisplay(request):
    return render(request, 'desktopdisplay/desktopdisplay.html')
