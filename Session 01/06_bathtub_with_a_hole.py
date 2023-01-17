### Code to complete [START] ###

water_vol = 0
filled_time  = 0

while water_vol < 80:
    water_vol += 11
    filled_time += 1
filled_time = filled_time + ((80 - water_vol)/11)