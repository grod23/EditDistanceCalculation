class Calculation:
    def __init__(self):
        self.distance = 0
        self.matrix = []
        self.alignment = []

    def calculate_edit_distance(self, word_1, word_2):
        """Calculate edit distance using (Levenshtein distance)"""
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
                align_1.append('_')
                align_2.append(word_2[j - 1])
                j -= 1
            else:
                # Deletion
                align_1.append(word_1[i - 1])
                align_2.append('_')
                i -= 1

        self.alignment = [''.join(reversed(align_1)), ''.join(reversed(align_2))]

    def display_matrix(self, word_1, word_2):
        """Return the edit distance matrix as a formatted string instead of printing."""
        output = []

        # Header row
        header = "    " + "    ".join([' '] + list(word_2))
        output.append(header)

        # Add dashed separator line
        dash_length = len(header)
        output.append("-" * dash_length)

        # Matrix rows
        for i, row in enumerate(self.matrix):
            # Row label
            if i == 0:
                row_label = "  |"
            else:
                row_label = f"{word_1[i - 1]} |"

            # Matrix values
            row_values = " : ".join(f"{val:2d}" for val in row)

            output.append(row_label + row_values)

        # Return entire matrix as a single string
        print("\n".join(output))
        return "\n".join(output)

    def display_alignment(self):
        alignment_display = f"\nOptimal Alignment: {self.distance}\n {self.alignment[0]}\n {self.alignment[1]}"
        return alignment_display


