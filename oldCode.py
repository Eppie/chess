data = []
blackPawnOnDark = squares[1][1].load()
for x in range(135):
  for y in range(135):
    data.append(blackPawnOnDark[x, y])
blackPawnOnDark = data

data = []
blackPawnOnLight = squares[1][0].load()
for x in range(135):
  for y in range(135):
    data.append(blackPawnOnLight[x, y])
blackPawnOnLight = data

data = []
blackRookOnDark = squares[0][0].load()
for x in range(135):
  for y in range(135):
    data.append(blackRookOnDark[x, y])
blackRookOnDark = data

data = []
blackRookOnLight = squares[0][7].load()
for x in range(135):
  for y in range(135):
    data.append(blackRookOnLight[x, y])
blackRookOnLight = data

data = []
blackKnightOnDark = squares[0][6].load()
for x in range(135):
  for y in range(135):
    data.append(blackKnightOnDark[x, y])
blackKnightOnDark = data

data = []
blackKnightOnLight = squares[0][1].load()
for x in range(135):
  for y in range(135):
    data.append(blackKnightOnLight[x, y])
blackKnightOnLight = data

data = []
blackBishopOnDark = squares[0][2].load()
for x in range(135):
  for y in range(135):
    data.append(blackBishopOnDark[x, y])
blackBishopOnDark = data

data = []
blackBishopOnLight = squares[0][5].load()
for x in range(135):
  for y in range(135):
    data.append(blackBishopOnLight[x, y])
blackBishopOnLight = data

data = []
blackQueenOnDark = squares[0][4].load()
for x in range(135):
  for y in range(135):
    data.append(blackQueenOnDark[x, y])
blackQueenOnDark = data

blackQueenOnLight = [(1000, 1000, 1000)]*135*135
# data = []
# blackQueenOnLight = squares[4][5].load()
# for x in range(135):
#   for y in range(135):
#     data.append(blackQueenOnLight[x, y])
# blackQueenOnLight = data

blackKingOnDark = [(1000, 1000, 1000)]*135*135
# data = []
# blackKingOnDark = squares[6][4].load()
# for x in range(135):
#   for y in range(135):
#     data.append(blackKingOnDark[x, y])
# blackKingOnDark = data

data = []
blackKingOnLight = squares[0][3].load()
for x in range(135):
  for y in range(135):
    data.append(blackKingOnLight[x, y])
blackKingOnLight = data


data = []
whitePawnOnDark = squares[6][0].load()
for x in range(135):
  for y in range(135):
    data.append(whitePawnOnDark[x, y])
whitePawnOnDark = data

data = []
whitePawnOnLight = squares[6][1].load()
for x in range(135):
  for y in range(135):
    data.append(whitePawnOnLight[x, y])
whitePawnOnLight = data

data = []
whiteRookOnDark = squares[7][7].load()
for x in range(135):
  for y in range(135):
    data.append(whiteRookOnDark[x, y])
whiteRookOnDark = data

data = []
whiteRookOnLight = squares[7][0].load()
for x in range(135):
  for y in range(135):
    data.append(whiteRookOnLight[x, y])
whiteRookOnLight = data

data = []
whiteKnightOnDark = squares[7][1].load()
for x in range(135):
  for y in range(135):
    data.append(whiteKnightOnDark[x, y])
whiteKnightOnDark = data

data = []
whiteKnightOnLight = squares[7][6].load()
for x in range(135):
  for y in range(135):
    data.append(whiteKnightOnLight[x, y])
whiteKnightOnLight = data

data = []
whiteBishopOnDark = squares[7][5].load()
for x in range(135):
  for y in range(135):
    data.append(whiteBishopOnDark[x, y])
whiteBishopOnDark = data

data = []
whiteBishopOnLight = squares[7][2].load()
for x in range(135):
  for y in range(135):
    data.append(whiteBishopOnLight[x, y])
whiteBishopOnLight = data

whiteQueenOnDark = [(1000, 1000, 1000)]*135*135
# data = []
# whiteQueenOnDark = squares[4][6].load()
# for x in range(135):
#   for y in range(135):
#     data.append(whiteQueenOnDark[x, y])
# whiteQueenOnDark = data

data = []
whiteQueenOnLight = squares[7][4].load()
for x in range(135):
  for y in range(135):
    data.append(whiteQueenOnLight[x, y])
whiteQueenOnLight = data

data = []
whiteKingOnDark = squares[7][3].load()
for x in range(135):
  for y in range(135):
    data.append(whiteKingOnDark[x, y])
whiteKingOnDark = data

whiteKingOnLight = [(1000, 1000, 1000)] * 135 * 135
# data = []
# whiteKingOnLight = squares[6][3].load()
# for x in range(135):
#   for y in range(135):
#     data.append(whiteKingOnLight[x, y])
# whiteKingOnLight = data

data = []
emptyLight = squares[2][1].load()
for x in range(135):
  for y in range(135):
    data.append(emptyLight[x, y])
emptyLight = data

data = []
emptyDark = squares[2][2].load()
for x in range(135):
  for y in range(135):
    data.append(emptyDark[x, y])
emptyDark = data

possibilities = {"blackPawnOnDark": blackPawnOnDark, "blackPawnOnLight": blackPawnOnLight, "blackRookOnDark": blackRookOnDark, "blackRookOnLight": blackRookOnLight, "blackKnightOnDark": blackKnightOnDark, "blackKnightOnLight": blackKnightOnLight, "blackBishopOnDark": blackBishopOnDark, "blackBishopOnLight": blackBishopOnLight, "blackQueenOnDark": blackQueenOnDark, "blackQueenOnLight": blackQueenOnLight, "blackKingOnDark": blackKingOnDark, "blackKingOnLight": blackKingOnLight, "whitePawnOnDark": whitePawnOnDark, "whitePawnOnLight": whitePawnOnLight, "whiteRookOnDark": whiteRookOnDark, "whiteRookOnLight": whiteRookOnLight, "whiteKnightOnDark": whiteKnightOnDark, "whiteKnightOnLight": whiteKnightOnLight, "whiteBishopOnDark": whiteBishopOnDark, "whiteBishopOnLight": whiteBishopOnLight, "whiteQueenOnDark": whiteQueenOnDark, "whiteQueenOnLight": whiteQueenOnLight, "whiteKingOnDark": whiteKingOnDark, "whiteKingOnLight": whiteKingOnLight, "emptyDark": emptyDark, "emptyLight": emptyLight}
