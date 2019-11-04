
class Grid:
    media = '@media (max-width : {}px) {'
    def __init__(self,number_of_columns,break_points,prefix='col',output_file='grid.css'):
        self.number_of_columns = number_of_columns
        self.set_break_points(break_points)
        self.output_file = output_file
        self.prefix = prefix
 
    def set_break_points(self,break_points):
        if self.is_valid_format(break_points):
            self.break_points = break_points
        else:
            raise ValueError('Breakpoints Bad Format')
    
    def is_valid_format(self,break_points):
        return isinstance(break_points,dict) and all(isinstance(v,int) for v in break_points.values())

                