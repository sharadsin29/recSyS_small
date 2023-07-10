# New Netflix Movie Recommender System

This project is a movie recommender system, dubbed 'New Netflix', that aims to give unbiased movie recommendations based on user input. It uses Streamlit for its UI, pandas for data manipulation, and numpy for calculations.

## Project Description

New Netflix is a movie recommendation application that helps users find similar movies based on their selection. Unlike Netflix, which often promotes its original productions, New Netflix is entirely unbiased and aimed at providing the best movie suggestions.

## Installation and Running

To install and run this project, you will need to have Python installed, along with the packages listed in the dependencies section. Once these are installed, you can run the application using Streamlit.

## Dependencies

- Python 3.6 or higher
- Streamlit
- Pandas
- NumPy
- Pickle
- PIL
- streamlit_lottie
- colorsys

To install these dependencies, use pip:

```
pip install streamlit pandas numpy pillow streamlit_lottie colorsys
```

## Running the Application

To run the application, navigate to the project directory and use the command:

```
streamlit run main.py
```

## Data

The recommender system uses a correlation matrix that stores the relationship between different movies. It uses this data to suggest movies that are similar to a user's selection.

The correlation matrix and other data resources are stored in the `res` directory. Included in this directory are:

- Movie Lists (`movies_list_small.txt` and `mv_list_small.csv`): These files contain lists of all the movies used by the recommender system.
- Correlation Matrix (`corr_mat_small.npz`): This file is a numpy file that contains the correlation matrix used for recommendations.
- Movies Data (`movies.csv`): This CSV file contains information about each movie.
- Links Data (`links.csv`): This CSV file contains links to the IMDb and TMDB pages for each movie.

## How It Works

Users are presented with a dropdown menu of movies. After selecting a movie, they choose the number of recommendations they want. The recommender system then uses the correlation matrix to find movies similar to the chosen one and displays them. Each recommendation is accompanied by links to its IMDb and TMDB pages for more information.

## Author

This project was created by Sharad. If you have any questions or suggestions, feel free to reach out!

Please note that this project is meant for educational purposes and is not affiliated with Netflix in any way.

## License

This project is under the MIT license.
