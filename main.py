import argparse
from pathlib import Path

from config import MODEL_NAME, CONFIDENCE_THRESHOLD, OUTPUT_DIR, REPORT_FILE
from src.detector import ObjectDetector
from src.processor import process_image, process_video, process_webcam


def build_parser():
    parser = argparse.ArgumentParser(description="VisionTrack Computer Vision System")
    parser.add_argument("--mode", choices=["image", "video", "webcam"], required=True)
    parser.add_argument("--source", help="Path to image/video for image or video mode")
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--confidence", type=float, default=CONFIDENCE_THRESHOLD)
    parser.add_argument("--report", action="store_true")
    return parser


def main():
    args = build_parser().parse_args()
    detector = ObjectDetector(args.model, args.confidence)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    report_path = REPORT_FILE if args.report else None

    if args.mode == "webcam":
        process_webcam(detector, report_path)
    elif not args.source:
        raise SystemExit("--source is required for image/video mode")
    elif args.mode == "image":
        process_image(detector, args.source, report_path)
    else:
        process_video(detector, args.source, report_path)


if __name__ == "__main__":
    main()
