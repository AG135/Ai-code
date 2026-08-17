import random
import sys
import time

# Game constants
ROAD_WIDTH = 9
CAR_ICON = "🏎️"
OBSTACLE_ICON = "💥"
EMPTY_ICON = "  "


def print_road(player_pos, obstacles):
    """Renders the current game frame in the terminal."""
    # Clear terminal screen (works in most browsers/terminals)
    print("\033[H\033[J", end="")

    print("╔" + "═" * (ROAD_WIDTH * 2) + "╗")

    for row in range(10):
        line = "║"
        for col in range(ROAD_WIDTH):
            if row == 9 and col == player_pos:
                line += CAR_ICON
            elif (row, col) in obstacles:
                line += OBSTACLE_ICON
            else:
                line += EMPTY_ICON
        line += "║"
        print(line)

    print("╚" + "═" * (ROAD_WIDTH * 2) + "╝")


def main():
    player_pos = ROAD_WIDTH // 2
    obstacles = []
    score = 0
    spawn_chance = 0.3

    print("--- TERMINAL CAR DODGER ---")
    print("Controls: Type 'a' to go left, 'd' to go right.")
    print("Press Enter without typing to keep driving straight.")
    input("Press Enter to start...")

    while True:
        print_road(player_pos, obstacles)
        print(f"Score: {score}")

        # Get player move
        move = (
            input("Move (a/d) and press Enter: ").strip().lower()
        )

        if move == "a" and player_pos > 0:
            player_pos -= 1
        elif move == "d" and player_pos < ROAD_WIDTH - 1:
            player_pos += 1
        elif move == "q":
            print("Game exited.")
            break

        # Move obstacles down
        obstacles = [
            (row + 1, col) for (row, col) in obstacles if row < 9
        ]

        # Check for collisions
        if any(row == 9 and col == player_pos for (row, col) in obstacles):
            print_road(player_pos, obstacles)
            print(
                f"\n💥 CRASH! Game Over. Final Score: {score}"
            )
            break

        # Spawn new obstacles at the top
        if random.random() < spawn_chance:
            spawn_col = random.randint(0, ROAD_WIDTH - 1)
            # Prevent instant blocking of the whole road
            if not any(col == spawn_col for (row, col) in obstacles if row == 0):
                obstacles.append((0, spawn_col))

        score += 1


if __name__ == "__main__":
    main()
