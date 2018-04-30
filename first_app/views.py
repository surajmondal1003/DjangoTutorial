from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,users_test
from . import forms
from first_app.forms import MyModelForm

# Create your views here.


def get_all_users():
    user_list = users_test.objects.order_by('first_name')

    return user_list

def get_userbyId(id_user):
    user_info=users_test.objects.get(pk=id_user)

    return user_info




def index(request):
    #return HttpResponse("<h1>hello World</h1>")
    mydict={'insert_me':"Suraj"}

    return render(request, 'first_app/index.html', context=mydict)

def help(request):
    #return HttpResponse("<h1>hello World</h1>")
    str={'page_name':"this is help page",'number':100}

    return render(request, 'first_app/help.html', context=str)

def about(request):
    #return HttpResponse("<h1>hello World</h1>")
    str={'page_name':"This is about page"}

    return render(request, 'first_app/about.html', context=str)

def projects(request):
    #return HttpResponse("<h1>hello World</h1>")
    #str={'page_name':"This is Projects page"}

    webpage_list=AccessRecord.objects.order_by('date')
    webpage_dict={'access_record':webpage_list}
    return render(request, 'first_app/projects.html', context=webpage_dict)

def users(request):

    user_list=get_all_users()
    user_dict={'user':user_list}

    return render(request, 'first_app/users.html', context=user_dict)

def form_page(request):

    form1=forms.Myform()
    if request.method == 'POST':
        form1=forms.Myform(request.POST)

        if form1.is_valid():
            print("Validation Success")
            print("NAME :"+form1.cleaned_data['name'])
            print("EMAIL :"+form1.cleaned_data['email'])
            print("TEXT :"+form1.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form':form1})



def model_form_page(request):

    form2=MyModelForm()
    if request.method == 'POST':
        form2=MyModelForm(request.POST)

        if form2.is_valid():
            form2.save(commit=True)
            return users(request)
        else:
            print("Error..")

    return render(request, 'first_app/model_form_page.html', {'form': form2})

def edit_model_form_page(request,id_user):
    user_info=get_userbyId(id_user)


    if request.method == 'POST':
        form2=MyModelForm(request.POST,instance=user_info)

        if form2.is_valid():
            form2.save(commit=True)
            return users(request)
        else:
            print("Error..")
    else:
        form2 = MyModelForm(instance=user_info)

    return render(request, 'first_app/model_form_page.html', {'form': form2})


def del_model_form_page(request,id_user):
    userinfo = get_userbyId(id_user)
    if userinfo:
        userinfo.delete()

    return users(request)

def error_404(request):
        data = {}
        return render(request, 'first_app/404.html', data)

def error_500(request):
    data = {}
    return render(request, 'first_app/404.html', data)

