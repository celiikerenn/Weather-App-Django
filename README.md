# 🌦 Weather App (Django)

A simple weather app built with Django where users can:

- Add and save city names 🏙️
- View current temperature and weather description 🌡️
- Toggle between light and dark themes 🌗
- Delete individual cities or all at once 🗑️
- Securely store your API key using `.env` 🔐
- Display weather icons next to each city (e.g., sunny, cloudy, rainy) 🖼️
---

## 🖼️ Weather Icons Feature

Each city now displays a relevant weather icon (fetched from OpenWeatherMap or mapped locally), enhancing the UI.

---

## 🚀 Features

- Real-time weather data via [OpenWeatherMap API](https://openweathermap.org/api)
- City storage in SQLite database
- Theme switch (dark/light)
- Weather list with delete options
- API key hidden using `.env` and `python-dotenv`

---

## ⚙️ Tech Stack

- Python 3.12
- Django 5.2
- SQLite (default DB)
- HTML + CSS (vanilla)
- OpenWeatherMap API
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

📁 Folder Structure (relevant parts)

weather_app/
├── static/
│   └── icons/          # Weather icons stored here (optional)
├── templates/
│   └── weather/
│       └── home.html
├── .env
├── requirements.txt
├── manage.py

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/celiikerenn/Weather-App-Django.git
cd Weather-App-Django
```

### 2. Create a virtual environment and activate it
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file and add your API key
```bash
API_KEY=your_openweathermap_api_key_here
```

### 5.Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the app
```bash
python manage.py runserver
```

### Then go to:
```bash
http://127.0.0.1:8000
```
