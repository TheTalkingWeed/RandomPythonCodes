from pytube import YouTube
import os

def load_links():
    with open('linkek.txt','r') as f:
        contents = f.read().splitlines()
    
    return contents


def download(link):
    yt = YouTube(link)
  
    video = yt.streams.filter(only_audio=True).first()
    
   
    destination = "C:\\Users\\Alex\\Music"
    
    out_file = video.download(output_path=destination)
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    print(yt.title + " has been successfully downloaded.")

def main():
    links = load_links()
    for i in range(len(links)):
        download(links[i])
        print("Letöltve: ",i+1," maradt: ",len(links) - (i + 1)   )

    print("COMPLETED")


if __name__ == "__main__":
    main()