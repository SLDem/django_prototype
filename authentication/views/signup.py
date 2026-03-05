from django.shortcuts import render, redirect
from pyexpat.errors import messages

from authentication.forms import SignupForm
from authentication.models import User


def signup(request):
    """
    Signup using email and password.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            repeat_password = form.cleaned_data.get('password2')

            if password == repeat_password:
                username = form.cleaned_data['username']
                user.is_active = True
                user = User.objects.create(email=user.email, username=username)
                user.set_password(password)
                user.save()
            else:
                raise ValueError('Passwords do not match')
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request,
        'authentication/signup.html',
        {'form': form}
    )
