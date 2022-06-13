from brownie import accounts, DonorUser


def create_new_user():
    account = accounts.load("polygonfellowship2022@gmail.com.com")
    print(account)

    # deploy an instance of the smart contract
    new_user_contract = DonorUser.deploy(
        "anshsarkar18@gmail.com",
        "aba811083011de7905401f0aa800bf7d3c694d858c61dc5dff2e095d2073c42a",
        {"from": account},
    )
    # get the owner of the smart contract
    print(new_user_contract.getOwner())

    # get the hashed password stored in the contract
    print(new_user_contract.getHashedPassword())
    # update and print the returned values when updatePassword function is run
    print(
        new_user_contract.updatePassword(
            "37fea394d6ccd90ba02277cc90f12d9a50e09283ef78096bbf208c858a89590f"
        )
    )
    # get the hashed password once again after updation
    print(new_user_contract.getHashedPassword())

    # get total donations
    print(new_user_contract.getTotalDonations())
    # increment donations by 2000
    print(new_user_contract.incrementDonations(2000))
    # get total donations to check reflection of previous transaction
    print(new_user_contract.getTotalDonations())
    # decrement donations by 1500
    print(new_user_contract.decrementDonations(1500))
    # get total donations to check reflection of previous transaction
    print(new_user_contract.getTotalDonations())

    # get email ID
    print(new_user_contract.getEmailID())
    # update email ID
    print(new_user_contract.updateEmailID("anshsark18@gmail.com"))
    # get email ID to check reflection of previous transaction
    print(new_user_contract.getEmailID())

    # we then delete the user (can only be done by owner)
    if new_user_contract.deleteUser:
        print("User has been deleted !")
    else:
        print("Something went wrong while deleting the user . Kindly retry !")


def main():
    create_new_user()
