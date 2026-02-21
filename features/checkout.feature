Feature: Checkout Product

  Scenario: User checkout product till payment page

    Given User is on home page
    When User selects a product
    And User adds product to cart
    And User proceeds to checkout
    
    
