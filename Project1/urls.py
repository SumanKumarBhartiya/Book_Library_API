from django.contrib import admin
from django.urls import path,include
from restapi import views
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()


# router.register(r'book', views.BookViewSet,basename='book')
# router.register(r'book-author', views.AuthorInfoViewSet,,basename='author') 
# router.register(r'user',views.UserViewSet,,basename='user')
# router.register(r'user-review',views.ReviewViewSet,,basename='review')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'',include(router.urls)),

# Class based apiviews urls are defined here

    path('user/',views.UserAPIView.as_view()),
    path('user/<int:id>/',views.UserAPIView.as_view()),

    path('book/',views.BookAPIView.as_view()),
    path('book/<int:id>/',views.BookAPIView.as_view()),

    # path('issuebook/',views.IssueBookAPIView.as_view()),
    # path('issuebook/<int:id>/',views.IssueBookAPIView.as_view()),

    path('issuebook/user/',views.IssueBookUserAPIView.as_view()),
    path('issuebook/user/<int:userid>/',views.IssueBookUserAPIView.as_view()),
    path('issuebook/user/<int:userid>/<int:id>/',views.IssueBookUserAPIView.as_view()),

    path('review/',views.ReviewAPIView.as_view()),
    path('review/<int:id>/',views.ReviewAPIView.as_view()),

    path('penalty/',views.PenaltyAPIView.as_view()),
    path('penalty/<int:id>/',views.PenaltyAPIView.as_view()),

    path('student/',views.StudentAPIView.as_view()),
    path('student/<int:id>/',views.StudentAPIView.as_view()),

    path('author/',views.AuthorInfoAPIView.as_view()),
    path('author/<int:id>/',views.AuthorInfoAPIView.as_view()),
    
# Function based apiviews urls are defined here

    # path('book/',views.book_apiview),
    # path('book/<int:id>/',views.book_apiview),

#26-12-2022
    path('issuebook/',views.IssueBookView.as_view()),
    path('issuebook/<int:id>',views.IssueBookView.as_view()),

]