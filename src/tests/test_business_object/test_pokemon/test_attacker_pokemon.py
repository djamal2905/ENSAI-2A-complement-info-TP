from src.business_object.pokemon.attacker_pokemon import AttackerPokemon
from src.business_object.statistic import Statistic


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AttackerPokemon(stat_current=Statistic(speed=200, attack=200))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 3


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
