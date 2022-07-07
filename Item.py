from TextBox import TextBox
from Button import Button

class Item:
    def __init__(self, name, price, quantity, description="") -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    @staticmethod
    def SetProgramManager(programMan):
        global pm
        pm = programMan

    def ShowItem(self, i=0):
        currentY = 200 + 90 * i
        itemName = TextBox(50, currentY, 500, 50, text=self.name, textSize=20, textColour=(255, 255, 255), static=True, border=True)
        itemName.CenterTextY()
        
        itemPrice = TextBox(550, currentY, 100, 50, text=f"${self.price}", textSize=20, textColour=(255, 255, 255), static=True, border=True)
        itemPrice.CenterTextY()

        itemDescription = TextBox(50, currentY+50, 400, 35, text=self.description, textSize=14, textColour=(255, 255, 255), static=True, border=True)
        itemDescription.CenterTextY()

        itemQuantity = TextBox(550, currentY+50, 100, 35, text=f"x{self.quantity}", textSize=14, textColour=(255, 255, 255), static=True, border=True)
        itemQuantity.CenterTextY()

        addToCart = Button(650, currentY, 50, 45, self.AddToCart, text="+1", textSize=17, textColour=(255, 255, 255), bgColour=(50, 50, 50))
        removeFromCart = Button(650, currentY+45, 50, 40, self.RemoveFromCart, text="-1", textSize=17, textColour=(255, 255, 255), bgColour=(50, 50, 50))

        return [itemName, itemPrice, itemDescription, itemQuantity, addToCart, removeFromCart]

    def AddToCart(self):
        pm.AddToCart(self)

    def RemoveFromCart(self):
        pm.RemoveFromCart(self)
