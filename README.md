# 🎲 Ergodicity & Risk Simulator

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-link.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Project Overview

An interactive Data Science simulation exploring the divergence between **Ensemble Averages** and **Time Averages** in non-ergodic systems.

This project demonstrates why *"group logic"* often fails the individual and how the **Kelly Criterion** mitigates the risk of ruin.

---

## 🔍 What This Simulator Shows

* **The absorbing barrier problem:**
  High volatility can lead to individual bankruptcy—even when average returns are positive.

* **Risk Management:**
  Using the Kelly Criterion to determine optimal bet sizing.

* **Social Safety Nets:**
  A "Reset Mechanism" simulating insurance or bailout systems.

---

## 🏗️ Architecture

The project follows a modular design:

```
.
├── engine.py   # Core stochastic simulations & Kelly calculations
├── app.py      # Streamlit UI and Plotly visualizations
└── requirements.txt
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RajeshKumar3451/Ergodicity-Simulator.git
cd ergodicity-simulator
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv .venv
```

Activate it:

* **Windows**

```bash
.venv\Scripts\activate
```

* **Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```
## 📊 Key Insights

- High volatility environments can destroy individual wealth despite positive expected returns  
- Ensemble averages are misleading in non-ergodic systems  
- Kelly Criterion significantly improves survival probability  
- Risk management is more important than return maximization  
  
---

## 📈 Kelly Criterion

The Kelly Criterion determines the optimal fraction of wealth to allocate in order to maximize long-term logarithmic growth.

**Formula:**
$f^* = \frac{\mu}{\sigma^2}$

---

### Where:

* $f^*$: Optimal fraction of wealth to invest (or risk)
* $\mu$: Expected return (drift)
* $\sigma$: Volatility (standard deviation of returns)

---

## 📘 Alternative (Discrete Form)

**Formula:**
$f^* = \frac{bp - q}{b}$
or
$f^* = \frac{W - (1 - W)}{R}$

---

### Where:

* $p$: Probability of winning
* $q = 1 - p$: Probability of losing
* $b$: Net odds received on the wager
* $W$: Win probability
* $R$: Win/Loss ratio

---

## 📊 Interpretation

* The optimal allocation increases with higher expected returns
* The optimal allocation decreases with higher volatility
* Overbetting ($f > f^*$) increases risk of ruin
* Underbetting ($f < f^*$) leads to suboptimal growth

---

### ⚠️ Non-Ergodicity

* The **Ensemble Average** (the crowd) grows exponentially
* The **Median Path** (typical individual) often declines toward zero

This divergence highlights why averages can be misleading in real-world systems.

---

## 🛠️ Tech Stack

* **Language:** Python
* **UI Framework:** Streamlit
* **Math/Data:** NumPy, Pandas
* **Visualization:** Plotly (interactive WebGL)

---

## 🌐 Live Demo

👉 https://ergodicity-simulator.streamlit.app/

---

## 👤 Author

**Rajesh Kumar**

*Aspiring Data Scientist*

*[Linkedin](http://www.linkedin.com/in/rajesh-kumar-9aa2261b7)*

---

## ⭐ If you found this useful, give it a star!