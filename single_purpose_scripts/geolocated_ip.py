'''
Find an IP's geolocation by making a get request to http://ip-api.com/ .
To get my own IP data simply request http://ip-api.com/data_format,
where data_format is either 'json' or 'xml'
to get info about another IP request http://ip-api.com/data_format/desired_ip .
'''

from requests import get
from bs4 import BeautifulSoup

def find_ip(ip, format_type):
    if format_type == 'json':
        # My own
        # endpoint = "http://ip-api.com/json"
        endpoint = "http://ip-api.com/json/" + ip
        json_response = get(endpoint).json()
        return json_response['city']

    elif format_type == 'xml':
        # My own
        # endpoint = "http://ip-api.com/xml"
        endpoint = "http://ip-api.com/xml/" + ip
        xml_response = get(endpoint).text
        xml_format = BeautifulSoup(xml_response, 'xml')
        return xml_format.find('query').find('city').text


print(find_ip("188.37.114.197", 'json'))
print()
print(find_ip("188.37.114.197", 'xml'))

# Successful request response
# JSON
'''
{
    "status": "success",
    "country": "COUNTRY",
    "countryCode": "COUNTRY CODE",
    "region": "REGION CODE",
    "regionName": "REGION NAME",
    "city": "CITY",
    "zip": "ZIP CODE",
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "timezone": "TIME ZONE",
    "isp": "ISP NAME",
    "org": "ORGANIZATION NAME",
    "as": "AS NUMBER / NAME",
    "query": "IP ADDRESS USED FOR QUERY"
}
'''
# XML
'''
<?xml version="1.0" encoding="UTF-8"?>
<query>
    <status>success</status>
    <country><![CDATA[COUNTRY]]></country>
    <countryCode><![CDATA[COUNTRY CODE]]></countryCode>
    <region><![CDATA[REGION CODE]]></region>
    <regionName><![CDATA[REGION NAME]]></regionName>
    <city><![CDATA[CITY]]></city>
    <zip><![CDATA[ZIP CODE]]></zip>
    <lat><![CDATA[LATITUDE]]></lat>
    <lon><![CDATA[LONGITUDE]]></lon>
    <timezone><![CDATA[TIME ZONE]]></timezone>
    <isp><![CDATA[ISP NAME]]></isp>
    <org><![CDATA[ORGANIZATION NAME]]></org>
    <as><![CDATA[AS NUMBER / NAME]]></as>
    <query><![CDATA[IP ADDRESS USED FOR QUERY]]></query>
</query>
'''

# Failed request response
# JSON
'''
{
    "status": "fail",
    "message": "ERROR MESSAGE",
    "query": "IP ADDRESS USED FOR QUERY"
}
'''
# XML
'''
<?xml version="1.0" encoding="UTF-8"?>
<query>
    <status>fail</status>
    <message>ERROR MESSAGE</message>
    <query><![CDATA[IP ADDRESS USED FOR QUERY]]></query>
</query>
'''