import json
from yt_extractor import get_audio_url, get_video_info
from api_communication import save_transcript

def save_video_sentiments(url):
    video_info = get_video_info(url)
    audio_url = get_audio_url(video_info)
    title = video_info["title"]
    title = title.strip().replace(" ", "_")
    title = "data/" + title
    save_transcript(audio_url, title, sentiment_analysis= True)

if __name__ == "__main__":
    save_video_sentiments("") #input link of YouTube videdo here.


    #The JSON file that is returned from entering the Youtube Video is put into here, for it to be analyzed. 
    with open("data/JSON file goes here", "r") as f:
        data = json.load(f)

    positives = []
    negatives = []
    neutrals = []
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else: 
            neutrals.append(text)

    n_pos = len(positives)
    n_neg = len(negatives)
    n_neut = len(neutrals)

    print("Num positives: ", n_pos)
    print("Num negatives: ", n_neg)
    print("Num neutrals: ", n_neut)

    r = n_pos / (n_pos + n_neg)
    print(f"Positive ratio: {r:.3f}")

