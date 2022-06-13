from django.db import models

# Create your models here.
class BankDetail(models.Model):
    """

    -> (String of length 255) user: Email of the user

    -> (String of length 255) bank_name: Name of the bank

    -> (String of length 50) bank_account_number: Account number of the bank

    -> (String of length 50) bank_confirm_account_number: Re enter the account number of bank

    -> (String of length 50) bank_ifsc_code: IFSC code

    -> (String of length 255) bank_name_of_holder: bank name of the holder

    -> (String)created_at: BankDetail model creation time

    -> (String)updated_at: BankDetail model updation time
    """

    user = models.EmailField(max_length=255, unique=True)
    bank_name = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=50)
    bank_confirm_account_number = models.CharField(max_length=50)
    bank_ifsc_code = models.CharField(max_length=50)
    bank_name_of_holder = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UPIDetail(models.Model):
    """
    -> (String of length 255) user: Email of the user

    -> (String of length 255) upi_id: Upi id of the user

    -> (String)created_at: UPIDetail model creation time

    -> (String)updated_at:UPIDetail model updation time

    """

    user = models.EmailField(max_length=255, unique=True)
    upi_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
