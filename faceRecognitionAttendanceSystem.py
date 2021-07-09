
import dill

activateFile = 'initFaceRecognitionAttendanceSystemModule.pkl'
infile = open(activateFile,'rb')

initFaceRecognitionAttendanceSystemAIHelper = dill.load(infile)
infile.close()


initFaceRecognitionAttendanceSystemAIHelper()