# 🏛️ Сайт с достопримечательностями

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

Веб-приложение для просмотра, поиска и изучения достопримечательностей. Проект предоставляет удобный каталог интересных мест с подробными описаниями, фотографиями и возможностью фильтрации.

## ✨ Возможности

- 📸 **Каталог достопримечательностей** — просмотр всех доступных мест с превью.
- 🔍 **Поиск и фильтрация** — поиск по названию, фильтрация по городам или категориям.
- 📖 **Детальные страницы** — подробная информация, история места и галерея изображений.
- 🗺️ **Интерактивная карта** *(если есть)* — отображение мест на карте.
- 📱 **Адаптивный дизайн** — корректное отображение на мобильных устройствах, планшетах и ПК.
- 🛠️ **Админ-панель** — удобное управление контентом через стандартную Django Admin.

## 📸 Скриншоты

*(Здесь рекомендуется добавить 2-3 скриншота твоего сайта. Раскомментируй и вставь ссылки на изображения)*
<!-- 
| Главная страница | Страница достопримечательности |
|:---:|:---:|
| ![Главная](ссылка_на_картинку) | ![Детальная](ссылка_на_картинку) |
-->

## 🛠 Стек технологий

**Backend:**
* Python 3
* Django (Django ORM, Django Admin)

**Frontend:**
* HTML5 / CSS3
* JavaScript (Vanilla JS / jQuery / *(укажи, если использовал фреймворк)*)

**База данных:**
* SQLite *(или PostgreSQL/MySQL, если используешь другую)*

## 🚀 Установка и локальный запуск

Следуйте этим шагам, чтобы развернуть проект на вашем локальном компьютере:

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/b8rgv8zwc4-lang/my_project.git
   cd my_project
2. Создайте и активируйте виртуальное окружение:
   # Для Windows
   ```bash
   python -m venv venv
   venv\Scripts\activate

   # Для macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Примените миграции базы данных:
   ```bash
   python manage.py migrate

5. Создайте суперпользователя для доступа в админ-панель:
   ```bash
  python manage.py createsuperuser

7. Запустите сервер разработки:
   ```bash
   python manage.py runserver

9. Откройте браузер и перейдите по адресу:
  Сайт: http://127.0.0.1:8000/
  Админ-панель: http://127.0.0.1:8000/admin/



📝 Планы на будущее (Roadmap)
Добавить систему рейтингов и отзывов от пользователей.
Интеграция с API Яндекс.Карт / Google Maps.
Реализация API (Django REST Framework) для мобильного приложения.
Добавление маршрутов и построение пути между достопримечательностями.

🤝 Участие в проекте (Contributing)
Любые предложения по улучшению проекта приветствуются!
Если вы хотите внести свой вклад:
Форкните репозиторий.
Создайте ветку для своей фичи (git checkout -b feature/AmazingFeature).
Закоммитьте изменения (git commit -m 'Add some AmazingFeature').
Запушьте в ветку (git push origin feature/AmazingFeature).
Откройте Pull Request.

📄 Лицензия
Распространяется под лицензией MIT. См. LICENSE для подробной информации.
👤 Автор
[Evgeny Kavrus]
Telegram: @kavrusevgeny
Email: kavgenya@gmail.com
Если проект был полезен, не забудьте поставить ⭐ на GitHub!

   
