import os
import json
from web3 import Web3
from solcx import compile_standard

os.getenv("hello")

"""
    Note: This file is not a part of the final implementation of the Fundzin Smart Contracts
    Library (FSCL). It has been deprecated as we now use brownie as an integrated environment
    for compiling, deploying and executing smart contracts.
"""

if __name__ == "__main__":

    # fetching file contents
    with open("./SimpleStorage.sol", "r") as file:
        simple_storage_file = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "SimpleStorage.sol": {
                    "content": simple_storage_file,
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": [
                            "abi",
                            "metadata",
                            "evm.bytecode",
                            "evm.sourceMap",
                        ],
                    },
                },
            },
        },
        solc_version="0.6.0",
    )

    # fetching compiled code
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    # extracting bytecode and abi
    bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

    # connecting to ganache
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    print(w3.isConnected())
    chain_id = 1337
    my_address = "<my-address>"
    # Note: Always add 0x in front of the private key
    private_key = "<private-key>"

    # creating the contract in python
    SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
    # get latest transaction count
    nonce = w3.eth.getTransactionCount(my_address)
    print("Creating Transaction . . . .")

    # creating a transaction
    transaction = SimpleStorage.constructor().buildTransaction(
        {"chainId": chain_id, "from": my_address, "nonce": nonce}
    )
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    # sending the transaction
    print("Deploying Contract on Ropsten Testnet . . . ")
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)
    print("Contract Deployed !")
    # print(nonce)

    # retrieving current state of contract
    simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    print("Retrieving Current Contract State . . .")
    print(simple_storage.functions.retrieve().call())

    # updating the contract
    print("Updating Contract . . . ")
    store_transaction = simple_storage.functions.store(15).buildTransaction(
        {
            "chainId": chain_id,
            "from": my_address,
            "nonce": nonce + 1,
        }
    )
    signed_store_tx = w3.eth.account.sign_transaction(
        store_transaction, private_key=private_key
    )
    transaction_hash = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("Contract Updated !")

    # retrieving current state of contract
    print("Retrieving Current Contract State . . .")
    print(simple_storage.functions.retrieve().call())
