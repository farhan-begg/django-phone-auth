from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# from accounts.forms import UserRegisterForm
from .forms import UserRegisterForm, UserLoginForm


# def register(request):
#     context={}
#     if request.POST:
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         context['register_form']=form

#     else:
#         form=UserRegistrationForm()
#         context['register_form']=form
#     return render(request, "account/register.html")


# def login_view(request):
#     return render(request, "account/login.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # messages.success(request, f'Account created for {email}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.POST:
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email_or_phone = request.POST['email_or_phone']
            password = request.POST['password']
            user = authenticate(request, email_or_phone=email_or_phone, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, "accounts/login.html", {'form': form})
