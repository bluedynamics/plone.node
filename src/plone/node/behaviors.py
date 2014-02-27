from AccessControl import ClassSecurityInfo
from AccessControl.Permissions import access_contents_information
from plumber import Behavior
from plumber import default
from Products.CMFCore.interfaces import IContentish
from zope.component import queryAdapter
from zope.index.interfaces import ISearchableText
from zope.interface import implementer


@implementer(IContentish)
class ContentishBehaviour(Behavior):

    security = ClassSecurityInfo()

    @default
    @security.protected(access_contents_information)
    def SearchableText(self):
        searchable = queryAdapter(self, ISearchableText)
        if searchable:
            return searchable.getSearchableText()
        return ''


# TODO (eventually)
# OFS.interfaces.IOrderedContainerIOrderedContainer,
# plone.folder.interfaces.IOrderableFolder
