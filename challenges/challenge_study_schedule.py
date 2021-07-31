def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for p in permanence_period:
            if target_time >= p[0] and target_time <= p[1]:
                counter += 1
        return counter
    except TypeError:
        return None
