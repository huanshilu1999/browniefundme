from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_script import get_account,depoly_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS,FORKED_LOCAL_ENVIRONMENTS 



def deplopy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS or FORKED_LOCAL_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
      
    else:
        depoly_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_me
    

def main():
    deplopy_fund_me()
    
