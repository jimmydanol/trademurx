import xml.etree.ElementTree as ET
import requests

# Namespaces
com = '{http://www.wipo.int/standards/XMLSchema/Common/1}'
tmk = '{http://www.wipo.int/standards/XMLSchema/Trademark/1}'

# Creates a Query class for instantiating objects that will pull data from tsdr
class Query:
    def __init__(self, serial_num = 0, owner = 'default', id = 'default'):
        self.serial_num = serial_num
        self.owner = owner
        self.id = id

    def parse_xml(self, root):
        """
        Establishes the attributes for the Query object
        root: The root of the XML file from using ET module
        """
        for node in root.iter(com + 'EntityName'):
            self.owner = node.text

        for node in root.iter(tmk + 'GoodsServicesDescriptionText'):
            self.id = node.text

def get_query(serial_num):
    """
    Queries the TSDR site and writes the returning XML file to server. Then derives
    the tree and root of the XML file using ET module. Then instantiates a Query
    object. Finally, returns a Query object to the starter application.
    serial_num: Trademark serial number
    """
    url = 'https://tsdrsec.uspto.gov/ts/cd/casestatus/' + str(serial_num) + '/v1/info.xml'
    response = requests.get(url)

    with open('feed.xml', 'w') as file:
        file.write(response.text)

    tree = ET.parse('feed.xml')
    root = tree.getroot()

    applicant = Query()
    applicant.parse_xml(root)

    return applicant
