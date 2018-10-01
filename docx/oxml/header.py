from .xmlchemy import (
    BaseOxmlElement, OneAndOnlyOne, RequiredAttribute, ZeroOrMore, ZeroOrOne
)

class CT_HeaderFooter(BaseOxmlElement):
    tbl = ZeroOrMore('w:tbl', successors=('w:sectPr',))
    p = ZeroOrMore('w:p', successors=('w:sectPr',))
