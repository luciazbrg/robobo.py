# This imports the library    


# This creates an instance of the Robobo class with the indicated IP address
# You have to modify next line
from robobopy.Robobo import Robobo
from robobopy_videostream.RoboboVideo import RoboboVideo

rob = Robobo("192.168.1.112")
video = RoboboVideo("192.168.1.112")
# This connects to the robobo base
rob.connect()

# This makes Robobo say "Hello World"
rob.sayText("Hello world")

# This disconnects from the robobo base
rob.disconnect()