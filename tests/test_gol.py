from hamcrest import assert_that, is_, is_not, is_in

import gol


def describe_next_generation():
    def describe_when_grid_is_empty():
        def it_returns_new_empty_grid():
            grid = gol.next_generation(gol.make_grid())

            assert_that(grid, is_(gol.make_grid()))

    def describe_when_cell_has_two_neighbours():
        def it_stays_alive():
            grid = gol.next_generation(gol.make_grid((0, 0), (1, 1), (2, 2)))

            assert_that(grid, is_(gol.make_grid((1, 1))))

    def describe_when_cell_has_three_neighbours():
        def it_stays_alive():
            grid = gol.next_generation(gol.make_grid((0, 0), (1, 0), (0, 1), (1, 1)))

            assert_that(grid,
                        is_(gol.make_grid((0, 0), (1, 0), (0, 1), (1, 1))))

    def describe_when_living_cell_has_more_than_three_neighbours():
        def it_dies():
            grid = gol.next_generation(
                gol.make_grid((0, 0), (1, 1), (1, 2), (2, 1), (2, 2)))

            assert_that((1, 1), is_not(is_in(grid)))

    def describe_when_cell_has_less_than_two_neighbours():
        def it_stays_dies():
            grid = gol.next_generation(gol.make_grid((0, 0), (1, 0)))

            assert_that(grid, is_(gol.make_grid()))

    def describe_when_dead_cell_has_three_neighbours():
        def it_becomes_alive():
            grid = gol.next_generation(gol.make_grid((0, 0), (2, 0), (0, 2)))

            assert_that(grid, is_(gol.make_grid((1, 1))))

def describe_live_neighbours():
    def it_returns_count_of_cell_neighbours():
        grid = gol.make_grid((0, 0), (1, 0), (2, 0))

        assert_that(gol.live_neighbours(grid, (1, 0)), is_(2))

def describe_neighbours():
    def it_returns_list_of_neighbour_cells():
        cells = set(gol.neighbours((5, 5)))

        assert_that(cells, is_(set([
            (4, 4), (5, 4), (6, 4),
            (4, 5), (6, 5),
            (4, 6), (5, 6), (6, 6),
        ])))

def describe_newborns():
    def it_returns_cells_that_will_be_born_if_it_is_surrounded_by_3_living_cells():
        new_cells = list(gol.newborns(gol.make_grid((0, 0), (2, 0), (0, 2))))

        assert_that(new_cells, is_([(1, 1)]))

    def describe_when_all_cells_are_surounded_by_3_neighbours():
        def it_returns_empty_set():
            new_cells = list(
                gol.newborns(gol.make_grid((0, 0), (1, 0), (0, 1), (1, 1)))
            )

            assert_that(new_cells, is_([]))

def describe_crop_grid():
    def describe_when_grid_is_empty():
        def it_returns_empty_grid():
            cropped = gol.crop_grid(gol.make_grid(), 10, 10)

            assert_that(cropped, is_(gol.make_grid()))

    def describe_when_grid_has_no_elemments_outside_the_matrix():
        def it_returns_grid_with_the_same_elements():
            cropped = gol.crop_grid(gol.make_grid((9, 9)), 10, 10)

            assert_that(cropped, is_(gol.make_grid((9, 9))))

    def it_removes_element_that_are_outside_the_crop_matrix():
        cropped = gol.crop_grid(
            gol.make_grid((1, 1), (10, 9), (-1, 0), (0, -1), (9, 10)), 10, 10)

        assert_that(cropped, is_(gol.make_grid((1, 1))))
