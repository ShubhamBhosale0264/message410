from django.shortcuts import redirect, render, HttpResponse
from message_app.models import Msg

def home(request):
    return HttpResponse('Page Loaded Successfully.......')

def create(request):
    if request.method == 'POST':
        n = request.POST['uname']
        m = request.POST['uemail']
        mb = request.POST['mobile']
        mesgd = request.POST['mesg']


        return redirect("/dashboard")
    else:
        # print("Request method is: " + request.method)
        return render(request, 'create.html')
def dashboard(request):
    m = Msg.objects.all()
    print(m)
    context = {}
    context['data']=m
    # return HttpResponse('dashboard is created')
    return render(request,'dashboard.html',context)
def edit(request, rid):
    if request.method == "POST":
        n = request.POST['uname']
        m = request.POST['uemail']
        mb = request.POST['mobile']
        mesgd = request.POST['mesg']
        msg_instance = Msg.objects.filter(id=rid)
        msg_instance.update(name=n, email=m, mobile=mb, mesg=mesgd)
        return redirect('/dashboard')
    else:
        data = Msg.objects.get(id=rid)
        context = {}
        context["data"] = data
        return render(request, 'edit.html', context)

    
def delete(request,rid):
    m  = Msg.objects.filter(id = rid)
    m.delete()
    return redirect('/dashboard')
