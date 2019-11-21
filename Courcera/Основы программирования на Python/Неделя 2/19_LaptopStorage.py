roomX = int(input())
roomY = int(input())
roomZ = int(input())
boxX = int(input())
boxY = int(input())
boxZ = int(input())

nX = roomX // boxX
nY = roomY // boxY
nZ = roomZ // boxZ
n1 = nX * nY * nZ

nX = roomX // boxX
nY = roomY // boxZ
nZ = roomZ // boxY
n2 = nX * nY * nZ

nX = roomX // boxY
nY = roomY // boxX
nZ = roomZ // boxZ
n3 = nX * nY * nZ

nX = roomX // boxY
nY = roomY // boxZ
nZ = roomZ // boxX
n4 = nX * nY * nZ

nX = roomX // boxZ
nY = roomY // boxX
nZ = roomZ // boxY
n5 = nX * nY * nZ

nX = roomX // boxZ
nY = roomY // boxY
nZ = roomZ // boxX
n6 = nX * nY * nZ

print(max(n1, n2, n3, n4, n5, n6))
