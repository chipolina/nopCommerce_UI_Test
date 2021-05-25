Примеры нескольких тестов для сайта [nopCommerce](https://admin-demo.nopcommerce.com/login "nopCommerce")


Небольшой фреймворк использует [PyTest](https://docs.pytest.org/en/6.2.x/ "PyTest"),    [Selenium WD](https://www.selenium.dev/, "Selenium WD")   , [Allure](https://docs.qameta.io/allure/ "Allure"), Page Object Model и так же [Google](https://www.google.com/ "Google")

Запуск тестов происходит командой в PyCharm или любой другой IDE:
pytest -v -s alluredir=Reports --browser=chrome|opera|firefox -m smoke|regullar(опционально)

Формирование Allure отчета:
allure serve Reports

Так как это мой первый учебный проект - старался показать мои знания и подход к оформлению и проектированию тестов. Писать сотню раз то как запускается драйвер мало кому будет интересно, поэтому ограничился стандартными проверками, использованием паттерна POM, формированием отчетов с помощью Allure, использование различных методов самого Python.

Готов слушать конструктивную критику, идеи и возможно совместную работу 
