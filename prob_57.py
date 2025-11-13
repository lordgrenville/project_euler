def conversion(num: int, denom: int) -> (int, int):
    # since we added 1 before the final step, we remove the denominator from the numerator
    old_input_num = num - denom
    new_input_num = old_input_num + 2 * denom  # now we're adding 2
    # swap the order since we're dividing one by the fraction
    new_input_num, new_input_denom = denom, new_input_num
    new_input_num = new_input_num + new_input_denom # add one
    return new_input_num, new_input_denom


NUM_LONGER_THAN_DENOM = 0
num, denom = 3, 2
for i in range(2, 1001):
    num, denom = conversion(num, denom)
    # print(f"Iteration {i}: {num} / {denom}")
    if len(str(num)) > len(str(denom)):
        # print(f"Example found at iteration {i}: {num} / {denom}")
        NUM_LONGER_THAN_DENOM += 1
print(NUM_LONGER_THAN_DENOM)
