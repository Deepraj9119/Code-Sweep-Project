from django.shortcuts import render

def UnusedChecker(request):
    if request.method == 'POST':
        # Handle the form submission
        # You can access the form data using request.POST
        # Perform any necessary processing here
        return render(request, 'result.html', {'message': 'Form submitted successfully!'})
    else:
        # Render the initial form
        return render(request, 'checkunused.html')