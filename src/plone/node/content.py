from node.ext.zodb import OOBTodictStorage
from node.ext.zodb import OOBTNodeAttributes
from node.ext.zodb import ZODB_NODE_PARTS
from persistent import Persistent
from plumber import plumber
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFCore.CMFCatalogAware import CMFCatalogAware
from Products.CMFCore.DynamicType import DynamicType
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import implementer

from .behaviors import ContentishBehaviour
from .interfaces import IContentNode

CONTENT_NODE_PARTS = (
    ContentishBehaviour,
    OOBTodictStorage
)


@implementer(IAttributeAnnotatable)
class ContentBase(Persistent,
                  DefaultDublinCoreImpl,
                  DynamicType,
                  BrowserDefaultMixin,
                  CMFCatalogAware):
    """Inherits everything needed to be a good citizen in CMF space as base
    """


@implementer(IContentNode)
class ContentNode(ContentBase):
    __metaclass__ = plumber
    __plumbing__ = ZODB_NODE_PARTS + CONTENT_NODE_PARTS
    attributes_factory = OOBTNodeAttributes


# dexterity has here too:
# - PasteBehaviourMixin looks like this is not needed,
# - DAVCollectionMixin - if we want webdav support
