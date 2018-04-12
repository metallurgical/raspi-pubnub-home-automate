# Import pubnub(websocket publisher) module
from pubnub import Pubnub
import time

# Import GPIO module(General Purpose Input Output)
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO! Run 'sudo' when executing script

# Pubnub configuration keys(look on pubnub dashboard)
pubnub = Pubnub(publish_key="<publish-key>",subscribe_key="<subscribe-key>")

# Channel to listen from web page
pubnubChannelName = '<pub-nub-channel>'

# Flag checking either ON or OFF
glowLamp = False
glowFan = False

# Initialize GPIO and PIN used on raspi
def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(16, GPIO.OUT) # Make pin 16 to be an output
  GPIO.setup(4, GPIO.OUT) # Make pin 4 to be an output

# Pubnub callback(will trigger on every publish from webpage)
def gpioCallback(msg, channel):
  
  global glowLamp, glowFan

  # Set pin number used
  lampPin = 16
  fanPin = 4

  # Debugging purpose
  command = msg
  print "Command is : " + str(command)

  # Check for command exist or not from response
  if('req' in command):
      
    # Only affected on pin 16(coming from webpage)
    if (command['pin'] == "16"):
        
      if(command['req'] == 'toggle'):

        # Make pin ON/OFF
        if(glowLamp):
          glowLamp = False
        else:
          glowLamp = True

        # Finally set pin ON/OFF
        GPIO.output(lampPin, glowLamp)

    # Only affected on pin 16(coming from webpage)    
    else:    
        
      if (command['req'] == 'toggle'):

        # Make pin ON/OFF
        if(glowFan):
          glowFan = False
        else:
          glowFan = True

        # Finally set pin ON/OFF
        GPIO.output(fanPin, glowFan)


# PubNub error callback(will trigger if got an error during data transmited)
def _error(msg):
    print 'Error :' + msg
    return;

# Only execute this script when calling directly from command(not for module import)
if __name__ == '__main__':

  # Call initialization option
  setup()

  # Subscribe to channel and register both success and error callback of pubnub
  pubnub.subscribe(channels=pubnubChannelName,callback=gpioCallback, error=_error)

  # Endless loop(keep listening on websocket connection)
  try:
    while True:
    
      # On every loop, sleep for 5 seconds(freezing memory)
      time.sleep(5000)

      # Check for status of Pin 16(optional)
      status = GPIO.gpio_function(16)
                
      if(status): 
      
        #All is over
        break
    
  except KeyboardInterrupt:
    pass

  # Cleanup PIN after used
  finally:
    GPIO.cleanup()
