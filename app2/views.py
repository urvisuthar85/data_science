
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login
from .models import U

# Create your views here.
default_data = {
    'projectName' : 'loan',
    'app1':'user'
}
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        all_users = U.objects,all()
        if len(all_users) == 0:
            if form.is_valid():
                u_name = form.cleaned_data['Firstname']
                P_name = form.cleaned_data['Password']
                return HttpResponse(f'{u_name} andd {P_name}')
            else:
                return HttpResponse('invalid method')
        else:
            return HttpResponse('in valid user')
    else:
        return HttpResponse('in valid')