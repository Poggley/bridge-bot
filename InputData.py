import numpy

class InputData(object):
    #------------------------------------------------------------------------
    # Opens a CSV file and parses into neural network input and output
    # matrices. 
    # 
    # The CSV file should be comma delimited with a header row. Currently
    # only supports a single column of output. 
    #
    # Attributes:s
    #    fileName: The full path to the CSV file.
    #    networkInputMatrix: The matrix of all available input data.
    #    networkOutputMatrix: The matrix of output data for this network.
    #------------------------------------------------------------------------

    def __init__(self, filename):
        #--------------------------------------------------------------------
        # Imports the CSV file as a matrix and splits this into two sub
        # matrices, one for inputs and one for outputs.
        #--------------------------------------------------------------------
        self.filename = filename
        self.fullMatrixFromCSV = self.__getFullMatrixFromCSV()
        self.networkInputMatrix = self.fullMatrixFromCSV[0:-1]
        self.networkOutputMatrix = self.fullMatrixFromCSV[-1]

    def __getFullMatrixFromCSV(self):
        #--------------------------------------------------------------------
        # Converts the CSV file into a 2D array
        #--------------------------------------------------------------------
        with open(self.filename) as csvFile:
            fullMatrixFromCSV = numpy.loadtxt(csvFile, 
                                              delimiter=",", 
                                              skiprows=1, 
                                              dtype=numpy.complex128)
            return fullMatrixFromCSV