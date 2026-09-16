from datetime import timezone
import pytest
from nebula.models import Candidate, Evaluation, EvolutionConfig, Generation

def test_candidate_requires_id() -> None:
    with pytest.raises(ValueError, match="candidate_id"):
        Candidate("", "print('hello')")

def test_evaluation_defaults_to_utc() -> None:
    evaluation = Evaluation("a", 1.0, True, 0.2)
    assert evaluation.measured_at.tzinfo == timezone.utc

def test_config_rejects_invalid_population() -> None:
    with pytest.raises(ValueError, match="population_size"):
        EvolutionConfig(population_size=0)

def test_generation_rejects_negative_number() -> None:
    with pytest.raises(ValueError, match="generation"):
        Generation(-1, ())
