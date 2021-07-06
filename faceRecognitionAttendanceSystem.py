import streamlit as st 
from initFaceRecognitionAttendanceSystemAIHelper import faceRecognitionAttendanceSystem
from webcam import webcam
from datetime import datetime


system = faceRecognitionAttendanceSystem()

system.homeInterface()

with st.sidebar.beta_expander("Section A: Registration"):
    st.sidebar.header("Registration")
    st.sidebar.write("Register a new staff info")
    st.sidebar.write("Take note that this prototype demo does not store any info permanently into the server.")
    st.sidebar.write("Should you feel uncomfortable, please use any cartoon face.")
    
    register = st.siderbar.button("Register")
    
    if register:
        system.initRegistrationModule()

        
with st.sidebar.beta_expander("Section B: Check in"):
    st.sidebar.header("Check in your attendance")

    system.initCheckInModule()
    
    
with st.sidebar.beta_expander("Section C: Summary"):
    st.sidebar.header("Check your attendance records")

    system.initSummaryModule()        
        
