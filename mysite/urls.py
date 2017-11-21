"""mind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf.urls.static import static
import myapp
from mysite import settings
from myapp import views





urlpatterns = [
    
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'reset.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
          auth_views.password_reset_confirm, {'template_name': 'confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # url(r'^payment-url/$', views.buy_my_item),
    # url(r'^paypal_payment/(?P<url>[0-9A-Za-z_\-]+)', views.paypal_payment, name="paypal_payment"),
    # url(r'^paypal_Return/', views.paypal_Return, name="paypal_Return"),
    # url(r'^success/', views.success, name="success"),
    # url(r'^cancel/', views.cancel, name="cancel"),
    # url(r'^notify/', views.notify, name="notify"),



    url(r'^admin/', admin.site.urls),
    url(r'^$', myapp.views.index, ),
    url(r'^about-us', myapp.views.about, ),
    url(r'^courses', myapp.views.courses, ),
    url(r'^corporate-training', myapp.views.corporate_training, ),
    url(r'^customer-reviews', myapp.views.customer_reviews, ),
    url(r'^career', myapp.views.career, ),
    url(r'^select_coures_ajax/', myapp.views.select_coures_ajax, ),
    url(r'^Savecorporate-training', myapp.views.Savecorporate_training, name="Savecorporate-training"),

    url(r'^free-resources', myapp.views.free_resources, ),
    url(r'^savefree_resources/', myapp.views.savefree_resources, name="savefree_resources"),

    url(r'^contact-us', myapp.views.contact_us, ),
    url(r'^savecontactus', myapp.views.savecontactus, name="savecontactus" ),

    
    url(r'^terms-conditions', myapp.views.terms_conditions, ),
    url(r'^privacy-policy', myapp.views.privacy_polic, ),
    url(r'^course/(?P<url>[0-9a-zA-Z_-]+)', myapp.views.product, ),
    url(r'^search', myapp.views.search_select, name="search"),
    url(r'^login-form', myapp.views.login_form),
    url(r'^subscribe', myapp.views.Subscribe, name="subscribe"),
    url(r'^savereviewfront/', myapp.views.savereviewfront, name="savereviewfront" ),
    url(r'^blogs/', myapp.views.blogs, name="blogs"),
    url(r'^blog/(?P<url>[0-9a-zA-Z_-]+)', myapp.views.single_blog, name="blog"),


    url(r'^profile', myapp.views.profile, name="profile"),
    # url(r'^user-signup', myapp.views.user_signup, name="user-signup"),


    #insta mojo url
    url(r'^instamojo', myapp.views.instamojo, name="instamojo"),

    url(r'^list', myapp.views.list_payments, name="list"),


   # url(r'^reviews/', myapp.views.reviews_front, ),
    # url(r'^become-affiliate/', myapp.views.become_affiliate, ),
    # url(r'^careers/', myapp.views.careers, ),
    # url(r'^become-an-instructor/', myapp.views.become_an_instructor, ),
    # url(r'^post-as-guest/', myapp.views.post_as_guest, ),
    # url(r'^saveREQUIREMENTS/', myapp.views.saveREQUIREMENTS, name="saveREQUIREMENTS" ),
    # url(r'^saveBECOME_Contact/', myapp.views.saveBECOME_Contact, name="saveBECOME_Contact" ),
    #




    # back panel url
    url(r'^mind', myapp.views.mind, ),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'mindcreature-admin/admin-login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'index.html'}, name='logout'),
    url(r'^admin-list/', myapp.views.admin_list, ),

    #categories url start
    url(r'^add-categories', myapp.views.add_categories, ),
    url(r'^list-categories', myapp.views.list_categories, ),
    url(r'^savecategories', myapp.views.savecategories, name="savecategories" ),
    url(r'^categoriesdelete/(?P<categories_id>[0-9]+)', myapp.views.categoriesdelete, name='categoriesdelete'),
    url(r'^categories-edit/(?P<categories_id>[0-9]+)', myapp.views.categories_edit, name='categories-edit'),
    url(r'^saveeditcategories', myapp.views.saveeditcategories,name='saveeditcategories'),
    #categories url end

    #teacher url start
    url(r'^teacher-add', myapp.views.teacher_add, ),
    url(r'^teacher-list', myapp.views.teacher_list, ),
    url(r'^Saveteacher', myapp.views.Saveteacher, name="Saveteacher" ),
    url(r'^teacherdelete/(?P<teacher_id>[0-9]+)', myapp.views.teacherdelete, name='teacherdelete'),
    url(r'^teacher-edit/(?P<teacher_id>[0-9]+)', myapp.views.teacher_edit, name='teacher-edit'),
    url(r'^saveeditteacher', myapp.views.editteacher, name='saveeditteacher'),
    #teacher url end

    #taem url start
    url(r'^team-add', myapp.views.team_add, ),
    url(r'^team-list', myapp.views.team_list, ),
    url(r'^Saveteam', myapp.views.Saveteam, name="Saveteam"),
    url(r'^teamdelete/(?P<team_id>[0-9]+)', myapp.views.teamdelete, name='teamdelete'),
    url(r'^team-edit/(?P<team_id>[0-9]+)', myapp.views.team_edit, name='team-edit'),
    url(r'^editteam', myapp.views.editteam, name='editteam'),
    #team url end

    #course url start
    url(r'^course-add', myapp.views.course_add, ),
    url(r'^course-list', myapp.views.course_list, ),
    url(r'^Savecorse', myapp.views.Savecorse, name="Savecorse"),
    url(r'^coursedelete/(?P<course_id>[0-9]+)', myapp.views.coursedelete, name='coursedelete'),
    url(r'^course-edit/(?P<course_id>[0-9]+)', myapp.views.course_edit, name='course-edit'),
    url(r'^editcourse', myapp.views.editcourse, name='editcourse'),
    #course url end

    #online course url start
    url(r'^online-course-add/(?P<course_id>[0-9]+)', myapp.views.online_course_add, name='online-course-add'),
    url(r'^Saveonlinecorse', myapp.views.Saveonlinecorse, name="Saveonlinecorse"),
    url(r'^online-course-list', myapp.views.online_course_list, name="online-course-list"),
    url(r'^onlinecoursedelete/(?P<course_id>[0-9]+)', myapp.views.onlinecoursedelete, name='onlinecoursedelete'),
    url(r'^online-course-edit/(?P<course_id>[0-9]+)', myapp.views.online_course_edit, name='online-course-edit'),
    url(r'^editonlinecourse', myapp.views.editonlinecourse, name='editonlinecourse'),
    #course url end

    #prome code url start
    url(r'^promo-code-add', myapp.views.promo_code_add, name='promo-code-add'),
    url(r'^promo-code-list', myapp.views.promo_code_list, name='promo-code-list'),
    url(r'^Savepromocode', myapp.views.Savepromocode, name='Savepromocode'),
    url(r'^promodelete/(?P<promo_id>[0-9]+)', myapp.views.promodelete, name='promodelete'),
    url(r'^promo-code-edit/(?P<promo_id>[0-9]+)', myapp.views.promo_code_edit, name='promo-code-edit'),
    url(r'^editpromocode', myapp.views.editpromocode, name='editpromocode'),
    #prome code url start

    #review url start
    url(r'^review-add', myapp.views.review_add, name='review-add'),
    url(r'^review-list', myapp.views.reviews_list, name='review-list'),
    url(r'^savereview', myapp.views.savereview, name='savereview'),
    url(r'^reviewdelete/(?P<review_id>[0-9]+)', myapp.views.reviewdelete, name='reviewdelete'),
    url(r'^review-edit/(?P<review_id>[0-9]+)', myapp.views.review_edit, name='review-edit'),
    url(r'^editreview', myapp.views.editreview, name='editreview'),
    #review url end

    #faq url start
    url(r'^faq-add', myapp.views.faq_add, name='faq-add'),
    url(r'^faq-list', myapp.views.faq_list, name='faq-list'),
    url(r'^Savefaq/', myapp.views.Savefaq, name='Savefaq'),
    url(r'^faqdelete/(?P<faq_id>[0-9]+)', myapp.views.faqdelete, name='faqdelete'),
    url(r'^faq-edit/(?P<faq_id>[0-9]+)', myapp.views.faq_edit, name='faq-edit'),
    url(r'^editfaq', myapp.views.editfaq, name='editfaq'),
    #faq url end

    #pdf url start
    url(r'^pdf-add', myapp.views.pdf_add, name='pdf-add'),
    url(r'^pdf-list', myapp.views.pdf_list, name='pdf-list'),
    url(r'^savepdf', myapp.views.savepdf, name='savepdf'),
    url(r'^pdfdelete/(?P<pdf_id>[0-9]+)', myapp.views.pdfdelete, name='pdfdelete'),
    url(r'^pdf-edit/(?P<pdf_id>[0-9]+)', myapp.views.pdf_edit, name='pdf-edit'),
    url(r'^Saveeditpdf', myapp.views.Saveeditpdf, name='Saveeditpdf'),

    #blog url start
    url(r'^blog-add', myapp.views.blog_add, name='blog-add'),
    url(r'^saveblog', myapp.views.saveblog, name='saveblog'),
    url(r'^blog-list', myapp.views.blog_list, name='blog-list'),
    url(r'^blogdelete/(?P<blog_id>[0-9]+)', myapp.views.blogdelete, name='blogdelete'),
    url(r'^blog-edit/(?P<blog_id>[0-9]+)', myapp.views.blog_edit, name='blog-edit'),
    url(r'^Saveeditblog', myapp.views.Saveeditblog, name='Saveeditblog'),





] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)


