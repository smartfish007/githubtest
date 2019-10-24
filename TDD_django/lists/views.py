from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    data={}
    if request.POST:
        data["new_item_text"]=request.POST['item_text']
    return render(request,'home.html',data)

# Create your views here.
