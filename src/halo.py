import math
from typing import Tuple
from data import bands, distance_to_centre


class HaloDistance:
    def __init__(self, distance_to_marker: int):
        self.distance_to_marker = distance_to_marker

    def to_band(self, target: str, distance_to_target: int, band: int):
        if band == 0:
            self.to_bands(target, distance_to_target)
            return
        centre = self._to_mid_band(target, distance_to_target, band)
        if centre > distance_to_target:
            print(f"Selected path does not intersect halo band {band}")
            return
        start, end = self._to_band_edges(target, distance_to_target, band)

        print(f"stop between {int(start):,}km and {int(end):,}km")
        print(f"stop at centre {int(centre):,}km")

    def to_bands(self, target: str, distance_to_target: int):
        for band in range(1, 11):
            print(f"Band {band}:")
            self.to_band(target, distance_to_target, band)
            print()

    def _to_mid_band(
        self, target: str, distance_to_target: int, band: int
    ) -> int:
        return self._calculate_interesect(
            distance_to_centre[target],
            distance_to_target,
            bands[band]["centre"],
        )

    def _to_band_edges(
        self, target: str, distance_to_target: int, band: int
    ) -> Tuple[int, int]:
        band_start = bands[band]["centre"] - bands[band]["width"] / 2
        band_end = bands[band]["centre"] + bands[band]["width"] / 2
        start = self._calculate_interesect(
            distance_to_centre[target],
            distance_to_target,
            band_start,
        )
        end = self._calculate_interesect(
            distance_to_centre[target],
            distance_to_target,
            band_end,
        )
        return (start, end)

    def _calculate_interesect(self, centre, target, band):
        angle_a = math.acos(
            (centre**2 + target**2 - self.distance_to_marker**2)
            / (2 * centre * target)
        )
        angle_b = math.asin(centre * math.sin(angle_a) / band)
        angle_c = math.pi - angle_a - angle_b
        band_intersect = (band / math.sin(angle_a)) * math.sin(angle_c)

        return band_intersect
