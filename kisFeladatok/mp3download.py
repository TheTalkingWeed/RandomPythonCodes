from pytube import YouTube
import os
import sys

def check_file(file_name,des):
    files = os.listdir(des)
    sub_files = [name for name in files if os.path.isfile(des+'/'+name)]

    return file_name in sub_files

def load_links(file_name):
    if check_file(file_name):
        with open(file_name,'r') as f:
            contents = f.read().splitlines()
        return contents
    else:
        print("A linkeket tartalmazo fajl nem talalhato.")



def download(link):
    print("egy")
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    print("ketto")
    destination = "C:\\Users\\Alex\\Music"
    print("itt van ")

    if check_file(yt.title + ".mp3",destination):
        print("A zene mar letoltve: ",yt.title)
    else:

        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")


def main():
    #links = load_links("linkek.txt")

    download("https://www.youtube.com/watch?v=27rPtLv60fc")

if __name__ == "__main__":
    main()