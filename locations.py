import messages
import movement

###################################
# Define borders for locations here
# Use only square coordinates for now
# Either all 4 points or 2 diagonal corners can be used
# All areas shall be defined and entered into the realize() function here
forest1 = [[0, 5], [5, 10]]
bigTree1 = [[3, 7]]

#forest1Outline = realize(2, forest1)
#print forest1
#forest1 = realize(1, forest1)
#print forest1

def Fforest1(xy):
    from game import ui
    if ui[0] == "go":
        print messages.forest1_travel
    elif ui[0] == "look":
        print messages.forest1_look
    if xy in bigTree1:
        print messages.bigTree1


def checkLoc(xy):
    """
    Simply checks if the player is within an area and will call the
    appropriate function as needed.
    """
    #xy = [[movement.x, movement.y]]
    print xy
    #These nested ifs could be combined with an and for less code
    if xy[0] in range(forest1[0][0],forest1[1][0]):
        #x is in range
        if xy[1] in range(forest1[0][1],forest1[1][1]):
            #y is in range
            print "in y range"
            Fforest1(xy)
    #del(xy)
