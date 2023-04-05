import os
from pydub import AudioSegment
#file_paths = ['/path/to/file1.mp3', '/path/to/file2.mp3', '/path/to/file3.mp3']
file_paths = ['dababy-suge-lyrics-1.mp3', 'samsung-notification-sound-bass-boosted.mp3' ]
output_file_name = 'output.mp3'
output_path = os.path.join(os.getcwd(), output_file_name)

def merge_mp3_files(file_paths, output_path):
    combined = AudioSegment.empty()
    for file_path in file_paths:
        sound = AudioSegment.from_mp3(file_path)
        combined += sound
    combined.export(output_path, format='mp3')
merge_mp3_files(file_paths, output_path)
