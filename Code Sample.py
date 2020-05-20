# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:44:37 2020

@author: hdb3uc
"""

import matplotlib.pyplot as plt
import numpy as np

import CoolProp.CoolProp as cp

# solving a complex rankine cycle for fixed mass flow to water heater
fl = 'water'
# state 1
P1 = 200e5
T1 = 923.15
H1 = cp.PropsSI('H','P',P1,'T',T1, fl)
S1 = cp.PropsSI('S','P',P1,'T',T1, fl)
#state 3
P3 = 60e5
T3 = 943.15
H3 = cp.PropsSI('H','P',P3,'T',T3, fl)
S3 = cp.PropsSI('S','P',P3,'T',T3, fl)
#state 2
P2 = 60e5
H2s = cp.PropsSI('H','P',P2,'S',S1, fl)
H2 = (H2s-H1)*(0.92)+H1
T2 = cp.PropsSI('T','P',P2,'H',H2, fl)
S2 = cp.PropsSI('S','P',P2,'H',H2, fl)
#state 4
P4 = 15e5
H4s = cp.PropsSI('H','P',P4,'S',S3, fl)
H4 = (H4s-H3)*(0.92)+H3
T4 = cp.PropsSI('T','P',P4,'H',H4, fl)
S4 = cp.PropsSI('S','P',P4,'H',H4, fl)
#state 8
P8 = 60e5
Tsat8 = cp.PropsSI('T','P',P8,'Q',0, fl)
T8 = Tsat8 + 25
H8 = cp.PropsSI('H','P',P8,'T',T8, fl)
S8 = cp.PropsSI('S','P',P8,'T',T8, fl)
#state 9
P9 = 15e5
H9 = H8
T9 = cp.PropsSI('T','P',P9,'H',H9, fl)
S9 = cp.PropsSI('S','P',P9,'H',H9, fl)
#state 6
P6 = 0.2e5
T6 = cp.PropsSI('T','P',P6,'Q',0, fl)
S6 = cp.PropsSI('S','P',P6,'Q',0, fl)
H6 = cp.PropsSI('H','P',P6,'Q',0, fl)
#state 7
P7 = 15e5
H7s = cp.PropsSI('H','P',P7,'S',S6, fl)
H7 = (H7s-H6)/(0.92)+H6
T7 = cp.PropsSI('T','P',P7,'H',H7, fl)
S7 = cp.PropsSI('S','P',P7,'H',H7, fl)
#state 5
P5 = 0.2e5
H5s = cp.PropsSI('H','P',P5,'S',S4, fl)
H5 = (H5s-H4)*(0.92)+H4
T5 = cp.PropsSI('T','P',P5,'H',H5, fl)
S5 = cp.PropsSI('S','P',P5,'H',H5, fl)
#state 10
P10 = 15e5
H10 = (65*H4+410*H7+25*H9)/500
T10 = cp.PropsSI('T','P',P10,'H',H10, fl)
S10 = cp.PropsSI('S','P',P10,'H',H10, fl)
#state 11
P11 = 200e5
H11s = cp.PropsSI('H','P',P11,'S',S10, fl)
H11 = (H11s-H10)/(0.92)+H10
T11 = cp.PropsSI('T','P',P11,'H',H11, fl)
S11 = cp.PropsSI('S','P',P11,'H',H11, fl)
#state 12
P12 = 200e5
H12 = (25*(H2-H8))/500 + H11
T12 = cp.PropsSI('T','P',P12,'H',H12, fl)
S12 = cp.PropsSI('S','P',P12,'H',H12, fl)

#vapor dome
tcrit = cp.PropsSI('Tcrit',fl)
nump = 200
t_array = np.linspace(274,tcrit,nump)

sLiq = np.empty(nump)
sVap = np.empty(nump)
for (i,t) in enumerate(t_array):
        sLiq[i]=cp.PropsSI('S','T',t,'Q', 0, fl)
        sVap[i]=cp.PropsSI('S','T',t,'Q', 1, fl)
            
plt.plot(sLiq/1000,t_array,'k:', linewidth=2)
plt.plot(sVap/1000,t_array,'k:', linewidth=2)

# isobars
s_array1 = np.linspace(0,7e3,nump)
s_array2 = np.linspace(0,7.8e3,nump)
s_array3 = np.linspace(0,8.3e3,nump)
s_array4 = np.linspace(0,8.6e3,nump)
p200 = np.empty(nump)
p60 = np.empty(nump)
p15 = np.empty(nump)
p02 = np.empty(nump)

for (i,s) in enumerate(s_array1):
    p200[i]= cp.PropsSI('T','P',200e5,'S',s, fl)
    
for (i,s) in enumerate(s_array2):
    p60[i]= cp.PropsSI('T','P',60e5,'S',s, fl)
    
for (i,s) in enumerate(s_array3):
    p15[i]= cp.PropsSI('T','P',15e5,'S',s, fl)
    
for (i,s) in enumerate(s_array4):
    p02[i]= cp.PropsSI('T','P',0.2e5,'S',s, fl)
    
plt.plot(s_array1/1000,p200, c = 'lightblue', linewidth = 2)
plt.plot(s_array2/1000,p60, c = 'lightblue', linewidth = 2)
plt.plot(s_array3/1000,p15, c = 'lightblue', linewidth = 2)
plt.plot(s_array4/1000,p02, c = 'lightblue', linewidth = 2)

plt.plot(S1/1000,T1,'*',c = 'cornflowerblue',markersize=10)
plt.text((S1-400)/1000, T1-50, '1')
plt.plot(S2/1000,T2,'*',c = 'cornflowerblue',markersize=10)
plt.text((S2-400)/1000, T2-50, '2')
plt.plot(S3/1000,T3,'*',c = 'cornflowerblue',markersize=10)
plt.text((S3+400)/1000, T3-50, '3')
plt.plot(S4/1000,T4,'*',c = 'cornflowerblue',markersize=10)
plt.text((S4+400)/1000, T4-50, '4')
plt.plot(S5/1000,T5,'*',c = 'cornflowerblue',markersize=10)
plt.text((S5-400)/1000, T5-50, '5')
plt.plot(S6/1000,T6,'*',c = 'cornflowerblue',markersize=10)
plt.plot(S7/1000,T7,'*',c = 'cornflowerblue',markersize=10)
plt.text((S7)/1000, T7-50, '6 / 7')
plt.plot(S8/1000,T8,'*',c = 'cornflowerblue',markersize=10)
plt.text((S8-500)/1000, T8-50, '8')
plt.plot(S9/1000,T9,'*',c = 'cornflowerblue',markersize=10)
plt.text((S9+400)/1000, T9-50, '9')
plt.plot(S10/1000,T10,'*',c = 'cornflowerblue',markersize=10)
plt.plot(S11/1000,T11,'*',c = 'cornflowerblue',markersize=10)
plt.plot(S12/1000,T12,'*',c = 'cornflowerblue',markersize=10)
plt.text((S11-1500)/1000, T11+50, '10 / 11 / 12')


plt.xlabel('Specific Entropy (kJ/kg/K)')
plt.ylabel('Temperature (K)')
plt.grid()

plt.title('Temperature Specific Entropy Diagram \n for Reheat and Regeneration Rankine Cycle')
plt.text(4.5,950, 'P = 200 bar')
plt.text(6,1090, 'P = 60 bar')
plt.text(7.9,800, 'P = 15 bar')
plt.text(7.8,525, 'P = 0.2 bar')

Qin12_1 = 500*(H1-H12)
Qin2_3 = 475*(H3-H2)
NetQin = Qin12_1+Qin2_3
#Work out
Wout1_2 = 500*(H1-H2)
Wout3_4 = 475*(H3-H4)
Wout4_5 = (410*(H4-H5))
NetWout = Wout1_2 + Wout3_4 + Wout4_5
#Work in 
Win6_7 = (410)*(H7-H6)
Win10_11 = 500*(H11-H10)
NetWin = Win6_7 + Win10_11
#final answer
NetWork = (NetWout - NetWin)/1000
n = (NetWout-NetWin)/NetQin

# varriation of efficiency with mass flow rate to open feed waterheater 

m4b_array = np.linspace(0.01*500,0.21*500,50)
NetWork = np.empty(50)
n = np.empty(50)
for (i,m4b) in enumerate(m4b_array):
    m4b = m4b
    m4a = m7 = 475 - m4b
    m9 = 25
    #state 10
    P10 = 15e5
    H10 = (m4b*H4+m7*H7+m9*H9)/500
    T10 = cp.PropsSI('T','P',P10,'H',H10, fl)
    S10 = cp.PropsSI('S','P',P10,'H',H10, fl)
    #state 11
    P11 = 200e5
    H11s = cp.PropsSI('H','P',P11,'S',S10, fl)
    H11 = (H11s-H10)/(0.92)+H10
    T11 = cp.PropsSI('T','P',P11,'H',H11, fl)
    S11 = cp.PropsSI('S','P',P11,'H',H11, fl)
    #state 12
    P12 = 200e5
    H12 = (25*(H2-H8))/500 + H11
    T12 = cp.PropsSI('T','P',P12,'H',H12, fl)
    S12 = cp.PropsSI('S','P',P12,'H',H12, fl)
    #Qin
    Qin12_1 = 500*(H1-H12)
    Qin2_3 = 475*(H3-H2)
    NetQin = Qin12_1+Qin2_3
    #Work out
    Wout1_2 = 500*(H1-H2)
    Wout3_4 = 475*(H3-H4)
    Wout4_5 = (m4a)*(H4-H5)
    NetWout = Wout1_2+Wout3_4+Wout4_5
    #Work in 
    Win6_7 = (m7)*(H7-H6)
    Win10_11 = 500*(H11-H10)
    NetWin = Win6_7 + Win10_11
    #final answer
    NetWork[i] = (NetWout - NetWin)/1000
    n[i] = (NetWout-NetWin)/NetQin
    
f1 = plt.figure()
plt.plot(m4b_array,NetWork,'r-', linewidth=2)
plt.xlabel('Mass Flow Rate at State 4a (kg/s)')
plt.ylabel('Net Work (KW)')
plt.title('Effect of Varrying Mass Flow Rate into Open Feedwater Heater \n on Net Work for the Cycle')
plt.grid()
f2 = plt.figure()
plt.plot(m4b_array,n,'r-', linewidth=2)
plt.xlabel('Mass Flow Rate at State 4a (kg/s)')
plt.ylabel('Efficiency')
plt.title('Effect of Varrying Mass Flow Rate into Open Feedwater Heater \n on Thermal Efficiency for the Cycle')
plt.grid()
plt.show()
