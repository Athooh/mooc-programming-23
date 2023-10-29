# # Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    
    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.ratings:
            total_ratings = len(self.ratings)
            avg_rating = round(sum(self.ratings) / total_ratings, 1)
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{total_ratings} ratings, average {avg_rating} points"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"
        
    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Rating should be between 0 and 5.")
def minimum_grade(rating: float, series_list: list):
        return [series for series in series_list if series.ratings and sum(series.ratings) / len(series.ratings) >= rating]

def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres]

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum rating of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

