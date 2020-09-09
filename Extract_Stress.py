# 2 June 2020
# Jacob Rusch
# Extract_Stress

# This script was made with the help of ABAQUS Macros ('File- Macro Manager')
# Need to open the .odb file in the directory you wish to run the script in.
# i.e. don't open ABAQUS from your main desktop and search for the file, 
#      (if using windows) double click on the odb file in the folder it is in
#      (if using linux) left click in the folder and open cmd and open abaqus
#      from there.
#
# ------------------------------------------------------------------------------
# Brief description for using Macros adapted from:
# (Yun Peng, PhD, Massachusetts General # Hospital/ Harvard Medical School)
#
# 1. Create a new macro and start recording ('File- Macro Manager')
# 2. Perform operations you want in GUI (e.g., save field output, create model, etc.)
# 3. Finish recording and go to your current working directory, open the newly created
#    python macro file
# 4. This macro actually creates a user-defined function, you can delete this declaration
#    and just keep the codes in the defined function (pay attention to the identations!)
# 5. Modify the codes as you wish, for example, add for loops, make your own file names..
# 6. Save the file, and go to Abaqus ->File->Run Script, run your code

from odbAccess import *
from abaqusConstants import *
import __main__
import math
import datetime
import visualization
import xyPlot
import displayGroupOdbToolset as dgo

# Input and ouput file names (i.e. Name of Job and Variable to appear in text file)
InputName='0_90_90_Angles'
OutName='S'

# ODB = Output Database file
print 'ODB = ' + InputName
print 'Output Variable = ' + OutName

# file name that will appear in the working directory after the script is run in ABAQUS
outputfilename=InputName+'-'+str(OutName)+'-'+ str('S33')+'.txt'

session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)

# opend .odb file to read from
odb = openOdb(InputName+'.odb')

# saving the desired field output data at the gauss points of the entire element
# Change last input to [NAME OF PART].[NAME OF NODE SET]
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
        variable=(('S', INTEGRATION_POINT, ((COMPONENT, 'S33'), )), ), 
        elementSets=("PART-1-1.SET-1", ))

xyp = session.XYPlot('XYPlot-2')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
x0 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 1']
x1 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 2']
x2 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 3']
x3 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 4']
x4 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 5']
x5 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 6']
x6 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 7']
x7 = session.xyDataObjects['_S:S33 PI: PART-1-1 E: 1 IP: 8']

# Output the time vs velocity data to a text file
session.writeXYReport(fileName=outputfilename, xyData=(x0, x1, x2, x3, x4, 
    x5, x6, x7))

# close input and output files
# odb.close()
