from city import City

def generateCityList(rawList:list):

    cityList = []

    for elem in rawList:
        city = City(elem["id"], elem["x"], elem["y"])
        cityList.append(city)

    return cityList
