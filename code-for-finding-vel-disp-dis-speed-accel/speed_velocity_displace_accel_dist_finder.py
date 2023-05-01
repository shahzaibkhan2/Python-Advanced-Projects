# Define initial and final conditions to find the resultant
initial_position = 0  # meters
final_position = 100  # meters
initial_velocity = 0  # meters/second
final_velocity = 50  # meters/second
time = 10  # seconds

# Calculate displacement
displacement = final_position - initial_position

# Calculate distance
distance = abs(displacement)

# Calculate average velocity
average_velocity = displacement / time

# Calculate acceleration
acceleration = (final_velocity - initial_velocity) / time

# Calculate speed
speed = distance / time

# Print results
print("Displacement:", displacement, "meters")
print("Distance:", distance, "meters")
print("Average Velocity:", average_velocity, "meters/second")
print("Acceleration:", acceleration, "meters/second^2")
print("Speed:", speed, "meters/second")
