# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observation_entries = []
        
    def add_observation(self, observation: str):
        if observation != "":
            self.__observation_entries.append(observation)
        
    def latest_observation(self):
        if len(self.__observation_entries) != 0:
            return self.__observation_entries[-1]
        else:
            return "empty string."
        
    def number_of_observations(self):
        return len(self.__observation_entries)
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)


