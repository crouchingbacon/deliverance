define shootout_timeout = 8

# `jump shootout` starts the shootout sequence

label shootout_end_out_of_time:
    "No...!"
    return

label shootout_end_oberon_shot:
    "I...I got him..."
    return

label shootout_end_out_of_bullets:
    "Fuck! I'm empty!"
    return
label shootout_shot_missed:
    "Damnit! Missed."
    return

label shootout_shot_nic:
    "No! I can't risk shooting her..."
    return
