import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
model=joblib.load(ROOT/"models/robot_failure_random_forest.joblib")

st.set_page_config(page_title="Robot Health Monitor",page_icon="🦾",layout="wide")
st.title("🦾 Robot Health Monitor")
st.caption("Educational portfolio prototype — not a certified safety or maintenance system.")

st.markdown("### Explore how sensor conditions affect the model's predicted failure probability.")

c1,c2,c3=st.columns(3)
with c1:
    motor=st.selectbox("Motor", [1,2,3,4,5,6])
with c2:
    position=st.number_input("Position", value=100.0)
with c3:
    temperature=st.slider("Temperature",20.0,100.0,45.0,0.5)

c4,c5,c6=st.columns(3)
with c4:
    voltage=st.slider("Voltage",5000.0,8000.0,7000.0,10.0)
with c5:
    time_s=st.number_input("Time since run start (s)",min_value=0.0,value=30.0)
with c6:
    time_frac=st.slider("Relative position in run",0.0,1.0,0.2)

# For the demo, recent-window values are approximated by the current inputs.
row=pd.DataFrame([{"position":position,"temperature":temperature,"voltage":voltage,
"relative_time_s":time_s,"time_frac":time_frac,
"temperature_roll_mean20":temperature,"temperature_roll_std20":0.0,"temperature_delta20":0.0,
"voltage_roll_mean20":voltage,"voltage_roll_std20":0.0,"voltage_delta20":0.0,
"position_roll_mean20":position,"position_roll_std20":0.0,"position_delta20":0.0,"motor":motor}])

features=['position', 'temperature', 'voltage', 'relative_time_s', 'time_frac', 'temperature_roll_mean20', 'temperature_roll_std20', 'temperature_delta20', 'voltage_roll_mean20', 'voltage_roll_std20', 'voltage_delta20', 'position_roll_mean20', 'position_roll_std20', 'position_delta20', 'motor']
prob=float(model.predict_proba(row[features])[:,1][0])

st.divider()
a,b=st.columns(2)
a.metric("Predicted failure probability",f"{prob*100:.1f}%")
b.metric("Motor",str(motor))

if prob < 0.25:
    st.success("Lower predicted risk in this model scenario.")
elif prob < 0.60:
    st.warning("Elevated predicted risk — investigate the sensor trend.")
else:
    st.error("High predicted risk — this scenario deserves investigation.")

st.info("This demo is designed to show the modeling concept. It should not be used to make real maintenance or safety decisions.")
