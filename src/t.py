from sabertooth import instigate, line
instigate()
l1=line(angle="30d",label="A,B",points="P=1:3,Q=3:1",showPoints=True,forwardArrow="a1=1:0")
l2=line(v1=l1.P,angle="-45d",label=" ,R",forwardArrow="a1=1:1")
l3=line(v1=l1.Q,v2=l2.v2,extension1={"length":"5","direction":"forward","style":"dashed"})