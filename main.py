cost = int(input("cost: "))
tax = int(input("tax rate: "))
quantity = int(input("quantity: "))
def totalcost():
  global cost
  cost = (cost*quantity)+(cost*quantity)*tax/100
  print(cost)
totalcost()