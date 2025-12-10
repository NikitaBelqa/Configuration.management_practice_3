# asm.py - ПРАВИЛЬНАЯ ВЕРСИЯ
import json

print("Ассемблер УВМ - Генерация тестовых байтов")

# Тестовые данные ИЗ СПЕЦИФИКАЦИИ
test_data = {
    45: [0xED, 0xF1, 0x00, 0x00, 0x64],  # LOAD_CONST 967 -> R25
    61: [0x3D, 0x60, 0x00, 0x00, 0x00],  # READ_MEM
    34: [0x62, 0x56, 0x07, 0x00, 0x00],  # WRITE_MEM
    5:  [0xC5, 0xC0, 0x00, 0x00, 0x00]   # SQRT
}

# Читаем программу
with open("program.json", "r") as f:
    program = json.load(f)

# Пишем бинарный файл
with open("program.bin", "wb") as f:
    for cmd in program:
        A = cmd["A"]
        
        if A in test_data:
            bytes_cmd = bytes(test_data[A])
            f.write(bytes_cmd)
            print(f"Команда {A}: {[hex(b) for b in bytes_cmd]}")
        else:
            print(f"⚠️ Неизвестная команда: {A}")

print(f"\n✅ Создан program.bin")