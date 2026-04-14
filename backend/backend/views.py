from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, JobsSerializer, ApplicationSerializer
from rest_framework import status
from django.contrib.auth.models import User
from .models import Job, Application
from django.contrib.auth import authenticate

@api_view(['GET'])
def hello_api(request):
    return Response({"message":"Hello from Django API"})


  ################ Register API ################333
@api_view(['POST'])
def register_user(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()    #save user, after save user, we return success response
        return Response({"message":"User registered successfully!"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    ##########  Login API ############
@api_view(['POST'])
def basic_login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    
    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({
            "user_id": user.id,
            "username": user.username,
            "message": "Login Successfully!"
        }, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    ##try:
    ##    user=User.objects.get(username=username, password=password)  #get the username and password from the User table, and check with above username and password
    ##   return Response({"user_id":user.id, "username":user.username,"message":"Login Successfully!"},status=status.HTTP_200_OK)
    ##except User.DoesNotExist:
    ##    return Response({"message":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)

################## Job Listing API ##################
@api_view(['GET'])
def job_list(request):
    jobs=Job.objects.all()  #'all' returns all job data
    serializer=JobsSerializer(jobs, many=True)  #'many' convert our list of jobs into dictionary 
    return Response(serializer.data)

################# Apply job API #######################
@api_view(['POST'])
def apply_job(request):
    serializer=ApplicationSerializer(data=request.data)
    #check if the application is already exist
    job_id=request.data.get("job")
    applicant_id=request.data.get("applicant")
    if Application.objects.filter(job=job_id, applicant=applicant_id).exists():
        return Response({"message":"You already have applied!!"},status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Application Submitted!!"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)