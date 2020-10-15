from django.shortcuts import render


def treesplittng(request):
    return render(request, 'treesplitting/treemain.html')

def desktopdisplay(request):
    return render(request, 'desktopdisplay/desktopdisplay.html')