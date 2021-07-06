import streamlit as st 
from initFaceRecognitionAttendanceSystemAIHelper import faceRecognitionAttendanceSystem
from webcam import webcam
from datetime import datetime


system = faceRecognitionAttendanceSystem()

system.homeInterface()

with st.beta_expander("Section A: Registration"):
    st.header("Registration")
    st.write("Register a new staff info")
    st.write("Take note that this prototype demo does not store any info permanently into the server.")
    st.write("Should you feel uncomfortable, please use any cartoon face.")
    
    register = st.button("Register")
    
    if register:
        system.initRegistrationModule()

        
with st.beta_expander("Section B: Check in"):
    st.header("Check in your attendance")

    checkin = st.button("Check In")
    
    if checkin:
        system.initCheckInModule()
    
    
with st.beta_expander("Section C: Summary"):
    st.header("Check your attendance records")
    
    summary = st.button("Attendance Record")
    
    if summary:
        system.initSummaryModule()        
        
