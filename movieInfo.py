#Made by Ajinesh Pratap Singh

from imdb import IMDb

# Create an instance of the IMDb class
ia = IMDb()

# Search for a movie by title
movies = ia.search_movie(input("enter movie name: "))

# Display basic information about the first result
if movies:
    movie = movies[0]
    print(f"Title: {movie['title']}")
    print(f"Year: {movie['year']}")

    # Fetch detailed info
    ia.update(movie)

    # Show the rating, genres, and plot
    print(f"Rating: {movie.get('rating')}")
    print(f"Genres: {', '.join(movie.get('genres', []))}")
    print(f"Plot: {movie.get('plot outline')}")

    # Fetch box office information
    box_office = movie.get('box office')

    if box_office:
        # Get the gross earnings worldwide
        worldwide_gross = box_office.get('Cumulative Worldwide Gross')
        if worldwide_gross:
            print(f"Worldwide Gross: {worldwide_gross}")
        else:
            print("Worldwide Gross: Not available")

        # Get the gross earnings in the USA
        usa_gross = box_office.get('Gross USA')
        if usa_gross:
            print(f"USA Gross: {usa_gross}")
        else:
            print("USA Gross: Not available")
    else:
        print("Box office information not available.")
else:
    print("No movies found.")
