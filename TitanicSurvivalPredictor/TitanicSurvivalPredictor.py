import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import  countplot
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib.pyplot import figure,show


def TitanicLogistic():
    # Step 1: Load data.
    titanic_data = pd.read_csv('TitanicDataset.csv')

    print("First 5 entries from loaded dataset:")
    print(titanic_data.head())

    print("Number of passengers: " + str(len(titanic_data)))

    # Step 2: Analyze data
    print("Visualization: Survived and non-survived passengers")
    figure()
    target="Survived"

    sns.countplot(data=titanic_data, x="Survived").set_title(
        " Survived and non-survived passengers")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on Gender")
    sns.countplot(data=titanic_data, x="Survived", hue="Sex").set_title(
        "  Survived and non-survived passengers based on Gender")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on the Passenger class")
    sns.countplot(data=titanic_data, x="Survived", hue="Pclass").set_title(
        " Survived and non-survived passengers based on the Passenger class")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title(
        " Survived and non-survived passengers based on Age")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on the Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title(
        " Survived and non-survived passengers based on Fare")
    plt.show()

    # Step 3: Data Cleaning
    titanic_data.drop("zero", axis=1, inplace=True)
    print("First 5 entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first=True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"], drop_first=True)
    print(Pclass.head(5))

    print("Values of data set after concatenating new columns")
    titanic_data = pd.concat([titanic_data, Sex, Pclass], axis=1)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevant columns")
    titanic_data.drop(["Sex", "sibsp", "Parch", "Embarked"], axis=1, inplace=True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived", axis=1)
    y = titanic_data["Survived"]

    print("-----")

    # Step 4: Data Training
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

    logmodel = LogisticRegression()
    logmodel.fit(x_train, y_train)

    # Step 5: Data Testing
    prediction = logmodel.predict(x_test)

    # Step 6: Calculate Accuracy
    print("Classification report of Logistic Regression:")
    print(classification_report(y_test, prediction))

    print("Confusion Matrix of Logistic Regression:")
    print(confusion_matrix(y_test, prediction))

    print("Accuracy of Logistic Regression:")
    print(accuracy_score(y_test, prediction))


def main():
    print("Supervised Machine Learning")
    print("Logistic Regression on Titanic dataset")
    TitanicLogistic()


if __name__ == "__main__":
    main()
