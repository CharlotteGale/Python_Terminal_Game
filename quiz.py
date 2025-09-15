
class Question:
    def __init__(self, question_text, choices, answer):
        self.question_text = question_text
        self.choices = choices
        self.answer = answer

    def ask(self):
        """Ask the user a question and return True if answered correctly, False if not."""
        print(self.question_text)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        choice = input(f"Your answer (1-{len(self.choices)}): ").strip()

        while True:
            choice = input(f"Your answer (1-{len(self.choices)}): ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(self.choices):
                    print()
                    return self.choices[idx - 1] == self.answer
            print("Please enter a number from the list.\n")

def main():
    questions = [
        Question("Q1. What position does Harry play in Quidditch?",
                 ["Chaser", "Seeker", "Beater", "Keeper"], "Seeker"),
        Question("Q2. What is the name of Hagrid's giant half-brother?",
                 ["Aragog", "Norbert", "Fluffy", "Grawp"], "Grawp"),
        Question("Q3. What gift does Mrs. Weasley give Harry each year?",
                 ["A fruitcake", "A new sweater", "A pair of socks", "A book"], "A new sweater"),
        Question("Q4. What spell can be used to summon objects?",
                 ["Lumos", "Reducto", "Accio", "Protego"], "Accio"),
        Question("Q5. What is the Ravenclaw emblem?",
                 ["Raven", "Eagle", "Owl", "Osprey"], "Eagle"),
        Question("Q6. What was Fred Weasley's code name on Potterwatch?",
                 ["Rapier", "Romulus", "River", "Royal"], "Rapier"),
        Question("Q7. Dumbledore has a scar above his left knee that is a perfect map of what?",
                 ["Hogwarts", "Diagon Alley", "London Underground", "Surrey"], "London Underground"),
        Question("Q8. Who is the Ghost of Hufflepuff?",
                 ["The Bloody Baron", "The Grey Lady", "The Fat Friar", "Nearly Headless Nick"], "The Fat Friar"),
        Question("Q9. Who was the first person to break out of Azkaban?",
                 ["Barty Crouch Jr", "Lucius Malfoy", "Bellatrix Lestrange", "Sirius Black"], "Sirius Black"),
        Question("Q10. What is the core of Hermione Granger's wand?",
                 ["Thestral Hair", "Unicorn Hair", "Dragon Heartstring", "Phoenix Feather"], "Dragon Heartstring")
    ]

    print("Are You a Potterhead?")
    house = input("What is your Hogwarts House?") or "Your House"
    print(f"Don't let {house} down!\n")

    score = 0
    for question in questions:
        if question.ask():
            score += 1
            print(f"Correct! 10 points to {house}!")
        else:
            print(f"Incorrect, the correct answer is {question.answer}")

    print("=" * 40)
    print(f"You earned {house} {score * 10} points!")
    print(f"You got {score} questions right out of {len(questions)}!")
    print("=" * 40)

if __name__ == "__main__":
    main()
