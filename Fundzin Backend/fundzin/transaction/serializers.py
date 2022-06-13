from rest_framework import serializers
from transaction.models import BankDetail, UPIDetail

"""
    Serializer for the transaction

    It has 4 classes

        ->BankDetailSerializer
        ->UPIDetailSerializer
        ->ExperimentalSerializer
        ->GetRequestSerializer

"""


class BankDetailSerializer(serializers.Serializer):
    """
    -> (int) id: To keep track of Bank Detail

    -> (String of length 255) user: Email of the user

    -> (String of length 255) bank_name: Name of the bank

    -> (String of length 50) bank_account_number: Account number of the bank

    -> (String of length 50) bank_confirm_account_number: Re enter the account number of bank

    -> (String of length 50) bank_ifsc_code: IFSC code

    -> (String of length 255) bank_name_of_holder: bank name of the holder
    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    bank_name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    bank_account_number = serializers.CharField(
        required=True, allow_blank=False, max_length=50
    )
    bank_confirm_account_number = serializers.CharField(
        required=True, allow_blank=False, max_length=50
    )
    bank_ifsc_code = serializers.CharField(
        required=True, allow_blank=False, max_length=50
    )
    bank_name_of_holder = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )

    def create(self, validated_data):
        """
        function to create a BankDetailSerializer

            accepts two Arguments
            self, validated_data

        creates the serializer
        """
        return BankDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        function to update a BankDetailSerializer

            accepts three Arguments
            self,instance, validated_data

        updates the serializer
        """
        # instance.username = validated_data.get('username', instance.username)
        # instance.email = validated_data.get('email', instance.email)
        # print(validated_data)
        # print(validated_data.keys())
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UPIDetailSerializer(serializers.Serializer):
    """
    -> (int) id: To keep track of Bank Detail

    -> (String of length 255) user: Email of the user

    -> (String of length 255) upi_id: upi id of the user
    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    upi_id = serializers.CharField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        function to create the UPIDeatailSerializer

            It takes two Arguments

                self, validated_data

        returns the created serializer
        """
        return UPIDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        function to update the UPIDeatailSerializer

            It takes three Arguments

                self,instance,validated_data

        returns the updated serializer
        """
        # instance.username = validated_data.get('username', instance.username)
        # instance.email = validated_data.get('email', instance.email)
        # print(validated_data)
        # print(validated_data.keys())
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


# class BankDetailUpdationRequestSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     user = serializers.EmailField(required=True,allow_blank=False,max_length=255)
#     new_bank_name = serializers.CharField(required=True,allow_blank=False,max_length=255)


class ExperimentalSerializer(serializers.Serializer):
    """
    -> (int) id: To keep track of Experiment

    -> (String of length 255) user: Email of the user

    -> (String of length 50) bank_account_number: Account number of the bank

    -> (String of length 50) bank_confirm_account_number: Re enter the account number of bank

    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    bank_account_number = serializers.CharField(
        required=True, allow_blank=False, max_length=50
    )
    bank_confirm_account_number = serializers.CharField(
        required=True, allow_blank=False, max_length=50
    )


class GetRequestSerializer(serializers.Serializer):
    """
    -> (int) id: To keep track of Requests

    -> (String of length 255) user: Email of the user
    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
