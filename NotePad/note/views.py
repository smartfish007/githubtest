from django.http import HttpResponse
from django.shortcuts import render,redirect
from note.models import Item,Name
def home_page(request):
    if request.POST:
        name_input = request.POST['name_text']
        saved_Name_list=Name.objects.all()
        f=1
        for Name_list in saved_Name_list:
            if name_input==Name_list.name:
                f=-1
                break
        if f==1:
            Name.objects.create(name=name_input)
        return redirect('/note/'+name_input)
    return render(request, 'home.html')
def first_skip(request,list_name):
    data={}
    saved_Name_list = Name.objects.all()
    for _Name in saved_Name_list:
        if _Name.name==list_name:
            data["name"] = list_name
            break
    if len(data)==0:
        return redirect('/')
    else:
        saved_Name = Name.objects.get(name=data['name'])
        data['list']=saved_Name
        if request.POST:
            item_input=request.POST['list_text']
            Item.objects.create(name=saved_Name,text=item_input)
            return render(request, 'node.html', data)
    return render(request, 'node.html',data)




# Create your views here.
