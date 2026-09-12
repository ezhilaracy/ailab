import random


class NQueensCSP:
    def __init__(self, N):
        self.N = N
        self.domains = list(range(N))

    def conflicts(self, assignment):
        """Returns the number of conflicts in the current assignment."""
        count = 0

        for i in range(self.N):
            for j in range(i + 1, self.N):
                if (
                    assignment[i] == assignment[j]
                    or abs(assignment[i] - assignment[j]) == j - i
                ):
                    count += 1

        return count

    def min_conflicts(self, max_steps=1000):
        """Min-Conflicts algorithm to solve the N-Queens problem."""

        assignment = [
            random.choice(self.domains)
            for _ in range(self.N)
        ]

        for _ in range(max_steps):
            if self.conflicts(assignment) == 0:
                return assignment

            conflicted_vars = []

            for i in range(self.N):
                temp_assignment = assignment.copy()

                # Check whether this queen is involved in a conflict
                current_value = temp_assignment[i]

                for j in range(self.N):
                    if i != j:
                        if (
                            current_value == temp_assignment[j]
                            or abs(current_value - temp_assignment[j]) == abs(i - j)
                        ):
                            conflicted_vars.append(i)
                            break

            if not conflicted_vars:
                return assignment

            var = random.choice(conflicted_vars)

            min_conflict_value = min(
                self.domains,
                key=lambda val: self.conflicts(
                    assignment[:var] + [val] + assignment[var + 1:]
                )
            )

            assignment[var] = min_conflict_value

        return None


# Example usage
N = 8

nqueens = NQueensCSP(N)

solution = nqueens.min_conflicts()

if solution:
    print("Solution found:", solution)
else:
    print("No solution found within the maximum number of steps")