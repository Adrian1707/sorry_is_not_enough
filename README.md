If I was to name the company that infuriates me more than any other, it would be South West Trains. For such expensive tickets customers are delivered a horrific service, often made to stand throughout entire journeys due to overcrowding and delays are often frequent. 

I wanted to create a program that would scan their Twitter profile and find out how many times they've had to recently apologise for their shoddy service, so used the Python library 'Tweepy' to help me do that. There is an API limit of 200 tweets per request, so if the number of apologies reaches 20, then they're having to apologise in 10% of their tweets. It's very nice and British of them to do so, but as this repo states...sorry is not enough. 

I used Flask, a lightweight Python framework, to get this working in the browser.

## Install

```
Ensure you have python installed
git clone https://github.com/Adrian1707/sorry_is_not_enough
cd sorry_is_not_enough
pip install -r requirements.txt
python run.py
visit localhost:5000
```
## Improvements

I started this wanting to find out how many times they'd apologised on the current date, but after much searching I couldn't find a way for the API to let me do that. If anyone knows how then I'd appreciate a pull request. In the meantime we're just left with how frequently they're apologising for their awful service in general. 