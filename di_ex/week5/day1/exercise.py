# We'll simulate a dataset of a small bookstore's sales records. Our dataset will include columns for Book Title, Author, Genre, Price, and Copies Sold.

# Here's how you can create this dataset using Pandas:


import pandas as pd

data = {
    "Book Title": [
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Catcher in the Rye",
    ],
    "Author": [
        "F. Scott Fitzgerald",
        "Harper Lee",
        "George Orwell",
        "Jane Austen",
        "J.D. Salinger",
    ],
    "Genre": ["Classic", "Classic", "Dystopian", "Classic", "Classic"],
    "Price": [10.99, 8.99, 7.99, 11.99, 9.99],
    "Copies Sold": [500, 600, 800, 300, 450],
}

df = pd.DataFrame(data)

# print(df.head())
# print(df.describe())
# print(df.info())
# print(df.sort_values(by="Price"))
# print(df[df["Price"] > 9])
# print(df.groupby(by="Author").sum("Copies Sold"))
# print(df.sum("Copies Sold"))
# Explore the Dataset:

# Use head() to view the first few rows of the DataFrame.
# Use describe() to get a statistical summary of the numerical columns.
# Use info() to get a concise summary of the DataFrame, including the number of non-null entries in each column.
# Sort the DataFrame based on the Price or Copies Sold.
# Filter the books by a specific Genre or books with Price above a certain threshold.
# Group the books by Author and sum up the Copies Sold.
