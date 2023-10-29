# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    sorted_items_list = sorted(items, key=lambda x: x["rating"], reverse=True)
    return sorted_items_list

if __name__ == "__main__":
    shows = [
        {"name": "Dexter", "rating": 8.6, "seasons": 9},
        {"name": "Friends", "rating": 8.9, "seasons": 10},
        {"name": "Simpsons", "rating": 8.7, "seasons": 32},
    ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")
