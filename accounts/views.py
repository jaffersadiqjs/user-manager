from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

def home(request):
    # Show a simple welcome page
    return render(request, "accounts/home.html")

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {"form": form, "profile": profile})
