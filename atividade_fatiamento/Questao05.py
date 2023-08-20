zero_um = ""
num_um = 0
for i in range(5):
    um = input("Digite apenas 0 ou 1: ")
    zero_um += um
for i in zero_um:
    if i == "1":
        num_um += 1
print(zero_um, " -->", num_um)