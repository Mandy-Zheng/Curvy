from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )
print("face.png")
parse_file( 'script', edges, transform, screen, color )
#for x in range(100):
#    for y in range(100):
#        draw_line(0,y,x,0,screen,color)
#parse_file( 'cute.txt', edges, transform, screen, color )
