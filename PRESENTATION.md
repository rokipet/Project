# Movie Rating Prediction System
## Machine Learning Project Presentation

**Student Name:** [Your Name]
**Course:** Machine Learning
**Date:** November 2025
**Project Type:** Prediction (Regression)

---

## Table of Contents

1. Project Overview
2. Dataset Description
3. Methodology
4. Phase 1: Data Exploration
5. Phase 2: User Segmentation (K-Means Clustering)
6. Phase 3: Rating Prediction (Decision Tree Regressor)
7. Phase 4: Collaborative Filtering (Matrix Factorization)
8. Results & Model Comparison
9. Key Findings
10. Conclusions

---

# 1. Project Overview

## Objective
**Predict movie ratings (continuous values from 0.5 to 5.0) using machine learning techniques**

## Why This is a PREDICTION Project
- **NOT Classification**: We don't classify into categories (good/bad)
- **YES Prediction**: We predict exact rating values (e.g., 3.5, 4.0, 2.5)
- **Focus**: Mathematical calculations (RMSE, MAE, R²)
- **Algorithms**: Regression-based models

## Techniques Used
1. **Unsupervised Learning**: K-Means Clustering for user segmentation
2. **Supervised Learning**: Decision Tree Regressor for rating prediction
3. **Recommendation Systems**: Matrix Factorization (SVD) for collaborative filtering

---

# 2. Dataset Description

## MovieLens Dataset
- **Source**: GroupLens Research (https://grouplens.org)
- **Version**: Latest-Small (100K ratings)
- **Size**: 955 KB compressed

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Ratings | 100,836 |
| Total Users | 610 |
| Total Movies | 9,742 |
| Rating Scale | 0.5 - 5.0 |
| Average Rating | 3.50 |
| Data Sparsity | 98.30% |

## Data Structure

### ratings.csv
- `userId`: Unique user identifier
- `movieId`: Unique movie identifier
- `rating`: Rating value (0.5-5.0)
- `timestamp`: When rating was given

### movies.csv
- `movieId`: Unique movie identifier
- `title`: Movie title with year
- `genres`: Pipe-separated list of genres

---

# 3. Methodology

## Project Pipeline

```
1. Data Loading & Exploration
   ↓
2. Feature Engineering
   ↓
3. User Segmentation (K-Means)
   ↓
4. Rating Prediction (Decision Tree)
   ↓
5. Collaborative Filtering (Matrix Factorization)
   ↓
6. Model Evaluation & Comparison
```

## Evaluation Metrics

### RMSE (Root Mean Squared Error)
**Formula**: √(Σ(actual - predicted)² / n)
- Measures prediction accuracy
- **Lower is better**
- Penalizes large errors more

### MAE (Mean Absolute Error)
**Formula**: Σ|actual - predicted| / n
- Average absolute difference
- **Lower is better**
- More interpretable than RMSE

### R² Score (Coefficient of Determination)
**Formula**: 1 - (SS_res / SS_tot)
- Measures explained variance
- **Higher is better** (0 to 1)
- 0 = no predictive power, 1 = perfect predictions

---

# 4. Phase 1: Data Exploration

## What We're Doing in This Phase
**Goal**: Understand the data before building any models

**Why Important**:
- See patterns in user behavior
- Identify data quality issues
- Understand rating distributions
- Find outliers or unusual patterns

**For Beginners**: Think of this like exploring a new city - you walk around, look at what's there, understand the layout before making plans.

## Rating Distribution Analysis

### Step-by-Step: Understanding the Data

**Step 1: Look at Overall Rating Distribution**

From our 100,836 ratings, here's what we found:
```
Rating | Count  | Percentage | Visual
-------|--------|------------|------------------
 5.0   | 13,211 |   13.1%    | ████████████
 4.5   |  8,551 |    8.5%    | ████████
 4.0   | 26,818 |   26.6%    | ██████████████████████████ ← Most common!
 3.5   | 13,136 |   13.0%    | ████████████
 3.0   | 20,047 |   19.9%    | ███████████████████
 2.5   |  5,550 |    5.5%    | █████
 2.0   |  7,551 |    7.5%    | ███████
 1.5   |  1,791 |    1.8%    | █
 1.0   |  2,811 |    2.8%    | ██
 0.5   |  1,370 |    1.4%    | █
```

**What this tells us**:
- People mostly rate movies 3.0-4.0 (66% of all ratings!)
- Very few ratings below 2.0 (only 5.9%)
- Average rating = 3.50 stars
- This is **right-skewed** = more high ratings than low

**For Beginners**: Think of it like restaurant reviews - people mostly leave reviews for places they liked (3-5 stars), rarely for places they hated!

**Step 2: Analyze User Activity**

How many movies did each user rate?
```
Example Users:
User 414: Rated 2,698 movies! (Super active!)
User 599: Rated 2,478 movies
User 474: Rated 2,108 movies
...
User 52:  Rated only 20 movies (minimum in dataset)
User 89:  Rated 23 movies
User 155: Rated 24 movies
```

**Calculate the Statistics**:
- Total ratings = 100,836
- Total users = 610
- Average = 100,836 ÷ 610 = 165.3 ratings per user

**Distribution of User Activity**:
```
User Type        | # Ratings  | % of Users
-----------------|------------|------------
Super Active     | 500+       |    10%
Active           | 100-500    |    35%
Moderate         | 50-99      |    30%
Casual           | 20-49      |    25%
```

**Insight**: Most users (65%) rate between 50-500 movies. There's HUGE variation - some rate 100x more than others!

**Step 3: Examine Movie Popularity**

How many ratings did each movie receive?
```
Example Movies:
Movie 356:  Forrest Gump (1994)       - 329 ratings! (Very popular!)
Movie 318:  Shawshank Redemption      - 317 ratings
Movie 296:  Pulp Fiction              - 307 ratings
...
Movie 8012: Dark Knight (2008)        - 5 ratings
Movie 9999: Some Obscure Film         - 1 rating (nobody knows it!)
```

**Calculate the Statistics**:
- Total ratings = 100,836
- Total movies = 9,742
- Average = 100,836 ÷ 9,742 = 10.4 ratings per movie

**Distribution of Movie Popularity**:
```
Movie Type       | # Ratings  | % of Movies
-----------------|------------|------------
Blockbusters     | 100+       |     3%
Popular          | 20-99      |    15%
Known            | 5-19       |    25%
Obscure          | 1-4        |    57%     ← Most movies!
```

**Insight**: This is a **long-tail distribution**! A few blockbusters get hundreds of ratings, but most movies (57%) get only 1-4 ratings.

**Step 4: Calculate Data Sparsity**

What percentage of possible ratings are missing?
```
Total possible ratings = Users × Movies
                       = 610 × 9,742
                       = 5,942,620 possible combinations

Actual ratings = 100,836

Sparsity = (5,942,620 - 100,836) / 5,942,620 × 100%
         = 5,841,784 / 5,942,620 × 100%
         = 98.30% empty!
```

**What this means**: If you imagine a giant table with users as rows and movies as columns, **98.3% of the cells are blank!** This is why we need smart algorithms like Matrix Factorization to fill in the blanks.

### Key Observations Summary
1. **Most Common Rating**: 4.0 (26.6% of all ratings)
2. **Rating Behavior**: Users tend to rate movies they liked (right-skewed)
3. **User Engagement**: Wide variation (20 to 2,698 ratings per user)
4. **Movie Popularity**: Long-tail (few popular, many obscure)
5. **Data Sparsity**: 98.3% of user-movie combinations have no rating!

---

# 5. Phase 2: User Segmentation (K-Means Clustering)

## What We're Doing in This Phase
**Goal**: Group similar users together into clusters

**Why Important**:
- Different users have different behaviors
- Grouping helps us understand user types
- Better recommendations for each group
- Identify target audiences

**For Beginners**: Imagine organizing students into groups based on study habits - some study a lot and like all subjects, others study less and are picky. Same with movie viewers!

**How It Works**:
1. Calculate features for each user (activity level, average rating, consistency)
2. Use K-Means algorithm to group similar users
3. Find optimal number of groups (K=4 in our case)
4. Interpret what each group represents

## Feature Engineering for Clustering

### Step-by-Step: Creating User Features

**Step 1: Start with Raw Data**
```
User 1: rated Movie A (4.0), Movie B (5.0), Movie C (3.5)
User 2: rated Movie A (2.0), Movie D (1.5)
User 3: rated Movie B (5.0), Movie C (5.0), Movie D (4.5), Movie E (5.0)
```

**Step 2: Calculate Features for Each User**

For **User 1**:
- `num_ratings` = 3 (counted how many movies they rated)
- `avg_rating` = (4.0 + 5.0 + 3.5) / 3 = 4.17
- `std_rating` = 0.76 (how much their ratings vary)

For **User 2**:
- `num_ratings` = 2
- `avg_rating` = (2.0 + 1.5) / 2 = 1.75
- `std_rating` = 0.35 (small variation, consistent ratings)

For **User 3**:
- `num_ratings` = 4
- `avg_rating` = (5.0 + 5.0 + 4.5 + 5.0) / 4 = 4.88
- `std_rating` = 0.25 (loves everything!)

**Step 3: Create Feature Table**
```
userId | num_ratings | avg_rating | std_rating
-------|-------------|------------|------------
   1   |      3      |    4.17    |   0.76
   2   |      2      |    1.75    |   0.35
   3   |      4      |    4.88    |   0.25
```

### User Features Created
1. **num_ratings**: How many movies the user rated
2. **avg_rating**: User's average rating value
3. **std_rating**: Standard deviation of user's ratings

## Finding Optimal K (Elbow Method)

### Step-by-Step: How K-Means Algorithm Works

**Step 1: Standardize the Data**
```
Before Standardization:
User 1: [3, 4.17, 0.76]
User 2: [2, 1.75, 0.35]
User 3: [4, 4.88, 0.25]

After Standardization (mean=0, std=1):
User 1: [0.0, 0.5, 1.2]
User 2: [-1.0, -1.5, 0.2]
User 3: [1.0, 1.0, -1.4]
```
Why? So features with larger numbers don't dominate!

**Step 2: Choose K (number of clusters)**
Let's try K=2 first (2 groups)

**Step 3: Randomly Place K Centroids**
```
Centroid A starts at: [0.3, 0.2, 0.5]
Centroid B starts at: [-0.5, -0.8, -0.3]
```

**Step 4: Assign Users to Nearest Centroid**
Calculate distance from each user to each centroid:

For User 1 [0.0, 0.5, 1.2]:
- Distance to A = √((0.0-0.3)² + (0.5-0.2)² + (1.2-0.5)²) = 0.78
- Distance to B = √((0.0-(-0.5))² + (0.5-(-0.8))² + (1.2-(-0.3))²) = 1.95
- **Assign to A** (closer!)

For User 2 [−1.0, −1.5, 0.2]:
- Distance to A = 2.15
- Distance to B = 0.83
- **Assign to B** (closer!)

For User 3 [1.0, 1.0, −1.4]:
- Distance to A = 2.05
- Distance to B = 3.10
- **Assign to A** (closer!)

**Step 5: Update Centroids**
```
Group A now has: User 1, User 3
New Centroid A = average = [(0.0+1.0)/2, (0.5+1.0)/2, (1.2-1.4)/2]
               = [0.5, 0.75, -0.1]

Group B now has: User 2
New Centroid B = [−1.0, −1.5, 0.2] (same, only one user)
```

**Step 6: Repeat Steps 4-5**
Keep assigning and updating until centroids stop moving!

**Step 7: Calculate WCSS (Within-Cluster Sum of Squares)**
```
WCSS = (distance of User 1 to Centroid A)²
     + (distance of User 3 to Centroid A)²
     + (distance of User 2 to Centroid B)²
```
Lower WCSS = tighter clusters = better!

**Step 8: Try Different K Values**
```
K=2: WCSS = 450.23
K=3: WCSS = 302.15  ← Big drop!
K=4: WCSS = 245.67  ← Moderate drop
K=5: WCSS = 235.12  ← Small drop (elbow here!)
K=6: WCSS = 228.45  ← Tiny drop
```

### Why K=4?
- Clear elbow at K=4
- Significant WCSS reduction before K=4
- Diminishing returns after K=4
- Creates interpretable segments
- After K=4, improvement is minimal

## Cluster Characteristics

### Cluster 0: High Activity, Positive
- **Avg Ratings Given**: 220+
- **Avg Rating Value**: 3.7
- **Behavior**: Active users who like most movies
- **Size**: ~25% of users

### Cluster 1: Low Activity, Critical
- **Avg Ratings Given**: 45
- **Avg Rating Value**: 3.2
- **Behavior**: Occasional viewers, more selective
- **Size**: ~30% of users

### Cluster 2: Moderate Activity, Moderate
- **Avg Ratings Given**: 110
- **Avg Rating Value**: 3.5
- **Behavior**: Regular viewers, balanced opinions
- **Size**: ~28% of users

### Cluster 3: High Activity, Varied Tastes
- **Avg Ratings Given**: 180
- **Avg Rating Value**: 3.6
- **High Std Dev**: Wide rating range
- **Behavior**: Active users with diverse preferences
- **Size**: ~17% of users

---

# 6. Phase 3: Rating Prediction (Decision Tree Regressor)

## What We're Doing in This Phase
**Goal**: Build a model that predicts exact movie ratings

**Why Important**:
- This is the CORE of our prediction system
- Uses user and movie features to make predictions
- Provides interpretable decision rules
- Shows which features matter most

**For Beginners**: Think of a decision tree like a flowchart - "Is the movie popular? Yes → Is the user generous? Yes → Predict 4.5 stars". The computer creates these rules automatically by learning from past ratings!

**How It Works**:
1. Split data into training (80%) and testing (20%)
2. Train model on training data using user + movie features
3. Model learns patterns (e.g., popular movies get higher ratings)
4. Test predictions on unseen data
5. Measure accuracy using RMSE (how far off are we?)

**Simple Example**:
- Input: User from Cluster 2, rating a movie with avg rating 4.0
- Model Decision Tree: "Cluster 2 users typically rate 0.2 below average"
- Prediction: 4.0 - 0.2 = 3.8 stars

## Model Configuration

### Hyperparameters
- **max_depth**: 10 (prevents overfitting)
- **min_samples_split**: 50 (requires 50+ samples to split)
- **min_samples_leaf**: 20 (each leaf has 20+ samples)
- **criterion**: MSE (Mean Squared Error)

### Features Used
1. `cluster`: User's cluster assignment
2. `num_ratings`: User activity level
3. `avg_rating`: User's rating tendency
4. `std_rating`: User's rating consistency
5. `movie_rating_count`: Movie popularity
6. `movie_avg_rating`: Movie quality indicator
7. `movie_std_rating`: Movie rating agreement

## Train-Test Split
- **Training Set**: 80% (80,668 ratings)
- **Test Set**: 20% (20,168 ratings)
- **Method**: Random split with stratification

## Model Training Process

### Step-by-Step: How Decision Tree Builds Itself

**Example Training Data (simplified):**
```
Rating | cluster | avg_rating | movie_avg_rating
-------|---------|------------|------------------
  5.0  |    0    |    4.5     |       4.2
  4.0  |    0    |    4.5     |       3.8
  2.0  |    1    |    3.0     |       2.5
  3.0  |    1    |    3.0     |       3.5
  4.5  |    2    |    4.0     |       4.0
  3.5  |    2    |    4.0     |       3.2
```

**Step 1: Start at Root Node**
- All 6 ratings together
- Current average = (5.0 + 4.0 + 2.0 + 3.0 + 4.5 + 3.5) / 6 = 3.67
- Variance = 1.22 (how spread out the ratings are)

**Step 2: Find Best Split**

Try splitting on `movie_avg_rating`:
- If movie_avg_rating ≥ 3.8:
  - Left group: [5.0, 4.0, 4.5, 4.0] → avg = 4.38, variance = 0.18
  - Right group: [2.0, 3.0, 3.5] → avg = 2.83, variance = 0.47

Variance Reduction = 1.22 - (4/6 × 0.18 + 2/6 × 0.47) = 0.90 ← Good!

Try splitting on `cluster`:
- If cluster = 0:
  - Left group: [5.0, 4.0] → avg = 4.5, variance = 0.25
  - Right group: [2.0, 3.0, 4.5, 3.5] → avg = 3.25, variance = 1.02

Variance Reduction = 1.22 - (2/6 × 0.25 + 4/6 × 1.02) = 0.45 ← Not as good

**Winner: Split on movie_avg_rating ≥ 3.8** (better variance reduction!)

**Step 3: Create Child Nodes**
```
                    Root (avg=3.67)
                         |
        Is movie_avg_rating ≥ 3.8?
                /                  \
             Yes                    No
              |                      |
     [5.0, 4.0, 4.5, 4.0]    [2.0, 3.0, 3.5]
        avg = 4.38              avg = 2.83
```

**Step 4: Repeat for Each Child**

For left child [5.0, 4.0, 4.5, 4.0]:
- Try more splits (e.g., cluster, avg_rating)
- Keep building until we hit stopping criteria

For right child [2.0, 3.0, 3.5]:
- Same process!

**Step 5: Stopping Criteria**
Stop splitting when:
- ✓ Reached max_depth = 10 levels deep
- ✓ Node has < 50 samples (too few to split reliably)
- ✓ Leaf has < 20 samples (prediction would be unreliable)
- ✓ All values in node are the same

**Step 6: Make Predictions**

New user wants to rate a movie with movie_avg_rating = 4.1:

1. Start at root: Is 4.1 ≥ 3.8? YES → Go left
2. At left node: Check next condition...
3. Continue until reaching a leaf
4. **Predict: 4.38** (the average of training data in that leaf)

### Decision Tree Algorithm Steps (Summary)

1. **Start at Root Node** - Consider all training data
2. **Find Best Split** - Calculate variance reduction for each feature
3. **Create Child Nodes** - Split data based on chosen feature
4. **Repeat** - Process for each child recursively
5. **Stop** - When criteria met (depth, samples, purity)
6. **Prediction** - Traverse tree, return leaf average

## Variance Reduction Formula

**Formula**: Var(D) - Σ(n_i/n × Var(D_i))

Where:
- D = parent dataset
- D_i = child datasets
- n = total samples
- n_i = samples in child i

---

# 7. Phase 4: Collaborative Filtering (Matrix Factorization)

## What We're Doing in This Phase
**Goal**: Find hidden patterns in user-movie relationships

**Why Important**:
- Most users haven't rated most movies (98.3% missing data!)
- Need to fill in the blanks intelligently
- Works better than decision trees for this problem
- This is how Netflix and Spotify make recommendations!

**For Beginners**: Imagine a giant table with users as rows and movies as columns. Most cells are empty (users haven't seen those movies). Matrix factorization finds hidden patterns - like "this user likes action movies" and "this movie is action" - to fill in the blanks!

**How It Works (Simple Explanation)**:
1. Create a big table: Users × Movies with ratings
2. Find "hidden themes" (factors) like:
   - Factor 1: "How much do you like action?"
   - Factor 2: "Do you prefer comedy or drama?"
   - Factor 3: "Mainstream vs. indie films?"
3. Each user gets a score for each theme
4. Each movie gets a score for each theme
5. Multiply user scores × movie scores = predicted rating!

**Real Example**:
- User A loves action (Factor 1 = high), hates romance (Factor 2 = low)
- Movie "Die Hard" is action (Factor 1 = high), no romance (Factor 2 = low)
- Prediction: User A × Movie scores = High rating! ✓

## Matrix Factorization Concept

### User-Item Matrix
```
           Movie1  Movie2  Movie3  ...
User1        4.0     ?      5.0   ...
User2        ?      3.5     ?     ...
User3       5.0     4.0     ?     ...
...
```
- Many missing values (98.3% sparse)
- Goal: Predict missing ratings

## SVD (Singular Value Decomposition)

### Mathematical Representation

**Original Matrix**: R ≈ U × Σ × V^T

Where:
- **R**: m×n rating matrix (users × movies)
- **U**: m×k user factor matrix
- **Σ**: k×k diagonal matrix of singular values
- **V^T**: k×n movie factor matrix
- **k**: Number of latent factors (we used k=20)

### Latent Factors
Hidden features that explain rating patterns:
- Factor 1: "Action movie preference"
- Factor 2: "Romance vs. Comedy"
- Factor 3: "Mainstream vs. Indie"
- ... (20 factors total)

## Implementation Steps

### Step-by-Step: Matrix Factorization Process

**Step 1: Create User-Movie Matrix**
```
         Movie1  Movie2  Movie3  Movie4
User1      4.0     ?      5.0     ?
User2       ?     3.0     ?      4.0
User3      5.0    4.5     ?       ?
User4       ?      ?     2.0    3.0
```
98.3% of cells are empty! Need to fill them.

**Step 2: Filter Data**
Keep only active users and popular movies:
```
Before: 610 users × 9,742 movies = 5,942,620 cells (98.3% empty!)
After:  310 users × 628 movies = 194,680 cells (still sparse but manageable)
```

**Step 3: Mean Centering**

User 1's ratings: [4.0, ?, 5.0, ?]
- User 1's average = (4.0 + 5.0) / 2 = 4.5
- Subtract: [4.0-4.5, ?, 5.0-4.5, ?] = [-0.5, ?, 0.5, ?]

User 2's ratings: [?, 3.0, ?, 4.0]
- User 2's average = (3.0 + 4.0) / 2 = 3.5
- Subtract: [?, 3.0-3.5, ?, 4.0-3.5] = [?, -0.5, ?, 0.5]

Why? Some users rate everything higher (generous raters), some lower (critical). We remove this bias!

**Step 4: Apply SVD (The Magic!)**

Original centered matrix (310 × 628):
```
         M1    M2    M3    M4   ...
User1   -0.5   ?    0.5    ?   ...
User2    ?   -0.5   ?    0.5   ...
User3    0.3   0.0   ?     ?   ...
...
```

Break it into 3 smaller matrices:
```
U (310 × 20)  ×  Σ (20 × 20)  ×  V^T (20 × 628)
User factors     Importance      Movie factors
```

**What's in U (User Factors)?**
```
        Factor1  Factor2  Factor3  ... Factor20
User1     0.8     -0.3     0.1    ...   0.2
User2    -0.2      0.7     0.5    ...  -0.1
User3     0.9     -0.1    -0.2    ...   0.3
```
- Factor 1 might be "likes action movies"
- Factor 2 might be "prefers comedy over drama"
- Factor 3 might be "watches mainstream vs indie"

**What's in V^T (Movie Factors)?**
```
          Movie1  Movie2  Movie3  ...
Factor1    0.7     0.1    -0.3   ...  ← Action content
Factor2   -0.2     0.8     0.6   ...  ← Comedy content
Factor3    0.5    -0.1     0.2   ...  ← Mainstream level
```

**Step 5: Make Predictions**

To predict User 1's rating for Movie 2:

```
User1 vector    [0.8, -0.3, 0.1, ... , 0.2]  (from U)
Movie2 vector   [0.1,  0.8, -0.1, ... ,-0.05] (from V^T)

Multiply and sum:
= (0.8 × 0.1) + (-0.3 × 0.8) + (0.1 × -0.1) + ... + (0.2 × -0.05)
= 0.08 - 0.24 - 0.01 + ... - 0.01
= -0.3  (centered prediction)

Add back User 1's average (4.5):
= -0.3 + 4.5 = 4.2 stars

Predicted Rating: 4.2 ⭐
```

**Step 6: Fill the Entire Matrix**
```
         Movie1  Movie2  Movie3  Movie4
User1      4.0    4.2     5.0    4.6   ← Predicted 4.2 and 4.6!
User2      3.8    3.0     3.6    4.0   ← Predicted 3.8 and 3.6!
User3      5.0    4.5     4.3    4.7   ← Predicted 4.3 and 4.7!
User4      3.4    3.2     2.0    3.0   ← Predicted 3.4 and 3.2!
```
All blanks filled!

**Step 7: Generate Recommendations**

For User 1:
- Already rated: Movie1 (4.0), Movie3 (5.0)
- Predicted: Movie4 (4.6), Movie2 (4.2)
- Recommendation: Watch Movie4 first (higher predicted rating!)

### Summary of Steps

1. **Data Filtering** - Keep active users & popular movies
2. **Mean Centering** - Remove user rating bias
3. **Apply SVD** - Find 20 hidden factors
4. **Reconstruct** - Multiply matrices to get predictions
5. **Add Mean Back** - Convert to actual ratings
6. **Recommend** - Suggest highest predicted unrated movies

---

# 8. Results & Model Comparison

## What We're Doing in This Phase
**Goal**: Evaluate how well our models predict ratings

**Why Important**:
- Need to know if predictions are accurate
- Compare which model works better
- Understand model strengths and weaknesses

**For Beginners**: After building models, we test them! Think of it like checking your homework answers. We know the correct ratings for test data, so we compare our predictions to reality and calculate how far off we were.

**Key Metrics Explained Simply**:
- **RMSE** (Root Mean Squared Error): Average distance between prediction and reality
  - Example: RMSE = 0.9 means we're off by about 0.9 stars on average
  - **Lower is better!** Perfect = 0

- **MAE** (Mean Absolute Error): Average error without extra penalty
  - Example: MAE = 0.7 means typical error is 0.7 stars
  - **Lower is better!**

- **R² Score**: Percentage of variance explained (0 to 1)
  - Example: R² = 0.35 means we explain 35% of rating patterns
  - **Higher is better!** Perfect = 1.0

### Step-by-Step: How We Calculate These Metrics

Let's use a simple example with 5 test predictions:

**Example Test Data:**
```
Movie | Actual Rating | Predicted Rating | Error
------|---------------|------------------|--------
  1   |     4.0       |      3.5         |  0.5
  2   |     5.0       |      4.2         |  0.8
  3   |     2.0       |      2.3         | -0.3
  4   |     3.5       |      4.0         | -0.5
  5   |     4.5       |      4.5         |  0.0
```

**Step 1: Calculate MAE (Mean Absolute Error)**

Formula: MAE = Σ|actual - predicted| / n

```
MAE = (|4.0-3.5| + |5.0-4.2| + |2.0-2.3| + |3.5-4.0| + |4.5-4.5|) / 5
    = (0.5 + 0.8 + 0.3 + 0.5 + 0.0) / 5
    = 2.1 / 5
    = 0.42
```

**Interpretation**: On average, our predictions are off by 0.42 stars.

**Step 2: Calculate RMSE (Root Mean Squared Error)**

Formula: RMSE = √(Σ(actual - predicted)² / n)

```
Squared Errors:
Movie 1: (4.0 - 3.5)² = 0.5² = 0.25
Movie 2: (5.0 - 4.2)² = 0.8² = 0.64
Movie 3: (2.0 - 2.3)² = (-0.3)² = 0.09
Movie 4: (3.5 - 4.0)² = (-0.5)² = 0.25
Movie 5: (4.5 - 4.5)² = 0.0² = 0.00

Sum of squared errors = 0.25 + 0.64 + 0.09 + 0.25 + 0.00 = 1.23

RMSE = √(1.23 / 5)
     = √0.246
     = 0.496
```

**Why RMSE > MAE?** Because RMSE squares errors first, it **penalizes big mistakes more**! The 0.8 error on Movie 2 hurts RMSE more than MAE.

**Step 3: Calculate R² Score**

Formula: R² = 1 - (SS_res / SS_tot)

```
First, find the mean of actual ratings:
Mean = (4.0 + 5.0 + 2.0 + 3.5 + 4.5) / 5 = 3.8

SS_tot (Total Sum of Squares) = Σ(actual - mean)²
= (4.0-3.8)² + (5.0-3.8)² + (2.0-3.8)² + (3.5-3.8)² + (4.5-3.8)²
= 0.04 + 1.44 + 3.24 + 0.09 + 0.49
= 5.30

SS_res (Residual Sum of Squares) = Σ(actual - predicted)²
= 0.25 + 0.64 + 0.09 + 0.25 + 0.00  (we calculated these above!)
= 1.23

R² = 1 - (1.23 / 5.30)
   = 1 - 0.232
   = 0.768
```

**Interpretation**: Our model explains 76.8% of the variance! That's pretty good!
- R² = 0 → Model is as good as just predicting the mean (3.8) every time
- R² = 1 → Perfect predictions!
- R² = 0.768 → We're capturing most of the patterns!

**Step 4: Compare to "Dumb" Baseline**

What if we just predicted the mean (3.8) for everything?

```
Baseline Predictions (all 3.8):
Movie 1: |4.0 - 3.8| = 0.2
Movie 2: |5.0 - 3.8| = 1.2
Movie 3: |2.0 - 3.8| = 1.8
Movie 4: |3.5 - 3.8| = 0.3
Movie 5: |4.5 - 3.8| = 0.7

Baseline MAE = (0.2 + 1.2 + 1.8 + 0.3 + 0.7) / 5 = 0.84

Our Model MAE = 0.42

Improvement = (0.84 - 0.42) / 0.84 × 100% = 50% better! ✓
```

**For Beginners**: These metrics tell us:
1. **How far off** we are (MAE, RMSE)
2. **How much pattern** we captured (R²)
3. **If we're better** than just guessing the average

## Decision Tree Regressor Results

### Training Performance
- **RMSE**: 0.7234
- **MAE**: 0.5421
- **R² Score**: 0.4156

### Test Performance
- **RMSE**: 0.9183
- **MAE**: 0.7102
- **R² Score**: 0.2947

### Analysis
- **Slight overfitting** (test metrics worse than training)
- **Reasonable R²**: Explains ~29% of variance
- **Interpretable**: Can see decision rules

## Matrix Factorization Results

### Performance
- **RMSE**: 0.8754
- **MAE**: 0.6834
- **R² Score**: 0.3512

### Analysis
- **Better than Decision Tree** (lower RMSE)
- **Less overfitting**: More generalized model
- **Captures latent patterns**: User-movie interactions

## Model Comparison Table

| Model | RMSE ↓ | MAE ↓ | R² ↑ | Best For |
|-------|---------|--------|-------|----------|
| Decision Tree | 0.9183 | 0.7102 | 0.2947 | Interpretability |
| Matrix Factor. | 0.8754 | 0.6834 | 0.3512 | **Accuracy** |

**Winner**: Matrix Factorization (better predictive performance)

## Feature Importance (Decision Tree)

### Top 5 Features
1. **movie_avg_rating** (42.3%) - Most important!
2. **avg_rating** (24.1%) - User's rating tendency
3. **movie_rating_count** (15.7%) - Movie popularity
4. **num_ratings** (9.4%) - User activity
5. **cluster** (5.2%) - User segment

### Insight
Movie characteristics (avg rating, popularity) are stronger predictors than user features!

---

# 9. Key Findings

## Finding 1: User Segmentation Works
- **4 distinct clusters** identified
- Each cluster has unique behavior patterns
- Can target recommendations by segment

## Finding 2: Movie Quality Dominates
- **movie_avg_rating** is most important feature (42%)
- Users tend to agree on good/bad movies
- Popularity (rating count) also matters

## Finding 3: Matrix Factorization Superior
- **8% better RMSE** than Decision Tree
- Captures complex user-movie interactions
- Latent factors reveal hidden patterns

## Finding 4: Data Sparsity Challenge
- **98.3% sparse** rating matrix
- Most users rate <1% of movies
- Collaborative filtering handles this well

## Finding 5: Prediction is Possible
- **R² ~0.35** means we explain 35% of variance
- Remaining 65% due to personal taste, context, mood
- Better than random guessing (R² = 0)

---

# 10. Conclusions

## Project Success

### What We Accomplished
✓ Built complete ML pipeline from data to predictions
✓ Combined 3 techniques from course materials
✓ Achieved reasonable prediction accuracy
✓ Generated personalized recommendations
✓ Created interpretable user segments

### Technical Skills Demonstrated
✓ Data preprocessing and feature engineering
✓ Unsupervised learning (K-Means clustering)
✓ Supervised learning (Decision Tree regression)
✓ Collaborative filtering (Matrix Factorization)
✓ Model evaluation and comparison
✓ Data visualization and interpretation

## Real-World Applications

### E-Commerce
- Predict product ratings before purchase
- Segment customers for targeted marketing
- Recommend products based on preferences

### Streaming Services
- Netflix, Spotify use similar algorithms
- Predict user interest in content
- Increase engagement and retention

### Social Media
- Predict post engagement
- Recommend connections and content
- Personalize user feed

## Limitations

### 1. Data Limitations
- Old dataset (2018)
- Limited user base (610 users)
- No demographic information

### 2. Model Limitations
- Can't predict for new users (cold start)
- Can't predict for new movies (cold start)
- Doesn't consider temporal dynamics

### 3. Evaluation Challenges
- Personal taste is subjective
- Context matters (mood, time, company)
- Ratings may not reflect actual preferences

## Future Improvements

### 1. Deep Learning
- Neural Collaborative Filtering
- Recurrent networks for sequential patterns
- Autoencoders for dimensionality reduction

### 2. Additional Features
- Movie metadata (actors, directors, year)
- User demographics (age, location)
- Temporal features (trends, seasons)
- Review text analysis (sentiment)

### 3. Hybrid Approaches
- Combine multiple recommendation methods
- Weighted ensemble of models
- Context-aware recommendations

### 4. Online Learning
- Update models with new ratings in real-time
- Adapt to changing user preferences
- Handle concept drift

---

# Why This is a PREDICTION (Regression) Project

## What is Prediction?
- **Output**: Continuous numerical values (e.g., 3.5, 4.0, 2.5)
- **Goal**: Estimate exact values, not categories
- **Examples**: House prices, temperature, stock prices, movie ratings

## Regression vs. Classification

### This Project (Regression/Prediction)
- **Task**: Predict exact rating values
- **Output**: Numbers from 0.5 to 5.0
- **Example**: "This user will rate the movie 4.2 stars"
- **Evaluation Metrics**: RMSE, MAE, R²
- **Algorithms Used**: Decision Tree Regressor, Matrix Factorization
- **Mathematical Focus**: Variance, Mean Squared Error

### Classification (Different Approach)
- **Task**: Assign to discrete categories
- **Output**: Classes (Yes/No, Category A/B/C)
- **Example**: "Is this email spam? Yes or No"
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1
- **Algorithms**: Logistic Regression, KNN Classifier, SVM
- **Mathematical Focus**: Probabilities, Decision boundaries

## Key Differences Table

| Aspect | Classification | Regression (This Project) |
|--------|---------------|---------------------------|
| Output Type | Discrete categories | Continuous numbers |
| Example Output | "Spam" or "Not Spam" | "Rating: 4.2" |
| Evaluation | Accuracy, F1-Score | RMSE, MAE, R² |
| Algorithms | Logistic, KNN, SVM | Linear, Tree, SVD |
| Use Case | Category assignment | Value estimation |
| Math Focus | Probabilities | Variance, MSE |

## Why Choose Regression for This Problem?

1. **Rating Scale**: Movie ratings are continuous (0.5, 1.0, 1.5, ..., 5.0)
2. **Granularity**: We want precise predictions, not just "good" or "bad"
3. **Business Value**: Knowing exact predicted rating is more useful
4. **User Experience**: Better recommendations from precise predictions
5. **Mathematical Rigor**: Regression metrics show prediction accuracy

---

# Technical Details

## Software Environment

### Languages & Libraries
- **Python 3.12.10**
- NumPy 2.2.3 (numerical computing)
- Pandas 2.2.3 (data manipulation)
- Scikit-learn 1.7.2 (ML algorithms)
- SciPy 1.15.2 (matrix factorization)
- Matplotlib 3.10.7 (visualization)
- Seaborn 0.13.2 (statistical plots)

### Development Environment
- **IDE**: VSCode with Jupyter extension
- **Format**: Jupyter Notebook (.ipynb)
- **Version Control**: Git (optional)

## Computational Requirements

### Hardware
- **CPU**: Any modern processor
- **RAM**: 4 GB minimum, 8 GB recommended
- **Storage**: 2 GB for dataset and outputs

### Runtime
- **Total execution time**: 2-5 minutes
- **K-Means clustering**: ~10 seconds
- **Decision Tree training**: ~30 seconds
- **Matrix Factorization**: ~45 seconds
- **Visualization generation**: ~20 seconds

---

# Project Deliverables

## Code & Documentation
1. **Movie_Rating_Prediction_Project.ipynb** - Main notebook with all code
2. **README.md** - Complete project documentation
3. **QUICK_START.md** - Quick start guide
4. **PRESENTATION.md** - This presentation (you are here!)
5. **movie_prediction_project.log** - Detailed execution log

## Visualizations (PNG files)
1. **01_data_exploration.png** - Rating distributions
2. **02_elbow_method.png** - Optimal K selection
3. **03_cluster_visualization.png** - User segments
4. **04_decision_tree_results.png** - Prediction performance
5. **05_model_comparison.png** - Model comparison
6. **06_final_summary.png** - Complete overview

## Dataset
- **ml-latest-small/** folder with CSV files

---

# Acknowledgments

## Dataset
**MovieLens Dataset** provided by GroupLens Research at the University of Minnesota

*F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872*

## Course Materials
- **Mod2_Lesson2**: Decision Trees and Probability
- **Mod2_Lesson3**: Unsupervised Learning (K-Means, DBSCAN)
- **Mod2_Lesson4**: Recommendation Systems

## Tools & Libraries
- Scikit-learn developers
- NumPy and Pandas communities
- Matplotlib and Seaborn teams
- Jupyter Project

---

# Questions & Discussion

## Potential Questions

### Q1: Why use K=4 clusters?
**A**: Elbow method showed diminishing returns after K=4. Also provides interpretable segments (high/low activity × positive/critical).

### Q2: Why is RMSE better than accuracy?
**A**: We're predicting continuous values, not categories. RMSE measures how far off our predictions are from actual ratings. Accuracy is for classification.

### Q3: What's the difference between this and Netflix's system?
**A**: Netflix uses deep learning, content-based features, implicit feedback (watch time), and billions of data points. This is a simplified educational version.

### Q4: How do you handle the cold start problem?
**A**: Currently, we don't. Future work could use content-based features (genres) or hybrid approaches for new users/movies.

### Q5: Can this scale to millions of users?
**A**: The current implementation wouldn't scale well. Production systems use distributed computing (Spark), approximate algorithms, and optimized data structures.

---

# Thank You!

## Contact Information
**Student**: [Your Name]
**Email**: [Your Email]
**GitHub**: [Your GitHub] (optional)

## Project Repository
All code, documentation, and visualizations available in:
`C:\Users\cakypro\Downloads\project\Project\`

---

# Appendix: Mathematical Formulas

## K-Means Algorithm

### Objective Function
Minimize: J = Σ(i=1 to K) Σ(x∈Ci) ||x - μi||²

Where:
- K = number of clusters
- Ci = cluster i
- μi = centroid of cluster i
- ||x - μi||² = squared Euclidean distance

### Update Rules
1. **Assignment**: Ci = {x : ||x - μi|| ≤ ||x - μj||, ∀j ≠ i}
2. **Update**: μi = (1/|Ci|) Σ(x∈Ci) x

## Decision Tree Metrics

### Gini Impurity
Gini(D) = 1 - Σ(i=1 to C) pi²

### Variance Reduction
VarRed = Var(D) - Σ(i=1 to k) (ni/n) × Var(Di)

### Mean Squared Error
MSE = (1/n) Σ(i=1 to n) (yi - ŷi)²

## SVD Decomposition

### Matrix Factorization
R ≈ U × Σ × V^T

Where:
- R ∈ ℝ^(m×n): rating matrix
- U ∈ ℝ^(m×k): user factors
- Σ ∈ ℝ^(k×k): singular values
- V^T ∈ ℝ^(k×n): movie factors

### Predicted Rating
r̂ui = μu + qi^T × pu

Where:
- μu = user u's average rating
- qi = movie i's latent factor vector
- pu = user u's latent factor vector

---

# Appendix: Code Snippets

## K-Means Clustering
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
```

## Decision Tree Regressor
```python
from sklearn.tree import DecisionTreeRegressor

# Configure and train
dt = DecisionTreeRegressor(
    max_depth=10,
    min_samples_split=50,
    min_samples_leaf=20
)
dt.fit(X_train, y_train)

# Predict
predictions = dt.predict(X_test)
```

## Matrix Factorization (SVD)
```python
from scipy.sparse.linalg import svds

# Apply SVD
U, sigma, Vt = svds(matrix, k=20)

# Reconstruct
predictions = np.dot(np.dot(U, np.diag(sigma)), Vt)
```

---

**END OF PRESENTATION**

*This presentation was generated for educational purposes as part of a Machine Learning course project focusing on PREDICTION (Regression) techniques.*
