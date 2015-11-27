from pprint import pprint
import simplejson
import matplotlib.pyplot as plt

class State(object):
    """This class handles each state of the traces"""

    def __init__(self):
        #print 'In the State class'
        pass

    def getStates(self, file_name):
        try:
            with open(file_name) as json_file:
                JSON_data = simplejson.load(json_file)
                #pprint(data)

            return JSON_data
        except ValueError as e:
            print '[Exception]: ' + str(e)

    def plot_last_trace(self, plotable_arr):
        plt.plot(plotable_arr[len(plotable_arr) - 1])
        plt.show()