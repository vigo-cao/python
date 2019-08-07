import xmltodict
import json

def pythonXmlToJson():
    with open('E:\\PythonMaster\\Day101-150\\xmldata.xml') as f:
        xmlStr = f.read()

        concertedDict = xmltodict.parse(xmlStr)
        jsonStr = json.dumps(concertedDict,indent=1)
        print(jsonStr)

if __name__ == '__main__':
    pythonXmlToJson()
