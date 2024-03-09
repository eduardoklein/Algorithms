def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0
    for period in permanence_period:
        if isinstance(period[0], int) and isinstance(period[1], int):
            if target_time in range(period[0], period[1] + 1):
                count += 1
        else:
            return None
    return count
    raise NotImplementedError
