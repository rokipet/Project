# Movie Rating Prediction System with User Segmentation

## Project Overview

This is a comprehensive Machine Learning project that focuses on **PREDICTION** (continuous values) rather than classification. The project combines multiple ML techniques learned in class:

1. **Unsupervised Learning**: K-Means Clustering for user segmentation
2. **Supervised Learning**: Decision Tree Regressor for rating prediction
3. **Recommendation Systems**: Matrix Factorization (SVD) for collaborative filtering

## Dataset

- **Name**: MovieLens (latest-small)
- **Source**: https://grouplens.org/datasets/movielens/
- **Size**: 100,000+ ratings from 600+ users on 9,000+ movies
- **Rating Scale**: 0.5 to 5.0 (continuous values)
- **Files**:
  - `ratings.csv` - User ratings for movies
  - `movies.csv` - Movie titles and genres

## Project Structure

```
project/
├── Movie_Rating_Prediction_Project.ipynb  # Main notebook with all code
├── README.md                              # This file
├── ml-latest-small/                       # Dataset folder
│   ├── ratings.csv
│   ├── movies.csv
│   ├── links.csv
│   └── tags.csv
└── Output Files (generated when you run):
    ├── movie_prediction_project.log       # Detailed execution log
    ├── 01_data_exploration.png
    ├── 02_elbow_method.png
    ├── 03_cluster_visualization.png
    ├── 04_decision_tree_results.png
    ├── 05_model_comparison.png
    └── 06_final_summary.png
```

## How to Run

### Requirements

Install required packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter
```

### Running the Project

1. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `Movie_Rating_Prediction_Project.ipynb`

3. Run all cells (Cell → Run All) or run them one by one

4. Check the generated visualizations and log file

## What This Project Does

### Phase 1: Data Loading & Exploration
- Loads MovieLens dataset
- Analyzes rating distributions
- Calculates dataset statistics
- **Logging**: Records all data characteristics

### Phase 2: Feature Engineering
- Creates user features (number of ratings, average rating, rating variance)
- Creates movie features (popularity, average rating)
- **Logging**: Tracks feature creation process

### Phase 3: User Segmentation (K-Means Clustering)
- Segments users into 4 distinct behavioral groups
- Uses Elbow Method to find optimal K
- Interprets clusters (e.g., "High Activity, Positive, Consistent")
- **Logging**: Records clustering metrics and cluster characteristics

### Phase 4: Decision Tree Regressor (PREDICTION)
- Predicts movie ratings (continuous values 0.5-5.0)
- Uses user and movie features
- Evaluates with RMSE, MAE, R² metrics
- Shows feature importance
- **Logging**: Logs all training metrics and predictions

### Phase 5: Matrix Factorization (Collaborative Filtering)
- Applies SVD (Singular Value Decomposition)
- Predicts ratings for user-movie pairs
- Generates personalized recommendations
- **Logging**: Records factorization process and results

### Phase 6: Recommendations & Analysis
- Generates top-10 movie recommendations per user
- Analyzes top movies for each cluster
- Compares model performance
- **Logging**: Documents all recommendations

## Key Results

### Models Compared:

| Model | Purpose | Evaluation Metrics |
|-------|---------|-------------------|
| K-Means Clustering | User Segmentation | WCSS, Silhouette |
| Decision Tree Regressor | Rating Prediction | RMSE, MAE, R² |
| Matrix Factorization (SVD) | Collaborative Filtering | RMSE, MAE, R² |

### Expected Performance:
- **Decision Tree RMSE**: ~0.8-1.0 (lower is better)
- **Matrix Factorization RMSE**: ~0.7-0.9 (lower is better)
- **R² Score**: 0.3-0.5 (higher is better)

## Why This is a PREDICTION Project (Not Classification)

Your professor wants **calculations and prediction**, not classification. This project:

✅ **PREDICTS continuous values** (ratings from 0.5 to 5.0)
✅ **Uses regression algorithms** (Decision Tree Regressor, not Classifier)
✅ **Shows mathematical calculations** (RMSE, MAE, variance reduction)
✅ **Matrix Factorization** involves heavy calculations (SVD decomposition)

❌ Does NOT do classification (no "spam/not spam", "yes/no", "category A/B/C")

## Logging Features

Every code cell includes comprehensive logging:

- **INFO level**: Successful operations, metrics, results
- **WARNING level**: Potential issues, fallbacks
- **ERROR level**: Failures, exceptions

All logs are saved to: `movie_prediction_project.log`

Example log entries:
```
2025-01-06 19:30:15 - INFO - ==========================================
2025-01-06 19:30:15 - INFO - MOVIE RATING PREDICTION PROJECT STARTED
2025-01-06 19:30:16 - INFO - Ratings dataset loaded: 100836 rows, 4 columns
2025-01-06 19:30:20 - INFO - K=4: WCSS=1234.56
2025-01-06 19:30:25 - INFO - Decision Tree training complete
2025-01-06 19:30:25 - INFO - Test RMSE: 0.8542
```

## Visualizations Generated

1. **Data Exploration**: Rating distributions, user activity
2. **Elbow Method**: Finding optimal number of clusters
3. **Cluster Visualization**: User segments in 2D space
4. **Decision Tree Results**: Predictions, residuals, feature importance
5. **Model Comparison**: RMSE, MAE, R² comparison
6. **Final Summary**: Complete project overview

## Concepts Demonstrated

### From Your Course Materials:

- ✅ **Mod2_Lesson2**: Decision Trees (Regression variant)
- ✅ **Mod2_Lesson3**: K-Means Clustering, DBSCAN concepts
- ✅ **Mod2_Lesson4**: Recommendation Systems, Matrix Factorization

### Additional ML Concepts:

- Feature Engineering
- Train-Test Split
- Model Evaluation Metrics
- Data Visualization
- Comprehensive Logging

## Differences from Your Friend's Project

Your friend (Benjamin) is doing:
- **Logistic Regression** (classification: yes/no, 0/1)
- **KNN Classifier** (classification: categories)

You are doing:
- **Decision Tree Regressor** (prediction: continuous values)
- **Matrix Factorization** (prediction: rating values)
- **K-Means Clustering** (unsupervised: user segmentation)

**This makes your project COMPLETELY DIFFERENT and focused on PREDICTION!**

## How to Present This Project

1. **Introduction**: Explain the goal (predict movie ratings)
2. **Data**: Show MovieLens dataset characteristics
3. **Clustering**: Explain user segmentation results
4. **Prediction Models**:
   - Show Decision Tree results and calculations
   - Show Matrix Factorization mathematics
5. **Evaluation**: Compare models using RMSE, MAE, R²
6. **Recommendations**: Show personalized recommendations
7. **Conclusion**: Summarize which model performs better

## Notes for Your Professor

- This project focuses on **PREDICTION with calculations**
- All code includes **comprehensive logging**
- Uses **regression algorithms**, not classification
- Demonstrates understanding of:
  - Probability and statistics (from Mod2_Lesson2)
  - Unsupervised learning (from Mod2_Lesson3)
  - Recommendation systems (from Mod2_Lesson4)
- **Unique approach**: Combines clustering + regression + recommendations

## Troubleshooting

If you encounter issues:

1. **Import errors**: Install missing packages
   ```bash
   pip install [package-name]
   ```

2. **Memory issues**: The code already uses a subset of data for efficiency

3. **SVD convergence**: Already configured with optimal parameters

4. **Logging issues**: Check if you have write permissions in the directory

## Credits

- **Dataset**: MovieLens by GroupLens Research
- **Techniques**: Based on course materials (Mod2_Lesson2, Mod2_Lesson3, Mod2_Lesson4)
- **Implementation**: Custom code with comprehensive logging

## License

This is an educational project for class purposes.

---

**Good luck with your presentation!** 🎬📊

If you have questions, check the log file `movie_prediction_project.log` for detailed execution information.
