#!/usr/bin/env python

from waveapi import events
from waveapi import model
from waveapi import robot

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("I'm alive!")

if __name__ == '__main__':
  myRobot = robot.Robot('citewave', 
      #image_url='http://citewave.appspot.com/icon.png',
      version='1',
      profile_url='http://citewave.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.Run()
