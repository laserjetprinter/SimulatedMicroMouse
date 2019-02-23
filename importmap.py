def main():
	#initialize matrix
	w, h = 34, 34;
	MapMatrix = [[0 for x in range(w)] for y in range(h)]

	xAxis, yAxis = 0,0;
	with open('mapcode.py') as f:
		while True:
			c=f.read(1)
			if not c:
				print "End of File"
				break
			if xAxis==33 and yAxis==33:
				break
			MapMatrix[xAxis][yAxis] = c
			print MapMatrix[xAxis][yAxis],
			if xAxis==33:
				xAxis=0
				yAxis=yAxis+1
			else:
				xAxis=xAxis+1
if __name__ == "__main__":
	main()
			
