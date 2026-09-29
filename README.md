🦾 Can We Predict When a Robot Will Fail?
An exploratory predictive-maintenance study using robotic-arm sensor data
> **Can condition-monitoring data from a robotic arm provide useful information about failure—and can it provide an early warning before failure begins?**
Engineering portfolio project | Robotics • Mechanical Engineering • Data Science • Predictive Maintenance
---
🔬 Why I chose this project
I am interested in Mechanical and Aerospace Engineering and have had exposure to a university medical-robotics environment.
I wanted to investigate a question at the intersection of physical machines, sensors, mathematics and programming:
> Can measurements collected from a robotic system reveal patterns that could help identify an approaching failure?
Rather than building a purely theoretical machine-learning exercise, I used a real public robotic-arm dataset and focused on an engineering question: how useful would the predictions actually be?
---
📊 Dataset
The project uses the public Robot Predictive Maintenance dataset from Kaggle.
The training data contain:
	
Sensor observations	235,854
Operating conditions	23
Robot motors	6
Failure observations	17,063
Failure observation rate	7.23%
The measurements include variables such as:
motor position
temperature
voltage
time
failure status
Dataset source: Kaggle — Robot Predictive Maintenance
The raw dataset is intentionally not stored in this GitHub repository.
---
🧪 Experiment 1 — Failure Classification
The first question was:
> **Can sensor measurements distinguish normal and failure conditions?**
I engineered features describing both current sensor values and recent behavior:
rolling mean
rolling standard deviation
recent change
operating time
relative position within a run
motor identity
I compared interpretable and nonlinear approaches, including:
Logistic Regression
Random Forest
Validation
Instead of randomly splitting individual time-series rows, I held out later operating conditions.
This was important because neighboring observations from the same run can be highly similar. A random split could therefore produce an overly optimistic estimate of performance.
The Random Forest achieved approximately:
> **ROC-AUC = 0.833**
on the held-out operating conditions.
---
⏱️ Experiment 2 — Can We Predict Failure Before It Happens?
This was the more interesting part of the project.
Instead of asking:
> "Is the robot failing now?"
I asked:
> **"Will a failure begin within the next 1, 3, 5 or 10 seconds?"**
Only observations occurring before the failure were used for this early-warning experiment.
Results
Warning horizon	ROC-AUC	Average Precision
1 second	0.877	0.005
3 seconds	0.810	0.010
5 seconds	0.793	0.015
10 seconds	0.804	0.031
These results require careful interpretation.
ROC-AUC shows that the model can distinguish the classes to some degree, but the very low precision reflects how rare the pre-failure events are.
That means I cannot reasonably claim that the model is ready for real predictive maintenance.
And that leads to the most interesting part of the project.
---
⚖️ Experiment 3 — The False-Alarm Problem
A predictive-maintenance system does not simply output "yes" or "no."
It produces a probability, and an engineer must decide:
> **At what probability should the system raise an alarm?**
I therefore tested multiple probability thresholds.
At a high-sensitivity operating point in the 10-second experiment:
Recall: ~99.7%
Precision: ~4.85%
False alarms per true warning: ~19.6
In other words, the model could identify almost all of the rare upcoming failures in this held-out experiment, but it would also generate many false alarms.
Why this matters
This demonstrates an important engineering principle:
> **A model can have useful discrimination and still be impractical if the cost of false alarms is too high.**
The correct threshold would depend on the real-world cost of:
missing a failure
inspecting a false alarm
interrupting operation
performing unnecessary maintenance
I therefore do not claim that one threshold is universally optimal.
---
🧠 What I learned
The most important result was not simply the model score.
I learned that predictive maintenance is a systems problem, not just a machine-learning problem.
Three things mattered:
1. Validation matters
A random row-level split can make a time-series model appear better than it really is.
2. Timing matters
Detecting a failure after it begins is different from providing useful warning beforehand.
3. False alarms matter
High recall alone does not make a predictive system useful.
A real engineering deployment would require much more data, domain expertise, probability calibration and event-level validation.
---
🛠️ Technical workflow
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
📁 Repository structure
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
🚧 Limitations
This is an exploratory student engineering project.
The dataset represents an educational robotic system, not a medical or industrial safety-critical robot.
The failure labels do not establish the physical cause of failure.
The early-warning experiment focuses on the first failure onset in each motor run.
The data contain rare failure events, making precision challenging.
The model has not been validated for operational maintenance decisions.
These limitations are part of the investigation rather than something to hide.
---
🚀 Future work
A natural next step would be to investigate:
multiple failure episodes per run
longer prediction horizons
event-level rather than row-level evaluation
probability calibration
additional sensor features
physical interpretation of the most predictive measurements
comparison with engineering threshold rules
---
📚 Project resources
Kaggle dataset: Robot Predictive Maintenance
Notebook: `notebooks/robot_failure_prediction.ipynb`
Early-warning experiment: `notebooks/early_warning_analysis.ipynb`
Interactive prototype: `app/app.py`
---
👩‍💻 About the project
This project was created as an independent engineering investigation combining:
Robotics + Mechanical Engineering + Mathematics + Programming + Data Science
It is part of my broader ScienceBehindIt Engineering Lab, where I explore the science and engineering behind real-world machines and communicate what I learn through computational experiments and science communication.
- Kaggle notebook
- GitHub repository
- Streamlit interactive demo
- ScienceBehindIt video
- engineering reflection
