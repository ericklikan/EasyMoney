from django.conf.urls import url
from . import views
app_name = 'manager'

urlpatterns = [
    #/manager/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/manager/section_title/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    url(r'budget/add/$',views.BudgetCreate.as_view(), name='budget-add'),

    url(r'budget/(?P<pk>[0-9]+)/$',views.BudgetUpdate.as_view(), name='budget-update'),

    url(r'budget/(?P<pk>[0-9]+)/delete/$',views.BudgetCreate.as_view(), name='budget-delete'),

    #Login, Logout, register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$',views.UserFormLogin.as_view(), name='login'),

    #url(r'^logout/$',)
]
