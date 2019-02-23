import os
import time

def main():
	#initial position
	os.system("coresendmsg node number=2 xpos=38 ypos=28")
	i=1
	x=38
	y=75
	while i<3:
		os.system("coresendmsg node number=2 xpos="+str(x)+" ypos="+str(y))
		i+=1
		y+=47
		time.sleep(0.5)

	#os.system("coresendmsg node number=1 xpos=200 ypos=100")

if __name__ == "__main__":
	main()
