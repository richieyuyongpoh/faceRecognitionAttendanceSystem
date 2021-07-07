import streamlit as st 
from initFaceRecognitionAttendanceSystemAIHelper import faceRecognitionAttendanceSystem
from webcam import webcam
from datetime import datetime


system = faceRecognitionAttendanceSystem()

# system.homeInterface()


user_choice = st.sidebar.selectbox(
    'Select an Option',
    ('Home','Register', 'Check in', 'View attendance Record'))

# system = faceRecognitionAttendanceSystem()
if user_choice== 'Register':
    
    st.sidebar.header("Registration")
    st.sidebar.write("Register a new staff info")
    st.sidebar.write("Take note that this prototype demo does not store any info permanently into the server.")
    st.sidebar.write("Should you feel uncomfortable, please use any cartoon face.")

    system.initRegistrationModule()

elif user_choice== 'Check in':        


    system.initCheckInModule()
    
    
elif user_choice== 'View attendance Record':  
    
    system.initSummaryModule()        

else:
    system.homeInterface()
        
