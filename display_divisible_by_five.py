#Display numbers divisible by 5
sample_list = [10, 20, 33, 46, 55]

print(f"Given list: {sample_list}")

print(f"Divisible by 5 list:")
for num in sample_list:
    if num % 5 == 0:
        print(num)
