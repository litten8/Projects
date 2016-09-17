#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 27 May 2015

###########################################################################
# Copyright (c) 2015 iRobot Corporation
# http://www.irobot.com/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
#
#   Neither the name of iRobot Corporation nor the names
#   of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written
#   permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###########################################################################

from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import time
import struct
import sys, glob # for listing serial ports

try:
    import serial
except ImportError:
    tkinter.messagebox.showerror('Import error', 'Please install pyserial.')
    raise

connection = None

TEXTWIDTH = 40 # window width, in characters
TEXTHEIGHT = 16 # window height, in lines

VELOCITYCHANGE = 200
ROTATIONCHANGE = 300

helpText = """\
Supported Keys:
P\tPassive
S\tSafe
F\tFull
C\tClean
D\tDock
R\tReset
Space\tBeep
Arrows\tMotion

If nothing happens after you connect, try pressing 'P' and then 'S' to get into safe mode.
"""

class TetheredDriveApp(Tk):
    # static variables for keyboard callback -- I know, this is icky
    callbackKeyUp = False
    callbackKeyDown = False
    callbackKeyLeft = False
    callbackKeyRight = False
    callbackKeyLastDriveCommand = ''

    def __init__(self):
        Tk.__init__(self)
        self.title("iRobot Create 2 Tethered Drive")
        self.option_add('*tearOff', FALSE)

        self.menubar = Menu()
        self.configure(menu=self.menubar)

        createMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Create", menu=createMenu)

        createMenu.add_command(label="Connect", command=self.onConnect)
        createMenu.add_command(label="Help", command=self.onHelp)
        createMenu.add_command(label="Quit", command=self.onQuit)

        self.text = Text(self, height = TEXTHEIGHT, width = TEXTWIDTH, wrap = WORD)
        self.scroll = Scrollbar(self, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.text.insert(END, helpText)

        self.bind("<Key>", self.callbackKey)
        self.bind("<KeyRelease>", self.callbackKey)

    # sendCommandASCII takes a string of whitespace-separated, ASCII-encoded base 10 values to send
    def sendCommandASCII(self, command):
        #print ("command1 = ", command)
        cmd = bytearray()
        for v in command.split():
            #print ("v = ", v)
            cmd.append(int(v))
        self.sendCommandRaw(cmd)

    # sendCommandRaw takes a string interpreted as a byte array
    def sendCommandRaw(self, command):
        global connection

        try:
            if connection is not None:
                print ("command = ", command)
                connection.write(command)
            else:
                tkinter.messagebox.showerror('Not connected!', 'Not connected to a robot!')
                print("Not connected.")
        except serial.SerialException:
            print("Lost connection")
            tkinter.messagebox.showinfo('Uh-oh', "Lost connection to the robot!")
            connection = None

        print(' '.join([ str(c) for c in command ]))
        self.text.insert(END, ' '.join([ str(c) for c in command ]))
        self.text.insert(END, '\n')
        self.text.see(END)

    # getDecodedBytes returns a n-byte value decoded using a format string.
    # Whether it blocks is based on how the connection was set up.
    def getDecodedBytes(self, n, fmt):
        global connection
        
        try:
            return struct.unpack(fmt, connection.read(n))[0]
        except serial.SerialException:
            print("Lost connection")
            tkinter.messagebox.showinfo('Uh-oh', "Lost connection to the robot!")
            connection = None
            return None
        except struct.error:
            print("Got unexpected data from serial port.")
            return None

    # get8Unsigned returns an 8-bit unsigned value.
    def get8Unsigned(self):
        return self.getDecodedBytes(1, "B")

    # get8Signed returns an 8-bit signed value.
    def get8Signed(self):
        return self.getDecodedBytes(1, "b")

    # get16Unsigned returns a 16-bit unsigned value.
    def get16Unsigned(self):
        return self.getDecodedBytes(2, ">H")

    # get16Signed returns a 16-bit signed value.
    def get16Signed(self):
        return self.getDecodedBytes(2, ">h")

    # A handler for keyboard events. Feel free to add more!
    def callbackKey(self, event):
        k = event.keysym.upper()
        global upCount #Check if these global variable work
        global downCount
        global leftCount
        global rightCount
        motionChange = False
        if event.type == '2': # KeyPress; need to figure out how to get constant
            if k == 'P':   # Passive
                self.sendCommandASCII('128')
            elif k == 'B': # Safe (
                self.sendCommandASCII('131')
            elif k == 'F': # Full
                self.sendCommandASCII('132')
            elif k == 'C': # Clean
                self.sendCommandASCII('135')
            elif k == 'O': # Dock (We changed it from D to O)
                self.sendCommandASCII('143')
            elif k == 'SPACE': # Beep
                self.sendCommandASCII('140 3 1 64 16 141 3')
            elif k == 'R': # Reset
                self.sendCommandASCII('7')
            elif k == 'UP':
                self.callbackKeyUp = True
                motionChange = True
            elif k == 'DOWN':
                self.callbackKeyDown = True
                motionChange = True
            elif k == 'LEFT':
                self.callbackKeyLeft = True
                motionChange = True
            elif k == 'RIGHT':
                self.callbackKeyRight = True
                motionChange = True
            elif(k == "Q"):
                time.sleep(2)
                self.sendCommandASCII('7')
                time.sleep(3)
                self.sendCommandASCII('128')
                time.sleep(2)
                self.sendCommandASCII('131')
            elif(k == "W"): #Code up second release change
                self.callbackKeyUp = True
                motionChange = True
            elif(k == "A"):
                self.callbackKeyLeft = True
                motionChange = True
            elif(k == "S"):
                self.callbackKeyUp = True
                motionChange = True
            elif(k == "D"):
                self.callbackKeyRight = True
                motionChange = True
            elif(k == "T"):
                self.test()
            else:
                print(repr(k), "not handled")
        elif event.type == '3': # KeyRelease; need to figure out how to get constant
            if k == 'UP': 
                self.callbackKeyUp = False
                motionChange = True
            elif k == 'DOWN':
                self.callbackKeyDown = False
                motionChange = True
            elif k == 'LEFT':
                self.callbackKeyLeft = False
                motionChange = True
            elif k == 'RIGHT':
                self.callbackKeyRight = False
                motionChange = True
            elif k == "W":
                upCount += 1
                if(upCount % 2 == 0):
                    self.callbackKeyUp = False
                    motionChange = True
            elif k == "S":
                downCount += 1
                if(downCount % 2 == 0):
                    self.callbackKeyDown = False
                    motionChange = True
            elif(k == "D"):
                rightCount += 1
                if(rightCount % 2 == 0):
                    self.callbackKeyRight = False
                    motionChange = True
            elif(k == "A"):
                leftCount += 1
                if(leftCount % 2 == 0):
                    self.callbackKeyLeft = False
                    motionChange = True
            
        if motionChange == True:
            velocity = 0
            velocity += VELOCITYCHANGE if self.callbackKeyUp is True else 0
            velocity -= VELOCITYCHANGE if self.callbackKeyDown is True else 0
            rotation = 0
            rotation += ROTATIONCHANGE if self.callbackKeyLeft is True else 0
            rotation -= ROTATIONCHANGE if self.callbackKeyRight is True else 0

            # compute left and right wheel velocities
            vr = velocity + (rotation/2)
            vl = velocity - (rotation/2)

            # create drive command
            vr = velocity + (rotation/2)
            vl = velocity - (rotation/2)
            #print ("vr = ", vr)
            #print ("vl = ", vl)
            cmd = struct.pack(">Bhh", 145, int(vr), int(vl))
            if cmd != self.callbackKeyLastDriveCommand:
                self.sendCommandRaw(cmd)
                self.callbackKeyLastDriveCommand = cmd

    def onConnect(self):
        global connection

        if connection is not None:
            tkinter.messagebox.showinfo('Oops', "You're already connected!")
            return

        try:
            ports = self.getSerialPorts()
            port = tkinter.simpledialog.askstring('Port?', 'Enter COM port to open.\nAvailable options:\n' + '\n'.join(ports))
        except EnvironmentError:
            port = tkinter.simpledialog.askstring('Port?', 'Enter COM port to open.')

        if port is not None:
            print("Trying " + str(port) + "... ")
            try:
                connection = serial.Serial(port, baudrate=115200, timeout=1)
                print("Connected!")
                tkinter.messagebox.showinfo('Connected', "Connection succeeded!")
            except:
                print("Failed.")
                tkinter.messagebox.showinfo('Failed', "Sorry, couldn't connect to " + str(port))


    def onHelp(self):
        tkinter.messagebox.showinfo('Help', helpText)

    def onQuit(self):
        if tkinter.messagebox.askyesno('Really?', 'Are you sure you want to quit?'):
            self.destroy()

    def getSerialPorts(self):
        """Lists serial ports
        From http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of available serial ports
        """
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]

        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this is to exclude your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result    

    def stop(self):
        self.sendCommandASCII('145 0 0 0 0')
 
    def forward(self, speed, seconds):
        cmd = struct.pack(">Bhh", 145, int(speed), int(speed))
        self.sendCommandRaw(cmd)
        time.sleep(seconds)
        self.sendCommandASCII('145 0 0 0 0')

    def rotate(self, speed, seconds):
        cmd = struct.pack(">Bhh", 145, int(speed), int(-speed))
        self.sendCommandRaw(cmd)
        time.sleep(seconds)
        self.sendCommandASCII('145 0 0 0 0')

    def slowRotateLeft(self, speed, seconds):
        cmd = struct.pack(">Bhh", 145, int(speed / 3), int(speed))
        self.sendCommandRaw(cmd)
        time.sleep(seconds)
        self.sendCommandASCII('145 0 0 0 0')

    
    def slowRotateRight(self, speed, seconds):
        cmd = struct.pack(">Bhh", 145, int(speed), int(speed / 3))
        self.sendCommandRaw(cmd)
        time.sleep(seconds)
        self.sendCommandASCII('145 0 0 0 0')

    def test(self):
        while True:
            self.sendCommandASCII('145 0 100 0 100')
            self.getBump()
            self.sendCommandASCII('145 0 0 0 ')
            cmd = struct.pack(">Bhh", 145, int(100), int(-100))
            self.sendCommandRaw(cmd)
    def curveRight(self, speed, seconds):
        cmd = struct.pack(">Bhh", 145, int(speed/1.5), int(speed))
        self.sendCommandRaw(cmd)

    def curveLeft(self, speed, seconds):
        cmd = struct.pack(">Bhh", 145, int(speed), int(speed/1.5))
        self.sendCommandRaw(cmd)        

    def maze(self): #WIP
        while(True):
            again = True
            while(again):
                self.curveLeft(75, 0.5)

    def getBump(self):
        global connection #The buffer is initialized at random.
        connection.flushInput() #Resets the buffer.

        while(True):
            self.sendCommandASCII("142 7") #Reads the bump sensor.
            x = self.get8Unsigned()
            print("Bump is: " + str(x))
            if(x != 0):
                break
        return x

global upCount
upCount = 0
global downCount
downCount = 0
global leftCount
leftCount = 0
global rightCount
rightCount = 0
if __name__ == "__main__":
    app = TetheredDriveApp()
    app.mainloop()

