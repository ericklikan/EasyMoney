from django.conf.urls import url
from . import views
app_name = 'manager'

urlpatterns = [
    #/manager/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/manager/section_title/
    url(r'^(?P<budget_title>[\w]+)/$',views.DetailView.as_view(), name='detail'),

    url(r'budget/add/$',views.BudgetCreate.as_view(), name='budget-add'),
]
