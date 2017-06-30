'''http://docs.qgis.org/2.6/de/docs/user_manual/processing/scripts.html'''
'''http://www.qgistutorials.com/de/docs/processing_python_scripts.html'''
'''Top Hilfe: https://gis.stackexchange.com/questions/193455/qgis-python-script-loop-for-raster-calculator'''

##CalcCWSI=name
##temp=raster
##Tair=number 26.8
##Tcmin=number 21.37
##OUT=folder
##nomodeler

from qgis.core import *
from qgis.utils import iface
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# Define Output file name
output_path = OUT + "/"
suffix = "_CWSI1.tif"

# Get layer object
bohLayer = processing.getObject(temp)

entries = []
# Define band1
boh1 = QgsRasterCalculatorEntry()
boh1.ref = 'boh@1'
boh1.raster = bohLayer
boh1.bandNumber = 1
entries.append( boh1 )

# Calculate CWSI1
#Tair = 20
Twet = Tcmin
Tdry = Tair + 5
Trange = Tdry - Twet
#formula = 'boh@1' + '+' + str(Tair)
'''CWSI = (Tc-Twet)/(Tdry-Twet) # using assumptions form.xyz.'''
formula = '(boh@1' + '-' + str(Twet) + ')/' + str(Trange)

calc = QgsRasterCalculator( formula, output_path + bohLayer.name() + suffix, 'GTiff', bohLayer.extent(), bohLayer.width(), bohLayer.height(), entries )
calc.processCalculation()
