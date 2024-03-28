# CrimiCheck: Criminal Record Lookup System

CrimiCheck is a simple Streamlit web application that allows users to check for criminal records in a database. Users can input the name, city, age, and gender of an individual, and the system will search the database for any matching records. If a record is found, it displays details such as the crime committed, sentence length, and arrest date.

## Features

- **User-Friendly Interface**: The application provides a simple and intuitive interface for users to input search parameters.

- **Case-Insensitive Search**: Searches are case-insensitive, allowing users to input names and cities in any case (upper, lower, or mixed).

- **Database Integration**: CrimiCheck reads data from an Excel or CSV file containing criminal records, allowing for easy integration with existing databases.

## Usage

1. Enter the name, city, age, and gender of the individual you want to search for.

2. Click the "Search" button.

3. If a criminal record matching the provided details is found, the details including the crime committed, sentence length, and arrest date will be displayed.

4. If no matching record is found, a message indicating the absence of criminal records will be displayed.

## Data Format

The application expects the criminal records to be provided in either Excel (.xlsx) or CSV (.csv) format. The data should include the following columns:

- Name: The name of the individual.
- Crime: The type of crime committed.
- City: The city where the crime took place.
- Age: The age of the individual at the time of the crime.
- Gender: The gender of the individual.
- Sentence Length: The length of the sentence imposed.
- Arrest Date: The date of the arrest.

Ensure that the data is correctly formatted and does not contain any missing or erroneous values.

## Contributors

- [Your Name](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
