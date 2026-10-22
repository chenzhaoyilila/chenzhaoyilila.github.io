import argparse
import sys

import yt_dlp

DEFAULT_URL = "https://www.youtube.com/watch?v=TnPP9JfSqBc"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download YouTube audio as MP3 using yt-dlp."
    )
    parser.add_argument(
        "url",
        nargs="?",
        default=DEFAULT_URL,
        help="YouTube video URL (optional; uses DEFAULT_URL if omitted).",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=".",
        help="Folder where the MP3 file will be saved (default: current directory).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "outtmpl": f"{args.output_dir}/%(title)s.%(ext)s",
        "quiet": False,
        "no_warnings": False,
    }

    print(f"Downloading audio from: {args.url}")
    print(f"Saving to folder: {args.output_dir}")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([args.url])
    except Exception as error:
        print(f"Download failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    print("Done.")


if __name__ == "__main__":
    main()
