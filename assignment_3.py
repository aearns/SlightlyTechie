#!/usr/bin/env python3

#input a sentence
user_sentence = input('Please enter your sentence:\n')

#output sentence details
print(len(user_sentence))    #display total number of char 
print(len(user_sentence.split()))  #display total number of words using split
print(user_sentence.split()[0])     #display first word
print(user_sentence.split()[-1])    #display last word

#indexing and slicing
print(user_sentence[0:3]) #display first three characters
print(user_sentence[-3:]) #display last three characters
print(user_sentence[::-1]) #display reverse of the sentence

#Modigy the sentence
print(user_sentence.upper()) #display in uppercase
print(user_sentence.lower()) #display in lowercase
print(user_sentence.replace(' ', '-')) #replace all ' ' with '-'