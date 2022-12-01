# Ask user for number of coordinates

n = int(input ("Enter the number of polygon points: "))

# Ask user for x and y values

print("Enter x and y coordinates for polygon points: ")
x = []
y = []


for i in range (0, n):
    inputx = float(input ("Coordinate x: "))
    x.append(inputx)

    inputy = float(input ("Coordinate y: "))
    y.append(inputy)


# Print the points


print("Point    x       y")
print("--------------------")
for i in range (0, n): 
    print(i+1,":","   ",x[i],"   ",y[i])


# Calculate and print Values

print("Geometric characteristics")

list_ax = []
for i in range (1, n): 
    ax = (x[i] + x[i-1]) * (y[i] - y[i-1])
    list_ax.append (ax) 

total_ax = sum (list_ax) / 2
print (("Ax:    "), round(total_ax, 2))


list_sx = []
for i in range (1, n):
    sx = (x[i] - x[i-1]) * (y[i]**2 + y[i-1] * y[i] + y[i-1]**2)
    list_sx.append (sx)

total_sx = - sum (list_sx) / 6
print (("Sx:    "), round(total_sx, 2))


list_sy = []
for i in range (1, n):
    sy = (y[i] - y[i-1]) * (x[i]**2 + x[i-1] * x[i] + x[i-1]**2) 
    list_sy.append (sy)

total_sy = sum (list_sy) / 6
print (("Sy:    "), round(total_sy, 2)) 


list_ix = []
for i in range (1, n):
    ix = (x[i] - x[i-1]) * (y[i]**3 + y[i]**2 * y[i-1] + y[i] * y[i-1]**2 + y[i-1]**3)
    list_ix.append (ix)

total_ix = - sum (list_ix) / 12
print (("Ix:    "), round(total_ix, 2))


list_iy = []
for i in range (1, n):
    iy = (y[i] - y[i-1]) * (x[i]**3 + x[i]**2 * x[i-1] + x[i] * x[i-1]**2 + x[i-1]**3)
    list_iy.append (iy)

total_iy = sum (list_iy) / 12
print (("Iy:    "), round(total_iy, 2))


list_ixy = []
for i in range (1, n):
    ixy = (y[i] - y[i-1]) * (y[i] * (3*x[i]**2 + 2*x[i] * x[i-1] + x[i-1]**2) + y[i-1] * (3*x[i-1]**2 + 2*x[i] * x[i-1] + x[i]**2))
    list_ixy.append (ixy)

total_ixy = - sum (list_ixy) / 24 
print (("Ixy:  "), round(total_ixy, 2)) 


total_xt = (total_sy) / (total_ax) 
print (("xt:    "), round(total_xt, 2)) 


total_yt = (total_sx) / (total_ax) 
print (("yt:    "), round(total_yt, 2))


total_ixt = (total_ix) - (total_yt)**2 * (total_ax)
print (("Ixt:   "), round(total_ixt, 2))


total_iyt = (total_iy) - (total_xt)**2 * (total_ax)
print (("Iyt:   "), round(total_iyt, 2))


total_ixyt = (total_ixy) + (total_xt) * (total_yt) * (total_ax) 
print (("Ixyt:  "), round(total_ixyt, 2))


print("mbp15-2022:bimaplus wilsonzarate")





