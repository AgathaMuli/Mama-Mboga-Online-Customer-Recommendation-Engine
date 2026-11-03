"""Recommendation engine package exports."""

from recommender import RecommendationEngine, jaccard, read_purchases


def main() -> None:
    """Run the recommendation workflow exposed by the package entry point."""
    from main import main as run_project_main

    run_project_main()


__all__ = ["RecommendationEngine", "jaccard", "read_purchases", "main"]
