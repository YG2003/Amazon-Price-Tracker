from django.shortcuts import redirect, render
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = UserRegisterForm()
    
    context = {'form': form}

    return render(request, 'users/register.html', context)
