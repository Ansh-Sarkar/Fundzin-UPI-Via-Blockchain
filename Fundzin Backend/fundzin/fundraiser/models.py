from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files import File

# Create your models here.


def compress(image, downSizeWidth=None, downSizeHeight=None):
    """
    Function to compress image size

        Takes 3 arguments

            image, downSizeWidth, downSizeHeight

            -> checks if height and width are non
            ->  Resizes the image

        returns the new image

    """
    im = Image.open(image)
    im_io = BytesIO()
    downSizeWidth = downSizeWidth
    downSizeHeight = downSizeHeight
    if downSizeHeight is not None and downSizeWidth is not None:
        im = im.resize((downSizeWidth, downSizeHeight), Image.ANTIALIAS)
    elif downSizeWidth is not None:
        wpercent = downSizeWidth / float(im.size[0])
        hsize = int((float(im.size[1]) * float(wpercent)))
        im = im.resize((downSizeWidth, hsize), Image.ANTIALIAS)
    else:
        hpercent = downSizeHeight / float(im.size[1])
        wsize = int((float(im.size[0]) * float(hpercent)))
        im = im.resize((wsize, downSizeHeight), Image.ANTIALIAS)
    print(dir(image))
    im.save(im_io, image.name.split(".")[-1], quality=70)
    new_image = File(im_io, name=image.name)
    return new_image


class Fundraiser(models.Model):
    """
    This is the Model class for Fundraiser:
        it contains:

        -> (String of length 255) user: An email field which is used to input the Email of the fundraiser

        -> (String of length 255) fundraiser_domain: fundraiser domain for putting the domain of the fundraiser

        -> (String of length 255) creator_location: location of the fundraiser

        -> (String of length 5) contact_number_country_code: a field for country code which has a max length of 5

        -> (String of length 10) contact_number: contact number of fundraser 10 digit

        -> (String of length 255) title: A title to be shown on the Application

        -> (String of length 255) cause: Reason why the fundraiser wants funds in a nutshell

        -> (String) Story: An elaborated version for why the fundraiser wants funding

        -> (int) target_amount: Money required to fullfill the goal of the user

        -> (boolean) political_or_religious_inclination: Is the fundraised amount going to get involved in any sort of political or religius activity?

        -> (String) add_upi: Add the upi id to transfer the money

        -> (String)created_at: fundraizer model creation time

        -> (String)updated_at: fundraizer model updation time

    """

    user = models.EmailField(max_length=255, unique=True)
    fundraiser_domain = models.CharField(max_length=255)
    creator_location = models.CharField(max_length=255)
    contact_number_country_code = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=10)
    verified_mobile_number = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    cause = models.CharField(max_length=255)
    story = models.CharField(max_length=5000)
    target_amount = models.IntegerField()
    political_or_religious_inclination = models.BooleanField(default=False)
    add_upi = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FundraiserImages(models.Model):
    """
    -> (String) user:

    -> (int) id: To keep track of image through an image id

    -> (String)img: Accept image from the user

    -> (String)created_at: fundraizer model creation time

    -> (String)updated_at: fundraizer model updation time
    """

    user = models.EmailField(max_length=255)
    image_id = models.IntegerField()
    img = models.ImageField(upload_to="imgs/fundraisers/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Functiont to save the image:

            Takes three arguments:

                self, *args, **kwargs
        """
        new_image = compress(self.img, downSizeWidth=500)
        self.img = new_image
        super().save(*args, **kwargs)


class FundraiserMilestones(models.Model):
    """
    -> (String of length 255) user: An email field which is used to input the Email of the fundraiser

    -> (int) milestone_id: An id to keep track of the milestone

    -> (String of length 100) milestone_title: A title for the Milestone

    -> (String of length 400) milestone_desc: A description for the Milestone

    -> (int) target_amount: Money required to fullfill the Milestone of the user

    -> (String) created_at: fundraizer model creation time

    -> (String) updated_at: fundraizer model updation time
    """

    user = models.EmailField(max_length=255)
    milestone_id = models.IntegerField(unique=True)
    milestone_title = models.CharField(max_length=100)
    milestone_desc = models.CharField(max_length=400)
    milestone_release_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
