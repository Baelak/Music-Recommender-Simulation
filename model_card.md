# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Zema 1.0 ~ ዜማ 1.0**  

---

## 2. Intended Use  

- This recommender suggests songs based on a user's preferred genre, mood, and audio features like energy and tempo. It assumes the user knows what they like and can describe it with specific values. This is a classroom simulation, not a production system.  

---

## 3. How the Model Works  

- Each song is scored by checking if the genre and mood match, then measuring how close the song's energy, tempo, and other features are to what the user wants. Genre is worth the most points since it's the strongest signal. The final score combines all of that into a ranking.

---

## 4. Data  

- The catalog has 17 songs across 14 genres, including lofi, rock, pop, jazz, classical, and folk. Most genres only have one song, so the dataset is pretty thin. Moods like happy, chill, and intense are covered, but other tastes like metal, R&B, or country are mostly missing. 

---

## 5. Strengths  

- It works best when the user knows exactly what they want. If you're a lofi listener or a workout music person, the top result is almost always the right one. In those cases, the top result almost always felt right. Genre and mood matching does a good job of anchoring the recommendations to something meaningful before the numeric scores even factor in.

---

## 6. Limitations and Bias 


- Most genres only have one song. So the system always plays that song first, then fills the rest of the list with whatever it can find. It's less of a recommendation and more of a "here's the only option, plus some others.".

---

## 7. Evaluation  


- I tested three user profiles: a late night coder, a workout listener, and a Sunday morning listener. The top results matched what I expected, the right genre and mood came up first each time.

I also tried doubling the energy weight and halving the genre bonus to see what changed. Most results stayed the same, but the top two lofi songs swapped positions by just 0.06 points, which shows how close those scores actually were.

---

## 8. Future Work  

- The biggest fix would be adding more songs per genre so results aren't dominated by a single track. It would also help to let users rate recommendations and adjust the weights over time based on what they actually like.

---

## 9. Personal Reflection  

- The biggest surprise was how much the genre bonus controlled everything. Even when we changed other weights, the top results barely moved. It was also interesting how a simple math formula can feel like a real recommendation app. I used AI tools to write and check the code faster, but I still had to verify the logic myself to catch edge cases. Next upgrade, I would want users to rate songs so the system could learn their taste over time.  
