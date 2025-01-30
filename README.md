# ✅ TaskManager (Django + Docker + PostgreSQL)

**TaskManager** — это веб-приложение для управления задачами. Позволяет создавать, редактировать, удалять и просматривать задачи. Также реализована фильтрация задач.

## 🚀 Функционал  

✅ **Создание задач** — удобная форма для добавления новых задач  
✅ **Просмотр задач** — список всех задач с детальной страницей  
✅ **Редактирование задач** — возможность изменять данные о задаче  
✅ **Удаление задач** — кнопка для удаления без лишних действий  
✅ **Фильтрация задач** — поиск и фильтрация по параметрам  

## 📦 Технологии  

- **Django** — веб-фреймворк Python  
- **PostgreSQL** — база данных  
- **Django ORM** — управление данными  
- **Docker & Docker Compose** — контейнеризация  
- **Django Filters** — фильтрация задач  

## 🛠 Установка и запуск  

### 1️⃣ Клонируйте репозиторий  


```bash
git clone https://github.com/Shoma0XCC/taskmanager.git
cd taskmanager
```

### 2️⃣ Установите Docker Desktop

### 🔗 Скачать Docker Desktop:


```
https://www.docker.com/products/docker-desktop/
```


## 🏗 Setup

### 3️⃣ Создайте виртуальное окружение

🖥️ macOS / Linux

```
python3 -m venv venv
source venv/bin/activate
```

🖥️ Windows

```
python3 -m venv venv
.\venv\Scripts\activate.bat
```

### 4️⃣ Установите зависимости

```
pip install --upgrade pip
pip install -r requirements.txt
```

### 5️⃣ Сделайте миграцию базы данных и создайте администратора

```
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Соберите Docker-контейнеры

```
docker compose build
```

### 7️⃣ Запустите проект в Docker в фоновом режиме

```
docker compose up -d
```


## 📝 **Использование**

### После установки можно:

- Создавать задачи через веб-интерфейс
- Просматривать детали задач на отдельной странице
- Редактировать задачи в удобной форме
- Удалять задачи одним кликом
- Фильтровать задачи по параметрам
  
## 🔗 **Доступ к проекту:**

Главная страница: http://localhost:8000

Админ-панель: http://localhost:8000/admin/

## 📝 **Разработчик**
👤 Shoma0XCC

🔗 GitHub: [Shoma0XCC](https://github.com/Shoma0XCC)
