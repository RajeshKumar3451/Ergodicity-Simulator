import streamlit as st
import plotly.graph_objects as go
import numpy as np
from engine import ErgodicityEngine

st.set_page_config(page_title="Ergodicity Lab", layout="wide")

# Sidebar
st.sidebar.header("Control Panel")
agents = st.sidebar.slider("Agents", 10, 500, 100)
steps = st.sidebar.slider("Steps", 50, 1000, 300)
vol = st.sidebar.slider("Volatility", 0.01, 0.50, 0.15)
growth = st.sidebar.slider("Expected Growth", -0.05, 0.10, 0.02)
use_kelly = st.sidebar.toggle("Use Kelly Criterion", value=True)
reset = st.sidebar.number_input("Reset Threshold", value=0.1)

# Run Simulation
sim = ErgodicityEngine(agents, steps, growth, vol, reset)
data, kelly_f = sim.run(use_kelly)

# Stats
ens_avg = np.mean(data, axis=1)
med_path = np.median(data, axis=1)

# UI Layout
st.title("📈 Ergodicity Simulator")
c1, c2, c3 = st.columns(3)
c1.metric("Kelly Fraction", f"{kelly_f:.2%}")
c2.metric("Final Ensemble Avg", f"{ens_avg[-1]:.2f}")
c3.metric("Final Median", f"{med_path[-1]:.2f}")

# Plotting
fig = go.Figure()
for i in range(min(agents, 50)):
    fig.add_trace(go.Scatter(y=data[:, i], line=dict(width=0.5, color='gray'), opacity=0.3, showlegend=False))

fig.add_trace(go.Scatter(y=ens_avg, name="Ensemble (The Group)", line=dict(color='cyan', width=3)))
fig.add_trace(go.Scatter(y=med_path, name="Median (The Individual)", line=dict(color='orange', width=3)))

fig.update_layout(template="plotly_dark", yaxis_type="log" if st.checkbox("Log Scale") else "linear")
st.plotly_chart(fig, use_container_width=True)