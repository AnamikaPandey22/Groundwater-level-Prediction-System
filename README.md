# 🌊 NeerAI – Groundwater Prediction & Awareness System

**NeerAI** is a data-driven groundwater prediction and awareness system developed to analyze historical groundwater trends and forecast future groundwater levels in the **Gandak River Basin**.

The project combines **time-series forecasting, data visualization, and an interactive Flask-based interface** to make groundwater insights easier to understand and use. Along with prediction capabilities, NeerAI provides historical trend analysis and water conservation information to promote awareness of sustainable water usage.

---

## ✨ Features -

* 📊 **District-wise Groundwater Prediction**

  * Forecasts groundwater levels using the **Facebook Prophet** time-series forecasting model.
  * Uses historical groundwater observations to identify trends and patterns.

* 📈 **Historical Trend Analysis**

  * Visualizes historical groundwater-level variations.
  * Helps understand changes and long-term patterns across districts.

* 🤖 **Interactive Chatbot Interface**

  * Flask-based interface for interacting with the groundwater prediction system.
  * Provides an accessible way to explore groundwater-related information.

* 💧 **Water Conservation Awareness**

  * Includes static information and practical tips for groundwater conservation.
  * Promotes responsible and sustainable water usage.

* 🗺️ **Gandak River Basin Focus**

  * Designed around historical groundwater data from districts within the Gandak River Basin.

---

## 🛠️ Tech Stack -

| Technology           | Purpose                                       |
| -------------------- | --------------------------------------------- |
| **Python**           | Core development and data processing          |
| **Facebook Prophet** | Groundwater-level forecasting                 |
| **Flask**            | Web application and chatbot interface         |
| **SARIMA**           | Time-series analysis and comparative analysis |
| **Matplotlib**       | Data visualization                            |
| **Pandas**           | Data manipulation and preprocessing           |
| **NumPy**            | Numerical computation                         |

---

## 📂 Dataset

The project uses the **BitByte Groundwater Dataset**, containing approximately **26 years of historical groundwater data** from the **Gandak River Basin**.

The historical dataset is used for:

* Data preprocessing
* Groundwater trend analysis
* Time-series modeling
* Future groundwater-level forecasting
* Visualization of historical and predicted trends

---

## 🔄 System Workflow

```text
Historical Groundwater Data
          │
          ▼
   Data Preprocessing
          │
          ▼
   Trend & Time-Series
       Analysis
          │
          ├───────────────┐
          ▼               ▼
      Prophet          SARIMA
     Forecasting       Analysis
          │
          ▼
  Groundwater Prediction
          │
          ▼
   Flask Web Interface
          │
          ▼
Prediction + Visualization
          │
          ▼
Water Conservation Awareness
```

---

## 📊 Prediction Module

The prediction module uses **Facebook Prophet** to model historical groundwater-level data and generate future forecasts.

Prophet is particularly useful for time-series forecasting because it can capture:

* Long-term trends
* Seasonal patterns
* Changes in time-series behavior
* Future trends based on historical observations

The system performs forecasting on a **district-wise basis**, allowing groundwater conditions to be analyzed at a more localized level.

---

## 📈 Visualization

**Matplotlib** is used to generate visual representations of groundwater data, including:

* Historical groundwater-level trends
* Forecasted groundwater levels
* Actual vs. predicted values
* Time-series patterns

These visualizations make it easier to interpret groundwater behavior and identify potential changes over time.

---

## 🌐 Application Interface

The project uses **Flask** to integrate the prediction functionality into a web-based application.

The application provides an interactive interface through which users can access groundwater-related information, explore predictions, and view relevant visualizations.

---

## 💧 Awareness & Conservation

NeerAI is not limited to prediction. It also focuses on creating awareness about groundwater conservation.

The application provides information and practical suggestions related to:

* Reducing unnecessary water consumption
* Rainwater harvesting
* Responsible groundwater usage
* Preventing water wastage
* Sustainable water management

The goal is to connect **data-driven prediction with environmental awareness**.

---

## 🎯 Project Objectives

The major objectives of NeerAI are:

1. To analyze historical groundwater-level data from the Gandak River Basin.
2. To identify long-term groundwater trends.
3. To forecast future groundwater levels using time-series models.
4. To provide district-wise groundwater insights.
5. To present predictions through an easy-to-use web interface.
6. To promote awareness regarding groundwater conservation.

---

## 👩‍💻 My Contribution

This project was developed as a **collaborative student project**.

My primary contribution focused on:

* Developing the **groundwater prediction module**.
* Working with historical groundwater data for forecasting.
* Implementing the **Facebook Prophet-based prediction workflow**.
* Integrating the prediction functionality with the Flask application.
* Supporting the visualization and presentation of prediction results.

---

## 🚀 Future Scope

NeerAI can be further enhanced by introducing:

* 🔮 More advanced machine-learning and deep-learning forecasting models.
* 🌦️ Integration of rainfall and weather data.
* 🛰️ Integration of satellite and remote-sensing data.
* 📍 Interactive maps for district-wise groundwater visualization.
* 📱 A mobile-friendly application.
* 🔔 Groundwater-level alerts and notifications.
* 📊 Real-time or regularly updated groundwater datasets.
* 🧠 A more advanced AI chatbot capable of answering groundwater-related queries dynamically.

---

## 📁 Project Structure

```text
NeerAI/
│
├── app.py                  # Flask application
├── prediction/             # Groundwater prediction module
├── models/                 # Forecasting/model files
├── data/                   # Dataset
├── static/                 # CSS, images and generated visualizations
├── templates/              # HTML templates
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

> *The exact project structure may vary depending on the implementation.*

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd NeerAI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it using:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open the local Flask server in your browser:

```text
http://127.0.0.1:5000/
```

---

## ⚠️ Disclaimer

NeerAI is an **academic/student project** developed for educational and awareness purposes. Forecasted groundwater levels are based on historical data and statistical modeling and should not be treated as official hydrological predictions or used as the sole basis for water-resource management decisions.

---

## 🌱 Impact

> **NeerAI aims to turn historical groundwater data into understandable insights—helping users visualize trends, explore future possibilities, and become more aware of the importance of groundwater conservation.**

---

## 📜 License

This project was developed for **academic and educational purposes**.
