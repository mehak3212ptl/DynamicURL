from django.shortcuts import render

# Create your views here.

# def home(request):
#     return render (request,'home.html' )

# def integer(request,pk):
#     data={
#         'data1':pk,
#     }
# data=pk
#     # return render (request,'home.html',data)
#     return render (request,'home.html',{'key':data})

# def string(request,id):
#     data=id
#     print(type(data))
#     return render (request,'home.html',{'key':data})

# def slug123(request,pkid):
#     data=pkid
#     return render (request,'home.html',{'key':data})

# def path123(request,abc):
#     data=abc
#     return render (request,'home.html',{'key':data})
def full(request,ab,abc,abcd):
    data={
        'data1':ab,
        'data2':abc,
        'data3':abcd
    }
    return render (request,'home.html',data)