def checkfour(row, col, i, b): 
	# check for four vertical 	
	if i < 4: 
		if b[i+1][col] == b[i+2][col] and b[i+1][col] == b[i+3][col]: 
			return True

	if col == 0: 
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3]:
			return True
		if i > 2 and dia1con1(i,b,col):
			return True
		if i < 4 and dia2con1(i,b,col):
			return True

	if col == 1: 
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3] or \
		 row[col-1] == row[col+1] and row[col+1] == row[col+2]:
			return True
		if i>2 and dia1con1(i,b,col):
			return True
		if i<4 and dia2con1(i,b,col):
			return True
		if i>1 and i<6 and dia1con2(i,b,col):
			return True
		if i>0 and i<5 and dia2con2(i,b,col):
			return True

	if col == 2: 
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3] or \
		 row[col-1] == row[col+1] and row[col+1] == row[col+2] or \
		 row[col-2] == row[col-1] and row[col-1] == row[col+1]: 
			return True
		if i>2 and dia1con1(i,b,col):
			return True
		if i<4 and dia2con1(i,b,col):
			return True
		if i>1 and i<6 and (dia1con2(i,b,col) or dia2con3(i,b,col)):
			return True
		if i>0 and i<5 and (dia2con2(i,b,col) or dia1con3(i,b,col)):
			return True

	if col == 3:
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3] or \
		 row[col-1] == row[col+1] and row[col+1] == row[col+2] or \
		 row[col-2] == row[col-1] and row[col-1] == row[col+1] or \
		 row[col-3] == row[col-2] and row[col-2] == row[col-1]: 
			return True
		if i>2 and (dia1con1(i,b,col) or dia2con4(i,b,col)):
			return True
		if i<4 and (dia2con1(i,b,col) or dia1con4(i,b,col)):
			return True
		if i>1 and i<6 and (dia1con2(i,b,col) or dia2con3(i,b,col)):
			return True
		if i>0 and i<5 and (dia2con2(i,b,col) or dia1con3(i,b,col)):
			return True

	if col == 4: 
		# check for four flat in the row. 
		if row[col-1] == row[col-2] and row[col-2] == row[col-3] or \
		 row[col+1] == row[col-1] and row[col-1] == row[col-2] or \
		 row[col+2] == row[col+1] and row[col+1] == row[col-1]: 
			return True
		if i>2 and dia2con4(i,b,col):
			return True
		if i<4 and dia1con4(i,b,col):
			return True
		if i>1 and i<6 and (dia1con2(i,b,col) or dia2con3(i,b,col)):
			return True
		if i>0 and i<5 and (dia2con2(i,b,col) or dia1con3(i,b,col)):
			return True

	if col == 5: 
		# check for four flat in the row. 
		if row[col-1] == row[col-2] and row[col-2] == row[col-3] or \
		 row[col+1] == row[col-1] and row[col-1] == row[col-2]:
			return True
		if i>2 and dia2con4(i,b,col):
			return True
		if i<4 and dia1con4(i,b,col):
			return True
		if i>1 and i<6 and dia2con3(i,b,col):
			return True
		if i>0 and i<5 and dia1con3(i,b,col):
			return True

	if col == 6: 
		# check for four flat in the row. 
		if row[col-1] == row[col-2] and row[col-2] == row[col-3]:
			return True
		if i>2 and dia2con4(i,b,col):
			return True
		if i<4 and dia1con4(i,b,col):
			return True
	
	return False

#diagonal1: /
#0123 i>2, c<4
def dia1con1(i,b,c):
	if b[i-1][c+1] == b[i-2][c+2] and b[i-2][c+2] == b[i-3][c+3]:
		return True
#1012 1<i<6, 0<c<6
def dia1con2(i,b,c):
	if b[i+1][c-1] == b[i-1][c+1] and b[i-1][c+1] == b[i-2][c+2]:
		return True
#2101 0<i<5, 1<c<6
def dia1con3(i,b,c):
	if b[i+2][c-2] == b[i+1][c-1] and b[i-1][c+1] == b[i+1][c-1]:
		return True
#3210 i<4, 2<c
def dia1con4(i,b,c):
	if b[i+3][c-3] == b[i+2][c-2] and b[i+2][c-2] == b[i+1][c-1]:
		return True

#diagonal2: \
#0123 i<2, c<2
def dia2con1(i,b,c):
	if b[i+1][c+1] == b[i+2][c+2] and b[i+2][c+2] == b[i+2][c+3]:
		return True
#1012 0<i<5, 0<c<5
def dia2con2(i,b,c):
	if b[i-1][c-1] == b[i+1][c+1] and b[i+1][c+1] == b[i+2][c+2]:
		return True
#2101 1<i<6, 1<c<6
def dia2con3(i,b,c):
	if b[i-2][c-2] == b[i-1][c-1] and b[i-1][c-1] == b[i+1][c+1]:
		return True
#3210 2<i, 2<c
def dia2con4(i,b,c):
	if b[i-3][c-3] == b[i-2][c-2] and b[i-2][c-2] == b[i-1][c-1]:
		return True

















