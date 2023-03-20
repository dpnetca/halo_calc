import math
from data import bands, distance_to_centre


class HaloDistance:
    def __init__(self, distance_to_marker: int):
        self.distance_to_marker = distance_to_marker

    def to_mid_band(
        self, target: str, distance_to_target: int, band: int
    ) -> int:
        return self._calculate_interesect(
            distance_to_centre[target],
            distance_to_target,
            bands[band]["centre"],
        )

    def _calculate_interesect(self, centre, target, band):
        angle_a = math.acos(
            (centre**2 + target**2 - self.distance_to_marker**2)
            / (2 * centre * target)
        )
        angle_b = math.asin(centre * math.sin(angle_a) / band)
        angle_c = math.pi - angle_a - angle_b
        band_intersect = (band / math.sin(angle_a)) * math.sin(angle_c)

        return band_intersect
