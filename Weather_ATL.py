"""
 This script is an example of getting the current weather data from 
 a webpage: "http://www.wsbtv.com/s/weather"
 
 Sample output:
      Current weather from WSBTV
      Monday, Feb. 9, 2015 | 10:20 p.m.
      Overcast
      Temperature: 47 degree (26.1 C)
      Humidity:  77%
      Pressure:  29.85 in.
      Wind:  From NNW at 17 mph

 Basic idea: 
            Load the content of the webpage, and save it as a string;
            Find the desired info (temperature, etc) in the string;

"""

import urllib   # import a package to handel webpages/url links

# open the weblink and get the 'object' the link 
response = urllib.urlopen("http://www.wsbtv.com/s/weather")

# read the string of the weblink object;
# html is a string with all the html source code of the webpage
html = response.read()

# find the lowest index in html where the "&deg;" sub is found
# In the string, the temperature is stored right before "&deg;"
EndofTemp_Index = html.find("&deg;")

# make a copy of the EndofTemp_Index
index = EndofTemp_Index

# Before the temperature, the character is '>'; after it, it is "&deg;"

# find the beginning index
# Move backward until '>' is found
while html[index] != '>':
  index = index - 1

# starting index of the temperature in html
StartofTemp_Index = index + 1 

# the text of temperature
textTemp = html[StartofTemp_Index:EndofTemp_Index]
temperature = int(textTemp)


### The following codes follow the same procedure to get other info ###
  
  ## Get Weather Description ##
start = html.find("cmWeatherDescription")
while html[start] != '>':
  start = start+1
start = start+1

end = start
while html[end] != '<':
  end = end+1
  
WeatherDescription = html[start:end].strip(' \t\n\r')


## Get Humidity Description ##
start = html.find("Humidity:")
while html[start] != '>':
  start = start+1
start = start+1
end = start
while html[end] != '<':
  end = end+1
Humidity = html[start:end].strip(' \t\n\r')


## Get Pressure Description ##
start = html.find("Pressure:")
while html[start] != '>':
  start = start+1
start = start+1
end = start
while html[end] != '<':
  end = end+1
Pressure = html[start:end].strip(' \t\n\r')

## Get Wind Description ##
start = html.find("Wind:")
while html[start] != '>':
  start = start+1
start = start+1
end = start
while html[end] != '<':
  end = end+1
  
Wind = html[start:end].strip(' \t\n\r')

## Get Date and Time Description ##
start = html.rfind("cmHeaderCap005")+19
end = start
while html[end] != '<':
  end = end+1
  
DateTime = html[start:end].strip(' \t\n\r')

print "    Current weather from WSBTV"
print "   ", DateTime
print "   ", WeatherDescription
print ("    Temperature: %d degree (%.1f C)") % (temperature, (temperature-32)*5./9.)
print "    Humidity: ", Humidity
print "    Pressure: ", Pressure
print "    Wind: ", Wind
  
