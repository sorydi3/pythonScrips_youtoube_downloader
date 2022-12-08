# Path: convertToMp3.py
import os


class CoverterToMp3:
    def __init__(self, from_format, to_format, sorce_path, destination_path):
        self.from_format = from_format
        self.to_format = to_format
        self.sorce_path = sorce_path
        # create destination folder
        self.make_dir_destination(destination_path)
        self.destination_path = destination_path

    def make_dir_destination(self, destination_path):
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

    def convert(self):
        print("Converting...%s", self.sorce_path)
        self.rename()
        files = [f for f in os.listdir(
            self.sorce_path) if f.endswith(self.from_format)]
        print("SIZE...%s", len(files))
        for file in files:
            print(file)
            input_path = os.path.join(self.sorce_path, file)
            output_path = os.path.join(
                self.destination_path, file.replace(self.from_format, self.to_format))
            print(file)
            os.system(
                f"ffmpeg -i {input_path} -acodec libmp3lame {output_path}")

    def rename(self):
        files = [f for f in os.listdir(
            self.destination_path) if f.endswith(self.to_format)]
        for file in files:
            input_path = os.path.join(self.destination_path, file)
            output_path = os.path.join(self.destination_path, file.encode(
                'ascii', 'ignore').decode('ascii').replace("_", "").replace("-", "").replace(" ", "_").replace("&", "_"))
            os.rename(input_path, output_path)

    def list_files(self):
        files = [f for f in os.listdir(
            self.sorce_path) if f.endswith(self.from_format)]
        for file in files:
            print(file)
