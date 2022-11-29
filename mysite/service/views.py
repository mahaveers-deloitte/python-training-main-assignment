from rest_framework import generics

from .models import Project, Issue
from .serializers import ProjectSerializer, IssueSerializer
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt import JWTAuthentication

class IssueList(generics.ListCreateAPIView):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    #authentication_classes = [ TokenAuthentication]
    #permission_classes = [ IsAuthenticated]
    #def get_queryset(self):
     #   queryset = Issue.objects.all()
      #  project_title = self.request.query_params.get('project_title')
       # if project_title is not None:
        #    queryset = queryset.filter(project_title = title)

class IssueDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()