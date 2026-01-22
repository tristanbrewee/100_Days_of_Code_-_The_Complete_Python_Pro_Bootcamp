import random
# import my_module

random_integer = random.randint(1, 10)
print(random_integer)
# if random_integer > my_module.my_favorite_number:
#     print(f"{random_integer} > {my_mod

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(0, 9)
print(random_float)

print("-----")

choice = random.random() * 2
if choice >= 1:
    print("HEADS")
else:
    print("TAILS")