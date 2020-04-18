from server.city import City

def generateCityList(rawList:list):
    '''
    This method will transform a raw list of cities as a list of dictionaries
    to a list of cities.
    '''

    cityList = []

    for elem in rawList:
        #We get all the useful information of each element of the raw list
        #and transform it into a city
        city = City(elem["id"], elem["x"], elem["y"])
        cityList.append(city)

    return cityList

def generateDictArray(cityList):
    '''
    This method will transform a list of cities to a list of dictionaries
    '''
    dicList = []

    for city in cityList:
        dic = {"id": city.name, "x": city.x, "y": city.y}
        dicList.append(dic)

    return dicList
