#sahi kiya hai, bas class main self kay saath mainay attributes nahi daalay, to
#19 20 ka farq hai ms say. 
class SaleData:
  def __init__(self):
    self.SaleID = ""
    self.Quantity = 0
    
CircularQueue = [SaleData() for i in range(5)]
Head = None
Tail = None
NumberOfItems = None

def initQueue():
  global Head,Tail,NumberOfItems
  for i in range(5):
    CircularQueue[i].SaleID = ""
    CircularQueue[i].Quantity = -1
    Head = 0
    Tail = 0
    NumberOfItems = 0

def Enqueue(data):
  global NumberOfItems,Tail
  if NumberOfItems == len(CircularQueue):
    return -1
  else:
    CircularQueue[Tail].Quantity = data.Quantity
    CircularQueue[Tail].SaleID = data.SaleID
    if Tail == 4:
      Tail = 0
      NumberOfItems += 1
      print(NumberOfItems)
      return 1
    else:
      Tail += 1
      NumberOfItems += 1
      return 1
        
def Dequeue():
    global NumberOfItems,Head
    data = SaleData()
    if NumberOfItems == 0:
      data.SaleID = ""
      data.Quantity = -1
      return 
    else:
      data.Quantity = CircularQueue[Head].Quantity
      data.SaleID = CircularQueue[Head].SaleID
      if Head == 4:
        Head = 0
        NumberOfItems =- 1
      else:
         Head += 1
         NumberOfItems -= 1
      return data
      
def EnterRecord():
  inData = SaleData()
  ID = input("Enter ID:")
  quantity = input("Enter quantity:")
  inData.SaleID = ID
  inData.Quantity = quantity
  ValueReturned = Enqueue(inData)
  if ValueReturned == -1:
    print("Full.")
  elif ValueReturned == 1:
    print("Stored.")
  else:
    print("Error.")

initQueue()

for i in range(6):
  EnterRecord()

Data = Dequeue()
if Data.Quantity == -1:
  print("Error:Queue is empty.")
else:
  print(Data.SaleID,"\t", Data.Quantity)
      
EnterRecord()

print("SaleID \t Quantity")

for i in range(5):
  print(CircularQueue[i].SaleID,"  \t  " ,CircularQueue[i].Quantity)
      
      

      
      
     
     