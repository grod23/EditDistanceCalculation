class Calculation:
    def __init__(self):
        self.distance = 0
        self.matrix = []
        self.alignment = []

    def calculate_edit_distance(self, word_1, word_2):
        """Calculate edit distance using dynamic programming (Levenshtein distance)"""
        rows = len(word_1) + 1
        cols = len(word_2) + 1

        # Initialize matrix
        self.matrix = [[0] * cols for _ in range(rows)]

        # Initialize first row and column
        for i in range(rows):
            self.matrix[i][0] = i
        for j in range(cols):
            self.matrix[0][j] = j

        # Fill the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if word_1[i - 1] == word_2[j - 1]:
                    cost = 0
                else:
                    cost = 1

                self.matrix[i][j] = min(
                    self.matrix[i - 1][j] + 1,  # deletion
                    self.matrix[i][j - 1] + 1,  # insertion
                    self.matrix[i - 1][j - 1] + cost  # substitution
                )

        self.distance = self.matrix[rows - 1][cols - 1]
        self._traceback(word_1, word_2)

        return self.distance, self.matrix

    def _traceback(self, word_1, word_2):
        """Traceback to find optimal alignment"""
        i = len(word_1)
        j = len(word_2)
        align_1 = []
        align_2 = []

        while i > 0 or j > 0:
            if i > 0 and j > 0 and word_1[i - 1] == word_2[j - 1]:
                align_1.append(word_1[i - 1])
                align_2.append(word_2[j - 1])
                i -= 1
                j -= 1
            elif i > 0 and j > 0 and self.matrix[i][j] == self.matrix[i - 1][j - 1] + 1:
                # Substitution
                align_1.append(word_1[i - 1])
                align_2.append(word_2[j - 1])
                i -= 1
                j -= 1
            elif j > 0 and self.matrix[i][j] == self.matrix[i][j - 1] + 1:
                # Insertion
                align_1.append('-')
                align_2.append(word_2[j - 1])
                j -= 1
            else:
                # Deletion
                align_1.append(word_1[i - 1])
                align_2.append('-')
                i -= 1

        self.alignment = [''.join(reversed(align_1)), ''.join(reversed(align_2))]

    def display_matrix(self, word_1, word_2):
        """Display the edit distance matrix"""
        print("\nEdit Distance Matrix:")
        print("     ", end="")
        print("  ".join([' '] + list(word_2)))

        for i, row in enumerate(self.matrix):
            if i == 0:
                print(f"  ", end="")
            else:
                print(f"{word_1[i - 1]} ", end="")
            print("  ".join(f"{val:2d}" for val in row))

    def display_alignment(self):
        """Display the optimal alignment"""
        print("\nOptimal Alignment:")
        print(self.alignment[0])
        print(self.alignment[1])

        # Show match indicators
        match_line = ""
        for c1, c2 in zip(self.alignment[0], self.alignment[1]):
            if c1 == c2:
                match_line += "|"
            elif c1 == '-' or c2 == '-':
                match_line += " "
            else:
                match_line += "x"
        print(match_line)

