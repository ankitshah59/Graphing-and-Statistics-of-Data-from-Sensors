#!/usr/bin/env python
# coding: utf-8

# In[42]:


#!/usr/bin/env python
# coding: utf-8

# In[50]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from decimal import Decimal
'''
X, Y , Z, A = [], [] , [] ,[]
for line in open('/Users/ankitshah/Desktop/SWOTA_WORKING/test.txt', 'r'):
values = [float(s) for s in line.split()]
X.append(values[0])
Y.append(values[1])
Z.append(values[2])
A.append(values[3])'''

fileName = str(input('ENTER FILE PATHNAME: '))
pdfInput = str(input('ENTER FILENAME YOU WANT TO SAVE: '))
pdfName = pdfInput+'.pdf'
txtName = pdfInput+'.txt'

with PdfPages(pdfName) as pdf:
    X,Y,Z,A,B,C =np.loadtxt(fileName, delimiter=',', unpack =True)

    plt.plot( X,Y, color='g',label ='X axis')
    plt.plot( X,Z, color='r',label ='Y axis')
    plt.plot(X,A, color='b', label = 'Z axis')
    
    #plt.plot(X,B, color='y', label = 'thrust')

    plt.xlabel('Time(s)')
    plt.ylabel('Data')
    plt.title('Pedicle Probe Data')
    plt.legend()
    pdf.savefig()
    plt.show()


    X,Y,Z,A,B,C =np.loadtxt(fileName, delimiter=',', unpack =True)

    
    '''plt.plot( X,Y, color='g',label ='X axis')
    plt.plot( X,Z, color='r',label ='Y axis')
    plt.plot(X,A, color='b', label = 'Z axis')'''
    plt.plot(X,B, color='b', label = 'Thrust/ N')

    
    plt.xlabel('Time')
    plt.ylabel('Thrust')
    plt.title('Pedicle Probe Data')
    plt.legend()
    pdf.savefig() 
    plt.show()
    
    meanTh =  str(round(np.mean(B),3))
    stdevTh = str(round(np.std(B),3))
    MinTh = str(round(max(B),2))
    MaxTh = str(round(min(B),2))
    print("Max Value is: " + MaxTh + " | Min Value is: " + MinTh)
    print("Mean Thrust is: " + meanTh)
    print("Standard Deviation of Thrust is: " + stdevTh)
    
    X,Y,Z,A,B,C =np.loadtxt(fileName, delimiter=',', unpack =True)

    '''plt.plot( X,Y, color='g',label ='X axis')
    plt.plot( X,Z, color='r',label ='Y axis')
    plt.plot(X,A, color='b', label = 'Z axis')'''
    plt.plot(X,C, color='blue', label = 'Torque/ N')

    plt.xlabel('Time')
    plt.ylabel('Torque')
    plt.title('Pedicle Probe Data')
    plt.legend()
    pdf.savefig()
    plt.show()

    meanTo = str(round(np.mean(C),3))
    stdevTo = str(round(np.std(C),3))
    MinTo = str(round(max(C),2))
    MaxTo = str(round(min(C),2))
    
    print("Max Value is: " + MaxTo + " | Min Value is: " + MinTo)
    print("Mean Torque is: " + meanTo)
    print("Standard Deviation of Torque is: " + stdevTo)
    
    a = open(txtName, 'w')
    
    a.write("Max Value of Thrust is: " + MaxTh + " | Min Value of Thrust is: " + MinTh +"\n" +
    "Mean Thrust is: " + meanTh +"\n"+
    "Standard Deviation of Thrust is: " + stdevTh + "\n")
    
    a.write("\n"+"Max Value of Torque is: " + MaxTo + " | Min Value of Torque is: " + MinTo +"\n" +
    "Mean Torque is: " + meanTo +"\n"+
    "Standard Deviation of Torque is: " + stdevTo)
    a.close()


# In[ ]:





# In[ ]:




