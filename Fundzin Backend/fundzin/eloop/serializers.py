from cryptography.fernet import Fernet
from rest_framework import serializers
from eloop.models import EventLoopTransaction


def call_key():
    return open("pass.key", "rb").read()


def encrypt(data):
    return (Fernet(call_key()).encrypt(data.encode())).decode()


def decrypt(data):
    return (Fernet(call_key()).decrypt(data.encode())).decode()


class EloopNewUserSerializer(serializers.Serializer):
    """
    event loop class to if donor or not

    -> (String of length 255) user_address: Email of the user

    -> (String of length 255) password: password of the user

    -> (String of length 255) address: Address of the user

    """

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(required=True, allow_blank=False, max_length=255)
    email = serializers.EmailField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        data = encrypt(
            "email:{email}~password:{password}~status:pending~type:newuser".format(
                email=validated_data["email"], password=validated_data["password"]
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        data = encrypt(
            "email:{email}~password:{password}~status:pending~type:newuser".format(
                email=validated_data["email"], password=validated_data["password"]
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopNewFundraiserSerializer(serializers.Serializer):
    """
    Class for the event loop Serializer

    -> (int) id: to keep tract of the eventloop serializer

    -> (String) user: Email of the user

    -> (String) password: Password of the user

    -> (String) account_holder: Account holder

    -> (String) ifsc_code: IFSC code

    -> (String) bank_name: Name of the bank

    -> (String) account_number: Account number of the user

    -> (String) upi_id: UPI id of the user

    -> (int) target_amount: Target amount by the user
    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    password = serializers.CharField(required=True, allow_blank=False, max_length=255)
    account_holder = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )
    ifsc_code = serializers.CharField(required=True, allow_blank=False, max_length=255)
    bank_name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    account_number = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )
    upi_id = serializers.CharField(required=True, allow_blank=False, max_length=255)
    target_amount = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        function to create the event loop

            -> encrypts the data

            -> (String) user

            -> (String) password

            -> (String) account_holder

            -> (String) ifsc_code

            -> (String) bank_name

            -> (String) account_number

            -> (String) upi_id

            -> (int) target_amount

        returns the event loop transaction
        """
        data = encrypt(
            "user:{user}~password:{password}~account_holder:{account_holder}~ifsc_code:{ifsc_code}~bank_name:{bank_name}~account_number:{account_number}~upi_id:{upi_id}~target_amount:{target_amount}~status:pending~type:newfundraiser".format(
                user=validated_data["user"],
                password=validated_data["password"],
                account_holder=validated_data["account_holder"],
                ifsc_code=validated_data["ifsc_code"],
                bank_name=validated_data["bank_name"],
                account_number=validated_data["account_number"],
                upi_id=validated_data["upi_id"],
                target_amount=validated_data["target_amount"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopNewFundraiserMilestoneSerializer

        takes two arguments

            self, validated_data

            assigns data:

           (String) user

            (String) password

            (String) address

            (String) milestone_desc

            (String) milestone_amt

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~account_holder:{account_holder}~ifsc_code:{ifsc_code}~bank_name:{bank_name}~account_number:{account_number}~upi_id:{upi_id}~target_amount:{target_amount}~status:pending~type:newfundraiser".format(
                user=validated_data["user"],
                password=validated_data["password"],
                account_holder=validated_data["account_holder"],
                ifsc_code=validated_data["ifsc_code"],
                bank_name=validated_data["bank_name"],
                account_number=validated_data["account_number"],
                upi_id=validated_data["upi_id"],
                target_amount=validated_data["target_amount"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopNewFundraiserMilestoneSerializer(serializers.Serializer):
    """
    New fundraizer milestone Serializer class

    -> (String of length 255) user: Email of the user

    -> (String of length 255) password: Password of the user

    -> (String of length 255) address: Address of the user

    -> (String of length 255) milestone_description: Reason for the milestone

    -> (String of length 255) milestone_release_amount: Amount released after completion

    """

    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    password = serializers.CharField(required=True, allow_blank=False, max_length=255)
    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    milestone_desc = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    milestone_release_amount = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopNewFundraiserMilestoneSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) password

            (String) address

            (String) milestone_desc

            (String) milestone_amt

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~milestone_desc:{milestone_desc}~milestone_amt:{milestone_amt}~status:pending~type:newfundraisermilestone".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
                milestone_desc=validated_data["milestone_desc"],
                milestone_amt=validated_data["milestone_release_amount"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopNewFundraiserMilestoneSerializer

        takes two arguments

            self, validated_data

            assigns data:

           (String) user

            (String) password

            (String) address

            (String) milestone_desc

            (String) milestone_amt

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~milestone_desc:{milestone_desc}~milestone_amt:{milestone_amt}~status:pending~type:newfundraisermilestone".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
                milestone_desc=validated_data["milestone_desc"],
                milestone_amt=validated_data["milestone_release_amount"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopNewDonationSerializer(serializers.Serializer):
    """
    event loop class to create a new donation serializer

    -> (String of length 255) user: Email of the user

    -> (String of length 255) password: Password of the user

    -> (String of length 255) address: Address of the user

    -> (String of length 255) donation_amount: Reason for the milestone

    """

    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    password = serializers.CharField(required=True, allow_blank=False, max_length=255)
    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    donation_amount = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )

    def create(self, validated_data):
        """
        this function creates the serializer of EloopNewDonationSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            (int) donation_amount

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~donation_amount:{donation_amount}~status:pending~type:newfundraiserdonation".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
                donation_amount=validated_data["donation_amount"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopActivateVotingSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) password

            (String) address

            (int) donation_amount

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~donation_amount:{donation_amount}~status:pending~type:newfundraiserdonation".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
                donation_amount=validated_data["donation_amount"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopNewCheckIsDonorRequestSerializer(serializers.Serializer):
    """
    event loop class to if donor or not

    -> (String of length 255) user_address: Address of the user

    """

    user_address = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )
    address = serializers.CharField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopNewCheckIsDonorRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:newisdonorcheckrequest".format(
                user=validated_data["user_address"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopNewCheckIsDonorRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:newisdonorcheckrequest".format(
                user=validated_data["user_address"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopNewGetAmountRaisedSerializer(serializers.Serializer):
    """
    event to get the amount raised

    -> (String of length 255) address: Address of the user

    """

    address = serializers.CharField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopNewGetAmountRaisedSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "address:{address}~status:pending~type:newgetamountraisedrequest".format(
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopNewGetAmountRaisedSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "address:{address}~status:pending~type:newgetamountraisedrequest".format(
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopNewVoteSerializer(serializers.Serializer):
    """
    This is a event loop class that creates the voting serializer

    ->(String of length 255) user: Email of the user

    ->(String of length 255) password: Password of the user

    ->(String of length 255) address: Address of the user

    """

    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    password = serializers.CharField(required=True, allow_blank=False, max_length=255)
    address = serializers.CharField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopNewVoteSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) password

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~status:pending~type:newvote".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopNewVoteSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~status:pending~type:newvote".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopActivateVotingSerializer(serializers.Serializer):
    """
    This is a event loop class that activates the voting serializer

    ->(String of length 255) address: Address of the user

    ->(String of length 255) password: Password of the user

    ->(String of length 255) user: Email of the user

    """

    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
    password = serializers.CharField(required=True, allow_blank=False, max_length=255)
    address = serializers.CharField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopActivateVotingSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~status:pending~type:newactivatevotingrequest".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopActivateVotingSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~password:{password}~address:{address}~status:pending~type:newactivatevotingrequest".format(
                user=validated_data["user"],
                password=validated_data["password"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopGetNumberOfDonorsRequestSerializer(serializers.Serializer):
    """
    This is a event loop class that gets the number of Doners

    ->(String of length 255) address: Address of the user

    ->(String of length 255) user: Email of the user

    """

    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopGetNumberOfVotesForCurrentMilestoneRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:getnumberofdonorsrequest".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopGetNumberOfVotesForCurrentMilestoneRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:getnumberofdonorsrequest".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopGetNumberOfVotesForCurrentMilestoneRequestSerializer(serializers.Serializer):
    """
    This is a event loop class that gets the number of votes for the current milestone

    ->(String of length 255) address: Address of the user

    ->(String of length 255) user: Email of the user

    """

    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopGetNumberOfVotesForCurrentMilestoneRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:getnumberofvotesforcurrentmilestonerequest".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopGetNumberOfVotesForCurrentMilestoneRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:getnumberofvotesforcurrentmilestonerequest".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopGetCurrentMilestoneNumberRequestSerializer(serializers.Serializer):
    """
    This is a event loop class that gets all the number of current Milestones

    ->(String of length 255) address: Address of the user

    ->(String of length 255) user: Email of the user

    """

    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopGetCurrentMilestoneNumberRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:getcurrentmilestonenumber".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopGetCurrentMilestoneNumberRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:getcurrentmilestonenumber".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)


class EloopFundraiserCompletionCheckRequestSerializer(serializers.Serializer):
    """
    This is a event loop class that checks the request of fundraiser completion

    ->(String of length 255) address: Address of the user

    ->(String of length 255) user: Email of the user

    """

    address = serializers.CharField(required=True, allow_blank=False, max_length=255)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        this function creates the serializer of EloopFundraiserCompletionCheckRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:fundraisercompletionrequest".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)

    def save(self, validated_data):
        """
        this function saves the serializer of EloopFundraiserCompletionCheckRequestSerializer

        takes two arguments

            self, validated_data

            assigns data:

            (String) user

            (String) address

            returns the eventlooptransaction
        """
        data = encrypt(
            "user:{user}~address:{address}~status:pending~type:fundraisercompletionrequest".format(
                user=validated_data["user"],
                address=validated_data["address"],
            )
        )
        return EventLoopTransaction.objects.create(data=data)
