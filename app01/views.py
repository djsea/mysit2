from django.shortcuts import render, HttpResponse

# Create your views here.


def login(request):
    print(request.method)


    # return HttpResponse("ok")
    # return render(request, "login.html")

    # return render(request,"login.html")

    return render(request,"login.html")