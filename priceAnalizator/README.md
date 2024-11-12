# Анализатор прайс-листов
Анализирует файлы формата .csv, после чего выдает таблицу запрашиваемых продуктов. Таблица состоит из наименования продукта, их веса и их стоимсоть. Так же Анализатор осуществляет запись всех товаров и их характеристик в HTML файл. Все сортируется по цене за киллограм.

## Содержание
- [Библиотеки и модули](#библиотеки и модули)
- [Использование](#использование)
- [Разработка](#разработка)

## Библиотеки и модули
- [os](https://docs.python.org/3/library/os.html)
- [pandas](https://pandas.pydata.org/docs/)
- [prettytable](https://pypi.org/project/prettytable/)

## Использование
1. Запустите программу через функцию main();
2. Следуйте указаниям в консоли;
3. Получите в результате таблицу с нужным вам товаром в консоли, и файл HTML со всеми товарми, отсортированными по цене за кг.

Пример вывода консоли:
![Иллюстрация консоли](https://github.com/iDivey/Diplom/blob/main/priceAnalizator/ZgZMEN-lHZk.jpg)

Пример HTML файла:
![Иллюстрация файла](https://github.com/iDivey/Diplom/blob/main/priceAnalizator/8BuT5Ux4iWg.jpg)

## Разработка
Выполнено задание в рамках аттестационной работы UrbanUniversity:
Реализован  класс для анализа файлов содержаших наименование продуктов, их вес и их стоимсоть. Благодаря трем методам класса:
load_prices - сканирует папку и загружает данные;
_search_product_price_weight - присваивает колонкам данных индекс;
export_to_html - выгружает все данные в html файл;
find_text - получает текст и возвращает список позиций, содержащий этот текст в названии продукта;
main - предоставляет интерфейс для поиска товара по фрагменту названия с сорторовкой по цене за килогорамм.
Интерфейс для поиска реализован через консоль, циклически получает информацию от пользователя.
Если введено слово "exit", то цикл обмена с пользователем завершается, программа выводит сообщение о том, что работа закончена и завершает свою работу. В противном случае введенный текст считается текстом для поиска. Программа выводит список найденных позиций в виде таблицы.