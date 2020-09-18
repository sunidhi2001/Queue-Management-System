import cv2
from functools import reduce

def scan(p):
    x = f"{p}.png"
    img = cv2.imread(x)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    z=data.split("-")[1]
    return(int(z))

pl = ["salt","sugar","rice","oil","soap"]

W = ''' WELCOME TO BIG BAZAAR...
HERE ARE SOME TIPS FOR MAKING YOUR SHOPPING EASY
1)take a smart trolley.
2)search for the products you are intrested in.
3)scan the QR code of the product with scanner mounted in the trolley.
4)collect back your item buy paying the final amount via online payment.
5)for payment scan the gpay code pasted on the trolley.
6)thank you enjoy your shopping.'''
print(W)
l=[]
while 1:
    print(f"products are:{pl}")
    i = input("enter the product name from above list or press e to exit and show your bill: ")
    if i == "e":
        break
    elif i not in pl:
        print("you have opted for an invalid product")
    else:
        print("product sucessfull added, select next")
        l.append(scan(i))
print(l)
amount=reduce(lambda x,y:x+y,l)
print(f"your final amount is Rs.{amount}")
print("PLEASE PAY THE AMOUNT AND TAKE AWAY YOUR ITEMS")
print("thank you for visiting our store!!!")