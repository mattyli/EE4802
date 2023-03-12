import requests

def geoCode(addy):
    req = requests.get('https://developers.onemap.sg/commonapi/search?searchVal='+addy+'&returnGeom=Y&getAddrDetails=Y&pageNum=1')
    resultsdict = eval(req.text)
    if len(resultsdict['results'])>0:
        return resultsdict['results'][0]['LATITUDE'], resultsdict['results'][0]['LONGITUDE']
    else:
        pass

def genAllCoords(addList: list)->list:
    uniqueCoords = []
    total = 0
    good = 0
    for add in addList:
        try:
            if len(geoCode(add)) > 0: # checking if we were able to sucessfuly query the API
                uniqueCoords.append(geoCode(add))
                good += 1
        except:
            uniqueCoords.append(add + 'unavailable')
        total+=1

    print('Geocoded ' + str((good/total)*100) + 'percent of all addresses.\n')
    return uniqueCoords