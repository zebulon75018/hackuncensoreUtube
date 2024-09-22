import argparse
import moviepy.editor as mp
from moviepy.video.fx.all import crop

def split_video(video_path):
    # Load the video
    video = mp.VideoFileClip(video_path)
    width, height = video.size
    
    # Split the video into left and right halves
    left_video = crop(video, x1=0, y1=0, x2=width//2, y2=height)
    right_video = crop(video, x1=width//2, y1=0, x2=width, y2=height)
    
    return left_video, right_video

def mute_alternate_seconds(audio, start_mute=0):
    segments = []
    
    # Create segments, muting every other second starting from `start_mute`
    for i, (start, end) in enumerate(zip(range(0, int(audio.duration)), range(1, int(audio.duration) + 1))):
        segment = audio.subclip(start, end)
        if (i + start_mute) % 2 == 0:
            segment = segment.volumex(0)
        segments.append(segment)
    
    return mp.concatenate_audioclips(segments)

def process_video(video_path):
    # Split the video
    left_video, right_video = split_video(video_path)
    
    # Mute alternate seconds
    left_audio = mute_alternate_seconds(left_video.audio, start_mute=0)
    right_audio = mute_alternate_seconds(right_video.audio, start_mute=1)
    
    # Set new audio to the videos
    left_video = left_video.set_audio(left_audio)
    right_video = right_video.set_audio(right_audio)
    
    # Save the videos
    left_video.write_videofile("left_video.mp4", codec="libx264", audio_codec="aac")
    right_video.write_videofile("right_video.mp4", codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a video into two halves with specified mute patterns.")
    parser.add_argument("video_path", help="Path to the input video file")
    args = parser.parse_args()

    process_video(args.video_path)

