d1={"a":2,"b":2,"c":3,"d":4}
d2={"a":1,"b":2,"c":3,"d":5}
d3=dict()
for val in d1:
    if(val in d2 and d1[val]==d2[val]):
        d3[val]=d1[val]
print(d3)

