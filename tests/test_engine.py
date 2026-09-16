from nebula import Candidate, Evaluation, EvolutionConfig, EvolutionEngine, candidate_id

class FixedFitness:
    def evaluate(self, candidate: Candidate) -> Evaluation:
        return Evaluation(candidate.candidate_id, float(len(candidate.source)), True, 0.0)

class AppendMutator:
    def mutate(self, candidate: Candidate, rng: object) -> Candidate:
        del rng
        source = candidate.source + "!"
        return Candidate(candidate_id(source, candidate.candidate_id), source, candidate.candidate_id)

def test_candidate_id_is_stable() -> None:
    assert candidate_id("x", "parent") == candidate_id("x", "parent")

def test_engine_records_generations_and_best() -> None:
    result = EvolutionEngine(
        EvolutionConfig(population_size=3, generations=3),
        AppendMutator(),
        FixedFitness(),
    ).run(Candidate(candidate_id("x"), "x"))
    assert len(result.generations) == 3
    assert result.best is not None
    assert result.best.source == "x!!"

def test_engine_is_reproducible() -> None:
    config = EvolutionConfig(population_size=2, generations=4, seed=42)
    initial = Candidate(candidate_id("x"), "x")
    assert EvolutionEngine(config, AppendMutator(), FixedFitness()).run(initial) == EvolutionEngine(config, AppendMutator(), FixedFitness()).run(initial)
