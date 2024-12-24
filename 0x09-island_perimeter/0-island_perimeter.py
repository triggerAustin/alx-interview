#!/usr/bin/python3
"""
A module to compute an island perimeter.
"""


def island_perimeter(grid):
    """Computes the  total perimeter of an island"""
    total_perimeter = 0

    if not isinstance(grid, list):
        return 0

    num_rows = len(grid)

    for row_index, row in enumerate(grid):
        num_columns = len(row)

        for column_index, cell_value in enumerate(row):
            if cell_value == 0:
                continue

            open_edges = (
                row_index == 0 or
                (len(grid[row_index - 1]) > column_index and
                 grid[row_index - 1][column_index] == 0),

                column_index == num_columns - 1 or
                (num_columns > column_index + 1 and
                 row[column_index + 1] == 0),

                row_index == num_rows - 1 or
                (len(grid[row_index + 1]) > column_index and
                 grid[row_index + 1][column_index] == 0),

                column_index == 0 or
                row[column_index - 1] == 0
            )

            total_perimeter += sum(open_edges)

    return total_perimeter