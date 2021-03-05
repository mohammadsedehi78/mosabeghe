from django.shortcuts import redirect


def seller_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_seller:
            return func(request, *args, **kwargs)
        else:
            return redirect('panel')
    return wrapper
