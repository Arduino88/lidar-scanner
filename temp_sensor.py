import machine, onewire, ds18x20, time

ir_rangefinder = machine.ADC(machine.Pin(33))
led_pin = machine.Pin(2, machine.Pin.OUT)
ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

ir_rangefinder.atten(machine.ADC.ATTN_11DB)
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  distance = ir_rangefinder.read()

  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    temp = ds_sensor.read_temp(rom)
    if temp > 24:
        led_pin.on()
    else:
        led_pin.off()
    print(f'temp is: {temp}')
    print(f'distance is: {distance}')
  time.sleep(1) 
