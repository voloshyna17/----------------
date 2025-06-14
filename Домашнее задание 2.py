import random
def get_numbers_ticket(min_num,max_num,quantity):
    if(
        not isinstance(min_num, int) or
        not isinstance(max_num, int) or
        not isinstance (quantity,int) or
        min_num <1 or
        max_num > 1000 or
        quantity > (max_num-min_num + 1)
    ):
        return[]

#генерация чисел
    numbers = random.sample(range(min_num, max_num + 1 ), quantity)
    numbers.sort()
    return numbers

print(get_numbers_ticket(1,49,6))