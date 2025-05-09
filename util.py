import math

def quadratic_formula(a, b, c):
    # return the two solutions of the quadratic equation ax^2 + bx + c = 0
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return x1, x2 

def calculate_time(distance, dh, angle):
    # calculate time needed to reach the distance
    return math.sqrt((-19.6 * dh + 19.6 * distance * math.tan(angle)) / 96.04)

def calculate_initial_velocity(distance, dh, angle):
    # calculate initial velocity needed
    try:
        t = calculate_time(distance, dh, angle)
        x_vel = distance / t
        vel = x_vel / math.cos(angle)
        return vel
    except:
        return None

def calculate_pressure(velocity, slope, intercept):
    # calculate pressure using the linear equation y = mx + b
    return (velocity - intercept) / slope

if __name__ == "__main__":
   print(calculate_initial_velocity(25.3, -10, math.radians(60)))