# 🦾 Can We Predict When a Robot Will Fail?

### An exploratory predictive-maintenance study using robotic-arm sensor data

> **Can condition-monitoring data from a robotic arm provide useful information about failure—and can it provide an early warning before failure begins?**

**Robotics • Mechanical Engineering • Data Science • Predictive Maintenance**

---

## ⭐ Project at a Glance

| | |
|---|---:|
| Sensor observations | **235,854** |
| Operating conditions | **23** |
| Robot motors | **6** |
| Failure observations | **17,063** |
| Failure observation rate | **7.23%** |
| Failure-classification ROC-AUC | **0.833** |

### The engineering question

I wanted to investigate whether measurements from a physical robotic system could reveal patterns associated with failure—and, more importantly, whether those patterns could provide **useful warning before failure occurs**.

This project combines **robotics, mathematics, programming, machine learning, and engineering reasoning**.

---

## 🔬 Why I Chose This Project

I am interested in Mechanical and Aerospace Engineering and have had exposure to a university medical-robotics environment.

Rather than building a purely theoretical machine-learning exercise, I wanted to work with measurements from a real robotic system and ask:

> **How useful would the predictions actually be?**

The project therefore focuses not only on model performance, but also on **validation, timing, false alarms, and engineering limitations**.

---

## 📊 Dataset

The project uses the public **Robot Predictive Maintenance** dataset from Kaggle.

The measurements include:

- Motor position
- Temperature
- Voltage
- Time
- Failure status

The raw Kaggle dataset is **not stored in this repository**.

---

# 🧪 Experiment 1 — Failure Classification

### Question

> **Can sensor measurements distinguish normal and failure conditions?**

I engineered features describing both current sensor values and recent behavior:

- Rolling mean
- Rolling standard deviation
- Recent sensor change
- Operating time
- Relative position within a run
- Motor identity

I compared:

- **Logistic Regression**
- **Random Forest**

### Validation strategy

Instead of randomly splitting individual time-series observations, I held out later operating conditions.

This is important because neighboring observations from the same run can be highly similar. A random split could therefore produce an overly optimistic estimate of model performance.

### Result

The Random Forest achieved approximately:

> **ROC-AUC = 0.833**

on the held-out operating conditions.

---

# ⏱️ Experiment 2 — Can We Predict Failure Before It Happens?

This was the more challenging experiment.

Instead of asking:

> Is the robot failing now?

I asked:

> **Will a failure begin within the next 1, 3, 5, or 10 seconds?**

Only observations occurring **before the failure** were used for the early-warning task.

### Results

| Warning horizon | ROC-AUC | Average Precision |
|---:|---:|---:|
| 1 second | **0.877** | 0.005 |
| 3 seconds | 0.810 | 0.010 |
| 5 seconds | 0.793 | 0.015 |
| 10 seconds | 0.804 | **0.031** |

### What does this mean?

The ROC-AUC values show that the model contains some useful discriminatory information.

However, **precision is very low because pre-failure events are rare**.

Therefore, I do **not** claim that this model is ready for real predictive-maintenance deployment.

Instead, this result led to the next engineering question:

> **What happens when we change the alarm threshold?**

---

# ⚖️ Experiment 3 — The False-Alarm Problem

A predictive-maintenance model produces a probability. An engineer must decide when that probability is high enough to trigger an alarm.

I therefore evaluated multiple probability thresholds for the 10-second warning model.

At a high-sensitivity operating point in the held-out data:

| Metric | Result |
|---|---:|
| Recall | **~99.7%** |
| Precision | **~4.85%** |
| False alarms per true warning | **~19.6** |

This means the model can identify almost all of the rare upcoming failures in this experiment, but it also produces many false alarms.

### Engineering lesson

> **A model can have useful discrimination and still be impractical if the cost of false alarms is too high.**

The correct threshold would depend on the real-world cost of:

- Missing a failure
- Investigating a false alarm
- Interrupting operation
- Performing unnecessary maintenance

I therefore do **not** assume that one threshold is universally optimal.

---

## 🧠 What I Learned

The most important result was not simply the model score.

### 1. Validation matters

A random row-level split can make a time-series model appear better than it really is.

### 2. Timing matters

Detecting a failure after it begins is fundamentally different from providing useful warning beforehand.

### 3. Rare events change the evaluation

When failures are rare, accuracy and ROC-AUC alone do not tell the whole story. **Precision, recall, and false-alarm burden** become important.

### 4. Engineering decisions require context

A useful predictive system would need domain experts to determine the acceptable trade-off between missed failures and false alarms.

---

## 🛠️ Technical Workflow

```text
Robot sensor data
        ↓
Data cleaning
        ↓
Exploratory analysis
        ↓
Feature engineering
        ↓
Failure classification
        ↓
Leakage-aware validation
        ↓
Early-warning prediction
        ↓
Threshold analysis
        ↓
Engineering interpretation
```

---

## 📁 Repository Structure

```text
robot-predictive-maintenance/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│       ├── condition_summary.csv
│       ├── early_warning_results.csv
│       └── threshold_analysis_10s.csv
│
├── images/
│   ├── failure_rate_by_motor.png
│   ├── sensor_distributions.png
│   ├── example_failure_timeline.png
│   ├── roc_curves.png
│   ├── early_warning_by_horizon.png
│   ├── threshold_precision_recall.png
│   └── false_alarm_tradeoff.png
│
├── models/
│
├── notebooks/
│   ├── robot_failure_prediction.ipynb
│   └── early_warning_analysis.ipynb
│
├── src/
│
├── README.md
└── requirements.txt
```

---

## 🚧 Limitations

This is an **exploratory student engineering project**.

- The dataset represents an educational robotic system, not a medical or industrial safety-critical robot.
- Failure labels do not establish the physical cause of failure.
- The early-warning experiment focuses on the first failure onset in each motor run.
- Pre-failure events are rare, making precision challenging.
- The model has not been validated for operational maintenance decisions.

These limitations are part of the investigation rather than something to hide.

---

## 🚀 Future Work

A natural next step would be to investigate:

- Multiple failure episodes per run
- Longer prediction horizons
- Event-level rather than row-level evaluation
- Probability calibration
- Additional sensor features
- Physical interpretation of the most predictive measurements
- Comparison with engineering threshold rules

---

## 📚 Project Resources

- **Main analysis:** [`robot_failure_prediction.ipynb`](notebooks/robot_failure_prediction.ipynb)
- **Early-warning experiment:** [`early_warning_analysis.ipynb`](notebooks/early_warning_analysis.ipynb)
- **Threshold analysis:** [`threshold_analysis_10s.csv`](data/processed/threshold_analysis_10s.csv)
- **Interactive prototype:** [`app.py`](app/app.py)

---

## 👩‍💻 About the Project

This project was created as an independent engineering investigation combining:

**Robotics + Mechanical Engineering + Mathematics + Programming + Data Science**

It is part of my broader **ScienceBehindIt Engineering Lab**, where I explore the science and engineering behind real-world machines through computational experiments and science communication.
