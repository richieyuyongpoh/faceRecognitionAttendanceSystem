import streamlit as st 
from initFaceRecognitionAttendanceSystemAIHelper import faceRecognitionAttendanceSystem
from webcam import webcam
from datetime import datetime


system = faceRecognitionAttendanceSystem()

system.homeInterface()

with st.sidebar.beta_expander("Section A: Registration"):
    st.header("Registration")
    st.write("Register a new staff info")
    st.write("Take note that this prototype demo does not store any info permanently into the server.")
    st.write("Should you feel uncomfortable, please use any cartoon face.")
    
    register = st.button("Register")
    
if register:
    
    system.user_choice = 1
#     system.initRegistrationModule()

        
with st.sidebar.beta_expander("Section B: Check in"):
    st.header("Check in your attendance")

    checkin = st.button("Check In")
    
if checkin:
       
    system.user_choice = 2   
#     system.initCheckInModule()
    
    
with st.sidebar.beta_expander("Section C: Summary"):
    st.header("Check your attendance records")
    
    summary = st.button("Attendance Record")
    
if summary:
    
    system.user_choice = 3
#     system.initSummaryModule()        



if system.user_choice ==1:
    system.initRegistrationModule()
    
elif system.user_choice ==2:
    system.initCheckInModule()
    
elif system.user_choice ==3:
    system.initSummaryModule()   
    
else:
    system.homeInterface()
        
