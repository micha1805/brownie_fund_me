from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONNEMENTS,
)


def deploy_fund_me():
    account = get_account()
    ### pass the price feed address to the fund_me contract
    # print(f"Active network: {network.show_active()}")
    # print(f"LOCAL_BLOCKCHAIN_ENVIRONNEMENTS : {LOCAL_BLOCKCHAIN_ENVIRONNEMENTS}")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONNEMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    # print(f"getPrice() = {fund_me.getPrice()}")
    return fund_me


def main():
    deploy_fund_me()
