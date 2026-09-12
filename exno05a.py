class PropositionalLogic:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def pl_resolution(self):
        """Perform propositional logic resolution to determine satisfiability."""
        while True:
            new = set()
            n = len(self.clauses)

            # Generate all pairs of clauses
            pairs = [
                (self.clauses[i], self.clauses[j])
                for i in range(n)
                for j in range(i + 1, n)
            ]

            for ci, cj in pairs:
                resolvents = self.pl_resolve(ci, cj)

                # Empty clause means unsatisfiable
                if [] in resolvents:
                    return False

                for res in resolvents:
                    new.add(tuple(sorted(res)))

            # If no new clauses are generated, it is satisfiable
            existing = set(tuple(sorted(clause)) for clause in self.clauses)

            if new.issubset(existing):
                return True

            # Add new clauses
            for clause in new:
                clause_list = list(clause)
                if tuple(clause) not in existing:
                    self.clauses.append(clause_list)

    def pl_resolve(self, ci, cj):
        """Resolve two clauses to produce a set of resolvents."""
        resolvents = []

        for di in ci:
            for dj in cj:
                if di == -dj:
                    resolvent = list((set(ci) - {di}) | (set(cj) - {dj}))

                    # Avoid tautological clauses
                    if not any(-literal in resolvent for literal in resolvent):
                        resolvents.append(resolvent)

        return resolvents


# Example usage
pl = PropositionalLogic()

# Adding clauses:
# (A OR B) AND (NOT A OR C) AND (NOT B OR NOT C)

pl.add_clause([1, 2])       # A OR B
pl.add_clause([-1, 3])      # NOT A OR C
pl.add_clause([-2, -3])     # NOT B OR NOT C

# Checking for satisfiability
is_satisfiable = pl.pl_resolution()

if is_satisfiable:
    print("The knowledge base is satisfiable.")
else:
    print("The knowledge base is not satisfiable.")