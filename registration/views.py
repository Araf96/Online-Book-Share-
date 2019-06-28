from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model,logout
from django.views import generic
from django.views.generic import View
from .forms import UserAccount
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm,UserProfile,UserFormAccount,ProfileForm,UserLibraryForm
from .models import UserLibrary,User,Chat,Notification
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse, Http404,JsonResponse
import json
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage









def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:sign_in'))




@login_required
@transaction.atomic
def update_home(request):
    recent_book = UserLibrary.objects.all()
    person = UserProfile.objects.get(user=request.user)
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(request.FILES or None,instance=request.user.profile)
    return render(request, 'onlinebookshare/homepage.html', {
        'person': person,
        'user_form': user_form,
        'profile_form': profile_form,
        'recent_books':recent_book
    })


@login_required
@transaction.atomic
def user_library(request):
    book_info = UserLibrary.objects.filter(user=request.user)
    return render(request, 'onlinebookshare/library.html',{'book_info':book_info})


@login_required
@transaction.atomic
def user_about(request):
    person = UserProfile.objects.get(user=request.user)
    return render(request, 'onlinebookshare/about.html',{
        'person':person
    })

@login_required
@transaction.atomic
def add_book(request):
    if request.method == 'POST':

        book_form = UserLibraryForm(request.POST, request.FILES or None)
        if book_form.is_valid():
            obj=book_form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('onlinebookshare:library')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        book_form =  UserLibraryForm(request.POST, request.FILES or None)
    return render(request, 'onlinebookshare/addBook.html', {
        'book_form': book_form
    })



@login_required
@transaction.atomic
def book_details(request,book_no):
    book_info = UserLibrary.objects.get(pk=book_no)
    return render(request, 'onlinebookshare/details.html',{'book_info':book_info})


@login_required
@transaction.atomic
def buy_book_details(request,book_no):
    book_info = UserLibrary.objects.get(pk=book_no)
    return render(request, 'onlinebookshare/details.html',{'book_info':book_info})



@login_required
@transaction.atomic
def book_delete(request,book_no):
    book_info = UserLibrary.objects.get(pk=book_no)
    book_info.delete()
    books = UserLibrary.objects.filter(user=request.user)
    return render(request,'onlinebookshare/library.html',{'books':books})



@login_required
@transaction.atomic
def book_favorite(request,book_no):
    book_info = UserLibrary.objects.get(pk=book_no)
    try:
        if book_info.isFavorite:
            book_info.isFavorite = False
        else:
            book_info.isFavorite = True
        book_info.save()
    except (KeyError, UserLibrary.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES or None, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('onlinebookshare:homepage')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'onlinebookshare/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })





class CreateAccountView(View):
    form_class = UserFormAccount
    template_name = 'onlinebookshare/sign_up.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    #return redirect('onlinebookshare:registration_form.html')
                    return HttpResponseRedirect(reverse('onlinebookshare:homepage'))

        return render(request, self.template_name, {'form': form})

class UserView(TemplateView):
    form_class = UserAccount
    template_name = 'onlinebookshare/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
            form=UserAccount(request.POST)



            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                    #return redirect('onlinebookshare:registration_form.html')
                return HttpResponseRedirect(reverse('onlinebookshare:homepage'))
            else:

                    return HttpResponseRedirect(reverse('onlinebookshare:sign_up'))





@login_required
def Home(request):
    c = Chat.objects.all()
    return render(request, "onlinebookshare/home.html", {'home': 'active', 'chat': c})

@login_required
def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

@login_required
def Messages(request):
    c = Chat.objects.all()
    return render(request, 'onlinebookshare/messages.html', {'chat': c})


@login_required
def Overview(request):
    return render(request, 'onlinebookshare/overview.html')


@login_required
def Help(request):
    return render(request, 'onlinebookshare/help.html')


@login_required
def Buy_or_Exchange(request):
    return render(request, 'onlinebookshare/buy_or_exchange.html')


@login_required
def search_books(request):
    if request.method == 'POST':
        query = request.POST.get('q',None)
        print(query)
        if query:
            queryset_list = UserLibrary.objects.filter(book_name__icontains=query)
        else:
            context = {
                "title": "No book found",
            }

            return render(request, "onlinebookshare/buy_or_exchange.html", context)

        context = {
            "object_list" : queryset_list,
            "title" : "List",
        }

        return render(request,"onlinebookshare/buy_or_exchange.html",context)
    context = {
        "title": "No book found",
    }

    return render(request, "onlinebookshare/search_results.html",context)



@login_required
def NotificatgionRead(request):
    if request.is_ajax():
        counter = Notification.objects.filter(to=request.user.username)
        hhh = list(counter.values('to', 'fromm', 'description', 'count'))
        print(hhh)
        return HttpResponse(json.dumps(hhh))
@login_required
def CreateNotification(request):
    if request.method == "POST":
        id = request.POST.get('slug')

        book_info = UserLibrary.objects.get(pk=id)

        no = Notification.objects.filter(user=request.user,book_info=book_info)
        nn = Notification.objects.exclude(user=request.user)
        hhh = list(nn.values('book_info'))
        if(no.count()==0):
            n = Notification(user=request.user,book_info=book_info,to=book_info.user.username,fromm=request.user.username,count=1,description="You are requested")
            n.save()
        return HttpResponse(json.dumps(hhh))








