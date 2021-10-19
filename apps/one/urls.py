#from .views import CreateEventAPIView, ListEventAPIView, EvenAPI
from .views import EvenAPI
from django.urls import path


urlpatterns = [
    # path("create", CreateEventAPIView.as_view(), name="create-event"),
    # path('list', ListEventAPIView.as_view(), name='list-view')
    path('', EvenAPI.as_view(), name='events')

]
