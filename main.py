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

# MAIN 
def main():
    # Get the distance and height difference from the user
    distance = float(input("Enter the distance (in meters): "))
    dh = float(input("Enter the height difference (in meters): "))

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