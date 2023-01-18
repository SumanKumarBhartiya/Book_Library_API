import datetime
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Book,AuthorInfo,Review,Issue_Book,Penalty,Student
from django.shortcuts import get_object_or_404
from .api.serializers import IssueBookSerializer,UserSerializer,BookSerializer,PenaltySerializer,AuthorInfoSerializer,ReviewSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle


# --------------------  -- 1. Class based APIView --   -----------------------

#  i. BookAPIView
class BookAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            book=Book.objects.get(id=id)
            serializer=BookSerializer(book)
            return Response(serializer.data)
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Book added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        book=Book.objects.get(id=id)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for book id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        book=Book.objects.get(id=id)
        serializer=BookSerializer(book,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for book id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None):
        book=Book.objects.get(id=id)
        book.delete()
        return Response({'message':'Book deleted'},status=status.HTTP_204_NO_CONTENT)

#  ii. AuthorInfoAPIView
class AuthorInfoAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            author=AuthorInfo.objects.get(id=id)
            serializer=AuthorInfoSerializer(author)
            return Response(serializer.data)
        authorinfo=AuthorInfo.objects.all()
        serializer=AuthorInfoSerializer(authorinfo,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=AuthorInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'AuthorInfo added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        authorinfo=AuthorInfo.objects.get(id=id)
        serializer=AuthorInfoSerializer(authorinfo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for Author id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        authorinfo=AuthorInfo.objects.get(id=id)
        serializer=AuthorInfoSerializer(authorinfo,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for Author id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None,format=None):
        authorinfo=AuthorInfo.objects.get(id=id)
        authorinfo.delete()
        return Response({'message':'Author deleted'},status=status.HTTP_204_NO_CONTENT)

#  iii.ReviewAPIView
class ReviewAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            review=Review.objects.get(id=id)
            serializer=ReviewSerializer(review)
            return Response(serializer.data)
        review=Review.objects.all()
        serializer=ReviewSerializer(review,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Review added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        review=Review.objects.get(id=id)
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for review id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        review=Review.objects.get(id=id)
        serializer=ReviewSerializer(review,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for review id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None,format=None):
        review=Review.objects.get(id=id)
        review.delete()
        return Response({'message':'Review deleted'},status=status.HTTP_204_NO_CONTENT)

#  iv.IssueBookAPIView
class IssueBookAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            issuebook=Issue_Book.objects.get(id=id)
            serializer=IssueBookSerializer(issuebook)
            return Response({"data":[serializer.data]})
        issuebook=Issue_Book.objects.all()
        serializer=IssueBookSerializer(issuebook,many=True)
        return Response({"data":serializer.data})
        
    def post(self,request):
        serializer=IssueBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'IssueBook added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        issuebook=Issue_Book.objects.get(id=id)
        serializer=IssueBookSerializer(issuebook,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for IssueBook id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        issuebook=Issue_Book.objects.get(id=id)
        serializer=IssueBookSerializer(issuebook,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for IssueBook id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None,format=None):
        issuebook=Issue_Book.objects.get(id=id)
        issuebook.delete()
        return Response({'message':'IssueBook deleted'},status=status.HTTP_204_NO_CONTENT)

#  v.UserAPIView
class UserAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            user=User.objects.get(id=id)
            serializer=UserSerializer(user)
            return Response(serializer.data)
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        user=User.objects.get(id=id)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for User id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        user=User.objects.get(id=id)
        serializer=UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for User id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None,format=None):
        user=User.objects.get(id=id)
        user.delete()
        return Response({'message':'User deleted'},status=status.HTTP_204_NO_CONTENT)

#  vi.PenaltyAPIView
class PenaltyAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            penalty=Penalty.objects.get(id=id)
            serializer=PenaltySerializer(penalty)
            return Response(serializer.data)
        penalty=Penalty.objects.all()
        serializer=PenaltySerializer(penalty,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=PenaltySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Penalty added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        penalty=Penalty.objects.get(id=id)
        serializer=PenaltySerializer(penalty,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for Penalty id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        penalty=Penalty.objects.get(id=id)
        serializer=PenaltySerializer(penalty,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for Penalty id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None,format=None):
        penalty=Penalty.objects.get(id=id)
        penalty.delete()
        return Response({'message':'Penalty deleted'},status=status.HTTP_204_NO_CONTENT)

#  vii.StudentAPIView
class StudentAPIView(APIView):
    
    def get(self,request,id=None):
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Student added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Complete data updated for Student id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id=None):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'Partial data updated for Student id: {id}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None,format=None):
        student=Student.objects.get(id=id)
        student.delete()
        return Response({'message':'Student deleted'},status=status.HTTP_204_NO_CONTENT)

#  viii.IssueBookuserAPIView
class IssueBookUserAPIView(APIView):
    
    def get(self,request,userid=None,id=None):
        if userid is not None:
            if id is not None:
                issuebookuser=Issue_Book.objects.get(id=id)
                if issuebookuser.is_penalty:
                    date=(datetime.datetime.today().date())-(issuebookuser.return_date.date())
                    if date.days <= 0:
                        total=5
                    else:
                        total=abs(date*20)
                serializer=IssueBookSerializer(issuebookuser)
                return Response({'msg':f'This is the data related to user id {userid}','penalty':total,'data':[serializer.data]})
            issuebook=Issue_Book.objects.filter(student=userid,is_return=False)
            #calculating penalty
            total=0
            for book in issuebook:
                if book.is_penalty:
                    date=(datetime.datetime.today().date())-(book.return_date.date())
                    if date.days <= 0:
                        total+=5
                    else:
                        total+=abs(date*20)

            serializer=IssueBookSerializer(issuebook,many=True)
            return Response({'msg':f'This is the data related to user id {userid}','penalty':total,'data':serializer.data})
        return Response({'message':'Please enter valid user id'})
 
 
  
 
    # def post(self,request):
    #     serializer=IssueBookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'IssueBook added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def put(self,request,id=None,):
    #     issuebook=Issue_Book.objects.get(id=id)
    #     serializer=IssueBookSerializer(issuebook,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':f'Complete data updated for IssueBook id: {id}'},status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def patch(self,request,id=None):
    #     issuebook=Issue_Book.objects.get(id=id)
    #     serializer=IssueBookSerializer(issuebook,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':f'Partial data updated for IssueBook id: {id}'},status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request,id=None,format=None):
    #     issuebook=Issue_Book.objects.get(id=id)
    #     issuebook.delete()
    #     return Response({'message':'IssueBook deleted'},status=status.HTTP_204_NO_CONTENT)


# ----------------------   -- 2. Function based apiview --   ------------------------

#  i.Book api_view
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def book_apiview(request,id=None):
    if request.method=='GET':
        if id is not None:
            book=Book.objects.get(id=id)
            serializer=BookSerializer(book)
            return Response(serializer.data,status=status.HTTP_200_OK)
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Book added successfully','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PUT':
        if id is not None:
            book=Book.objects.get(id=id)
            serializer=BookSerializer(book,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':f'Complete data updated for id {id}','data':f'{serializer.data}'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':f'No data found for id : {id}'},status=status.HTTP_204_NO_CONTENT)

    if request.method=='PATCH':
        if id is not None:
            emp=Book.objects.get(id=id)
            serializer=BookSerializer(emp,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':f'Partial data updated for id : {id}'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':f'No data found for id : {id}'},status=status.HTTP_204_NO_CONTENT)
        
    if request.method=='DELETE':
        book=Book.objects.get(id=id)
        book.delete()
        return Response({'message':'Book deleted'},status=status.HTTP_204_NO_CONTENT)


#-------------------------  -- 3. ViewSet --   -----------------------------

#  i.User viewset
class UserViewSet(viewsets.ViewSet):

    def list(self,request):
        print(f"412--------get---")
        queryset=User.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,id):
        print(f"418--------get single data---")
        queryset = User.objects.all()
        user = get_object_or_404(queryset, id=id)
        serializer=UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        print(f"425--------post---")
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        return Response(serializer.errors)

    def update(self, request, id=None):
        print(f"433--------put---")
        queryset=User.objects.all()
        user=get_object_or_404(queryset,id=id)
        serializer=UserSerializer(user,data=request.data)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, id=None):
        print(f"441--------patch---")
        queryset=User.objects.all()
        user=get_object_or_404(queryset,id=id)
        serializer=UserSerializer(user,data=request.data,partial=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, id=None):
        print(f"449--------delete---")
        queryset=User.objects.all()
        user=get_object_or_404(queryset,id=id)
        user.delete()
        return Response({"message":"User deleted successfully!!"})

#  ii.Book Viewset

class BookViewSet(viewsets.ViewSet):

    def list(self,request):
        print(f"460--------get---")
        queryset=Book.objects.all()
        serializer=BookSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,id=None):
        print(f"466--------get single---")
        queryset=Book.objects.all()
        book=get_object_or_404(queryset,id=id)
        serializer=BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        print(f"473--------post---")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book added successfully'})
        return Response(serializer.errors)

    def update(self, request, id=None):
        print(f"481--------patch---")
        queryset=Book.objects.all()
        book=get_object_or_404(queryset,id=id)
        serializer=BookSerializer(book,data=request.data)
        serializer.save()
        return Response({'message':'Book details updated completely'},serializer.data)

    def partial_update(self, request, id=None):
        print(f"489--------put---")
        queryset=Book.objects.all()
        book=get_object_or_404(queryset,id=id)
        serializer=BookSerializer(book,data=request.data,partial=True)
        serializer.save()
        return Response({'message':'Book details updated partially'},serializer.data)
    def destroy(self, request, id=None):
        print(f"496--------delete---")
        queryset=Book.objects.all()
        book=get_object_or_404(queryset,id=id)
        book.delete()
        return Response({"message":"Book deleted successfully!!"})
    
#  iii.AuthorInfo Viewset

class AuthorInfoViewSet(viewsets.ViewSet):

    def list(self,request):
        print(f"507--------get---")
        queryset=AuthorInfo.objects.all()
        serializer=AuthorInfoSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,id=None):
        print(f"513--------get single data---")
        queryset=AuthorInfo.objects.all()
        author=get_object_or_404(queryset,id=id)
        serializer=AuthorInfoSerializer(author)
        return Response(serializer.data)

    def create(self, request):
        print(f"520--------post---")
        serializer=AuthorInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Author added successfully'})
        return Response(serializer.errors)

    def update(self, request, id=None):
        print(f"528--------put---")
        queryset=AuthorInfo.objects.all()
        author=get_object_or_404(queryset,id=id)
        serializer=AuthorInfoSerializer(author,data=request.data)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, id=None):
        print(f"536--------patch---")
        queryset=AuthorInfo.objects.all()
        author=get_object_or_404(queryset,id=id)
        serializer=AuthorInfoSerializer(author,data=request.data,partial=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, id=None):
        print(f"544--------delete---")
        queryset=AuthorInfo.objects.all()
        author=get_object_or_404(queryset,id=id)
        author.delete()
        return Response({"message":"author deleted successfully!!"})

#  iv.Review Viewset

class ReviewViewSet(viewsets.ViewSet):

    def list(self,request):
        print(f"555--------get---")
        queryset=Review.objects.all()
        serializer=ReviewSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,id=None):
        print(f"561--------get single data---")
        queryset=Review.objects.all()
        review=get_object_or_404(queryset,id=id)
        serializer=ReviewSerializer(review)
        return Response(serializer.data)

    def create(self, request):
        print(f"568--------post---")
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review added successfully'})
        return Response(serializer.errors)

    def update(self, request, id=None):
        print(f"576--------put---")
        queryset=Review.objects.all()
        review=get_object_or_404(queryset,id=id)
        review(request.POST)
        review.save()
        serializer=ReviewSerializer(review)
        return Response(serializer.data)

    def partial_update(self, request, id=None):
        print(f"585--------patch---")
        pass

    def destroy(self, request, id=None):
        print(f"589--------delete---")
        queryset=Review.objects.all()
        review=get_object_or_404(queryset,id=id)
        review.delete()
        return Response({"message":"Review deleted successfully!!"})



#-----------------------  ApiView  ---------------------- 


# class IssueBookAPIView2(APIView):

#     def get(self,request,id=None):
#         id=id
#         if id is not None:
#             issue_book=Issue_Book.objects.filter(student=id)
#             #calculating penalty
#             total=0
#             for book in issue_book:
#                 if book.is_penalty:
#                     date=(datetime.datetime.today().date())-(book.return_date.date())
#                     if date.days <= 0:
#                         total+=5
#                         print(date.days)
#                     else:
#                         total+=abs(date*20)

#             serializer=IssueBookSerializer(issue_book,many=True)
#             return Response({'msg':f'This is the data related to user id {id}','penalty':total,'data':serializer.data})

#         serializer=IssueBookSerializer(Issue_Book.objects.all(),many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer=IssueBookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Book issued to the user'})
#         return Response(serializer.errors)



#----------------------Applying pagination class-----------------------------

class IssueBookView(generics.ListAPIView):
    queryset = Issue_Book.objects.all()
    # print(request.user)
    serializer_class = IssueBookSerializer
    pagination_class = PageNumberPagination
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle]