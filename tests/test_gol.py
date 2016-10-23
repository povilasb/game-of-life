from hamcrest import assert_that, is_, is_not, is_in, equal_to

import gol
from gol import Grid


def describe_neighbours():
    def it_returns_list_of_neighbour_cells():
        cells = set(gol.neighbours((5, 5)))

        assert_that(cells, is_(set([
            (4, 4), (5, 4), (6, 4),
            (4, 5), (6, 5),
            (4, 6), (5, 6), (6, 6),
        ])))

def describe_grid():
    def describe_live_neighbours():
        def it_returns_count_of_cell_neighbours():
            grid = Grid((0, 0), (1, 0), (2, 0))

            assert_that(grid.live_neighbours((1, 0)), is_(2))

    def describe_newborns():
        def it_returns_cells_that_will_be_born_if_it_is_surrounded_by_3_living_cells():
            new_cells = list(Grid((0, 0), (2, 0), (0, 2)).newborns())

            assert_that(new_cells, is_([(1, 1)]))

        def describe_when_all_cells_are_surounded_by_3_neighbours():
            def it_returns_empty_set():
                new_cells = list(
                    Grid((0, 0), (1, 0), (0, 1), (1, 1)).newborns())

                assert_that(new_cells, is_([]))

    def describe_next_generation():
        def describe_when_grid_is_empty():
            def it_returns_new_empty_grid():
                grid = Grid().next_generation()

                assert_that(grid, equal_to(Grid()))

        def describe_when_cell_has_two_neighbours():
            def it_stays_alive():
                grid = Grid((0, 0), (1, 1), (2, 2)).next_generation()

                assert_that(grid, equal_to(Grid((1, 1))))

        def describe_when_cell_has_three_neighbours():
            def it_stays_alive():
                grid = Grid((0, 0), (1, 0), (0, 1), (1, 1)).next_generation()

                assert_that(grid,
                            equal_to(Grid((0, 0), (1, 0), (0, 1), (1, 1))))

        def describe_when_living_cell_has_more_than_three_neighbours():
            def it_dies():
                grid = Grid((0, 0), (1, 1), (1, 2), (2, 1), (2, 2)).next_generation()

                assert_that((1, 1), is_not(is_in(grid._cells)))

        def describe_when_cell_has_less_than_two_neighbours():
            def it_stays_dies():
                grid = Grid((0, 0), (1, 0)).next_generation()

                assert_that(grid, equal_to(Grid()))

        def describe_when_dead_cell_has_three_neighbours():
            def it_becomes_alive():
                grid = Grid((0, 0), (2, 0), (0, 2)).next_generation()

                assert_that(grid, is_(Grid((1, 1))))

    def describe_crop():
        def describe_when_grid_is_empty():
            def it_returns_empty_grid():
                cropped = Grid().crop(10, 10)

                assert_that(cropped, equal_to(Grid()))

        def describe_when_grid_has_no_elemments_outside_the_matrix():
            def it_returns_grid_with_the_same_elements():
                cropped = Grid((9, 9)).crop(10, 10)

                assert_that(cropped, equal_to(Grid((9, 9))))

        def it_removes_element_that_are_outside_the_crop_matrix():
            cropped = Grid((1, 1), (10, 9), (-1, 0), (0, -1), (9, 10)).crop(10, 10)

            assert_that(cropped, equal_to(Grid((1, 1))))
