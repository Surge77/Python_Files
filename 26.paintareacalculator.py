"""
YOu are painting a wall.the instructions on the paint can says that 1 can of paint can 
cover 5 square meters of wall.given an random height and width of wall,calcualtel how many cans of paint you'll need to buy

number of cans = (wall height X wall width) / coverage per can --formula directly put into the functions

If the answer is like 0.6 of a can of paint the result should be rounded upto 2 cans

"""

def paint_cal(height,width,cover):
    number_of_cans = (height*width) / cover
    return number_of_cans

test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5

area = paint_cal(height=test_h, width=test_w, cover=coverage) #here the concept of keyword arguments is used
area_round = round(area) # we rounded the decimal values
print(f"You'll need {area_round} cans of paint")