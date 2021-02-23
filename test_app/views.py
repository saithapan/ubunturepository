from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import task_list, user_profile,customer_profile,task_list2,student_test,mark_test
from .serializers import task_listSerializer,task_list_newSerializer,mark_testSerializer,student_testSerializer
from rest_framework import status
from .forms import profile_Form, customer_profile_Form
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class list_data(APIView):
    def get(self,request,*args,**kwargs):
        task = task_list.objects.all()
        print(task)
        serializer  = task_listSerializer(task,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        data1 = request.data
        print(data1)
        serializer = task_listSerializer(data = data1)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class list_update_data(APIView):
    def patch(self,request,*args,**kwargs):
        print(self.kwargs)
        task = task_list.objects.get(id = self.kwargs['pk'])
        print(task)
        serializer = task_listSerializer(instance = task, data = request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)

    def delete(self,request,*args,**kwargs):
        print(self.kwargs)
        task = task_list.objects.get(id = self.kwargs['pk'])
        print(task)
        task.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class create_profile(View):

    def get(self,request):
        form = profile_Form()
        context = {
            'form':form
        }
        return render(request,'profile_maker/create.html',context)
    
    def post(self,request):
        form = profile_Form(request.POST, request.FILES)
        print("------")
        print(form)
        if form.is_valid():
            user_pr = form.save(commit = False)
            print("#33")
            print(user_pr)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            print(user_pr)
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})


class new_details_page(View):
    def get(self, request):
        data = user_profile.objects.all()
        print(data)
        user_pr = data
        for i in user_pr:
            print(i.display_picture)
        return render(request,'profile_maker/details.html',{'user_pr': user_pr})





class customer_form(View):
    def get(self, request):
        form  = customer_profile_Form()
        context = {
            'form':form
        }
        return render(request, 'profile_maker/customer_form.html', context)


    def post(self,request):
        form = customer_profile_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        data = customer_profile.objects.all()
        return render(request,'profile_maker/customer_details.html',{'data':data})

# def newpage(request):

#     return render(request,'profile_maker/newpage.html')
class newpage(APIView):

    def get(self,request,*args,**kwargs):
        task2 = task_list2.objects.all()
        print(task2)
        serializer = task_list_newSerializer(task2,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        data = request.data
        print(data)
        serializer  = task_list_newSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class forupdate(APIView):
    def get(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        task = task_list2.objects.get(id = pk)
        serializer = task_list_newSerializer(task)
        return Response(serializer.data)
    def patch(self,request,*args,**kwargs):
        pk = self.kwargs['pk']
        print(pk)
        task = task_list2.objects.get(id = pk)
        serializer = task_list_newSerializer(instance = task,data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)        

from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def ajaxpage(request):
    data = request.GET.get('firstdata')
    print(data)
    # registration.objects.all(data = data)
    context = {
        "data":data
    }
    return JsonResponse(context)


class serial_test(APIView):
    def get(self,request,*args,**kwargs):
        a = student_test.objects.all()
        b = mark_test.objects.all().select_related()
        print(b)
        serializer = student_testSerializer(a,many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        print("hi")
        serializer = mark_testSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


