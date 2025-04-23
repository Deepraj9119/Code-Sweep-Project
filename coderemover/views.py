from django.shortcuts import render
from coderemover.unusedfinder import get_unused_resources

def UnusedChecker(request):
    if request.method == 'POST':

        url = request.POST.get('url')
        if url is None:
            return render(request, 'checkunused.html', {'error': 'URL is required.'})
        
        unused_resources = [] 

        unused_resources = get_unused_resources(url)

        print(unused_resources)
        context = {
            'unused_resources': unused_resources,
            'url': url,
        }

        return render(request, 'result.html', context)
    else:
        # Render the initial form
        return render(request, 'checkunused.html')