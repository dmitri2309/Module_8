class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.vin = vin
        self.numbers = numbers

    def is_valid_vin(self):
        if not isinstance(self.vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if not 1000000 <= self.vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def is_valid_numbers(self):
        if not isinstance(self.numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not len(self.numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
    first.is_valid_vin()
    first.is_valid_numbers()
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
    second.is_valid_vin()
    second.is_valid_numbers()
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
    third.is_valid_vin()
    third.is_valid_numbers()
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
