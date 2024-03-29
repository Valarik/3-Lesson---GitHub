# Обрезка ссылок с помощью Битли

Модуль предназначен для сокращения ссылок с помощью API сервиса [Bitly](bitly.com) и подсчета кликов по этим ссылкам.

### Как установить

Для начала работы с кодом требуется индивидуальный токен. Получить его можно на [странице для разработчиков](https://dev.bitly.com) по ссылке [access token](https://app.bitly.com/settings/api/). **Необходима _регистрация_ на сайте**.

После генерации токена его необходимо положить в файл с названием **.env** (_не требуется писать какое бы то ни было название до точки_). Если этого файла нет - его нужно создать.
Пример заполнения файла ниже:

```
BITLY_API_TOKEN='122333444455555666666777777788888888999999999'
```

***Обратите внимание***: не надо ставить пробел перед и после =, а также нужно заключить токен в ' ' или " ".

Python3 должен быть уже установлен. 
Затем, используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Как запустить

Для запуска программы следует ввести в терминале:

```
python main.py -url ВАША_ССЫЛКА
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

### Ссылки
* Документация Bitly: https://dev.bitly.com/api-reference/
* Документация библиотеки os (en): https://docs.python.org/3/library/os.html
* Документация библиотеки os (ru): https://all-python.ru/osnovy/os.html
