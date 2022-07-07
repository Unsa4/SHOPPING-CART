from Item import Item

class ItemManager:
    def __init__(self) -> None:
        self.itemList = []
        with open("Assets/ItemList.txt", 'r') as itemFile:
            items = itemFile.read().split("\n")
            for item in items:
                if item:
                    item = item.split(",")
                    self.itemList.append(Item(item[0], item[1], item[2], item[3]))

    def GetItems(self):
        return self.itemList