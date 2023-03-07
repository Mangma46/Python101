class Book:
    #Attribute
    NumberofBoox=0

    #Constructoe
    def __init__(self,title,price,page):
        self.title=title
        self.price=price
        self.page=page
        Book.NumberofBoox += 1
        print(f'The number of books in the shelf: {Book.NumberofBoox}')
        

   

class BuyBook(Book):
    def __init__(self,title,price,page,date,shop):
        super().__init__(title,price,page)
        self.Date=date
        self.shop=shop

    def showDetail(self):
        print(f'\nBook Name: {self.title}')
        print(f'Book Price: {self.price} Bath')
        print(f'Buy Date: {self.Date}')

    def readBook(self,readpage):
        if readpage > self.page:
            readpage = self.page

        self.page -= readpage
        print(f'\n{self.title} Remaining {self.page} page ')

    def sellBook(self,score,sellPrice):
        if score > 80 :
            ratting='***'
        elif score > 33 :
            ratting='**'
        else :
            ratting='*'

        print(f'\nIn my opinion rate this book: {ratting} star, I would like to sell this book for {sellPrice} baht. ')
        
        if (sellPrice-self.price)>0:
            print(f'You have gain profit {sellPrice-self.price} bath')
        elif(sellPrice-self.price)<0:
            print(f'You have loss profit {sellPrice-self.price} bath')
        else:
            print(f'You sell at cost')
        




Book01=BuyBook('Python101',20,85,'07-07-2023','Central Rama2')
Book02=BuyBook('Calculus2',125,123,'12-03-2023','Terminal21 Rama3')
Book03=BuyBook('Physics101',999,555,'23-01-2023','Central World')
Book01.readBook(15)
Book02.readBook(18)
Book01.showDetail()
Book03.sellBook(50,500)

