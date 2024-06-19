from django.shortcuts import render



def test(request):
    return render(request, 'baseapp/index.html')

def about(request):
    return render(request, 'baseapp/about.html')