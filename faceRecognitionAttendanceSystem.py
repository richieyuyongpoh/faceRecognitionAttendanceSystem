import streamlit as st 
from initFaceRecognitionAttendanceSystemAIHelper import faceRecognitionAttendanceSystem , VideoTransformer
import face_recognition
from datetime import datetime
# from streamlit_webrtc import webrtc_streamer

system = faceRecognitionAttendanceSystem()


user_choice = st.sidebar.selectbox(
    'Select an Option',
    ('Home','Register', 'Check in', 'View attendance Record'))

# system = faceRecognitionAttendanceSystem()
if user_choice== 'Register':
    
    system.initRegistrationModule()

elif user_choice== 'Check in':        


    system.initCheckInModule()
    
    
elif user_choice== 'View attendance Record':  
    
    system.initSummaryModule()        

else:
    system.homeInterface()
        
