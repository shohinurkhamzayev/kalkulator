# main.py
print("Добро пожаловать в калькулятор!")
def add(a, b):
    return a + b
def subtract(a, b):   # <-- Новая функция
    return a - b
if __name__ == "__main__":
    print(f"2 + 2 = {add(2, 2)}")
    print(f"10 - 3 = {subtract(10, 3)}") # <-- Новая строка

