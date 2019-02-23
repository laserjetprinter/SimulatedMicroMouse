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

	#move_node()
	
	#set initial position of the node
        xPos, yPos = 1,1;
	xNodePos, yNodePos = 38,28
	os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
	time.sleep(0.5)

        #maze traversal algorithm
        while True:
                if MapMatrix[xPos][yPos+1] == " " and MapMatrix[xPos][yPos+2] == " ": #go down
                        yPos=yPos+2
			yNodePos=yNodePos+47
                        os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.5)
			print "In go down...current pos: (" + str(xPos) + "," + str(yPos) + ")",
			print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]
                
		elif MapMatrix[xPos+1][yPos] == " " and MapMatrix[xPos+2][yPos] == " ": #go right
                        xPos=xPos+2
			xNodePos=xNodePos+73
			os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.5)
			print "In go right...current pos: (" + str(xPos) + "," + str(yPos) + ")",
			print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]
                
		elif MapMatrix[xPos-1][yPos] == " " and MapMatrix[xPos-2][yPos] == " ": #go left
                        xPos=xPos-2
			xNodePos=xNodePos-73
			os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.5)
			print "In go left...current pos: (" + str(xPos) + "," + str(yPos) + ")",
			print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]
                
		elif MapMatrix[xPos][yPos-1] == " " and MapMatrix[xPos][yPos-2] == " ": #go up
                        yPos=yPos-2
			yNodePos=yNodePos-47
			os.system("coresendmsg node number=1 xpos="+str(xNodePos)+" ypos="+str(yNodePos))
                        time.sleep(0.5)
			print "In go down...current pos: (" + str(xPos) + "," + str(yPos) + ")",
			print "MapMatrix character at (" + str(xPos) + "," + str(yPos) + ")" + MapMatrix[xPos][yPos]

'''
def move_node():

	#set initial position of the node
	xPos, yPos = 1,1;

	#maze traversal algorithm
	while True:
		if MapMatrix[xPos][yPos+1] == " ": #go down
			yPos=yPos+47
			os.system("coresendmsg node number=1 xpos="+str(xPos)+" ypos="+str(yPos))
			time.sleep(0.5)
		elif MapMatrix[xPos+1][yPos] == " ": #go right
			xPos=xPos+73
			os.system("coresendmsg node number=1 xpos="+str(xPos)+" ypos="+str(yPos))
			time.sleep(0.5)
		elif MapMatrix[xPos-1][yPos] == " ": #go left
			xPo=xPos-73
			os.system("coresendmsg node number=1 xpos="+str(xPos)+" ypos="+str(yPos))
			time.sleep(0.5)
		elif MapMatrix[xPos][yPos+1] == " ": #go up
			yPos=yPos-47
			os.system("coresendmsg node number=1 xpos="+str(xPos)+" ypos="+str(yPos))
			time.sleep(0.5)
'''

if __name__ == "__main__":
	main()
			
