
from django.contrib import admin
from django.urls import path
from Taskapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view),
    path('delete/<int:id>/',views.delete_view),
]
