# run.py - АВТОЗАПУСК УЧЕБНОЙ ВИРТУАЛЬНОЙ МАШИНЫ
import os
import time

def print_header(text):
    print("=" * 60)
    print(f"🚀 {text}")
    print("=" * 60)

def main():
    print_header("АВТОЗАПУСК УВМ (Вариант 6)")
    
    # 1. Проверяем наличие файлов
    print("\n📁 ПРОВЕРКА ФАЙЛОВ:")
    
    required_files = ["program.json", "asm.py", "interp.py"]
    all_ok = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - НЕ НАЙДЕН")
            all_ok = False
    
    if not all_ok:
        print("\n❌ ОШИБКА: Не все файлы найдены!")
        return
    
    # 2. Запускаем ассемблер
    print("\n1. 🛠  ЗАПУСК АССЕМБЛЕРА...")
    print("   Команда: python asm.py")
    
    start_time = time.time()
    exit_code = os.system("python asm.py")
    asm_time = time.time() - start_time
    
    if exit_code != 0:
        print("❌ ОШИБКА при компиляции!")
        return
    
    # 3. Проверяем результат компиляции
    if not os.path.exists("program.bin"):
        print("❌ ОШИБКА: program.bin не создан!")
        return
    
    file_size = os.path.getsize("program.bin")
    print(f"   ✅ Создан program.bin ({file_size} байт, {asm_time:.2f} сек)")
    
    # 4. Запускаем интерпретатор
    print("\n2. 🚀 ЗАПУСК ИНТЕРПРЕТАТОРА...")
    print("   Команда: python interp.py")
    
    start_time = time.time()
    exit_code = os.system("python interp.py")
    interp_time = time.time() - start_time
    
    if exit_code != 0:
        print("❌ ОШИБКА при выполнении!")
        return
    
    # 5. Проверяем результат
    print("\n3. 📊 РЕЗУЛЬТАТ:")
    
    if os.path.exists("result.xml"):
        file_size = os.path.getsize("result.xml")
        
        # Читаем и показываем содержимое
        with open("result.xml", "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
        
        # Подсчитываем ячейки
        lines = [line for line in content.split('\n') if 'cell address' in line]
        
        if lines:
            print(f"\n✅ УСПЕХ! Записано {len(lines)} ячеек памяти")
            print(f"   Время выполнения: {interp_time:.2f} сек")
            
            # Показываем адреса
            print("   Адреса:")
            for line in lines:
                # Извлекаем адрес из XML
                import re
                match = re.search(r'address="(\d+)"', line)
                if match:
                    print(f"     • {match.group(1)}")
        else:
            print("\n⚠️  Память пустая (программа ничего не записала)")
    else:
        print("❌ ОШИБКА: result.xml не создан!")
    
    # 6. Итог
    print("\n" + "=" * 60)
    print("📈 СТАТИСТИКА:")
    print(f"   • Время компиляции: {asm_time:.2f} сек")
    print(f"   • Время выполнения: {interp_time:.2f} сек")
    print(f"   • Общее время: {asm_time + interp_time:.2f} сек")
    print(f"   • Размер программы: {file_size} байт")
    print("=" * 60)
    print("🏁 ВЫПОЛНЕНИЕ ЗАВЕРШЕНО!")
    print("=" * 60)

if __name__ == "__main__":
    main()