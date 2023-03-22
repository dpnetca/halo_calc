from data import distance_to_centre
from halo import HaloDistance
import cli


def main():
    args = cli.get_args()

    distance_to_target = args.distance_to_target.replace(",", "")
    if not distance_to_target.isdigit():
        print("ERROR, distance to target must be an integer value.")
        exit(1)
    distance_to_target = int(distance_to_target)

    distance_to_marker = args.distance_to_marker.replace(",", "")
    if not distance_to_marker.isdigit():
        print("ERROR, distance to marker must be an integer value.")
        exit(1)
    distance_to_marker = int(distance_to_marker)

    target = args.target.replace(" ", "").lower()
    if target not in distance_to_centre.keys():
        print(f"ERROR, {args.route_target} is not a valid target")
        exit(1)

    if args.band < 0 or args.band > 10:
        print("ERROR, band must be an integer value between 0 and 10.")
        exit(1)

    halo = HaloDistance(distance_to_marker)

    halo.to_band(target, distance_to_target, args.band)

    # halo.to_bands(route_target, distance_to_target)


if __name__ == "__main__":
    main()
