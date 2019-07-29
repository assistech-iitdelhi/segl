from sabertooth import instigate, line
instigate()
l1=line(angle="15d",length="10",label="A,B")
l2=line(angle="30d",length="10",label=" ,C")
l3=line(angle="0d",length="10",label=" ,D")
l4=line(v1=l2.v2,v2=l1.v2)
l5=line(v1=l2.v2,v2=l3.v2)