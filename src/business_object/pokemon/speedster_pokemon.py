from src.business_object.pokemon import AbstractPokemon


class SpeedSterPokemon(AbstractPokemon):
    def __init__():
        super.__init__()

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the SpeedSter pokemon.

        Returns :
            float : the multiplier
        """

        return 1 + (self.speed_current + self.sp_atk_current) / 200

