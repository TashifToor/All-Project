# Weatherable 🌦️

Weatherable is a simple and responsive weather web app that displays real-time weather data for any city using a weather API (e.g., OpenWeatherMap).

This project is optimized to **reduce API usage costs** by implementing caching, optimized requests, and free-tier-friendly techniques.

---

## 🚀 Features
- Search for weather by city name
- Real-time temperature, weather condition, and humidity
- Caches results locally to reduce repeated API calls
- Uses free tier API effectively
- Fully responsive design (HTML, CSS, JavaScript)

---

## 💡 How API Cost is Reduced
1. **Local Caching**  
   Stores weather data in the browser's `localStorage` for 10 minutes to avoid repeated API calls for the same city.

2. **On-Demand Requests Only**  
   API is called only when the user clicks "Search" or presses Enter, not on every keystroke.

3. **Minimal Data Request**  
   Uses API parameters to fetch only the necessary fields (temperature, humidity, weather condition) to reduce data size.

4. **Free API Usage**  
   Works with OpenWeatherMap free tier (1,000 requests/day) or completely free alternatives like Open-Meteo.

---

## 🛠️ Technologies Used
- HTML
- CSS
- JavaScript
- Weather API (OpenWeatherMap / Open-Meteo)

---

## 📦
