# Variable Definitions and Transformations

## Dependent Variables
TIMSS Science Score: mean eighth-grade science achievement score.
TIMSS Mathematics Score: mean eighth-grade mathematics achievement score.

## Independent Variables

Science:
- Class Size
- Students Like Learning Science
- Students Value Science
- Students Confident in Science

Mathematics:
- Students Value Mathematics
- Students Like Learning Mathematics
- Students Confident in Mathematics
- Class Size

## 1999 Categorical Coding

Three-category variables:
- Low = 1
- Medium = 2
- High = 3

Four-category like learning variables:
- I don't like it at all = 1
- I don't like it = 2
- I like it = 3
- I like it very much = 4

## Weighted Average Calculation

WA = sum(p_i * w_i)

where WA is the weighted average score, p_i is the valid response percentage or proportion in category i, and w_i is the numerical weight assigned to category i.

## Approximate SCL-Equivalent Transformation

Three-category variables:
SCL-equivalent = 4 + ((WA - 1) / (3 - 1)) * (16 - 4)

Four-category like learning variables:
SCL-equivalent = 4 + ((WA - 1) / (4 - 1)) * (16 - 4)

These transformed values are approximate SCL-equivalent values and should not be interpreted as official TIMSS SCL scores.

## Linear Interpolation for 2003

X_2003 = (X_1999 + X_2007) / 2

The 2003 values were estimated between harmonized 1999 values and retrospectively harmonized 2007 values.

## Evaluation Metrics
- MAE
- MSE
- RMSE
- DTW
