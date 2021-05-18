
cost_of_Coin = 400

from math import ceil


def coinPrice(price):

    return ceil(price/cost_of_Coin)

def get_current_coin_price():
    return cost_of_Coin