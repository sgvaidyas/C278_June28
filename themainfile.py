class Category:
    def setdata(self,cid=0):
        self.catId  = cid
        self.name   = input("Enter the category name = ")
        self.catdesc = input("Enter the category description = ")

    def display(self):
        print("CAT ID             = ",self.catId)
        print("CAT NAME           = ",self.name)
        print("CAT DESCRIPTION    = ",self.catdesc)

class Product:
    def setdata(self,cid=0):#222
        self.pid  = int(input("Enter the product id = "))
        self.pname   = input("Enter the product name = ")
        self.pdesc = input("Enter the product description = ")
        self.price   = float(input("Enter the product price = "))
        self.catid = cid
    def display(self):
        print("PRODUCT ID            = ",self.pid)
        print("PRODUCT NAME          = ",self.pname)
        print("PRODUCT DESCRIPTION   = ",self.pdesc)
        print("PRODUCT PRICE         = ",self.price)
        print("CAT ID                = ",self.catid)

flag=True
categorylist = []
productlist = []
while flag==True:
    print("1 ADD CATEGORY \n2 ADD PRODUCT \n3 PRODUCTS BASED ON CATEGORY NAME\n4 Product (low to high) \n5 EXIT ")
    ch = int(input("ENTER THE CHOICE = "))
    if ch==1:
        cid = int(input("Enter the Category Id = "))
        for cat in categorylist:
            if cid == cat.catId:
                print("Duplicate entry Please try again ")
                break
        else:
            ob = Category()
            ob.setdata(cid)
            #adding object of category into categorylist
            categorylist.append(ob)

    elif ch==2:
        #ask the user to specify the category id
        cid = int(input("Enter the Category Id to which you want add the product = "))
        #loop through the list of categories
        #each entity inside the list is object of category

        for cat in categorylist:
            #found the category in the list
            if cat.catId == cid:
                print("Please enter the product details for the category = ", cat.name)
                prod = Product()
                prod.setdata(cid)
                productlist.append(prod)
                break
        else:
            print("The category id does not exist , Do you want to add a new category ?")
            ch1 = int(input("1 = YES 2 NO"))
            if(ch1==1):
                for cat in categorylist:
                    if cid == cat.catId:
                        print("Duplicate entry Please try again ")
                        break
                else:
                    ob = Category()
                    ob.setdata(cid)
                    categorylist.append(ob)
                    prod = Product()
                    prod.setdata(ob.catId)
                    productlist.append(prod)
    elif ch==3:
        catname = input("Enter the Category name of which you want to display the products ")
        cid = 0
        for cat in categorylist:
            if cat.name == catname:
                cid = cat.catId   #222
                break
        else:
            print("No such category exists")
        if cid != 0:
            isFound=False
            for p in productlist:
                if p.catid == cid:
                    print("***********************************************")
                    p.display()
                    print("***********************************************")
                    isFound = True
            if isFound==False:
                print("No matching Products for the category mentioned !!!")

    elif ch==4:
        n = len(productlist)
        for i in range(n-1):
            for j in range(n-1-i):
                if productlist[j].price>productlist[j+1].price:
                    productlist[j],productlist[j+1] = productlist[j+1],productlist[j]
        print("SORTED PROD = PRICE : LOW TO HIGH ")
        for prod in productlist:
            prod.display()

    elif ch==5:
        flag=False

    print("the category list = ")
    for x in categorylist:
        x.display()
    print("the product list = ")
    for x in productlist:
        x.display()



