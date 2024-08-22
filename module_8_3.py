class IncorrectVinNumber(Exception):
    def __init__(self, messange):
        self.messange = messange

class IncorrectCarNumbers(Exception):
    def __init__(self, messange):
        self.messange = messange

class Car():
    def __init__(self, model, __vin, numbers):
        self.model = model
        self.__vin = __vin
        self.numbers = numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(numbers)


    def __is_valid_vin(seif, vin_number):
        if isinstance(vin_number, int):
            if (vin_number >= 1000000) and (vin_number) <= 9999999:
                return True
            else:
                raise IncorrectVinNumber(f'Некорректный тип vin номера')
        else:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers(f'Неверная длина номера')
        else:
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.messange)
except IncorrectCarNumbers as exc:
    print(exc.messange)
else:
   print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.messange)
except IncorrectCarNumbers as exc:
  print(exc.messange)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.messange)
except IncorrectCarNumbers as exc:
  print(exc.messange)
else:
  print(f'{third.model} успешно создан')

