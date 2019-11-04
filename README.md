
# css-grid

A simple python script to generate a css grid.

Installation
------------
For now just clone the repo ! ( Will eventually make it a cli-tool)

Example
-------------------
```python
    # generate a 12 grid column with three breakpoints
    g = Grid(12,{"sm": 600, "md": 900, "lg": 1200})
    g.generate_grid()
```
