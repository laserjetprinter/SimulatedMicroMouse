def main():

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

if __name__ == "__main__":
	main()
			
