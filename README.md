# FastAPIProject
test task

  


<details>
<summary>
  
# Задачи

</summary>

1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.


2. Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.

4. Желательно, если при выполнении задания вы будете использовать docker-compose, SqlAalchemy,  пользоваться аннотацией типов.

</details>

**Описание проекта**

<details>
  <summary>

  # Локальный запуск

  </summary>

  1. Клонирование репозитория

`https://github.com/OksanaZakharovaIP-31/FastAPIProject.git`

2. Установка виртуального окружения и его активация

`python -m venv venv`

`venv\Scripts\activate.bat` - Windows

`source venv/bin/activate` - Linux and MacOS

3. Установка зависимостей

`pip install -r requirements.txt`

4. База данных - PostgreSQL
5. Создать БД
6. Все ключи, пароли храняться в файле .env (создать в папке проекта) (заполнить для себя)

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASS=
```
6. Запуск миграций

```
cd src
alembic upgrate caf269a259ee
```
7. Запуск проекта

```
cd src
uvicorn main:app --reload
```
Прейти по [ссылке](http://127.0.0.1:8000/docs)
</details>

<details>
  <summary>
    
# Docker 
  </summary>

  ***Создание нового файла***
  1. Создать файл `.env-non-dev`
  2. Запольнить файл
```
DB_HOST=db
DB_PORT=5435
DB_NAME=
DB_USER=
DB_PASS=
```

  ***Запуск докера**
  
  ```
  docker build . -t <name>
docker run -d -p <your_port>:8000 <name>
```

***Запуск docker-compose***

```
docker compose build
docker compose up
```
Перейти по [ссылке](http://127.0.0.1:8000/docs)
</details>
