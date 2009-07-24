#!/usr/bin/env python

from waveapi import events
from waveapi import model
from waveapi import robot

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("citewave is now monitoring this document")
  
def OnBlipSubmitted(properties, context):
  """Invoked when the document is submitted."""
  root_wavelet = context.GetRootWavelet()
  blip = context.GetBlipById(properties['blipId']) 
  # root_wavelet.GetRootBlipId()
  if not blip.IsRoot():
    return 0
    
  document = blip.GetDocument()
  text = document.GetText()
  
  elements = blip.GetElements()
  annotations = blip.GetAnnotations()

if __name__ == '__main__':
  myRobot = robot.Robot('citewave', 
      #image_url='http://citewave.appspot.com/icon.png',
      version='2',
      profile_url='http://citewave.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
