from pytube import YouTube, Playlist

def video_downloader(link):
    youtube_1 = YouTube(link)

    # print(youtube_1.title)
    # print(youtube_1.description)
    # print(youtube_1.length)
    # print(youtube_1.thumbnail_url)
    # print(youtube_1.streaming_data)

    # video_streams = youtube_1.streams.all() #All Formats
    while True: #Checks for Valid Resolution / Extension Input
        while True: #Checks for Valid Download Input
            download_type = str(input("Do you want to download Video or Audio? "))
            if download_type.lower() == "video":
                stream_type = str(input("Input the Stream Type of the content you want to Download (in numbers): ")) + "p"
                file_type = str(input("Enter the File type you want to download (MP4 or WEBM): ").lower())
                video_streams = youtube_1.streams.filter(only_video = True, res = stream_type, file_extension = file_type, ) #Only Videos Streams
                break
            elif download_type.lower() == "audio":
                stream_type = str(input("Input the Stream Type of the content you want to Download (in numbers): ")) + "kbps"
                video_streams = youtube_1.streams.filter(only_audio = True, abr = stream_type) #Only Audio Streams
                break
            else:
                print("The Download Type Doesn't Exist, Please Try Again!")

        video = list(enumerate(video_streams)) #Makes a tuple list of the data received from the video.
        if len(video) != 0:
            for i in video: #For Checking Stream
                print(i)
            break
        else:
            print("The Stream Type / File Extension Doesn't Exist, Please Try Again!")

    #Download Prompt
    print(f"Downloading: {youtube_1.title}")
    enter = int(input("Stream: "))
    video_streams[enter].download()
    print("Downloaded Successfully")

def playlist_downloader(link):
    data_playlist = Playlist(link)

    print(f"Downloading: {data_playlist.title}")
    for video in data_playlist.videos:
        video_link = video.watch_url
        video_downloader(video_link)

def main():
    while True:
        content_type = str(input("Do you want to retrive the content of a single VIDEO or a PLAYLIST: ").lower())
        if content_type == "video" or content_type == "playlist":
            # link = str(input("Enter the Link: "))
            break
        else:
            print("Invalid Content Input, Please Try Again!")
    
    if content_type == "video":
        link = "https://youtu.be/d9MyW72ELq0"
        video_downloader(link)
    else:
        link = "https://www.youtube.com/playlist?list=PLHSr5eXnkaJkP4pOjcw_dx9JmwKclCI1-"
        playlist_downloader(link)

if __name__ == "__main__":
    main()