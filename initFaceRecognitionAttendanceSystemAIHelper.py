import streamlit as st
from datetime import datetime
import face_recognition
from tempfile import NamedTemporaryFile    


class faceRecognitionAttendanceSystem:

    
    
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.registerUserInfo = []
        self.registrationStatus = 0

        self.attendanceRecord = []
        self.face_encodings = []
        self.face_names = []
   
        
    def clearMemory(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.registerUserInfo = []
        self.registrationStatus = 0


        self.attendanceRecord = []
        self.face_encodings = []
        self.face_names = []   
        
        
        return
        
    def homeInterface(self):

#         self.registrationStatus = 0
#         self.user_choice = []
        st.title("Welcome to RICHIEYYPTUTORIALPAGE Face Recognition Attendance System")
        
        readme = st.checkbox('Read Me.')

        if readme:
 
            st.write("For demo + privacy reason, it uses file uploading widget instead real-time webcam recording. ")
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
            
            self.clearMemory()
            
        
        return
        
    def initCheckInModule(self):
        temp_file = NamedTemporaryFile(delete=False)
        
        if self.registrationStatus ==0:
            st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
            st.write("Please register first.")
            st.write("")
           
               
            return
        
        else:
            
            uploaded_file = st.file_uploader(
            "Upload a facial image",
            type=['png', 'jpg','tiff','jpeg']    )
 
            temp_file = NamedTemporaryFile(delete=False)
            
            if uploaded_file:

                temp_file.write(uploaded_file.getvalue())
        
                face_locations = face_recognition.face_locations(temp_file.name)
                face_encodings = face_recognition.face_encodings(temp_file.name, face_locations)
                face_names = []
            
                for face_encoding in face_encodings:
         
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown Person"
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
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
                    self.attendanceRecord.append = [(name,ct)]
            
 
                
                    return 

    def initSummaryModule(self):
        
        
        if self.registrationStatus ==0:
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
 
            
                for (name,pwd) in self.registerUserInfo:
            
                    if user_name == name and password == pwd:
                        st.write(self.registerUserInfo)
                    
                st.write("Wrong User Name or Password.")
                st.write("Please try again.")
    
   
        
    def initRegistrationModule(self):
        
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
                
                st.write("face not identified")
             
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
            
                        self.known_face_encodings.append(new_face_encoding) 
                        self.known_face_names.append(user_name)
                        self.registerUserInfo.append(user_name,password1)
            
                        st.write("You have register successfully.")
      
            
                        self.registrationStatus = 1
        
        
                        return 
    
    


