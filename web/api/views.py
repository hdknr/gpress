from django.shortcuts import render

# Create your views here.


def index(request):
    meta = dict((k, v) for (k, v) in request.META.items())
    ctx = {'name': 'index', 'meta': meta}
    return render(request, 'api/index.html',context=ctx)
