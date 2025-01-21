import random
from Timer import Timer

class VoiceNode:
    def __init__(self, can_interface, voice_question, voice_answer, voice_hint_label, voice_hint_button, log):
        self.can_interface = can_interface
        self.voice_question = voice_question
        self.voice_answer = voice_answer
        self.voice_hint_label = voice_hint_label
        self.voice_hint_button = voice_hint_button
        self.log = log

        self.voice_questions = [
            "Je suis là où le temps est souvent glacial, et où les ours blancs trouvent leur royaume. Mon nom est gravé sur toutes les cartes, mais je ne bouge jamais. Qui suis-je ?",
            "Descendez toujours, et vous me trouverez. Là où les manchots chantent, et où les vents hurlent sur des glaces éternelles. Qui suis-je ?",
            "Loin dans ma direction, on trouve les premiers rayons du soleil. Sur la boussole, je suis fidèle à ma place, mais invisible à l’œil nu. Qui suis-je ?",
            "Je commence la nuit et je termine le matin. Qui suis-je ?",
            "On ne peut la voir, on ne peut la sentir, on ne peut l’entendre, on ne peut la respirer. Elle s’étend derrière les étoiles et sous les collines, elle remplit les trous vides. Elle revient d’abord et suit après. Elle termine la vie, tue le rire. Réponse: Obscurité",
            "Cette chose toutes choses dévore: Oiseaux, bêtes, arbres, fleurs; elle ronge le fer, mord l’acier; réduit les dures pierres en poudre; met à mort les rois, détruit les villes; et rabat les hautes montagnes. Réponse: Temps",
            "Une boîte sans charnière, sans clé, sans couvercle: Pourtant à l’intérieur est caché un trésor doré. Réponse: Œuf",
            "Je suis toujours devant toi, mais tu ne peux jamais m’atteindre. Qui suis-je ?",
            "Je suis léger comme une plume, mais même l’homme le plus fort ne peut pas me tenir longtemps. Qui suis-je ?",
            "Vivant sans souffle, froid comme la mort, jamais assoiffé, toujours buvant, en cotte de maille, jamais cliquetant. Réponse: Poisson"
        ]

        self.voice_answers = [
            "Nord",
            "Sud",
            "Est",
            "Rêve",
            "Obscurité",
            "Temps",
            "Œuf",
            "Futur",
            "Souffle",
            "Poisson"
        ]

        self.voice_hint = []

        self.timer = Timer(60, "Timer module Voix", self.log)

    def enable_hint(self):
        self.voice_hint_label.grid()

    def play(self):
        question_index = random.randint(0, len(self.voice_questions) - 1)
        self.voice_question.config(text=self.voice_questions[question_index])
        self.voice_answer.config(text="")

        answer = False
        while not answer:
            if self.timer.get_time() == 0:
                self.voice_hint_button.config(command=self.enable_hint)
                self.voice_hint_button.grid()

            msg = self.can_interface.read_can_data()
            if msg and msg['arbitration_id'] == '0x020':
                answer_index = int(msg['data'], 16) - 1
                if answer_index == question_index:
                    self.voice_answer.config(text=self.voice_answers[answer_index], fg="green")
                    answer = True
                else:
                    self.voice_answer.config(text=self.voice_answers[answer_index], fg="red")
