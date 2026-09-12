def find_unit_clause(clauses):
    """Find a unit clause."""
    for clause in clauses:
        if len(clause) == 1:
            return clause[0]
    return None


def simplify_clauses(clauses, literal):
    """Simplify clauses by setting the literal to True."""
    simplified = []

    for clause in clauses:
        if literal in clause:
            continue

        new_clause = [l for l in clause if l != -literal]

        if not new_clause:
            return None

        simplified.append(new_clause)

    return simplified


def dpll(clauses, assignments):
    """DPLL algorithm for propositional model checking."""

    # Unit propagation
    while True:
        unit = find_unit_clause(clauses)

        if unit is None:
            break

        if unit not in assignments:
            assignments.append(unit)

        clauses = simplify_clauses(clauses, unit)

        if clauses is None:
            return None

    # All clauses are satisfied
    if not clauses:
        return assignments

    # Choose a literal
    literal = clauses[0][0]

    # Try literal as True
    new_clauses = simplify_clauses(clauses, literal)

    if new_clauses is not None:
        result = dpll(new_clauses, assignments + [literal])

        if result is not None:
            return result

    # Try literal as False
    new_clauses = simplify_clauses(clauses, -literal)

    if new_clauses is not None:
        result = dpll(new_clauses, assignments + [-literal])

        if result is not None:
            return result

    return None


def main():
    # Variables
    A, B, C = 1, 2, 3

    # CNF:
    # (A OR B) AND (NOT A OR C) AND (NOT B OR NOT C)

    clauses = [
        [A, B],
        [-A, C],
        [-B, -C]
    ]

    # Initial assignments
    assignments = []

    # Run DPLL
    result = dpll(clauses, assignments)

    if result is not None:
        print("SATISFIABLE")
        print("Assignments:", result)

        # Display assignments clearly
        for literal in result:
            if literal == A:
                print("A = True")
            elif literal == -A:
                print("A = False")
            elif literal == B:
                print("B = True")
            elif literal == -B:
                print("B = False")
            elif literal == C:
                print("C = True")
            elif literal == -C:
                print("C = False")
    else:
        print("UNSATISFIABLE")


if __name__ == "__main__":
    main()