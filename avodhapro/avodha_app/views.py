from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import shop
from .forms import ModelForm


# Create your views here.
def demo(request):
    product = shop.objects.all()
    return render(request, "home1.html", {'products': product})


def details(request, book_id):
    product1 = shop.objects.get(id=book_id)
    return render(request, "details.html", {'products': product1})


def add_products(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Description = request.POST.get('Description')
        Image = request.FILES["Image"]
        Price = request.POST.get('Price')
        s = shop(Name=Name, Description=Description, Image=Image, Price=Price)
        s.save()
        print("products added")
    return render(request, "add_products.html")


def update(request, id):
    objc = shop.objects.get(id=id)
    form = ModelForm(request.POST or None, request.FILES, instance=objc)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html", {'form': form, 'objc': objc})


def delete(request, id):
    if request.method == 'POST':
        objc1 = shop.objects.get(id=id)
        objc1.delete()
        return redirect('/')
    return render(request, "delete.html")
