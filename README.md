# ToneCheckerApp

This repository contains the source code for the ToneCheckerApp, a web application that allows users to analyze the sentiment of their text. It is built using **Python** and leverages the **TextBlob NLP package** for natural language processing.

---

## Features

* **Text Input:** Users can input text directly into a text area for analysis.
* **Sentiment Analysis:** Utilizes TextBlob to determine the polarity (positive, negative, neutral) and subjectivity of the input text.
* **Results Display:** Presents the sentiment analysis results (polarity and subjectivity scores) in a clear format.
* **Web Interface:** Provides a simple web interface for interacting with the analysis functionality.

---

## Technologies Used

* **Backend:**
    * **Python:** The core programming language.
* **NLP Library:**
    * **TextBlob:** A Python library for processing textual data, providing sentiment analysis capabilities.
* **Frontend (Basic):**
    * **HTML:** For structuring the web content.
    * **CSS:** For basic styling of the application.

---

## Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.x installed on your machine.
* `pip` (Python package installer).

### Installation

1.  **Clone the repo:**

    ```bash
    git clone https://github.com/smenard215/ToneCheckerApp.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd ToneCheckerApp
    ```

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    *If `requirements.txt` is not present, you might need to manually install `TextBlob`:*
    ```bash
    pip install TextBlob
    ```

4.  **Run the application:**

    ```bash
    python manage runserver
    ```

    This will typically start the development server, and the application will be accessible in your browser at `http://127.0.0.1:8000` 

---

## Usage

1.  Open the application in your web browser.
2.  Enter the text you wish to analyze into the provided text area.
3.  Click the "Check Tone" (or similar) button.
4.  View the sentiment analysis results (polarity and subjectivity) displayed on the page.

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---
