from time import sleep
import tkinter as tk


# Constants
CANVAS_HEIGHT : int = 500
CANVAS_WIDTH : int = 700
ELECTROSTATIC_CONSTANT : int = 9000000


# Variables
sim_time : float = 0
update_interval : int = 10

# Class for physical particles
class Particles():
    def __init__(self, x:float, mass:float, charge:float, velocity:float=0, acceleration: float=0):
        self.x : float = x
        self.velocity : float = velocity
        self.acceleration : float = acceleration
        self.mass : float = mass
        self.charge : float = charge

    def update_position(self):
        self.x += self.velocity * update_interval/1000

    def update_velocity(self):
        self.velocity += self.acceleration * update_interval/1000

    def applied_force(self, other_particle_pos, other_particle_cha):
        return (ELECTROSTATIC_CONSTANT*self.charge*other_particle_cha)*(self.x-other_particle_pos)/abs(self.x-other_particle_pos)**3


# All the particles
electron1 = Particles(0, 1, -1)
proton1 = Particles(100, 100, 1)
neutron1 = Particles(110, 100, 0)
proton2 = Particles(-100, 100, 1)
neutron2 = Particles(-110, 100, 0)

particles = [electron1, proton1, proton2, neutron1, neutron2]


def update_all(root_display, canvas_display, time_display, particles_pos, particles_cha):

    global sim_time, update_interval

    canvas_display.delete("all")

    for i in range(len(particles)):
        net_force = 0
        for j in range(len(particles)):
            if j != i:
                net_force += particles[i].applied_force(particles[j].x, particles[j].charge)
        particles[i].acceleration = net_force/particles[i].mass

    for i in range(len(particles)):
        particles[i].update_velocity()
    
    for i in range(len(particles)):
        particles[i].update_position()

    sim_time += update_interval/1000
    sim_time = float(f"{sim_time:.5f}")
    time_display.config(text=f"{sim_time}s")

    particles_pos = [particles[x].x for x in range(len(particles))]
    particles_cha = [particles[x].charge for x in range(len(particles))]

    draw_particles(particles_pos, particles_cha, canvas_display)

    print(particles[0].x, particles[1].x, particles[2].x, particles[3].x, particles[4].x)

    root_display.after(update_interval, update_all, root_display, canvas_display, time_display, particles_pos, particles_cha)

def draw_particles(particles_pos, particles_cha, canvas_display):

    for i in range(len(particles_pos)):

            if particles_cha[i] == 0: 
                fill = 'green'
            elif particles_cha[i] == 1:
                fill = 'blue'
            elif particles_cha[i] == -1:
                fill = 'red'

            canvas_display.create_oval(particles_pos[i]+(CANVAS_WIDTH//2-5), (CANVAS_HEIGHT//2-5), particles_pos[i]+(CANVAS_WIDTH//2+5), (CANVAS_HEIGHT//2+5), fill=fill)

"""
Used to display all the particles
"""
def display() -> None:

    global update_interval

    particles_pos = [particles[x].x for x in range(len(particles))]
    particles_cha = [particles[x].charge for x in range(len(particles))]

    root_display = tk.Tk()
    canvas_display = tk.Canvas(root_display, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas_display.pack()
    
    time_display = tk.Label(root_display, text=f"{sim_time}s")
    draw_particles(particles_pos, particles_cha, canvas_display)
    time_display.pack()

    root_display.after(update_interval, update_all, root_display, canvas_display, time_display, particles_pos, particles_cha)
    root_display.mainloop()


if __name__ == "__main__":
    display()
