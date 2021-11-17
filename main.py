from utils import DataLoader
from core.DetectViolation import check_signal_violation, check_centerline_violation


def run():
    m_lanes, m_traffic_lights, m_objects = DataLoader('source name')

    for frame_no, (lanes, traffic_lights, objects) in enumerate(zip(m_lanes, m_traffic_lights, m_objects)):
        is_violation = [
            check_signal_violation(),
            check_centerline_violation()
        ]
        print('[#{}] Signal violation: {} Centerline violation: {}'.format(frame_no, *is_violation))


if __name__ == '__main__':
    run()
