import pandas as pd

def get_book_id(df, book_title):
    isbn = df.loc[df['Book-Title'] == book_title, 'ISBN'].values
    return isbn[0] if len(isbn) > 0 else None

def get_book_title(df, book_id):
    title = df.loc[df['ISBN'] == book_id, 'Book-Title'].values
    return title[0] if len(title) > 0 else None

def get_image_url(df, book_id):
    image = df.loc[df['ISBN'] == book_id, 'Image-URL-M'].values
    return image[0] if len(image) > 0 else None