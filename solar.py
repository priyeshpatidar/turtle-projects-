from turtle import Shape, Turtle, mainloop, Vec2D as Vec
import gravity_system as gs



## create compound yellow/blue turtleshape for planets

def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.getscreen().bgcolor("black")
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"green")
    planetshape.addcomponent(m2,"black")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)

    
    ## setup gravitational system
    #sun 
    g = gs.GravSys()
    sun = gs.Star(1000000, Vec(0,0), Vec(0,-3.8), g, "circle")
    sun.color("yellow")
    sun.pencolor("yellow")
    sun.shapesize(1.9)
    sun.pu()
    
    #making earth
    earth = gs.Star(12500, Vec(210,0), Vec(0,195), g, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    
    #making mars
    
    mars = gs.Star(3000, Vec(360,0), Vec(0,150), g, "planet")
    mars.pencolor("red")
    mars.shapesize(0.8)

    #making moon so it will revolve around the earth

    moon = gs.Star(1, Vec(220,0), Vec(0,295), g, "planet")
    moon.pencolor("blue")
    moon.shapesize(.5)


    # making a mercury 
    
    mercury=gs.Star(2000,Vec(100,0),Vec(0,290),g,"planet")
    mercury.pencolor("pink")
    mercury.shapesize(.5)
    
    
    g.init()
    g.start()



    return "Done!"

#starting 

if __name__ == '__main__':
    main()
    mainloop()
