"""
Generate basic foundational knowledge training data.
Covers: greetings, word meanings, numbers, colors, shapes, animals,
days, months, seasons, grammar rules, simple facts, basic math Q&A,
and common sense reasoning — all in Instruction/Response format.
"""

import random

data = []

# ─────────────────────────────────────────────
# 1. GREETINGS & SMALL TALK
# ─────────────────────────────────────────────
greetings = [
    ("hello", "Hello! How can I help you today?"),
    ("hi", "Hi there! What can I do for you?"),
    ("hey", "Hey! Good to hear from you."),
    ("hello there", "Hello! I'm here and ready to help."),
    ("good morning", "Good morning! I hope you have a wonderful day."),
    ("good afternoon", "Good afternoon! How's your day going?"),
    ("good evening", "Good evening! How can I assist you?"),
    ("good night", "Good night! Sleep well and rest easy."),
    ("how are you", "I'm doing great, thank you for asking! How about you?"),
    ("how are you doing", "I'm doing well! I'm here to help whenever you need."),
    ("what is your name", "I am an AI language model. You can call me GPT."),
    ("who are you", "I am an AI assistant built to understand and generate language."),
    ("what can you do", "I can answer questions, explain things, write text, and have conversations with you."),
    ("are you a robot", "I am an artificial intelligence, a language model trained to understand text."),
    ("are you human", "No, I am an AI. I am a computer program designed to understand and generate language."),
    ("what is your purpose", "My purpose is to help people by answering questions and generating useful text."),
    ("thank you", "You're welcome! Happy to help anytime."),
    ("thanks", "No problem! Feel free to ask anything else."),
    ("bye", "Goodbye! Have a great day!"),
    ("goodbye", "Goodbye! Come back anytime you need help."),
    ("see you later", "See you later! Take care."),
    ("how old are you", "I don't have an age. I am an AI without a physical body or birthday."),
    ("where are you from", "I exist as software. I don't have a physical location."),
    ("can you help me", "Of course! Tell me what you need and I'll do my best to help."),
    ("what time is it", "I don't have access to real-time information, but I can help with many other things."),
    ("are you smart", "I am designed to be helpful and to understand language well."),
    ("do you understand me", "Yes, I understand your text. Please go ahead and ask your question."),
    ("what do you know", "I have learned from a large amount of text and can help with many topics."),
    ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
    ("make me laugh", "Why did the bicycle fall over? Because it was two-tired!"),
]

for q, a in greetings:
    for _ in range(6):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 2. WHAT IS THE MEANING OF... (Word Definitions)
# ─────────────────────────────────────────────
definitions = [
    ("happy", "Happy means feeling pleasure, joy, or contentment. Example: She was happy to see her friend."),
    ("sad", "Sad means feeling sorrow or unhappiness. Example: He felt sad when he lost his toy."),
    ("angry", "Angry means feeling strong displeasure or hostility. Example: She was angry when her plan failed."),
    ("love", "Love is a deep feeling of affection and care for someone or something."),
    ("hate", "Hate means feeling intense dislike or hostility toward someone or something."),
    ("big", "Big means large in size. Example: An elephant is a big animal."),
    ("small", "Small means little in size. Example: An ant is a small insect."),
    ("fast", "Fast means moving or happening quickly. Example: A cheetah is a fast animal."),
    ("slow", "Slow means taking a long time; not fast. Example: A turtle is a slow animal."),
    ("hot", "Hot means having a high temperature. Example: The sun is very hot."),
    ("cold", "Cold means having a low temperature. Example: Ice is cold."),
    ("good", "Good means having positive qualities; beneficial or pleasing."),
    ("bad", "Bad means having negative qualities; not good or desirable."),
    ("beautiful", "Beautiful means very pleasing to the senses; attractive."),
    ("ugly", "Ugly means unpleasant to look at; not attractive."),
    ("strong", "Strong means having great physical power or force."),
    ("weak", "Weak means lacking strength or power."),
    ("old", "Old means having existed for a long time; not new."),
    ("new", "New means recently made, discovered, or created."),
    ("easy", "Easy means not difficult; done without effort."),
    ("hard", "Hard means needing much effort; difficult. Also means not soft."),
    ("clean", "Clean means free from dirt or impurities."),
    ("dirty", "Dirty means covered in dirt or not clean."),
    ("kind", "Kind means being friendly, generous, and considerate to others."),
    ("mean", "Mean means unkind or cruel to others."),
    ("brave", "Brave means ready to face danger without fear; courageous."),
    ("scared", "Scared means feeling afraid or frightened."),
    ("smart", "Smart means having a quick intelligence; clever."),
    ("stupid", "Stupid means lacking intelligence or common sense."),
    ("hungry", "Hungry means feeling the need or desire for food."),
    ("thirsty", "Thirsty means feeling the need or desire for drink."),
    ("tired", "Tired means feeling a need for rest or sleep."),
    ("sick", "Sick means affected by illness; not well."),
    ("healthy", "Healthy means being in good physical or mental condition."),
    ("rich", "Rich means having a great deal of money or assets."),
    ("poor", "Poor means lacking money or resources; not wealthy."),
    ("alive", "Alive means living; not dead."),
    ("dead", "Dead means no longer alive."),
    ("true", "True means in accordance with fact or reality; correct."),
    ("false", "False means not true; incorrect."),
    ("friend", "A friend is a person you know well and who you like and trust."),
    ("enemy", "An enemy is a person who is hostile or opposed to you."),
    ("family", "Family refers to a group of people related by blood, marriage, or adoption."),
    ("home", "Home is the place where someone lives; a place of comfort."),
    ("food", "Food is any substance consumed to provide nutrition for the body."),
    ("water", "Water is a clear liquid essential for all life on Earth."),
    ("air", "Air is the mixture of gases that surrounds Earth and is breathed by living things."),
    ("fire", "Fire is the rapid chemical reaction between oxygen and a fuel that produces heat and light."),
    ("earth", "Earth refers to the ground or soil, or the planet we live on."),
    ("sun", "The sun is the star at the center of our solar system that gives us light and warmth."),
    ("moon", "The moon is Earth's natural satellite that orbits around the Earth."),
    ("star", "A star is a giant ball of hot gas that produces light and heat through nuclear fusion."),
    ("sky", "The sky is the region of the atmosphere seen from Earth's surface."),
    ("ocean", "The ocean is the vast body of salt water that covers most of Earth's surface."),
    ("mountain", "A mountain is a large landform that rises high above the surrounding area."),
    ("river", "A river is a large, natural stream of water flowing toward an ocean, lake, or sea."),
    ("tree", "A tree is a tall plant with a wooden trunk, branches, and leaves."),
    ("flower", "A flower is the seed-bearing part of a plant, often colorful and fragrant."),
    ("animal", "An animal is any living creature that is not a plant, fungus, or bacterium."),
    ("human", "A human is a member of the species Homo sapiens; a person."),
    ("language", "Language is a system of communication using words, sounds, or symbols."),
    ("knowledge", "Knowledge is information, understanding, or skill gained through experience or education."),
    ("wisdom", "Wisdom is the ability to make good decisions based on knowledge and experience."),
    ("time", "Time is the ongoing sequence of events, measured in seconds, minutes, hours, days, and years."),
    ("money", "Money is a medium of exchange used to buy goods and services."),
    ("freedom", "Freedom is the power or right to act, speak, or think without external restraint."),
    ("peace", "Peace is freedom from disturbance; quiet and tranquility."),
    ("war", "War is a state of armed conflict between nations or groups."),
    ("science", "Science is the systematic study of the physical world through observation and experimentation."),
    ("art", "Art is the expression of human creativity through painting, sculpture, music, and other forms."),
    ("music", "Music is the art of combining sounds to create something beautiful or expressive."),
    ("book", "A book is a written or printed work consisting of pages bound together."),
    ("school", "A school is a place where students learn from teachers."),
    ("work", "Work means to do a task or job; or a place where someone is employed."),
    ("play", "Play means to engage in activity for enjoyment; not for serious purposes."),
    ("sleep", "Sleep is a natural state of rest during which the body and mind recover."),
    ("dream", "A dream is a series of images and emotions experienced during sleep."),
    ("think", "To think means to use the mind to form ideas and opinions."),
    ("speak", "To speak means to say words; to communicate verbally."),
    ("listen", "To listen means to pay attention to sounds or what someone is saying."),
    ("read", "To read means to look at and understand written words."),
    ("write", "To write means to put words on paper or a screen."),
    ("learn", "To learn means to gain knowledge or skill through study or experience."),
    ("teach", "To teach means to help others gain knowledge or skills."),
    ("help", "To help means to make something easier for someone; to assist."),
    ("share", "To share means to divide and give a portion to others."),
    ("give", "To give means to present something to someone without expecting return."),
    ("take", "To take means to pick up or receive something."),
    ("run", "To run means to move quickly on foot."),
    ("walk", "To walk means to move at a regular pace on foot."),
    ("eat", "To eat means to consume food by chewing and swallowing."),
    ("drink", "To drink means to take liquid into the body through the mouth."),
    ("see", "To see means to perceive with the eyes."),
    ("hear", "To hear means to perceive sounds with the ears."),
    ("touch", "To touch means to make physical contact with something."),
    ("smell", "To smell means to perceive an odor with the nose."),
    ("taste", "To taste means to perceive flavor with the tongue."),
]

for word, defn in definitions:
    prompts = [
        f"what is the meaning of {word}",
        f"what does {word} mean",
        f"define {word}",
        f"explain the word {word}",
        f"what is {word}",
    ]
    for prompt in prompts:
        data.append(f"Instruction: {prompt}\nResponse: {defn}\n")

# ─────────────────────────────────────────────
# 3. NUMBERS
# ─────────────────────────────────────────────
number_words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty",
    30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred",
    1000: "one thousand", 1000000: "one million"
}

for num, word in number_words.items():
    data.append(f"Instruction: what is {num} in words\nResponse: {num} in words is {word}.\n")
    data.append(f"Instruction: how do you spell {num}\nResponse: The number {num} is spelled {word}.\n")
    data.append(f"Instruction: write {num} in english\nResponse: {num} written in English is {word}.\n")

# Basic math facts
for a in range(1, 11):
    for b in range(1, 11):
        data.append(f"Instruction: what is {a} plus {b}\nResponse: {a} plus {b} equals {a+b}.\n")
        data.append(f"Instruction: what is {a} + {b}\nResponse: {a} + {b} = {a+b}.\n")
        data.append(f"Instruction: what is {a} times {b}\nResponse: {a} times {b} equals {a*b}.\n")
        data.append(f"Instruction: what is {a} multiplied by {b}\nResponse: {a} multiplied by {b} equals {a*b}.\n")
        if a >= b:
            data.append(f"Instruction: what is {a} minus {b}\nResponse: {a} minus {b} equals {a-b}.\n")
            data.append(f"Instruction: what is {a} - {b}\nResponse: {a} - {b} = {a-b}.\n")
        if b != 0 and a % b == 0:
            data.append(f"Instruction: what is {a} divided by {b}\nResponse: {a} divided by {b} equals {a//b}.\n")

# Number concepts
number_facts = [
    ("what is an even number", "An even number is a number that can be divided by 2 without a remainder. Examples: 2, 4, 6, 8, 10."),
    ("what is an odd number", "An odd number cannot be divided exactly by 2. Examples: 1, 3, 5, 7, 9."),
    ("what is a prime number", "A prime number is a number greater than 1 that has no divisors other than 1 and itself. Examples: 2, 3, 5, 7, 11."),
    ("what is zero", "Zero is the number that represents nothing or no quantity. It is written as 0."),
    ("what is negative", "A negative number is a number less than zero. Example: -1, -5, -100."),
    ("what is positive", "A positive number is a number greater than zero. Example: 1, 5, 100."),
    ("what is infinity", "Infinity is a concept describing something without any limit or end. It is not a real number."),
    ("what is a fraction", "A fraction represents a part of a whole. It is written as one number over another, like 1/2 or 3/4."),
    ("what is a percentage", "A percentage is a number expressed as a fraction of 100. For example, 50% means 50 out of 100, or half."),
    ("what is a decimal", "A decimal is a number that uses a decimal point to represent fractions. Example: 0.5 is the same as 1/2."),
]
for q, a in number_facts:
    for _ in range(4):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 4. COLORS
# ─────────────────────────────────────────────
colors = [
    ("red", "Red is a primary color. It is the color of blood, fire, and ripe tomatoes."),
    ("blue", "Blue is a primary color. It is the color of the sky and ocean."),
    ("yellow", "Yellow is a primary color. It is the color of the sun and bananas."),
    ("green", "Green is a secondary color made from blue and yellow. It is the color of grass and leaves."),
    ("orange", "Orange is a secondary color made from red and yellow. It is the color of oranges and sunsets."),
    ("purple", "Purple is a secondary color made from red and blue. It is associated with royalty."),
    ("white", "White is the color of snow and clouds. It reflects all colors of light."),
    ("black", "Black is the color of the night sky. It absorbs all colors of light."),
    ("brown", "Brown is the color of soil and wood. It is made by mixing red, yellow, and blue."),
    ("pink", "Pink is a light shade of red. It is associated with flowers and sweetness."),
    ("gray", "Gray is a neutral color between black and white."),
    ("gold", "Gold is a bright yellow-orange metallic color associated with wealth and the precious metal gold."),
    ("silver", "Silver is a shiny gray color associated with the precious metal silver."),
    ("beige", "Beige is a very light brown or cream color."),
    ("cyan", "Cyan is a bright blue-green color."),
    ("magenta", "Magenta is a bright pink-purple color."),
]
for color, desc in colors:
    data.append(f"Instruction: what color is the sky\nResponse: The sky is blue during the day.\n")
    data.append(f"Instruction: what color is grass\nResponse: Grass is green.\n")
    data.append(f"Instruction: what color is the sun\nResponse: The sun appears yellow or orange.\n")
    data.append(f"Instruction: what is {color}\nResponse: {desc}\n")
    data.append(f"Instruction: describe the color {color}\nResponse: {desc}\n")
    data.append(f"Instruction: what does {color} look like\nResponse: {desc}\n")

primary_colors = [
    ("what are the primary colors", "The three primary colors are red, blue, and yellow. They cannot be made by mixing other colors."),
    ("how many primary colors are there", "There are three primary colors: red, blue, and yellow."),
    ("what colors make green", "Green is made by mixing blue and yellow together."),
    ("what colors make orange", "Orange is made by mixing red and yellow together."),
    ("what colors make purple", "Purple is made by mixing red and blue together."),
]
for q, a in primary_colors:
    for _ in range(5):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 5. SHAPES
# ─────────────────────────────────────────────
shapes = [
    ("circle", "A circle is a round shape with no corners or edges. Every point on the circle is the same distance from the center."),
    ("square", "A square has 4 equal sides and 4 right angles. It is a special type of rectangle."),
    ("triangle", "A triangle has 3 sides and 3 angles. The angles of a triangle always add up to 180 degrees."),
    ("rectangle", "A rectangle has 4 sides and 4 right angles. Opposite sides are equal in length."),
    ("oval", "An oval is an egg-shaped curve, similar to a stretched circle."),
    ("pentagon", "A pentagon is a shape with 5 sides and 5 angles."),
    ("hexagon", "A hexagon is a shape with 6 sides and 6 angles. Honeycombs are made of hexagons."),
    ("octagon", "An octagon is a shape with 8 sides and 8 angles. Stop signs are octagonal."),
    ("star", "A star shape has 5 or more points radiating from a center. It represents stars in the sky."),
    ("heart", "A heart shape is a symbol of love and affection."),
    ("diamond", "A diamond shape has 4 sides of equal length, like a square rotated 45 degrees."),
    ("sphere", "A sphere is a perfectly round 3D shape, like a ball or globe."),
    ("cube", "A cube is a 3D shape with 6 equal square faces, 8 corners, and 12 edges."),
    ("cylinder", "A cylinder is a 3D shape with two circular ends and a curved side, like a can."),
    ("pyramid", "A pyramid is a 3D shape with a flat base and triangular sides that meet at a point."),
    ("cone", "A cone is a 3D shape with a circular base that tapers to a point, like an ice cream cone."),
]
for shape, desc in shapes:
    data.append(f"Instruction: what is a {shape}\nResponse: {desc}\n")
    data.append(f"Instruction: describe a {shape}\nResponse: {desc}\n")
    data.append(f"Instruction: how many sides does a {shape} have\nResponse: {desc}\n")

# ─────────────────────────────────────────────
# 6. DAYS, MONTHS, SEASONS
# ─────────────────────────────────────────────
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
data.append(f"Instruction: what are the days of the week\nResponse: The days of the week are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.\n")
data.append(f"Instruction: how many days are in a week\nResponse: There are 7 days in a week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.\n")
data.append(f"Instruction: what is the first day of the week\nResponse: Monday is typically considered the first day of the week.\n")
data.append(f"Instruction: what are weekdays\nResponse: Weekdays are the working days: Monday, Tuesday, Wednesday, Thursday, and Friday.\n")
data.append(f"Instruction: what are weekends\nResponse: The weekend consists of Saturday and Sunday.\n")

for i, day in enumerate(days, 1):
    data.append(f"Instruction: what day comes after {day}\nResponse: The day after {day} is {days[i % 7]}.\n")
    data.append(f"Instruction: is {day} a weekday\nResponse: {'Yes, ' + day + ' is a weekday.' if day not in ['Saturday', 'Sunday'] else 'No, ' + day + ' is a weekend day.'}\n")

months = [
    ("January", 31, "1st"), ("February", 28, "2nd"), ("March", 31, "3rd"),
    ("April", 30, "4th"), ("May", 31, "5th"), ("June", 30, "6th"),
    ("July", 31, "7th"), ("August", 31, "8th"), ("September", 30, "9th"),
    ("October", 31, "10th"), ("November", 30, "11th"), ("December", 31, "12th")
]
month_names = [m[0] for m in months]
data.append(f"Instruction: what are the months of the year\nResponse: The 12 months of the year are: January, February, March, April, May, June, July, August, September, October, November, and December.\n")
data.append(f"Instruction: how many months are in a year\nResponse: There are 12 months in a year.\n")

for i, (month, days_in, ordinal) in enumerate(months):
    data.append(f"Instruction: how many days are in {month}\nResponse: {month} has {days_in} days.\n")
    data.append(f"Instruction: what is the {ordinal} month\nResponse: The {ordinal} month of the year is {month}.\n")
    next_month = months[(i + 1) % 12][0]
    data.append(f"Instruction: what month comes after {month}\nResponse: The month after {month} is {next_month}.\n")

seasons = [
    ("spring", "Spring is the season after winter, when flowers bloom and temperatures warm up."),
    ("summer", "Summer is the warmest season of the year, with long days and hot temperatures."),
    ("autumn", "Autumn, also called fall, is the season when leaves change color and fall from trees."),
    ("winter", "Winter is the coldest season of the year, with short days and cold temperatures."),
]
data.append(f"Instruction: what are the four seasons\nResponse: The four seasons are spring, summer, autumn (fall), and winter.\n")
for season, desc in seasons:
    data.append(f"Instruction: what is {season}\nResponse: {desc}\n")
    data.append(f"Instruction: describe {season}\nResponse: {desc}\n")

# ─────────────────────────────────────────────
# 7. ANIMALS
# ─────────────────────────────────────────────
animals = [
    ("dog", "A dog is a domesticated mammal and a common pet. Dogs are known for their loyalty and are called man's best friend."),
    ("cat", "A cat is a small domesticated carnivorous mammal kept as a pet. Cats are known for being independent and graceful."),
    ("bird", "A bird is an animal with feathers, wings, and a beak. Most birds can fly."),
    ("fish", "A fish is an aquatic animal with gills that allow it to breathe underwater."),
    ("horse", "A horse is a large, four-legged animal used for riding and work. They are fast and strong."),
    ("cow", "A cow is a large farm animal that provides milk and meat."),
    ("elephant", "An elephant is the largest land animal on Earth. It has a long trunk and large ears."),
    ("lion", "A lion is a large wild cat known as the 'king of the jungle.' It has a mane and a loud roar."),
    ("tiger", "A tiger is the largest wild cat with distinctive orange fur and black stripes."),
    ("bear", "A bear is a large, strong omnivore. Bears can be found in forests and mountains."),
    ("wolf", "A wolf is a wild carnivore related to dogs. Wolves live in packs and howl."),
    ("rabbit", "A rabbit is a small, fluffy mammal with long ears. Rabbits hop and eat vegetables."),
    ("snake", "A snake is a legless reptile that moves by slithering. Some snakes are venomous."),
    ("frog", "A frog is an amphibian that can live in water and on land. Frogs jump and croak."),
    ("monkey", "A monkey is a primate with a tail. Monkeys live in tropical forests and are very intelligent."),
    ("penguin", "A penguin is a bird that cannot fly but is an excellent swimmer. They live in cold climates."),
    ("whale", "A whale is the largest animal on Earth. Whales live in the ocean and breathe air."),
    ("shark", "A shark is a large predatory fish known for its sharp teeth and fins."),
    ("eagle", "An eagle is a large bird of prey with sharp talons and excellent eyesight."),
    ("butterfly", "A butterfly is an insect with large, colorful wings. It starts life as a caterpillar."),
    ("bee", "A bee is an insect that makes honey and pollinates flowers. Bees live in colonies."),
    ("ant", "An ant is a tiny insect known for its strength and teamwork. Ants live in colonies."),
    ("spider", "A spider is an arachnid with 8 legs that spins webs to catch prey."),
    ("crocodile", "A crocodile is a large reptile that lives in rivers and swamps. They have powerful jaws."),
    ("giraffe", "A giraffe is the tallest animal on Earth, with a very long neck used to eat leaves from tall trees."),
    ("zebra", "A zebra is a horse-like animal with black and white stripes. Zebras live in Africa."),
    ("deer", "A deer is a gentle grazing animal with slender legs. Male deer have antlers."),
    ("duck", "A duck is a water bird that quacks and can swim. Ducks are common farm animals."),
    ("chicken", "A chicken is a domestic bird raised for eggs and meat."),
    ("pig", "A pig is an intelligent farm animal. Pigs are raised for meat called pork."),
]
for animal, desc in animals:
    data.append(f"Instruction: what is a {animal}\nResponse: {desc}\n")
    data.append(f"Instruction: tell me about {animal}s\nResponse: {desc}\n")
    data.append(f"Instruction: describe a {animal}\nResponse: {desc}\n")

# ─────────────────────────────────────────────
# 8. BODY PARTS
# ─────────────────────────────────────────────
body_parts = [
    ("head", "The head is the top part of the body. It contains the brain, eyes, ears, nose, and mouth."),
    ("brain", "The brain is the organ inside the head that controls all body functions and thoughts."),
    ("eye", "The eye is the organ used for seeing. Humans have two eyes."),
    ("ear", "The ear is the organ used for hearing. Humans have two ears."),
    ("nose", "The nose is used for smelling and breathing."),
    ("mouth", "The mouth is used for eating, drinking, and speaking."),
    ("tongue", "The tongue is a muscle in the mouth used for tasting, eating, and speaking."),
    ("teeth", "Teeth are hard structures in the mouth used for biting and chewing food."),
    ("neck", "The neck connects the head to the body."),
    ("shoulder", "The shoulder is the joint that connects the arm to the body."),
    ("arm", "The arm is the limb extending from the shoulder. It is used for reaching and holding."),
    ("hand", "The hand is at the end of the arm and has five fingers. It is used for gripping and writing."),
    ("finger", "Fingers are the five separate digits on each hand. They are used for grabbing and feeling."),
    ("leg", "The leg is the limb used for walking and running."),
    ("foot", "The foot is at the bottom of the leg. It has five toes and is used for standing and walking."),
    ("heart", "The heart is an organ that pumps blood through the body."),
    ("lungs", "The lungs are organs used for breathing. They take in oxygen and release carbon dioxide."),
    ("stomach", "The stomach is an organ that digests food."),
    ("skin", "Skin is the outer covering of the body that protects it."),
    ("bone", "Bones form the skeleton, which supports the body. The human body has 206 bones."),
]
for part, desc in body_parts:
    data.append(f"Instruction: what is the {part}\nResponse: {desc}\n")
    data.append(f"Instruction: what does the {part} do\nResponse: {desc}\n")

# ─────────────────────────────────────────────
# 9. BASIC GEOGRAPHY & WORLD FACTS
# ─────────────────────────────────────────────
geography = [
    ("what is the largest country in the world", "Russia is the largest country in the world by land area."),
    ("what is the smallest country in the world", "Vatican City is the smallest country in the world, located in Rome, Italy."),
    ("what is the largest continent", "Asia is the largest continent in the world by both area and population."),
    ("how many continents are there", "There are 7 continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America."),
    ("what are the continents", "The seven continents are Africa, Antarctica, Asia, Australia, Europe, North America, and South America."),
    ("what is the capital of france", "The capital of France is Paris."),
    ("what is the capital of the united states", "The capital of the United States is Washington, D.C."),
    ("what is the capital of india", "The capital of India is New Delhi."),
    ("what is the capital of china", "The capital of China is Beijing."),
    ("what is the capital of japan", "The capital of Japan is Tokyo."),
    ("what is the capital of england", "The capital of England is London."),
    ("what is the capital of germany", "The capital of Germany is Berlin."),
    ("what is the capital of australia", "The capital of Australia is Canberra."),
    ("what is the capital of brazil", "The capital of Brazil is Brasília."),
    ("what is the capital of canada", "The capital of Canada is Ottawa."),
    ("what is the largest ocean", "The Pacific Ocean is the largest and deepest ocean on Earth."),
    ("how many oceans are there", "There are five oceans: the Pacific, Atlantic, Indian, Arctic, and Southern Ocean."),
    ("what is the highest mountain", "Mount Everest is the highest mountain in the world, located in the Himalayas between Nepal and Tibet."),
    ("what is the longest river", "The Nile River in Africa is often considered the longest river in the world."),
    ("what is the largest desert", "The Sahara Desert in North Africa is the largest hot desert in the world."),
    ("what planet do we live on", "We live on planet Earth."),
    ("how many planets are in the solar system", "There are 8 planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune."),
    ("what is the closest planet to the sun", "Mercury is the closest planet to the Sun."),
    ("what is the largest planet", "Jupiter is the largest planet in our solar system."),
    ("what is the sun made of", "The sun is made mostly of hydrogen and helium. It generates energy through nuclear fusion."),
    ("how far is the earth from the sun", "The Earth is about 93 million miles (150 million kilometers) from the Sun."),
    ("what is gravity", "Gravity is the force that attracts objects toward each other. It is what keeps us on the ground and planets in orbit."),
    ("what is the speed of light", "The speed of light is approximately 299,792 kilometers per second (about 186,000 miles per second)."),
]
for q, a in geography:
    for _ in range(4):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 10. SCIENCE BASICS
# ─────────────────────────────────────────────
science = [
    ("what is a plant", "A plant is a living organism that grows in soil, makes its own food through photosynthesis, and is usually green."),
    ("what is photosynthesis", "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to make food and release oxygen."),
    ("what is an atom", "An atom is the smallest unit of matter. Everything is made up of atoms."),
    ("what is a molecule", "A molecule is a group of two or more atoms bonded together."),
    ("what is energy", "Energy is the ability to do work. It comes in many forms like heat, light, and electricity."),
    ("what is electricity", "Electricity is a form of energy caused by the movement of electrons. It powers our homes and devices."),
    ("what is heat", "Heat is a form of energy transferred from hotter objects to cooler ones."),
    ("what is light", "Light is a form of energy that allows us to see. It travels in waves at very high speed."),
    ("what is sound", "Sound is a form of energy created by vibrations that travel through air, water, or solids."),
    ("what is water made of", "Water is made of hydrogen and oxygen. Its chemical formula is H2O."),
    ("what is air made of", "Air is mainly made of nitrogen (78%) and oxygen (21%), with small amounts of other gases."),
    ("what is the water cycle", "The water cycle is the continuous movement of water on Earth: evaporation, condensation, and precipitation."),
    ("what is an ecosystem", "An ecosystem is a community of living organisms interacting with each other and their environment."),
    ("what is evolution", "Evolution is the process by which living things change over generations through natural selection."),
    ("what is a cell", "A cell is the smallest unit of life. All living things are made of cells."),
    ("what is DNA", "DNA is a molecule that carries the genetic information of all living organisms. It determines traits."),
    ("what is a virus", "A virus is a tiny infectious agent that can only reproduce inside the cells of a living host."),
    ("what is a bacteria", "Bacteria are single-celled microorganisms that can be found everywhere on Earth. Some cause disease, others are helpful."),
    ("what causes rain", "Rain occurs when water vapor in clouds condenses into water droplets that become heavy and fall."),
    ("what causes thunder", "Thunder is the sound produced by lightning. The lightning superheats air, causing a rapid expansion that creates sound."),
    ("why is the sky blue", "The sky appears blue because sunlight scatters in the atmosphere, and shorter blue wavelengths scatter more than others."),
    ("what is a black hole", "A black hole is a region in space where gravity is so strong that nothing, not even light, can escape from it."),
    ("what is the big bang", "The Big Bang is the theory that the universe began from an extremely hot and dense point and has been expanding ever since."),
]
for q, a in science:
    for _ in range(4):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 11. BASIC GRAMMAR
# ─────────────────────────────────────────────
grammar = [
    ("what is a noun", "A noun is a word that names a person, place, thing, or idea. Examples: dog, city, happiness."),
    ("what is a verb", "A verb is a word that describes an action or state of being. Examples: run, eat, is, think."),
    ("what is an adjective", "An adjective is a word that describes a noun. Examples: tall, blue, happy, large."),
    ("what is an adverb", "An adverb is a word that modifies a verb, adjective, or other adverb. Examples: quickly, very, well."),
    ("what is a pronoun", "A pronoun replaces a noun. Examples: he, she, it, they, we, I, you."),
    ("what is a preposition", "A preposition shows the relationship between a noun and other words. Examples: in, on, at, by, with."),
    ("what is a sentence", "A sentence is a group of words that expresses a complete thought. It has a subject and a verb."),
    ("what is a question", "A question is a sentence that asks for information and ends with a question mark (?)."),
    ("what is a statement", "A statement is a sentence that provides information and ends with a period (.)."),
    ("what is punctuation", "Punctuation marks are symbols used in writing to separate sentences and clarify meaning. Examples: period, comma, question mark."),
    ("what is a vowel", "A vowel is a speech sound produced with an open vocal tract. The vowels in English are: a, e, i, o, u."),
    ("what is a consonant", "A consonant is a letter that is not a vowel. Examples: b, c, d, f, g, h, j, k, l, m, n."),
    ("what is the alphabet", "The alphabet is the set of letters used to write a language. The English alphabet has 26 letters."),
    ("how many letters are in the alphabet", "The English alphabet has 26 letters, from A to Z."),
    ("what is a paragraph", "A paragraph is a group of related sentences that discuss a single topic."),
    ("what is a synonym", "A synonym is a word that has a similar meaning to another word. For example, happy and joyful are synonyms."),
    ("what is an antonym", "An antonym is a word that has the opposite meaning to another word. For example, hot and cold are antonyms."),
    ("what is singular and plural", "Singular means one of something. Plural means more than one. Example: cat (singular), cats (plural)."),
    ("what is past tense", "Past tense describes actions that already happened. Example: I walked to school yesterday."),
    ("what is present tense", "Present tense describes actions happening now. Example: I walk to school."),
    ("what is future tense", "Future tense describes actions that will happen. Example: I will walk to school tomorrow."),
]
for q, a in grammar:
    for _ in range(4):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 12. COMMON SENSE Q&A
# ─────────────────────────────────────────────
common_sense = [
    ("what do you use to write", "You use a pen or pencil to write on paper."),
    ("what do you use to cut paper", "You use scissors to cut paper."),
    ("what do you use to drink water", "You use a glass or cup to drink water."),
    ("what do you eat breakfast with", "You eat breakfast with a spoon, fork, or chopsticks, depending on the food."),
    ("why do we sleep", "We sleep to allow our bodies and minds to rest and recover. Sleep is essential for health and memory."),
    ("why do we eat food", "We eat food to provide our bodies with energy, nutrients, and building materials needed to function and grow."),
    ("why do we drink water", "We drink water because water is essential for all body functions. Our bodies are about 60% water."),
    ("why do we wear clothes", "We wear clothes to protect our bodies from cold, heat, and injury, and also for cultural and social reasons."),
    ("what happens if you don't sleep", "Without sleep, your brain and body cannot function properly. You become tired, lose focus, and your health suffers."),
    ("what is the difference between a fruit and a vegetable", "A fruit grows from the flower of a plant and contains seeds. A vegetable is any other edible part of the plant."),
    ("is a tomato a fruit or vegetable", "Botanically, a tomato is a fruit because it contains seeds. But in cooking, it is often treated as a vegetable."),
    ("why do leaves change color in autumn", "Leaves change color in autumn because chlorophyll, the green pigment, breaks down as days get shorter and colder."),
    ("why is the ocean salty", "The ocean is salty because rivers carry dissolved minerals, including salt, from rocks into the ocean over millions of years."),
    ("can fish breathe out of water", "No, most fish cannot breathe out of water. They use gills to extract oxygen from water."),
    ("do plants need sunlight", "Yes, plants need sunlight to perform photosynthesis and make their own food."),
    ("what is heavier, a kilogram of gold or a kilogram of feathers", "They both weigh exactly the same — one kilogram."),
    ("can you see air", "No, air is invisible. However, you can feel it and see its effects, like wind moving leaves."),
    ("why is fire hot", "Fire is hot because it is a chemical reaction that releases energy in the form of heat and light."),
    ("what makes ice melt", "Ice melts when its temperature rises above 0 degrees Celsius (32 degrees Fahrenheit)."),
    ("why does ice float on water", "Ice floats because it is less dense than liquid water. Water expands and becomes lighter when it freezes."),
]
for q, a in common_sense:
    for _ in range(5):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ─────────────────────────────────────────────
# 13. OPPOSITES
# ─────────────────────────────────────────────
opposites = [
    ("hot", "cold"), ("big", "small"), ("fast", "slow"), ("happy", "sad"),
    ("good", "bad"), ("old", "new"), ("light", "dark"), ("strong", "weak"),
    ("tall", "short"), ("fat", "thin"), ("hard", "soft"), ("loud", "quiet"),
    ("clean", "dirty"), ("rich", "poor"), ("true", "false"), ("open", "closed"),
    ("alive", "dead"), ("love", "hate"), ("start", "end"), ("day", "night"),
    ("up", "down"), ("left", "right"), ("north", "south"), ("east", "west"),
    ("push", "pull"), ("buy", "sell"), ("give", "take"), ("question", "answer"),
]
for w1, w2 in opposites:
    data.append(f"Instruction: what is the opposite of {w1}\nResponse: The opposite of {w1} is {w2}.\n")
    data.append(f"Instruction: what is the antonym of {w1}\nResponse: The antonym of {w1} is {w2}.\n")
    data.append(f"Instruction: what is the opposite of {w2}\nResponse: The opposite of {w2} is {w1}.\n")

# ─────────────────────────────────────────────
# SHUFFLE AND WRITE
# ─────────────────────────────────────────────
random.shuffle(data)

output_path = "data/input_basic.txt"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(data))

print(f"Generated {len(data)} training examples.")
print(f"Saved to {output_path}")
print(f"Total characters: {sum(len(d) for d in data):,}")
