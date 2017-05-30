Feature: Show autoretry creates multiple JSON entries
  In order to have clear and readable results
  As a consumer of Behave who uses autoretry and JSON results
  I want to have clear and unambiguous results

  @autoretry
  Scenario: I have a test that fails three times
    Given I have a step that fails sometimes

  @autoretry
  Scenario: I have a test that fails twice before passing
    Given I have a step that fails sometimes