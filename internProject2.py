# Using pywhatkit Library

import pywhatkit as py

#Send Message on Whatsapp
ReceiverNumber = input("Enter Mobile Number with Country Code")

Msg = input("Enter the Message You want to send to the Receiver")

Hour = int(input("Enter hours in 24 hours format"))

Min = int(input("Enter minute"))

py.sendwhatmsg(ReceiverNumber,Msg,Hour,Min)

print("Sent Successfully")

#Play Video on Youtube
TopicName = input("Enter the Topic Name to search on Youtube")

py.playonyt(TopicName)

print("Video Played")

#Search topic on Google
topicName = input("Enter the Topic Name to search on Google")

py.search(topicName)

print("Completed") 

#Search number of lines you want to know about that topic
topic_name = input("Enter the topic name")

no_of_lines = input("Number of lines that should be displayed")

py.info(topic_name,lines = no_of_lines)



