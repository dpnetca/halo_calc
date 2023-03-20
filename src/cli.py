import argparse


def get_args():
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

    return parser.parse_args()
