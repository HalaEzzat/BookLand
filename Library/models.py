from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


# Create your models here.
#from django.db import models
from django.urls import reverse

class Author(models.Model):
    name=models.CharField(max_length=100)
    bornAt=models.DateField(null=True)
    diedAt=models.DateField(null=True)
    bio=models.TextField()
    country=CountryField(default='EG')
    pic=models.ImageField(upload_to = 'images/Authors',default='no images available',null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


class Category(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('category-detail', args=[str(self.id)])


class Book(models.Model):
    name=models.CharField(max_length=100)
    publishedAt=models.DateField(null=True)
    desc=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to = 'images/Books',default='no images available',null=True)
    category=models.ManyToManyField(Category)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('book-detail', args=[str(self.id)])


class FollowList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def book_author(self):
        books=Book.objects.filter(author=self)
        return books

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
class CateList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class BookRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate= models.IntegerField(default=0)
