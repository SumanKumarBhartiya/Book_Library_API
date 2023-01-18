from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    book_image=models.ImageField(upload_to='book_image',default='default_book_image.png')
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    description=models.CharField(max_length=500)
    author_name=models.CharField(max_length=50)
    publish_date=models.DateField()
    pages=models.IntegerField()
    
    def __str__(self):
        return self.title

class AuthorInfo(models.Model):
    author_name=models.CharField(max_length=50)
    author_image=models.ImageField(upload_to='author_image',default='default_author_image.png')
    desc=models.CharField(max_length=1000)

    def __str__(self):
        return str(self.author_name)

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()
    desc=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.review_user.username

#Adding new models Student and Issue_Book
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10,default="")
    mail=models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Issue_Book(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    issue_date=models.DateTimeField(auto_now=True)
    is_return=models.BooleanField()
    is_penalty=models.BooleanField(default=True)

    @property
    def return_date(self):
        return (self.issue_date)+ (datetime.timedelta(30))
   
    def __str__(self):
        return str(self.book.title)+"--"+str(self.student.name)

#Adding penalty model if there is any problem with issued books.
class Penalty(models.Model):
    issued_book=models.ForeignKey(Issue_Book,on_delete=models.CASCADE)
    late_fine=models.PositiveIntegerField()
    damage_fine=models.PositiveIntegerField()
    lost_fine=models.PositiveIntegerField()

