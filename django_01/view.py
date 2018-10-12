from django.http import HttpResponse
from django.shortcuts import render
from login import models
user_list = [{'user':'jack','passwd':'abc'}, {'user':'liam','passwd':'tmz'}]
def hello(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username+"\n"+password)
        models.UserInfo.objects.create(user=username, passwd=password)
    user_list = models.UserInfo.objects.all()

    print(user_list)
    return render(request,'hello.html', {'data':user_list})
def derive(request):
    return render(request,'derive.html')
def base(request):
    return render(request,'base.html')