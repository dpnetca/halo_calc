import argparse
import math
from data import bands, distance_to_centre


"""
TODO distance to halo func:
    * change return to provide more information (currently on provides int
      as centre of return should include start and end of band as well)
    * add error handling if target system name does not exist
    * add handling if path never intersects band
    * add handling if path intesects band twice
    * add '0' to return all bands
    * likely break into smaller functions and convert to class...
"""


def distance_to_halo(
    target: str, distance_to_target: int, distance_to_marker: int, band: int
) -> int:
    """
    Using the sine and cosine given any three elements of a triangle
    including one side, and 2 sides or angles, we can calculate all sides
    and angles of the triangle.

    Use the existing distances to form a triangle with three known sides
    the distance from current location to Stanton marker and target, and
    the distance from the target to Stanton marker.  With this we use the
    law of cosines to calculate the angle between the path to the target
    and the target to the Stanton marker.  As we travel to the target
    this angle does not change.
    We are now able to form a triangle with three known components, the
    distance from the target to the Stanton marker, the angle previously
    calculated, and the distance from the Standon marker to the desired path.
    Using the law of sines we can not calculate the length of the path at
    our desired band, or where we need to stop to land in the band

    Args:
        target (str): Name of target system, all lower case no spaces
        distance_to_target (int): distance in km from current location to
            the target location
        distance_to_marker (int): distance in km from current location to
            the Stanton marker
        band (int): band number (1-10), or 0 to show distances for all bands

    Returns:
        int: Distance from stopping point to target
    """
    # get angle of path and target to stanton marker using current position
    # and known side lengths with arccosine
    angle_a = math.acos(
        (
            distance_to_centre[target] ** 2
            + distance_to_target**2
            - distance_to_marker**2
        )
        / (2 * distance_to_centre[target] * distance_to_target)
    )

    # with known sides standon marker to target and halo, and known angle from
    # path and target to stanton marker, use arcsine to calculate angle from
    # path and band to standton marker
    angle_b = math.asin(
        distance_to_centre[target]
        * math.sin(angle_a)
        / bands[band + 1]["centre"]
    )

    # triangle laws state all angled must add up to pi radians (180 degrees)
    angle_c = math.pi - angle_a - angle_b

    # with 2 known sides and 3 known angles, finally calculate the last
    # side, this will be the distance where we need to stop
    band_intersect = (
        bands[band + 1]["centre"] / math.sin(angle_a)
    ) * math.sin(angle_c)

    return band_intersect


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("route_target", type=str, help="target system")
    parser.add_argument(
        "distance_to_target",
        type=str,
        help="distance from your current location to target",
    )
    parser.add_argument(
        "distance_to_marker",
        type=str,
        help="distance from your current location to standon marker",
    )
    parser.add_argument(
        "band",
        type=int,
        help="which halo band you want (1-10)",  # (0 to show all bands)
    )

    args = parser.parse_args()
    # allow inputs to be numeric only with or without , seperation
    # TODO add error handling here if input can not be converted to int
    distance_to_target = int(args.distance_to_target.replace(",", ""))
    distance_to_marker = int(args.distance_to_marker.replace(",", ""))
    # ensure target is lowercase with no spaces
    route_target = args.route_target.replace(" ", "").lower()
    # TODO add error handing on band input ensure valid range
    stop = distance_to_halo(
        route_target, distance_to_target, distance_to_marker, args.band
    )
    print(f"stop at centre {int(stop):,}km")


if __name__ == "__main__":
    main()
