"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import index, course_created,  user_enrolled,  user_created

urlpatterns = [
    path('admin/', admin.site.urls),
    path("course_created/",course_created,name="course-created"),
    # path("course_deleted/",course_deleted,name="course-deleted"),
    path("user_enrolled/",user_enrolled,name="user-enrolled"),
    # path("user_un_enrolled/",user_un_enrolled,name="user-un-nrolled"),
    path("user_created/",user_created,name="user-created"),
    # path("user_deleted/",user_deleted,name="user-deleted"),
    # path("user_updated/",user_updated,name="user-updated"),
    # path("course_completed/",course_completed,name="course-completed"),
    # path("quiz_submitted/",quiz_submitted,name="quiz-submitted"),
    # path("assignment_submitted/",assignment_submitted,name="assignment-submitted"),
]
