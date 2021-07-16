# names_path = r"D:/專題/data/hw03/charater_names.txt"

# with open(names_path, "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     names = tuple([line[:-1] for line in lines])

# print(names)
# given = input("Enter name: ")
# print(given in names)


names = ["andy", "bob", "cindy", "ken"]
print(names)

with open(r"D:/專題/data/hw03/test_output.txt", "w", encoding="utf-8") as file:
    file.write(names)
