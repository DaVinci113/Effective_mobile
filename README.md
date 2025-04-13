УСТАНОВКА ПРОЕКТА

Переходим в папку нашего пользователя (если ее нет, то создать):
cd /home/<user_name>/

Устанавливаем пакетный менеджер uv: 
wget -qO- https://astral.sh/uv/install.sh | sh

Клонируем репозиторий с проектом: git clone https://github.com/DaVinci113/Effective_mobile

Переходим в папку с проектом: cd Effective_mobile/Effect_mob 

Запуск миграций: uv run manage.py migrate

Запуск сервера: uv run manage.py server

ГЛАВНАЯ СТРАНИЦА - http://127.0.0.1:8000/ads

Запуск тестов: ur run manage.py test

