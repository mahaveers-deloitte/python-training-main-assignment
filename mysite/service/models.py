from django.db import models

class Issue(models.Model):
    id=models.IntegerField(primary_key=True)
    type=models.CharField(max_length=20)
    title=models.CharField(max_length=50)
    description=models.TextField()
    reporter=models.CharField(max_length=50) 
    assignee=models.CharField(max_length=50)
    status=models.CharField(max_length=20)
    #project_title=models.ForeignKey(Project, on_delete=models.CASCADE)

class Project(models.Model):
    project_id=models.IntegerField(primary_key=True)
    description=models.TextField()
    title=models.CharField(max_length=50)
    creator=models.CharField(max_length=50)
    #issue_r=models.ForeignKey(Issue,on_delete=models.PROTECT, null=True)
    issue_r=models.CharField(max_length=50)
    sprint=models.CharField(max_length=50)
    #def __str__(self):
     #   return self.title
# Create your models here.
