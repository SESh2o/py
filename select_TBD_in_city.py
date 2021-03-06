# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# select_TBD_in_city.py
# Created on: 2014-07-01 16:05:42.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
SLAMM_landuse_single = "SLAMM_landuse_single"
SLAMM_landuse_single__2_ = "SLAMM_landuse_single"

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(SLAMM_landuse_single, "NEW_SELECTION", "\"IN_CITY\" = 'TBD'")

# Process: Select Layer By Location
#arcpy.SelectLayerByLocation_management(SLAMM_landuse_single__2_, "HAVE_THEIR_CENTER_IN", "", "", "REMOVE_FROM_SELECTION")
Layers.zoomToSelectedFeatures()



