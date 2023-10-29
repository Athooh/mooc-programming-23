# Write your solution here
def new_person(name: str, age: int):

    if not name or len(name.split()) < 2:
        raise ValueError("Invalid name. Name should have at least two words.")
    
    if len(name) > 40:
        raise ValueError("Invalid name. Name should not exceed 40 characters.")

    if age < 0 or age > 150:
        raise ValueError("Invalid age. Age should be a non-negative number less than 150.")

    return (name, age)

if __name__ == "__main__":
    try:
        person_data = new_person("John Doe", 30)
        print(person_data)  

        person_data = new_person("", 25)  
        person_data = new_person("John", 200)  
        person_data = new_person("Lorem Ipsum is simply dummy text of the printing and typesetting industry.", 50)  # Raises ValueError
        person_data = new_person("Jane", -5)  

    except ValueError as e:
        print(f"Error: {e}")
