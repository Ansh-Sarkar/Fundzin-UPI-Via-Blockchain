from rest_framework import serializers
from fundraiser.models import Fundraiser, FundraiserImages, FundraiserMilestones


class FundraiserSerializer(serializers.Serializer):
    """
    This is the serializer class for Fundraiser:
        it contains:

        -> (String of length 255) user: An email field which is used to input the Email of the fundraiser

        -> (String of length 255) fundraiser_domain: fundraiser domain for putting the domain of the fundraiser

        -> (String of length 255) creator_location: location of the fundraiser

        -> (String of length 255) contact_number_country_code: a field for country code which has a max length of 5

        -> (String of length 255) contact_number: contact number of fundraser 10 digit

        -> (String of length 255) title: A title to be shown on the Application

        -> (String of length 255) cause:Reason why the fundraiser wants funds in a nutshell

        -> (String) Story: An elaborated version for why the fundraiser wants funding

        -> (int) target_amount: Money required to fullfill the goal of the user

        -> Is the fundraised amount going to get involved in any sort of political or religius activity?

        -> Add the upi id to transfer the money
    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    fundraiser_domain = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )
    creator_location = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )
    contact_number_country_code = serializers.CharField(
        required=True, allow_blank=False, max_length=5
    )
    contact_number = serializers.CharField(
        required=True, allow_blank=False, max_length=10
    )
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    cause = serializers.CharField(required=True, allow_blank=False, max_length=255)
    story = serializers.CharField(required=True)
    target_amount = serializers.IntegerField(required=True)
    political_or_religious_inclination = serializers.BooleanField(required=True)
    add_upi = serializers.BooleanField(required=True)

    def create(self, validated_data):
        """
        This function creates the fundraiser serializer

        Takes 2 arguments:
            self
            validated_data


        """
        return Fundraiser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        This function handles any
        sort of addition or deletion in the fundraiser serializer

        This function takes three arguments:

            self,
            instance,
            validated_data

        and returns the updated serializer
        """
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FundraiserImageSerializer(serializers.Serializer):
    """
    This is the serializer class for Fundraiser:

    it contains:

        it takes an image
    """

    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        This is the function to create the Fundraiser image

            takes two argument
                self and validated data

            and returns the created Image serializer
        """
        return FundraiserImages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        This is the function to update the Fundraiser image

            takes three argument
                self instance and validated data

            and updates the image serializer
        """
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FundraiserMilestoneSerializer(serializers.Serializer):
    """
    This is the serializer class for Fundraiser:
        it contains:

        -->id
        -->(String of length 255) user: An email field which is used to input the Email of the fundraiser

        -->(String of length 255) milestone_id: An id for milestone

        -->(String of length 255) milestone_title: Title for milestone to be displayed

        -->(String of length 255) milestone_desc: Milestone description

        -->(String of length 255) milestone_release_amount: Money after completion of each milestone

    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    milestone_id = serializers.IntegerField(required=True)
    milestone_title = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    milestone_desc = serializers.CharField(
        required=True, allow_blank=False, max_length=400
    )
    milestone_release_amount = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        This is the function to create the Fundraiser image

            takes two argument
                self, validated data

            and creates the milestone serializer
        """
        return FundraiserMilestones.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
