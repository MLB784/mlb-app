
import streamlit as st
from core.poisson_model import estimate_goal_probabilities
from core.value_bet import calculate_ev_kelly
from core.alerts import check_alerts
import pandas as pd

st.title("Mlb - Analyse Over 1.5 / 2.5")

match = st.text_input("Entrer un match (ex: Sarmiento - Lanus)")
if match:
    proba_15, proba_25 = estimate_goal_probabilities(match)
    ev_15, stake_15 = calculate_ev_kelly(proba_15, 1.50)
    ev_25, stake_25 = calculate_ev_kelly(proba_25, 2.00)
    alert = check_alerts(match)

    st.markdown(f"### Résultats pour {match}")
    st.write(f"Probabilité Over 1.5 : {proba_15*100:.1f} %")
    st.write(f"Probabilité Over 2.5 : {proba_25*100:.1f} %")
    st.write(f"EV Over 1.5 : {ev_15:.2f} | Mise suggérée : {stake_15:.2f} %")
    st.write(f"EV Over 2.5 : {ev_25:.2f} | Mise suggérée : {stake_25:.2f} %")
    st.warning(f"Alerte : {alert}" if alert else "Pas d'alerte.")
