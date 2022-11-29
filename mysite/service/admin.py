from django.contrib import admin
from service.models import Project
from service.models import Issue

class ServiceAdmin(admin.ModelAdmin):
    list_display=('project_id','description','title','creator')
admin.site.register(Project,ServiceAdmin)

class ServiceAdmin(admin.ModelAdmin):

    list_display=('id','type','title','description','reporter','assignee','status')

admin.site.register(Issue,ServiceAdmin)
#class ServiceProject_Manager(admin.ModelAdmin):
#    list_display=('id','type','title','description','reporter','assignee','status')
#admin.site.register(Issue,ServiceProject_Manager)
# Register your models here.
