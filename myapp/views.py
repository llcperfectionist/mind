# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import smtplib

from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.shortcuts import render
from paypal.pro.views import PayPalPro
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED

from myapp.form import SignUpForm, CategoriesForm, CategorieseditForm, TeacherForm, TeachereditForm, TeamForm, \
    TeameditForm, courseForm, CourseeditForm, onlinecourseForm, onlinecourse_editForm, promocodeForm, promocodeeditForm, \
    reviewForm, revieweditForm, faqForm, pdfForm, carporate_traningForm, free_esourcesForm, contactForm, \
    REQUIREMENTSForm, BECOME_ContactForm, BlogForm, subscribeForm ,PayForm
from myapp.models import categories, teachers, team, course, onlinecourse, promecode, reviews, faq, pdf, Blog, payment,instamojo_payment,instamojo_payment_done

from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from simple_search import search_filter
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext

from mysite import settings
import paypalrestsdk as paypal


paypal.configure({
    "mode": "live",  # sandbox or live
    "client_id": "AXCIG0QtlJvYQl046CMhRHMXyGlOf_orjAag0MqFbWcaNdEpQNQlUFJGyBhaGV-mpfo6ikBRzrb9F886",
    "client_secret": "EC7lm5XIW1nxsG5iChvR1Ys7DMR8cz6ildGE9BV1kgIDusadzC4CW8dDw9wJuMy_ALXubj4Mo-RKWUoc"})





def index(request):
    side_blog = Blog.objects.all().order_by('-id')[:4]
    popular = course.objects.filter(id=1).order_by('-id')[:9]
    return render(request, "index.html", {'popular': popular, 'side_blog': side_blog})


def about(request):
    team_list = team.objects.all().order_by('-id')
    return render(request, "about.html", {'team_list': team_list})


def courses(request):
    allcourse = course.objects.filter(id=1).order_by('-id')
    return render(request, "course.html", {'allcourse': allcourse})


def corporate_training(request):
    categorieslisting = categories.objects.all().order_by('-id')
    return render(request, "cooprate-training.html", {'categorieslisting': categorieslisting})


def select_coures_ajax(request):
    if request.method == "POST":
        id = request.POST.get("categorisename", "")
        allcourse = course.objects.filter(categorie_id=id)
    return render(request, "select_coures_ajax.html", {'allcourse': allcourse})


def Savecorporate_training(request):
    saved = False

    if request.method == "POST":
        course_id = request.POST.get("course_id", "")
        categorie = request.POST.get("categorie", "")
        course_id = course.objects.get(id=course_id)
        categorie = categories.objects.get(id=categorie)

        MyForm = carporate_traningForm(request.POST or None, request.FILES)
        if MyForm.is_valid():
            new_book = MyForm.save(commit=False)  # Don't save it yet
            new_book.course_id = course_id
            new_book.categorie = categorie  # Add person
            new_book.save()
            saved = True  # Now save it
            messages.success(request, 'Thank You I Will Contact u soon.')


    else:
        carporate_traningForm()
        messages.error(request, '.')
    return render(request, "cooprate-training.html", locals())


def free_resources(request):
    return render(request, "free-resourse.html", {})


def savefree_resources(request):
    saved = False
    if request.method == "POST":
        form = free_esourcesForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            messages.success(request, 'Thank You I Will Contact u soon.')
    else:
        CategoriesForm()
        messages.error(request, '')
    return HttpResponseRedirect('../free-resources', locals())


def contact_us(request):
    return render(request, "contact.html", {})


def profile(request):
    id = request.user.id
    user_data = User.objects.filter(id=id)

    payment_data = instamojo_payment_done.objects.filter(user_id=id)

    return render(request, "profile.html", {'payment_data':payment_data ,'user_data':user_data})


def savecontactus(request):
    saved = False

    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            messages.success(request, 'Thank you , We will contact you soon.')

    else:
        contactForm()
        messages.error(request, '')
    return HttpResponseRedirect('../contact-us', locals())


def terms_conditions(request):
    return render(request, "trems-condition.html", {})


def privacy_polic(request):
    return render(request, 'privacy.html', {})


def login_form(request):
    return render(request, 'login-form.html', {})


def customer_reviews(request):
    return render(request, "customer-reviews.html", {})


def career(request):
    return render(request, "career.html", {})


def product(request, url):
    product = course.objects.filter(url=url)
    for product_review in product:
        product_id = product_review.id
        categorie_id = product_review.categorie_id
        paypal_dict = {
            "business": "onlinemindcreature@gmail.com",
            "amount": product_review.price,
            "item_name": product_review.name,
            "invoice": "1",
            "notify_url": "http://127.0.0.1:8000/" + reverse('paypal-ipn'),
            "return_url": "http://127.0.0.1:8000/success?amount="+str(product_review.price)+"&item_name="+str(product_review.name)+"&item_id="+str(product_id),
            "cancel_return": "http://127.0.0.1:8000/success",
            "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        print form
        print "helooooooooooooooo"
        ternding = course.objects.filter(trending=1).order_by('-id')[:5]
        reviews_list = reviews.objects.filter(course_id=product_id).order_by('-id')
        related = course.objects.filter(categorie_id=categorie_id).order_by('-id')[:3]
    return render(request, "product-page.html",
                  {'product': product, 'related': related, 'reviews_list': reviews_list, 'form': form,
                   'ternding': ternding})




# instamojo code  here
from instamojo_wrapper import Instamojo


API_KEY = 'd82016f839e13cd0a79afc0ef5b288b3'
AUTH_TOKEN = '3827881f669c11e8dad8a023fd1108c2'
# API_KEY = '1786971b44c4188e7924a96a0c3420483'
# AUTH_TOKEN = '1cf8c7b96c3cd7d423cff84f75e9755c'
api = Instamojo(api_key = API_KEY, auth_token = AUTH_TOKEN ,endpoint='https://www.instamojo.com/api/1.1/')

def instamojo(request):
    if request.method == 'POST':
        print("\n\nPOST\n\n" + str(request.POST))
        # create a form instance and populate it with data from the request:
        form = PayForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            # Create a new Payment Request
            response = api.payment_request_create(
                amount=str(data['Amount']),
                purpose=data['Purpose'],
                send_email=False,
                email=data['Email'],
                buyer_name=data['Name'],
                # phone=data['Phone'],
                redirect_url=request.build_absolute_uri(reverse("list"))
            )
            obj = instamojo_payment()
            obj.name = data['Name']
            obj.email= data['Email']
            obj.amount= str(data['Amount'])
            obj.item_name = data['Purpose']
            obj.payment_request_id = response['payment_request']['id']
            obj.save()
            print(response)
            print(response['payment_request']['id'])


            # return HttpResponse(response)
            return HttpResponseRedirect(response['payment_request']['longurl'])

            # if a GET (or any other method) we'll create a blank form
    else:
        print("\n\nGET\n\n")
        form = PayForm()
        # form.fields['Amount'].clean(10)
        # form.fields['Amount']=10
        print("\n\n" + str(form) + "\n\n")

    return render(request, 'instamojo.html', {'form': form})
    # return HttpResponse("Hello, world. You're at the API TEST index.")




def list_payments(request):
    baseurl = request.get_full_path()
    payment_id=request.GET['payment_id']
    payment_request_id = request.GET['payment_request_id']
    print(payment_id,payment_request_id)
    response = api.payment_requests_list()
    # Loop over all of the payment requests
    # h = "<div><table><tr><th>ID</th><th>amount</th><th>Purpose</th><th>status</th></tr>"
    for payment_request in response['payment_requests']:

            id = request.user.id
            id = str(id).replace('L', '')
            id = User.objects.get(id=id)
            obj = instamojo_payment_done()
            obj.name = payment_request['buyer_name']
            obj.email=  payment_request['email']
            obj.amount=  payment_request['amount']
            obj.item_name = payment_request['purpose']
            obj.payment_request_id = payment_request['id']
            obj.status = payment_request['status']
            obj.payment_id = payment_id
            obj.user_id = id
            obj.save()
            # h += "<tr>"
            # h += "<td>" + payment_request['id'] + "</td>"
            # h += "<td>" + payment_request['amount'] + "</td>"
            # h += "<td>" + payment_request['purpose'] + "</td>"
            # h += "<td>" + payment_request['status'] + "</td>"
            # h += "<td>" + payment_request['buyer_name'] + "</td>"
            # h += "<td>" + payment_request['email'] + "</td>"
            # # h += "<td>" + payment_request['phone'] + "</td>"
            # h += "</tr>"
            break
    # h += "</table></div>"
    return redirect("../profile")

    # return HttpResponse(h)


# def paypal_payment(request, url):
#     product = course.objects.filter(url=url)
#     for product in product:
#
#         response = api.payment_request_create(
#             amount= product.price,
#             purpose=product.name,
#             send_email=True,
#             email="hazoorsingh.webtunix@gmail.com",
#             redirect_url="https://www.mindcreature.com/"
#         )
#         # print the long URL of the payment request.
#         print(response['payment_request']['longurl'])
#         # print the unique ID(or payment request ID)
#         print(response['payment_request']['id'])








    # for product in product:
    #     payment = paypal.Payment({
    #         "intent": "sale",
    #         "payer": {
    #             "payment_method": "paypal"},
    #         "redirect_urls": {
    #             "return_url": "http://127.0.0.1:8000/paypal_Return?success=true",
    #             "cancel_url": "http://127.0.0.1:8000//paypal_Return?cancel=true"},
    #         "transactions": [{
    #
    #             "item_list": {
    #                 "items": [{
    #                     "name": product.name,
    #                     "sku": product.id,
    #                     "price": product.price,
    #                     "currency": "INR",
    #                     "quantity": 1}]},
    #
    #             # Amount
    #             # Let's you specify a payment amount.
    #             "amount": {
    #                 "total": product.price,
    #                 "currency": "INR"},
    #             "description": product.description}]})
    #
    #     # Create Payment and return status
    #     if payment.create():
    #         print("Payment[%s] created successfully" % (payment.id))
    #         # Redirect the user to given approval url
    #         for link in payment.links:
    #             if link.method == "REDIRECT":
    #                 # Convert to str to avoid google appengine unicode issue
    #                 # https://github.com/paypal/rest-api-sdk-python/pull/58
    #                 redirect_url = str(link.href)
    #                 print("Redirect for approval: %s" % (redirect_url))
    #                 return redirect(redirect_url)
    #     else:
    #         print("Error while creating payment:")
    #         print(payment.error)
    #         return "Error while creating payment"


def paypal_Return(request):
    # ID of the payment. This ID is provided when creating payment.
    paymentId = request.args['paymentId']
    payer_id = request.args['PayerID']
    payment = paypal.Payment.find(paymentId)

    # PayerID is required to approve the payment.
    if payment.execute({"payer_id": payer_id}):  # return True or False
        print("Payment[%s] execute successfully" % (payment.id))
        return 'Payment execute successfully!' + payment.id
    else:
        print(payment.error)
        return 'Payment execute ERROR!'







@csrf_exempt
def success(request):
    if request.method == "GET":
        obj_payment = payment()
        amount= request.GET.get('amount')
        item_name = request.GET.get('item_name')
        item_id = request.GET.get('item_id')
        current_user = request.user
        item_id = course.objects.get(id=item_id)
        user_id = User.objects.get(id=current_user.id)

        obj_payment.user_id=user_id
        obj_payment.email=current_user.email
        obj_payment.item_id=item_id
        obj_payment.item_name=item_name
        obj_payment.amount=amount
        obj_payment.save()
    #context = {}
    return render_to_response("succes.html")

def nvp_handler(nvp):
    nvp = lambda nvp: nvp
    # This is passed a PayPalNVP object when payment succeeds.
    # This should do something useful!
    pass
#




@csrf_exempt
def notify(request):
    # valid_ipn_received.connect()

    context = {}
    return render_to_response("notify.html", context)


@csrf_exempt
def cancel(request):
    # valid_ipn_received.connect()

    context = {}
    return render_to_response("cancel.html", context)


@csrf_exempt
def return_view(request):
    # valid_ipn_received.connect()

    context = {}
    return render_to_response("return.html", context)


def search_select(request):
    allcourse = ''
    if request.method == "GET":
        q = request.GET.get("q", "")
        search_fields = ['name', 'description', 'brief_description']
        allcourse = course.objects.filter(search_filter(search_fields, q))
    return render(request, "course.html", {'allcourse': allcourse})


def Subscribe(request):
    abc = ''
    if request.method == "POST":
        form = subscribeForm(request.POST)
        if form.is_valid():
            form.save()
            abc = 'Thank you for  Subscribe.'
            return HttpResponse(
                '<script type="text/javascript">alert("Thanks for  Subscribing."); window.location = "../";</script>')

            # d = Context({'email': email})
            # plaintext = get_template('webtunix-admin/email.txt')
            # htmly = get_template('subscribe.html')
            # subject, from_email, to = 'Thank You For Subscribe' , 'hazoorsingh.webtunix@gmail.com', email
            # text_content = plaintext.render(d)
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
    else:
        subscribeForm()
        abc = 'Your subscription was not updated.'
    return redirect("/")


def savereviewfront(request):
    saved = False

    if request.method == "POST":
        course_id = request.POST.get("course_id", "")
        course_id = course.objects.get(id=course_id)
        MyForm = reviewForm(request.POST)
        if MyForm.is_valid():
            new_book = MyForm.save(commit=False)  # Don't save it yet
            new_book.course_id = course_id
            new_book.save()  # Now save it
            messages.success(request, ' Thanks for your valuable reviews')

    else:
        reviewForm()
        messages.error(request, 'Review was not saved.')
    return render(request, "messege.html", locals())


def blogs(request):
    # side_blog= Blog.objects.all()
    # side_categories = categories.objects.all().order_by('-id')[:3]
    blog_list = Blog.objects.all().order_by('-id')[:3]
    return render(request, 'blog.html', {'blog_list': blog_list})


def single_blog(request, url):
    side_blog = Blog.objects.all().order_by('-id')[:5]
    side_categories = categories.objects.all().order_by('-id')[:3]
    blog_list = Blog.objects.filter(url=url)
    return render(request, 'bloginner.html',
                  {'blog_list': blog_list, 'side_blog': side_blog, 'side_categories': side_categories})






from django.contrib.auth import login as auth_login, authenticate


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            d = Context({'email': email})
            plaintext = get_template('mindcreature-admin/email.txt')
            htmly = get_template('welcome.html')
            subject, from_email, to = 'Welcome To Mindcreature', 'hazoorsingh.webtunix@gmail.com', email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect('/')
    else:
        form = SignUpForm()
    return redirect('/', {'form': form})


# back panel function
@login_required(login_url="login")
def mind(request):
    if request.user.is_staff:
        return render(request, 'mindcreature-admin/index.html', {})
    return redirect('/')


@login_required(login_url="login")
def admin_list(request):
    if request.user.is_staff:
        return render(request, 'mindcreature-admin/admin-list.html', {})
    return redirect('/')


# categories function start
@login_required(login_url="login")
def add_categories(request):
    if request.user.is_staff:
        return render(request, 'mindcreature-admin/add-category.html', {})
    return redirect('/')


@login_required(login_url="login")
def list_categories(request):
    if request.user.is_staff:
        categorieslisting = categories.objects.all().order_by('-id')
        return render(request, 'mindcreature-admin/list-category.html', {'categorieslisting': categorieslisting})
    return redirect('/')


@login_required(login_url="login")
def savecategories(request):
    if request.user.is_staff:
        savedcategories = False
        if request.method == "POST":
            MycategoriesForm = CategoriesForm(request.POST)
            if MycategoriesForm.is_valid():
                MycategoriesForm.save()
                savedcategories = True
                messages.success(request, 'Your category saved successfuly.')
        else:
            CategoriesForm()
            messages.error(request, 'Your category was not saved , Please try again.')
        return HttpResponseRedirect('../add-categories', locals())

    return redirect('/')


@login_required(login_url="login")
def categoriesdelete(request, categories_id):
    if request.user.is_staff:
        emp = categories.objects.get(id=categories_id)
        emp.delete()
        return HttpResponseRedirect('../list-categories')
    return redirect('/')


@login_required(login_url="login")
def categories_edit(request, categories_id):
    if request.user.is_staff:
        categories_editing = categories.objects.filter(id=categories_id)
        return render(request, "mindcreature-admin/categories-edit.html", {'categories_editing': categories_editing})
    return redirect('/')


@login_required(login_url="login")
def saveeditcategories(request):
    if request.user.is_staff:
        savedcategories = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            instance = get_object_or_404(categories, id=id)
            form = CategorieseditForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                savedcategories = True
                messages.success(request, 'Category updated.')
        else:
            CategorieseditForm()
            messages.error(request, 'Your category was not updated.')
        return HttpResponseRedirect('../list-categories', locals())
    return redirect('/')


# categories function end


# teachers function  start
@login_required(login_url="login")
def teacher_add(request):
    if request.user.is_staff:
        return render(request, "mindcreature-admin/teacher-add.html", {})
    return redirect('/')


@login_required(login_url="login")
def Saveteacher(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            MyForm = TeacherForm(request.POST, request.FILES)
            if MyForm.is_valid():
                MyForm.save()
                saved = True
                messages.success(request, 'New teacher added.')
        else:
            TeacherForm()
            messages.error(request, 'Failed to add new teacher , Please try again.')
        return HttpResponseRedirect('../teacher-add', locals())

    return redirect('/')


@login_required(login_url="login")
def teacher_list(request):
    if request.user.is_staff:
        teacherlist = teachers.objects.all()
        return render(request, 'mindcreature-admin/teacher-list.html', {'teachers': teacherlist})
    return redirect('/')


@login_required(login_url="login")
def teacherdelete(request, teacher_id):
    if request.user.is_staff:
        emp = teachers.objects.get(id=teacher_id)
        emp.delete()
        return HttpResponseRedirect('../teacher-list')
    return redirect('/')


@login_required(login_url="login")
def teacher_edit(request, teacher_id):
    if request.user.is_staff:
        teacher_data_id = teachers.objects.filter(id=teacher_id)
        return render(request, "mindcreature-admin/teacher-edit.html", {'teacher_data_id': teacher_data_id})
    return redirect('/')


@login_required(login_url="login")
def editteacher(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            instance = get_object_or_404(teachers, id=id)
            form = TeachereditForm(request.POST or None, request.FILES or None, instance=instance)

            if form.is_valid():
                form.save()
                saved = True
                messages.success(request, 'Teacher info updated.')


        else:
            TeachereditForm()
            messages.error(request, 'Unable to update teacher info.')
        return HttpResponseRedirect('../teacher-list', locals())
    return redirect('/')


# teachers function  end


# team add function start
@login_required(login_url="login")
def team_add(request):
    if request.user.is_staff:
        return render(request, "mindcreature-admin/team-add.html", {})
    return redirect('/')


@login_required(login_url="login")
def Saveteam(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            MyForm = TeamForm(request.POST, request.FILES)
            if MyForm.is_valid():
                MyForm.save()
                saved = True
                messages.success(request, 'Team updated.')
        else:
            TeamForm()
            messages.error(request, 'Unable to update team.')
        return HttpResponseRedirect('../team-add', locals())

    return redirect('/')


@login_required(login_url="login")
def team_list(request):
    if request.user.is_staff:
        teamlist = team.objects.all()
        return render(request, 'mindcreature-admin/team-list.html', {'teamlist': teamlist})
    return redirect('/')


@login_required(login_url="login")
def teamdelete(request, team_id):
    if request.user.is_staff:
        emp = team.objects.get(id=team_id)
        emp.delete()
        return HttpResponseRedirect('../team-list')
    return redirect('/')


@login_required(login_url="login")
def team_edit(request, team_id):
    if request.user.is_staff:
        team_data_id = team.objects.filter(id=team_id)
        return render(request, "mindcreature-admin/team-edit.html", {'team_data_id': team_data_id})
    return redirect('/')


@login_required(login_url="login")
def editteam(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            instance = get_object_or_404(team, id=id)
            form = TeameditForm(request.POST or None, request.FILES or None, instance=instance)

            if form.is_valid():
                form.save()
                saved = True
                messages.success(request, 'Team Was Update.')


        else:
            TeameditForm()
            messages.error(request, 'Team Was Not  Update.')
        return HttpResponseRedirect('../team-list', locals())
    return redirect('/')


# team function and

# course function start
@login_required(login_url="login")
def course_add(request):
    if request.user.is_staff:
        teacherlist = teachers.objects.all()
        categorieslisting = categories.objects.all()
        return render(request, "mindcreature-admin/course-add.html",
                      {'teacherlist': teacherlist, 'categorieslisting': categorieslisting})
    return redirect('/')


@login_required(login_url="login")
def Savecorse(request):
    if request.user.is_staff:
        saved = False

        if request.method == "POST":
            teacher = request.POST.get("teacher", "")
            categorie = request.POST.get("categorie", "")

            teacher = teachers.objects.get(id=teacher)
            categorie = categories.objects.get(id=categorie)

            MyForm = courseForm(request.POST or None, request.FILES)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.teacher = teacher
                new_book.categorie = categorie  # Add person
                new_book.save()  # Now save it
                messages.success(request, 'New course added successfuly.')

        else:
            courseForm()
            messages.error(request, 'Course Was Not  Saved.')
        return HttpResponseRedirect('../course-add', locals())
    return redirect('/')


@login_required(login_url="login")
def course_list(request):
    if request.user.is_staff:
        courselist = course.objects.all()
        return render(request, 'mindcreature-admin/course-list.html', {'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def coursedelete(request, course_id):
    if request.user.is_staff:
        emp = course.objects.get(id=course_id)
        emp.delete()
        return HttpResponseRedirect('../course-list')
    return redirect('/')


@login_required(login_url="login")
def course_edit(request, course_id):
    if request.user.is_staff:
        teacherlist = teachers.objects.all()
        categorieslisting = categories.objects.all()
        course_data_id = course.objects.filter(id=course_id)
        return render(request, "mindcreature-admin/course-edit.html",
                      {'course_data_id': course_data_id, 'teacherlist': teacherlist,
                       'categorieslisting': categorieslisting})
    return redirect('/')


@login_required(login_url="login")
def editcourse(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            teacher = request.POST.get("teacher", "")
            categorie = request.POST.get("categorie", "")

            teacher = teachers.objects.get(id=teacher)
            categorie = categories.objects.get(id=categorie)

            instance = get_object_or_404(course, id=id)
            form = CourseeditForm(request.POST or None, request.FILES or None, instance=instance)

            if form.is_valid():
                new_book = form.save(commit=False)  # Don't save it yet
                new_book.teacher = teacher
                new_book.categorie = categorie  # Add person
                new_book.save()  # Now save it
                messages.success(request, 'Course Was Updated.')


        else:
            CourseeditForm()
            messages.error(request, 'Course Was Not Updated.')
        return HttpResponseRedirect('../course-list', locals())
    return redirect('/')


# course function end

# online course function start
@login_required(login_url="login")
def online_course_add(request, course_id):
    if request.user.is_staff:
        course_data_id = course.objects.filter(id=course_id)
        return render(request, "mindcreature-admin/online-course-add.html", {'course_data_id': course_data_id})
    return redirect('/')


@login_required(login_url="login")
def Saveonlinecorse(request):
    if request.user.is_staff:
        saved = False

        if request.method == "POST":
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            MyForm = onlinecourseForm(request.POST)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()  # Now save it
                messages.success(request, 'Online Course Was Saved.')

        else:
            onlinecourseForm()
            messages.error(request, 'Online Course Was Not  Saved.')
        return HttpResponseRedirect('../online-course-list', locals())
    return redirect('/')


@login_required(login_url="login")
def online_course_list(request):
    if request.user.is_staff:
        onlinecourselist = onlinecourse.objects.all()
        return render(request, 'mindcreature-admin/online-course-list.html', {'onlinecourselist': onlinecourselist})
    return redirect('/')


@login_required(login_url="login")
def onlinecoursedelete(request, course_id):
    if request.user.is_staff:
        emp = onlinecourse.objects.get(id=course_id)
        emp.delete()
        return HttpResponseRedirect('../online-course-list')
    return redirect('/')


@login_required(login_url="login")
def online_course_edit(request, course_id):
    if request.user.is_staff:
        course_data_id = onlinecourse.objects.filter(id=course_id)
        return render(request, "mindcreature-admin/online-course-edit.html", {'course_data_id': course_data_id})
    return redirect('/')


@login_required(login_url="login")
def editonlinecourse(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            instance = get_object_or_404(onlinecourse, id=id)
            form = onlinecourse_editForm(request.POST or None, instance=instance)

            if form.is_valid():
                new_book = form.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()  # Now save it
                messages.success(request, 'Course Updated.')


        else:
            onlinecourse_editForm()
            messages.error(request, 'Course Was Not  Update.')
        return HttpResponseRedirect('../online-course-list', locals())
    return redirect('/')


# online course function end


# promo code function start
@login_required(login_url="login")
def promo_code_add(request):
    if request.user.is_staff:
        courselist = course.objects.all()
        return render(request, 'mindcreature-admin/promo-code-add.html', {'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def Savepromocode(request):
    if request.user.is_staff:
        saved = False

        if request.method == "POST":
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            MyForm = promocodeForm(request.POST)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()  # Now save it
                messages.success(request, 'Prome Code  Was Saved.')
        else:
            promocodeForm()
            messages.error(request, 'Prome Code Was Not  Saved.')
        return HttpResponseRedirect('../promo-code-add', locals())
    return redirect('/')


@login_required(login_url="login")
def promo_code_list(request):
    if request.user.is_staff:
        promolist = promecode.objects.all()
        return render(request, 'mindcreature-admin/promo-code-list.html', {'promolist': promolist})
    return redirect('/')


@login_required(login_url="login")
def promodelete(request, promo_id):
    if request.user.is_staff:
        emp = promecode.objects.get(id=promo_id)
        emp.delete()
        return HttpResponseRedirect('../promo-code-list')
    return redirect('/')


@login_required(login_url="login")
def promo_code_edit(request, promo_id):
    if request.user.is_staff:
        courselist = course.objects.all()
        promocode_list = promecode.objects.filter(id=promo_id)
        return render(request, "mindcreature-admin/promo-code-edit.html",
                      {'promocode_list': promocode_list, 'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def editpromocode(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            instance = get_object_or_404(promecode, id=id)
            form = promocodeeditForm(request.POST or None, instance=instance)

            if form.is_valid():
                new_book = form.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()  # Now save it
                messages.success(request, 'Promo Code Was Update.')


        else:
            promocodeeditForm()
            messages.error(request, 'Promo Code Was Not  Update.')
        return HttpResponseRedirect('../promo-code-list', locals())
    return redirect('/')


# prome code function end


# review  function start
@login_required(login_url="login")
def review_add(request):
    if request.user.is_staff:
        courselist = course.objects.all()
        return render(request, 'mindcreature-admin/review-add.html', {'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def savereview(request):
    if request.user.is_staff:
        saved = False

        if request.method == "POST":
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            MyForm = reviewForm(request.POST)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()  # Now save it
                messages.success(request, 'Review   Was Saved.')

        else:
            reviewForm()
            messages.error(request, 'Review Was Not  Saved.')
        return HttpResponseRedirect('../review-add', locals())
    return redirect('/')


@login_required(login_url="login")
def reviews_list(request):
    if request.user.is_staff:
        review_list = reviews.objects.all()
        return render(request, 'mindcreature-admin/review-list.html', {'review_list': review_list})
    return redirect('/')


@login_required(login_url="login")
def reviewdelete(request, review_id):
    if request.user.is_staff:
        emp = reviews.objects.get(id=review_id)
        emp.delete()
        return HttpResponseRedirect('../review-list')
    return redirect('/')


@login_required(login_url="login")
def review_edit(request, review_id):
    if request.user.is_staff:
        courselist = course.objects.all()
        review_list = reviews.objects.filter(id=review_id)
        return render(request, "mindcreature-admin/review-edit.html",
                      {'review_list': review_list, 'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def editreview(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            instance = get_object_or_404(reviews, id=id)
            form = revieweditForm(request.POST or None, instance=instance)

            if form.is_valid():
                new_book = form.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()
                saved = True
                messages.success(request, 'Promo Code Was Update.')


        else:
            revieweditForm()
            messages.error(request, 'Promo Code Was Not  Update.')
        return HttpResponseRedirect('../review-list', locals())
    return redirect('/')


# review function end

# faq function start
@login_required(login_url="login")
def faq_add(request):
    if request.user.is_staff:
        return render(request, 'mindcreature-admin/faq-add.html', {})
    return redirect('/')


@login_required(login_url="login")
def Savefaq(request):
    if request.user.is_staff:
        saved = False

        if request.method == "POST":

            MyForm = faqForm(request.POST, request.FILES)
            if MyForm.is_valid():
                MyForm.save()
                saved = True
                messages.success(request, 'Qustion Was Saved.')

        else:
            faqForm()
            messages.error(request, 'Qustion Was Not  Saved.')
        return HttpResponseRedirect('../faq-add', locals())
    return redirect('/')


@login_required(login_url="login")
def faq_list(request):
    if request.user.is_staff:
        list_faq = faq.objects.all()
        return render(request, 'mindcreature-admin/faq-list.html', {'list_faq': list_faq})
    return redirect('/')


@login_required(login_url="login")
def faqdelete(request, faq_id):
    if request.user.is_staff:
        emp = faq.objects.get(id=faq_id)
        emp.delete()
        return HttpResponseRedirect('../faq-list')
    return redirect('/')


@login_required(login_url="login")
def faq_edit(request, faq_id):
    if request.user.is_staff:
        faq_list = faq.objects.filter(id=faq_id)
        return render(request, "mindcreature-admin/faq-edit.html", {'faq_list': faq_list})
    return redirect('/')


@login_required(login_url="login")
def editfaq(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            instance = get_object_or_404(faq, id=id)
            form = faqForm(request.POST or None, instance=instance)

            if form.is_valid():
                form.save()
                saved = True
                messages.success(request, 'Qustion Was Update.')


        else:
            faqForm()
            messages.error(request, 'Qustion Was Not  Update.')
        return HttpResponseRedirect('../faq-list', locals())
    return redirect('/')


# faq function end


# pdf fuction start
@login_required(login_url="login")
def pdf_add(request):
    if request.user.is_staff:
        courselist = course.objects.all()
        return render(request, 'mindcreature-admin/pdf-add.html', {'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def savepdf(request):
    if request.user.is_staff:
        saved = False

        if request.method == "POST":
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            MyForm = pdfForm(request.POST or None, request.FILES)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()  # Now save it
                saved = True
                messages.success(request, 'Pdf   Was Saved.')

        else:
            pdfForm()
            messages.error(request, 'Pdf Was Not  Saved.')
        return HttpResponseRedirect('../pdf-add', locals())
    return redirect('/')


@login_required(login_url="login")
def pdf_list(request):
    if request.user.is_staff:
        pdf_list = pdf.objects.all()
        return render(request, 'mindcreature-admin/pdf-list.html', {'pdf_list': pdf_list})
    return redirect('/')


@login_required(login_url="login")
def pdfdelete(request, pdf_id):
    if request.user.is_staff:
        emp = pdf.objects.get(id=pdf_id)
        emp.delete()
        return HttpResponseRedirect('../pdf-list')
    return redirect('/')


@login_required(login_url="login")
def pdf_edit(request, pdf_id):
    if request.user.is_staff:
        pdf_list = pdf.objects.filter(id=pdf_id)
        courselist = course.objects.all()
        return render(request, "mindcreature-admin/pdf-edit.html", {'pdf_list': pdf_list, 'courselist': courselist})
    return redirect('/')


@login_required(login_url="login")
def Saveeditpdf(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            course_id = request.POST.get("course_id", "")
            course_id = course.objects.get(id=course_id)
            instance = get_object_or_404(pdf, id=id)
            form = pdfForm(request.POST or None, request.FILES or None, instance=instance)

            if form.is_valid():
                new_book = form.save(commit=False)  # Don't save it yet
                new_book.course_id = course_id
                new_book.save()
                saved = True
                messages.success(request, 'PDF  Was Update.')


        else:
            pdfForm()
            messages.error(request, 'PDF Was Not  Update.')
        return HttpResponseRedirect('../pdf-list', locals())
    return redirect('/')
    # pdf function end


# blog function start

def blog_add(request):
    if request.user.is_staff:
        categorieslisting = categories.objects.all()
        return render(request, 'mindcreature-admin/blog-add.html', {'categorieslisting': categorieslisting})
    return redirect('/')


@login_required(login_url="login")
def saveblog(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            categories_id = request.POST.get("categories_id", "")
            categories_id = categories.objects.get(id=categories_id)
            MyForm = BlogForm(request.POST or None, request.FILES)
            if MyForm.is_valid():
                new_book = MyForm.save(commit=False)  # Don't save it yet
                new_book.categories_id = categories_id
                new_book.save()  # Now save it
                saved = True
                messages.success(request, 'Blog  Was Saved.')
        else:
            BlogForm()
            messages.error(request, 'Blog Was Not  Saved.')
        return HttpResponseRedirect('../blog-add', locals())
    return redirect('/')


@login_required(login_url="login")
def blog_list(request):
    if request.user.is_staff:
        blog_list = Blog.objects.all()
        return render(request, 'mindcreature-admin/blog-list.html', {'blog_list': blog_list})
    return redirect('/')


@login_required(login_url="login")
def blogdelete(request, blog_id):
    if request.user.is_staff:
        emp = Blog.objects.get(id=blog_id)
        emp.delete()
        return HttpResponseRedirect('../blog-list')
    return redirect('/')


@login_required(login_url="login")
def blog_edit(request, blog_id):
    if request.user.is_staff:
        blog_list = Blog.objects.filter(id=blog_id)
        categorieslisting = categories.objects.all()
        return render(request, "mindcreature-admin/blog-edit.html",
                      {'blog_list': blog_list, 'categorieslisting': categorieslisting})
    return redirect('/')


@login_required(login_url="login")
def Saveeditblog(request):
    if request.user.is_staff:
        saved = False
        if request.method == "POST":
            id = request.POST.get("id", "")
            categories_id = request.POST.get("categories_id", "")
            categories_id = categories.objects.get(id=categories_id)
            instance = get_object_or_404(Blog, id=id)
            form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
            if form.is_valid():
                new_book = form.save(commit=False)  # Don't save it yet
                new_book.course_id = categories_id
                new_book.save()
                saved = True
                messages.success(request, 'Blog  Was Update.')
        else:
            BlogForm()
            messages.error(request, 'Blog Was Not  Update.')
        return HttpResponseRedirect('../blog-list', locals())
    return redirect('/')





#
# def reviews_front(request):
#     review_list = reviews.objects.all().order_by('-id')
#     return render(request, "reviews.html", {'review_list':review_list})
#

#

#
#
#
#
#
#
# def become_affiliate(request):
#    return render(request, "become-affiliate.html", {})
#

#
# def careers(request):
#    return render(request, "careers.html", {})
#
#
#
# def become_an_instructor(request):
#    return render(request, 'become-an-instructor.html', {})
#
# def post_as_guest(request):
#    return render(request, 'post-as-guest.html', {})
#
#
#

#
#
#
# def saveREQUIREMENTS(request):
#    saved = False
#
#    if request.method == "POST":
#       form =REQUIREMENTSForm(request.POST)
#       if  form.is_valid():
#           form.save()
#           saved = True
#           messages.success(request, 'Thanx I Will Contact u soon.')
#
#    else:
#       REQUIREMENTSForm()
#       messages.error(request, '')
#    return render(request, "messege.html", locals())
#
#
#
# def saveBECOME_Contact(request):
#    saved = False
#
#    if request.method == "POST":
#       form =BECOME_ContactForm(request.POST)
#       if  form.is_valid():
#           form.save()
#           saved = True
#           messages.success(request, 'Thanx I Will Contact u soon.')
#
#    else:
#       BECOME_ContactForm()
#       messages.error(request, '')
#    return render(request, "messege.html", locals())
#
#
#
#

#