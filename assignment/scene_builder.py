import maya.cmds as cmds

# This is clearing the scene.
cmds.file(new=True, force=True)

# This is creating the plane that all of the objects will sit on.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# This creates a small building on top of the plane.
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
cmds.move(building_x, building_height / 2.0, building_z, building)

# This creates the base of the silo shape object in the scene.
tower_radius = 2
tower_height = 10
tower_x = 4
tower_z = 6

tower = cmds.polyCylinder(
    name="tower_01",
    radius=tower_radius,
    height=tower_height,
)[0]
cmds.move(tower_x, tower_height / 2.0, tower_z, tower)


# This creates the top of the silo object in the scene.
cone_radius = 2
cone_height = 4
cone_x = 4
cone_z = 6

cone = cmds.polyCone(
    name="cone_01",
    radius=cone_radius,
    height=cone_height,
)[0]
cmds.move(cone_x, tower_height+cone_height / 2.0, cone_z, cone)


# This creates the bottom sphere of the snowman object in the scene.
bottom_radius = 6
bottom_x = 0
bottom_z = -4

bottom = cmds.polySphere(
    name="bottom_01",
    radius=bottom_radius,
)[0]
cmds.move(bottom_x, bottom_radius, bottom_z, bottom)

# This creates the middle sphere of the snowman object in the scene.
middle_radius = 4
middle_x = 0
middle_z = -4

middle = cmds.polySphere(
    name="middle_01",
    radius=middle_radius,
)[0]
cmds.move(middle_x, middle_radius+bottom_radius*2, middle_z, middle)

# This creates the bottom sphere of the snowman object in the scene.
top_radius = 2
top_x = 0
top_z = -4

top = cmds.polySphere(
    name="top_01",
    radius=top_radius,
)[0]
cmds.move(top_x, top_radius+middle_radius*2+bottom_radius*2, top_z, top)


# If this prints then that means that everything in the scene is operating properly.
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
