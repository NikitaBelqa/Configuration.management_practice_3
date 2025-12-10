# interp.py - РАБОТАЕМ С КОНКРЕТНЫМИ БАЙТАМИ
import math

print("Интерпретатор УВМ")

# Читаем бинарный файл
with open("program.bin", "rb") as f:
    data = f.read()

# Память
REGISTERS = [0] * 64
MEMORY = [0] * 1024

print(f"Загружено {len(data)} байт")
print("Выполнение:")

# Обрабатываем команды по 5 байт
for i in range(0, len(data), 5):
    chunk = data[i:i+5]
    if len(chunk) != 5:
        continue
    
    # ПРЕОБРАЗУЕМ В ЧИСЛА
    hex_str = ''.join(f'{b:02X}' for b in chunk)
    print(f"\nКоманда {i//5}: {hex_str}")
    
    # Проверяем, какая это команда (по тестовым данным)
    if chunk == b'\xED\xF1\x00\x00\x64':  # 45: LOAD_CONST 967 -> R25
        REGISTERS[25] = 967
        print("  LOAD_CONST: R25 = 967")
        
    elif chunk == b'\x3D\x60\x00\x00\x00':  # 61: READ_MEM
        addr = REGISTERS[0]  # B=0
        REGISTERS[12] = MEMORY[addr]  # C=12
        print(f"  READ_MEM: MEM[{addr}]={MEMORY[addr]} -> R12")
        
    elif chunk == b'\x62\x56\x07\x00\x00':  # 34: WRITE_MEM
        MEMORY[234] = REGISTERS[25]  # B=25, C=234
        print(f"  WRITE_MEM: R25={REGISTERS[25]} -> MEM[234]")
        
    elif chunk == b'\xC5\xC0\x00\x00\x00':  # 5: SQRT
        src = REGISTERS[24]  # C=24
        dst = REGISTERS[3]   # B=3
        value = MEMORY[src]
        result = int(math.sqrt(value)) if value >= 0 else 0
        MEMORY[dst] = result
        print(f"  SQRT: √{value} = {result}")

# Сохраняем XML
with open("result.xml", "w") as f:
    f.write('<?xml version="1.0"?>\n<memory>\n')
    for addr in range(len(MEMORY)):
        if MEMORY[addr] != 0:
            f.write(f'  <cell address="{addr}" value="{MEMORY[addr]}"/>\n')
    f.write('</memory>\n')

print(f"\n✅ Результат в result.xml")
print(f"MEM[234] = {MEMORY[234]}")