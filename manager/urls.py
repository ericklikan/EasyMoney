from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<budget_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^budget/add/$',views.budget_create, name='budget_create'),
    url(r'^budget/(?P<pk>[0-9]+)/delete/$',views.budget_delete, name='budget-delete'),
    url(r'^(?P<budget_id>[0-9]+)/section/add/$',views.section_create, name='section_create'),
    url(r'^transaction/(?P<pk>[0-9]+)/delete/$',views.trans_delete, name='trans-delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, {'template_name':'manager/login.html'} , name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/login/'}, name='logout'),
    #url(r'^logout/$',)
]

'''
url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
'''
