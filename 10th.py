from math import sqrt
def simil():
    a1 = int(input('Enter the base of first triangle: '))
    a2 = int(input('Enter the base of first triangle: '))
    b1 = int(input('Enter the base of first triangle: '))
    b2 = int(input('Enter the base of first triangle: '))
    c = float(a1*a2)/float(b1*b2)
    print('The result is: ',c)
    
def pytha():
    s1 = float(input('Enter one side: '))
    s2 = float(input('Enter side two: '))
    hyp = sqrt((s1*s1)+(s2*s2))
    print('The value of hypotenuse is: ',hyp)

def coord():
    print('Enter 1 for distance formula,2 for section formula,3 for midpoint formula,4 for centroid formula')
    
    inp = input('Input: ')
    if inp == '1' :
        x1 = int(input('Enter X coordinate for first point: '))
        y1 = int(input('Enter Y coordinate for first point: '))
        x2 = int(input('Enter X coordinate for second point: '))
        y2 = int(input('Enter Y coordinate for second point: '))
        x = sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        
        print(x)
    elif inp == '2':
        x1 = int(input('Enter X coordinate for first point: '))
        y1 = int(input('Enter Y coordinate for first point: '))
        x2 = int(input('Enter X coordinate for second point: '))
        y2 = int(input('Enter Y coordinate for second point: '))        
        m = int(input('Enter the value of m: '))
        n = int(input('Enter the value of n: '))
        mod = m+n
        x = (m*x2+n*x1)/mod
        y = (m*y2+n*y1)/mod
        print('The coordinate of section point is: ''(',x,',',y,')')
    elif inp == '3':
        x1 = int(input('Enter X coordinate for first point: '))
        y1 = int(input('Enter Y coordinate for first point: '))
        x2 = int(input('Enter X coordinate for second point: '))
        y2 = int(input('Enter Y coordinate for second point: '))   
        x = (x1+x2)/2
        y = (y1+y2)/2
        print('The coordinate of midpoint point is: ''(',x,',',y,')')
    elif inp == '4':
        x1 = int(input('Enter X coordinate for first vertex: '))
        y1 = int(input('Enter Y coordinate for first vertex: '))
        x2 = int(input('Enter X coordinate for second vertex: '))
        y2 = int(input('Enter Y coordinate for second vertex: '))  
        x3 = int(input('Enter X coordinate of third vertex: '))
        y3 = int(input('Enter Y coordinate of third vertex: '))
        x = (x1+x2+x3)/3
        y = (y1+y2+y3)/3
        print('The coordinate of midpoint point is: ''(',x,',',y,')')
    else:
        print('Invalid option')

def mess():
    print('Enter 1 for cube,2 for cubiod,3 for cylinder,4 for cone,5 for sphere and 6 for hemisphere')
    ip = input('Input: ')
    pi = math.pi
    if ip == '1':
        s = int(input('Enter side of cube: '))
        print('The volume of the cube is: ',s**3)
    elif ip == '2':
        l = int(input('Enter length of the cuboid: '))
        b = int(input('Enter breath of the cuboid: '))
        h = int(input("Enter height of the cuboid: "))
        print('The volume of cuboid is: ',l*b*h)
    elif ip == '3':
        r = int(input('Enter the radius of cylinder: '))
        h = int(input('Enter the height of cylinder: '))
        v = pi*pow(r,2)*h
        print('The volume of the cylinder is: ',round(v,3))

    elif ip == '4':
        h = int(input('Enter the height of cone: '))
        r = int(input('Enter the radius if cone: '))
        v = 1/3*(pi*pow(r,2)*h)
        print('The volume of the cylinder is: ',round(v,3))

    elif ip == '5':
        r = int(input('Enter the radius of the sphere: '))
        v = 4/3*(pi*pow(r,3))
        print('The volume of the sphere is: ',round(v,3))
        
    elif ip == '6':
        r = int(input('Enter the radius of the hemi-sphere: '))
        v = 2/3*(pi*pow(r,3))
        print('The volume of the hemi-sphere is: ',round(v,3))
    else:
        print('Invalid option')
        
print('This program is only for 10th standard students')
print('Enter:\n1.For similarity\n2.For pythagoras theorem\n3.Coordinate geometry\n4.For Mensuration\nMore will be added soon:)')
minp = input('Enter the input: ')
if minp == '1':
    simil()
elif minp == '2':
    pytha()
elif minp == '3':
    coord()
elif minp == '4':
    mess()
else:
    print('Invalid option')
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
