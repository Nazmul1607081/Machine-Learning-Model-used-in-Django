from django.shortcuts import render

import pandas as pd


def home(request):

    return render(request, 'home.html')


def result(request):
    model = pd.read_pickle(r'F:\PyCharmProjects\DjangoML\newmdoel.pickle')

    li = [request.GET['sl'], request.GET['sw'], request.GET['pl'], request.GET['pw']]
    print(li)
    results = model.predict([li])
    print(result)
    context = {
        'result': results[0]
    }
    return render(request, 'result.html', context)
