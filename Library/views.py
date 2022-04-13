from django.http import JsonResponse
from django.views.generic import ListView, DetailView,UpdateView
from .models import Book,Author,Category,FollowList,CateList,ReadingList,WishList,BookRate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Avg,Count
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

class index(LoginRequiredMixin,TemplateView):
    def get(self,request):
        return redirect("/home/")

    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class BookList(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'book_list.html'
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'
    paginate_by = 4

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class home(LoginRequiredMixin,TemplateView):
    def get(self, request):
        if(request.user.is_superuser):
            return redirect('/admin/')
        else:
            return redirect('/profile/')

    login_url = '/login/'
    redirect_field_name = 'registration/login.html'


class profile(LoginRequiredMixin,TemplateView):

    template_name = 'registration/home.html'
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Author
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class CategoryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Category
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

def followAuth(request):
    auth_id = request.GET.get('AuthId')
    myAuth = get_object_or_404(Author, pk=auth_id)
    try:
        my_object = FollowList.objects.get(user=request.user,author=myAuth)
        data = {"AuthId": auth_id, "found": "True"}
    except FollowList.DoesNotExist:
        data={"AuthId":auth_id,"found":"False"}
        FollowList.objects.create(user=request.user,author=myAuth)
    return JsonResponse(data)


def unfollowAuth(request):
    auth_id = request.GET.get('AuthId')
    myAuth = get_object_or_404(Author, pk=auth_id)
    try:
        my_object = FollowList.objects.get(user=request.user, author=myAuth)
        FollowList.objects.filter(user=request.user, author=myAuth).delete()
        data = {"AuthId": auth_id, "found": "True"}
    except FollowList.DoesNotExist:
        data = {"AuthId": auth_id, "found": "False"}
    return JsonResponse(data)



def unfollowCate(request):
    cate_id = request.GET.get('CateId')
    myCate = get_object_or_404(Category, pk=cate_id)
    try:
        my_object = CateList.objects.get(user=request.user, category=myCate)
        CateList.objects.filter(user=request.user, category=myCate).delete()
        data = {"CateId": cate_id, "found": "True"}
    except CateList.DoesNotExist:
        data = {"CateId": cate_id, "found": "False"}
    return JsonResponse(data)

def followCate(request):
    cate_id = request.GET.get('CateId')
    myCate = get_object_or_404(Category, pk=cate_id)
    try:
        my_object = CateList.objects.get(user=request.user, category=myCate)
        data = {"CateId": cate_id, "found": "True"}
    except CateList.DoesNotExist:
        data = {"CateId": cate_id, "found": "False"}
        CateList.objects.create(user=request.user, category=myCate)
    return JsonResponse(data)

def chk_Catefollow(request):
    cate_id = request.GET.get('CateId')
    myCate = get_object_or_404(Category, pk=cate_id)
    try:
        my_object = CateList.objects.get(user=request.user, category=myCate)
        data = {"CateId": cate_id, "found": "True"}
    except CateList.DoesNotExist:
        data = {"CateId": cate_id, "found": "False"}
    return JsonResponse(data)

def chk_Authfollow(request):
    auth_id = request.GET.get('AuthId')
    myAuth = get_object_or_404(Author, pk=auth_id)
    try:
        my_object = FollowList.objects.get(user=request.user,author=myAuth)
        data = {"AuthId": auth_id, "found": "True"}
    except FollowList.DoesNotExist:
        data={"AuthId":auth_id,"found":"False"}
    return JsonResponse(data)

def readBook(request):
    book_id = request.GET.get('BookId')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        my_object = ReadingList.objects.get(user=request.user, book=myBook)
        data = {"BookId": book_id, "found": "True"}
    except ReadingList.DoesNotExist:
        data = {"BookId": book_id, "found": "False"}
        ReadingList.objects.create(user=request.user, book=myBook)
    return JsonResponse(data)

def chk_reading(request):
    book_id = request.GET.get('BookId')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        my_object = ReadingList.objects.get(user=request.user, book=myBook)
        data = {"BookId": book_id, "found": "True"}
    except ReadingList.DoesNotExist:
        data = {"BookId": book_id, "found": "False"}
    return JsonResponse(data)

def chk_wish(request):
    book_id = request.GET.get('BookId')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        my_object = WishList.objects.get(user=request.user, book=myBook)
        data = {"BookId": book_id, "found": "True"}
    except WishList.DoesNotExist:
        data = {"BookId": book_id, "found": "False"}
    return JsonResponse(data)

def addToWish(request):
    book_id = request.GET.get('BookId')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        my_object = WishList.objects.get(user=request.user, book=myBook)
        data = {"BookId": book_id, "found": "True"}
    except WishList.DoesNotExist:
        data = {"BookId": book_id, "found": "False"}
        WishList.objects.create(user=request.user, book=myBook)
    return JsonResponse(data)

def rmfmWish(request):
    book_id = request.GET.get('BookId')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        my_object = WishList.objects.get(user=request.user, book=myBook)
        WishList.objects.filter(user=request.user, book=myBook).delete()
        data = {"BookId": book_id, "found": "True"}
    except WishList.DoesNotExist:
        data = {"BookId": book_id, "found": "False"}
    return JsonResponse(data)

class WishListList(LoginRequiredMixin,ListView):
    model = WishList
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class ReadingListList(LoginRequiredMixin,ListView):
    model = ReadingList
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class FollowListList(LoginRequiredMixin,ListView):
    model = FollowList
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

class CateListList(LoginRequiredMixin,ListView):
    model = CateList
    login_url = '/login/'
    redirect_field_name = 'registration/login.html'

def rate(request):
    book_id = request.GET.get('BookId')
    rating= request.GET.get('Score')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        my_object = BookRate.objects.get(user=request.user, book=myBook)
        BookRate.objects.filter(user=request.user, book=myBook).update(rate=rating)
        data = {"BookId": book_id, "found": "True","Score":rating}
    except BookRate.DoesNotExist:
        BookRate.objects.create(user=request.user, book=myBook,rate=rating)
        data = {"BookId": book_id, "found": "False","Score":rating}
    return JsonResponse(data)

def getRating(request):
    book_id = request.GET.get('BookId')
    myBook = get_object_or_404(Book, pk=book_id)
    try:
        myrate=BookRate.objects.filter(book=myBook).aggregate(avg=Avg('rate'))
        if myrate['avg'] is None:
            myrate['avg']=0
        Book.objects.filter(pk=book_id).update(rating=myrate['avg'])
        data = {"rate": myrate['avg'], "found": "True"}
    except WishList.DoesNotExist:
        data = {"rate": myrate['avg'], "found": "False"}
    return JsonResponse(data)


class UpdateProfile(UpdateView):
    model = User
    fields = ['first_name', 'last_name','email','username']
    success_url = reverse_lazy('home')

    template_name = 'registration/update.html'

    def get_object(self):
        return self.request.user

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

def search(request):
    search=request.GET.get("search",None)
    print(search)
    template = 'Library/search.html'
    if search is not None:
        books = Book.objects.all()
        authors = Author.objects.all()
        booksfilter = books.filter(name__icontains= search)
        authorsfilter = authors.filter(name__icontains=search)
        result = {
            "booksList" : booksfilter,
            "authorsList":authorsfilter,
        }
        print(result)
    return render(request,template,result)




def topBook(request):
    template = 'Library/topBook.html'
    books= Book.objects.order_by('-rating').distinct() [:5]

    return render(request,template,{"bookName":books})

def topAuth(request):
    template = 'Library/topAuth.html'

    topFol = FollowList.objects.values('author').annotate(countUsers=Count('user')).order_by('-countUsers').distinct() [:5]
    authorName = []
    for authobj in topFol:
        authorName.append(Author.objects.get(pk=authobj["author"]))

    return render(request, template, {"authorName": authorName})

def catelist(request):
    template = 'Library/catelist_list.html'
    catelist=CateList.objects.filter(user=request.user)
    mybooks=[]
    flag=False
    for c in catelist:
        books=Book.objects.filter(category=c.category)
        for el in books:
            if el in mybooks:
                pass
            else:
                mybooks.append(el)


    result={
        "booklist":mybooks
    }
    return render(request,template,result)

def followlist(request):
    template = 'Library/followlist_list.html'
    followlist=FollowList.objects.filter(user=request.user)
    mybooks=[]
    flag=False
    for f in followlist:
        books=Book.objects.filter(author=f.author)
        for el in books:
            mybooks.append(el)


    result={
        "booklist":mybooks
    }
    return render(request,template,result)

def readinglist(request):
    template = 'Library/readinglist_list.html'
    readlist=ReadingList.objects.filter(user=request.user)
    mybooks=[]
    flag=False
    for f in readlist:
        mybooks.append(f.book)


    result={
        "booklist":mybooks
    }
    return render(request,template,result)

def wishlist(request):
    template = 'Library/wishlist_list.html'
    wishlist=WishList.objects.filter(user=request.user)
    mybooks=[]
    flag=False
    for f in wishlist:
        mybooks.append(f.book)


    result={
        "booklist":mybooks
    }
    return render(request,template,result)
