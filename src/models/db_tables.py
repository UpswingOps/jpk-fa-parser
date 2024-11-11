"""
DB tables for the database.
"""
from src.models.faktura_ctrl_tags import FakturaCtrlTags
from src.models.faktura_tags import FakturaTags
from src.models.faktura_wiersz_ctrl_tags import FakturaWierszCtrlTags
from src.models.faktura_wiersz_tags import FakturaWierszTags
from src.models.naglowek_tags import NaglowekTags
from src.models.podmiot1_tags import Podmiot1Tags

db_tables = {
    "Naglowek": NaglowekTags,
    "Podmiot1": Podmiot1Tags,
    "Faktura": FakturaTags,
    "FakturaCtrl": FakturaCtrlTags,
    "FakturaWiersz": FakturaWierszTags,
    "FakturaWierszCtrl": FakturaWierszCtrlTags
}
