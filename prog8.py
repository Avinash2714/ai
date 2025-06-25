from collections import deque

def monkey_banana_problem():
    # Initial state: (Monkey Location, Chair Position, Monkey on Chair or not, Holding Banana or not)
    initial_state = ('Far-Chair', 'Chair-Not-Under-Banana', 'Off-Chair', 'Empty')
    print(f"\nInitial state is {initial_state}")

    goal_state = ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', 'Holding')

    # Possible actions and their effects
    actions = {
        "Move to Chair": lambda s: ('Near-Chair', s[1], s[2], s[3]) if s[0] != 'Near-Chair' else None,
        "Push Chair under Banana": lambda s: ('Near-Chair', 'Chair-Under-Banana', s[2], s[3]) if s[0] == 'Near-Chair' and s[1] != 'Chair-Under-Banana' else None,
        "Climb Chair": lambda s: (s[0], s[1], 'On-Chair', s[3]) if s[0] == 'Near-Chair' and s[1] == 'Chair-Under-Banana' and s[2] != 'On-Chair' else None,
        "Grasp Banana": lambda s: (s[0], s[1], s[2], 'Holding') if s[0] == 'Near-Chair' and s[1] == 'Chair-Under-Banana' and s[2] == 'On-Chair' and s[3] != 'Holding' else None
    }

    # BFS to explore states
    dq = deque([(initial_state, [])])  # (current_state, actions_taken)
    visited = set()

    while dq:
        current_state, actions_taken = dq.popleft()

        if current_state == goal_state:
            print("\n✅ Solution Found!")
            print("Actions to achieve goal:")
            for action in actions_taken:
                print(action)
            print(f"Final State: {current_state}")
            return

        if current_state in visited:
            continue
        visited.add(current_state)

        # Try all possible actions
        for action_name, action_func in actions.items():
            next_state = action_func(current_state)
            if next_state and next_state not in visited:
                dq.append((next_state, actions_taken + [f"{action_name} → {next_state}"]))

    print("❌ No solution found.")

# Run the program
monkey_banana_problem()
