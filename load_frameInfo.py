import scipy.io as sio
import matlab.engine

def loadInfo(filename, option=2):
  if option == 1:
    eng = matlab.engine.start_matlab()
    eng.MotionBasedMultiObjectTrackingExample(filename, nargout=0)

  mat_contents = sio.loadmat('frameInfo.mat')
  frameInfo = mat_contents['frameInfo'][0]
  frameInfoList = []
  for i in range(len(frameInfo)):
    if len(frameInfo[i]) == 0:
      frameInfoList.append(None)
    else:
      frameInfoList.append(frameInfo[i][1])
  return frameInfoList