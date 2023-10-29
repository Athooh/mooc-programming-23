class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(routes: list):
    sorted_routes = sorted(routes, key=lambda route: route.length, reverse=True)
    return sorted_routes

def grade_sort_key(route):
    numeric_part = ''.join(filter(str.isdigit, route.grade))
    non_numeric_part = ''.join(filter(lambda x: not x.isdigit(), route.grade))
    numeric_value = int(numeric_part) if numeric_part else 0
    
    return (  -numeric_value, -route.length, non_numeric_part )

def sort_by_difficulty(routes: list):
    sorted_routes = sorted(routes, key=grade_sort_key, reverse=False)
    return sorted_routes

if __name__ == '__main__':
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]

    for route in sort_by_difficulty(routes):
        print(route)