# | **Beginner** | **Game** | **15. Mad Libs Generator** | User input, string formatting (f-strings). |
import random

while True:
    # asking the user to enter different parts of speech
    adjective1 = input("Enter an Adjective : ")
    plural_noun = input("Enter a plural noun : ")
    liquid = input("Enter a type of liquid : ")
    verb = input("Enter a verb (ending in -ing) : ")
    place = input("Enter a place : ")
    adjective2 = input("Enter an adjective : ")
    past_tense_verb = input("Enter a past tense verb : ")

    # Various list items, to let user get something different every time.

    l1 = f"Yesterday, my {adjective1} pet {plural_noun} decided to escape. I chased it down the street, tripping over a bucket of {liquid}. The whole neighborhood could hear it {verb} as it ran toward the {place}. Its fur was suddenly {adjective2}, and it {past_tense_verb} straight into the sewer. I think I need a new hobby."

    l2 = f"Our captain was known for his {adjective1} bravery, but even he hesitated when the ship's sensor picked up {plural_noun} approaching at light speed. We had to jettison all our cargo, including 50 barrels of frozen {liquid}. The emergency beacon began {verb} before we even left the system. Our destination, a remote research station on {place}, was visible on the screen. The captain's face turned {adjective2} as he suddenly {past_tense_verb} the controls, sending us hurtling into the black void."

    l3 = f"Life in the castle was usually quite {adjective1}, filled with feast preparation and training the squires. However, a local wizard had recently turned all the {plural_noun} in the village into sentient beings. This meant that the water supply, a vast pool of {liquid}, was constantly {verb} and churning with life. The court jester, a man of great reputation in this {place}, tried to reason with them. He was found hours later, looking {adjective2}, and claimed the little creatures had {past_tense_verb} his favorite hat."

    l4 = f"In the {adjective1} basement of the old factory, Dr. Blork was performing his dangerous experiments. His latest creation, a hybrid species of sentient {plural_noun}, was becoming unstable. They needed regular feedings of pure, thick {liquid}, which they absorbed while {verb} softly to themselves. When the creatures escaped and ran through the industrial park—a truly creepy {place}—the entire facility was put on lockdown. Security found them, looking quite {adjective2}, near the ventilation shaft after they {past_tense_verb} through the steel door."

    l5 = f"Our plan to steal the {adjective1} crown jewels relied entirely on three trained {plural_noun}. They were supposed to use a long siphon to drain the protective moat, which was inexplicably filled with sparkling {liquid}. Instead, they got distracted, and soon the central alarm was {verb} loudly throughout the bank's lobby. This was not the secure vault in {place} we had planned for. I felt completely {adjective2} when my partner, Leo, finally {past_tense_verb} the bag of chips he'd been hiding in his pocket."

    l6 = f"Exploring the {adjective1} deep-sea trench revealed many secrets, including schools of shimmering {plural_noun} that had never been cataloged. Our submarine was filled with pressurized {liquid} to equalize the exterior pressure. The pilot had difficulty navigating when the sea monsters began {verb} around the hull. We finally anchored in a strange, glowing {place} at the bottom of the trench. The creatures there were oddly {adjective2} and immediately {past_tense_verb} their massive tails toward our lights."

    list_of_stories = [l1, l2, l3, l4, l5, l6]

    # Choosing stories randomly
    story = random.choice(list_of_stories)
    print(story)

    # if user wants to play more..........
    query = input("Wanna try once more? (y/n) : ")
    if query.lower() == 'y':
        continue
    elif query.lower() == 'n':
        break
    else:
        print("Invalid choice ❌...Choose either 'y' or 'n'.")