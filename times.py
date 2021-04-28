import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    """
    A function to represent equally spaced intervals within a time range as a list of tuples
    :param start_time: the start time of the time range
    :param end_time: the end time of the time range
    :param number_of_intervals: the number of equally spaced intervals (defaults to 1)
    :param gap_between_intervals_s: the number of seconds to be left as a gap between each of the intervals (default 0)
    :return: a list of tuples, each of which represents the start and the end of each interval in the time range
    """
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    """
    A function to compute all overlaps between two time ranges.
    :param range1: a time range
    :param range2: another time range
    :return: All overlapping time intervals as a list of tuples
    """
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time

