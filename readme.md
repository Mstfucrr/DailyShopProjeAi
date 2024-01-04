## Purpose of the Project

This project creates a machine learning model to help users predict the prices of products.

## Scope of the Project

This project creates a machine learning model to help users predict the prices of products.
and uses a machine learning model to help users predict the prices of products.

## Technologies Used:
- Python
- Flask
- Pandas
- Numpy
- Scikit-learn
- preprocessing (LabelEncoder, StandardScaler)
- LinearRegression

## Project Setup

You can follow the steps below to use the project:

1. Clone this project to your computer:

    ```bash
    git clone https://github.com/Mstfucrr/DailyShopProjeAi
    ```

2. Run the `getQuoteApi.py` file:

    ```bash
    python getQuoteApi.py
    ```

    This step starts the basic API service of the project.

3. Send a "POST" request to the API. Request body example:

    ```json
    {
        "data": {
            "category": 1,
            "status": "new"
        }
    }
    ```

    You can use tools such as [curl](https://curl.se/) or [Postman](https://www.postman.com/) as a tool for sending requests.

4. You should get a sample answer:

    ```json
    {
        "data": {
            "max": 250.0,
            "min": 150.0
        },
        "message": "Products price suggestion has been successfully fetched.",
        "status": 200
    }
    ```

    This answer contains the price range for the specified category and status.

## Notes

- Python and the necessary dependencies must be installed to run the project.
- The API service will run at `http://localhost:5000` by default.
- For further configuration of the project files and the API you can refer to the relevant documentation.
  
This simple user manual describes the basic use of the project. For more details and customisations it is recommended to refer to the project documentation.