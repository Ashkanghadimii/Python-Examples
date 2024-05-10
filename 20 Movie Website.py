import csv

def add_cast(order):
    L_admin = []
    L_admin.append(order)
    L_admin = order.split()
    if L_admin[0] != "ADD-CAST":
        print("Invalid order")
    else:
        f = order.split()
        name = f[1]
        try:
            if len(name) > 20:
                raise ValueError("Name cannot be more than 20 characters!!!")
            with open("Casts.csv", "a") as file:
                with open("Casts.csv", "r") as readfile:
                    cast_id = sum(1 for line in readfile)
                file.write("Name:" + name + "\n")
                print(f"Added successfully / Cast ID: {cast_id}")
        except ValueError as e:
            print("Error:", e)

def show_movie(movie_id):
    try:
        movie_id = int(movie_id)
        if movie_id < 0:
            raise ValueError("Movie ID must be a non-negative integer")

        # Read Films.csv to get movie information
        with open('Films.csv', 'r') as file:
            reader = csv.reader(file)
            movie_data = list(reader)

        if movie_id >= len(movie_data):
            print("Movie ID not found")
            return

        movie_title = movie_data[movie_id][0]  # Assuming title is in the first column

        # Read Links.csv to get linked cast information
        linked_cast = []
        with open('Links.csv', 'r') as file:
            for line in file:
                if f"Movie ID: {movie_id}" in line:
                    parts = line.split(',')
                    cast_id = parts[0].split()[2]
                    linked_cast.append(cast_id)

        # Print movie details and linked cast IDs
        print(f"Movie ID: {movie_id}, Title: {movie_title}")
        print("Linked Cast IDs:")
        for cast_id in linked_cast:
            print(cast_id.strip())

    except ValueError as e:
        print("Error:", e)

def show_cast(cast_id):
    try:
        cast_id = int(cast_id)
        if cast_id < 0:
            raise ValueError("Cast ID must be a non-negative integer")

        # Read Casts.csv to get cast information
        with open('Casts.csv', 'r') as file:
            reader = csv.reader(file)
            cast_data = list(reader)

        if cast_id >= len(cast_data):
            print("Cast ID not found")
            return

        cast_name = cast_data[cast_id][0]  # Assuming name is in the first column

        # Read Links.csv to get linked movie information
        linked_movies = []
        with open('Links.csv', 'r') as file:
            for line in file:
                if f"Cast ID: {cast_id}" in line:
                    parts = line.split(',')
                    movie_id = parts[2].split()[2]
                    movie_title = parts[3].split()[2]
                    linked_movies.append((movie_id, movie_title))

        # Print cast details and linked movies
        print(f"Cast ID: {cast_id}, {cast_name}")
        print("Linked Movies:")
        for movie_id, movie_title in linked_movies:
            print(f"Movie ID: {movie_id},{movie_title}")

    except ValueError as e:
        print("Error:", e)

def add_movie(order):
    L_admin = []
    L_admin.append(order)
    L_admin = order.split()
    if L_admin[0] != "ADD-MOVIE":
        print("Invalid order")
    else:
        f = order.split(" ")
        title = f[1]
        date = f[2]
        quality = f[3]
        try:
            x = int(date)
            if len(title) > 20:
                raise ValueError("Title cannot be more than 20 characters!!!")
            if 1888 > x or x > 2024:
                raise ValueError("Date must be from 1888 to 2024!!!")
            if quality not in ["4K", "1080", "720"]:
                raise ValueError("Quality must be 720, 1080 or 4K !!!")
            with open("Films.csv", "a") as file:
                with open("Films.csv", "r") as readfile:
                    movie_id = sum(1 for line in readfile)
                file.write("Title:" + title + " Date:" + f[2] + " Quality:" + f[3] + "\n")
                print(f"Added successfully / Movie ID: {movie_id}")
        except ValueError as e:
            print("Error:", e)

def remove_cast(cast_id):
    try:
        cast_id = int(cast_id)
        if cast_id < 0:
            raise ValueError("Cast ID must be a positive integer")
        with open("Casts.csv", "r") as file:
            reader = csv.reader(file)
            data = list(reader)

        if cast_id > len(data):
            print("Cast ID not found")
            return

        del data[cast_id]
        with open("Casts.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Cast with ID {cast_id} removed successfully")
    except ValueError as e:
        print("Error:", e)

def remove_movie(movie_id):
    try:
        movie_id = int(movie_id)
        if movie_id < 0:
            raise ValueError("Movie ID must be a positive integer")

        with open('Films.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        if movie_id > len(data):
            print("Movie ID not found")
            return

        del data[movie_id]  # Adjust for 0-based indexing

        with open('Films.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print(f"Movie with ID {movie_id} removed successfully")
    except ValueError as e:
        print("Error:", e)


def link_cast_to_movie(cast_id, movie_id):
    try:
        cast_id = int(cast_id)
        movie_id = int(movie_id)
        if cast_id < 0 or movie_id < 0:
            raise ValueError("Both Cast ID and Movie ID must be non-negative integers")

        # Read Links.csv to check if the cast is already linked to the movie
        with open('Links.csv', 'r') as file:
            for line in file:
                if f"Cast ID: {cast_id}" in line and f"Movie ID: {movie_id}" in line:
                    print("Cast is already linked to this movie")
                    return

        # Read Casts.csv to get cast information
        with open('Casts.csv', 'r') as file:
            reader = csv.reader(file)
            cast_data = list(reader)

        if cast_id >= len(cast_data):
            print("Cast ID not found")
            return

        cast_name = cast_data[cast_id][0]  # Assuming name is in the first column

        # Read Films.csv to get movie information
        with open('Films.csv', 'r') as file:
            reader = csv.reader(file)
            movie_data = list(reader)

        if movie_id >= len(movie_data):
            print("Movie ID not found")
            return

        movie_title = movie_data[movie_id][0]  # Assuming title is in the first column

        # Link the cast to the movie
        with open('Links.csv', 'a') as file:
            file.write(
                f"Cast ID: {cast_id}, Cast Name: {cast_name}, Movie ID: {movie_id}, Movie Title: {movie_title}\n")

        print(f"Linked successfully: {cast_name} to {movie_title}")

    except ValueError as e:
        print("Error:", e)


def filter_movies_by_quality(quality):
    try:
        quality = quality.upper()
        if quality not in ["720", "1080", "4K"]:
            raise ValueError("Invalid quality. Quality must be 720, 1080, or 4K")

        # Read Films.csv to get movie information
        with open('Films.csv', 'r') as file:
            reader = csv.reader(file)
            movie_data = list(reader)

        filtered_movies = []

        # Filter movies by quality
        for movie in movie_data:
            try:
                title, date, quality_str = [field.split(":")[1].strip() for field in movie]
                if quality_str.upper() == quality:
                    filtered_movies.append((title, date, quality_str))
            except IndexError:
                print("Warning: Movie entry has insufficient data")
            except Exception as e:
                print(f"Error processing movie entry: {e}")

        if not filtered_movies:
            print(f"No movies found with {quality} quality.")
        else:
            # Print filtered movies
            print(f"Movies with {quality} quality:")
            for title, date, quality_str in filtered_movies:
                print(f"Title: {title}, Date: {date}, Quality: {quality_str}")

    except ValueError as e:
        print("Error:", e)

def filter_movies_by_date(start_year):
    try:
        start_year = int(start_year)
        if start_year < 1888 or start_year > 2024:
            raise ValueError("Invalid start year. Year must be between 1888 and 2024")

        # Read Films.csv to get movie information
        with open('Films.csv', 'r') as file:
            reader = csv.reader(file)
            movie_data = list(reader)

        filtered_movies = []

        # Filter movies by date
        for movie in movie_data:
            try:
                title, date_str, quality = [field.split(":")[1].strip() for field in movie]
                movie_year = int(date_str)
                if start_year <= movie_year <= 2024:  # Limiting to 2024
                    filtered_movies.append((title, date_str, quality))
            except IndexError:
                print("Warning: Movie entry has insufficient data")
            except Exception as e:
                print(f"Error processing movie entry: {e}")

        if not filtered_movies:
            print(f"No movies found released from {start_year} until 2024.")
        else:
            # Print filtered movies
            print(f"Movies released from {start_year} until 2024:")
            for title, date, quality in filtered_movies:
                print(f"Title: {title}, Date: {date}, Quality: {quality}")

    except ValueError as e:
        print("Error:", e)


while True:
    order = input()
    if order.startswith("ADD-MOVIE"):
        add_movie(order)
    elif order.startswith("REM-MOVIE"):
        movie_id = order.split()[1]
        remove_movie(movie_id)
    elif order.startswith("ADD-CAST"):
        add_cast(order)
    elif order.startswith("SHOW-CAST"):
        command, cast_id = order.split()
        show_cast(cast_id)
    elif order.startswith("REM-CAST"):
        cast_id = order.split()[1]
        remove_cast(cast_id)
    elif order.startswith("SHOW-MOVIE"):
        movie_id = order.split()[1]
        show_movie(movie_id)
    elif order.startswith("LINK-CAST-TO-MOVIE"):
        command, cast_id, movie_id = order.split()
        link_cast_to_movie(cast_id, movie_id)
    elif order.startswith("FILTER-MOVIES-BY-QUALITY"):
        command, quality = order.split()
        filter_movies_by_quality(quality)
    elif order.startswith("FILTER-MOVIES-BY-DATE"):
        start_year = order.split()[1]
        filter_movies_by_date(start_year)
    else:
        print("Invalid order")