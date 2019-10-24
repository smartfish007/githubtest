from django.http import HttpResponse
from django.shortcuts import render,redirect
from lists.models import Item
def home_page(request):
    if request.POST:
        Item.objects.create(text=request.POST['item_text'])#objects创建一个简化的Item对象，无需调用save
        return redirect('/')
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})

# Create your views here.
