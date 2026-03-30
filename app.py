import streamlit as st
import pandas as pd

from database.db import engine, SessionLocal
from database.models import Base, VerificationLog
from services.register_service import register_user
from background.monitor import start_monitoring, stop_monitoring

# Create tables if not exist
Base.metadata.create_all(bind=engine)

# Page config
st.set_page_config(page_title="TrustID", layout="centered")

st.title("🔐 TrustID - Continuous Face Authentication")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Option",
    ["Register User", "Start Monitoring", "View Logs"]
)

# =====================================================
# REGISTER USER
# =====================================================
if menu == "Register User":

    st.header("👤 Register New User")

    user_id = st.text_input("User ID")
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Register"):
        if not user_id or not name or not email:
            st.warning("All fields are required.")
        else:
            with st.spinner("Capturing face..."):
                register_user(user_id, name, email)
            st.success("User registered successfully ✅")


# -----------------------------
# START MONITORING
# -----------------------------

elif menu == "Start Monitoring":

    st.header("🟢 Start Continuous Monitoring")

    user_id = st.text_input("Enter User ID")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Start Monitoring", key="start_monitor"):
            if user_id:
                start_monitoring(user_id)
                st.success("Monitoring Started ✅")
            else:
                st.warning("Enter User ID")

    with col2:
        if st.button("Stop Monitoring", key="stop_monitor"):
            stop_monitoring()
            st.error("Monitoring Stopped ⛔")


# =====================================================
# VIEW LOGS
# =====================================================
elif menu == "View Logs":

    st.header("📊 Verification Logs")

    db = SessionLocal()
    logs = db.query(VerificationLog).all()

    if logs:
        data = [{
            "User ID": log.user_id,
            "Similarity": log.similarity,
            "Result": log.result,
            "Time": log.timestamp
        } for log in logs]

        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No logs available yet.")

    db.close()
if st.button("Start Monitoring"):
    if not user_id:
        st.warning("Enter User ID")

    else:
        db = SessionLocal()
        user = db.query(VerificationLog).filter_by(user_id=user_id).first()
        db.close()

        if user is None:
            st.warning("⚠️ User not registered. Please register first.")

        else:
            start_monitoring(user_id)
            st.success("Monitoring Started ✅")