//Task 1:
const books = [
  {title: "To Kill a Mockingbird", author: "Harper Lee", pages: 336},
  {title: "The Great Gatsby", author: "F. Scott Fitzgerald", pages: 180},
  {title: "1984", author: "George Orwell", pages: 328},
  {title: "The Catcher in the Rye", author: "J.D. Salinger", pages: 224},
  {title: "Brave New World", author: "Aldous Huxley", pages: 288}
]

//Task 2:
books.forEach((book) => {
  console.log(book.title)
})

//Task 3:
let number_of_pages=0
books.forEach((book) => {
  number_of_pages += book.pages
})
console.log(`The total number of pages is ${number_of_pages}.`)

//Task 4:
let most_pages = 0
let book_title = ''
books.forEach((book) => {
  if(book.pages > most_pages){
    most_pages = book.pages
    book_title = book.title
  }
})
console.log(`The book with the most pages is "${book_title}" with ${most_pages} pages.`)

//Task 5:
let shortest_title = books[0].title
books.forEach((book) => {
  if(book.title.length < shortest_title.length){
    shortest_title = book.title
  }
})
console.log(`The book with the shortest title is "${shortest_title}".`)

//Task 6:
const author_arr=[]
books.forEach((book) => {
  author_arr.push(book.author)
})
console.log(author_arr)

//Task 7:
const new_arr=[]
books.forEach((book) => {
  let author = new_arr.find(author => author.name === book.author)

  if(!author){
    author = {name: book.author, books: []}
    new_arr.push(author)
  }
  author.books.push(book.title)
})
console.log(new_arr)
