from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, ForgotPasswordForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import Http404


# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Signup View
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Forgot Password View
def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        print(user.id)
        reset_link = f"http://localhost:8000/reset-password/{user.id}/"
        try:
            subject = "Password Reset Link"
            body = f"""
    <html>
        <body>
            <p>Hi there,</p>
            <p>You requested to reset your password. Click the link below to reset it:</p>
            <p><a href="{reset_link}" target="_blank">Reset Password</a></p>
            <p>If you did not request this, please ignore this email.</p>
            <br>
            <p>Regards,<br>Your Team</p>
        </body>
    </html>
    """
            
            msg = MIMEMultipart()
            msg['From'] = 'temporaryaryan09@gmail.com'
            msg['To'] = email
            msg['Subject'] = 'subject'
            msg.attach(MIMEText(body, 'html'))  
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            print("reached beginning!")
            server.login('temporaryaryan09@gmail.com', 'vsdj dsgc mrkl eowu') 
            server.sendmail('temporaryaryan09@gmail.com', email, msg.as_string())
            print("Mail sent ")
            server.quit()
        except smtplib.SMTPAuthenticationError as e:
            print(f"SMTP Authentication Error: {e}")

        except User.DoesNotExist:
            messages.error(request, "Account Not Found.")
        messages.success(request, "Password reset instructions have been sent to your email.")
    return render(request, 'forgot_password.html')


def reset_password_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User doesn't exist.")

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not new_password or not confirm_password:
            messages.error(request, "Both password fields are required.")
        elif new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password updated successfully.")
            return redirect('login') 

    return render(request, 'reset_password.html', {'user_id': user_id})


# Change Password View
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password updated successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'username': request.user.username})

# Profile View
@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'user': request.user,
    })

# Logout View
def logout_view(request):
    logout(request)
    request.session.flush() 
    return redirect('login')
