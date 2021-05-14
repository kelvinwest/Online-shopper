

class objects:

    def __init__(self, name = None , price = None , quality = None ):
        self.name = name
        self.price = price
        self.quality = quality
        self.items = []
        #self.items=[ name , price ]

    def getName( self ):
        return self.name

    def getPrice( self ):
        return self.price

    def commonObjects( self , item ):
        item.append(objects('bicycle',100.99,2))
        item.append(objects('backpack', 22.99,3))
        item.append(objects('umbrella', 6.99,2))
        item.append(objects('snowboard', 54.99,2))
        item.append(objects('baseball bat', 29.99,2))
        item.append(objects('baseball glove', 14.84,3))
        item.append(objects('skateboard', 49.99,3))
        item.append(objects('spoon', 12.15,5))
        item.append(objects('bowl', 9.88,4))
        item.append(objects('pizza', 12.99,2))
        item.append(objects('donut', 5.79,3))
        item.append(objects('cake', 16.48,4))
        item.append(objects('sandwich', 4.98,3))
        item.append(objects('orange', 2.98,4))
        item.append(objects('broccolli', 3.74,3))
        item.append(objects('chair', 75.95,4))
        item.append(objects('couch', 399.95,3))
        item.append(objects('potted plant', 84.99,5))
        item.append(objects('bed', 229.95,1))
        item.append(objects('mirror', 128.99,3))
        item.append(objects('window', 168.00,3))
        item.append(objects('tennis racket', 16.99,2))
        item.append(objects('plate', 2.19,3))
        item.append(objects('desk', 54.99,2))
        item.append(objects('laptop', 549.99,2))
        item.append(objects('cell phone', 648.99,4))
        item.append(objects('clock', 75.52,4))
        item.append(objects('scissors', 9.88,3))
        item.append(objects('tooth brush', 24.99,4))
        item.append(objects('hair brush', 15.45,2))
        item.append(objects('hair drier', 59.99,4))
        item.append(objects('blender', 79.99,4))
        item.append(objects('toaster', 49.95,3))
        item.append(objects('fork', 5.00,4))
        item.append(objects('knife', 2.97,1))
        item.append(objects('tv',199.99,3))
        # print("item in obj", item[0].getName(), item[0].getPrice() )
        # print("items in obj", self.items[0].getName(), self.items[0].getPrice() )
        return item

# obj3 = objects()
# obj4=objects()
# print("Whats happening")
# item=[]
# obj4 = obj3.commonObjects(item)
# print("len obj4", len(obj4))
# for i in range(0,35):
#     print("item from db",obj4[i].getName(),obj4[i].getPrice())


