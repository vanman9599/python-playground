import numpy as np
import matplotlib.pyplot as plt

# Constants retrieved from NASA's black hole data
G = 6.67430e-11  # Gravitational constant (in m^3 kg^−1 s^−2)
c = 299792458  # Speed of light (in m/s)


def schwarzschild_radius(mass):
    """Calculate the Schwarzschild radius (event horizon) based on NASA's black hole physics."""
    return 2 * G * mass / c**2


def gravitational_acceleration(mass, distance):
    """Calculate gravitational acceleration based on the black hole's mass and the object's distance."""
    return G * mass / distance**2


def simulate_object_fall(mass, initial_distance, time_steps=1000, dt=1e-3):
    """Simulate an object's fall towards a black hole using retrieved physics principles."""
    event_horizon_radius = schwarzschild_radius(mass)
    distances = [initial_distance]
    velocities = [0]  # Initial velocity
    times = [0]

    for _ in range(time_steps):
        distance = distances[-1]
        velocity = velocities[-1]
        time = times[-1]

        # Stop if the object reaches the event horizon
        if distance <= event_horizon_radius:
            break

        # Calculate gravitational acceleration
        accel = gravitational_acceleration(mass, distance)

        # Update velocity and position using basic motion equations
        new_velocity = velocity + accel * dt
        new_distance = distance - new_velocity * dt

        distances.append(new_distance)
        velocities.append(new_velocity)
        times.append(time + dt)

    return times, distances, velocities


def plot_trajectory(times, distances, velocities, event_horizon_radius):
    """Plot the object's trajectory and velocity as it approaches the black hole's event horizon."""
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Distance (m)', color='tab:blue')
    ax1.plot(times, distances, label='Distance from Black Hole', color='tab:blue')
    ax1.axhline(y=event_horizon_radius, color='r',
                linestyle='--', label='Event Horizon')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Velocity (m/s)', color='tab:green')
    ax2.plot(times, velocities, label='Velocity', color='tab:green')
    ax2.tick_params(axis='y', labelcolor='tab:green')

    fig.tight_layout()
    plt.title('Object Falling into a Black Hole')
    plt.legend()
    plt.show()


# Example usage with input validation for edge cases
if __name__ == '__main__':
    try:
        black_hole_mass = float(
            input("Enter the mass of the black hole (in kg): "))
        initial_distance = float(
            input("Enter the initial distance from the black hole (in meters): "))

        if black_hole_mass <= 0 or initial_distance <= 0:
            raise ValueError("Mass and distance must be positive values.")

        # Simulate the object's fall
        times, distances, velocities = simulate_object_fall(
            black_hole_mass, initial_distance)

        # Plot the trajectory and velocity
        event_horizon_radius = schwarzschild_radius(black_hole_mass)
        plot_trajectory(times, distances, velocities, event_horizon_radius)

    except ValueError as e:
        print(f"Error: {e}")
