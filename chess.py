from PIL import Image
import pickle

possibilities = pickle.load( open( "possibilities.p", "rb" ) )


def diff((r1, g1, b1), (r2, g2, b2)):
	rDiff = abs( r1 - r2 )
	gDiff = abs( g1 - g2 )
	bDiff = abs( b1 - b2 )
	difference = rDiff + gDiff + bDiff
	return difference


im = Image.open("testBoard1.png")
w, h = im.size
box = (0, int(511.0/1920*h), w, int(1591.0/1920*h))
im = im.crop(box)
w = int(w/8.0)
squares = [ [] for _ in range(8) ]
for j in range(8):
	for i in range(8):
		tempImg = im.copy()
		box = ( i * w, j * w, ( i * w ) + w, ( j * w ) + w )
		tempImg = tempImg.crop(box)
		squares[7 - j].append(tempImg.copy())
		# tempImg.save("squares\square{0}{1}.jpg".format(7-j, i))


def bestGuess(data):
	result = []
	for k, v in possibilities.items():
		result.append( ( sum( [ diff( v[x], data[x] ) for x in range(135*135) ] ), k ) )
	return min(result)

for i in range(8):
	for j in range(8):
		newSquare = squares[i][j].load()
		data = []
		for x in range(135):
			for y in range(135):
				data.append(newSquare[x, y])

		print bestGuess(data), i, j

