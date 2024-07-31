# from django.shortcuts import render
# from django.views import View
# from .models import UserModel

# class HomePageview(View):
#     def get(self, request):
#                 user_list = UserModel.objects.all()

#         # context ={
#         #      'my_ursers_list':user_list
#         #  }     
# return render(request,'home.html',context)
    


# class IndexPageview(View):
#     def get(self, request):

#         return render(request,'index.html')
# class HomePageview(View):
#     def get(self, request):
#         return render(request, 'home.html')


# def IndexView(request):
#     return render(request,'index.html')

# views.py
# from django.shortcuts import render
# from django.views import View

# class HomePageview(View):
#     def get(self, request):
#         return render(request, 'home.html')

# class IndexPageview(View):
#     def get(self, request):
#         return render(request, 'index.html')

# from django.shortcuts import render
# from django.views import View
# from .models import UserModel

# class HomePageView(View):
#     def get(self, request):
#         user_list = UserModel.objects.all()
#         context = {
#             'my_users_list': user_list
#         }     
#         return render(request, 'home.html', context)


# class IndexPageView(View):
#     def get(self, request):
#         return render(request, 'index.html')


# def IndexView(request):
#     return render(request, 'index.html')
# from django.shortcuts import render
# from django.views import View
# from .models import UserModel

# class HomePageView(View):
#     def get(self, request):
#         user_list = UserModel.objects.all()
#         context = {
#             'my_users_list': user_list
#         }     
#         return render(request, 'home.html', context)


# class IndexPageView(View):
#     def get(self, request):
#         return render(request, 'index.html')


# def IndexView(request):
#     return render(request, 'index.html')
from django.shortcuts import render
from django.views import View
from .models import UserModel

class HomePageView(View):
    def get(self, request):
        user_list = UserModel.objects.all()
        context = {
            'my_users_list': user_list
        }     
        return render(request, 'home.html', context)


class IndexPageView(View):
    def get(self, request):
        return render(request, 'index.html')


def IndexView(request):
    return render(request, 'index.html')
