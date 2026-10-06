import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# -----------------------------
# Physics Sort Core Mechanics
# -----------------------------

def compute_momentum(arr):
    n = len(arr)
    momentum = [0] * n
    for i in range(n):
        left = arr[i-1] if i > 0 else arr[i]
        right = arr[i+1] if i < n-1 else arr[i]
        momentum[i] = abs(arr[i] - left) + abs(right - arr[i])
    return momentum

def physics_step(arr, momentum):
    n = len(arr)
    changed = False

    for i in range(n):
        if momentum[i] <= 0:
            continue

        # Determine direction
        direction = 0
        if i > 0 and arr[i] < arr[i-1]:
            direction = -1
        elif i < n-1 and arr[i] > arr[i+1]:
            direction = +1

        # Compute friction
        left = arr[i-1] if i > 0 else arr[i]
        right = arr[i+1] if i < n-1 else arr[i]
        friction = (abs(arr[i] - left) + abs(right - arr[i])) / 2

        # Reduce momentum
        momentum[i] -= friction
        if momentum[i] <= 0:
            momentum[i] = 0
            continue

        # Move particle
        if direction == -1 and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            momentum[i-1] += momentum[i] * 0.3
            changed = True

        elif direction == +1 and i < n-1:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            momentum[i+1] += momentum[i] * 0.3
            changed = True

    return changed


# -----------------------------
# Animation Setup
# -----------------------------

def animate_physics_sort(arr):
    arr = arr[:]
    momentum = compute_momentum(arr)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(0, max(arr) + 10)
    ax.set_title("Physics Sort Animation")

    frames = []

    # Generate frames until sorted
    while any(m > 0 for m in momentum):
        frames.append((arr[:], momentum[:]))
        physics_step(arr, momentum)

    # Animation update function
    def update(frame):
        ax.clear()
        ax.set_xlim(-1, len(arr))
        ax.set_ylim(0, max(arr) + 10)

        arr_state, mom_state = frame

        # Draw particles
        for i, val in enumerate(arr_state):
            glow = mom_state[i] * 3
            ax.scatter(i, val, s=80 + glow, color="blue")
            ax.text(i, val + 1, str(val), ha="center")

            # Momentum bar
            ax.plot([i, i], [val, val + mom_state[i]], color="red", linewidth=2)

        ax.set_title("Physics Sort — Momentum + Friction")

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=120)
    plt.show()


# -----------------------------
# Run Example
# -----------------------------
arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
animate_physics_sort(arr)
