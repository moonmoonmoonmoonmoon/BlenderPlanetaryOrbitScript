
# <github.com/MOONMOONMOONMOONMOON> - Computer Graphics Fall 2020
# version: Blender 2.90
# Final Exam/Program: Create a solar system with all 10 known celestial bodies.
#
#
# to run, switch to 'Scripting' workspace
# then run this script by playing the script or "Alt+P"
# lastly, go to 'Animation' workspace and play the animation
# changing the 'Viewport Shading' to see the textures
#
# NOTE: that this script was made in Blender 2.90

import bpy
import mathutils
import math

# this is a function to add textures to the celestial objects
#
# parameters: 
# "texture_path" is the location of the image that you will be applying to the object
# "obj" is the specified object that you will be applying the image to
#
def add_texture(texture_path, obj):
    mat = bpy.data.materials.new(name='texture')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    texImage = nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(texture_path)
    principled = nodes['Principled BSDF']
    mat.node_tree.links.new( texImage.outputs[0], principled.inputs[0] )

    # Assign to object
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
        

# the skybox is an image of the galactic disk
# you can find any image of the night sky on google
# this can be commented out if no images are to be applied
# *** YOU MUST SPECIFY YOUR TEXTURE LOCATION ***
skybox = "" # SPECIFY YOUR TEXTURE LOCATION
celestial = 10 # celestial body count
radius = 0 # planetary orbit position
height = 0
circle = 7 # planetary orbit
c = 1 # orbital movement

# planetary images names
# named all of the texture images sun.jpg, merc.jpg, and so on
planets = ["sun",
"merc","venus",
"earth","mars",
"jup","sat","ura",
"nept","pluto","moon"]

# celestial scaling of each object in the solar system
# accuracy was not applied to the script in any way
celestial_scale = [mathutils.Vector((20,20,20)), # sun
mathutils.Vector((1,1,1)), # mercury
mathutils.Vector((4,4,4)), # venus
mathutils.Vector((4,4,4)), # earth
mathutils.Vector((3,3,3)), # mars
mathutils.Vector((10,10,10)), # jupiter
mathutils.Vector((7,7,7)), # saturn
mathutils.Vector((6,6,6)), # uranus
mathutils.Vector((6,6,6)), # neptune
mathutils.Vector((1,1,1))] # pluto

# delete all existing objects before applying new ones
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# creating the skybox first
bpy.ops.mesh.primitive_uv_sphere_add()
sky = bpy.context.active_object
add_texture(skybox, sky) # this can be commented out if no images are to be applied
sky.scale = mathutils.Vector((200,200,200))
bpy.ops.object.shade_smooth()

i = 0
# this is to create each individual celestial body and spawn them in
while (i < celestial):

    theta = (c-1)*math.pi*2/(celestial*circle)
    x = radius*circle*math.cos(theta)
    y = radius*circle*math.sin(theta)
    z = height
    bpy.ops.mesh.primitive_uv_sphere_add(
    location = [x, y, z], rotation = [0, 0, theta], scale = celestial_scale[i])
    obj = bpy.context.active_object
    # the next line to this comment can be commented out if no images are to be applied
    add_texture("C:/Users/LUNA/Desktop/BlenderFiles/"+planets[i]+".jpg", obj)
    radius +=2
    c = 1
    
    # the objects were made smoother
    # also the objects' distance from the center of the sun is captured using r1, r2, r3, and so on
    # each celestial object is assigned its own name: sun, mer, ven, and so on
    bpy.ops.object.shade_smooth()
    if planets[i] == 'sun':
        sun = obj
        r1 = sun.location.x
    elif planets[i] == 'merc':
        mer = obj
        r2 = mer.location.x
    elif planets[i] == 'venus':
        ven = obj
        r3 = ven.location.x
    elif planets[i] == 'earth':
        ear = obj
        r4 = ear.location.x
    elif planets[i] == 'mars':
        mar = obj
        r5 = mar.location.x
    elif planets[i] == 'jup':
        jup = obj
        r6 = jup.location.x
    elif planets[i] == 'sat':
        sat = obj
        r7 = sat.location.x
    elif planets[i] == 'ura':
        ura = obj
        r8 = ura.location.x
    elif planets[i] == 'nept':
        nep = obj
        r9 = nep.location.x
    elif planets[i] == 'pluto':
        plu = obj
        r10 = plu.location.x
    
    i +=1

days = 365 * 1 # days * years  
# WARNING: Setting the years higher than a 5 could result in a long rendering time
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = days
last = bpy.context.scene.frame_end

for n in range(last):
    bpy.context.scene.frame_set(n)
    
    # creating all of the orbital location of each celestial body
    # the sun stays still and does not move. it is the one being orbited
    sun.location = [sun.location.x, 
    sun.location.y, 
    sun.location.z]
    
    # notice that each celestial body have a different orbital speed in the animation
    # an attempt was made to make the orbital speeds as accurate as possible
    mer.location = [r2*math.cos(math.radians(n*4.1)), 
    r2*math.sin(math.radians(n*4.1)), 
    mer.location.z]
    
    ven.location = [r3*math.cos(math.radians(n*1.6)), 
    r3*math.sin(math.radians(n*1.6)), 
    ven.location.z]
    
    ear.location = [r4*math.cos(math.radians(n)),
    r4*math.sin(math.radians(n)), 
    ear.location.z]
    
    mar.location = [r5*math.cos(math.radians(n*0.53)), 
    r5*math.sin(math.radians(n*0.53)), 
    mar.location.z]
    
    jup.location = [r6*math.cos(math.radians(n*0.08)), 
    r6*math.sin(math.radians(n*0.08)), 
    jup.location.z]
    
    sat.location = [r7*math.cos(math.radians(n*0.034)), 
    r7*math.sin(math.radians(n*0.034)), 
    sat.location.z]
    
    ura.location = [r8*math.cos(math.radians(n*0.012)), 
    r8*math.sin(math.radians(n*0.012)), 
    ura.location.z]
    
    nep.location = [r9*math.cos(math.radians(n*(n/60190))), 
    r9*math.sin(math.radians(n*(n/60190))), 
    nep.location.z]
    
    plu.location = [r10*math.cos(math.radians(n*(n/90520))), 
    r10*math.sin(math.radians(n*(n/90520))), 
    plu.location.z]
    
    # record each keyframe for each celestial body
    sun.keyframe_insert(data_path="location")
    mer.keyframe_insert(data_path="location")
    ven.keyframe_insert(data_path="location")
    ear.keyframe_insert(data_path="location")
    mar.keyframe_insert(data_path="location")
    jup.keyframe_insert(data_path="location")
    sat.keyframe_insert(data_path="location")
    ura.keyframe_insert(data_path="location")
    nep.keyframe_insert(data_path="location")
    plu.keyframe_insert(data_path="location")