# 🚨 Real-Time Emergency Response Dashboard

### 🌎 Stay Alert, Stay Safe!

![Image](https://github.com/user-attachments/assets/25967eab-ae71-4f6c-9d62-ea0cee80a388)

![Image](https://github.com/user-attachments/assets/b1eff4c6-8e7b-4d61-83ff-4568b18f2fc7)

![Image](https://github.com/user-attachments/assets/d05822f3-dcef-4ced-9de7-3f607344952d)

### 🚀 Live Deployment: [Click Here](https://systemdesignavailability-c77vz8fscjczep2nb5bsqg.streamlit.app/)

Imagine a smart emergency assistant that never sleeps—always ready to provide **live weather alerts** and **incident updates** whenever you need them. This **Real-Time Emergency Response Dashboard** ensures you stay informed with up-to-the-minute data, no matter the situation.

Built with **Streamlit, OpenWeatherMap API, and SQLite**, the dashboard offers a seamless experience for monitoring emergency events with speed, reliability, and high availability.

---
## 🎯 What This Project Does

✅ **Live Weather Alerts** – Simply enter a city, and the system fetches real-time weather data. If conditions trigger an alert (e.g., extreme temperatures), an emergency incident is recorded.  
✅ **Incident Management** – Each weather alert becomes a stored incident, retrievable anytime from the dashboard.  
✅ **Interactive Map** – Visualizes incidents, centering on the latest alert for quick situational awareness.  
✅ **On-Demand History Reset** – With one click, clear all past incidents and start fresh.  
✅ **High Availability & Caching** – Uses a JSON cache to ensure lightning-fast data retrieval, even during high-traffic situations.

---
## ⚡ How It Stays Always On

🔹 **Quick Data Access with Caching**  
A **JSON cache** of recent incidents enables rapid data retrieval, reducing the load on the database and ensuring smooth operation, even in critical situations.

🔹 **Robust Data Storage**  
Incidents are stored in **SQLite**, but the system is designed to scale—easily switch to **MySQL with replication & failover** for enterprise-grade reliability.

🔹 **Resilient Architecture**  
Built with **Streamlit**, each interaction refreshes the script, guaranteeing you always see the most up-to-date information. This modular approach ensures high availability and fault tolerance.

---
## 🛠️ Setup & Installation

### 🔹 Prerequisites
Ensure you have **Python 3.7 or later** installed on your system.

### 🔹 Installation Steps
```bash
# Clone this repository
git clone https://github.com/YOUR_GITHUB/real-time-emergency-dashboard.git
cd real-time-emergency-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---
## 🎮 How It Works

1️⃣ **Enter a city name** – The dashboard fetches live weather data using OpenWeatherMap.  
2️⃣ **Automatic Alert Detection** – If extreme weather conditions are detected, an incident record is created.  
3️⃣ **Incident Map** – Alerts are plotted on an interactive map that automatically centers on the latest event.  
4️⃣ **Clear Incident History** – Hit the "Refresh Data" button to start fresh at any time.

---
## 🏆 Why Use This?

🔹 **Real-Time Insights:** Always have up-to-date emergency weather alerts at your fingertips.  
🔹 **High Availability:** Designed to work even under heavy loads with caching and scalable storage options.  
🔹 **User-Friendly:** A clean, intuitive interface powered by Streamlit.  
🔹 **Scalable & Customizable:** Swap SQLite for MySQL or add integrations like SMS/email alerts.  

---
## 📜 License

This project is **open-source** under the MIT License. Feel free to modify, enhance, and contribute!

---
## 🙌 Contribute

🚀 Got ideas or improvements? Feel free to **fork the repo & submit a PR!**  
📩 Found a bug? Open an **issue** on GitHub!

🌟 **If you found this useful, give it a star on GitHub!** ⭐

🔥 Stay informed, stay safe! 🚀
