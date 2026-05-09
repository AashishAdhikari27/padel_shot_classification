"""
Test Script 1: Load and Display Video
Purpose: Make sure OpenCV is working and we can read the video
"""

import cv2
import os
import sys

print("🎬 Testing Video Loading...")
print("=" * 50)

# Path to your video
video_path = '../data/raw/input_sample_video.mp4'

# Check if file exists
if not os.path.exists(video_path):
    print("❌ ERROR: Video file not found!")
    print(f"   Looking for: {os.path.abspath(video_path)}")
    print("\n📝 Action needed:")
    print("   1. Put your video in data/raw/ folder")
    print("   2. Name it 'input_sample_video.mp4'")
    print("   3. Run this script again")
    sys.exit(1)

print(f"✅ Video file found: {video_path}")
print(f"   Full path: {os.path.abspath(video_path)}")
print(f"   File size: {os.path.getsize(video_path) / (1024*1024):.2f} MB")

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("❌ ERROR: Could not open video!")
    sys.exit(1)

print("✅ Video opened successfully!")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration = total_frames / fps

print("\n📊 Video Information:")
print(f"   Resolution: {width} x {height} pixels")
print(f"   FPS (Frames Per Second): {fps}")
print(f"   Total Frames: {total_frames}")
print(f"   Duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")

# Read the first frame
ret, frame = cap.read()

if ret:
    print("\n✅ Successfully read first frame!")
    print(f"   Frame shape: {frame.shape}")
    print(f"   Frame data type: {frame.dtype}")
    print(f"   Frame min/max values: {frame.min()} / {frame.max()}")
    
    # Save the first frame as an image
    os.makedirs('../data/processed', exist_ok=True)
    output_path = '../data/processed/first_frame.jpg'
    cv2.imwrite(output_path, frame)
    print(f"\n💾 Saved first frame to: {output_path}")
    print(f"   Full path: {os.path.abspath(output_path)}")
    
    # Save frames 100, 500, 1000 for reference
    frame_numbers = [100, 500, 1000]
    for frame_num in frame_numbers:
        if frame_num < total_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()
            if ret:
                output_path = f'../data/processed/frame_{frame_num}.jpg'
                cv2.imwrite(output_path, frame)
                print(f"   Saved frame {frame_num} to: {output_path}")
else:
    print("❌ ERROR: Could not read first frame!")

# Clean up
cap.release()
print("\n✅ Test completed successfully!")
print("=" * 50)
print("\n📸 View the saved frames:")
print("   nautilus ../data/processed/  # Or use your file manager")