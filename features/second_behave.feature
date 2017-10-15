Feature: My first behave feature

  @one @test
  Scenario: Add two numbers -second -1
    Given I have two integers a and b
    When I add the numbers
    Then I print the addition result


  @two @test
  Scenario: Add two numbers - second -2
    Given I have two integers a and b
    When I add the numbers
    Then I print the addition result