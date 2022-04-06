
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import secrets
# import Gift
from django.db.models.signals import post_save


class UniqueCodes(models.Model): 
       
    # Model field for our unique code
    code = models.CharField(max_length=8, blank=True, null=True, unique=True)
    
    def __str__(self):
        return "%s" % (self.code)

    
    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        
        # If new database record
        if created:
            # We have the primary key (ID Field) now so let's grab it
            id_string = str(instance.id)
            # Define our random string alphabet (notice I've omitted I,O,etc. as they can be confused for other characters)
            upper_alpha = "ABCDEFGHJKLMNPQRSTVWXYZ"
            # Create an 8 char random string from our alphabet
            random_str = "".join(secrets.choice(upper_alpha) for i in range(8))
            # Append the ID to the end of the random string
            instance.code = (random_str + id_string)[-8:]
            # Save the class instance
            instance.save()

    def __str__(self):
        return "%s" % (self.code,)


# Connect the post_create function to the UniqueCodes post_save signal
post_save.connect(Gift.post_create, sender=UniqueCodes)



# class Coupon(models.Model):

#     # number_of_coupons =models.IntegerField()


#     code = models.CharField(max_length=8, blank=True, null=True, unique=True)

#     valid_from = models.DateTimeField()

#     valid_to = models.DateTimeField()

#     discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

#     active = models.BooleanField()


#     def __str__(self):
#         return self.code