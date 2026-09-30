"""Interactive logistic-growth demonstration for the Streamlit lesson."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Logistic Growth Lab")
st.title("Logistic Growth Lab")
st.write("Adjust the parameters to update the plot and data table.")

with st.sidebar:
    st.header("Parameters")
    p0 = st.slider("Initial population P(0)", 10, 100, 20, 5)
    capacity = st.slider("Carrying capacity K", 200, 1000, 500, 50)
    rate = st.slider("Growth rate r", 0.1, 1.0, 0.4, 0.1)
    max_time = st.slider("Final time", 5, 30, 20)
    show_table = st.checkbox("Show data table", value=True)

time = np.linspace(0, max_time, 201)
population = capacity / (1 + (capacity / p0 - 1) * np.exp(-rate * time))
data = pd.DataFrame({"time": time, "population": population})

fig, ax = plt.subplots()
ax.plot(time, population, color="#123f6c", linewidth=2)
ax.axhline(capacity, color="#dc8d29", linestyle="--", label="K")
ax.set(xlabel="Time", ylabel="Population", title="Logistic growth")
ax.grid(alpha=0.25)
ax.legend()
st.pyplot(fig)
plt.close(fig)

st.metric("Population at final time", f"{population[-1]:.2f}")
if show_table:
    st.dataframe(data.round(2), hide_index=True)

csv_bytes = data.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download CSV", csv_bytes, file_name="logistic_growth.csv", mime="text/csv"
)

if st.button("Show equation"):
    st.latex(r"P(t)=\frac{K}{1+\left(\frac{K}{P_0}-1\right)e^{-rt}}")
