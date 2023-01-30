
## Для запуска контейнера:
1) скачать файы в целевую папку

2) запустить команду 
```console
user@station:~$ sudo bash dup.sh 
```
3) по итогу должна быть доступна ссылка на swagger, где можно протестировать (_обращаю внимание на ПОРТ 89_)

http://0.0.0.0:89/api/openapi

## Для удаления контейнера:
запустить команду 
```console
user@station:~$ sudo bash remove_compose_containers.sh
```


## Суть задачи:
Сделать сервис генерации короткой ссылки

## Детали:
На fastapi или aiohttp сделать API с 3 эндпоинтами:
    • Создание короткой ссылки (на вход передаём полный url, в ответ получаем короткий url)
    
    • Удаление ссылки (на вход ранее сгенерированный короткий url, ответ статус операции)
    
    • Получение полного url (на вход короткий url, в ответ полный url)
Пример полного url - https://music.yandex.ru/album/5307396/track/38633706 Пример короткого url - const.com/A8z1БД - PostgreSQL (желательно) или SQLite Код должна возможность запустить локально или в докере, как удобнее
Результат прислать публичной ссылкой на gitlab /GitHub.



