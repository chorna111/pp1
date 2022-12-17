
class BOOK:
    def __init__(self,title,author,number_of_pages,current_page_no):
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
        self.current_page_no=current_page_no
 
    def open(self):
        self.is_open=True
        self.is_close=False
    def close(self):
        self.is_open=False
        self.is_close=True
           
    def next_page(self):
        if self.is_open==True:
            
            if self.current_page_no==self.number_of_pages:
                self.close()
            else:
                self.current_page_no+=1
        else:
            print('You cannot go to the next page, the book is closed')
    def show_status(self):
        if self.is_open==True:
            print(f'Title:{self.title}\nAuthor:{self.author}\nNumbers of pages:{self.number_of_pages}\nCurrent page:{self.current_page_no}')
        else:
            print('The book is closed')

 

        






