# %%
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        # only run once, if length changed later, diagonal wont update
        # to do this, create a property
        # self.diagonal = (self.length**2 + self.breadth**2)**0.5

    # if some task is very complex, create a normal function for it, dont use @property
    @property
    def diagnoal(self):
        return self.diagonal = (self.length**2 + self.breadth**2)**0.5
    
    def area(self):
        return (self.length*self.breadth)

    def paramter(self):
        return 2*(self.length+self.breadth)
# %%
