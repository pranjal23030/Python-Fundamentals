class Book:
    def __init__(self, author, pages, title):
        self.author = author
        self.pages = pages
        self.title = title

    def change_author(self, new_author):
        self.author = new_author

    def __str__(self):  # Overrides and prints the main thing instead of the pointer
        return f'Title: {self.title} \n Author: {self.author} \n Pages: {self.pages}'


harry_Potter = Book('JK Rowling', 255, "Harry Potter and the prisoner of azkaban")
hunger_Games = Book('Suzanne Peterson', 300, "Hunger Games 2")

hunger_Games.change_author('John Williams')
print(hunger_Games)
print()
print(harry_Potter)