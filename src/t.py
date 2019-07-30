from sabertooth import instigate, line
instigate()
l1=line(angle="15d",length="10",label="A,B",points="p1=1:1")
l2=line(angle="30d",length="10",label=" ,C",points="p2=1:1")
l3=line(v1=l1.p1,v2=l2.p2)