import streamlit as st
import pandas as pd
from surprise import dump
from utils import get_book_id, get_book_title, get_image_url

def main():
    algo, _ = dump.load('collab_filtering_model.pkl')
    df = pd.read_csv('book_rating.csv')

    st.title('Book Recommendation App')

    book_title = st.selectbox(label='Book Title', options=df['Book-Title'].unique(), index=None, placeholder='Choose a book.')

    book_id = get_book_id(df, book_title)

    if st.button('Get Recommendations'):
        item_inner_id = algo.trainset.to_inner_iid(book_id)
        neighbors = algo.get_neighbors(item_inner_id, k=5)

        suggested_book_ids = [algo.trainset.to_raw_iid(inner_id) for inner_id in neighbors]

        st.write(f'Recommended Books for {book_title}:')
        for suggested_book_id in suggested_book_ids:
            st.write(f'- {get_book_title(df, suggested_book_id)}')
            st.markdown(f'![]({get_image_url(df, suggested_book_id)})')

if __name__ == '__main__':
    main()