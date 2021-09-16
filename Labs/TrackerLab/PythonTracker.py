
# -*- coding: utf-8 -*-
"""
ME 200 Relative Motion Tracking
Workshop 3 
Fall 2021


"""

import numpy as np
import matplotlib.pyplot as plt

#IMPORT DATA
tracker_data = np.genfromtxt('./TrackerData.csv', delimiter = ",", usecols = (0, 1), skip_header= 2)     #Import tracker data into Python
tracker_data = np.nan_to_num(tracker_data, nan=0.0) #Use this line if you use the genfromtxt command 
tracker_data = tracker_data * 1000

tracker_transpose = np.transpose(tracker_data)

# =============================================================================
# print(tracker_data)
# print(tracker_transpose)
# =============================================================================

time = tracker_transpose[0]          #pull out time data from tracker
#tracker_data=tracker_data * -1000 # Convert m to mm and flip x axis; May or may not be necessary depending on how you defined your scale in tracker - BE CAREFUL! 

vicon_data = np.genfromtxt('./A_sawhney_zaretsky.csv', delimiter = ",", skip_header= 1, usecols =(0, 1, 4))  #Import vicon data into Python; pay attention to the size of this compared to the size of the tracker data
vicon_transpose = np.transpose(vicon_data)

#CALCULATIONS
camera_vicon =   vicon_transpose[1]  #camera position from vicon (ground truth)
pencil_vicon = vicon_transpose[2]     #pencil position from vicon (ground truth) - for comparison
pencil_tracker = tracker_transpose[1]   #pencil position from tracker data    

camera_vicon = np.resize(camera_vicon,pencil_tracker.size)
pencil_vicon = np.resize(pencil_vicon,pencil_tracker.size)


pencil_calculated =  camera_vicon - camera_vicon[0] - pencil_tracker + pencil_vicon[0] #calculate absolute pencil position 



# Plot camera position from vicon, pencil position from tracker, and your calculated position
# Plot the pencil aboslute position from vicon as the ground truth
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.title('Relative Motion')
plt.plot(time, camera_vicon, 'bo', label= 'camera_vicon')
plt.plot(time, pencil_tracker, 'go', label= 'pencil_tracker')
plt.plot(time, pencil_calculated, 'co', label= 'pencil_calculated')
plt.xlabel('Time (s)')
plt.ylabel('X Position (mm)')
plt.plot(time, pencil_vicon, 'r*', label= 'ground_truth')
plt.legend(loc='best')  # legend text comes from the plot's label parameter
plt.show()

