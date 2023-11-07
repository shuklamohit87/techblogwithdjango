# use for pdf certificate
# from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, landscape
# from reportlab.lib.pagesizes import A4
# from datetime import datetime
# end use for pdf certificate

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from django.contrib import messages
from categories.models import Course
from popularcourse.models import popularCourse
from upcomingbatches.models import upcomingBatches
from studentsay.models import studentSay
from ourclients.models import ourClients
from slider.models import sliders
from mainheader.models import mainHeader
from headermenu.models import headerMenu
from footercontact.models import footerContact
from footercontact.models import subscribeNews
from quicklinks.models import quickLinks
from businesshours.models import BusinessHours
from placement.models import placeStudent
from aboutpage.models import aboutData
from contactpage.models import contactData
from contactpage.models import ContactForm
from blogposts.models import blogPosts
from django.core.paginator import Paginator
from postcategories.models import postCategories
from termpolicy.models import termPolicy
from policy.models import Policy
from privacy.models import privacyPolicy
from certificaterequest.models import CertificateRequest,ChooseCenter
from students.models import StudentJoined
from headerservices.models import EnquiryNow
from headerservices.models import CampusTraining
from headerservices.models import CorporateTraining
from headerservices.models import ClassRoomTraining
from headerservices.models import IndustrialTraining
from submenu.models import SubMenu
def CourseDetails(request,slug):
    
    course_content = Course.objects.filter(course_title=slug)
    Coursecat = Course.objects.all()
    Popularcourse = popularCourse.objects.all()
    upcomingbatches = upcomingBatches.objects.all()
    studentsay = studentSay.objects.all()
    ourclients= ourClients.objects.all()
    slider = sliders.objects.all()
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    contactinfo = contactData.objects.all()
    submenu = SubMenu.objects.all()
    choosecenter = ChooseCenter.objects.all()
    courses = postCategories.objects.all()
    data = {
        'choosecenter':choosecenter,
        'courses':courses,
        'Coursecat' : Coursecat,
        'Popularcourse': Popularcourse,
        'upcomingBatches': upcomingbatches,
        'studentsay':studentsay,
        'ourclients':ourclients,
        'slider':slider,
        'course_content':course_content,
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'contactinfo':contactinfo,
        'submenu':submenu
    }
    return render(request,'course_category.html',data)
    
def HomePage(request):
    Coursecat = Course.objects.all()
    Popularcourse = popularCourse.objects.all()
    upcomingbatches = upcomingBatches.objects.all()
    studentsay = studentSay.objects.all()
    ourclients= ourClients.objects.all()
    slider = sliders.objects.all()
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    submenu = SubMenu.objects.all()
    
    
    data = {
        
        'Coursecat' : Coursecat,
        'Popularcourse': Popularcourse,
        'upcomingBatches': upcomingbatches,
        'studentsay':studentsay,
        'ourclients':ourclients,
        'slider':slider,
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'submenu':submenu
        
    }
    # data = {
        
    #     'WebsiteTitle' : 'Home | Welcome to techblog',
    #     'MainData': 'Welcome to techblog by Mohit',
    #     'CourseList': ['Python','Java','PHP'],
    #     'Numbers':[10,20,30,40],
    #     'StudentDetails': [
    #         {'name':'Mohit','Phone':'7856465236'},
    #         {'name':'Rohit','Phone':'8956895645'}
    #     ]
    # }
    return render(request,'index.html',data)
def AboutUs(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    aboutdata = aboutData.objects.all()
    
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'aboutdata':aboutdata
        
    }
    return render(request,'about.html',data)
def Services(request):
    return render(request,'services.html')

def Contact(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    contactinfo = contactData.objects.all()
    # aboutdata = aboutData.objects.all()
    
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'contactpageinfo':contactinfo
        # 'aboutdata':aboutdata
        
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone= request.POST.get('phone')
        message = request.POST.get('message')
        contactinfo = ContactForm(name=name,email=email,subject=subject,phone=phone,message=message)
        contactinfo.save()
        messages.success(request,'Thanks for submitted your details.We will get back to you shortly')
    return render(request,'contact.html',data)

# def ContactFormSave(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         phone= request.POST.get('phone')
#         message = request.POST.get('message')
#         contactinfo = ContactForm(name=name,email=email,subject=subject,phone=phone,message=message)
#         contactinfo.save()
#     return render(request,'contact.html')

def Placement(request):
    Coursecat = Course.objects.all()
    Popularcourse = popularCourse.objects.all()
    upcomingbatches = upcomingBatches.objects.all()
    studentsay = studentSay.objects.all()
    ourclients= ourClients.objects.all()
    slider = sliders.objects.all()
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    placement = placeStudent.objects.all()
    submenu = SubMenu.objects.all()
    data = {
        
        'Coursecat' : Coursecat,
        'Popularcourse': Popularcourse,
        'upcomingBatches': upcomingbatches,
        'studentsay':studentsay,
        'ourclients':ourclients,
        'slider':slider,
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'placement':placement,
        'submenu':submenu
    }
    return render(request,'placement.html',data)
def SubscribeNews(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       subscribed = subscribeNews(email=email)
       subscribed.save()
       messages.success(request,'You have subscribed our Newsletter.Now you will get latest updates and much more!')  
         
    return redirect('/')

def Certificate(request):
    return render(request,'certificate.html')

def Blog(request):
    
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    contactinfo = contactData.objects.all()
    blogposts = blogPosts.objects.all()
    postcategories = postCategories.objects.all()
    paginator = Paginator(blogposts,2)
    pagenumber = request.GET.get('page')
    blogpostfinalpage = paginator.get_page(pagenumber)
    totalnumpages = blogpostfinalpage.paginator.num_pages
    
    data = {
        'title' :'mohit',
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'contactpageinfo':contactinfo,
        'blogposts':blogposts,
        'postcategories':postcategories,
        'blogpostfinalpage':blogpostfinalpage,
        'lastpage':totalnumpages,
        'totalnumpages':[n+1 for n in range(totalnumpages)]
    }
    return render(request,'blog.html',data)

def Campus(request):
    
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    choosecenter = ChooseCenter.objects.all()
    courses = postCategories.objects.all()
    campustraining = CampusTraining.objects.all()
    submenu = SubMenu.objects.all()

    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'choosecenter':choosecenter,
        'courses':courses,
        'campustraining':campustraining,
        'submenu':submenu
    }
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        course=request.POST.get('choosecourse')
        center=request.POST.get('choosecenter')
        enquirynow = EnquiryNow(name=name,email=email,contact=contact,course_id=course,center_id=center)
        enquirynow.save()
        messages.success(request,"Thanks for submitted your Enquiry. we will be get back to you shortly..")
    
    return render(request,'campus.html',data)

def Corporate(request):
    
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    corporatetraining=CorporateTraining.objects.all()
    submenu = SubMenu.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'corporatetraining':corporatetraining,
        'submenu':submenu
    }
    
    return render(request,'corporate.html',data)


def Classroom(request):
    
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    classroomtraining = ClassRoomTraining.objects.all()
    submenu = SubMenu.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'classroomtraining':classroomtraining,
        'submenu':submenu
    }
    
    return render(request,'classroom.html',data)

def Industrial(request):
    
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    industrialtraining = IndustrialTraining.objects.all()
    submenu = SubMenu.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'industrialtraining':industrialtraining,
        'submenu':submenu
    }
    
    return render(request,'industrial.html',data)
def SearchPosts(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    contactinfo = contactData.objects.all()
    blogposts = blogPosts.objects.all()
    postcategories = postCategories.objects.all(    )
    if request.method == "GET":
        posttitle = request.GET.get('posttitle')
        if posttitle!= None:
           blogposts = blogPosts.objects.filter(post_tittle__icontains=posttitle)
               
    data = {
        'title' :'mohit',
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'contactpageinfo':contactinfo,
        'blogposts':blogposts,
        'postcategories':postcategories,
    }    
    return render(request,'searchposts.html',data)

def CategoryPosts(request,id):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    contactinfo = contactData.objects.all()
    postcategories = postCategories.objects.all()
    categoryposts = blogPosts.objects.filter(post_category_id=id)

    
    data = {
        'title' :'mohit',
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'contactpageinfo':contactinfo,
        'categoryposts':categoryposts,
        'postcategories':postcategories
        
    }
    return render(request,'categoryposts.html',data)
    
def PostDetails(request,slug):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    contactinfo = contactData.objects.all()
    singlepost = blogPosts.objects.get(post_slug=slug)
    blogposts = blogPosts.objects.all()
    postcategories = postCategories.objects.all()
    
    data = {
        'title' :'mohit',
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'contactpageinfo':contactinfo,
        'singlepost':singlepost,
        'blogposts':blogposts,
        'postcategories':postcategories
    }    
    return render(request,'postdetails.html',data)

def Career(request):
    return render(request,'career.html')
def RefundPolicy(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    refundpolicy = Policy.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'termpolicy':refundpolicy
        
    }
    return render(request,'policy.html',data)
def TermsConditions(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    termpolicy = termPolicy.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'termpolicy':termpolicy
        
    }
    return render(request,'terms.html',data)
def PrivacyPolicy(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    privacypolicy = privacyPolicy.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'privacypolicy':privacypolicy
        
    }
    return render(request,'privacy.html',data)
def Certificate(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    data = {
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
    }
    return render(request,'certificate.html',data)
def ApplyForCertificate(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    centerchoose = ChooseCenter.objects.all()
    data={
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
        'centerchoose':centerchoose
    }
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        course=request.POST.get('course')
        choosecenter=request.POST.get('choosecenter')
        facultyname=request.POST.get('facultyname')
        studentid=request.POST.get('studentid')
        phone=request.POST.get('phone')
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        certificatereq = CertificateRequest(name=name,email=email,course=course,center_id=choosecenter,facultyname=facultyname,studentid=studentid,phoneno=phone,startdate=startdate,enddate=enddate)
        certificatereq.save()
        messages.success(request,"Thanks for submitted your request. we will be get back to you shortly..")
        
    return render(request,'apply-for-certificate.html',data)

def DownloadCertificate(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    
    data={
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours,
    }
    return render(request,'download-certificate.html',data)

def ViewCertificate(request,studentid):
    # StudentJoined = StudentJoined.objects.all()
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    
    if request.method == 'GET':
        studentid = request.GET.get('studentid')
        if studentid!= None:
           studentinfo = StudentJoined.objects.filter(id=studentid)  
       
    data={
        'studentinfo':studentinfo,
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours
    }
    return render(request,'view-certificate.html',data)

def VerifyCertificate(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    
    
    data={
        
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours
        
    }
    return render(request,'verify-certificate.html',data)

def StudentExists(request):
    mainheader = mainHeader.objects.all()
    headermenu = headerMenu.objects.all()
    footercontact=footerContact.objects.all()
    quicklinks = quickLinks.objects.all()
    businesshours = BusinessHours.objects.all()
    
    id = request.POST.get('stuid')
    if StudentJoined.objects.filter(id=id).exists():
        messages.success(request,"This Student Certificate is Verified..")
    else:
        messages.warning(request,"Wrong Student and Certificate is not Verified..")
    
    data={
        
        'mainheader':mainheader,
        'headermenu':headermenu,
        'footercontact':footercontact,
        'quicklinks':quicklinks,
        'businesshours':businesshours
        
    }    
    return render(request,"verify-certificate.html",data) 
     
# def generate_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     d = datetime.today().strftime('%Y-%m-%d')
#     response['Content-Disposition'] = f'inline; filename="{d}.pdf"'
    
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)
    
#     #data to print
#     if request.method == 'GET':
#         studentid = request.GET.get('studentid')
#         if studentid!= None:
#            studentinfo = StudentJoined.objects.filter(id=studentid)
       
#     data={
#         'studentinfo':studentinfo
#     }
    
#     #starting writing the pdf here
#     p.setFont("Helvetica",15,leading=None)
#     p.setFillColorRGB(0.29296875,0.453125,0.609375)
#     p.drawString(260,800,"Certificate of Completion")
#     p.line(0,780,1000,780)
#     p.line(0,778,1000,778)
#     xl = 20
#     yl = 750
#     # render data
#     for k,v in data.items():
#         p.setFont("Helvetica",15,leading=None)
#         p.drawString(xl,yl-12,f"{k}")
#         yl=yl-60
#     p.setTitle(f'Report on  {d}')
#     p.showPage()
#     p.save()
    
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
    
#     return response