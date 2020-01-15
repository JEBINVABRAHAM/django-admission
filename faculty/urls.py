from django.views.generic import TemplateView
from django.urls import path
from .import views
urlpatterns= [
 path('',TemplateView.as_view(template_name='index.html'),name='index'),
 path('logins/',TemplateView.as_view(template_name='login.html'),name='login'),
 path('fhome',TemplateView.as_view(template_name='faculty-login.html'),name='faculty-login'),
 path('faclog',views.display1,name='flogin'),
 path('dboard/',TemplateView.as_view(template_name='dashboard.html'),name='dashboard'),
 path('sleave/',TemplateView.as_view(template_name='student-leave.html'),name='student-leave'),
 path('sasses/',TemplateView.as_view(template_name='assessment.html'),name='assessment'),
 path('sattend/',TemplateView.as_view(template_name='attendence_1.html'),name='attendence_1'),
 path('facprof',TemplateView.as_view(template_name='facultyprofile.html'),name='facultyprofile'),
 path('facprofed',TemplateView.as_view(template_name='faculty-profile-edit.html'),name='faculty-profile-edit'),
 path('sout',views.logout_view,name='signout'),
 path('leavforw',TemplateView.as_view(template_name='leave-forwarded.html'),name='leave-forwarded'),
 path('leavrej',TemplateView.as_view(template_name='leave-rejected.html'),name='leave-rejected'),
 path('facdetails',views.viewfacpro,name='facultyprofile'),
 path('fedit',views.facdetailsedit,name='facedits'),
 path('fedits',views.faceditprof,name='faculty-profile-edit'),
 path('fachome',TemplateView.as_view(template_name='faculity_home_batch.html'),name='faculity_home_batch'),
 path('stdreg',TemplateView.as_view(template_name='student-reg.html'),name='student-reg'),
 path('sturr',views.display,name='studentreg'),
 path('facstudde',views.facstuddetails,name='faculity_home_batch'),



 
      
      
      



]