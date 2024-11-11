"""
Test XML parser functions
"""
import unittest
import xml.etree.ElementTree as ET
from io import StringIO
from src.utils.xml_parser import parse_xml_to_dict, create_record, get_value


class TestXMLParser(unittest.TestCase):
    """
    Test XML parser functions
    """

    def setUp(self):
        self.xml_content = """<?xml version="1.0" encoding="utf-8"?>
            <JPK xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                 xmlns="http://jpk.mf.gov.pl/wzor/2022/02/17/02171/">
                <Naglowek>
                    <KodFormularza kodSystemowy="JPK_FA (4)" wersjaSchemy="1-0">JPK_FA</KodFormularza>
                    <WariantFormularza>4</WariantFormularza>
                </Naglowek>
                <Podmiot1>
                    <IdentyfikatorPodmiotu>
                        <NIP>VATEU Adres Firmy 1</NIP>
                        <PelnaNazwa>Nazwa Firmy 1</PelnaNazwa>
                    </IdentyfikatorPodmiotu>
                    <AdresPodmiotu>
                        <KodKraju xmlns="http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2018/08/24/eD/DefinicjeTypy/">PL</KodKraju>
                        <Wojewodztwo xmlns="http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2018/08/24/eD/DefinicjeTypy/">
                            kujawsko-pomorskie
                        </Wojewodztwo>
                    </AdresPodmiotu>
                </Podmiot1>
                <Faktura>
                    <KodWaluty>EUR</KodWaluty>
                    <P_1>2019-01-01</P_1>
                </Faktura>
                <Faktura>
                    <KodWaluty>EUR</KodWaluty>
                    <P_1>2019-02-01</P_1>
                </Faktura>
                <FakturaCtrl>
                    <LiczbaFaktur>2</LiczbaFaktur>
                    <WartoscFaktur>10.00</WartoscFaktur>
                </FakturaCtrl>
                <FakturaWiersz>
                    <P_2B>FS 1/01/2019</P_2B>
                    <P_7>Pozycja faktury</P_7>
                </FakturaWiersz>
                <FakturaWiersz>
                    <P_2B>FS 2/02/2019</P_2B>
                    <P_7>Pozycja faktury</P_7>
                </FakturaWiersz>
                <FakturaWierszCtrl>
                    <LiczbaWierszyFaktur>2</LiczbaWierszyFaktur>
                    <WartoscWierszyFaktur>10</WartoscWierszyFaktur>
                </FakturaWierszCtrl>
            </JPK>
            """
        self.xml_file = StringIO(self.xml_content)
        self.record_tags = [{"tag": "ns1:KodFormularza", "name": "KodFormularza"}]

    def test_parse_xml_to_dict(self):
        """
        Test parse_xml_to_dict function
        :return:
        """
        expected_data = {
            "Naglowek": [{'KodFormularza': 'JPK_FA', 'WariantFormularza': '4'}],
            "Podmiot1": [{'NIP': 'VATEU Adres Firmy 1', 'PelnaNazwa': 'Nazwa Firmy 1',
                          'KodKraju': 'PL', 'Wojewodztwo': 'kujawsko-pomorskie'}],
            "Faktura": [{'KodWaluty': 'EUR', 'P_1': '2019-01-01'},
                        {'KodWaluty': 'EUR', 'P_1': '2019-02-01'}],
            'FakturaCtrl': [{'LiczbaFaktur': '2', 'WartoscFaktur': '10.00'}],
            "FakturaWiersz": [{'P_2B': 'FS 1/01/2019', 'P_7': 'Pozycja faktury'},
                              {'P_2B': 'FS 2/02/2019', 'P_7': 'Pozycja faktury'}],
            "FakturaWierszCtrl": [{'LiczbaWierszyFaktur': '2', 'WartoscWierszyFaktur': '10'}]
        }
        result = parse_xml_to_dict(self.xml_file)
        self.assertEqual(result, expected_data)

    def test_create_record(self):
        """
        Test create_record function
        :return:
        """
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        node = root.find("ns1:Naglowek", {'ns1': 'http://jpk.mf.gov.pl/wzor/2022/02/17/02171/'})
        result = create_record(self.record_tags, node)
        expected_record = {"KodFormularza": "JPK_FA"}
        self.assertEqual(result, expected_record)

    def test_get_value(self):
        """
        Test get_value function
        :return:
        """
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        node = root.find("ns1:Naglowek", {'ns1': 'http://jpk.mf.gov.pl/wzor/2022/02/17/02171/'})
        result = get_value(node, "ns1:KodFormularza")
        self.assertEqual(result, "JPK_FA")


if __name__ == '__main__':
    unittest.main()

# Run the test:
# python -m tests.xml_parser_test
