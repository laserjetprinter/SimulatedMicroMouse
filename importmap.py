import os
import time

def main():

	'''
	Import the map code and store it into a matrix
	titled MapMatrix (34x34) matrix. This matrix
	will be used to navigate the maze
	'''

	#initialize matrix
	w, h = 34, 34;
	MapMatrix = [[0 for x in range(w)] for y in range(h)]
	xAxis, yAxis = 0,0;

	with open('mapcode.py') as f:
		while True:
			
			#reads character from input file
			c=f.read(1)
			
			if not c:
				print "End of File"
				break

			#end of matrix
			if xAxis==33 and yAxis==33:
				break

			#adds character and prints the matrix
			MapMatrix[xAxis][yAxis] = c
			print MapMatrix[xAxis][yAxis],
			
			#reach the end of line, increment to next...otherwise increment x
			if xAxis==33:
				xAxis=0
				yAxis=yAxis+1
			else:
				xAxis=xAxis+1

	'''
	Add, position, and change image of node
	'''

	os.system("coresendmsg node flags=add number=1 type=0 name=heart xpos=38 ypos=28")
	os.system("coresendmsg node number=1 icon=/home/core/Downloads/rsz_heart.gif")

	'''
	Starts the moving algorithm for the node
	'''

	#set initial position of the node
        xPos, yPos = 1,1;
	xNodePos, yNodePos = 38,28
	os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
	time.sleep(0.5)

	treeNodeVal = 0
	xParentNode, yParentNode = 38,28;
	xParentPos, yParentPos = 1,1;

	xPNStack = []
	yPNStack = []
	xPPStack = []
	yPPStack = []

	while True:

		treeNodeVal=0

		#sets the current matrix position to number of child branches
		if MapMatrix[xPos][yPos+1] == " " and MapMatrix[xPos][yPos+2] == " ": #go down
			treeNodeVal+=1
		if MapMatrix[xPos+1][yPos] == " " and MapMatrix[xPos+2][yPos] == " ": #go right
			treeNodeVal+=1
		if MapMatrix[xPos-1][yPos] == " " and MapMatrix[xPos-2][yPos] == " ": #go left
			treeNodeVal+=1
		if MapMatrix[xPos][yPos-1] == " " and MapMatrix[xPos][yPos-2] == " ": #go up
			treeNodeVal+=1
		if treeNodeVal==0:
			print "Back to parent"

		MapMatrix[xPos][yPos] = treeNodeVal
		
		#navigating the matrix		
		if MapMatrix[xPos][yPos+1] == " " and MapMatrix[xPos][yPos+2] == " ": #go down
                        
			#setting parent node values
			xPNStack.append(xNodePos)
        		yPNStack.append(yNodePos)
        		xPPStack.append(xPos)
        		yPPStack.append(yPos)			

			#updating current node values
			yPos=yPos+2
                        yNodePos=yNodePos+47
                        os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.1)
                        print "In go down...current pos: (" + str(xPos) + "," + str(yPos) + ")",
                        print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]

                elif MapMatrix[xPos+1][yPos] == " " and MapMatrix[xPos+2][yPos] == " ": #go right
                        
			#setting parent node values
			xPNStack.append(xNodePos)
                        yPNStack.append(yNodePos)
                        xPPStack.append(xPos)
                        yPPStack.append(yPos)

                        #updating current node values
			xPos=xPos+2
                        xNodePos=xNodePos+73
                        os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.1)
                        print "In go right...current pos: (" + str(xPos) + "," + str(yPos) + ")",
                        print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]

                elif MapMatrix[xPos-1][yPos] == " " and MapMatrix[xPos-2][yPos] == " ": #go left
                        
			#setting parent node values
			xPNStack.append(xNodePos)
                        yPNStack.append(yNodePos)
                        xPPStack.append(xPos)
                        yPPStack.append(yPos)

                        #updating current node values
			xPos=xPos-2
                        xNodePos=xNodePos-73
                        os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.1)
                        print "In go left...current pos: (" + str(xPos) + "," + str(yPos) + ")",
                        print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]

		elif MapMatrix[xPos][yPos-1] == " " and MapMatrix[xPos][yPos-2] == " ": #go up
                        
			#setting parent node values
			xPNStack.append(xNodePos)
                        yPNStack.append(yNodePos)
                        xPPStack.append(xPos)
                        yPPStack.append(yPos)

                        #updating current node values
			yPos=yPos-2
                        yNodePos=yNodePos-47
                        os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.1)
                        print "In go down...current pos: (" + str(xPos) + "," + str(yPos) + ")",
                        print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]
		
		#if the stack is empty
		if len(xPNStack) == 0:
			break

		if treeNodeVal==0:
			xNodePos = xPNStack.pop()
                        yNodePos = yPNStack.pop()
			os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
			time.sleep(0.1)
                        xPos = xPPStack.pop()
                        yPos = yPPStack.pop()
	
	#print out the traveresed matrix
	xVal, yVal = 0,0;
	while True:
		print MapMatrix[xVal][yVal],	
		if xVal==33 and yVal==32:
			break
		if xVal==33:
			xVal=0
			yVal+=1
		else:
			xVal+=1
		
if __name__ == "__main__":
	main()
			
