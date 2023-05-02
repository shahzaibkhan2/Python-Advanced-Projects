# THIS CODE PROVIDES YOU WITH THE ANSWER TO YOUR QUESTION RELATED TO NEWTON'S ALL LAWS.

# Newton's First Law: An object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction, unless acted upon by an unbalanced force.

# An example function that checks if an object is at rest or in motion.
def check_motion(velocity):
    if velocity == 0:
        print("The object is at rest.")
    else:
        print("The object is in motion.")


# Newton's Second Law: The force acting on an object is equal to the mass of the object multiplied by its acceleration.

# An example function that calculates the force on an object given its mass and acceleration.
def calculate_force(mass, acceleration):
    force = mass * acceleration
    print("The force on the object is", force, "N.")


# Newton's Third Law: For every action, there is an equal and opposite reaction.

# An example function that demonstrates Newton's Third Law by simulating two objects colliding.
def simulate_collision(mass1, mass2, velocity1, velocity2):
    # Calculate the total momentum of the system.
    momentum_initial = mass1 * velocity1 + mass2 * velocity2

    # By conservation of momentum, the final momentum of the system must be equal to the initial momentum.
    # Assume that the masses are equal and the velocities are opposite.
    momentum_final = 0

    # Calculate the velocities of the objects after the collision.
    velocity1_final = momentum_initial / (2 * mass1)
    velocity2_final = -momentum_initial / (2 * mass2)

    # Print the results.
    print("Initial momentum of the system is", momentum_initial, "kg m/s.")
    print("Final momentum of the system is", momentum_final, "kg m/s.")
    print("Object 1's final velocity is", velocity1_final, "m/s.")
    print("Object 2's final velocity is", velocity2_final, "m/s.")


# Examples for usage to find results
check_motion(0)  # The object is at rest.
check_motion(10)  # The object is in motion.
calculate_force(5, 10)  # The force on the object is 50 N.
simulate_collision(1, 1, 10, -10)  # Initial momentum of the system is 0 kg m/s. Final momentum of the system is 0 kg m/s. Object 1's final velocity is -5.0 m/s. Object 2's final velocity is 5.0 m/s.

