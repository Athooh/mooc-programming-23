# Write your solution here
import urllib.request
import json

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            active_courses = [(course['fullName'], course['name'], course['year'], sum(course['exercises'])) 
                              for course in data if course.get('enabled', False)]
            return active_courses
    except Exception as e:
        print("Error while retrieving data:", e)
        return []

# Test the function
if __name__ == "__main__":
    courses = retrieve_all()
    for course in courses:
        print(course)
