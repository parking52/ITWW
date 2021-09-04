from card import card, cost, production, discard_reward


class Cardbank:

    def __init__(self):
        self.cards = {
            "military_base": self.military_base(),
            "recycling_plant": self.recycling_plant(),
            "financial_center": self.financial_center(),
            "industrial_complex": self.industrial_complex(),
            "offshore_oil_rig": self.offshore_oil_rig(),
            "research_center": self.research_center(),
            "nuclear_plant": self.nuclear_plant(),
            "zeppelin": self.zeppelin(),
            "icebreaker": self.icebreaker(),
            "tank_division": self.tank_division(),
            "mega_drill": self.mega_drill(),
            "submarine": self.submarine(),
            "airborne_laboratory": self.airborne_laboratory(),

        }

    def card_from_name(self, name):
        return self.cards[name]

    def military_base(self):
        return card("military_base", cost(3, 1, 0, 0, 0), discard_reward(1, 0, 0, 0, 0), production(1, 0, 1, 0, 0), "grey")

    def recycling_plant(self):
        return card("recycling_plant", cost(2, 0, 0, 0, 0), discard_reward(1, 0, 0, 0, 0), production(2, 0, 0, 0, 0), "grey")

    def financial_center(self):
        return card("financial_center", cost(4, 1, 0, 0, 0), discard_reward(0, 0, 1, 0, 0), production(0, 0, 2, 0, 0), "grey")

    def industrial_complex(self):
        return card("industrial_complex", cost(3, 1, 0, 0, 0), discard_reward(0, 0, 1, 0, 0), production(1, 0, 1, 0, 0), "grey")

    def offshore_oil_rig(self):
        return card("offshore_oil_rig", cost(3, 0, 0, 0, 1), discard_reward(0, 1, 0, 0, 0), production(0, 1, 1, 0, 0), "grey")

    def wind_turbines(self):
        return card("wind_turbines", cost(2, 0, 0, 0, 0), discard_reward(0, 1, 0, 0, 0), production(0, 1, 0, 0, 0), "grey")

    def research_center(self):
        return card("research_center", cost(3, 1, 0, 0, 0), discard_reward(0, 0, 1, 0, 0), production(0, 0, 2, 0, 0), "grey")

    def nuclear_plant(self):
        return card("nuclear_plant", cost(4, 0, 1, 0, 0), discard_reward(0, 1, 0, 0, 0), production(0, 3, 0, 0, 0), "grey")

    def zeppelin(self):
        return card("zeppelin", cost(0, 2, 0, 0, 0), discard_reward(0, 0, 0, 0, 1), production(0, 0, 0, 0, 1), "black")

    def icebreaker(self):
        return card("icebreaker", cost(0, 3, 1, 0, 0), discard_reward(0, 0, 0, 0, 1), production(0, 0, 0, 0, 2), "black")

    def tank_division(self):
        return card("tank_division", cost(1, 2, 0, 0, 0), discard_reward(1, 0, 0, 0, 0), production(0, 0, 0, 0, 1), "black")

    def mega_drill(self):
        return card("mega_drill", cost(1, 2, 0, 0, 0), discard_reward(1, 0, 0, 0, 0), production(1, 0, 0, 0, 1), "black")

    def submarine(self):
        return card("submarine", cost(2, 3, 0, 0, 0), discard_reward(1, 0, 0, 0, 0), production(0, 0, 0, 0, 2), "black")

    def airborne_laboratory(self):
        return card("airborne_laboratory", cost(0, 3, 0, 0, 0), discard_reward(0, 0, 1, 0, 0), production(0, 0, 1, 0, 1), "black")