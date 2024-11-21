import yt_dlp
from colorama import Fore, Style, init
import sys

init(autoreset=True)

def fetch_video_data(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            return ydl.extract_info(channel_url, download=False)
        except Exception as e:
            print(f"{Fore.RED}Error fetching data: {e}")
            sys.exit(1)

def display_channel_info(channel_data):
    if 'entries' in channel_data:
        channel_title = channel_data.get('title')
        channel_id = channel_data.get('id')

        if " - Videos" in channel_title:
            channel_title = channel_title.replace(" - Videos", "")

        print(f"{Fore.GREEN}Channel: {Fore.YELLOW}{channel_title}")
        print(f"{Fore.GREEN}Channel ID: {Fore.YELLOW}{channel_id}\n")
        print(f"{Fore.GREEN}Videos:\n")
        print(f"{Fore.CYAN}{'Title':<80} {'Views':<10} {'URL'}")
        print(f"{Fore.WHITE}-" * 110)

        return True
    return False

def print_video_details(video_data, total_views):
    for entry in video_data:
        video_url = f"https://www.youtube.com/watch?v={entry['id']}"
        video_title = entry['title']
        video_views = entry.get('view_count', 0)

        print(f"{Fore.YELLOW}{video_title:<80} {Fore.CYAN}{video_views:<10} {Fore.BLUE}{video_url}")

        total_views += video_views

    return total_views

def get_channel_videos(channel_url):
    channel_data = fetch_video_data(channel_url)
    
    if display_channel_info(channel_data):
        total_views = 0
        total_views = print_video_details(channel_data['entries'], total_views)

        print(f"\n{Fore.WHITE}{'-' * 110}")
        print(f"{Fore.GREEN}Total Views for all videos: {Fore.RED}{total_views:,}")
    else:
        print(f"{Fore.RED}No videos found in this channel.")

if __name__ == "__main__":
    channel_url = input(f"{Fore.MAGENTA}Enter the YouTube channel URL: ")
    get_channel_videos(channel_url)
