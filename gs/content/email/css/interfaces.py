# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from zope.viewlet.interfaces import IViewletManager


class IHTMLEmailStyle(IViewletManager):
    '''A viewlet manager for the CSS in an HTML-formatted email notification'''


class IHTMLOpenEmailStyle(IViewletManager):
    '''A viewlet manager for the CSS in an HTML-formatted email notification.
    Used when the CSS is not turned into style-attributes (may be ignored by
    developers and clients).'''
