# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:37:56 2020

@author: Dhondi Sai Ganesh
"""


alphabet='bcghjklmpqrtvwxyz'
score=0
names=input('Enter Your Name and give Space and then friend name')
for character in names:
    if character in 'aeiou':
        score+=5
    if character in 'friends':
        score+=10
    if character in alphabet:
        score+=alphabet.find(character)
    else:
        score+=0
if score>100:
    print('Your friendship score is : ',score)
    print('Congratulation you both are friends!')
else:
    print('Your Friendship score is : ',score)