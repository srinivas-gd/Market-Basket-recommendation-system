# Market Basket Recommendation System

## Project Overview

The Market Basket Recommendation System is a data-driven recommendation application that analyzes customer transaction data to identify relationships between products and generate product recommendations.

The system uses the **Market Basket Optimisation dataset** and applies **Association Rule Mining with the Apriori algorithm** to discover products that are frequently purchased together.

The generated association rules are used to recommend related products based on the products selected by the user. The project combines data analysis, association rule mining, and a web-based interface to demonstrate how transaction data can be used for product recommendation.

## Problem Statement

Retail and e-commerce transaction datasets contain valuable information about customer purchasing behavior. Customers frequently purchase certain products together, but these relationships may not be immediately visible when analyzing individual transactions.

The objective of this project is to identify meaningful product relationships from transaction data and use these relationships to generate relevant product recommendations.

## Objectives

* Analyze customer transaction data.
* Preprocess transaction-level purchasing data.
* Identify frequently purchased product combinations.
* Apply the Apriori algorithm for frequent itemset mining.
* Generate association rules from frequent itemsets.
* Evaluate association rules using support, confidence, and lift.
* Generate product recommendations based on discovered associations.
* Provide recommendations through a web-based application.
* Demonstrate the practical application of Market Basket Analysis in recommendation systems.

## Dataset

The project uses the **Market Basket Optimisation dataset**.

### Dataset Characteristics

The dataset contains customer transaction records where each row represents a transaction and the products purchased during that transaction.

The dataset is used to identify recurring purchasing patterns and relationships between products.

### Dataset File

```text
Market_Basket_Optimisation.csv
```

The transaction data is processed to create the format required for frequent itemset mining and association rule generation.

## Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Data Analysis and Visualization

* Matplotlib
* Seaborn

### Machine Learning / Data Mining

* Apriori Algorithm
* Association Rule Mining

### Web Application

* Flask
* HTML
* CSS
* Python

### Development Environment

* Jupyter Notebook
* Visual Studio Code

## Methodology

The complete project follows the following workflow:

```text
Transaction Dataset
        |
        v
Data Loading
        |
        v
Data Preprocessing
        |
        v
Transaction Transformation
        |
        v
Frequent Itemset Generation
        |
        v
Apriori Algorithm
        |
        v
Association Rule Generation
        |
        v
Support / Confidence / Lift Evaluation
        |
        v
Recommendation Generation
        |
        v
Flask Web Application
        |
        v
User Product Selection
        |
        v
Recommended Products
```

## Market Basket Analysis

Market Basket Analysis is used to discover relationships between products based on customer purchasing behavior.

For example, if a particular product is frequently purchased together with another product, the relationship can be represented as an association rule:

```text
Product A → Product B
```

This relationship can then be used to recommend Product B when Product A is selected.

## Apriori Algorithm

The Apriori algorithm is used to identify frequent itemsets from the transaction dataset.

The process consists of:

1. Preparing transaction data.
2. Identifying frequent individual products.
3. Generating candidate itemsets.
4. Filtering itemsets based on minimum support.
5. Generating association rules.
6. Evaluating the generated rules.
7. Using suitable rules for product recommendations.

## Association Rule Metrics

The generated association rules are evaluated using three primary metrics.

### Support

Support represents how frequently an itemset occurs within the complete transaction dataset.

It helps identify how common a particular product combination is.

### Confidence

Confidence represents the likelihood that the consequent product is purchased when the antecedent product is purchased.

For example:

```text
Bread → Butter
```

A high confidence value indicates that customers who purchase bread frequently also purchase butter.

### Lift

Lift measures the strength of the relationship between the antecedent and consequent compared with their independent occurrence.

A lift value greater than 1 generally indicates a positive association between the products.

## Recommendation Process

The recommendation system uses the association rules generated from the transaction dataset.

The recommendation workflow is:

```text
User Selects Product
        |
        v
Identify Product in Dataset
        |
        v
Search Generated Association Rules
        |
        v
Identify Associated Products
        |
        v
Evaluate Relevant Rules
        |
        v
Generate Recommendations
        |
        v
Display Recommended Products
```

The recommendations are therefore based on **actual purchasing relationships identified from the transaction dataset**.

## Web Application

The project includes a Flask-based web application that provides an interface for interacting with the recommendation system.

### Application Components

```text
app.py
    |
    ├── Flask Application
    |
    ├── Recommendation Logic
    |
    └── Web Routes
          |
          ├── index.html
          ├── login.html
          └── Introduction.html
```

The application allows users to interact with the recommendation system through a web interface rather than directly executing the data mining code.

## Project Files

The current repository contains the following major files:

```text
Market-Basket-recommendation-system/
│
├── README.md
│
├── Market_Basket_Optimisation.csv
│
├── apriory_recomendation_rule.ipynb
│
├── rules.csv
│
├── app.py
│
├── index.html
│
├── login.html
│
├── Introduction.html
│
└── FINAL YEAR PROJECT REPORT recommendation engine.doc
```

### File Description

| File                                                  | Description                                                                                          |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `Market_Basket_Optimisation.csv`                      | Transaction dataset used for Market Basket Analysis                                                  |
| `apriory_recomendation_rule.ipynb`                    | Jupyter Notebook containing data processing, Apriori implementation, and association rule generation |
| `rules.csv`                                           | Generated association rules used by the recommendation system                                        |
| `app.py`                                              | Flask application and recommendation system backend                                                  |
| `index.html`                                          | Main web application interface                                                                       |
| `login.html`                                          | Login interface                                                                                      |
| `Introduction.html`                                   | Project introduction/interface page                                                                  |
| `FINAL YEAR PROJECT REPORT recommendation engine.doc` | Project documentation/report                                                                         |
| `README.md`                                           | Project documentation                                                                                |

## Results

The system successfully processes transaction data and generates association rules using the Apriori algorithm.

The generated rules are stored in:

```text
rules.csv
```

These rules contain product relationships that can be used by the recommendation system to identify related products.

The Flask application uses the generated rules to provide recommendations based on the user's selected product.

## Key Outcomes

The project demonstrates the complete process of building a transaction-based recommendation system:

```text
Raw Transaction Data
        ↓
Data Preprocessing
        ↓
Frequent Itemsets
        ↓
Association Rules
        ↓
Rule Evaluation
        ↓
Recommendation Engine
        ↓
Web Application
```

The system demonstrates how historical customer transactions can be transformed into actionable product recommendations.

## Business Applications

The approach demonstrated in this project can be applied to several real-world scenarios, including:

* E-commerce product recommendations
* Retail analytics
* Cross-selling
* Product bundling
* Promotional campaigns
* Customer purchasing behavior analysis
* Product placement strategies
* Online shopping recommendation systems

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/srinivas-gd/Market-Basket-recommendation-system.git
```

### 2. Navigate to the Project Directory

```bash
cd Market-Basket-recommendation-system
```

### 3. Install Required Libraries

Install the required Python packages used by the project.

```bash
pip install pandas numpy matplotlib seaborn mlxtend flask
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Application

After starting the Flask server, open the local application URL provided by Flask in your web browser.

## Running the Notebook

The complete Market Basket Analysis process can also be explored through:

```text
apriory_recomendation_rule.ipynb
```

The notebook contains the data processing and association rule mining workflow.

Open the notebook using Jupyter:

```bash
jupyter notebook
```

Then open:

```text
apriory_recomendation_rule.ipynb
```

and execute the cells sequentially.

## Limitations

The current recommendation system is primarily based on product associations discovered from historical transaction data.

It does not currently provide advanced user-level personalization based on individual customer profiles or long-term user preferences.

The recommendations depend on the relationships available in the transaction dataset and the association rules generated from it.

## Future Enhancements

The system can be further improved by:

* Adding user-specific recommendation models.
* Implementing hybrid recommendation techniques.
* Incorporating real-time transaction data.
* Improving recommendation ranking.
* Adding customer-level personalization.
* Integrating additional recommendation algorithms.
* Developing an interactive analytics dashboard.
* Deploying the application as an online service.
* Adding recommendation evaluation metrics.
* Integrating the system with an e-commerce platform.

## Learning Outcomes

This project provided practical experience in:

* Data preprocessing
* Transaction data analysis
* Exploratory data analysis
* Market Basket Analysis
* Association Rule Mining
* Apriori Algorithm
* Support, confidence, and lift
* Recommendation system development
* Python programming
* Flask web application development
* Converting data mining results into a usable application

## Conclusion

The Market Basket Recommendation System demonstrates how association rule mining can be used to transform customer transaction data into product recommendations.

By applying the Apriori algorithm to the Market Basket Optimisation dataset, the system identifies frequently occurring product relationships and generates association rules. These rules are then used by the recommendation engine to provide product recommendations through a Flask-based web application.

The project provides a practical implementation of Market Basket Analysis and demonstrates the connection between data mining, recommendation systems, and web application development.

## Author

**Srinivas G D**

MSc Data Science & Analytics

Areas of Interest:

* Data Analytics
* Machine Learning
* Artificial Intelligence
* Recommendation Systems

## Project Information

| Category                | Details                    |
| ----------------------- | -------------------------- |
| Domain                  | Data Science               |
| Project Type            | Recommendation System      |
| Recommendation Approach | Market Basket Analysis     |
| Algorithm               | Apriori                    |
| Technique               | Association Rule Mining    |
| Dataset                 | Market Basket Optimisation |
| Programming Language    | Python                     |
| Web Framework           | Flask                      |
| Output                  | Product Recommendations    |
