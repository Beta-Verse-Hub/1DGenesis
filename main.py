from time import sleep
import tkinter as tk

# Class for physical particles
class Particles():
    def __init__(self, x:float, mass:float, charge:float):
        self.x : float = x
        self.mass : float = mass
        self.charge : float = charge


electron1 = Particles(0, 1, -1)
proton1 = Particles(100, 100, 1)
neutron1 = Particles(110, 100, 0)
proton2 = Particles(-100, 100, 1)
neutron2 = Particles(-110, 100, 0)

particles = [electron1, proton1, proton2, neutron1, neutron2]

def display():
    particles_pos = [particles[x].x for x in range(len(particles))]
    particles_cha = [particles[x].charge for x in range(len(particles))]

    root_display = tk.Tk()
    canvas_display = tk.Canvas(root_display, height=500, width=500)
    for i in range(len(particles_pos)):
        if particles_cha[i] == 0: 
            fill = 'green'
        elif particles_cha[i] == 1:
            fill = 'blue'
        elif particles_cha[i] == -1:
            fill = 'red'
        canvas_display.create_oval(particles_pos[i]+245, 245, particles_pos[i]+255, 255, fill=fill)
    canvas_display.pack()
    root_display.mainloop()

if __name__ == "__main__":
    display()