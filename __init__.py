# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TransparentClass
                                 A QGIS plugin
 Create trasparency of selection
                             -------------------
        begin                : 2015-12-07
        copyright            : (C) 2015 by Dkrav
        email                : dkrav2006@yandex.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TransparentClass class from file TransparentClass.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .trasparenter import TransparentClass
    return TransparentClass(iface)
