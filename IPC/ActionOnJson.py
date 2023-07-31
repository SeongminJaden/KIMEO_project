import json

fileForScreen = "/home/pi/Desktop/Kimeo/kimeo/IPC/data.json"

class ScreenJsonSerializer:
    def __init__(self, imageName, stay, timeToStay):
        self.imageName = imageName
        self.stay = stay
        self.timeToStay = timeToStay

class ActionOnJson:
    class __ActionOnJson:
        def __init__(self, fileNameIn):
            self.fileName = fileNameIn

        def __str__(self):
            return repr(self) + self.fileName

    instance = None

    def __init__(self, fileNameIn):
        if not ActionOnJson.instance:
            ActionOnJson.instance = ActionOnJson.__ActionOnJson(fileNameIn)
        else:
            ActionOnJson.instance.fileNameIn = fileNameIn

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def updateValueJsonFile(self, variable, value):
        jsonFile = open(self.fileName, "r+")
        data = json.load(jsonFile)
        jsonFile.seek(0, 0)
        jsonFile.truncate()

        print(data)
        if (variable in data):
            data[variable] = value
            jsonFile.write(json.dumps(data))
        else:
            print("no value for ", variable)

        jsonFile.close()

        print(data)
        return data

    def updateValueJsonFileWithList(self, listIn):
        jsonFile = open(self.fileName, "r+")
        data = json.load(jsonFile)
        jsonFile.seek(0, 0)
        jsonFile.truncate()

        print(data)
        for item in listIn:
            if (item[0] in data):
                data[item[0]] = item[1]
            else:
                print("no value for ", item[0])

        jsonFile.write(json.dumps(data))
        jsonFile.close()

        print(data)
        return data

    def writeJson(self, data):
        jsonFile = open(self.fileName, "r+")
        jsonFile.seek(0, 0)
        jsonFile.truncate()
        jsonFile.write(json.dumps(data))
        jsonFile.close()

    def getValueJsonFile(self, variable):
        jsonFile = open(self.fileName, "r")
        data = json.load(jsonFile)

        if (variable in data):
            dataReturn = data[variable]
        else:
            print("no value for ", variable)

        jsonFile.close()
        # print("dataReturn = " + dataReturn)
        return dataReturn

    def showJson(self):
        jsonFile = open(self.fileName, "r+")
        data = json.load(jsonFile)
        print(data)
        jsonFile.close()

    def getJson(self):
        jsonFile = open(self.fileName, "r+")
        data = json.load(jsonFile)
        jsonFile.close()
        return data

    def getJsonString(self):
        jsonFile = open(self.fileName, "r+")
        data = json.load(jsonFile)
        jsonFile.close()
        return json.dumps(data)

if __name__ == '__main__':
    actionJson = ActionOnJson("data.json")

    screen = ScreenJsonSerializer("bla", True, 3)

    actionJson.writeJson(screen.__dict__)