# 🌦️ Python Weather App

A simple **Dockerized Python Weather Application** that fetches real-time weather information for any city using the OpenWeather API.

---

## 📌 Features

* 🌍 Search weather by city name
* 🌡️ Display current temperature
* ☁️ Show weather condition
* 💧 Display humidity
* 💨 Show wind speed
* 🐳 Dockerized for easy deployment

---

## 🛠️ Technologies Used

* Python 3.12
* Docker
* Requests
* Python Dotenv
* OpenWeather API

---

## 📁 Project Structure

```text
python-weather-app/
│── app.py
│── Dockerfile
│── requirements.txt
│── .env
│── README.md
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/YourUsername/python-weather-app.git
cd python-weather-app
```

---

## 🔑 API Key Setup

1. Create a free account on **OpenWeather**.
2. Generate your API key.
3. Create a `.env` file in the project root.

Example:

```text
API_KEY=YOUR_API_KEY
```

---

## 🐳 Build Docker Image

```bash
docker build -t python-weather-app .
```

---

## ▶️ Run the Docker Container

```bash
docker run -it --env-file .env python-weather-app
```

---

## 💻 Example Output

```text
Enter city name: Mumbai

========== Weather Report ==========
City        : Mumbai
Country     : IN
Temperature : 29.7 °C
Feels Like  : 33.1 °C
Humidity    : 74 %
Weather     : Clear Sky
Wind Speed  : 3.6 m/s
====================================
```

---

## 📚 Dependencies

Install locally using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Mustafa Shikalgar**

GitHub: https://github.com/Mustafa-shikalgar
