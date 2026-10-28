from time import sleep
import tkinter as tk


# Constants
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500


# Variables
sim_time = 0


# Class for physical particles
class Particles():
    def __init__(self, x:float, mass:float, charge:float, velocity:float=0):
        self.x : float = x
        self.velocity : float = velocity
        self.mass : float = mass
        self.charge : float = charge

    def update_position(self):
        self.x += self.velocity


# All the particles
electron1 = Particles(0, 1, -1, velocity=10)
proton1 = Particles(100, 100, 1)
neutron1 = Particles(110, 100, 0)
proton2 = Particles(-100, 100, 1)
neutron2 = Particles(-110, 100, 0)

particles = [electron1, proton1, proton2, neutron1, neutron2]

def update_all(root_display):
    global sim_time

    for i in range(len(particles)):
        particles[i].update_position()
    sim_time += 1

    root_display.after(10, update_all, root_display)

"""
Used to display all the particles
"""
def display() -> None:
    particles_pos = [particles[x].x for x in range(len(particles))]
    particles_cha = [particles[x].charge for x in range(len(particles))]

    root_display = tk.Tk()
    canvas_display = tk.Canvas(root_display, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    for i in range(len(particles_pos)):
        if particles_cha[i] == 0: 
            fill = 'green'
        elif particles_cha[i] == 1:
            fill = 'blue'
        elif particles_cha[i] == -1:
            fill = 'red'
        canvas_display.create_oval(particles_pos[i]+(CANVAS_WIDTH//2-5), (CANVAS_HEIGHT//2-5), particles_pos[i]+(CANVAS_WIDTH//2+5), (CANVAS_HEIGHT//2+5), fill=fill)
    canvas_display.pack()
    
    time_display = tk.Label(root_display, textvariable=sim_time)
    time_display.pack()

    root_display.after(10, update_all, root_display)
    root_display.mainloop()


if __name__ == "__main__":
    display()