import streamlit as st 

import face_recognition
from datetime import datetime
from tempfile import NamedTemporaryFile  
import pandas as pd
import numpy as np


@st.cache(allow_output_mutation=True)
def known_face_encodings():
    return []
  
@st.cache(allow_output_mutation=True)
def known_face_names():
    return []

@st.cache(allow_output_mutation=True)
def registerUserInfo():
    return []
  
@st.cache(allow_output_mutation=True)
def face_encodings():
    return []
  
@st.cache(allow_output_mutation=True)
def nameRecord():
    return []

@st.cache(allow_output_mutation=True)
def timeRecord():
    return []
        
        
def clearMemory():
    
    st.write("To clear the registration and attendance records, press CLEAR button below.")
    st.write("")
    st.write("") 
        
    clear = st.button("CLEAR")
        
    if clear:
    
        known_face_encodings().clear()
        known_face_names().clear()
        registerUserInfo().clear()
        nameRecord().clear()
        timeRecord().clear()
    

        
        st.write("<font color='Aquamarine'>Memory has been cleared</font>", unsafe_allow_html=True)
            

        
    return
        
def homeInterface():



    st.title("Welcome to RICHIEYYPTUTORIALPAGE Face Recognition Attendance System")
        
    readme = st.checkbox('Read Me.')

    if readme:
 
        st.write("For demo + privacy reason, it uses file upload widget instead real-time offline/local webcam recording. ")
        st.write("For Real Deployment, it is suggested to use a local webcam to detect and recognize the faces directly.") 
        st.write("Take note that this prototype demo does not store any info permanently into the backend server.")
        st.write("Should you feel uncomfortable, please use any cartoon face, fake user name and fake password.")
    st.write("")
    st.write("")
    st.write("")

        
    st.write ("For more info, please contact:")
    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)
    st.write("")
    st.write("")        
        

            
    return    
 
        
        
        
def initCheckInModule():
        
    if registerUserInfo() ==[]:
        st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
        st.write("Please register first.")
        
        return
        
    else:
            
        uploaded_file1 = st.file_uploader(
            "Upload a facial image to check in",
            type=['png', 'jpg','tiff','jpeg']    )
 
        temp_file1 = NamedTemporaryFile(delete=False)
 
         
        if uploaded_file1:

            temp_file1.write(uploaded_file1.getvalue())
            
            captured_image1 = temp_file1.name
            
            new_image1 = face_recognition.load_image_file(captured_image1)
            
            if face_recognition.face_locations(new_image1)==[]:
                
                st.write("<font color='Red'>Face not identified. Please upload other image.</font>", unsafe_allow_html=True)
                
                return
            
            else:
        
                face_locations = face_recognition.face_locations(new_image1)
                face_encodings = face_recognition.face_encodings(new_image1, face_locations)
                face_names = []
            
                for face_encoding in face_encodings:
         
                    matches = face_recognition.compare_faces(known_face_encodings(), face_encoding)
                
                name = "Unknown Person"
                face_distances = face_recognition.face_distance(known_face_encodings(), face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names()[best_match_index]
            
            
                st.write("")
                st.write(f" {name} is detected.")
            
                st.write("")
                st.write("")
            
                checkIn = st.button("check in")
            
                if checkIn:
                    ct = datetime.now()
                    st.write("You have checked in on : {}".format( ct))
                    
       
                    nameRecord().append(name)
                    timeRecord().append(ct)
            
                    return
 

def initSummaryModule():
        
    
        
    if registerUserInfo()==[]:
        st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
        st.write("Please register first.")

        return 
        
    else:  
            
            
        st.write("")
        st.write("Please insert your name and password")
        
        ####################
        
        st.write("")
        user_name = st.text_input ("User Name", help="The user name you registered before")
    
        if user_name=="":
            st.write("<font color='red'>Key in the User Name</font>", unsafe_allow_html=True)
            
        ####################
        
        st.write("")
        password = st.text_input ("Password", help="The password you registered before", type="password")
    
        if password=="":
            st.write("<font color='red'>Key in the Password</font>", unsafe_allow_html=True)
           
        ####################
                
        confirmEnter = st.button("Enter")
            
  
                
        if confirmEnter:
 
            
            for (name,pwd) in registerUserInfo():
            
                if user_name == name and password == pwd:
                    st.write(pd.DataFrame({'User Name': nameRecord(), 'Checked-in Time': timeRecord()}))
                    return
         
            st.write("Wrong User Name or Password.")
            st.write("Please try again.")
    
            return
            
            
        
def initRegistrationModule():
        
    st.header("Registration")
    st.write("Take note that this prototype demo does not store any info permanently into the server.")
    st.write("Should you feel uncomfortable, please use any cartoon face.")
    st.write("")
    st.write("")

    st.write("Upload Facial Image.")
        
    uploaded_file = st.file_uploader(
        "Upload a facial image to register",
        type=['png', 'jpg','tiff','jpeg']    )
  
   
    temp_file = NamedTemporaryFile(delete=False)
            
    if uploaded_file:

        temp_file.write(uploaded_file.getvalue())
        captured_image = temp_file.name
            
        new_image = face_recognition.load_image_file(captured_image)
           
        if face_recognition.face_locations(new_image)==[]:
                
            st.write("<font color='Red'>Face not identified. Please upload other image.</font>", unsafe_allow_html=True)
            
             
        else:
            
            
        

            st.write("")
            st.write("Please register your name and password")
        
            ####################
        
            st.write("")
            user_name = st.text_input ("User Name", help="Any User Name")
    
            if user_name=="":
                st.write("<font color='red'>Key in the User Name</font>", unsafe_allow_html=True)
            
            ####################
        
            st.write("")
            password1 = st.text_input ("Password", help="Any password. Do not use any real password.", type="password")
    
            if password1=="":
                st.write("<font color='red'>Key in the Password</font>", unsafe_allow_html=True)
           
            ####################
        
            st.write("")
            password2 = st.text_input ("Type Same Password again", help="Same Password.", type="password")
    
            if password2=="":
                st.write("<font color='red'>Key in the Password</font>", unsafe_allow_html=True)
                
            confirmRegistration = st.button("Register")
            
  
                
            if confirmRegistration:
               if password2!=password1:
                    st.write("<font color='red'>Please make sure that the passwords are same.</font>", unsafe_allow_html=True)
                
               else:
                    new_face_encoding = face_recognition.face_encodings(new_image)[0]
                    known_face_encodings().append(new_face_encoding) 
                    known_face_names().append(user_name)
                    registerUserInfo().append((user_name,password1))
            
                    st.write("You have register successfully.")
      

                    
                 
user_choice = st.sidebar.selectbox(
    'Select an Option',
    ('Home','Register', 'Check in', 'View attendance Record','Clear Memory'))

# system = faceRecognitionAttendanceSystem()
if user_choice== 'Register':
    
    initRegistrationModule()

elif user_choice== 'Check in':        


    initCheckInModule()
    
    
elif user_choice== 'View attendance Record':  
    
    initSummaryModule()      
    
elif user_choice== 'Clear Memory':
    clearMemory()

else:
    homeInterface()
                             
    
