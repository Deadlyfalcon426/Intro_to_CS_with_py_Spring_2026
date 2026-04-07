#Full name: Ahsan Mohammed
#Date: 2/3/2026
#Chapter number: 2
#Exercise Title: Turtle Practice
#Description: In this exercise, I used the turtle module in Python to draw my initials, "AM".
import turtle as t #imports turtle, and imports as a shortened version to speed up time AM
t.speed(1)#sets speed of the turtle, useful if needing to see fine details or wanting to skip most of the drawing AM
t.right(90)
t.right(15)
t.forward(100)#drawing the first leg of the 'A' AM
t.backward(100)#going back to the top of the 'A' AM
t.left(30)#facing the next leg AM
t.forward(100)#drawing the next leg AM
t.backward(50)#pausing at the part where the part in between the 2 halves of the 'A' will be drawn AM
t.right(105)#aiming the drawing tool so that part in between the 2 halves of the 'A' can be drawn AM
t.forward(26)#this is for the part in between the 2 halves of the 'A' AM
t.backward(26)#going back to the 2nd leg AM
t.left(105)
t.forward(50)
t.left(75)
t.penup()#begins movement to the other letter AM
t.forward(20) #distance between the 2 initials AM
t.pendown()#puts pen down to begin next letter AM
t.left(70)# aims pen upwards to start the 'M' AM
t.forward(100)#drawing the first leg of the 'M' AM
t.right(70)#adjusting the drawing tool for the middle part AM
t.right(75)#same as above AM
t.forward(100)#drawing the middle part AM
t.left(130)
t.left(15)
t.forward(100)
t.right(75)#adjusting tool to draw the second leg AM
t.right(70)
t.forward(100)#drawing second leg AM