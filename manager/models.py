from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, default=1)
    budget_title = models.CharField(max_length=50)
    budget_total = models.DecimalField(max_digits=17,decimal_places=2) #Must be >0, up to 1 quadrillion dollars

    def get_absolute_url(self):
        return reverse('manager:detail', kwargs={'budget_id':self.pk})

    def __str__(self):
        return self.budget_title + ': $' + str(self.budget_total)

class Section(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    section_title = models.CharField(max_length=50)
    section_budget = models.DecimalField(max_digits=17,decimal_places=2) #Must be less than BudgetTotal and >0, up to 1 quadrillion dollars
    def __str__(self):
        return self.section_title

class Transaction(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=17,decimal_places=2) #Can be + or -, , up to 1 quadrillion dollars
    trans_title = models.CharField(max_length=50)
    trans_description = models.CharField(max_length=250)
    trans_datetime = models.DateTimeField()
