
class Grid:
    media = '@media (max-width : {}px) {'
    def __init__(self,number_of_columns,break_points,prefix='col',output_file='grid.css'):
        self.number_of_columns = number_of_columns
        self.set_breakpoints(break_points)
        self.output_file = output_file
        self.prefix = prefix
    
    def generate_grid(self):
        with open(self.output_file,'w') as out:
            # add a grid class
            print(f".grid {{\n  display:grid;\n}}",file=out);
            
            # print all possible column combinations
            for k,v in self.break_points.items():
                print(f"@media (max-width: {v}px) {{",file=out)
                for i in range(1, self.number_of_columns + 1):
                    for j in range(i+1, self.number_of_columns + 1):
                        print(f"  .{self.prefix}-{k}-{i}-{j} {{\n"
                        f"    grid-column: {i} \ {j};\n"
                        f"  }}",file=out)
                print(f"}}",file=out)
    
    def set_breakpoints(self,break_points):
        if self.is_valid_format(break_points):
            self.break_points = break_points
        else:
            raise ValueError('Breakpoints Bad Format')
    
    def is_valid_format(self,break_points):
        return isinstance(break_points,dict) and all(isinstance(v,int) for v in break_points.values())

# g = Grid(12,{"sm": 600, "xs": 400, "md": 900, "lg":1200})
# g.generate_grid()
