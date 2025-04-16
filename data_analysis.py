import pandas as pd
import matplotlib.pyplot as plt

bestsellers = pd.read_csv("bestsellers_british_price.csv")
bestsellers = bestsellers.drop_duplicates(subset="Name", keep="last")


print(bestsellers)

number_of_bestsellers_written = bestsellers.groupby(
    "Author")[["Name"]].count().sort_values("Name", ascending=False).head(10).reset_index()

plt.bar(
    number_of_bestsellers_written.Author,
    number_of_bestsellers_written.Name,
    color="maroon",
    width=0.4,
)
plt.xlabel("Author")
plt.ylabel("Number of bestselling books")
plt.title("My first chart!")
plt.show()

number_books_genre = bestsellers.groupby("Genre")[["Name"]].count().sort_values("Name", ascending=False).reset_index()

print(number_books_genre)

plt.pie(
    number_books_genre.Name, labels=number_books_genre.Genre, autopct="%1.1f%%"
)
plt.show()