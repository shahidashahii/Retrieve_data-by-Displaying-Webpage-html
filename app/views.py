from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic_name inserted successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        Name=request.POST['Name']
        Url=request.POST['Url']
        TO=Topic.objects.get(topic_name=topic)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)[0]
        WO.save()
        return HttpResponse('webpage inserted successfully')
        
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    LAO=Webpage.objects.all()
    d={'webpage':LAO}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['au']
        date=request.POST['dt']     
        WO=Webpage.objects.get(name=name)

        AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('AccessRecord data inserted successfully')

    return render(request,'insert_accessrecord.html',d)

def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()
        
        for i in td :
             webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)

        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)
