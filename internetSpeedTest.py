# GitHub: github.com/massif-py
# Author: Gabriel Anaya Delgado

import os
import time
import turtle
import random
import socket
import requests
import speedtest

#Username, IPv4 and IPv6.
usr = os.getlogin()
hostName = socket.gethostname()
IPv4 = socket.gethostbyname(hostName)
IPv6 = requests.get('https://checkip.amazonaws.com')

#Initial screen values.
s = turtle.Screen()
s.setup(450, 570)
s.cv._rootwindow.resizable(False, False)
s.title('Internet Speed Test')
p = turtle.Turtle()
p.hideturtle()

#Loading screen.
p.up()
p.goto(-80, 0)
p.write('𝗟𝗢𝗔𝗗𝗜𝗡𝗚...', font = ('Calibri', 30, 'normal'))
p.goto(-83, -18)
p.write('Internet Speed Test', font = ('Calibri', 15, 'normal'))

p.pensize(50)
p.speed(2)
#Upper side of the window.
p.goto(216, 282)
p.down()
p.color('#9b59b6')
p.goto(176, 282)
p.color('#8e44ad')
p.goto(136, 282)
p.color('#2980b9')
p.goto(96, 282)
p.color('#3498db')
p.goto(56, 282)
p.color('#1abc9c')
p.goto(16, 282)
p.color('#16a085')
p.goto(-24, 282)
p.color('#27ae60')
p.goto(-64, 282)
p.color('#2ecc71')
p.goto(-104, 282)
p.color('#f1c40f')
p.goto(-144, 282)
p.color('#f39c12')
p.goto(-184, 282)
p.color('#e67e22')
p.goto(-222, 282)

#Left side of the window.
p.color('#9b59b6')
p.goto(-222, 242)
p.color('#8e44ad')
p.goto(-222, 202)
p.color('#2980b9')
p.goto(-222, 162)
p.color('#3498db')
p.goto(-222, 122)
p.color('#1abc9c')
p.goto(-222, 82)
p.color('#16a085')
p.goto(-222, 42)
p.color('#27ae60')
p.goto(-222, 2)
p.color('#2ecc71')
p.goto(-222, -38)
p.color('#f1c40f')
p.goto(-222, -78)
p.color('#f39c12')
p.goto(-222, -118)
p.color('#e67e22')
p.goto(-222, -158)
p.color('#9b59b6')
p.goto(-222, -198)
p.color('#8e44ad')
p.goto(-222, -238)
p.color('#2980b9')
p.goto(-222, -274)

#Bottom side of the window.
p.color('#3498db')
p.goto(-182, -274)
p.color('#1abc9c')
p.goto(-142, -274)
p.color('#16a085')
p.goto(-102, -274)
p.color('#27ae60')
p.goto(-62, -274)
p.color('#2ecc71')
p.goto(-22, -274)
p.color('#f1c40f')
p.goto(18, -274)
p.color('#f39c12')
p.goto(58, -274)
p.color('#e67e22')
p.goto(98, -274)
p.color('#9b59b6')
p.goto(138, -274)
p.color('#8e44ad')
p.goto(178, -274)
p.color('#2980b9')
p.goto(215, -274)

#Right side of the window.
p.color('#3498db')
p.goto(215, -234)
p.color('#1abc9c')
p.goto(215, -194)
p.color('#16a085')
p.goto(215, -154)
p.color('#27ae60')
p.goto(215, -114)
p.color('#2ecc71')
p.goto(215, -74)
p.color('#f1c40f')
p.goto(215, -34)
p.color('#f39c12')
p.goto(215, 6)
p.color('#e67e22')
p.goto(215, 46)
p.color('#9b59b6')
p.goto(215, 86)
p.color('#8e44ad')
p.goto(215, 126)
p.color('#2980b9')
p.goto(215, 166)
p.color('#3498db')
p.goto(215, 206)
p.color('#1abc9c')
p.goto(215, 246)
p.color('#16a085')
p.goto(215, 286)

t = speedtest.Speedtest()
#Download test.
t_dA = time.time()
d = round(t.download() / 1_000_000, 2)
t_dB = time.time()
t_d = int(t_dB - t_dA)
dY = round(d / 9, 2) 

#Upload test.
t_uA = time.time()
u = round(t.upload() / 1_000_000, 2)
t_uB = time.time()
t_u = int(t_uB - t_uA)
uY = round(u / 9, 2) 

#Download frame.
s.reset()
p.hideturtle()
p.up()
p.pensize(2)
p.goto(-185, 245)
p.down()
p.goto(-185, 20)
p.goto(40, 20)
p.up()
p.color('gray')
p.pensize(1)
p.speed(10)
d_X = []
d_Y = []
n = 22.5
for A in range(1, 10):
    d_X.append(-185 + (A * n))
    d_Y.append(20 + (A * n))
    p.goto(-192, 245 - (A * n))
    p.down()
    p.goto(40, 245 - (A * n))
    p.up()
for B in range(1, 10):
    p.goto(-185 + (B * n), 13)
    p.down()
    p.goto(-185 + (B * n), 245)
    p.up()
p.goto(-199, 245)
p.color('#cb4335')
p.write('Mbps', font = ('Calibri', 8, 'normal'))
p.color('black')
x = 0
for C in range(1, 10):
    p.goto(-220, 238 - (C * n))
    p.write(round(d - (x * dY), 2))
    x += 1
for D in range(1, 10):
    p.goto(-188 + (D * n), 0)
    p.write(int(t_d / 9 * D), font = ('Calibri', 8, 'normal'))
p.goto(45, 13)
p.color('#cb4335')
p.write('Seconds', font = ('Calibri', 8, 'normal'))
p.goto(-185, 20)
p.color('#2980b9')
p.pensize(3)
p.down()
for E in range(0, 9):
    p.goto(d_X[E] + random.uniform(-11.25, 11.25), d_Y[E] + random.uniform(-11.25, 11.25))
p.color('black')
p.up()
p.goto(-99, 255)
p.write('DOWNLOAD')

#Upload frame.
p.speed(3)
p.pensize(2)
p.goto(-185, -30)
p.down()
p.goto(-185, -255)
p.goto(40, -255)
p.up()
p.color('gray')
p.pensize(1)
p.speed(10)
u_X = []
u_Y = []
for F in range(1, 10):
    u_X.append(-185 + (F * n))
    u_Y.append(-255 + (F * n))
    p.goto(-192, -30 - (F * n))
    p.down()
    p.goto(40, -30 - (F * n))
    p.up()
for G in range(1, 10):
    p.goto(-185 + (G * n), -262)
    p.down()
    p.goto(-185 + (G * n), -30)
    p.up()
p.goto(-199, -30)
p.color('#cb4335')
p.write('Mbps', font = ('Calibri', 8, 'normal'))
p.color('black')
y = 0
for H in range(1, 10):
    p.goto(-220, -37 - (H * n))
    p.write(round(u - (y * uY), 2))
    y += 1
for I in range(1, 10):
    p.goto(-188 + (I * n), -275)
    p.write(int(t_u / 9 * I), font = ('Calibri', 8, 'normal'))
p.goto(45, -263)
p.color('#cb4335')
p.write('Seconds', font = ('Calibri', 8, 'normal'))
p.goto(-185, -255)
p.color('#2980b9')
p.pensize(3)
p.down()
for J in range(0, 9):
    p.goto(u_X[J] + random.uniform(-11.25, 11.25), u_Y[J] + random.uniform(-11.25, 11.25))
p.color('black')
p.up()
p.goto(-90, -23)
p.write('UPLOAD')

#Summary.
p.goto(100, 255)
p.write('𝗦𝗨𝗠𝗠𝗔𝗥𝗬', font = ('Calibri', 15, 'normal'))
p.goto(60, 230)
p.write(f'User: {usr}')
p.goto(60, 210)
p.write(f'Upload speed: {u} Mbps')
p.goto(60, 190)
p.write(f'Download speed: {d} Mbps')
p.goto(60, 170)
p.write(f'IPv4: {IPv4}')
p.goto(60, 135)
p.write(f'IPv6: {IPv6.text}')

#Credits.
p.goto(110, -263)
p.write('𝓹𝓸𝔀𝓮𝓻𝓮𝓭 𝓫𝔂')
p.goto(133, -277)
p.write('massif')

