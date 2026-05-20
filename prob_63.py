from helpers import get_num_digits

print([f"{j}^{i} =     {j**i}" for i in range(22) for j in range(10) if get_num_digits(j**i) == i])

# some experimentation showed that 9**21 (21 digits) is the last one
