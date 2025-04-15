from django.shortcuts import render

# Create your views here.
def UnusedChecker(request):
    return render(request, 'checkunused.html')