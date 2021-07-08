import streamlit as st
from webcam import webcam
from datetime import datetime
import face_recognition
from tempfile import NamedTemporaryFile    
from streamlit_webrtc import (
    ClientSettings,
    VideoTransformerBase,
    WebRtcMode,
    webrtc_streamer)


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
#         st.write("Note: This is a prototype demo. No files will be stored into the cloud.")
#         st.write("Should you feel uncomfortable, please use any cartoon face.")
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("To Rregister a new user, please go to <Section A: Registration> on the left pane.")
#         st.write("To check in, please go to <Section B: Check in> on the left pane.")
#         st.write("To check the attendance record, please go to <Section C: Summary> on the left pane.")
        
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
        return
        
    def initCheckInModule(self):
        temp_file = NamedTemporaryFile(delete=False)
        if self.registrationStatus ==0:
            st.write("<font color='red'>No registration is found</font>", unsafe_allow_html=True)
            st.write("Please register first.")
            st.write("")
           
               
            return
        
        else:
            
            st.write("Stand in front of the camera and register your information.")
            temp_file.write(webcam()) 
        
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
        st.write("Register a new staff info")
        st.write("Take note that this prototype demo does not store any info permanently into the server.")
        st.write("Should you feel uncomfortable, please use any cartoon face.")
        st.write("")
        st.write("")

        st.write("Stand in front of the camera and press the capture button")
        
#         captured_image = webcam()
#         if captured_image is None:
#             st.write("Waiting for capture...")
#         else:
#             st.write("The following image has been captured. ")
#             st.image(captured_image)
            
#         ctx = webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)


        captured_image = []
    
        WEBRTC_CLIENT_SETTINGS = ClientSettings(
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            media_stream_constraints={"video": True, "audio": False},
            )
        
        webrtc_ctx = webrtc_streamer(
            key="loopback",
#             mode=WebRtcMode.SENDONLY,
            mode=WebRtcMode.RECVONLY,
            client_settings=WEBRTC_CLIENT_SETTINGS,
            )

        if webrtc_ctx.video_receiver:
            image_loc = st.empty()
            while True:
            
                try:
                    frame = webrtc_ctx.video_receiver.get_frame(timeout=1)
                except queue.Empty:
                    print("Queue is empty. Stop the loop.")
                    webrtc_ctx.video_receiver.stop()
                    break

                img_rgb = frame.to_ndarray(format="rgb24")
                image_loc.image(img_rgb)
        
                captured_image = img_rgb
        
        
        self.registrationStatus = 0
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
            
                new_image = face_recognition.load_image_file(captured_image)
                new_face_encoding = face_recognition.face_encodings(new_image)[0]
                    
                self.known_face_encodings.append(new_face_encoding) 
                self.known_face_names.append(user_name)
                self.registerUserInfo.append(user_name,password1)
            
                st.write("You have register successfully.")
      
            
                self.registrationStatus = 1
        
        
            return 
    
    
    
    
class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.threshold1 = 100
        self.threshold2 = 200

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        return img



