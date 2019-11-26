import Constants
import AccountAgent


def init(webdriver):
    Constants.init()
    AccountAgent.login(webdriver)


def update(webdriver):
    return