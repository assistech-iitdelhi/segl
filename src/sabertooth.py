import tkinter
import math
root = tkinter.Tk()
root.withdraw()
screenWidth,screenHeight= root.winfo_screenwidth(), root.winfo_screenheight()
cm=screenWidth/40.64
mm=cm/10
inch=2.54*cm
path="draw.html"
file=open(path,"w+")

def instigate(width=screenWidth,height=screenHeight):
	width=str(width)
	height=str(height)
	file.write('<svg width="'+width+'" height="'+height+'">\n<marker id="m2" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto">\n<circle cx="5" cy="5" r="2" fill="black"/>\n</marker>\n')

class line:
	def __init__(self,length="10",color="black",x1=screenWidth/2,y1=screenHeight/2,angle="0",label=" , ",x2=None,y2=None,showLength=False,style="",extension1={},extension2={},width=None,v1=(screenWidth/2,screenHeight/2),v2=None,points=""):
		self.points=points
		self.width=width
		self.extension1=extension1
		self.extension2=extension2
		self.style=style
		self.showLength=showLength
		self.label=label
		self.angle=angle #angle at x1y1
		self.length=length
		self.color=color
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
		self.v1=v1
		self.v2=v2
		if(self.v1!=(screenWidth/2,screenHeight/2)):
			self.x1,self.y1=self.v1
		else:
			self.v1=(self.x1,self.y1)
		self.draw() #draws the line

	def handlePoints(self):
		point=self.points.split(",")
		for p in point:
			s=p.split("=")
			ratio=s[1].split(":")
			ratio[0]=int(ratio[0])
			ratio[1]=int(ratio[1])
			x=self.x1+((self.x2-self.x1)*ratio[0]/(ratio[0]+ratio[1]))
			y=self.y1+((self.y2-self.y1)*ratio[0]/(ratio[0]+ratio[1]))
			setattr(self, s[0], (x,y))
			file.write(f'<path d="M {x},{y} h 1" marker-start="url(#m2)"/>\n')

	def returnStyleInfo(self):
		if((self.style).lower()=="dashed"):
			styleInfo='stroke-dasharray="5 2" '
		else:
			styleInfo=""
		return styleInfo
	def handleAngle(self):
		angleMeasure=""
		angleUnits=""
		for character in self.angle:
			if(character.isalpha()==0):
				angleMeasure=angleMeasure+character
		else:
			angleUnits=angleUnits+character
		angleUnits.lower()
		angleMeasure = 0-float(angleMeasure)
		if(angleUnits=="d" or angleUnits==""):
			sinValue=math.sin(math.radians(angleMeasure))
			cosValue=math.cos(math.radians(angleMeasure))
		else:
			sinValue=math.sin(angleMeasure)
			cosValue=math.cos(angleMeasure)
			angleMeasure = math.degrees(angleMeasure)
		return cosValue,sinValue,angleMeasure

	def handleLine(self):
		cosValue,sinValue,angleMeasure=self.handleAngle()
		measure=""
		units=""
		for character in self.length:
			if(character.isalpha()==0):
				measure=measure+character
			else:
				units=units+character
		units.lower()
		if(units=="cm"):
			measure=int(float(measure)*cm)
		elif(units=="inch"):
			measure=int(float(measure)*inch)
		elif(units=="mm"):
			measure=int(float(measure)*mm)
		else:
			measure=int(float(measure)*cm)
		return measure

	def handleLabel(self):
		cosValue,sinValue,angleMeasure=self.handleAngle()
		individualLabels=self.label.split(',')
		labelBeginX=int(self.x1-cosValue*8) #x coordinate of the label for beginning of the line
		labelBeginY=int(self.y1+sinValue*8)
		labelEndX=int(self.x2+cosValue*8) #x coordinate of the label for the endpoint of the line
		labelEndY=int(self.y2-sinValue*8)
		labelExpression=f'<text x="{labelBeginX}" y="{labelBeginY}" fill="{self.color}">{individualLabels[0]}</text>\n<text x="{labelEndX}" y="{labelEndY}" fill="{self.color}">{individualLabels[1]}</text>\n'
		file.write(labelExpression)

	def handleLength(self):
		cosValue,sinValue,angleMeasure=self.handleAngle()
		lengthOfLength=len(self.length)*8
		textX=(self.x1+self.x2-lengthOfLength)/2 #x coordinate for text tag
		textY=(self.y1+self.y2+8)/2 #y coordinate for text tag
		if(self.showLength==True):
			file.write(f'<text x="0" y="0" fill="{self.color}" transform="translate({textX} {textY}) rotate(-{angleMeasure} 0,0)" lengthAdjust="spacingAndGlyphs" textLength="{lengthOfLength}">{self.length}</text>\n')

	def handleExtension(self):
		if(not self.extension1=={}):
			if(self.extension1[direction]=="backward"):
				e1=line(color=self.color,x1=self.x1,y1=self.y1,length=self.extension1[length],style=self.extension1[style],angle=self.angle)
			else:
				e1=line(color=self.color,x1=self.x2,y1=self.y2,style=self.extension1[style],length=self.extension1[length],angle=self.angle)
		if(not self.extension2=={}):
			if(self.extension2[direction]=="backward"):
				e2=line(color=self.color,x1=self.x1,y1=self.y1,length=self.extension2[length],style=self.extension2[style],angle=self.angle)
			else:
				e2=line(color=self.color,x1=self.x2,y1=self.y2,length=self.extension2[length],style=self.extension2[style],angle=self.angle)

	def handleWidth(self):
		if(self.width==None):
			widthExpression=""
		else:
			widthExpression=f'stroke-width="{self.width}" '
		return widthExpression

	def draw(self):
		styleInfo,measure,widthExpression=self.returnStyleInfo(),self.handleLine(),self.handleWidth()
		cosValue,sinValue,angleMeasure=self.handleAngle()
		if(self.v2!=None):
			self.x2,self.y2=self.v2
		else:
			if(self.y2==None):
				self.y2=int(self.y1+(sinValue*measure)) #because it may get into non-terminating, non-reckering decimal values
			if(self.x2==None):
				self.x2=int(self.x1+(cosValue*measure))
			self.v2=(self.x2,self.y2)
		file.write(f'<line x1="{self.x1}" {styleInfo} {widthExpression} y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.color}"/>\n')
		self.handleLabel()
		self.handleLength()
		self.handleExtension()
		if(self.points!=""):
			self.handlePoints()