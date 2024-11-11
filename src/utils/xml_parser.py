import xml.etree.ElementTree as ET

from src.models.xml_tags import xml_tags

_XMLNS = {'ns1': 'http://jpk.mf.gov.pl/wzor/2022/02/17/02171/',
          'ns2': 'http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2018/08/24/eD/DefinicjeTypy/'}


def createRecord(record_tags, node):
    """
    Create a record from the given tags and node
    :param record_tags:
    :param node:
    :return:
    """
    return_value = {}

    for tag in record_tags:
        value = get_value(node, tag.get("tag"))
        if value:
            return_value[tag.get("name")] = value.strip()

    return return_value


def get_value(element, path, namespace=_XMLNS):
    """
    Get the value of the element at the given path
    :param element:
    :param path:
    :param namespace:
    :return:
    """
    target = element.find(path, namespace)
    return target.text if target is not None else None


def parse_xml_to_dict(xml_file):
    """
    Parse the given XML file
    :param xml_file:
    :return:
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = {
        "Naglowek": [],
        "Podmiot1": [],
        "Faktura": [],
        "FakturaCtrl": [],
        "FakturaWiersz": [],
        "FakturaWierszCtrl": []
    }

    # for key, record_tags in tags.items():
    #     node = root.find(key, _XMLNS)
    #     if node is not None:
    #         key_parts = key.split(":")
    #         data_key = key_parts[1] if len(key_parts) > 1 else key
    #         data[data_key].append(createRecord(record_tags, node))

    for key, record_tags in xml_tags.items():
        node = root.findall(key, _XMLNS)
        # if node is not None:
        #     key_parts = key.split(":")
        #     data_key = key_parts[1] if len(key_parts) > 1 else key
        #     data[data_key].append(createRecord(record_tags, node))
        for n in node:
            key_parts = key.split(":")
            data_key = key_parts[1] if len(key_parts) > 1 else key
            data[data_key].append(createRecord(record_tags, n))

    return data
