# from django.urls import path

# from.views import HomePageview ,IndexPageview

# urlpatterns = [
    # path('home/',HomePageview.as_view(),name='home_page'),
    # path('index/',IndexPageview.as_view(),name='index_page'),
    # path('home/',HomePageview,name='home_page'),
    # path('index/',IndexPageview ,name='index_page'),
# ]
# urls.py
# from django.urls import path
# from .views import HomePageview, IndexPageview

# urlpatterns = [
#     path('', HomePageview.as_view(), name='home'),
#     path('index/', IndexPageview.as_view(), name='index'),
# ]
from django.urls import path
from .views import HomePageView, IndexPageView, IndexView

urlpatterns = [
    path('', IndexView, name='index'),
    path('home/', HomePageView.as_view(), name='home'),
    path('index/', IndexPageView.as_view(), name='index_page'),
]


