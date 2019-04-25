import xml.etree.ElementTree as ET
import requests

com = '{http://www.wipo.int/standards/XMLSchema/Common/1}'
tmk = '{http://www.wipo.int/standards/XMLSchema/Trademark/1}'

class Query:
    def __init__(self, serial_num = 0, owner = 'default', id = 'default'):
        self.serial_num = serial_num
        self.owner = owner
        self.id = id

    def parse_xml(self, root):
        for node in root.iter(com + 'EntityName'):
            # print(node.text)
            self.owner = node.text

        for node in root.iter(tmk + 'GoodsServicesDescriptionText'):
            # print(node.text)
            self.id = node.text

def get_query(serial_num):
    url = 'https://tsdrsec.uspto.gov/ts/cd/casestatus/' + str(serial_num) + '/v1/info.xml'
    response = requests.get(url)

    with open('feed.xml', 'w') as file:
        file.write(response.text)

    # xml_filename = "feed.xml"

    tree = ET.parse('feed.xml')

    root = tree.getroot()
    applicant = Query()
    applicant.parse_xml(root)

    return applicant.owner, applicant.id
