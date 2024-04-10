# views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def request_card(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        pin = request.POST.get('pin')
        merchantname = request.POST.get('merchantname')
        # Process the form data as needed (e.g., send email, save to database)
        return HttpResponse("Your request has been submitted successfully!")
    return render(request, 'request_card.html')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request-card/', views.request_card, name='request_card'),
]

# home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VKT Payments</title>
    <!-- Add your CSS and scripts here -->
</head>
<body>
    <div>
        <h2>VKT Payments</h2>
        <p>A safe and secure payment system you can trust!</p>
        <p>This website is completely secure and is run by Python and HTML combined, so you do not have to be worried of entering sensitive info.</p>
        <p><a href="https://wa.link/2i13xz">Message me via WhatsApp!</a></p>
    </div>
</body>
</html>

# request_card.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Card</title>
    <!-- Add your CSS and scripts here -->
</head>
<body>
    <div>
        <h2>Request a Card</h2>
        <form action="{% url 'request_card' %}" method="post">
            {% csrf_token %}
            <input type="text" name="name" placeholder="Enter your name here!" required><br>
            <input type="email" name="email" placeholder="Enter your email here!" required><br>
            <input type="password" name="pin" placeholder="Enter your new PIN here!" required><br>
            <input type="text" name="merchantname" placeholder="Enter the merchant name here" required><br>
            <button type="submit">Send</button>
        </form>
    </div>
</body>
</html>
