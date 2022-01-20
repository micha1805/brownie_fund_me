from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    # print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})
    print("Funded!")


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("Withdrawing...")
    fund_me.withdraw({"from": account})
    print("Withdrawed!")


def main():
    fund()
    withdraw()
