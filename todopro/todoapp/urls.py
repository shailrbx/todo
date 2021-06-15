
from django.urls import path
from . import  views
app_name='todoapp'
urlpatterns = [
    path('',views.index,name='index'),
    # path('details/',views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvlist/',views.tasklist.as_view(),name='cbvlist'),
    path('cbvdetails/<int:pk>',views.taskdetail.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>',views.taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.taskdelete.as_view(), name='cbvdelete'),

    ]