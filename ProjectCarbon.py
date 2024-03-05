class CarbonEmissionReport():
    def __init__(self,data):
        self.data = data

    def generateReport():
        print("Function to generate carbon emission report")



class ErrorHandlers():

    def __init__(self):
        self.error = error

    def errorHandler():
        print("Function to handle errors")

class CarbonEmissionCalculator():

    def __init__(self):
        self.data = {
            'energyConsumption' : {},
            'wasteConsumption' : {},
            'TravelConsumption':{}
        }

    def getTransportData(self):
        print("Transportation Information")
        travelPerYear= float(input("How many Kilometers do your employees travel per year for business purposes?"))
        fuelUse = float(input("What is the average fuel efficiency of the vehicle used for business travel in litres per 100 Kilomters?"))
        fuelAverage = float ((1 /fuelUse) * (2.31))
        self.data['TravelConsumption']['fuelAverage'] = travelPerYear * fuelAverage 

    def getEnergyConsumption(self):
        print("Getting Energy Consumption")
        eBill = float(input("What is your average monthly electricity bill in euros?"))
        nBill = float(input("What is your average monthly natural gas bill in euros"))
        tBill = float(input("What is your average monthly fuel bill in euros?"))
        self.data['energyConsumption']['energyAvg'] = (eBill) *(12)*(0.0005) + (nBill)*(12)*(0.0053) + (tBill) * (12) * (2.32) 

    def getWasteData(self):
        print("Taking Waste data")
        wasteGenerated=float(input("How much waste do you generate per month in Kilograms?"))
        wasteRecycled= float(input("How much of that waste is recycled?"))
        percent = (wasteRecycled / wasteGenerated) * (100)
        self.data['wasteConsumption']['wasteAvg'] = wasteGenerated * 12 * (0.57 - percent)

    def getUserData(self):
        self.getEnergyConsumption()
        self.getTransportData()
        self.getWasteData()


if __name__ == "__main__":
    carbonEmissionCalculator = CarbonEmissionCalculator()
    carbonEmissionCalculator.getUserData()
    