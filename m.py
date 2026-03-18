import streamlit as st

st.set_page_config(page_title="Cloud Storage Model", layout="wide")

st.title("📊 Cloud Storage Growth Model")

# Sidebar Navigation
page = st.sidebar.radio("Go to", ["Model Simulation", "Project Explanation"])

# -----------------------------
# PAGE 1 → MODEL
# -----------------------------
if page == "Model Simulation":
    import numpy as np
    import matplotlib.pyplot as plt

    def cloud_storage_model(S0, r, K, U, days, threshold, expansion):
        S = S0
        storage = []
        capacity = []

        for t in range(days):
            dS = r * S * (1 - S / K) + U
            S += dS

            if S >= threshold * K:
                K += expansion

            storage.append(S)
            capacity.append(K)

        return storage, capacity

    st.header("📈 Simulation")

    S0 = st.sidebar.number_input("Initial Storage", 500)
    r = st.sidebar.slider("Growth Rate", 0.01, 0.2, 0.05)
    K = st.sidebar.number_input("Capacity", 2000)
    U = st.sidebar.number_input("Daily Upload", 20)
    days = st.sidebar.slider("Days", 10, 200, 60)
    threshold = st.sidebar.slider("Threshold", 0.5, 1.0, 0.8)
    expansion = st.sidebar.number_input("Expansion Size", 500)

    S, K_hist = cloud_storage_model(S0, r, K, U, days, threshold, expansion)

    fig, ax = plt.subplots()
    ax.plot(S, label="Storage")
    ax.plot(K_hist, linestyle='--', label="Capacity")
    ax.legend()
    ax.set_xlabel("Days")
    ax.set_ylabel("Storage (GB)")

    st.pyplot(fig)

# -----------------------------
# PAGE 2 → EXPLANATION
# -----------------------------
elif page == "Project Explanation":

    st.header("📘 Cloud Storage Growth Model – Explanation")

    st.markdown("""
## 1. Problem Definition

### 📌 Introduction
In modern organizations, corporate data is increasing rapidly due to daily uploads such as documents, images, videos, backups, logs, and application data. As businesses expand, cloud storage requirements also grow.

Initially, storage grows **exponentially**, but later slows down due to **capacity limits**, forming a **logistic growth pattern**.

---

### 📌 Problem Statement
We aim to predict future storage usage using:
- **Exponential Growth** (fast initial growth)
- **Logistic Growth** (capacity limitation)

The model considers:
- Daily uploads  
- Current storage  
- Maximum capacity  
- Expansion planning  

---

### 📌 Objective
- Predict storage usage  
- Identify saturation point  
- Plan expansion in advance  

---

### 📌 Importance
- Prevents overflow  
- Reduces downtime  
- Helps budgeting  
- Supports long-term planning  

---

## 2. Design Model

### 📌 Models Used
- Exponential: S(t) = S0 e^(rt)  
- Logistic: S(t) = K / (1 + Ae^(-rt))  
- Combined: dS/dt = rS(1 - S/K) + U  

---

### 📌 Variables
- S0 → Initial storage  
- r → Growth rate  
- K → Capacity  
- U → Daily upload  
- t → Time  
- Threshold → Expansion trigger  

---

### 📌 System Flow
Daily Uploads → Storage → Growth → Capacity Limit → Update → Expansion
---

## 3. Visualization & Analysis

### Scenario 1 (Moderate Growth)
- Gradual increase  
- Expansion occurs later  

### Scenario 2 (High Growth)
- Rapid increase  
- Early expansion required  

---

### 📌 Observations
- Higher r → Faster growth  
- Higher U → More storage usage  
- Lower K → Early saturation  

---

## ✅ Conclusion

- Growth is not purely exponential  
- Logistic limits are necessary  
- Combined model is realistic  
- Expansion planning avoids failure  
- Useful for real-world cloud systems  
""")