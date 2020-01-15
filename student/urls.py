from django.views.generic import TemplateView
from django.urls import path
from .import views
urlpatterns= [
    path('sthome',TemplateView.as_view(template_name='home.html'),name='home'),
    path('stprof',TemplateView.as_view(template_name='student-profile.html'),name='studentprofile'),
    path('stassess',TemplateView.as_view(template_name='student-assessment.html'),name='student-assessment'),
    path('stattend',TemplateView.as_view(template_name='student-attendence.html'),name='student-attendence'),
    path('stdleave',TemplateView.as_view(template_name='student-leave-management.html'),name='student-leave-management'),
    path('stdappleave',TemplateView.as_view(template_name='student-applied-leave.html'),name='student-applied-leave'),
    path('stuedit',TemplateView.as_view(template_name='student-edit.html'),name='student-edit'),
    path('stpr',views.viewstpro,name='studentprofile'),
    path('stee',views.stueditprof,name='student-edit'),
    path('sde',views.studetailsedit,name='sseditdetails'),
    path('sleave',views.stuleave,name='studleave'),
    path('sappleave',views.stuappliedleave,name='student-applied-leave'),
   
   
      
    
 
 



]