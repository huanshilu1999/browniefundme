from brownie import accounts,network,config,MockV3Aggregator
from web3 import Web3
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["development","mainnet-fork-dev"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
def depoly_mocks():
    print(f"Contract network is {network.show_active()}")
        #print(f"Contract deploy to {fund_me.address}")
    print("Deploying Mocks..... ")
    if len(MockV3Aggregator) <= 0:
         MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from": get_account()}
        )
    print("Mocks Deployed! ")

def main():
    get_account()