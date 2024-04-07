from django.db import models

# step 1 after creating the model
# Create your models here.
class creator(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    updated_on=models.DateTimeField(auto_now=True)

    # for better readability in admin.
    def __str__(self):
        return self.title