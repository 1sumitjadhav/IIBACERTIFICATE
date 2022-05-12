from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import secrets
from django.db.models.signals import post_save
import random
from datetime import datetime
from datetime import date
from django.utils import timezone
todayDate = date.today()

# expires date  
class ActiveManager(models.Manager):
    """
    This special manager only retrieves active objects (when the current date
    is between the object's publish date and/or its expiration date).

    The date fields are given when creating the Manager instance. If either is
    None then the manager will not take it into account for filtering.

    Example definition for a model:

    class ExampleModel(models.Model):
        publish_date = models.DateTimeField()
        expire_date = models.DateTimeField(blank=True, null=True)

        actives = ActiveManager(from_date='publish_date', to_date='expire_date')

    Or if the model only had an expire_date:

    class ExampleModel(models.Model):
        expire_date = models.DateTimeField(blank=True, null=True)

        actives = ActiveManager(from_date=None, to_date='expire_date')

    Each instance of the manager has an attribute date_filters which can be used in
    custom queries. For example, if you have a ManyToMany relationship to a model
    with ActiveManager and you can't access via the manager (because you
    need to use select_related, for example) then you can do:

    instance.many_to_many.filter(*ExampleModel.actives.date_filters)

    """

    def __init__(self, from_date=None, to_date=None):
        super(ActiveManager, self).__init__()
        self.from_date = from_date
        self.to_date = to_date
        now = datetime.now
        if from_date and to_date:
            self.date_filters = (models.Q(**{'%s__isnull' % self.to_date: True}) |
                                 models.Q(**{'%s__gte' % self.to_date: now}),
                                 models.Q(**{'%s__isnull' % self.from_date: True}) |
                                 models.Q(**{'%s__lte' % self.from_date: now}))

        elif from_date:
            self.date_filters = (models.Q(**{'%s__isnull' % self.from_date: True}) |
                                 models.Q(**{'%s__lte' % self.from_date: now}),)
        elif to_date:
            self.date_filters = (models.Q(**{'%s__isnull' % self.to_date: True}) |
                                 models.Q(**{'%s__gte' % self.to_date: now}),)
        else:
            raise ValueError( "At least one date field is required")

    def get_query_set(self):
        """Retrieves items with publication dates according to self.date_filters
        """
class Coupon_gener(models.Model): 
       
    # Model field for our unique code
    # coupon = models.BooleanField(default=False)
    code = models.CharField(max_length=8, blank=True, null=True, unique=True)

    def __str__(self):
        return "%s" % (self.code)
class coupon(models.Model):
    # coupon =  models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    publish_date = models.DateTimeField(default=todayDate)
    expire_date = models.DateTimeField()

    objects = models.Manager()
    actives = ActiveManager(from_date='publish_date', to_date='expire_date')
    def __str__(self):
        return self.code
