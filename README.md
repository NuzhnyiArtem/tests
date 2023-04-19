# Тестовое задание

### Установка
В виртуальном окружении

1. `git clone https://github.com/NuzhnyiArtem/tests`
2. `cd tests\Flashlight`
3. `pip install -r requirements.txt`


### Запуск сервера
`python server.py`
#### Запуск сервера на aiohttp
`server_aiohttp.py`

### Запуск клиента
`python Flashlight.py`
#### Запуск клиента для сервера на aiohttp
``client_for_aiohttp_server.py`

### Подаются команды вида

`{"command": "on"}`
`{"command":"color", "metadata": 2}`
