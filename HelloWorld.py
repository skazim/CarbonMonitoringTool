class CarbonEmissionCalculator:
    def __init__(self):
        self.data={}
    def inputData(self):
            print("This is working")

    def calculateEnergyUsage(self):
         eBill = int(input("What is your average monthly electricity bill in euros?"))
         nBill = int(input("What is your average monthly natural gas bill in euros"))
         tBill = int(input("What is your average monthly fuel bill in euros?"))
         calEnergy = (eBill) *(12)*(0.0005) + (nBill)*(12)*(0.0053) + (tBill) * (12) * (2.32) 
         return calEnergy
    

    def calculateWasteUsage(self):
         wasteGenerated=int(input("How much waste do you generate per month in Kilograms?"))
         wasteRecycled= int(input("How much of that waste is recycled?"))
         percent = (wasteRecycled / wasteGenerated) * (100)
         return wasteGenerated * 12 * (0.57 - percent)
    
    def calculateBusinessTravel(self):
         travelPerYear= int(input("How many Kilometers do your employees travel per year for business purposes?"))
         fuelUse = int(input("What is the average fuel efficiency of the vehicle used for business travel in litres per 100 Kilomters?"))
         fuelAverage = (1 /fuelUse) * (2.31)
         return travelPerYear * fuelAverage
    
if __name__ == "__main__":
    carbonEmissionCalculator = CarbonEmissionCalculator()
    carbonEmissionCalculator.inputData()

    energyUsage = carbonEmissionCalculator.calculateEnergyUsage()
    wasteUsage = carbonEmissionCalculator.calculateWasteUsage()
    businessUsage = carbonEmissionCalculator.calculateBusinessTravel()

    print("Your Energy Usage is",energyUsage)
    print("Your waste usage is", wasteUsage)
    print("Your Business Usage is", businessUsage)
