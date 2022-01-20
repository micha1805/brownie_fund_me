from pickletools import pystring
from brownie import network, accounts, exceptions
import pytest
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONNEMENTS
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    # +100 pour etre sur que ça marche
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONNEMENTS:
        pytest.skip("Only for local testing")
    fund_me = deploy_fund_me()
    other_account = accounts.add()
    # if another account (not the owner) tries to withdraw, it should raise an error:
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": other_account})
