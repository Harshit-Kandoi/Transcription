import os
import whisper

def find_media_files(directory):
    """Recursively scan a directory for audio and video files."""
    media_extensions = ['.mp3', '.wav', '.mp4', '.avi', '.mkv']  # Add more if needed
    media_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in media_extensions):
                media_files.append(os.path.join(root, file))
    
    return media_files

def transcribe_media_files(media_files, output_dir):
    """Transcribe media files using Whisper and save results as text files."""
    model = whisper.load_model("medium")  # Upgraded from 'tiny' to 'small' for better accuracy
    
    for file in media_files:
        try:
            print(f"Processing: {file}")
            result = model.transcribe(file)
            transcription = result['text'].strip()
            
            if not transcription:
                print(f"Warning: No transcription generated for {file}")
                continue
            
            output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(file))[0] + ".txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(transcription)
            
            print(f"✅ Transcription saved: {output_file}")
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

def main():
    input_directory = "media"  # Replace with your actual media folder path
    output_directory = "outputs"  # Replace with your output folder path

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created output directory: {output_directory}")

    media_files = find_media_files(input_directory)
    print(f"Found {len(media_files)} media files: {media_files}")

    if media_files:
        transcribe_media_files(media_files, output_directory)
    else:
        print("No media files found for transcription.")

if __name__ == "__main__":
    main()