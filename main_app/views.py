from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import lxml
from .models import Item
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler
# Create your views here.

@login_required
def search(request):
    if request.method == "POST":
        item_url = request.POST.get("searchbox")
        maximum_price = int(request.POST.get("max_price"))
        if item_url !="" and maximum_price!="":
            user = request.user
            item_model = Item(user=user, url=item_url, max_price=maximum_price)
            item_model.save()
            return redirect('search')
    return render(request, 'main_app/search.html')

def search_price():
    
    hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en",}
    
    for element in Item.objects.all():
        user = element.user
        if element.status == False:
            user = element.user
            user_email = user.email
            item_url = element.url
            max_price = element.max_price
            

            url = requests.get(str(item_url), headers=hdr)

            soup = BeautifulSoup(url.text, "lxml")
            price_span = soup.select_one(selector="#priceblock_dealprice").text[1:].split(',')
            price = float("".join(price_span))

            if price <= max_price:
               subject = 'Your product has now reduced!!!'
               message = f"HI {user.username}, your product {item_url}, that you set to track has now reduced to {price}"
               email_from = settings.EMAIL_HOST_USER
               recipient_list = [user_email]
               send_mail(subject, message, email_from, recipient_list)
               element.status = True
               element.save()
               


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(search_price, 'interval', minutes=90)

    scheduler.start()

