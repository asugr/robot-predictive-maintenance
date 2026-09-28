# 🦾 Can We Predict When a Robot Will Fail?

**Engineering portfolio project — Robotics + Data Science + Predictive Maintenance**

## Research question

> Can condition-monitoring data from a robotic arm help identify failure conditions?

### Why I chose this problem

I am interested in mechanical/aerospace engineering and have had exposure to medical robotics. I wanted to investigate independently how measurements from a physical machine can be transformed into useful engineering information.

## Dataset

Public Kaggle **Robot Predictive Maintenance** dataset.

The uploaded training data contain:

- **235,854 observations**
- **23 operating conditions**
- **6 motors**
- **17,063 labeled failure observations**
- failure observation rate: **7.23%**

## What makes this an engineering project?

The project does not stop at model accuracy. It asks:

1. Which sensor patterns are associated with failure?
2. Does a model generalize to later operating conditions?
3. What happens when validation is made more realistic?
4. What would be required before such a model could support real maintenance decisions?

## Modeling approach

Features:

- position
- temperature
- voltage
- recent rolling means
- recent rolling standard deviations
- 20-sample changes
- relative time
- motor identity

Models:

- Logistic Regression
- Random Forest

### Validation

The **last four training conditions chronologically** were held out:

`20240503_163963, 20240503_164435, 20240503_164675, 20240503_165189`

This prevents rows from the same operating condition appearing in both training and test sets.

## Results

| Model | ROC-AUC | Average Precision | Precision @ 0.5 | Recall @ 0.5 | F1 |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.704 | 0.068 | 0.000 | 0.000 | 0.000 |
| Random Forest | 0.833 | 0.135 | 0.000 | 0.000 | 0.000 |

## Main finding

The project shows that **generalization to new operating conditions is substantially harder than a random row-level split would suggest**.

That is an important engineering/data-science result. A model can learn patterns associated with known operating conditions without necessarily becoming a reliable predictor for a new condition.

## Limitations

- The dataset represents an educational robot, not a medical robot.
- Labels describe observed failure states and do not establish physical causation.
- The model is not a certified safety or maintenance system.
- More experiments and data are needed for a genuine predictive-maintenance application.

## Future work

The next version will investigate an **early-warning problem**:

> Can current sensor measurements predict whether failure will occur within a defined future time window?

## Portfolio deliverables

- Kaggle notebook
- GitHub repository
- Streamlit interactive demo
- ScienceBehindIt video
- engineering reflection
