import os
import pandas as pd
from prettytable import PrettyTable


class PriceMachine:
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path='.'):
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

    def find_text(self, text):
        results = []
        for i in self.data:
            if text.lower() in i['name'].lower():
                results.append(i)
        results_sort = sorted(results, key=lambda x: x['price_kg'])
        return results_sort


def main():
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
