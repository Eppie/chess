from PIL import Image

def averageColor(img, width, height):

	pixels = img.load()
	data = []
	for x in range(width):
		for y in range(height):
			cpixel = pixels[x, y]
			data.append(cpixel)

	r, g, b = 0, 0, 0
	count = len(data)

	for x in range(count):
		r+=data[x][0]
		g+=data[x][1]
		b+=data[x][2]

	rAvg = r/count
	gAvg = g/count
	bAvg = b/count

	return (rAvg, gAvg, bAvg)

def diff((r1, g1, b1), (r2, g2, b2)):
	rDiff = abs( r1 - r2 )
	gDiff = abs( g1 - g2 )
	bDiff = abs( b1 - b2 )
	difference = rDiff + gDiff + bDiff
	return difference


im = Image.open("chess.png")
w, h = im.size
box = (0, int(511.0/1920*h), w, int(1591.0/1920*h))
im = im.crop(box)
w = int(w/8.0)
squares = [ [] for _ in range(8) ]
colors = [ [] for _ in range(8) ]
for j in range(8):
	for i in range(8):
		tempImg = im.copy()
		box = ( i * w, j * w, ( i * w ) + w, ( j * w ) + w )
		tempImg = tempImg.crop(box)
		squares[7 - j].append(tempImg.copy())
		tempImg.save("squares\square{0}{1}.jpg".format(7-j, i))
		colors[7 - j].append(averageColor(tempImg, w, w))

data = []
blackPawnOnDark = squares[6][4].load()
for x in range(135):
	for y in range(135):
		data.append(blackPawnOnDark[x, y])
blackPawnOnDark = data

data = []
blackPawnOnLight = squares[4][5].load()
for x in range(135):
	for y in range(135):
		data.append(blackPawnOnLight[x, y])
blackPawnOnLight = data

data = []
blackRookOnDark = squares[7][7].load()
for x in range(135):
	for y in range(135):
		data.append(blackRookOnDark[x, y])
blackRookOnDark = data

data = []
blackRookOnLight = squares[7][0].load()
for x in range(135):
	for y in range(135):
		data.append(blackRookOnLight[x, y])
blackRookOnLight = data

data = []
blackKnightOnDark = squares[7][1].load()
for x in range(135):
	for y in range(135):
		data.append(blackKnightOnDark[x, y])
blackKnightOnDark = data

data = []
blackKnightOnLight = squares[7][6].load()
for x in range(135):
	for y in range(135):
		data.append(blackKnightOnLight[x, y])
blackKnightOnLight = data

data = []
blackBishopOnDark = squares[7][5].load()
for x in range(135):
	for y in range(135):
		data.append(blackBishopOnDark[x, y])
blackBishopOnDark = data

data = []
blackBishopOnLight = squares[7][2].load()
for x in range(135):
	for y in range(135):
		data.append(blackBishopOnLight[x, y])
blackBishopOnLight = data

data = []
blackQueenOnDark = squares[7][3].load()
for x in range(135):
	for y in range(135):
		data.append(blackQueenOnDark[x, y])
blackQueenOnDark = data

# data = []
# blackQueenOnLight = squares[4][5].load()
# for x in range(135):
# 	for y in range(135):
# 		data.append(blackQueenOnLight[x, y])
# blackQueenOnLight = data

# data = []
# blackKingOnDark = squares[6][4].load()
# for x in range(135):
# 	for y in range(135):
# 		data.append(blackKingOnDark[x, y])
# blackKingOnDark = data

data = []
whitePawnOnDark = squares[1][1].load()
for x in range(135):
	for y in range(135):
		data.append(whitePawnOnDark[x, y])
whitePawnOnDark = data

data = []
whitePawnOnLight = squares[1][0].load()
for x in range(135):
	for y in range(135):
		data.append(whitePawnOnLight[x, y])
whitePawnOnLight = data

data = []
whiteRookOnDark = squares[0][0].load()
for x in range(135):
	for y in range(135):
		data.append(whiteRookOnDark[x, y])
whiteRookOnDark = data

data = []
whiteRookOnLight = squares[0][7].load()
for x in range(135):
	for y in range(135):
		data.append(whiteRookOnLight[x, y])
whiteRookOnLight = data

data = []
whiteKnightOnDark = squares[2][2].load()
for x in range(135):
	for y in range(135):
		data.append(whiteKnightOnDark[x, y])
whiteKnightOnDark = data

# data = []
# whiteKnightOnLight = squares[7][6].load()
# for x in range(135):
# 	for y in range(135):
# 		data.append(whiteKnightOnLight[x, y])
# whiteKnightOnLight = data

data = []
whiteBishopOnDark = squares[0][2].load()
for x in range(135):
	for y in range(135):
		data.append(whiteBishopOnDark[x, y])
whiteBishopOnDark = data

data = []
whiteBishopOnLight = squares[3][2].load()
for x in range(135):
	for y in range(135):
		data.append(whiteBishopOnLight[x, y])
whiteBishopOnLight = data

data = []
whiteQueenOnDark = squares[4][6].load()
for x in range(135):
	for y in range(135):
		data.append(whiteQueenOnDark[x, y])
whiteQueenOnDark = data

# data = []
# whiteQueenOnLight = squares[4][5].load()
# for x in range(135):
# 	for y in range(135):
# 		data.append(whiteQueenOnLight[x, y])
# whiteQueenOnLight = data

data = []
whiteKingOnDark = squares[0][4].load()
for x in range(135):
	for y in range(135):
		data.append(whiteKingOnDark[x, y])
whiteKingOnDark = data

# data = []
# whiteKingOnLight = squares[6][3].load()
# for x in range(135):
# 	for y in range(135):
# 		data.append(whiteKingOnLight[x, y])
# whiteKingOnLight = data

data = []
emptyLight = squares[2][1].load()
for x in range(135):
	for y in range(135):
		data.append(emptyLight[x, y])
emptyLight = data

data = []
emptyDark = squares[2][4].load()
for x in range(135):
	for y in range(135):
		data.append(emptyDark[x, y])
emptyDark = data
print emptyDark

for i in range(8):
	for j in range(8):
		newSquare = squares[i][j].load()
		data = []
		for x in range(135):
			for y in range(135):
				data.append(newSquare[x, y])

		result = sum( [ diff( emptyLight[x], data[x] ) for x in range(135*135) ] )
		print result, i, j
