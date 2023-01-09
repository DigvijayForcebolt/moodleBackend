from rest_framework.decorators import  api_view
from rest_framework import status
from django.shortcuts import HttpResponse
import datetime
import requests
import json
from .helper import access_token_sf


@api_view(['POST'])
def course_created(request):
    ###Test it###
    if request.method == 'POST':
        msg = request.data
        id = msg['data'][0]
        course_data = getCourse(id)
        url = "https://chefannfoundation--appststng.sandbox.my.salesforce.com/services/apexrest/courses"
        payload = course_data
        access_token = access_token_sf()
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        # response = requests.request("POST", url, headers=headers, data=payload)
        return HttpResponse("response", status=200)
    return HttpResponse("Failed", status=400)



@api_view(['POST'])
def user_enrolled(request):
    if request.method == 'POST':
        res = request.data
        course_id = res['course_id']
        id = res['user_id']
        course_data = getCourse(course_id)
        user_data = getUser(id)
        
        enroll_info = {
            "firstname": user_data[0]["firstname"],
            "lastname": user_data[0]["lastname"],
            "email": user_data[0]["email"],
            "department":user_data[0]["department"],
            "description": user_data[0]["description"],
            "delivery_Date":"",
            "course_name":course_data[0]["fullname"],
            "is_completed":"false"
        }
        url = "https://chefannfoundation--appststng.sandbox.my.salesforce.com/services/apexrest/enrollment"
        payload = json.dumps(enroll_info)
        access_token = access_token_sf()
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }

        # response = requests.request("POST", url, headers=headers, data=payload)
        # print("userEnroll Res",response.text)
        
        return HttpResponse("response", status=200)
    return HttpResponse("Failed", status=400)

# @api_view(['POST'])
# def user_un_enrolled(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("User Un-Enrolled")
#         print(msg)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)

@api_view(['POST'])
def user_created(request):
    ### Test It ###
    if request.method == 'POST':
        msg = request.data
        print("User Created")

        # url = "chefannfoundation--cafdev.sandbox.my.salesforce.com/services/apexrest/courses"
        # payload = json.dumps(msg)
        # headers = {
        # 'Content-Type': 'application/json',
        # 'Authorization': 'Bearer 00D41000000WTE0!AQcAQMF9P03OmiaWKic_XjLKwNw17slPh2hNCWjEOr9bwWN1vHQyjQZfghdhjFNHXpWJgUeZRf7jFmxgKLnhD1dWy8KMuMob'
        # }

        # response = requests.request("POST", url, headers=headers, data=payload)
        return HttpResponse("response", status=200)
    return HttpResponse("Failed", status=400)


# @api_view(['POST'])
# def user_updated(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("User Updated")
#         id = msg['data'][0]
#         url = f"https://learn.chefannfoundation.org/webservice/rest/server.php?wstoken=64bf6dd815639858c0dcc3ad4e7c6acf&wsfunction=core_user_get_users_by_field&moodlewsrestformat=json&field=id&values[0]={id}"
#         payload={}
#         headers = {}

#         response = requests.request("GET", url, headers=headers, data=payload)

#         print(response.text)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)

# @api_view(['POST'])
# def course_completed(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("Course Completed")
#         print(msg)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)


# @api_view(['POST'])
# def user_deleted(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("User Deleted")
#         print(msg)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)

# @api_view(['POST'])
# def quiz_submitted(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("Quiz Submitted")
#         print(msg)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)

# @api_view(['POST'])
# def assignment_submitted(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("Assignment Submitted")
#         print(msg)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)

# @api_view(['POST'])
# def course_deleted(request):
#     if request.method == 'POST':
#         msg = request.data
#         print("Course Deleted")
#         print(msg)
#         return HttpResponse(msg, status=200)
#     return HttpResponse("Failed", status=400)

def getCourse(id):
        
    url = f'http://localhost/moodle/webservice/rest/server.php?wstoken=420e1fba6edb4cce5d5a8fd89687e8b2&wsfunction=core_course_get_courses&moodlewsrestformat=json&options[ids][0]={id}'

    payload={}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload).json()

    return response

def getUser(id):
    url = f"http://localhost/moodle/webservice/rest/server.php?wstoken=420e1fba6edb4cce5d5a8fd89687e8b2&wsfunction=core_user_get_users_by_field&moodlewsrestformat=json&field=id&values[0]={id}"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    return response