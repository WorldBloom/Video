from manim import *
class CAD(ThreeDScene):
    def construct(self):
        body1 = Cylinder(height=2.5,radius=1,show_ends=False)
        handle = Torus(major_radius=0.7,minor_radius=0.25).shift(RIGHT)
        handle.rotate(PI/2,axis=RIGHT)  

        wholecup = VGroup(body1,handle).shift(3*LEFT)
       
        donut = Torus(major_radius=1,minor_radius=0.5).shift(3*RIGHT)

        
        self.add(wholecup,donut)

        self.set_camera_orientation(phi=80 * DEGREES, theta=270 * DEGREES)


class ExampleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        circle = Circle(radius=1,color=BLUE,fill_opacity=0.7)
        square = Square(side_length=1,color=BLUE,fill_opacity=0.7)

        sphere = Sphere(
            center=(0, 0, 0),
            radius=0.5,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001], 
            v_range=[0, TAU]
        )
        sphere.set_color(BLUE)   

        sphere1 = Sphere(
            center=(0, 0, 0),
            radius=2,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere1.set_color(BLUE)

        cube = Cube(side_length=2, fill_opacity=0.7, fill_color=BLUE)






        self.play(Create(circle),run_time=2)
        self.play(ApplyWave(circle))
        self.wait()
        self.play(ReplacementTransform(circle,square),run_time=3)
        self.wait()
        self.play(ReplacementTransform(square,sphere),run_time=3)
        self.wait()   
        self.play(ReplacementTransform(sphere,sphere1),run_time=3)
        self.wait()
        self.play(sphere1.animate.scale(0.001))
        self.wait()
        self.play(ReplacementTransform(sphere1,cube),run_time=3)
        self.wait(2)


class BTD(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=80 * DEGREES, theta=270 * DEGREES)

        donut = Torus(major_radius=1,minor_radius=0.5).shift(3*RIGHT)

        sphere = Sphere(
            center=(0, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001], 
            v_range=[0, TAU]
        ).shift(3*LEFT)
        
        donut.set_color(BLUE)
        sphere.set_color(BLUE)
        self.add(sphere,donut)
        self.play(ReplacementTransform(sphere,donut),run_time=3,lag_ratio=0.05)
        self.wait()

class BTD2(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=80 * DEGREES, theta=270 * DEGREES)

        donut = Torus(major_radius=1,minor_radius=0.5).shift(3*RIGHT)

        sphere = Sphere(
            center=(0, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001], 
            v_range=[0, TAU]
        ).shift(3*LEFT)
        
        donut.set_color(BLUE)
        sphere.set_color(BLUE)
        self.add(sphere,donut)


       