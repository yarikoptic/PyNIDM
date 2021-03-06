import os, sys
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import rdflib as rdf
from nidm.core import Constants
from nidm.experiment import *
from prov.model import *

class AcquisitionObject(ProvEntity,Core):
    """Class for NIDM-Experimenent AcquisitionObject-Level Objects.

    Default constructor uses empty graph with namespaces added from NIDM/Scripts/Constants.py.
    Additional alternate constructors for user-supplied graphs and default namespaces (i.e. from Constants.py)
    and user-supplied graph and namespaces

    @author: David Keator <dbkeator@uci.edu>
    @copyright: University of California, Irvine 2017

    """
    #constructor
    def __init__(self, acquisition,attributes=None):
        """
        Default contructor, creates an acquisition object and links to acquisition activity object

        :param acquisition: a Aquisition activity object
        :param attributes: optional attributes to add to entity
        :return: none

        """
        #execute default parent class constructor
          #execute default parent class constructor
        super(AcquisitionObject,self).__init__(acquisition.graph, QualifiedName(Namespace("nidm",Constants.NIDM),self.getUUID()),attributes)
        acquisition.graph._add_record(self)

        #self.add_attributes({PROV_TYPE: Constants.NIDM_ACQUISITION_ENTITY})
        #carry graph object around
        self.graph = acquisition.graph
        #create link to acquisition activity
        acquisition.add_acquisition_object(self)


    def __str__(self):
        return "NIDM-Experiment AcquisitionObject Class"


