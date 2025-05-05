from django.shortcuts import render, redirect
from coderemover.unusedfinder import get_unused_resources
from .models import History
import json

def UnusedChecker(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url is None:
            return render(request, 'checkunused.html', {'error': 'URL is required.'})

        unused_resources = get_unused_resources(url) or []

        # Save to history
        History.objects.create(
            url=url,
            unused_resources=json.dumps(unused_resources),
            user=request.user if request.user.is_authenticated else None
        )

        context = {
            'unused_resources': unused_resources,
            'url': url,
        }
        return render(request, 'result.html', context)
    else:
        return render(request, 'checkunused.html')

def history_view(request):
    if request.user.is_authenticated:
        history_items = History.objects.filter(user=request.user).order_by('-timestamp')
    else:
        history_items = History.objects.all().order_by('-timestamp')[:10]  # Show recent 10 for anonymous

    # Convert JSON string back to list for display
    for item in history_items:
        try:
            item.unused_resources = json.loads(item.unused_resources)
        except Exception:
            item.unused_resources = []

    return render(request, 'history.html', {'history_items': history_items})