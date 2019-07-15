import pyowm
owm = pyowm.OWM("616d91844813fd9746ff4f205cea0bf3")
observation = owm.weather_at_place("london, uk")
w = observation.get_weather()

w.get_wind()
w.get_humidity()