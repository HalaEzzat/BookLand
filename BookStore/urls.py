"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Library import views
#from Library.views import BookList
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('', views.index.as_view()),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(),name="signup"),
    path('update/',views.UpdateProfile.as_view(),name="update"),
    path('password/', views.change_password, name='change_password'),
    path('search/', views.search, name='search'),
    path('home/', views.home.as_view(),name="home"),
    path('topBook/', views.topBook, name='topBook'),
    path('topAuth/', views.topAuth, name='topAuth'),
    path('profile/', views.profile.as_view(), name="profile"),
    path('profile/book/',views.BookList.as_view(),name="book"),
    path('profile/book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book-detail/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('followAuthor/', views.followAuth,name="followAuth"),
    path('unfollowAuthor/', views.unfollowAuth,name="unfollowAuth"),
    path('followCate/', views.followCate,name="followCate"),
    path('unfollowCate/', views.unfollowCate,name="unfollowCate"),
    path('chk_Catefollow/', views.chk_Catefollow, name="chk_Catefollow"),
    path('chk_Authfollow/', views.chk_Authfollow, name="chk_Authfollow"),
    path('readBook/', views.readBook, name="readBook"),
    path('chk_reading/', views.chk_reading, name="chk_reading"),
    path('chk_wish/', views.chk_wish, name="chk_wish"),
    path('addToWish/', views.addToWish, name="addToWish"),
    path('rmfmWish/', views.rmfmWish, name="rmfmWish"),
    path('rate/', views.rate, name="rate"),
    path('getRating/', views.getRating, name="getRating"),
    path('profile/wishlist/', views.wishlist, name="wishlist"),
    path('profile/readinglist/', views.readinglist, name="readinglist"),
    path('profile/FollowList/', views.followlist, name="followlist"),
    path('profile/CateList/', views.catelist, name="catelist"),
    path('profile/book/author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
