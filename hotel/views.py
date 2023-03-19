from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import signup
# Create your views here.

def index(request):
    p = []
    for ob in signup.objects.all():
        p.append(ob.Number)
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph_no = request.POST.get('number')
        password = request.POST.get('password')
        c_password = request.POST.get('conform_Password')
        Location = request.POST.get('address_search')
        if(Location != None):
            return render(request, Location + ".html")
        if(password != c_password):
            params = {'warning': "The password and confirm passwords are not matching.please try again"}
        elif (ph_no in p):
                params = {'warning': "Already signed up!!please login through credentials"}
        else:
            params = {'warning': "Signed up successfully" }
            if ph_no not in p and ph_no != "None":
                if (len(ph_no) == 10):
                    customer = signup(Name=name, Email=email, Number=ph_no, password=password, c_password=c_password)
                    customer.save()
                else:
                    print("sorry your phone number is invalid")
        return render(request,"index.html",params)
    return render(request,'index.html')