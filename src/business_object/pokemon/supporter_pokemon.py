from src.business_object.pokemon import AbstractPokemon


class SupporterPokemon(AbstractPokemon):
    def __init__():
        super.__init__()

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the attacker pokemon.

        Returns :
            float : the multiplier
        """

        return 1 + (self.sp_atk_current + self.defense_current) / 200

