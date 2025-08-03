class Matrix:
    """Interface of a matrix.

    This class provides only the matrix size N and a method for swapping
    two items. The actual storage of the matrix in memory is provided by
    subclasses in testing code.
    """

    def __init__(self, N):
        self.N = N

    def swap(self, i1, j1, i2, j2):
        """Swap elements (i1,j1) and (i2,j2)."""

        # Overridden in subclasses
        raise NotImplementedError

    def transpose(self):
        """Transpose the matrix."""
        
        # TODO: Implement more efficiently
        # for i in range(self.N):
        #     for j in range(i):
        #         self.swap(i, j, j, i)
        def _trans_swap(i, j, height, width):
            if width + height == 2:
                self.swap(j, i, i, j)
            elif width >= height:
                r_width = width // 2
                l_width = width - r_width

                _trans_swap(j, i, l_width, height)
                _trans_swap(j + l_width, i, r_width, height)
            else:
                _trans_swap(j, i, width, height)

        def _trans(i, j, width):
            if width > 1:
                r_width = width // 2
                l_width = width - r_width

                _trans(i, j, l_width) 
                _trans_swap(i + l_width, j, r_width, l_width) 
                _trans(i + l_width, j + l_width, r_width) 

        _trans(0, 0, self.N) 
