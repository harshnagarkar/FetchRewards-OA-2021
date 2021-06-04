# Fetch Rewards Online Assesment
## Design Sentence Similarity API from scratch

### Getting started
Run the following command to download the docker image and run it port 5000
```
docker pull hknagark/fetchrewards-oa-2021:latest
docker run -p 5000:80 hknagark/fetchrewards-oa-2021:latest
```
### Algorithm
Input: Two string S1 and S2.

Body:
    Preprocessing: 
        Remove Punctuation
        Split using Space and convert into list
        Convert the list into defaultDictionary 
            Key: Word in list
            Value: Heap made of list containing the index where the word occured
    Processing
        Calculate Manhattan distance for each word in S1 and S2
            Words in S1 Present in S2:
                Use the Manhattan distance Formula
            Words in S1 not Present in S2:
                Assign the length of list(S1) which is maximum distance where the word would be present if it was their
            Words in S2 not Present in S1:
                Assign the length of list(S1) which is maximum distance where the word would be present if it was their
        Post Processing:
            Get the distance, total count of word processed and the max distance that is length of sentence S1
            Normalize the Distance with distance calculated divied by the (max distance*count of words processed)
            Calculate the cosine value of the distance processed
Output:
    The Cosine similarity score that takes into account not only intersection and disjoint set of words but also the magnitude of where the word displacement between two texts

### API
Flask framework is used.

"/": This is Hello world path, inorder to ensure that the service is running.

"/comparestring": This path takes in two POST variable lower case 's1' and 's2' and return the similarity score using the algorithm described above

### Containment
Flask docker container
https://github.com/tiangolo/uwsgi-nginx-flask-docker

### Discussion
* I do belive that the stop words do add a value in my model and hence I decide to keep them while processing. 
* Also this is memory intensive processing as if the two sentences are big enough then it will take significant amount of time to process.
* Nginx is running in UWSGI mode in the backend, this means that the threads will have a definite time limit to process a call. Sentence exceed this limit will end up with either 500 or 400 level error.
* Because of UWSGI there should be independent threads to process the call, so simultaneous requests should be handled by the server.
