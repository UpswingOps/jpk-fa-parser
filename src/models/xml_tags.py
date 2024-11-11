from src.models.faktura_ctrl_tags import FakturaCtrlTags
from src.models.faktura_tags import FakturaTags
from src.models.faktura_wiersz_ctrl_tags import FakturaWierszCtrlTags
from src.models.faktura_wiersz_tags import FakturaWierszTags
from src.models.naglowek_tags import NaglowekTags
from src.models.podmiot1_tags import Podmiot1Tags

xml_tags = {
    "ns1:Naglowek": NaglowekTags,
    "ns1:Podmiot1": Podmiot1Tags,
    "ns1:Faktura": FakturaTags,
    "ns1:FakturaCtrl": FakturaCtrlTags,
    "ns1:FakturaWiersz": FakturaWierszTags,
    "ns1:FakturaWierszCtrl": FakturaWierszCtrlTags
}
