import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", type=str, help="target system")
    parser.add_argument(
        "-dt",
        "--distance_to_target",
        type=str,
        help="distance from your current location to target",
    )
    parser.add_argument(
        "-dm",
        "--distance_to_marker",
        type=str,
        help="distance from your current location to standon marker",
    )
    parser.add_argument(
        "-b",
        "--band",
        type=int,
        help="which halo band you want (1-10)",  # (0 to show all bands)
    )

    return parser.parse_args()
