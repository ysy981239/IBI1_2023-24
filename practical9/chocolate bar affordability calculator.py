def chocolate_bar_affordability(total_money, price_per_bar):
    bars_bought = total_money // price_per_bar
    change_left = total_money % price_per_bar
    return bars_bought, change_left

# example
total_money = 100  
price_per_bar = 7  
bars, change = chocolate_bar_affordability(total_money, price_per_bar)
print(f"You can buy {bars} chocolate bars and you will have {change} left as change.")