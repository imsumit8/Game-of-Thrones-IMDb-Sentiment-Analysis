import requests
import csv
url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"

querystring = {"tconst":"tt0944947"}

headers = {
	"X-RapidAPI-Key": "39ef32686fmsh77806f90a2ef1f7p18fa6djsn8015fc42af1a",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}




list=[]
# Print json data using loop
for i in range(220):  # In each loop we are getting 25 reviews by hitting the API
    response = requests.get(url, headers=headers, params=querystring)
    # print(response.json())
    API_Data = response.json()
    querystring["paginationKey"]=API_Data["paginationKey"]
    for key in API_Data["reviews"]:
        #print(key, ":", API_Data[key][''])
        #print(key)
        if key.get('authorRating')==None:
            authorRating = None;
        else:
            authorRating = key['authorRating']
        if key.get('helpfulnessScore')==None:
            helpfulnessScore = None;
        else:
            helpfulnessScore = key['helpfulnessScore']

        list.append([key['id'], key['languageCode'], key['submissionDate'], key['reviewText'], authorRating, helpfulnessScore , key['spoiler']])

print(list)
with open('GOT_main', 'w', encoding='utf-8') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)


    write.writerows(list)
