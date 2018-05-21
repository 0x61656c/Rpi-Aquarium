import time 

class aquarium(object):
	def __init__(self, numberOfFish = 0, numberOfSnails = 0, numberOfAxlotls = 0, feederLevel = 0):
		self.numberOfFish = numberOfFish
		self.numberOfSnails = numberOfSnails
		self.numberOfAxlotls = numberOfAxlotls
		self.feederLevel = feederLevel

	def __repr__(self):
		return "<Feeder Object: Level = %i, numberOfFish = %i>" %(self.feederLevel, self.numberOfFish)

	def addFeed(self, quantity):
		self.feederLevel += quantity
		print("Feeder level increased by %i"%quantity)

	def changeCreature(self, creature, quantity):
		validAttributes = ["fish","axlotl","snail"]

		if creature not in validAttributes:
			print('Invalid "Creature" Attribute: Valid Creature Attributes include: [snail, axlotl, fish]')

		else:
			if str(creature) == validAttributes[0]:
				self.numberOfFish += quantity
			
			elif str(creature) == validAttributes[1]:
				self.numberOfAxlotls += quantity
			
			elif str(creature) == validAttributes[2]:
				self.numberOfSnails += quantity

			print("Number of %ss changed by %i") %(creature,quantity)
				
	def feed(self):
		feedRequired = int(self.numberOfSnails * .5) + self.numberOfFish + (self.numberOfAxlotls * 2)

		if self.feedeerLevel >= feedRequired:
			self.feederLevel -= feedRequired
			pass #insert custom hardware function here

		else: 
			print("Error: Insufficient Feeder Level")
			pass #insert custom hardware function here

def main():
	myAquarium = aquarium(0,3,2,500)
	while True:
		myAquarium.feed()
		time.sleep(86400) #sleeps for one day, adjust based on preference. Measured in seconds by default.



if __name__ == "__main__":
	main()

