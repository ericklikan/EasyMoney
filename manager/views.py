from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Budget

class IndexView(generic.ListView):
    template_name = 'manager/index.html'
    context_object_name = 'all_budgets'

    def get_queryset(self):
        return Budget.objects.all()

class DetailView(generic.DetailView):
    model = Budget
    def get_context_data(self, budget_title):
        context = super(DetailView, self.get_context_data(budget_title))
        return context


class BudgetCreate(CreateView):
    model = Budget
    fields = ['budget_title','budget_total']
