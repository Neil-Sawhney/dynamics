
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:59:41 2021
Tutorial on basic Python Programming.
Example used is Jai-Alai-like Launcher

@author: george.sidebotham@cooper.edu
"""

## IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt

## DEFINE INPUT PARAMETERS
g = 9.81   #m/s^2
half_period = 0.1   #sec, time to swing 180 deg (need to measure this)
L = 0.375    #m, stick length
m = 0.0145   #kg, mass of "ball" or "collar" that is launched
r0_ratio = float(input("Enter a ratio r0/L (less than 1):  "))
if r0_ratio >= 1.:
    raise ValueError('Ratio must be less than 1.')

## DERIVED PARAMETERS
r0 = r0_ratio * L    #m, initial position
omega = np.pi/half_period    #rad/sec, angular freq
rpm = omega/2/np.pi * 60   #rev/min      

## DEFINE FUNCTIONS
#NOT NECESSARY/HELPFUL FOR THIS PROBLEM

## DETERMINE SOLUTION
event_time = 1/omega*np.arccosh(L/r0)
theta_launch = omega*event_time  #rad, angle at launch
print("Angle at launch = %.3g deg" %(theta_launch*180/np.pi))
n_points = 20  
t = np.linspace(0,event_time,n_points)
r = r0*np.cosh(omega*t)
vr = omega*(r**2 - r0**2)**0.5
theta = omega*t
v_theta = omega*r
dvr_dt = r0*omega**2*np.cosh(omega*t)
N = m*2*vr*omega    #N, normal force
torque = N*r        #N-m, torque required

#find Cartesian coords after launch
vx = -v_theta*np.sin(theta) + vr*np.cos(theta)
vy = v_theta*np.cos(theta) + vr*np.sin(theta)
print("x component = %.3g m/s, y component = %.3g m/s" %(vx[-1], vy[-1]))
#how far does it travel?
time_to_fall = vy[-1]/g*(1+(1+2*L*np.sin(theta_launch)*g/vy[-1]**2)**0.5)
x_launch = -(vx[-1]*time_to_fall + L*np.cos(theta_launch))
print('Horizontal distance = %.3g m' %x_launch)
launch_angle = 180/np.pi*np.arctan(vy[-1]/-vx[-1])
if launch_angle < 45.:
    print("\nLaunch angle of %.4g deg is too low" %launch_angle)
    print("Enter a higher ratio r0/L next time")
else:
    print("\nLaunch angle of %.4g deg is too high" %launch_angle)
    print("Enter a higher ratio r0/L next time")
        
##PLOT RESULTS
#Figure with r vs theta
fig0 = plt.figure()
ax0 =fig0.add_subplot()
ax0.plot(theta*180/np.pi,r*100)   #Converts angle to deg, r to cm
ax0.set_ylabel("position, r (cm)")
ax0.set_xlabel('Angle (deg)')
ax0.set_ylim(0)
ax0.set_title('Position of Mass vs Angle')

#Figure with dvr/dt, vr and r vs t
fig1 = plt.figure(figsize = (5,8))
ax1 = fig1.add_subplot(311)
ax2 = fig1.add_subplot(312)
ax3 = fig1.add_subplot(313)
ax1.plot(t*1000,dvr_dt/g)
ax1.set_ylabel("Radial 'g force'")
ax1.set_title('Radial Acceleration')
ax1.set_ylim(bottom =0)
ax2.plot(t*1000,vr)
ax2.set_ylabel("vr (m/s)")
ax2.set_ylim(0)
ax2.set_title('Radial Velocity')
ax3.plot(t*1000,r*100)
ax3.set_ylabel("r (cm)")
ax3.set_xlabel("time (ms)")
ax3.set_ylim(0,L*100)
ax3.set_title('Radial Position')
fig1.tight_layout()

#Figure with velocities in Polar Coords (r,theta)
fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(t, vr, label='Radial')
ax.plot(t, v_theta, label='Transverse')
ax.plot(t, (vr**2 + v_theta**2)**0.5, label='Total')
ax.set_xlabel('time (s)')
ax.set_ylabel('Velocity (m/s)')
ax.set_title('Velocities in Polar Coordinates')
ax.legend()

#Figure with velocities in Cartesian Coords (x,y)
fig3 = plt.figure()
ax = fig3.add_subplot()
ax.plot(t, vx, label='x')
ax.plot(t, vy, label='y')
ax.plot(t, (vx**2 + vy**2)**0.5, label='Total')
ax.set_xlabel('time (s)')
ax.set_ylabel('Velocity (m/s)')
ax.set_title('Velocites in Cartesian Coordinates')
ax.legend()

#Figure with normal force (giving Coriolis Accel)) and torque
fig4 = plt.figure()
ax1 = fig4.add_subplot(211)
ax2 = fig4.add_subplot(212)
ax1.plot(t, N/4.448)  #unit conversion 1 lbf = 4.448N
ax1.set_ylabel('Normal Force (lbf)')
ax2.plot(t, torque)
ax2.set_ylabel('Torque (N-m)')
ax2.set_xlabel("time (s)")
ax1.set_title('Normal force and Torque required to maintain omega')
fig4.tight_layout()