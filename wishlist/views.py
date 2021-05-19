from django.shortcuts import render


def wishlist(request):
    """ A view that renders the wishlist page """

    return render(request, 'wishlist/wishlist.html')
