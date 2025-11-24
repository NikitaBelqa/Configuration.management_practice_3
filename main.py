register = [0] * 64
memory = [0] * 1024


comands = {"45": lambda num, ind: register.__setitem__(ind, num),
           "61": lambda target_ind, source: register.__setitem__(source, memory[register[target_ind]]),
           "34": lambda reg_ind, mem_ind: memory.__setitem__(mem_ind, register[reg_ind]),
           "5": lambda reg_ind, target_reg_ind: memory.__setitem__(register[target_reg_ind], (memory[register[reg_ind]] ** 1/2))}


while True:
    cmd = input()
    if cmd == "exit":
        break
    if cmd == "mem":
        print("register =", register)
        print("memory =", memory)
    else:
        a, b, c = cmd.split(" ")
        comands[a](int(b), int(c))
    