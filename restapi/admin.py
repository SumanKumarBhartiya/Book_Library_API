from django.contrib import admin
from .models import Book,AuthorInfo,Review,Issue_Book,Student,Penalty
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','phone','mail','user_id']

@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display=['id','late_fine','damage_fine','lost_fine','issued_book']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['id','review_user_id','rating']

@admin.register(Issue_Book)
class Issue_BookAdmin(admin.ModelAdmin):
    list_display=['id','issue_date','return_date','is_return','book_id','student_id']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','title','category','author_name','publish_date','pages']

@admin.register(AuthorInfo)
class AuthorInfoAdmin(admin.ModelAdmin):
    list_display=['id','author_name','author_image','desc']