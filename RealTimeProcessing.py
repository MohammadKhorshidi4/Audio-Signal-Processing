# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:29:48 2021

@author: Mehran Khorshidi
"""
y2=['a']

import pyaudio
import numpy as np
CHUNK = 512
WIDTH = 2
CHANNELS = 1
RATE = 8192
FORMAT = pyaudio.paInt16
data2=np.linspace(0,1,2)
import scipy.io
from scipy import signal
p = pyaudio.PyAudio()
mat = scipy.io.loadmat('FREQUNCIES.mat')
f1209=mat.get('f1209')
f1336=mat.get('f1336')
f1477=mat.get('f1477')
f1633=mat.get('f1633')
f697=mat.get('f697')
f770=mat.get('f770')
f852=mat.get('f852_1')
f941=mat.get('f941')

def signal_processing(x):
    dokmeh=[]
    data1=x
    maxi=max(abs(data1))
    data1=data1/maxi
    f1=signal.lfilter(f1209[0,:],1,data1)
    f2=signal.lfilter(f1336[0,:],1,data1)
    f3=signal.lfilter(f1477[0,:],1,data1)
    f4=signal.lfilter(f1633[0,:],1,data1)
    f5=signal.lfilter(f697[0,:],1,data1)
    f6=signal.lfilter(f770[0,:],1,data1)
    f7=signal.lfilter(f852[0,:],1,data1)
    f8=signal.lfilter(f941[0,:],1,data1)
    Y1=np.fft.fft(f1)
    Y2=np.fft.fft(f2)
    Y3=np.fft.fft(f3)
    Y4=np.fft.fft(f4)
    Y5=np.fft.fft(f5)
    Y6=np.fft.fft(f6)
    Y7=np.fft.fft(f7)
    Y8=np.fft.fft(f8)
    L1=len(Y1)
    L2=len(Y2)
    L3=len(Y3)
    L4=len(Y4)
    L5=len(Y5)
    L6=len(Y6)
    L7=len(Y7)
    L8=len(Y8)
    P1 = abs(Y1/L1)
    P2 = abs(Y2/L2)
    P3 = abs(Y3/L3)
    P4 = abs(Y4/L4)
    P5 = abs(Y5/L5)
    P6 = abs(Y6/L6)
    P7 = abs(Y7/L7)
    P8 = abs(Y8/L8)
    col=[max(P1),max(P2),max(P3),max(P4)]
    row=[max(P5),max(P6),max(P7),max(P8)]
    mmco=max(col)
    mmro=max(row)
    if mmco>0.02 and mmro>0.02:
        mcol = col.index(mmco)         
        mrow = row.index(mmro)
        if mcol==0 and mrow==0:
            dokmeh=dokmeh+['1']
        elif mcol==0 and mrow==1:
            dokmeh=dokmeh+['4']
        elif mcol==0 and mrow==2:
            dokmeh=dokmeh+['7']
        elif mcol==0 and mrow==3:
            dokmeh=dokmeh+['*']
        elif mcol==1 and mrow==0:
            dokmeh=dokmeh+['2']
        elif mcol==1 and mrow==1:
            dokmeh=dokmeh+['5']
        elif mcol==1 and mrow==2:
            dokmeh=dokmeh+['8']
        elif mcol==1 and mrow==3:
            dokmeh=dokmeh+['0']
        elif mcol==2 and mrow==0:
            dokmeh=dokmeh+['3']
        elif mcol==2 and mrow==1:
            dokmeh=dokmeh+['6']
        elif mcol==2 and mrow==2:
            dokmeh=dokmeh+['9']
        elif mcol==2 and mrow==3:
            dokmeh=dokmeh+['#']
        elif mcol==3 and mrow==0:
            dokmeh=dokmeh+['A']
        elif mcol==3 and mrow==1:
            dokmeh=dokmeh+['B']
        elif mcol==3 and mrow==2:
            dokmeh=dokmeh+['C']
        elif mcol==3 and mrow==3:
            dokmeh=dokmeh+['D']
    else:
        dokmeh=dokmeh+['Nothing']
    return dokmeh


stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

stream.start_stream()

try:
    while True:
        y2=signal_processing(data2)
        data=stream.read(CHUNK)
        x=np.frombuffer(data,dtype=np.int16)
        data2=x
        y=signal_processing(x)
        if y[0]=='Nothing':
            y[0]=y2[0]
        if y!=y2:
            print(y)
        #stream.write(y)
except KeyboardInterrupt: 
    pass


    
stream.stop_stream()
stream.close()

p.terminate()