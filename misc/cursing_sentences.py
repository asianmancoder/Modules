import random


class Cursing_Improved:

    def __init__(self, word=None):
        self.word = word
        self.words_to_phrases = {
            "shit": ["Ayo I took a giant shit last night and dumped it all over my friend.", "Ew what is that smell? Did you take a shit or something?", "Your code looks like complete shit, man."],
            "hell": ["Why the hell is there dog shit on my lawn? No way in hell am I gonna take this from who ever thought it would be a good idea to leave their dog's excretion on my lawn!", "Go to hell, man. I thought we were supposed to be friends - partners! But you went and took my entire percentage from the payment for our app!", "Bro there's a hell lotta people out there who just wanna scam you and take all your money. Gotta be careful out there. It's hell, man."],
            "fuck": ["Fuck you, fuck you. I hate you.", "Yo, did you see that guy right there get all fucked up by his own dog? I really feel bad for him. Probably gotta call an ambulance and the animal control service.", "Why do they say 'fuck' so much in that movie? I thought it was supposed to be PG - 13! But no, that should be rated R."],
            "bitch": ["Yo, did you see that bitch give birth to its pup? I swear I saw it shit all over the pup right after it came out. I feel bad for the pup, man. Really bad. If my momma did that to me, then my daddy would've called HER a bitch.", "HEY! You BITCH! Why'd you just ram your car into mine like that for no reason, eh? I'm calling the cops on you. You're such a fucking bitch.", "Bro, I just dumped that bitch right on the spot when I saw her in bed with another man. That btich ain't gonna be seein' me for a long time, no sir."],
            "damn": ["Damn, bro. How did you code that all by yourself? It's like, more than 50,000 fucking lines of code long, ain't it?", "Son, look at that monkey right there. Its ass is so damn huge. Now you don't turn out like that, alright, son? You got me? Good.", "GOSH DAMN IT, MAN! I SPENT SO MANY YEARS DEVELOPING THIS COMPANY'S PRODUCTS AND NOW I JUST FOUND OUT THAT MY BUSINESS PARTNER TOOK MY SHARE OF THE PAYMENT? DAMN IT! I WANNA FUCKING KILL HIM RIGHT NOW, MAN? HELP ME DO IT, WILL YA? BE A GOOD FRIEND. PLEASE, I'M GOING THROUGH A REALLY HARD TIME, RIGHT NOW. I'D REALLY APPRECIATE IT."]
        }
        self.default = ["What the fucking hell, man? You just deleted my entire Web API repository on GitHub. I hope you die in a hole of burning shit. We are no longer friends.", "Ayo why is that monkey's ass so fucking huge? I think they need to give that monkey some treatment.", "Damn, son! I never knew you could throw a baseball that fucking far. Let me try, even though I think I'll be complete shit at it."]

    def get_sentence(self):
        if self.word == None:
            return self.__do_default()

        if self.words_to_phrases[self.word.lower()]:
            return random.choice(self.words_to_phrases[self.word.lower()])
        else:
            return False

    def get_words_to_phrases(self):
        return self.words_to_phrases

    def __do_default(self):
        return random.choice(self.default)
