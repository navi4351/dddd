from enum import Enum
import random

# Перечисление для единиц измерения
class TemperatureUnit(Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"
    KELVIN = "K"

# Список городов Хакасии
CITIES = ["Абакан", "Сорск", "Усть-Абакан", "Таштып", "Боград", "Копьёво", "Абаза", "Черногорск"]

# Генерация случайной температуры для городов
city_temperatures = {city: round(random.uniform(-30, 40), 1) for city in CITIES}

# Функции преобразования температур
def celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 1)

def celsius_to_kelvin(celsius):
    return round(celsius + 273.15, 1)

# Функция получения погоды в трех единицах измерения
def get_weather(city):
    if city not in city_temperatures:
        return f"Город {city} не найден."
    celsius = city_temperatures[city]
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return [f"{celsius}°{TemperatureUnit.CELSIUS.value}", 
            f"{fahrenheit}°{TemperatureUnit.FAHRENHEIT.value}", 
            f"{kelvin}°{TemperatureUnit.KELVIN.value}"]

# Фильтрация городов по температуре
def filter_cities_by_sign(sign):
    if sign == "+":
        return list(filter(lambda x: x[1] > 0, city_temperatures.items()))
    elif sign == "-":
        return list(filter(lambda x: x[1] <= 0, city_temperatures.items()))
    else:
        return "Некорректный символ фильтрации."

# Сортировка городов по температуре
def sort_cities(order="asc"):
    return sorted(city_temperatures.items(), key=lambda x: x[1], reverse=(order == "desc"))

# Тестирование в консоли
if __name__ == "__main__":
    # Погода в заданном городе
    city = "Абакан"
    print(f"Погода в городе {city}: {get_weather(city)}")

    # Фильтрация городов
    print("Города с положительной температурой:")
    print(filter_cities_by_sign("+"))

    print("Города с отрицательной температурой:")
    print(filter_cities_by_sign("-"))

    # Сортировка
    print("Города, отсортированные по температуре (возрастание):")
    print(sort_cities(order="asc"))

    print("Города, отсортированные по температуре (убывание):")
    print(sort_cities(order="desc"))