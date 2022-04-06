import requests
import xmltodict
import json
import time

def getWarningBMGK():
    response = requests.get(
        "https://bmkg-content-inatews.storage.googleapis.com/warninggeof.xml"
    )
    return response.text


def parseXML(xml):
    return xmltodict.parse(xml)


def main():
    xml = getWarningBMGK()
    doc = parseXML(xml)
    data = f"""
[!] {doc['alert']['info']['event']} :
    
> Magnitudo : {doc['alert']['info']['magnitude']}
> Kedalaman : {doc['alert']['info']['depth']}
> Lokasi Gempa : {doc['alert']['info']['area']}
> Arahan : {doc['alert']['info']['potential']}
> Saran BMKG : {doc['alert']['info']['instruction']}

"{doc['alert']['info']['description']}"
    """
    print(data)


if __name__ == "__main__":
    main()
