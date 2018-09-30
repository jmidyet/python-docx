from .blkcntnr import BlockItemContainer
from .shared import Parented



class StructuredDocumentTag(Parented):
    """
    Proxy class for a WordprocessingML ``<w:sdt>`` element.
    """
    def __init__(self, sdt, parent):
        super(StructuredDocumentTag, self).__init__(parent)
        self._element = self._sdt = sdt
        self.__content = None

    @property
    def paragraphs(self):
        """
        A list of |Paragraph| instances corresponding to the paragraphs in
        the document, in document order. Note that paragraphs within revision
        marks such as ``<w:ins>`` or ``<w:del>`` do not appear in this list.
        """
        return self._content.paragraphs

    @property
    def _content(self):
        """
        The |StructuredDocumentTagContent| instance containing the content for this sdt.
        """
        if self.__content is None:
            self.__content = StructuredDocumentTagContent(self._element.tag_content, self)
        return self.__content


class StructuredDocumentTagContent(BlockItemContainer):
    """
    Proxy for ``<w:sdtContent>`` element for this StructuredDocumentTag, having primarily a
    container role.
    """
    def __init__(self, content, parent):
        super(StructuredDocumentTagContent, self).__init__(content, parent)
        self._content = content