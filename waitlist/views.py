from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WaitlistForm
from .models import WaitlistEntry


def index(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if email already exists
            if WaitlistEntry.objects.filter(email=email).exists():
                messages.info(request, "You're already on the list.")
            else:
                form.save()
                messages.success(request, "Thanks for joining! We'll be in touch soon.")
            return redirect('index')
    else:
        form = WaitlistForm()
    
    return render(request, 'waitlist/index.html', {'form': form})
