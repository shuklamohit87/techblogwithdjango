"""
URL configuration for techblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# For importing setting Media root and media urls
from django.conf import settings
from django.conf.urls.static import static
# End for For importing setting Media root and media urls
from techblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.HomePage,name='home'),
    path('placement/',views.Placement,name='placement'),
    path('certificate/',views.Certificate,name='certificate'),
    path('about/', views.AboutUs,name='about'),
    path('blog/', views.Blog,name='blog'),
    path('contact/', views.Contact,name='contact'),
    # path('enquiry/', views.ContactFormSave,name='enquiry'),
    path('subscribe/',views.SubscribeNews,name='subscribe'),
    path('career/',views.Career,name='career'),
    path('policy/',views.RefundPolicy,name='refundpolicy'),
    path('terms/',views.TermsConditions,name='termscondition'),
    path('privacy/',views.PrivacyPolicy,name='privacypolicy'),
    path('campus-training/',views.Campus,name='campus'),
    path('corporate-training/',views.Corporate,name='corporate'),
    path('classroom-training/',views.Classroom,name='classroom'),
    path('industrial-training/',views.Industrial,name='industrial'),
    path('details/<slug>',views.PostDetails),
    path('searchquery/',views.SearchPosts,name='details'),
    path('categoryposts/<id>',views.CategoryPosts),
    path('applycertificate/',views.ApplyForCertificate,name='applycertificate'),
    path("downloadcertificate/",views.DownloadCertificate,name="downloadcertificate"),
    path('viewcertificate/<studentid>',views.ViewCertificate,name='viewcertificate'),
    path('verifycertificate/',views.VerifyCertificate, name="verifycertificate"),
    path('studentexists/',views.StudentExists,name='studentexists'),
    path('course-category/<slug>/',views.CourseDetails,name='coursecategory')
    # path('generate-pdf', views.generate_pdf, name='generate-pdf')
    # path('details/<int:courseid>', views.blogDetails),
]

admin.site.site_header  =  "TechCampus Panel"  
admin.site.site_title  =  "TechCampus"
admin.site.index_title  =  "TechCampus Admin"


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)