from nebula import (
    Candidate,
    Evaluation,
    EvolutionConfig,
    EvolutionEngine,
    ExperimentManifest,
    candidate_id,
)


class Fitness:
    def evaluate(self, candidate: Candidate) -> Evaluation:
        return Evaluation(candidate.candidate_id, float(len(candidate.source)), True, 0.0)


class Mutator:
    def mutate(self, candidate: Candidate, rng: object) -> Candidate:
        del rng
        source = candidate.source + "!"
        return Candidate(candidate_id(source, candidate.candidate_id), source, candidate.candidate_id)


def test_manifest_is_json_serializable() -> None:
    initial = Candidate(candidate_id("x"), "x")
    config = EvolutionConfig(population_size=2, generations=2, seed=7)
    result = EvolutionEngine(config, Mutator(), Fitness()).run(initial)
    manifest = ExperimentManifest(objective="improve x", config=config, result=result)

    payload = manifest.to_dict()
    assert payload["schema_version"] == 1
    assert payload["objective"] == "improve x"
    assert payload["config"]["seed"] == 7
    assert payload["best_candidate_id"] == result.best.candidate_id if result.best else False
    assert '"candidate_ids"' in manifest.to_json()


def test_manifest_rejects_empty_objective() -> None:
    initial = Candidate(candidate_id("x"), "x")
    config = EvolutionConfig(generations=1)
    result = EvolutionEngine(config, Mutator(), Fitness()).run(initial)
    try:
        ExperimentManifest(objective=" ", config=config, result=result)
    except ValueError as exc:
        assert str(exc) == "objective must not be empty"
    else:
        raise AssertionError("expected ValueError")
