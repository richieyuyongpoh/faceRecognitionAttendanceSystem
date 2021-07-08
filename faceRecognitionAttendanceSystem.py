import streamlit as st 

import face_recognition
from datetime import datetime
from tempfile import NamedTemporaryFile  
import pandas as pd


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
def attendanceRecord():
    return []


attendanceRecord()
        
        
def clearMemory():
    known_face_encodings().clear()
    known_face_names().clear()
    registerUserInfo().clear()
    attendanceRecord()
        
        
def homeInterface():



    st.title("Welcome to RICHIEYYPTUTORIALPAGE Face Recognition Attendance System")
        
    readme = st.checkbox('Read Me.')

    if readme:
 
        st.write("For demo + privacy reason, it uses file upload widget instead real-time offline/local webcam recording. ")
        st.write("Take note that this prototype demo does not store any info permanently into the server.")
        st.write("Should you feel uncomfortable to u, please use any cartoon face.")
    st.write("")
    st.write("")
    st.write("")

        
    st.write ("For more info, please contact:")
    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)
    st.write("")
    st.write("")        
        
    st.write("To clear the registration and attendance records, press CLEAR button below.")
    st.write("")
    st.write("") 
        
    clear = st.button("CLEAR")
        
    if clear:
            
        st.write("<font color='Aquamarine'>Memory has been cleared</font>", unsafe_allow_html=True)
            
        clearMemory()
            
    return    
 
        
        
        
def initCheckInModule():
        
    if registerUserInfo() ==[]:
        st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
        st.write("Please register first.")
        
        return
        
    else:
            
        uploaded_file1 = st.file_uploader(
            "Upload a facial image",
            type=['png', 'jpg','tiff','jpeg']    )
 
        temp_file1 = NamedTemporaryFile(delete=False)
 
            
        if uploaded_file1:

            temp_file1.write(uploaded_file1.getvalue())
            
            captured1_image = temp_file1.name
            
            new_image1 = face_recognition.load_image_file(captured_image1)
            
            if face_recognition.face_locations(new_image1)==[]:
                
                st.write("<font color='Red'>Face not identified. Please upload other image.</font>", unsafe_allow_html=True)
                
                return
            
            else:
        
                face_locations = face_recognition.face_locations(captured_image1)
                face_encodings = face_recognition.face_encodings(captured_image1, face_locations)
                face_names = []
            
                for face_encoding in face_encodings:
         
                    matches = face_recognition.compare_faces(known_face_encodings(), face_encoding)
                
                name = "Unknown Person"
                face_distances = face_recognition.face_distance(known_face_encodings(), face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
            
            
                st.write("")
                st.write(" {} is detected.")
            
                st.write("")
                st.write("")
            
                checkIn = st.button("check in")
            
                if checkIn:
                    ct = datetime.datetime.now()
                    st.write("You have checked in on : {}".format( ct))
                    attendanceRecord().append = [{'User Name':name},{'Checked-In Time':ct]
            
 

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
        user_name = st.text_input ("User Name", value="The user name you registered before")
    
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
                    st.write(pd.DataFrame(attendanceRecord()))
                    return
         
            st.write("Wrong User Name or Password.")
            st.write("Please try again.")
    
   
            
            
        
def initRegistrationModule():
        
    st.header("Registration")
    st.write("Take note that this prototype demo does not store any info permanently into the server.")
    st.write("Should you feel uncomfortable, please use any cartoon face.")
    st.write("")
    st.write("")

    st.write("Upload Facial Image.")
        
    uploaded_file = st.file_uploader(
        "Upload a facial image",
        type=['png', 'jpg','tiff','jpeg']    )
  
   
    temp_file = NamedTemporaryFile(delete=False)
            
    if uploaded_file:

        temp_file.write(uploaded_file.getvalue())
        captured_image = temp_file.name
            
        new_image = face_recognition.load_image_file(captured_image)
           
        if face_recognition.face_locations(new_image)==[]:
                
            st.write("<font color='Red'>Face not identified. Please upload other image.</font>", unsafe_allow_html=True)
            
             
        else:
            
            new_face_encoding = face_recognition.face_encodings(new_image)[0]
        

            st.write("")
            st.write("Please register your name and password")
        
            ####################
        
            st.write("")
            user_name = st.text_input ("User Name", value="Any User Name")
    
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
            
                    known_face_encodings().append(new_face_encoding) 
                    known_face_names().append(user_name)
                    registerUserInfo().append((user_name,password1))
            
                    st.write("You have register successfully.")
      

                    
                 
user_choice = st.sidebar.selectbox(
    'Select an Option',
    ('Home','Register', 'Check in', 'View attendance Record'))

# system = faceRecognitionAttendanceSystem()
if user_choice== 'Register':
    
    initRegistrationModule()

elif user_choice== 'Check in':        


    initCheckInModule()
    
    
elif user_choice== 'View attendance Record':  
    
    initSummaryModule()        

else:
    homeInterface()
                             
    


































# import streamlit as st 
# from initFaceRecognitionAttendanceSystemAIHelper import faceRecognitionAttendanceSystem 
# import face_recognition
# from datetime import datetime
# from tempfile import NamedTemporaryFile    
# # from streamlit_webrtc import webrtc_streamer







# class faceRecognitionAttendanceSystem:

#     def __init__(self):
#         self.known_face_encodings = []
#         self.known_face_names = []
#         self.registerUserInfo = []
# #         self.registrationStatus = 0

#         self.attendanceRecord = []
#         self.face_encodings = []
#         self.face_names = []
   
        
#     def clearMemory(self):
#         self.known_face_encodings = []
#         self.known_face_names = []
#         self.registerUserInfo = []
# #         self.registrationStatus = 0


#         self.attendanceRecord = []
#         self.face_encodings = []
#         self.face_names = []   
        
        
#         return
        
#     def homeInterface(self):

# #         self.registrationStatus = 0
# #         self.user_choice = []
#         st.title("Welcome to RICHIEYYPTUTORIALPAGE Face Recognition Attendance System")
        
#         readme = st.checkbox('Read Me.')

#         if readme:
 
#             st.write("For demo + privacy reason, it uses file upload widget instead real-time offline/local webcam recording. ")
#             st.write("Take note that this prototype demo does not store any info permanently into the server.")
#             st.write("Should you feel uncomfortable to u, please use any cartoon face.")
#         st.write("")
#         st.write("")
#         st.write("")

        
#         st.write ("For more info, please contact:")
#         st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)
#         st.write("")
#         st.write("")        
        
#         st.write("To clear the registration and attendance records, press CLEAR button below.")
#         st.write("")
#         st.write("") 
        
#         clear = st.button("CLEAR")
        
#         if clear:
            
#             st.write("<font color='Aquamarine'>Memory has been cleared</font>", unsafe_allow_html=True)
            
#             self.clearMemory()
            
        
#         return
        
#     def initCheckInModule(self):
#         temp_file = NamedTemporaryFile(delete=False)
        
#         if self.registrationStatus ==0:
#             st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
#             st.write("Please register first.")
#             st.write("")
           
               
#             return
        
#         else:
            
#             uploaded_file = st.file_uploader(
#             "Upload a facial image",
#             type=['png', 'jpg','tiff','jpeg']    )
 
#             temp_file = NamedTemporaryFile(delete=False)
            
#             if uploaded_file:

#                 temp_file.write(uploaded_file.getvalue())
        
#                 face_locations = face_recognition.face_locations(temp_file.name)
#                 face_encodings = face_recognition.face_encodings(temp_file.name, face_locations)
#                 face_names = []
            
#                 for face_encoding in face_encodings:
         
#                     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                 name = "Unknown Person"
#                 face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#                 best_match_index = np.argmin(face_distances)
#                 if matches[best_match_index]:
#                     name = known_face_names[best_match_index]
            
            
#                 st.write("")
#                 st.write(" {} is detected.")
            
#                 st.write("")
#                 st.write("")
            
#                 checkIn = st.button("check in")
            
#                 if checkIn:
#                     ct = datetime.datetime.now()
#                     st.write("You have checked in on : {}".format( ct))
#                     self.attendanceRecord.append = [(name,ct)]
            
 
                
#                     return 

#     def initSummaryModule(self):
        
#         st.write(self.registerUserInfo)
        
#         if self.registerUserInfo==[]:
#             st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
#             st.write("Please register first.")

#             return 
        
#         else:  
            
            
#             st.write("")
#             st.write("Please insert your name and password")
        
#             ####################
        
#             st.write("")
#             user_name = st.text_input ("User Name", value="The user name you registered before")
    
#             if user_name=="":
#                 st.write("<font color='red'>Key in the User Name</font>", unsafe_allow_html=True)
            
#             ####################
        
#             st.write("")
#             password = st.text_input ("Password", help="The password you registered before", type="password")
    
#             if password=="":
#                 st.write("<font color='red'>Key in the Password</font>", unsafe_allow_html=True)
           
#             ####################
                
#             confirmEnter = st.button("Enter")
            
  
                
#             if confirmEnter:
 
            
#                 for (name,pwd) in self.registerUserInfo:
            
#                     if user_name == name and password == pwd:
#                         st.write(self.registerUserInfo)
                    
#                 st.write("Wrong User Name or Password.")
#                 st.write("Please try again.")
    
   
        
#     def initRegistrationModule(self):
        
#         st.header("Registration")
#         st.write("Take note that this prototype demo does not store any info permanently into the server.")
#         st.write("Should you feel uncomfortable, please use any cartoon face.")
#         st.write("")
#         st.write("")

#         st.write("Upload Facial Image.")
        
#         uploaded_file = st.file_uploader(
#             "Upload a facial image",
#             type=['png', 'jpg','tiff','jpeg']    )
 
#         temp_file = NamedTemporaryFile(delete=False)
            
#         if uploaded_file:

#             temp_file.write(uploaded_file.getvalue())
#             captured_image = temp_file.name
            
#             new_image = face_recognition.load_image_file(captured_image)
           
#             if face_recognition.face_locations(new_image)==[]:
                
#                 st.write("<font color='Red'>Face not identified. Please upload other image.</font>", unsafe_allow_html=True)
            
             
#             else:
            
#                 new_face_encoding = face_recognition.face_encodings(new_image)[0]
        

#                 st.write("")
#                 st.write("Please register your name and password")
        
#                 ####################
        
#                 st.write("")
#                 user_name = st.text_input ("User Name", value="Any User Name")
    
#                 if user_name=="":
#                     st.write("<font color='red'>Key in the User Name</font>", unsafe_allow_html=True)
            
#                 ####################
        
#                 st.write("")
#                 password1 = st.text_input ("Password", help="Any password. Do not use any real password.", type="password")
    
#                 if password1=="":
#                     st.write("<font color='red'>Key in the Password</font>", unsafe_allow_html=True)
           
#                 ####################
        
#                 st.write("")
#                 password2 = st.text_input ("Type Same Password again", help="Same Password.", type="password")
    
#                 if password2=="":
#                     st.write("<font color='red'>Key in the Password</font>", unsafe_allow_html=True)
                
#                 confirmRegistration = st.button("Register")
            
  
                
#                 if confirmRegistration:
#                     if password2!=password1:
#                         st.write("<font color='red'>Please make sure that the passwords are same.</font>", unsafe_allow_html=True)
                
#                     else:
            
#                         self.known_face_encodings.append(new_face_encoding) 
#                         self.known_face_names.append(user_name)
#                         self.registerUserInfo.append((user_name,password1))
            
#                         st.write("You have register successfully.")
      
#                         st.write(self.registerUserInfo)
                      
    
    


























# system = faceRecognitionAttendanceSystem()


# user_choice = st.sidebar.selectbox(
#     'Select an Option',
#     ('Home','Register', 'Check in', 'View attendance Record'))

# # system = faceRecognitionAttendanceSystem()
# if user_choice== 'Register':
    
#     system.initRegistrationModule()

# elif user_choice== 'Check in':        


#     system.initCheckInModule()
    
    
# elif user_choice== 'View attendance Record':  
    
#     system.initSummaryModule()        

# else:
#     system.homeInterface()
        
