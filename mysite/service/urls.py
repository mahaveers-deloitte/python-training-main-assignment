from django.urls import path
from .views import ProjectList, ProjectDetails, IssueList, IssueDetails



urlpatterns = [
   path('project/', ProjectList.as_view()),
   path('project/<int:pk>/', ProjectDetails.as_view()),
   path('issue/', IssueList.as_view()),
   path('issue/<int:pk>/', IssueDetails.as_view()),
]