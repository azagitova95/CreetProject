# CreetProject
### Суть проекта:

Легкий доступ к Интернету радикально изменил то, как люди сегодня покупают почти все. От мобильных телефонов до стоматологических услуг — редко кто слепо принимает решение о покупке, не прочитав несколько обзоров в Интернете. Согласно исследованиям (https://www.oberlo.com/blog/online-review-statistics) 89% покупателей читают отзывы перед покупкой, поэтому игнорировать обратную связь от клиентов не стоит. Отзывы клиентов — это мощный инструмент, который может дать важную информацию о каждой части компании, помогая зарабатывать больше денег или сокращать расходы на маркетинг. 

Поэтому в качестве пректной работы было принято решение реализовать приложение для отзывов для условной стоматологической клиники. Клиент после посещения стоматологии может оставить на сайте обратную связь о своем опыте: понравилось\не понравилось обслуживание, какие плюсы и минусы для себя выявил. Эти данные записываются в базу данных и в дальнейшем на основе анализа собранных отзывов можно выявить недостатки, улучшить сервис и привлечь больше клиентов.

### Использованные технологии:
- Веб-приложение написано на Python3 (для корректной работы приложения требуется версия не ниже 3.6.9)
- В качестве фреймворка был использован Flask
- Для хранения данных использована база данных SQLite

### Структура пректа:
- в папке static находятся css-файлы и изображения, используемые на фронтенде
- в папке templates лежат html файлы
- в файле requirements.txt описаны требуемые библиотеки с версиями
- в файле app.py описана основная логика приложения
- в файле makedb.py описана код для создания таблицы в базе данных

### Для сборки и запуска приложения необходимо:
1. Проверить версию Python (!!! чтобы избежать конфликта библиотек требуется версия 3.6.9 и выше) 
2. Создать папку <мой_проект>, где будет лежать проект с исходным кодом 
3. Склонировать проект на локальнкю машину (код на ветке master):
   - если есть установленный git, то можно:
      - открыть командную строку
      - перейти в папку cd C:\\путь_до_папки\<мой_проект>
      - выполнить git clone https://github.com/azagitova95/CreetProject.git
      - выполнить git checkout master
   - если git не установлен, то можно скачать архив перейдя в Clone -> Download zip
      - разархивировать папку в директорию <мой_проект>
      - открыть командную строку
      - перейти в папку cd C:\\путь_до_папки\<мой_проект>
3. Установить виртуальное окружение
```shell
pip install virtualenv
virtualenv --python C:\\path_to_python\python.exe venv
```
4. Активировать виртуально окружение
```shell
.\venv\Scripts\activate
```
5. Установить библиотеки, требуемые для работы приложения
```shell
pip install -r requirements.txt
```
6. Запустить приложение
```shell
python app.py
```
7. Открыть в браузере http://127.0.0.1:5000/
8. Для того, чтобы посмотреть зписи в базе данных:
   - установить dbeaver или любой другой инструмент для работы с базами данных
   - перейти в Базы Данных -> Новое подключение
   - из списка баз выбрать SQLite
   - указать путь до папки, куда был склонирован исходный код <мой_проект>\feedback.db
   - подключиться Test Connection
