# 🛒 OpenCart BDD Framework

A comprehensive **Behavior-Driven Development (BDD)** test automation framework for the OpenCart e-commerce platform. This framework leverages **Selenium WebDriver, Cucumber, TestNG, and Java** to provide automated functional testing with maintainability, scalability, and CI/CD integration.

---

## 📋 Table of Contents

* Overview
* Project Structure
* Prerequisites
* Installation
* Configuration
* Running Tests
* Writing Test Scenarios
* Reporting
* Best Practices
* Troubleshooting
* Contributing
* License
* Contact & Support

---

## 📖 Overview

This framework follows:

* ✅ Page Object Model (POM)
* ✅ BDD with Cucumber (Gherkin syntax)
* ✅ Maven build management
* ✅ TestNG execution support
* ✅ Parallel execution capability
* ✅ Screenshot capture on failure
* ✅ Logging with Log4j2
* ✅ Extent & Cucumber HTML Reporting

Designed for real-world enterprise automation projects.

---

## 🏗️ Project Structure

```
opencart-bdd-framework/
│
├── src/
│   ├── main/java/
│   │   ├── pages/
│   │   │   ├── LoginPage.java
│   │   │   ├── ProductPage.java
│   │   │   ├── CartPage.java
│   │   │   └── CheckoutPage.java
│   │   │
│   │   ├── utils/
│   │   │   ├── DriverFactory.java
│   │   │   ├── WaitUtils.java
│   │   │   ├── ScreenshotUtils.java
│   │   │   └── ConfigReader.java
│   │   │
│   │   └── constants/
│   │       └── Constants.java
│   │
│   └── test/java/
│       ├── stepdefinitions/
│       │   ├── LoginSteps.java
│       │   ├── ProductSteps.java
│       │   ├── CartSteps.java
│       │   └── CheckoutSteps.java
│       │
│       ├── runners/
│       │   ├── TestRunner.java
│       │   └── ParallelRunner.java
│       │
│       └── hooks/
│           └── Hooks.java
│
├── src/test/resources/
│   ├── features/
│   │   ├── login.feature
│   │   ├── shopping.feature
│   │   └── checkout.feature
│   │
│   ├── config.properties
│   └── log4j2.xml
│
├── drivers/
├── logs/
├── screenshots/
├── reports/
├── pom.xml
├── testng.xml
├── README.md
└── .gitignore
```

---

## 🔧 Prerequisites

* Java 8+
* Maven 3.6+
* Git
* Chrome/Firefox Browser
* ChromeDriver / GeckoDriver (or WebDriverManager)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sandepakulareddy/opencart-bdd-framework.git
cd opencart-bdd-framework
```

### 2️⃣ Install Dependencies

```bash
mvn clean install
```

### 3️⃣ WebDriver Setup

Place WebDriver executables inside `drivers/` folder

OR use WebDriverManager dependency in `pom.xml`:

```xml
<dependency>
    <groupId>io.github.bonigarcia</groupId>
    <artifactId>webdrivermanager</artifactId>
    <version>5.6.2</version>
</dependency>
```

---

## ⚙️ Configuration

Update `src/test/resources/config.properties`

```properties
# Application URL
app.url=https://opencart.demo.opencart.com

# Browser Settings
browser=chrome
headless.mode=false
implicit.wait=10
explicit.wait=20

# Screenshot Settings
screenshot.on.failure=true
screenshot.path=screenshots/

# Reporting
report.path=reports/
```

---

## 🚀 Running Tests

### ▶ Run All Tests

```bash
mvn clean test
```

### ▶ Run Specific Feature

```bash
mvn test -Dcucumber.options="src/test/resources/features/login.feature"
```

### ▶ Run with Tag

```bash
mvn test -Dcucumber.options="--tags @smoke"
```

### ▶ Run in Parallel

```bash
mvn test -Dparallel=true -DthreadCount=4
```

### ▶ Run Headless

```bash
mvn test -Dheadless=true
```

---

## ✍️ Writing Test Scenarios

### Example Feature File

```gherkin
Feature: User Login Functionality

  Background:
    Given User navigates to the application

  @smoke @regression
  Scenario: Successful login with valid credentials
    When User enters email "user@example.com"
    And User enters password "password123"
    And User clicks the login button
    Then User should be redirected to dashboard
```

---

### Example Step Definition

```java
public class LoginSteps {

    private WebDriver driver;
    private LoginPage loginPage;

    @Given("User navigates to the application")
    public void navigateToApp() {
        driver = DriverFactory.getDriver();
        loginPage = new LoginPage(driver);
        driver.get(ConfigReader.get("app.url"));
    }
}
```

---

### Example Page Object

```java
public class LoginPage {

    private WebDriver driver;

    @FindBy(id = "email")
    private WebElement emailField;

    @FindBy(id = "password")
    private WebElement passwordField;

    @FindBy(xpath = "//button[@type='submit']")
    private WebElement loginButton;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }
}
```

---

## 📊 Reporting

### Extent Report

Generated at:

```
reports/index.html
```

Includes:

* Execution summary
* Pass/Fail statistics
* Screenshots for failed tests
* Logs with timestamps
* System & browser details

### Cucumber HTML Report

```
target/cucumber-reports/
```

---

## 🎯 Best Practices

* Write business-readable scenarios
* Keep steps reusable
* Avoid hardcoding values
* Use configuration files
* Follow POM design pattern
* Use explicit waits (avoid Thread.sleep)
* Tag tests properly (@smoke, @regression)
* Maintain reports for analysis

---

## 🔍 Troubleshooting

### WebDriver Not Found

* Ensure drivers exist in `drivers/`
* Or use WebDriverManager

### Tests Timeout

* Increase waits in config.properties
* Check application performance

### Screenshot Issues

* Verify screenshot directory exists
* Ensure write permissions

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 📧 Contact & Support

For support:

* Open a GitHub issue
* GitHub Profile: [https://github.com/sandepakulareddy](https://github.com/sandepakulareddy)

---

⭐ If you find this framework useful, consider giving it a star!
