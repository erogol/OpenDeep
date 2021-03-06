'''
.. module:: musedata

Object for the MuseData midi dataset
'''
__authors__ = "Markus Beissinger"
__copyright__ = "Copyright 2015, Vitruvian Science"
__credits__ = ["Markus Beissinger"]
__license__ = "Apache"
__maintainer__ = "OpenDeep"
__email__ = "opendeep-dev@googlegroups.com"

# standard libraries
import logging
import os
import glob
# third party imports
import theano
# internal imports
from opendeep import make_shared_variables
import opendeep.data.dataset as datasets
from opendeep.data.dataset import FileDataset
from opendeep.utils.midi import midiread

log = logging.getLogger(__name__)

class MuseData(FileDataset):
    '''
    Object for the MuseData midi dataset. Pickled file of midi piano roll provided by Montreal's
    Nicolas Boulanger-Lewandowski into train, valid, and test sets.
    '''
    def __init__(self, dataset_dir='../../datasets'):
        log.debug("Loading MuseData midi dataset...")

        filename = 'MuseData.zip'
        source = 'http://www-etud.iro.umontreal.ca/~boulanni/MuseData.zip'

        super(MuseData, self).__init__(filename=filename, source=source, dataset_dir=dataset_dir)
