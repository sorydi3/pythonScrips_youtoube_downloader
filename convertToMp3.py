import os

# The path to the folder containing the .webm files
webm_folder = os.path.join(r"C:\Users\ibrah\pythonScrips", "videos2")

# The path to the folder where the .mp3 files should be saved
mp3_folder = os.path.join(r"C:\Users\ibrah\pythonScrips", "videos2", "mp3")


# Get a list of all .webm files in the webm folder
webm_files = [f for f in os.listdir(webm_folder) if f.endswith(".webm")]

for webm_file in webm_files:

    # Construct the input and output file paths
    input_path = os.path.join(webm_folder, webm_file)

    output_path = os.path.join(webm_folder, webm_file.encode(
        'ascii', 'ignore').decode('ascii').replace("_", "").replace("-", "").replace(" ", "_").replace("&", "_"))
    os.rename(input_path, output_path)

webm_files = [f for f in os.listdir(webm_folder) if f.endswith(".webm")]

# Convert each .webm file to an .mp3 file

for webm_file in webm_files:
    # Construct the input and output file paths
    input_path = os.path.join(webm_folder, webm_file)
    output_path = os.path.join(mp3_folder, webm_file.replace(".webm", ".mp3"))
    print(webm_file)
    # Use ffmpeg to convert the .webm file to an .mp3 file
    os.system(f"ffmpeg -i {input_path} -acodec libmp3lame {output_path}")
