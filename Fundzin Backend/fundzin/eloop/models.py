from django.db import models

# Create your models here.


class EventLoopTransaction(models.Model):
    """
    Event loop class for transaction

    -> (String) data: data for tansaction

    -> (String) status: Status of transaction Pending / Successful or failure

    -> (String) created_at: Creation of the model

    -> (String) updated_at: Updation of the model

    """

    data = models.TextField()
    status = models.CharField(default="pending", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
