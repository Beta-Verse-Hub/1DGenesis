from time import sleep
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Particles():
    def __init__(self, x:float, mass:float, charge:float):
        self.x : float = x
        self.mass : float = mass
        self.charge : float = charge


electron1 = Particles(0, 1, -1)
proton1 = Particles(10, 100, 1)
neutron1 = Particles(11, 100, 0)
proton2 = Particles(-10, 100, 1)
neutron2 = Particles(-11, 100, 0)

particles = [electron1, proton1, proton2, neutron1, neutron2]

def display():
    particles_pos = [particles[x].x for x in range(len(particles))]
    plt.figure(figsize=(8, 5))
    plt.plot(particles_pos, marker='o', color='blue', linewidth=2)
    
    plt.title("1D Universe")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)

    # Show the window
    plt.show()

if __name__ == "__main__":
    display()