## Making a universe with 3 paricles

There are three types of particles and 5 total number of particles (1 electron and 2 protons and neutrons)

| Particle  | Mass | Charge|
|-----------|------|-------|
| proton    | 100  | 1     |
| neutron   | 100  | 0     |
| electrons | 1    | -1    |

Next I added velocity and acceleration to the particle class which are related to the simulation time.

Next are the fundamental forces

### Electromagnetic
Coulomb's law should be used here but since I am dealing with 1 Dimension, it must be modified

$F=k\frac{q_1q_2}{r^2}$

where F is electrostatic force
q is charge of the particle
r is the distance between them
and k is Coulomb's constant which is 8.99 * 10^9 N*m^2/C^2

