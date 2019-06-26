import tkinter
import math
cm=37.795
mm=cm/10
inch=2.54*cm
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
	def __init__(self,length="10",color="black",x1=100,y1=100,angle="0",label="",x2=0,y2=0,showLength=False):
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
	def draw(self):
		angleMeasure=""
		angleUnits=""
		for character in self.angle:
			if(character.isalpha()==0):
				angleMeasure=angleMeasure+character
		else:
			angleUnits=angleUnits+character
		angleUnits.lower()
		angleMeasure=int(angleMeasure)
		if(angleUnits=="d" or angleUnits==None):
			angleMeasure=math.radians(angleMeasure)
		sinValue=math.sin(angleMeasure)
		cosValue=math.cos(angleMeasure)
		individualLabels=["",""]
		lengthOfLabel=len(self.label)
		labelNumber=nthCharacter=0
		while nthCharacter<lengthOfLabel:
			if(self.label[nthCharacter]==','):
				labelNumber=labelNumber+1
			else:
				individualLabels[labelNumber]=individualLabels[labelNumber]+self.label[nthCharacter]
			nthCharacter=nthCharacter+1
		labelBeginX=int(self.x1-cosValue*8) #x coordinate of the label for beginning of the line
		labelBeginY=int(self.y1+sinValue*8)
		labelEndX=int(self.x2+cosValue*8) #x coordinate of the label for the endpoint of the line
		labelEndY=int(self.y2-sinValue*8)
		labelExpression=f'<text x="{labelBeginX}" y="{labelBeginY}" fill="{self.color}">{individualLabels[0]}</text>\n<text x="{labelEndX}" y="{labelEndY}" fill="{self.color}">{individualLabels[1]}</text>\n'
		file.write(labelExpression)
		lengthOfLength=len(self.length)*8
		textX=(self.x1+self.x2-lengthOfLength)/2 #x coordinate for text tag
		textY=(self.y1+self.y2+8)/2 #y coordinate for text tag
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
		self.y2=int(self.y1-(sinValue*measure)) #because it may get into non-terminating, non-reckering decimal values
		self.x2=int(self.x1+(cosValue*measure))
		file.write(f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.color}"/>\n')
		if(self.showLength==True):
			file.write(f'<text x="0" y="0" fill="{self.color}" transform="translate({textX} {textY}) rotate(-{angleMeasure} 0,0)" lengthAdjust="spacingAndGlyphs" textLength="{lengthOfLength}">{self.length}</text>\n')
