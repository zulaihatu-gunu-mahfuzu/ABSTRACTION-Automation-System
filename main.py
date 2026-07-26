from abc import ABC, abstractmethod

# Abstract class
class BuildingSystem(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

# Child class 1
class AirConditioningSystem(BuildingSystem):

    def start(self):
        print("Air Conditioning System started.")

    def stop(self):
        print("Air Conditioning System stopped.")

    def status(self):
        print("Air Conditioning System is running.")
# Child class 2
class LightingSystem(BuildingSystem):

    def start(self):
        print("Lighting System turned on.")

    def stop(self):
        print("Lighting System turned off.")

    def status(self)
        print("Lighting System is operational.")

# Child class 3
class SecuritySystem(BuildingSystem):

    def start(self):
        print("Security System activated.")

    def stop(self):
        print("Security System deactivated.")

    def status(self):
        print("Security System is monitoring the building.")
New child class
class FireAlarmSystem(BuildingSystem):

    def start(self):
        print("Fire Alarm System activated.")
    
    def stop(self):
        print("Fire Alarm System deactivated.")

    def status(self):
        print("Fire Alarm System is ready.")

Store objects in a list
systems = [
      AirConditioningSystem(),
      LightingSystem(),
      SecuritySystem(),
      FireAlarmSystem()
]

# Demonstrate polymorphism
for system in systems:
    system.start()
    system.status()
    system.stop()
    print("-" * 40)
