def restake(money, apr, hyper_param_day, cost):
    return money + money * apr / 365 * hyper_param_day - cost


how_many_money_your_farm = float(input("how_many_money_are_your_farming?: "))
APR = float(input("please input APR: "))
result = []
for hyper_param_day in range(1, 100):
    money = how_many_money_your_farm
    for _ in range(int(100 / hyper_param_day)):
        money = restake(money, APR, hyper_param_day, 1)
    result.append({"hyper_param_day": hyper_param_day, "money": money})
print(
    "hyper_param_day is the day that you should restake to optimize your yield!",
    sorted(result, key=lambda x: -x["money"])[:10],
)
