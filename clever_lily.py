age = int(input())
washing_machine_price = float(input())
R = int(input())
toys = 0
money = 0
money_gifted = 10
brother = 0

for i in range(1, age + 1):
    if i % 2 == 1:
        toys += 1
    elif i % 2 == 0:
        money += money_gifted
        money_gifted += 10
        brother += 1

toys_sell = toys * R
total_money = (money - brother) + toys_sell

if total_money >= washing_machine_price:
    N = total_money - washing_machine_price
    print(f"Yes! {N:.2f}")
else:
    M = washing_machine_price - total_money
    print(f"No! {M:.2f}")
