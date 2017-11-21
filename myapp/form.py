from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import categories, teachers, team, course, onlinecourse, promecode, reviews, faq, pdf, \
    carporate_traning, free_esources, contactus, REQUIREMENTS, BECOME_Contact, Blog, subscribe



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CategoriesForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    class Meta:
        model = categories
        fields = ['name',  ]

class CategorieseditForm(forms.ModelForm):
      class Meta:
         model = categories
         fields = ['name', ]

class TeacherForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    image = forms.ImageField()
    about = forms.CharField(max_length=10000)
    class Meta:
        model = teachers
        fields = ['name', 'image', 'about', ]

class TeachereditForm(forms.ModelForm):
    class Meta:
        model = teachers
        fields = ['name', 'image', 'about', ]

class TeamForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    designation = forms.CharField(max_length=100)
    image = forms.ImageField()
    facebook = forms.CharField(max_length=1000)
    twitter = forms.CharField(max_length=1000)
    youtube = forms.CharField(max_length=1000)
    class Meta:
        model = team
        fields = ['name', 'designation', 'image', 'facebook', 'twitter', 'youtube',]

class TeameditForm(forms.ModelForm):
     class Meta:
        model = team
        fields = ['name', 'designation', 'image', 'facebook', 'twitter', 'youtube',]

class courseForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    url = forms.CharField(max_length=200, required=True )
    description = forms.CharField(required=False)
    price = forms.IntegerField(required=True)
    image = forms.ImageField(required=False)
    video_link = forms.CharField(max_length=500)
    brief_description = forms.CharField(required=False)
    certification = forms.CharField(max_length=2000,required=False)
    curricalum = forms.CharField(required=False)
    course_assign_time = forms.CharField(max_length=100,required=False)
    course_assign_description = forms.CharField(required=False)
    project_time = forms.CharField(max_length=100,required=False)
    project_description = forms.CharField(required=False)
    life_time_access = forms.CharField(required=False)
    support = forms.CharField(required=False)
    get_certified = forms.CharField(required=False)
    trending = forms.CharField(max_length=10,required=False)
    popular = forms.CharField(max_length=10,required=False)
    class Meta:
        model = course
        fields = ['name', 'url', 'description', 'price', 'image', 'video_link', 'brief_description', 'certification', 'curricalum', 'course_assign_time', 'course_assign_description', 'project_time', 'project_description', 'life_time_access', 'support', 'get_certified','trending','popular',]
        exclude = ('teacher', 'categorie')

class CourseeditForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    url = forms.CharField(max_length=200, required=True)
    description = forms.CharField(required=False)
    price = forms.IntegerField(required=True)
    image = forms.ImageField(required=False)
    video_link = forms.CharField(max_length=500)
    brief_description = forms.CharField(required=False)
    certification = forms.CharField(max_length=2000, required=False)
    curricalum = forms.CharField(required=False)
    course_assign_time = forms.CharField(max_length=100, required=False)
    course_assign_description = forms.CharField(required=False)
    project_time = forms.CharField(max_length=100, required=False)
    project_description = forms.CharField(required=False)
    life_time_access = forms.CharField(required=False)
    support = forms.CharField(required=False)
    get_certified = forms.CharField(required=False)
    trending = forms.CharField(max_length=10, required=False)
    popular = forms.CharField(max_length=10, required=False)
    class Meta:
        model = course
        fields = ['name', 'url', 'description', 'price', 'image', 'video_link', 'brief_description', 'certification', 'curricalum', 'course_assign_time', 'course_assign_description', 'project_time', 'project_description', 'life_time_access', 'support', 'get_certified', 'trending', 'popular', ]
        exclude = ('teacher', 'categorie')

class onlinecourseForm(forms.ModelForm):
    date1 = forms.CharField(max_length=100,required=False)
    month1 = forms.CharField(max_length=100,required=False)
    day1 = forms.CharField(max_length=100,required=False)
    price1 = forms.CharField(max_length=100,required=False)
    date2 = forms.CharField(max_length=100,required=False)
    month2 = forms.CharField(max_length=100,required=False)
    day2 = forms.CharField(max_length=100,required=False)
    price2 = forms.CharField(max_length=100,required=False)
    date3 = forms.CharField(max_length=100,required=False)
    month3 = forms.CharField(max_length=100,required=False)
    day3 = forms.CharField(max_length=100,required=False)
    price3 = forms.CharField(max_length=100,required=False)
    class Meta:
        model = onlinecourse
        fields = ['date1', 'month1', 'day1', 'price1', 'date2', 'month2', 'day2', 'price2', 'date3', 'month3', 'day3', 'price3', ]

class onlinecourse_editForm(forms.ModelForm):
    class Meta:
        model = onlinecourse
        fields = ['date1', 'month1', 'day1', 'price1', 'date2', 'month2', 'day2', 'price2', 'date3', 'month3', 'day3', 'price3', ]

class promocodeForm(forms.ModelForm):
    promo = forms.CharField(max_length=100)
    discount = forms.IntegerField()

    class Meta:
        model = promecode
        fields = ['promo', 'discount', ]

class promocodeeditForm(forms.ModelForm):
    promo = forms.CharField(max_length=100)
    discount = forms.IntegerField()
    class Meta:
        model = promecode
        fields = ['promo', 'discount', ]

class reviewForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    discription = forms.CharField(required=False)
    class Meta:
        model = reviews
        fields = ['name', 'email','discription', ]

class revieweditForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ['name', 'email','discription', ]

class faqForm(forms.ModelForm):
    qustion = forms.CharField(max_length=100)
    answer = forms.CharField(required=False)
    class Meta:
        model = faq
        fields = ['qustion', 'answer', ]

class pdfForm(forms.ModelForm):
    course_pdf = forms.FileField(required=False)
    image = forms.ImageField(required=False)
    video_link = forms.CharField(required=False)
    class Meta:
        model = pdf
        fields = ['course_pdf', 'image' , 'video_link', ]

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=500,required=False)
    url = forms.CharField(max_length=500,required=False)
    image = forms.ImageField()
    discription = forms.CharField(required=False)
    keywords = forms.CharField(max_length=500, required=False)
    date = forms.CharField(max_length=2000, required=False)
    class Meta:
        model = Blog
        fields = ['title', 'url' , 'image', 'discription', 'keywords' , 'date']

class carporate_traningForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False)
    email = forms.CharField(max_length=200,required=False)
    company = forms.CharField(max_length=500,required=False)
    primary_role = forms.CharField(max_length=500,required=False)
    phone = forms.CharField(max_length=12,required=False)
    mode = forms.CharField(max_length=12, required=False)
    message = forms.CharField(max_length=500,required=False)
    class Meta:
        model = carporate_traning
        fields = ['name', 'email', 'company', 'primary_role', 'phone' , 'mode' , 'message', ]

class free_esourcesForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False)
    email = forms.CharField(max_length=200,required=False)
    phone = forms.CharField(max_length=12,required=False)
    message = forms.CharField(max_length=500,required=False)
    class Meta:
        model = free_esources
        fields = ['name', 'email', 'phone' , 'message', ]

class contactForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False)
    email = forms.CharField(max_length=200,required=False)
    mobile = forms.CharField(max_length=12,required=False)
    subject = forms.CharField(max_length=200, required=False)
    message = forms.CharField(max_length=500,required=False)
    class Meta:
        model = contactus
        fields = ['name', 'email', 'mobile' , 'subject', 'message', ]

class REQUIREMENTSForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False)
    email = forms.CharField(max_length=200,required=False)
    mobile = forms.CharField(max_length=12,required=False)
    skype = forms.CharField(max_length=200, required=False)
    hours = forms.CharField(max_length=200, required=False)
    message = forms.CharField(max_length=500,required=False)
    class Meta:
        model = REQUIREMENTS
        fields = ['name', 'email', 'mobile' , 'skype', 'hours', 'message', ]

class BECOME_ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False)
    email = forms.CharField(max_length=200,required=False)
    mobile = forms.CharField(max_length=12,required=False)
    website = forms.CharField(max_length=200, required=False)
    message = forms.CharField(max_length=500,required=False)
    class Meta:
        model = BECOME_Contact
        fields = ['name', 'email', 'mobile' , 'website', 'message',]


class subscribeForm(forms.ModelForm):
     email = forms.EmailField(max_length=100,required=False)
     suscribes = forms.CharField(max_length=2,required=False)
     class Meta:
        model = subscribe
        fields = ['email', 'suscribes' ]

class PayForm(forms.Form):
    Name = forms.CharField(label='Your name', max_length=100)
    Email = forms.EmailField(label='Email Address')
    # Phone = forms.IntegerField(label='Phone Number', min_value=7000000000, max_value=9999999999)
    Amount = forms.IntegerField(label='Amount')
    Purpose = forms.CharField(label="Purpose", max_length=100)
