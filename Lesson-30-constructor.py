class Keyboard:
   def __init__(self, language, connection):  # Corrected to __init__
         self.language = language
         self.connection = connection  # Fixed the attribute name "connectin" to "connection"

   def defination(self):
      print("Keyboard is an input device")
   
   def number_of_keys(self):
         print("There are 101 keys")

my_keyboard = Keyboard('English', 'wireless')  # Corrected "wirless" to "wireless" for consistency
print(my_keyboard.language)

class AboutMe:
      def __init__(self, name, address, occupation):
          self.name = name
          self.address = address
          self.occupation = occupation
      
      def talk(self):
          print(f"My name is {self.name}. I am from {self.address}, and I am a {self.occupation}.")

Shanto = AboutMe('Shanto', 'Bangladesh', 'Teacher')           
Shanto.talk()
