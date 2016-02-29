import bpy
from random import randint, random
from math import sqrt, pi
 
# Function to calculate the distance between two points
def distance(a, b) :
    '''
    list , list --> float
    a = list with three element
    b = list with three element
   
    return the distance between two points in float
    '''
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
 
# How many Sphere you want to add
count = 100
 
# Sphere properties
size = 0.1

# Ellispoid properties
ellipsoidSize = [0.1, 0.2, 0.1]
 
# The sphere will be created between -domain <--> domain
domain = 2
 
# Max time to try finding a new location before break the loop
maxTry = 100000
 
# Variable to count how many try has been done
Try = 0
 
# list with three element to generate locations
location = [0, 0, 0]
 
# Variable to hold the distant between balls
dist = 0
 
# True == Won't collide , False == Will collide
State = True
 
# This tuple will hold centers of created spheres
locList = ()
 
while count > 0 :
   
    # Calculate x, y, z position
    location[0] = round(random()*(domain-size*2)-(domain-size*2)/2, 5)
    location[1] = round(random()*(domain-size*2)-(domain-size*2)/2, 5)
    location[2] = round(random()*(domain-size*2)-(domain-size*2)/2, 5)
          
   
    # Start check if it will collide with other spheres
    for x in locList :
        # Calculate the distant
        dist = distance(x, location)
       
        # If it's too close make State = False
        if dist < size*2 + 0.1 :
            State = False
            break
        # If it's in a good position State = True
        else :
            State = True
   
    # The distant is too close , recalculate the location
    if State == False :
        Try += 1
        continue
   
    # After Try reach maxTry break the loop
    if Try > maxTry :
        break
   
    # Successfully found a New location
    # Add this point
    locList += (location[:],)
   
    # Create a new Sphere
    #bpy.ops.mesh.primitive_uv_sphere_add(size = size, location = location)

    # Smooth the faces
    bpy.ops.object.shade_smooth()

    #Create a new sphere at the same location, and resize it to an ellipsoid
    bpy.ops.mesh.primitive_uv_sphere_add(size = 1.0, location = location)
    bpy.ops.transform.resize(value=ellipsoidSize)

    #Give the ellipsoid a random orientation
    bpy.ops.transform.rotate(value=(2*pi*random()-1), axis=((2*pi*random()-1), (2*pi*random()-1), (2*pi*random()-1)))

    #Smooth the faces
    bpy.ops.object.shade_smooth()
   
    # reset Try
    Try = 0
   
    # Decrease the counter
    count -= 1     
