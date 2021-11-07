# Analysis Part

## Data Filtering
[`data/public_high_schools_data.xlsx`] is the data reached as a result of cleaning and merging operations. Data sets of provinces, high schools and students were created by filtering this data:
-[`data/public_high_schools_data.xlsx`]
-[`data/public_high_schools_data.xlsx`]
-[`data/public_high_schools_data.xlsx`]

1. Change directory:

  ```pyfunctiontypecomment
   cd [Path]
   ```


  ```pyfunctiontypecomment
   python data_filtering.py
   ```

## Regression Analysis

1. To find correlation coefficients
2. To create OLS Model and fit
3. To find predicted values and compare with real values
4. To visualize the predicted values vs real values
5. Hypothesis testing 
6. To check Multicollinearity
7. To create Table 1 and Table 2

  ```pyfunctiontypecomment
   python regression.py
   ```


## Creating Graphs



2. To generate Figure 4:


  ```pyfunctiontypecomment
   python graph_high_school_exam_bubble.py
   ```

3. To generate Figure 5a:

 ```pyfunctiontypecomment
   python graph_high_school_efficiency_factor_bubble.py
   ```
   
4. To generate Figure 5b:

 ```pyfunctiontypecomment
   python graph_high_school_efficiency_factor_bar.py
   ```
   
4. To generate Figure 7a:

 ```pyfunctiontypecomment
   python graph_province_efficiency_factor_bubble.py
   ```
4. To generate Figure 7b:

 ```pyfunctiontypecomment
   python graph_province_efficieny_factor_map.py
   ```

- [`analysis`](https://github.com/asen16/high-schools-analysis/tree/main/analysis) : Shows how master data is filtered, analyzed and data visualized.
- [`data_scraping`](https://github.com/asen16/high-schools-analysis/tree/main/data_scraping): Explains how raw data is scraped from its source.

