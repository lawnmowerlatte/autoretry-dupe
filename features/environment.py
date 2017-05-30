from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry


def before_feature(scenario, feature):
    for scenario in feature.scenarios:
        if "autoretry" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=3)