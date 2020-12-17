#!/usr/bin/env python

"""
CoronaSafe Engineering Fellowship Solution for test problem statement using python
"""

import sys
import os.path
from datetime import datetime


def ForHelp():

	# when argument == 'help' is passed or no argument is passed, 'forhelp' get printed

	forhelp = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""

	# printing using utf-8 encoding

	sys.stdout.buffer.write(forhelp.encode('utf8'))
	

def AddTodo(line):

	# if file 'todo.txt' exists add line to file
	
	if os.path.isfile('todo.txt'):

	    with open("todo.txt",'r') as ToView:
	    	data = ToView.read()

	    with open("todo.txt",'w') as ToWrite:
	    	ToWrite.write(line+'\n'+data)


	# if file 'todo.txt' doesn't exists then create file and add line to file

	else:

	    with open("todo.txt",'w') as ToWrite:
	    	ToWrite.write(line+'\n')


	print('Added todo: "{}"'.format(line))


def ViewTodo():

	# if file 'todo.txt' has content, then print all todos

	if os.path.isfile('todo.txt'):

	    with open("todo.txt",'r') as ToView:
	    	data = ToView.readlines()

	    count = len(data)
	    x = ""

	    for line in data:
	    	x += '[{}] {}'.format(count,line)
	    	count -= 1

	    sys.stdout.buffer.write(x.encode('utf8'))


	# if 'todo.txt' is empty

	else:

	    print ("There are no pending todos!") 


def RemoveTodo(index):

	# Removing todo from the 'todo.txt' using index of todo

	if os.path.isfile('todo.txt'):

	    with open("todo.txt",'r') as ToView:
	    	data = ToView.readlines()

	    count=len(data)


	    if index > count or index <= 0:

	    	print(f"Error: todo #{index} does not exist. Nothing deleted.")


	    else:

	    	with open("todo.txt",'w') as ToWrite:
	    		for line in data:
	    			if count != index:
	    				ToWrite.write(line)
	    			count -= 1

	    	print("Deleted todo #{}".format(index))


	else:

	    print("Error: todo #{} does not exist. Nothing deleted.".format(index))


def DoneTodo(index):

	# To mark Todo as Done

	if os.path.isfile('todo.txt'):

	    with open("todo.txt",'r') as ToView:
	    	data = ToView.readlines()

	    count = len(data)

	    if index > count or index <= 0:
	    	print("Error: todo #{} does not exist.".format(index))

	    else:
	    	with open("todo.txt",'w') as ToWrite:

	    		if os.path.isfile('done.txt'):
	    			with open("done.txt",'r') as DoneView:
				    	done = DoneView.read()
			    	with open("done.txt",'w') as DoneWrite:

			    		for line in data:

			    			if count == index:
			    				DoneWrite.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)

			    			else:
			    				ToWrite.write(line)

			    			count -= 1

			    		DoneWrite.write(done)

		    	else:

		    		with open("done.txt",'w') as DoneWrite:

			    		for line in data:

			    			if count == index:
			    				DoneWrite.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)

			    			else:
			    				ToWrite.write(line)

			    			count -= 1

	    	print("Marked todo #{} as done.".format(index))


	else:

	    print("Error: todo #{} does not exist.".format(index))


def ForReport():

	# To generate report

	TodoCount = 0
	DoneCount = 0

	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as ToWrite:
	    	line=ToWrite.readlines()
	    TodoCount=len(line)

	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as doneFile:
	    	done=doneFile.readlines()
	    DoneCount=len(done)


	var = datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(TodoCount,DoneCount)
	sys.stdout.buffer.write(var.encode('utf8'))


# main() function

def main():

	if len(sys.argv) == 1:
		ForHelp()

	elif sys.argv[1] == 'help':
		ForHelp()

	elif sys.argv[1] == 'ls':
		ViewTodo()

	elif sys.argv[1] == 'add':

		if len(sys.argv) > 2:
			AddTodo(sys.argv[2])

		else:
			print("Error: Missing todo string. Nothing added!")

	elif sys.argv[1] == 'del':

		if len(sys.argv) > 2:
			RemoveTodo(int(sys.argv[2]))

		else:
			print("Error: Missing NUMBER for deleting todo.")

	elif sys.argv[1] == 'done':

		if len(sys.argv) > 2:
			DoneTodo(int(sys.argv[2]))

		else:
			print("Error: Missing NUMBER for marking todo as done.")

	elif sys.argv[1] == 'report':
		ForReport()

	else:
		print('Option Not Available. Please use "./todo help" for Usage Information')


if __name__=="__main__": 
    main() 