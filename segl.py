
try:# work with both python 2 and 3
	import Tkinter as tk
except ImportError:
	import tkinter as tk

root = tk.Tk()
W = 200
H = 200
canvas = tk.Canvas(root, width=W, height=H, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
objs = []

class Rectangle:
	def __init__(self, 
			vertices=['v1', 'v2', 'v3', 'v4'],
			length=80,
			width=80):
		self.vertices = vertices
		self.v1 = (0+W*0.20, 0+H*0.20)
		self.v3 = (0+W*0.80, 0+H*0.80)	
		self.v2 = self.v1[0], self.v3[1]		
		self.v4 = self.v3[0], self.v1[0]
			
		self.length = length
		self.width = width
		objs.append(self)
		
	def draw(self):
		canvas.create_rectangle(self.v1[0], self.v1[1], 
					self.v3[0], self.v3[1],
					outline="#DDD", width=4)
		
class Circle:
	def __init__(self, 
			center=['c1'],
			radius=80):			
		self.center = center
		self.radius = radius
		objs.append(self)
		
	def draw(self):
		canvas.create_oval(self.center[0]-self.radius, 
				   self.center[1]-self.radius,
				   self.center[0]+self.radius, 
				   self.center[1]+self.radius,
				   outline="#DDD", width=4)
		
def draw():
	for o in objs:
		o.draw()
	root.mainloop()
	