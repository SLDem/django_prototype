from django.shortcuts import render


def index(request):
    """
    Index view, make with this what you will.
    """
    return render(
        request,
        'authentication/index.html',
    )
