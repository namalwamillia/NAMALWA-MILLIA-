class book:
  def __init__( textbk,title, Author , pages):
        textbk.title= title
        textbk.Author = Author
        textbk.pages =pages
#create a book class with properties ie title,Author,and pages.
class book:
  def __init__( textbk,title, Author , pages):
        textbk.title= title
        textbk.Author = Author
        textbk.pages =pages
    
tb = book("English Grammer ","Dr. Alinda Aaron",250)
print(tb.title)
print(tb.Author)
print(tb.pages)

# creating an object
tb=book("English Grammer","Dr.Alinda Aaron",250) 
print(f'The title of the book is {tb.title} ,Authored by {tb.Author} and it has  {tb.pages}pages')

#qn2iii)
def book_title_and_Author(title,Author):
   print(f"The book title is {title} Authored by Dr.{Author}.")
book_title_and_Author("English Grammer", "Alinda Aaron") 


#QN2iv)
#Class is a template for an object .
#  An Object is simply an instance of a class