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
Coulomb's law should be used here and since I am dealing with 1 Dimension, vectors aren't required rather scalar would work far better

$F=k\frac{q_1q_2}{r^2}$

- F = electrostatic force
- q = charge of the particle
- r = distance between them
- k = Coulomb's constant which is 8.99 * 10^9 N*m^2/C^2
