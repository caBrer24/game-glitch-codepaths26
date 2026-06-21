# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? The game looked fun, with an easy to understand UI, but that was before the hints got me off track.
- List at least two concrete bugs you noticed at the start  
  - Hints are backwards. With a secret number of 93, I input 99. It said "Go higher"
  - The button "New Game" does not start a new game when game is done. Only worked when clicked in the middle of the game.
    I have to refresh the entire page to do so.
  - The score on the developer debug info goes negative. Does not match score, or there isn't any score tracker that matches the final score shown at the  end of the game.
  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  33   |  Go Higher hint         Go Lower           None
| New Game | Start new game |  Nothing |  None |
| 44    | Go Lower Hint    |  Go Higher | 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Sonnet 4.6
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). On even attempts, if I made a guess that triggered the "Too High" output, it would award me 5 points, even if it was wrong. I tested it using the developer info tab.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). Not something AI got wrong, but something it didn't catch until I brought it up; There was a mismatch between the score shown and the score displayed at the end/after guessing the number. It also didn't catch that the "Guess a number between..." was hardcoded and not based off the difficulty chosen. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? By playing the game multiple times while checking the developer info and until playing without any hiccup.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
