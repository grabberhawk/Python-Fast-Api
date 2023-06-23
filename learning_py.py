myDICT={
    "Fast": "A series of movies",
    "David": "jounior",
     "list" : [1,4,'string'],
     1: 89
}
#list=["price","should Be ","paid",234]
tuple=(1,3,4)
#cant update index values
myDICT['list']=[75,"yo!"]
#print(list)
print(myDICT)

updateDict={
    "Song":"A time In HAvana"
}
myDICT.update(updateDict)
myDICT.update({"Friend" : "ShashiDhar"})
print(myDICT)
print(myDICT.values())
print(myDICT.keys())
#print(myDICT["API"]) #throws error code Break
print(myDICT.get("API")) #while this does'nt
print(list(myDICT.keys()))
#CLASS SET
a={1,2,5,2} # non -repeatative terms store
print(a)
b=set () #initialize empty set
b.add(5)
b.add(7)
print(b)

i=7
while i<10:
    i=i+1
    print("oH God")
    
fruits=['banana','apple','WaterMelon']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1                       
    
for item in fruits:
    print(item) 

    
for i in range(100,107,2):        #(ini,final+1,++i)by default intial pos= 0,
    print(i)       
    
for i in range(5):
    print(i)
    if(i==3):
        break
else:
    print("Loop Breaks") #prints during successful execution  here doesn't run      
def sum(a,b) :
    return (a+b)/2
print(sum(6,7))
def greet(name):
    print("GooD Morning "+name)
    
(greet("DAVID"))
def fun2():
    print("GOD mOVEMENT")
fun2()