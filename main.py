import json
import settings
import random

settings.tests_enabled

register = [0] * 64
memory = [0] * 1024


comands = {45: lambda num, ind: register.__setitem__(ind, num),
           61: lambda target_ind, source: register.__setitem__(source, memory[register[target_ind]]),
           34: lambda reg_ind, mem_ind: memory.__setitem__(mem_ind, register[reg_ind]),
           5: lambda reg_ind, target_reg_ind: memory.__setitem__(register[target_reg_ind], int(memory[register[reg_ind]] ** 1/2))}

json_comands = list(comands.keys())
with open("comands.json", "w") as file:
    json.dump(json_comands, file, ensure_ascii=False)

while True:
    if settings.tests_enabled:
        cmd = input("Num of tests: ")
        for test in range(int(cmd)):
            a, b, c = random.choice(json_comands), random.randint(0, 63), random.randint(0, 63)
            comands[a](b, c)
            print(a, b, c)
        print("register =", register)
        print("memory =", memory)
        if cmd == "exit":
            break
    else: 
        cmd = input()
        if cmd == "exit":
            break
        if cmd == "mem":
            print("register =", register)
            print("memory =", memory)
        else:
            a, b, c = map(int, cmd.split(" "))
            comands[a](b, c)
    