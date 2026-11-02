from time import sleep
import tkinter as tk


# Constants
CANVAS_HEIGHT : int = 500
CANVAS_WIDTH : int = 700
ELECTROSTATIC_CONSTANT : int = 50000000
UP_CHARGE : int = 2 # Set as int to aviod floating point division problems
DOWN_CHARGE : int = -1 # Set as int to aviod floating point division problems


# Variables
sim_time : float = 0
update_interval : int = 1
dt : float = 0.001

# Class for physical particles
class Particles():

    def __init__(self, x:float, mass:float, particle_type:str,velocity:float=0, acceleration: float=0):

        self.particle_type : str = particle_type
        self.mass : float = mass

        self.x : float = x
        self.velocity : float = velocity
        self.acceleration : float = acceleration

        if particle_type == "electron":
            self.quarks : str = ""
        elif particle_type == "proton":
            self.quarks : str = "uud"
        elif particle_type == "neutron":
            self.quarks : str = "udd"

        if self.quarks == "":
            self.electromagnetic_charge : float = -1
        else:
            self.electromagnetic_charge : float = 0
            for i in self.quarks:
                self.electromagnetic_charge += (DOWN_CHARGE if i == "d" else UP_CHARGE)
            self.electromagnetic_charge = self.electromagnetic_charge // 3

    def update_position(self) -> None:

        self.x += self.velocity * dt

    def update_velocity(self) -> None:

        self.velocity += self.acceleration * dt

    def applied_force(self, other_particle_pos, other_particle_cha) -> float:

        if self.x-other_particle_pos != 0:
            return (ELECTROSTATIC_CONSTANT*self.electromagnetic_charge*other_particle_cha)*(self.x-other_particle_pos)/abs(self.x-other_particle_pos)**3
        else:
            return (ELECTROSTATIC_CONSTANT*self.electromagnetic_charge*other_particle_cha)*(self.x-other_particle_pos)/0.00001


# All the particles
electron1 = Particles(0, 1, 'electron')
proton1 = Particles(50, 100, 'proton')
proton2 = Particles(-50, 100, 'proton')
neutron1 = Particles(100, 100, 'neutron')
neutron2 = Particles(-100, 100, 'neutron')

particles = [electron1, proton1, proton2, neutron1, neutron2]


def update_all(root_display, canvas_display, time_display, particles_pos, particles_cha):

    global sim_time, update_interval

    canvas_display.delete("all")

    for i in range(len(particles)):
        net_force = 0
        for j in range(len(particles)):
            if j != i:
                net_force += particles[i].applied_force(particles[j].x, particles[j].electromagnetic_charge)
        particles[i].acceleration = net_force/particles[i].mass

    for i in range(len(particles)):
        particles[i].update_velocity()
    
    for i in range(len(particles)):
        particles[i].update_position()

    sim_time += dt
    sim_time = float(f"{sim_time:.5f}")
    time_display.config(text=f"{sim_time}s")

    particles_pos = [particles[x].x for x in range(len(particles))]
    particles_cha = [particles[x].electromagnetic_charge for x in range(len(particles))]

    draw_particles(particles_pos, particles_cha, canvas_display)

    for i in particles:
        print(i.x,end=" ")
    print()

    root_display.after(update_interval, update_all, root_display, canvas_display, time_display, particles_pos, particles_cha)

def draw_particles(particles_pos, particles_cha, canvas_display):

    for i in range(len(particles_pos)):

            if particles_cha[i] == 0: 
                fill = 'green'
            elif particles_cha[i] > 0:
                fill = 'blue'
            elif particles_cha[i] < 0:
                fill = 'red'

            canvas_display.create_oval(particles_pos[i]+(CANVAS_WIDTH//2-5), (CANVAS_HEIGHT//2-5), particles_pos[i]+(CANVAS_WIDTH//2+5), (CANVAS_HEIGHT//2+5), fill=fill)

"""
Used to display all the particles
"""
def display() -> None:

    global update_interval

    particles_pos = [particles[x].x for x in range(len(particles))]
    particles_cha = [particles[x].electromagnetic_charge for x in range(len(particles))]

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
