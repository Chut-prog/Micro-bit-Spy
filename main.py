from microbit import *
import log

log.set_labels('event_type', 'conv_duration', 'avg_sound', 'avg_temp', 'avg_light')

display.set_pixel(2, 2, 9)
sleep(10000)
display.clear()

ambient_noise_sum = 0
ambient_measures_count = 0

@run_every(s=3600)
def hourly_log():
    global ambient_noise_sum, ambient_measures_count
    
    if ambient_measures_count > 0:
        real_avg_sound = ambient_noise_sum // ambient_measures_count
    else:
        real_avg_sound = microphone.sound_level()
        
    log.add({
        'event_type': 0,
        'conv_duration': 0.0,
        'avg_sound': real_avg_sound,
        'avg_temp': temperature(),
        'avg_light': display.read_light_level()
    })
    
    ambient_noise_sum = 0
    ambient_measures_count = 0
    print("Automatic hourly log recorded.")

noise_threshold = 85
in_progress = False
start_time = 0
sound_sum = 0
temp_sum = 0
light_sum = 0
measures_count = 0

while True:
    sound = microphone.sound_level()
    light = display.read_light_level()
    temp = temperature()
    current_time = running_time()
    
    if sound > noise_threshold:
        if not in_progress:
            in_progress = True
            start_time = current_time
            sound_sum = sound
            temp_sum = temp
            light_sum = light
            measures_count = 1
        else:
            sound_sum += sound
            temp_sum += temp
            light_sum += light
            measures_count += 1
    else:
        ambient_noise_sum += sound
        ambient_measures_count += 1
        
        if in_progress:
            end_time = current_time
            conv_duration = (end_time - start_time) / 1000.0  
            avg_sound = sound_sum // measures_count
            avg_temp = temp_sum // measures_count
            avg_light = light_sum // measures_count
            
            log.add({
                'event_type': 1,
                'conv_duration': conv_duration,
                'avg_sound': avg_sound,
                'avg_temp': avg_temp,
                'avg_light': avg_light
            })
            
            print("Conversation recorded -> Duration:", conv_duration, "s | Avg Sound:", avg_sound)
            in_progress = False
            
    sleep(10)
