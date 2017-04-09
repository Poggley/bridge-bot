from InputData import InputData

class BridgeBot(object):
    inputData = InputData("bridgeBotInput.csv")
    print(inputData.networkInputMatrix)
    print(inputData.networkOutputMatrix)
