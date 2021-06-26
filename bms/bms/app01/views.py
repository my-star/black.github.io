from django.shortcuts import render
from .models import Author, Book, Publisher
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
def publisher_list(request):
    publishers = Publisher.objects.all().order_by('-id')
    return render(request, 'pub_list.html', {'publishers':publishers})

def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        new_publisher_addr = request.POST.get('addr')
        Publisher.objects.create(name=new_publisher_name, addr=new_publisher_addr)
        return redirect('/pub_list/')
    return render(request,'pub_add.html')

def edit_publisher(request,id):
    publisher = Publisher.objects.get(pk=id)
    context = {
        'publisher':publisher
    }
    return render(request, 'edit_publisher.html', context)