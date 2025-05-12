# IMPORTS
import util
import math

# CONSTANTS
SLOPES = [.178]
INTERCEPTS = [9.49]
ANGLES = [15, 30, 45, 60, 75]

# FUNCTIONS
def determine_pairs(dh, distance):
    pairs = []
    for angle in ANGLES:
        pairs.append((angle, util.calculate_initial_velocity(distance, dh, math.radians(angle))))
    return pairs

def handle_input(value):
    if value[-1].lower() == 'y':
        return float(value[:-1]) * 0.9144  # Convert yards to meters
    else:
        return float(value)  # Already in meters

# MAIN 
def main():
    # Get the distance and height difference from the user
    distance = handle_input(input("Enter the distance (in meters or \"y\" after for yards): "))
    dh = handle_input(input("Enter the height difference (in meters or \"y\" after for yards): "))

    # Calculate the pairs of angles and initial velocities
    pairs = determine_pairs(dh, distance)

    # Print the results
    print(f"Distance: {distance} m, Height Difference: {dh} m")
    for angle, velocity in pairs:
        if velocity is None:
            print(f"Angle: {angle} degrees, Initial Velocity: Not possible")
        else:
            print(f"Angle: {angle} degrees, Initial Velocity: {velocity:.2f} m/s, Pressure: {util.calculate_pressure(velocity, SLOPES[0], INTERCEPTS[0]):.2f} PSI")

# MAIN
if __name__ == "__main__":
    main()