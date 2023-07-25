import json


class BookmarksDAO:

    def __init__(self, path_book):
        self.path = path_book

    def load_bookmarks(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def upload_bookmarks(self, book):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(book, file, ensure_ascii=False)

    def bookmarks_add(self, post):
        book = self.load_bookmarks()
        if post not in book:
            book.append(post)
        self.upload_bookmarks(book)

    def bookmarks_remove(self, post):
        book = self.load_bookmarks()
        book.remove(post)
        self.upload_bookmarks(book)


