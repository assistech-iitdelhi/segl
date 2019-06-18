import tkinter
import math
root = tkinter.Tk()
root.withdraw()
screenWidth,screenHeight= root.winfo_screenwidth(), root.winfo_screenheight()
path="draw.html"
file=open(path,"w+")

def instigate(width=screenWidth,height=screenHeight):
	width=str(width)
	height=str(height)
	file.write('<svg width="'+width+'" height="'+height+'">\n')

class line:
	def __init__(self,measurement="",length=80,color="black",x1=100,y1=100,angle=0):
		self.angle=angle #angle at x1y1
		self.measurement=measurement
		self.length=length
		self.color=color
		self.x1=x1
		self.y1=y1
		self.draw() #draws the line
	def draw(self):
		sinValue=math.sin(math.radians(self.angle))
		cosValue=math.cos(math.radians(self.angle))
		y2=int(self.y1-(sinValue*self.length)) #because it may get into non-terminating, non-reckering decimal values
		x2=int(self.x1+(cosValue*self.length))
		textX=(self.x1+x2)/2 #x coordinate for text tag
		textY=(self.y1+y2)/2+10 #y coordinate for text tag
		textX=str(textX)
		textY=str(textY)
		self.x1=str(self.x1)
		x2=str(x2)
		self.y1=str(self.y1)
		y2=str(y2)
		file.write('<line x1="'+self.x1+'" y1="'+self.y1+'" x2="'+x2+'" y2="'+y2+'" stroke="'+self.color+'"/>\n')
		lengthOfMeasurement=len(self.measurement)*8
		lengthOfMeasurement=str(lengthOfMeasurement)
		file.write('<text x="'+textX+'" y="'+textY+'" fill="'+self.color+'" transform="rotate(-'+self.angle+' 0,0)" lengthAdjust="spacingAndGlyphs" textLength="'+lengthOfMeasurement+'">'+self.Measurement+'</text>\n')
