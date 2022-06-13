import time
import psycopg2
import brownie._cli.accounts as cli
from cryptography.fernet import Fernet
from brownie import accounts, SimpleStorage

# defines the priority given to tasks in the queue
PRIORITY_FILTER = {
    0: "newuser",
    1: "newfundraiser",
    2: "newfundraisermilestone",
    3: "newfundraiserdonation",
    4: "newisdonorcheckrequest",
    5: "newgetamountraisedrequest",
    6: "newvote",
    7: "newactivatevotingrequest",
    8: "getnumberofdonorsrequest",
    9: "getnumberofvotesforcurrentmilestonerequest",
    10: "getcurrentmilestonenumber",
    11: "fundraisercompletionrequest",
}

# assigns priority to tasks
def priority_assign():
    priority_array = [
        "newuser",
        "newfundraiser",
        "newfundraisermilestone",
        "newfundraiserdonation",
        "newisdonorcheckrequest",
        "newgetamountraisedrequest",
        "newvote",
        "newactivatevotingrequest",
        "getnumberofdonorsrequest",
        "getnumberofvotesforcurrentmilestonerequest",
        "getcurrentmilestonenumber",
        "fundraisercompletionrequest",
    ]
    for i in range(len(PRIORITY_FILTER)):
        PRIORITY_FILTER[i] = priority_array[i]


# loading key from local storage
def call_key():
    return open("pass.key", "rb").read()


# encrypting data using Fernet Encryption
def encrypt(data):
    return (Fernet(call_key()).encrypt(data.encode())).decode()


# decrypting data using Fernet Encryption
def decrypt(data):
    return (Fernet(call_key()).decrypt(data.encode())).decode()


# fetch the contract by passing its address
def getContract(address):
    contract = SimpleStorage.at(address)
    print(contract.getOwner())
    return contract


# get a list of all the accounts in brownie
def list_accounts():
    cli._list()


# load a particular account in brownie
def load_account(user, password):
    account = accounts.load(user + ".fnzbuff", password=password)
    return account


# parsing the data
def parse(data):
    tokens = data.split("~")
    d = {}
    for token in tokens:
        token = token.split(":")
        d[token[0]] = token[1]
    return d


# execute a task based on type
def execute(d):
    return_obj = {}

    if d["type"] == "newuser":
        try:
            return_obj = create_new_account(d["email"], d["password"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newfundraiser":
        try:
            return_obj = deploy_contract(
                d["user"],
                d["password"],
                d["account_holder"],
                d["ifsc_code"],
                d["bank_name"],
                d["account_number"],
                d["upi_id"],
                d["target_amount"],
            )
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newfundraisermilestone":
        try:
            return_obj = add_new_milestone(
                d["address"],
                d["user"],
                d["password"],
                d["milestone_desc"],
                d["milestone_amt"],
            )
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newfundraiserdonation":
        try:
            return_obj = make_new_donation(
                d["user"],
                d["password"],
                d["address"],
                d["donation_amount"],
            )
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newisdonorcheckrequest":
        try:
            return_obj = is_donor_check(d["user"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newgetamountraisedrequest":
        try:
            return_obj = get_amount_raised(d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newvote":
        try:
            return_obj = new_vote(d["user"], d["password"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "newactivatevotingrequest":
        try:
            return_obj = activate_voting(d["user"], d["password"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "getnumberofdonorsrequest":
        try:
            return_obj = number_of_donors(d["user"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "getnumberofvotesforcurrentmilestonerequest":
        try:
            return_obj = votes_for_current(d["user"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "getcurrentmilestonenumber":
        try:
            return_obj = current_milestone(d["user"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    elif d["type"] == "fundraisercompletionrequest":
        try:
            return_obj = check_fundraiser_completion(d["user"], d["address"])
            return return_obj
        except Exception as error:
            return_obj["message"] = "possible malformed request"
            return_obj["error"] = str(error)
            return_obj["status"] = "fatalerror"
            return return_obj

    else:
        return_obj["message"] = "possible malformed request"
        return_obj["error"] = str(error)
        return_obj["status"] = "fatalerror"
        return return_obj


# -------------------------------------------------------------------
#                         Execution Functions                      #
# -------------------------------------------------------------------

# create a new account
def create_new_account(user, password):

    return_obj = {}

    try:
        new_user = accounts.add()
        new_user.save(user, password=password)
        account = load_account(user, password)
        return_obj[
            "message"
        ] = "your account was successfully created. account address : {address}".format(
            address=str(account)
        )
        return_obj["user_address"] = str(account)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj["message"] = "failed to create account . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# add a new milestone
def add_new_milestone(address, user, password, milestone_desc, milestone_amt):

    return_obj = {}

    try:
        contract = getContract(address)
        account = load_account(user, password)
        newMilestoneCreation = contract.addMilestone(
            milestone_desc, milestone_amt, {"from": account}
        )
        number_of_milestones = contract.getNumberOfMilestones
        events = str(newMilestoneCreation.events)

        return_obj[
            "message"
        ] = "new milestone added successfully to fundraiser : {address}".format(
            address=address
        )
        return_obj["milestone_number"] = "{number}".format(number=number_of_milestones)
        return_obj["raw_event_data"] = events
        return_obj["user_address"] = str(account)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to add new milestone . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# deploy a contract
def deploy_contract(
    user,
    password,
    account_holder,
    ifsc_code,
    bank_name,
    account_number,
    upi_id,
    target_amount,
):

    return_obj = {}

    try:
        account = load_account(user, password)
        print(account)
        simple_storage = SimpleStorage.deploy(
            account_holder,
            ifsc_code,
            bank_name,
            account_number,
            upi_id,
            target_amount,
            {
                "from": account,
            },
        )

        return_obj[
            "message"
        ] = "new fundraiser deployed successfully at {address}".format(
            address=simple_storage.address
        )
        return_obj["user_address"] = str(account)
        return_obj["contract_address"] = str(simple_storage.address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to deploy new fundraiser . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# make a new donation
def make_new_donation(user, password, address, donation_amount):

    return_obj = {}

    try:
        account = load_account(user, password)
        contract = getContract(address)
        txn = contract.newDonation(str(account), donation_amount, {"from": account})
        events = str(txn.events)

        return_obj[
            "message"
        ] = "new donation added successfully to contract : {address}".format(
            address=address
        )
        return_obj["user_address"] = str(account)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to add new donation . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# check whether user address is donor or not
# Note : In this case we need to pass the user address
def is_donor_check(user_address, address):

    return_obj = {}

    try:
        contract = getContract(address)
        txn = contract.isDonor(user_address)
        print(txn)

        return_obj[
            "message"
        ] = "donor data fetched successfully from : {address}".format(address=address)
        return_obj["is_donor"] = txn
        return_obj["user_address"] = str(user_address)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to fetch donor data . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# fetch the amount raised
def get_amount_raised(address):

    return_obj = {}

    try:
        contract = getContract(address)
        txn = contract.getFundraiserAmountRaised()
        print(txn)

        return_obj[
            "message"
        ] = "fundraiser_amount_raised data fetched successfully from : {address}".format(
            address=address
        )
        return_obj["amount_raised"] = txn
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to fetch fundraiser_amount_raised data . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# cast vote
def new_vote(user, password, address):

    return_obj = {}

    try:
        account = load_account(user, password)
        contract = getContract(address)
        txn = contract.castVote(str(account), {"from": account})
        print(txn)

        return_obj["message"] = "vote casted successfully to : {address}".format(
            address=address
        )
        return_obj["events"] = str(txn)
        return_obj["user_address"] = str(account)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj["message"] = "failed to cast vote . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# activate voting for a particular milestone
def activate_voting(user, password, address):

    return_obj = {}

    try:
        account = load_account(user, password)
        contract = getContract(address)
        txn = contract.activateVotingForCurrentMilestone({"from": account})
        print(txn)

        return_obj["message"] = "voting activated successfully for : {address}".format(
            address=address
        )
        return_obj["events"] = str(txn)
        return_obj["user_address"] = str(account)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to activate voting . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# fetch the number of donors
def number_of_donors(user, address):

    return_obj = {}

    try:
        contract = getContract(address)
        txn = contract.getNumberOfDonors()
        print(txn)
        print(user)

        return_obj[
            "message"
        ] = "fetched number of donors successfully for : {address}".format(
            address=address
        )
        return_obj["number_of_donors"] = str(txn)
        return_obj["user_address"] = str(user)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to activate voting . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# fetch number of votes for the current milestone
def votes_for_current(user, address):

    return_obj = {}

    try:
        contract = getContract(address)
        txn = contract.votesCastForCurrentMilestone()
        print(txn)
        print(user)

        return_obj[
            "message"
        ] = "fetched number of votes successfully for current milestone in : {address}".format(
            address=address
        )
        return_obj["number_of_votes"] = str(txn)
        return_obj["user_address"] = str(user)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to fetch number of votes for the current milestone . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# fetch the current milestone number
def current_milestone(user, address):

    return_obj = {}

    try:
        contract = getContract(address)
        txn = contract.currentMilestoneNumber()
        print(txn)
        print(user)

        return_obj[
            "message"
        ] = "fetched current milestone number successfully for contract : {address}".format(
            address=address
        )
        return_obj["current_milestone"] = str(txn)
        return_obj["user_address"] = str(user)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to fetch current milestone number . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# check if the fundraiser has been completed
def check_fundraiser_completion(user, address):

    return_obj = {}

    try:
        contract = getContract(address)
        txn = contract.isFundraiserCompleted()
        print(txn)
        print(user)

        return_obj[
            "message"
        ] = "fundraiser_completion data fetched successfully for contract : {address}".format(
            address=address
        )
        return_obj["completed"] = str(txn)
        return_obj["user_address"] = str(user)
        return_obj["contract_address"] = str(address)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "success"

    except Exception as error:
        return_obj[
            "message"
        ] = "failed to fetch fundraiser_completion data . kindly retry after sometime"
        return_obj["error"] = str(error)
        return_obj["txn_exec_timestamp"] = time.time()
        return_obj["status"] = "rejected"

    return return_obj


# get user contract address given username and password
def get_user_address(user, password):
    account = load_account(user, password)
    return str(account)


def main():
    # connect to the database
    conn = psycopg2.connect(
        host="<host>", database="<database>", user="<user>", password="<password>"
    )
    BATCH_SIZE = 100
    cursor = conn.cursor()
    while True:
        local_cache = []

        cursor.execute(
            """SELECT * FROM public.eloop_eventlooptransaction WHERE status = 'pending' LIMIT {batch_size};""".format(
                batch_size=BATCH_SIZE
            )
        )

        for pending_transaction in cursor.fetchall():
            print(pending_transaction)
            txn_data = decrypt(pending_transaction[1])
            local_cache.append(parse(txn_data))
            print(txn_data)

        for level in PRIORITY_FILTER.keys():
            for txn in local_cache:
                if txn["type"] == PRIORITY_FILTER[level]:
                    print(txn)
                    try:
                        post_exec = execute(txn)
                        print(post_exec)
                    except:
                        pass
    cursor.close()
    conn.close()
