def loose_change(coins_list, amount_of_change):
    solution = [0] + [amount_of_change + 1] * amount_of_change
    for atmc in range(1, amount_of_change + 1):
        for coin in coins_list:
            if coin <= atmc:
                solution[atmc] = min(solution[atmc], solution[atmc - coin] + 1)
    return -1 if solution[amount_of_change] > amount_of_change else solution[amount_of_change]