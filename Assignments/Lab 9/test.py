import pytest

try:
    import glob
    import importlib

    script_path = glob.glob("./lab9.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except Exception:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    word_frequency_in_text = module.word_frequency_in_text
    analyze_quotes = module.analyze_quotes
except Exception:
    raise Exception("Please ensure all required classes have been implemented.")


word_frequency_in_text_link1 = "https://www.gutenberg.org/files/1662/1662-8.txt"
word_frequency_in_text_link2 = "http://data.pr4e.org/romeo-full.txt"
word_frequency_in_text_link3 = "https://www.gutenberg.org/files/1661/1661-0.txt"


@pytest.mark.parametrize(
    "url, word_to_search, ans",
    [
        (word_frequency_in_text_link1, "Diplomatic", 476),
        #(word_frequency_in_text_link2, "Romeo", 4),
        (word_frequency_in_text_link3, "mystery", 20),
    ],
)
def test_word_frequency_in_text(url, word_to_search, ans):
    assert word_frequency_in_text(url, word_to_search) == ans


analyze_quotes_link1 = "http://quotes.toscrape.com/page/1/"
analyze_quotes_link2 = "http://quotes.toscrape.com/page/2/"


@pytest.mark.parametrize(
    "url, ans",
    [
        (
            analyze_quotes_link1,
            {
                "Albert Einstein": [
                    "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
                    "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”",
                    "“Try not to become a man of success. Rather become a man of value.”",
                ],
                "J.K. Rowling": [
                    "“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
                ],
                "Jane Austen": [
                    "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”"
                ],
                "Marilyn Monroe": [
                    "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”"
                ],
                "André Gide": [
                    "“It is better to be hated for what you are than to be loved for what you are not.”"
                ],
                "Thomas A. Edison": [
                    "“I have not failed. I've just found 10,000 ways that won't work.”"
                ],
                "Eleanor Roosevelt": [
                    "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”"
                ],
                "Steve Martin": ["“A day without sunshine is like, you know, night.”"],
            },
        ),
        (
            analyze_quotes_link2,
            {
                "Marilyn Monroe": [
                    "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”"
                ],
                "J.K. Rowling": [
                    "“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”"
                ],
                "Albert Einstein": [
                    "“If you can't explain it to a six year old, you don't understand it yourself.”"
                ],
                "Bob Marley": [
                    "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”"
                ],
                "Dr. Seuss": [
                    "“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”"
                ],
                "Douglas Adams": [
                    "“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”"
                ],
                "Elie Wiesel": [
                    "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”"
                ],
                "Friedrich Nietzsche": [
                    "“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”"
                ],
                "Mark Twain": [
                    "“Good friends, good books, and a sleepy conscience: this is the ideal life.”"
                ],
                "Allen Saunders": [
                    "“Life is what happens to us while we are making other plans.”"
                ],
            },
        ),
    ],
)
def test_analyze_quotes(url, ans):
    assert analyze_quotes(url) == ans
