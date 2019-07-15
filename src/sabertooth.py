import tkinter
import math
direction,length,style="direction","length","style"
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
	file.write('<svg width="'+width+'" height="'+height+'">\n')

class line:
	def __init__(self,length="10",color="black",x1=100,y1=100,angle="0",label=" , ",x2=0,y2=0,showLength=False,style="",extension1={},extension2={}):
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
		self.draw() #draws the line
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
		angleMeasure = float(angleMeasure)
		if(angleUnits=="d" or angleUnits==None):
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

	def draw(self):
		styleInfo,measure=self.returnStyleInfo(),self.handleLine()
		cosValue,sinValue,angleMeasure=self.handleAngle()
		self.y2=int(self.y1-(sinValue*measure)) #because it may get into non-terminating, non-reckering decimal values
		self.x2=int(self.x1+(cosValue*measure))
		file.write(f'<line x1="{self.x1}" {styleInfo}y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.color}"/>\n')
		self.handleLabel()
		self.handleLength()
		self.handleExtension()