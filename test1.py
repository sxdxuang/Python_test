first_input = input("第一次输入").split(',')
second_input = input("第二次输入").split(',')

results = list(set(map(int,first_input+second_input)))
results.sort()

print(results)