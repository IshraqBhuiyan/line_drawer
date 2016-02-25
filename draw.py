from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if x1 < x0:
        startx = x1
        starty = y1
        x = x0
        y = y0
    else:
        startx = x0
        starty = y0
        x = x1
        y = y1
    A = y - starty
    B = -(x - startx)
    ## Octant 1
    if A >= 0 and A <= -B:
        print "Octant1\n"
        d = 2*A + B
        z =0
        while startx <= x:
            #print "Making octant1 Line\n"
            #print z
            plot(screen, color, x, y)
            if d>0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
            #z+= 1
    ## Octant 8
    elif A < 0 and -A >= B:
        #print "Octant 8\n"
        d = 2*A - B
        while startx <= x:
            plot(screen, color, x, y)
            if d<0:
                y-=1
                d-=2*B
            x+=1
            d+=2*A
    elif A > -B:
        #print "Octant 2\n"
        d = A + 2*B
        while starty <= y:
            plot(screen, color, x, y)
            if d<0:
                x+=1
                d+=2*A
            y+=1
            d+=2*B
    else:
        #print "Octant 7\n"
        d= A-2*B
        while starty>=y:
            plot(screen, color, x, y)
            if d>0:
                x+=1
                d+=2*A
            y-=1
            d-=2*B
    pass
