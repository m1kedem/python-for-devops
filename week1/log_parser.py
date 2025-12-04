import re
import psutil  # pip install psutil

def parse_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            logs = f.readlines()
    except FileNotFoundError:
        print("Файл example.log не найден! Создаю тестовый...")
        example_logs = [
            "2025-12-04 10:00:01 INFO  Всё ок\n",
            "2025-12-04 10:05:12 ERROR  Диск переполнен\n",
            "2025-12-04 10:10:33 WARNING  Память на исходе\n",
            "2025-12-04 10:15:44 ERROR  Соединение разорвано\n",
        ]
        with open("example.log", "w", encoding='utf-8') as f:
            f.writelines(example_logs)
        logs = example_logs

    errors = [line.strip() for line in logs if re.search(r'ERROR', line, re.IGNORECASE)]
    print(f"Найдено ошибок: {len(errors)}")
    for err in errors:
        print("   →", err)

    print(f"\nТекущая загрузка системы:")
    print(f"   CPU: {psutil.cpu_percent(interval=1)}%")
    print(f"   RAM: {psutil.virtual_memory().percent}%")

if __name__ == "__main__":
    parse_log("example.log")