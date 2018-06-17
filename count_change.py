def count_change(amount, kinds_of_coins, index, choices):
    if amount == 0:
        print(choices)
        return 1
    elif amount < 0 or len(kinds_of_coins) < index + 1:
        return 0 
    else:
        choices.append(kinds_of_coins[index]) 
        count_choose = count_change(amount - kinds_of_coins[index], kinds_of_coins, index, choices)
        choices.pop()
        count_no_choose = count_change(amount, kinds_of_coins, index + 1, choices)
        return count_choose + count_no_choose


amount = 10 
kinds_of_coins = [1, 2, 5]
choices = []
ret = count_change(amount, kinds_of_coins, 0, choices)
print(ret)
