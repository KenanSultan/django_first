from django.shortcuts import render

def index(request):

    mydict = {}
    if request.method == 'POST':
        name = request.POST.get('ad', '')
        color = request.POST.get('reng', '')

        mydict['name'] = name
        mydict['color'] = color

    return render(request, 'cars.html', context = mydict)
