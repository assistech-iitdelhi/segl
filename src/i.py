from sabertooth import instigate, line
instigate()
l1=line(length="5cm",label="A,B",color="red",points="P=1:1",showPoints=True)
l2=line(v1=l1.P,angle="90d")
l3=line(x1=10,y1=10,x2=210,y2=10)