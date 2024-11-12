import os
import pandas as pd
from prettytable import PrettyTable


class PriceMachine:
    """
    Класс для анализа файлов содержаших наименование продуктов, их вес и их стоимсоть
    """
    
    def __init__(self):
        """
        Конструктор класса
        """
        self.data = []
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path='.'):
        """Выгрузка данных о стоимости, весе и цене продукта из файлов содержащих "price" формата ".csv".

        Функция проходится по всем файлам, которые содержаться по пути, указанному как обязательные аргумент.
        Выбираются файлы исходя из условия содержания в названии "price" и формат ".csv". Впроцессе обработки выдаются
        сообщения указывающие какие файлы обрабатываются и какие заголовки они имеют. После при помощи следующей функции
        по присвоенным номерам, нужным нам колонок в каждом файле данные записываются по ключу в словарь: имени - "name",
        цены - "price", веса - "weight", файла - "file", цена за кг. - "price_kg" (вычесляется по формуле деление цены на
        предлогаемый вес за эту цену, при условии, что вес не равен нулю, иначе ноль). Где df.iterrows() создает итератор,
        который возвращает пары индекс и данные строки. _ - проходимся по индексу строки, name - закрепелеят необходимые
        данные этой строки. В конце словарь сортируем по цене за кг. (условие задачи) и выводим число всех товаров во всех фалах.

        Args:
            file_path (str): Путь к файлам по которым должна проходить функция

        Returns:
            Количество товаров внутри отсортированного списска фсех имеющихся продуктов из файлов содержащих "price" формата ".csv"
        """
        for file in os.listdir(file_path):
            if 'price' in file and file.endswith('.csv'):
                print(f"Обрабатывается файл: {file}")
                df = pd.read_csv(file, sep=',', encoding='utf-8')
                print(f"Заголовки: {df.columns.tolist()}")
                name_id, price_id, weight_id = self._search_product_price_weight(df.columns)
                if name_id is not None and price_id is not None and weight_id is not None:
                    for _, number in df.iterrows():
                        self.data.append({
                            'name': number.iloc[name_id],
                            'price': number.iloc[price_id],
                            'weight': number.iloc[weight_id],
                            'file': file,
                            'price_kg': number.iloc[price_id] / number.iloc[weight_id] if number.iloc[weight_id] > 0 else 0
                        })
        self.data = sorted(self.data, key=lambda x: x['price_kg'])
        return f'Всего товаров: {len(self.data)}'
        
    def _search_product_price_weight(self, headers):
        """Определяет номера колонок.

        Функция проходится по всем колонкам файла, обнаруживая необходимое название записывается индекс этой колонки, унификация,
        для последующей работы, убирая из поля деятельности разные названия, к которым нельзя обращаться. Дает колонки с нужным
        названием номер по которому можно будет получить данный строки.

        Args:
            headers list: список заголовков

        Returns:
            Аргументы с индексами заголовка имени, цены, веса для конкретного файла
        """
        name_id = None
        price_id = None
        weight_id = None

        for i, header in enumerate(headers):
            if header.lower() in ['товар', 'название', 'наименование', 'продукт']:
                name_id = i
            elif header.lower() in ['цена', 'розница']:
                price_id = i
            elif header.lower() in ['вес', 'масса', 'фасовка']:
                weight_id = i

        return name_id, price_id, weight_id

    def export_to_html(self, fname='output.html'):
        """ Запись всех данных в Html файл.

        Запись строковых выражений в файл указанный как аргумент, посредством способов описанных ранее.

        Args:
            fname str: Имя файла в который будет происходить запись.

        Returns:
            Html файл с таблицей в который записаны все товары из словаря self.data, который формируется в функции load_prices.
        """
        self.result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''

        for i, number in enumerate(self.data):
            self.result += f'''
                        <tr>
                            <td>{i + 1}</td>
                            <td>{number["name"]}</td>
                            <td>{number["price"]:.2f}</td>
                            <td>{number["weight"]}</td>
                            <td>{number["file"]}</td>
                            <td>{number["price_kg"]:.2f}</td>
                        </tr>
                    '''
        self.result += '''
            </table>
        </body>
        </html>
        '''
        with open(fname, 'w', encoding='utf-8') as file:
            file.write(self.result)
        return fname

    def find_text(self, text):
        """ Поиск текста из словаря сформированного в функции load_prices.

        Ищет значение передаваемое в аргумент по всему словарю с данными по ноименованию продукта, перенося запись об этом
        продукте в словрь результатов

        Args:
            text str: значение которое функция будет искать в словаре

        Returns:
            словарь с подходящими записиями с соответсвующем именем продуктом, который был указан в качестве аргумента
        """
        results = []
        for i in self.data:
            if text.lower() in i['name'].lower():
                results.append(i)
        return results


def main():
    """ Основная функция запуска проекта.

    Обозначается объект класса. В консоль выводится принт результата функии load_prices. Далее реализуется цикл в процессе
    которого предлагается ввести текс для поиска внутри файлов price. Цикл не закнчивается пока пользовтель не введет в консоль
    exit. Формируется словарь который принимает в себя значения результаты метода класса find_text, если запрашиваемый тоавр
    был найден, формируется таблица, благодаря библиотеке prettytable, котрая выводится в консоль, если нет, то выдается
    сообщение "Товары не найдены." После ввода exit выводится сообщение о завершении анализа, и выводится файл Html в который
    были записаны все результаты.

    Returns:
        Таблицу с нужными товарами в консоль и записанный файл Html со списком всех товаров.
    """
    pm = PriceMachine()
    print(pm.load_prices())
    while True:
        text = input("Введите текст для поиска (или 'exit' для выхода): ")
        if text.lower() == 'exit':
            break

        results = pm.find_text(text)
        if results:
            table = PrettyTable()
            table.field_names = ["Номер", "Название", "Цена", "Фасовка", "Файл", "Цена за кг."]
            for i, number in enumerate(results):
                table.add_row([f"{i + 1}", f"{number['name']}", f"{number['price']:.2f}", f"{number['weight']}", f"{number['file']}", f"{number['price_kg']:.2f} за кг."])
            print(table)
        else:
            print("Товары не найдены.")
    print('the end')
    print(pm.export_to_html())


if __name__ == '__main__':
    main()
