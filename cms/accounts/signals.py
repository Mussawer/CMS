from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer

'''
Signals comprised senders and receivers that send out some information to
receivers when event has occured 
'''
# sender is the model class whch is sending the signal
# instance is the actual instance being saved (which is instance of the sender)
# created is boolean True if new record is created
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )

# this how we connect sender to a receiver
# receiver = customer profile
# and sender is the model that is going to trigger        
post_save.connect(customer_profile, sender=User)
