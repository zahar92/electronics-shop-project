import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total = None

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity}"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            summ = self.quantity + other.quantity
            return summ
        else:
            raise Exception("Неверный объект")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            print("Длина наименования товара больше 10 символов")
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        cls.all.clear()
        try:
            with open(path, encoding="CP1251", newline='') as f:
                csv_file = csv.DictReader(f)
                for row in csv_file:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(str_num):
        try:
            return int(float(str_num))
        except ValueError:
            return 'Введено некорректное значение'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total = self.price * self.quantity
        return self.total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
