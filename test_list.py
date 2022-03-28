a = ["a.txt", "b.txt"]
i = 0
file_data = []
file_name = []
for file in a:

    with open(file, "rb") as f:
        file_data.append("1")
        # file_name[i] = 2
    print(file_data[i])
    i = i + 1


print(file_data[0])
