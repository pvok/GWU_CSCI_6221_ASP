from abc import ABC, abstractmethod

class Spectacles(ABC):
   @abstractmethod
   def manufacture(self):
      pass

class RimlessSpectacles(Spectacles):
   def manufacture(self):
      print("Manufacturing Rimless Spectacles")

class FullFrameSpectacles(Spectacles):
   def manufacture(self):
      print("Manufacturing Full Frame Spectacles")

class SpectaclesFactory(ABC):
   @abstractmethod
   def create_spectacles(self):
      pass

class RimlessSpectaclesFactory(SpectaclesFactory):
   def create_spectacles(self):
      return RimlessSpectacles()

class FullFrameSpectaclesFactory(SpectaclesFactory):
   def create_spectacles(self):
      return FullFrameSpectacles()

class SpectaclesDecorator(Spectacles):
   def __init__(self, decorated_spectacles):
      self.decorated_spectacles = decorated_spectacles

   def manufacture(self):
      self.decorated_spectacles.manufacture()

class AntiGlareCoating(SpectaclesDecorator):
   def manufacture(self):
      super().manufacture()
      print("Adding Anti-Glare Coating on Lenses")

class PolarizedLenses(SpectaclesDecorator):
   def manufacture(self):
      super().manufacture()
      print("Polarizing the Lenses")
      
class BlueLightCoating(SpectaclesDecorator):
   def manufacture(self):
      super().manufacture()
      print("Adding Blue Light Filter on Lenses")      

def manufacture_spectacles(factory, anti_glare_coating, polarized_lenses, blue_light_coating):
   spectacles = factory.create_spectacles()

   if anti_glare_coating:
      spectacles = AntiGlareCoating(spectacles)

   if polarized_lenses:
      spectacles = PolarizedLenses(spectacles)

   if blue_light_coating:
      spectacles = BlueLightCoating(spectacles)

   spectacles.manufacture()

if __name__ == '__main__':
   factory = RimlessSpectaclesFactory()
   manufacture_spectacles(factory, True, False, False)
   manufacture_spectacles(factory, False, True, True)

   factory = FullFrameSpectaclesFactory()
   manufacture_spectacles(factory, True, True, True)
