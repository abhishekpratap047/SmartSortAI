import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from processor import process_file

WATCH_FOLDER = "uploads"


class SmartSortHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        try:

            filepath = event.src_path

            print(
                f"\nNew file detected: {filepath}"
            )

            # Give Windows time to finish copying the file
            time.sleep(2)

            process_file(filepath)

        except Exception as e:

            print(
                "Processing Error:",
                e
            )


def start_monitor():

    os.makedirs(
        WATCH_FOLDER,
        exist_ok=True
    )

    observer = Observer()

    observer.schedule(
        SmartSortHandler(),
        WATCH_FOLDER,
        recursive=False
    )

    observer.start()

    print(
        f"Watching folder: {WATCH_FOLDER}"
    )

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("\nStopping monitor...")

        observer.stop()

    observer.join()


if __name__ == "__main__":
    start_monitor()