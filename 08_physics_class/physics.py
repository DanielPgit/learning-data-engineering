def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


print(f_to_c(10))


def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


print(c_to_f(399))

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


def get_force(mass, acceleration):
    return mass * acceleration


train_mass = 22680
train_acceleration = 10


train_force = get_force(train_mass, train_acceleration)

print(f"The GE train supplies {train_force} Newtons of force")

bomb_mass = 1


def get_energy(mass, c=3 * 10**8):
    return mass * (c**2)


bomb_energy = get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules.")


# This function demonstrates function nesting:
# It calls 'get_force' to calculate the force first,
# then multiplies the result by distance to get work.
# It works because 'get_force' returns a number that
# Python can immediately use in the next calculation.
def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    return work


train_distance = 100


train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
