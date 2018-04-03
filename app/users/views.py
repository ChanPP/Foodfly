from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from users.models import SignupForm

User = get_user_model()

__all__ = (
    'signup_view',
)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'signup_form': form,
    }
    return render(request, 'test.html', context)