from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image, downSizeWidth=None, downSizeHeight=None):
    """
    Function to compress image size

        Takes 3 arguments

            image, downSizeWidth, downSizeHeight

            -> checks if height and width are non
            -> Resizes the image

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


# Create your models here.
class Notification(models.Model):
    """
    -> (String of length 255) sent_to: Email id of the reciever

    -> (String of length 255) title: A title to be shown on the Notification

    -> (String) message: A message to be shown on the Notification

    -> (String) img: Image for the notification

    -> (String)created_at: Notification model creation time
    """

    sent_to = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    img = models.ImageField(upload_to="imgs/notifications/")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        a function that saves the image,
        takes two argument

            self.img,downSizeWidth

        saves the image
        """
        new_image = compress(self.img, downSizeWidth=500)
        self.img = new_image
        super().save(*args, **kwargs)
